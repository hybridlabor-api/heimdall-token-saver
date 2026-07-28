"""BDB memB Vector Memory MCP processor."""

import json
import re
from ..base import Processor


class BdbMembProcessor(Processor):
    priority = 17
    hook_patterns = [
        r"^(memb_mcp|memb-skill|memb_)",
    ]

    @property
    def name(self) -> str:
        return "bdb_memb"

    def can_handle(self, command: str) -> bool:
        cmd_lower = command.lower()
        return any(cmd_lower.startswith(p) for p in ("memb_mcp", "memb-skill", "memb_")) or "memb" in cmd_lower

    def process(self, command: str, output: str) -> str:
        if not output or not output.strip():
            return output

        try:
            data = json.loads(output)
            if isinstance(data, (dict, list)):
                return self._compress_memb_json(data)
        except Exception:
            pass

        lines = output.splitlines()
        filtered = []
        for line in lines:
            line = re.sub(r"\[(?:\s*-?\d+\.\d+,\s*){3,}-?\d+\.\d+\s*\]", "[...embedding array truncated...]", line)
            filtered.append(line)

        return "\n".join(filtered)

    def _compress_memb_json(self, data) -> str:
        def _clean_obj(obj):
            if isinstance(obj, dict):
                cleaned = {}
                for k, v in obj.items():
                    if k in ("embedding", "embeddings", "vector", "distance_matrix") and isinstance(v, list):
                        cleaned[k] = f"[{len(v)} float embeddings truncated]"
                    else:
                        cleaned[k] = _clean_obj(v)
                return cleaned
            elif isinstance(obj, list):
                return [_clean_obj(item) for item in obj]
            return obj

        cleaned_data = _clean_obj(data)
        return json.dumps(cleaned_data, indent=2)
