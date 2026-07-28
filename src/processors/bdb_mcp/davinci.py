"""BDB DaVinci Resolve MCP processor."""

import json
from ..base import Processor


class BdbDavinciProcessor(Processor):
    priority = 14
    hook_patterns = [
        r"^(bdb_davinci_|resolve_mcp|davinci_)",
    ]

    @property
    def name(self) -> str:
        return "bdb_davinci"

    def can_handle(self, command: str) -> bool:
        cmd_lower = command.lower()
        return any(cmd_lower.startswith(p) for p in ("bdb_davinci_", "resolve_mcp", "davinci_")) or "davinci" in cmd_lower or "resolve" in cmd_lower

    def process(self, command: str, output: str) -> str:
        if not output or not output.strip():
            return output

        try:
            data = json.loads(output)
            if isinstance(data, dict):
                return self._compress_davinci_dict(data)
        except Exception:
            pass

        lines = output.splitlines()
        filtered = [l for l in lines if any(k in l.lower() for k in ("offline", "fail", "render", "marker", "clip", "timeline", "error"))]
        if len(filtered) < len(lines):
            filtered.insert(0, f"[Heimdall BDB-DaVinci] Compressed {len(lines)} lines -> {len(filtered)} lines:")
        return "\n".join(filtered)

    def _compress_davinci_dict(self, data: dict) -> str:
        cleaned = {}
        for k, v in data.items():
            if k in ("offline_media", "render_errors", "cut_markers", "active_clip_ids", "timeline_name"):
                cleaned[k] = v
            elif k == "clips" and isinstance(v, list):
                cleaned["clips"] = [
                    {ck: cv for ck, cv in c.items() if ck in ("id", "name", "duration", "is_offline")}
                    if isinstance(c, dict) else c
                    for c in v
                ]
            elif v not in (None, [], {}, ""):
                cleaned[k] = v
        return json.dumps(cleaned, indent=2)
