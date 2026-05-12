#!/usr/bin/env python3
"""Initialize a local long-novel project structure."""

from __future__ import annotations

import argparse
from pathlib import Path

FILES = {
    "00_meta/premise.md": "# 核心卖点\n\n一句话：\n",
    "00_meta/style_guide.md": "# 文风指南\n\n- 叙事人称：\n- 句式偏好：\n- 禁用表达：\n",
    "00_meta/world_rules.md": "# 世界规则\n\n## 不可违背规则\n- \n",
    "01_outline/master_outline.md": "# 总纲\n\n## 卷列表\n1. \n",
    "02_characters/cast.md": "# 角色卡\n\n## 主角\n- 目标：\n- 秘密：\n- 恐惧：\n- 反转点：\n",
    "02_characters/relationships.md": "# 人物关系\n",
    "02_characters/arcs.md": "# 人物弧线\n",
    "04_memory/timeline.md": "# 时间线\n",
    "04_memory/facts.md": "# 事实库\n",
    "04_memory/unresolved_threads.md": "# 未回收伏笔\n",
    "05_revision/continuity_issues.md": "# 一致性问题清单\n",
    "05_revision/line_edit_log.md": "# 行文修订记录\n",
}

FOLDERS = [
    "03_drafts/vol01",
]


def write_if_missing(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="初始化百万字小说工程")
    parser.add_argument("--path", required=True, help="输出目录，例如 ./novel-project")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    root.mkdir(parents=True, exist_ok=True)

    for folder in FOLDERS:
        (root / folder).mkdir(parents=True, exist_ok=True)

    for rel, content in FILES.items():
        write_if_missing(root / rel, content)

    print(f"已初始化小说工程：{root}")


if __name__ == "__main__":
    main()
