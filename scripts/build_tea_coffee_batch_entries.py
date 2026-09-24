#!/usr/bin/env python3
"""Write reader-facing entries from frozen stage-2 summaries and post-Jev mappings."""
from __future__ import annotations

import json
from pathlib import Path

from build_tea_coffee_batch_stage12 import PROFILES

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "qa/jev-tea-coffee-batch/raw"


def reader_layer(entry_id: str, profile: dict) -> str:
    data = json.loads((RAW / f"{entry_id}.json").read_text(encoding="utf-8"))
    answers = data["runs"][0]["native_answers"]
    tastes = {"sour": "酸", "bitter": "苦", "sweet": "甘", "pungent": "辛", "salty": "咸"}
    organs = {"heart": "心", "liver": "肝", "spleen": "脾", "lung": "肺", "kidney": "肾"}
    top_tastes = sorted(
        ((tastes[k.removeprefix("taste_")], v["noul"]) for k, v in answers.items() if k.startswith("taste_")),
        key=lambda x: -x[1],
    )
    highest = max((answers[f"meridian_{key}"]["noul"], label) for key, label in organs.items())

    mapping = (ROOT / "references/entries" / entry_id / "mapping.md").read_text(encoding="utf-8").splitlines()
    section = ""
    qi_m = "M-0"
    taste_m: dict[str, str] = {}
    for line in mapping:
        if line == "## 四气":
            section = "qi"
        elif line == "## 五味":
            section = "taste"
        elif line.startswith("## 五脏"):
            section = ""
        elif section and line.startswith("|") and not line.startswith("|---"):
            cells = [x.strip() for x in line.split("|")]
            if section == "qi" and len(cells) >= 4 and cells[1] in {"寒", "凉", "平", "温", "热"}:
                if cells[1] == answers["qi"]["choice"]:
                    qi_m = cells[3]
            elif section == "taste" and len(cells) >= 5 and cells[1] in set(tastes.values()):
                taste_m[cells[1]] = cells[3]

    qi = answers["qi"]
    top_text = "、".join(f"{label} {score:.2f}" for label, score in top_tastes[:2])
    mapped = [f"{label} M-IV" for label, grade in taste_m.items() if grade == "M-IV"]
    mapped_text = "、".join(mapped) if mapped else "各味 M-0"
    return (
        f"Jev v0.4 的四气 Choice 为**{qi['choice']}**（原生倾向分数 {qi['probabilities'][qi['choice']]:.2f}；"
        f"Choice confidence {qi['confidence']:.2f}），该项 M：{qi_m}。五味原生分数相对靠前的是{top_text}；"
        f"具感官依据的项目只作 M-IV 类推（{mapped_text}）。最高归经 Noul 为{highest[1]} {highest[0]:.2f}，"
        "低于项目读者层展示线；所有方向 Choice 和概率保留在 mapping.md 与原始 JSON，五脏归经及方向 M-0。"
        "这些模型分数不是现实世界概率，也不能由高分推成临床效应。"
    )


def main() -> None:
    for entry_id, profile in PROFILES.items():
        mapping = ROOT / "references/entries" / entry_id / "mapping.md"
        if not mapping.exists():
            raise FileNotFoundError(f"Build Mapping first: {entry_id}")
        tradition = (
            "茶叶母页只作传统历史背景，不能自动决定现代浸泡/复合制品的属性。"
            if entry_id in {"cold-brew-tea", "sparkling-tea"}
            else "咖啡共享母页的近现代资料不等于本条所有制品的直接传统分类。"
        )
        body = f"""# {profile['name']}

{profile['body']}

{profile['evidence_body']}

**安全与选择。** {profile['care']}

**本草按。** {reader_layer(entry_id)} {tradition}

研究底稿：[research.md](../references/entries/{entry_id}/research.md) · 冻结摘要：[summary.md](../references/entries/{entry_id}/summary.md) · Jev 与 M 记录：[mapping.md](../references/entries/{entry_id}/mapping.md)。

**参考文献**

"""
        body += "\n".join(f"{i}. {ref}" for i, ref in enumerate(profile["body_refs"], 1)) + "\n"
        (ROOT / "entries" / f"{entry_id}.md").write_text(body, encoding="utf-8")
    print(f"Wrote {len(PROFILES)} reader-facing entries from frozen evidence and mappings.")


if __name__ == "__main__":
    main()
