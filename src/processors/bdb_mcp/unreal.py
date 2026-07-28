"""BDB Unreal Engine MCP processor."""

import json
import re
from ..base import Processor


class BdbUnrealProcessor(Processor):
    priority = 12
    hook_patterns = [
        r"^(bdb_unreal_|mcp_unreal_|unreal_)",
    ]

    @property
    def name(self) -> str:
        return "bdb_unreal"

    def can_handle(self, command: str) -> bool:
        cmd_lower = command.lower()
        return any(cmd_lower.startswith(p) for p in ("bdb_unreal_", "mcp_unreal_", "unreal_")) or "unreal" in cmd_lower

    def process(self, command: str, output: str) -> str:
        if not output or not output.strip():
            return output

        try:
            data = json.loads(output)
            if isinstance(data, dict):
                return self._compress_unreal_dict(data)
        except Exception:
            pass

        lines = output.splitlines()
        filtered = []
        for line in lines:
            if any(k in line for k in ("LogUnrealEngine", "Error:", "Warning:", "Blueprint", "PCG", "Transform", "Failed")):
                filtered.append(line)
            elif not re.search(r"AssetRegistry|ClassIcon|Ticker|LogTemp:\s*Verbose", line):
                filtered.append(line)

        if len(filtered) < len(lines):
            filtered.insert(0, f"[Heimdall BDB-Unreal] Compressed {len(lines)} lines -> {len(filtered)} lines:")
        return "\n".join(filtered)

    def _compress_unreal_dict(self, data: dict) -> str:
        cleaned = {}
        for k, v in data.items():
            if k in ("errors", "warnings", "actor_name", "transform", "pcg_status", "blueprint_errors"):
                cleaned[k] = v
            elif k == "asset_registry":
                cleaned["asset_registry"] = f"[{len(v)} assets]" if isinstance(v, list) else "filtered assets"
            elif v not in (None, [], {}, ""):
                cleaned[k] = v
        return json.dumps(cleaned, indent=2)
