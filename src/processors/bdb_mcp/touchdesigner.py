"""BDB TouchDesigner MCP processor."""

import json
import re
from ..base import Processor


class BdbTouchdesignerProcessor(Processor):
    priority = 11
    hook_patterns = [
        r"^(bdb_td_|mcp_td_|touchdesigner_|tdmcp_)",
    ]

    @property
    def name(self) -> str:
        return "bdb_touchdesigner"

    def can_handle(self, command: str) -> bool:
        cmd_lower = command.lower()
        return any(cmd_lower.startswith(p) for p in ("bdb_td_", "mcp_td_", "touchdesigner_", "tdmcp_")) or "touchdesigner" in cmd_lower or "td_node" in cmd_lower

    def process(self, command: str, output: str) -> str:
        if not output or not output.strip():
            return output

        try:
            data = json.loads(output)
            if isinstance(data, dict):
                return self._compress_td_dict(data)
            elif isinstance(data, list):
                return json.dumps([self._compress_td_dict(item) if isinstance(item, dict) else item for item in data], indent=2)
        except Exception:
            pass

        lines = output.splitlines()
        filtered = []
        for line in lines:
            if any(k in line.lower() for k in ("error", "fail", "warning", "exception", "modified", "path", "op:")):
                filtered.append(line)
            elif not re.search(r"frame\s+\d+|cook\s+time|fps:\s*\d+", line, re.I):
                filtered.append(line)

        if len(filtered) < len(lines):
            filtered.insert(0, f"[Heimdall BDB-TD] Compressed {len(lines)} lines -> {len(filtered)} lines:")
        return "\n".join(filtered)

    def _compress_td_dict(self, data: dict) -> str:
        cleaned = {}
        for k, v in data.items():
            if k in ("errors", "warnings", "path", "name", "type", "modified_parameters", "script_errors"):
                cleaned[k] = v
            elif k == "parameters" and isinstance(v, dict):
                cleaned["parameters"] = {pk: pv for pk, pv in v.items() if isinstance(pv, dict) and pv.get("is_default") is False or pk in ("file", "text", "expr", "value")}
            elif k == "nodes" and isinstance(v, (dict, list)):
                cleaned["nodes"] = f"[{len(v)} nodes summary]"
            elif v not in (None, [], {}, ""):
                cleaned[k] = v
        return json.dumps(cleaned, indent=2)
