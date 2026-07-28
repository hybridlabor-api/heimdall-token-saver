"""BDB After Effects MCP processor."""

import json
import re
from ..base import Processor


class BdbAfterEffectsProcessor(Processor):
    priority = 13
    hook_patterns = [
        r"^(bdb_after_effects_|ae-mcp|mcp_aftereffects_)",
    ]

    @property
    def name(self) -> str:
        return "bdb_aftereffects"

    def can_handle(self, command: str) -> bool:
        cmd_lower = command.lower()
        return any(cmd_lower.startswith(p) for p in ("bdb_after_effects_", "ae-mcp", "mcp_aftereffects_")) or "aftereffects" in cmd_lower or "after_effects" in cmd_lower

    def process(self, command: str, output: str) -> str:
        if not output or not output.strip():
            return output

        try:
            data = json.loads(output)
            if isinstance(data, dict):
                return self._compress_ae_dict(data)
        except Exception:
            pass

        lines = output.splitlines()
        filtered = []
        for line in lines:
            if any(k in line.lower() for k in ("extendscript", "error", "line", "layer", "keyframe", "exception")):
                filtered.append(line)
            elif not re.search(r"rendering\s+\d+%", line, re.I):
                filtered.append(line)

        if len(filtered) < len(lines):
            filtered.insert(0, f"[Heimdall BDB-AE] Compressed {len(lines)} lines -> {len(filtered)} lines:")
        return "\n".join(filtered)

    def _compress_ae_dict(self, data: dict) -> str:
        cleaned = {}
        for k, v in data.items():
            if k in ("errors", "extendscript_error", "layer_index", "layer_name", "keyframe_deltas", "composition"):
                cleaned[k] = v
            elif k == "layers" and isinstance(v, list):
                cleaned["layers"] = [
                    {lk: lv for lk, lv in layer.items() if lk in ("index", "name", "hasVideo", "error")}
                    if isinstance(layer, dict) else layer
                    for layer in v
                ]
            elif v not in (None, [], {}, ""):
                cleaned[k] = v
        return json.dumps(cleaned, indent=2)
