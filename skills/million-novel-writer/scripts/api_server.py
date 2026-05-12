#!/usr/bin/env python3
"""API server for local usage and WeChat Cloud Hosting."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel, Field

from init_novel_project import FILES, FOLDERS, write_if_missing

app = FastAPI(title="Million Novel Writer API", version="1.0.0")


class InitProjectRequest(BaseModel):
    path: str = Field(..., description="项目目录路径，例如 /data/novel-project")


class ChapterCardRequest(BaseModel):
    volume_goal: str
    prev_ending: str
    chapter_goal: str
    conflict: str
    new_facts: str


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/init_project")
def init_project(req: InitProjectRequest) -> dict[str, Any]:
    root = Path(req.path).resolve()
    root.mkdir(parents=True, exist_ok=True)

    for folder in FOLDERS:
        (root / folder).mkdir(parents=True, exist_ok=True)

    for rel, content in FILES.items():
        write_if_missing(root / rel, content)

    return {"ok": True, "path": str(root)}


@app.post("/chapter_card")
def chapter_card(req: ChapterCardRequest) -> dict[str, Any]:
    # 这里先返回结构化草案，后续可接入任意模型服务。
    points = [
        f"推进卷目标：{req.volume_goal}",
        f"承接上章结尾：{req.prev_ending}",
        f"核心冲突升级：{req.conflict}",
    ]
    return {
        "ok": True,
        "chapter_card": {
            "goal": req.chapter_goal,
            "plot_points": points,
            "new_facts": req.new_facts,
            "hook_candidates": ["角色做出高风险选择", "出现反常信息打断计划"],
        },
    }
