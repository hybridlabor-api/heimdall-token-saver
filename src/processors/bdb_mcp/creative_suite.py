"""BDB Creative Suite (Blender, Resolume, Rhino, Adobe UXP, Vectorworks) MCP processor."""

import json
import re
from ..base import Processor


class BdbCreativeSuiteProcessor(Processor):
    priority = 16
    hook_patterns = [
        r"^(bdb_blender_|blender_|blender-mcp|bdb_resolume_|bdb_rhino_|rhino_|adobe_uxp_|vectorworks_)",
    ]

    @property
    def name(self) -> str:
        return "bdb_creative_suite"

    def can_handle(self, command: str) -> bool:
        cmd_lower = command.lower()
        return any(cmd_lower.startswith(p) for p in ("bdb_blender_", "blender_", "blender-mcp", "bdb_resolume_", "bdb_rhino_", "rhino_", "adobe_uxp_", "vectorworks_")) or any(k in cmd_lower for k in ("blender", "resolume", "rhino", "adobe_uxp", "vectorworks"))

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
        filtered = []
        for l in lines:
            # Compress large vertex arrays or matrix transforms
            l_sub = re.sub(r"\[(?:\s*-?\d+\.\d+,\s*){5,}-?\d+\.\d+\s*\]", "[...mesh vertex/matrix data truncated...]", l)
            if not any(k in l_sub.lower() for k in ("matrix_transform", "zeroed", "schema_definition", "openapi")):
                filtered.append(l_sub)

        if len(filtered) < len(lines):
            filtered.insert(0, f"[Heimdall BDB-CreativeSuite] Compressed {len(lines)} lines -> {len(filtered)} lines:")
        return "\n".join(filtered)

    def _compress_cs_dict(self, data: dict) -> str:
        cleaned = {}
        for k, v in data.items():
            if k in ("matrix_transform", "zero_matrix", "full_schema"):
                continue
            elif k in ("vertices", "mesh_data", "polygons") and isinstance(v, list):
                cleaned[k] = f"[{len(v)} mesh elements truncated]"
            else:
                cleaned[k] = v
        return json.dumps(cleaned, indent=2)
