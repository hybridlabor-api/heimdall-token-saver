"""BDB Creative Suite (Resolume, Rhino, Adobe UXP, Vectorworks) MCP processor."""

import json
from ..base import Processor


class BdbCreativeSuiteProcessor(Processor):
    priority = 16
    hook_patterns = [
        r"^(bdb_resolume_|bdb_rhino_|rhino_|adobe_uxp_|vectorworks_)",
    ]

    @property
    def name(self) -> str:
        return "bdb_creative_suite"

    def can_handle(self, command: str) -> bool:
        cmd_lower = command.lower()
        return any(cmd_lower.startswith(p) for p in ("bdb_resolume_", "bdb_rhino_", "rhino_", "adobe_uxp_", "vectorworks_")) or any(k in cmd_lower for k in ("resolume", "rhino", "adobe_uxp", "vectorworks"))

    def process(self, command: str, output: str) -> str:
        if not output or not output.strip():
            return output

        try:
            data = json.loads(output)
            if isinstance(data, dict):
                return self._compress_cs_dict(data)
        except Exception:
            pass

        lines = output.splitlines()
        filtered = [l for l in lines if not any(k in l.lower() for k in ("matrix_transform", "zeroed", "schema_definition", "openapi"))]
        if len(filtered) < len(lines):
            filtered.insert(0, f"[Heimdall BDB-CreativeSuite] Compressed {len(lines)} lines -> {len(filtered)} lines:")
        return "\n".join(filtered)

    def _compress_cs_dict(self, data: dict) -> str:
        cleaned = {}
        for k, v in data.items():
            if k in ("matrix_transform", "zero_matrix", "full_schema"):
                continue
            cleaned[k] = v
        return json.dumps(cleaned, indent=2)
