import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

"""Unit tests for BDB MCP Processors."""

import json
from src.processors.bdb_mcp.touchdesigner import BdbTouchdesignerProcessor
from src.processors.bdb_mcp.unreal import BdbUnrealProcessor
from src.processors.bdb_mcp.aftereffects import BdbAfterEffectsProcessor
from src.processors.bdb_mcp.davinci import BdbDavinciProcessor
from src.processors.bdb_mcp.creative_suite import BdbCreativeSuiteProcessor
from src.processors.bdb_mcp.memb import BdbMembProcessor


class TestBdbTouchdesignerProcessor:
    def setup_method(self):
        self.proc = BdbTouchdesignerProcessor()

    def test_can_handle(self):
        assert self.proc.can_handle("bdb_td_get_nodes")
        assert self.proc.can_handle("mcp_td_cook")
        assert self.proc.can_handle("touchdesigner_pipeline")

    def test_compress_json(self):
        sample = {
            "path": "/project1/base1",
            "errors": ["Cook error in DAT script line 12"],
            "nodes": [{"name": f"node{i}"} for i in range(50)],
            "parameters": {
                "file": {"value": "shader.glsl", "is_default": False},
                "unused": {"value": "0", "is_default": True}
            }
        }
        res = self.proc.process("bdb_td_get_nodes", json.dumps(sample))
        data = json.loads(res)
        assert data["path"] == "/project1/base1"
        assert "Cook error" in data["errors"][0]
        assert "file" in data["parameters"]
        assert "unused" not in data["parameters"]


class TestBdbUnrealProcessor:
    def setup_method(self):
        self.proc = BdbUnrealProcessor()

    def test_can_handle(self):
        assert self.proc.can_handle("bdb_unreal_spawn_actor")
        assert self.proc.can_handle("mcp_unreal_pcg_build")

    def test_compress_json(self):
        sample = {
            "actor_name": "BP_Player",
            "errors": ["Blueprint compilation failed"],
            "asset_registry": [{"name": f"asset{i}"} for i in range(100)]
        }
        res = self.proc.process("bdb_unreal_spawn_actor", json.dumps(sample))
        data = json.loads(res)
        assert data["actor_name"] == "BP_Player"
        assert "Blueprint compilation failed" in data["errors"][0]
        assert "assets" in data["asset_registry"]


class TestBdbAfterEffectsProcessor:
    def setup_method(self):
        self.proc = BdbAfterEffectsProcessor()

    def test_can_handle(self):
        assert self.proc.can_handle("bdb_after_effects_render")
        assert self.proc.can_handle("ae-mcp_keyframe")

    def test_compress_json(self):
        sample = {
            "extendscript_error": "SyntaxError at line 45",
            "layers": [
                {"index": 1, "name": "TextLayer", "unused": "xyz"},
                {"index": 2, "name": "Null", "unused": "abc"}
            ]
        }
        res = self.proc.process("bdb_after_effects_render", json.dumps(sample))
        data = json.loads(res)
        assert data["extendscript_error"] == "SyntaxError at line 45"
        assert data["layers"][0]["name"] == "TextLayer"
        assert "unused" not in data["layers"][0]


class TestBdbDavinciProcessor:
    def setup_method(self):
        self.proc = BdbDavinciProcessor()

    def test_can_handle(self):
        assert self.proc.can_handle("bdb_davinci_timeline")
        assert self.proc.can_handle("resolve_mcp_render")

    def test_compress_json(self):
        sample = {
            "offline_media": ["/Volumes/Media/clip01.mov"],
            "timeline_name": "MainCut"
        }
        res = self.proc.process("bdb_davinci_timeline", json.dumps(sample))
        data = json.loads(res)
        assert data["timeline_name"] == "MainCut"
        assert "/Volumes/Media/clip01.mov" in data["offline_media"]


class TestBdbCreativeSuiteProcessor:
    def setup_method(self):
        self.proc = BdbCreativeSuiteProcessor()

    def test_can_handle(self):
        assert self.proc.can_handle("bdb_blender_render")
        assert self.proc.can_handle("blender-mcp_mesh")
        assert self.proc.can_handle("bdb_resolume_clip")
        assert self.proc.can_handle("bdb_rhino_mesh")

    def test_compress_json(self):
        sample = {
            "clip_id": 42,
            "matrix_transform": [[1,0,0],[0,1,0],[0,0,1]]
        }
        res = self.proc.process("bdb_resolume_clip", json.dumps(sample))
        data = json.loads(res)
        assert data["clip_id"] == 42
        assert "matrix_transform" not in data


class TestBdbMembProcessor:
    def setup_method(self):
        self.proc = BdbMembProcessor()

    def test_can_handle(self):
        assert self.proc.can_handle("memb_mcp_query")
        assert self.proc.can_handle("memb-skill_remember")

    def test_compress_vector_json(self):
        sample = {
            "memory_id": "mem_12345",
            "text": "User prefers dark mode and React App Router",
            "embedding": [0.123, -0.456, 0.789, 0.012, -0.999, 0.555, 0.333]
        }
        res = self.proc.process("memb_mcp_query", json.dumps(sample))
        data = json.loads(res)
        assert data["memory_id"] == "mem_12345"
        assert data["text"] == "User prefers dark mode and React App Router"
        assert "truncated" in data["embedding"]
