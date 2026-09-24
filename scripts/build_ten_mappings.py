#!/usr/bin/env python3
"""Render auditable mapping records from frozen native Jev results.

M annotations below are editorial judgments based on each research dossier.
This script never changes the model's native scores.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "qa/jev-ten-batch/raw"
TASTES = {"sour": "酸", "bitter": "苦", "sweet": "甘", "pungent": "辛", "salty": "咸"}
ORGANS = {"heart": "心", "liver": "肝", "spleen": "脾", "lung": "肺", "kidney": "肾"}
QI = ["寒", "凉", "平", "温", "热"]
DIRECTIONS = ["阴-", "阴+", "阳-", "阳+"]

# These notes are intentionally separate from the Jev API response.
NOTES = {
    "pistachio": {
        "qi": ("传统直录；现代形态类推 M-IV", "《本草拾遗》经《本草纲目》转引有温；《饮膳正要》未定寒温，且研究未测证候。"),
        "taste": {"sweet": ("传统直录；现代类推 M-IV", "《饮膳正要》记甘。"), "pungent": ("传统直录；现代类推 M-IV", "《本草拾遗》转引记辛，另记涩。")},
        "meridian": {"spleen": ("M-0", "传统有调中、去冷气及诸痢记录，但没有可核实的明确脾经原文；现代代谢指标不能证明归经。")},
        "allowed": "可以并列呈现古籍辛温涩与甘的不同记载；脾阳+仅作为 Jev 的分类倾向，不写成确定功效。",
    },
    "dark-chocolate": {"taste": {"bitter": ("M-IV", "高可可产品有苦味，商品糖和黄烷醇差异大。")}, "allowed": "短期情绪信号可谨慎陈述；不写安神、治抑郁或归经。"},
    "pearl-milk-tea": {"taste": {"sweet": ("M-IV", "典型配方的直接感官甜味与实测糖量支持类推，但配方可减糖。")}, "allowed": "写糖、份量、咖啡因和定制变量；不写生湿、性寒或确定归经。"},
    "yogurt": {"taste": {"sour": ("M-IV", "发酵酸味及传统酪的近似记载，食品身份不完全相同。"), "sweet": ("M-IV", "牛乳母本与原味酸奶口感类比。")}, "allowed": "只写活菌产品对乳糖消化不良者的限定作用；健脾最多是类比，不作本条定论。"},
    "instant-noodles": {"taste": {"salty": ("M-IV", "汤料的感官咸味与钠含量随品牌和使用量变化。")}, "allowed": "写钠和食用方式；不写固定燥热、湿热或伤脾胃。"},
    "paper-filtered-coffee": {"taste": {"bitter": ("M-IV", "纸滤黑咖啡的感官苦味，烘焙与萃取影响强度。")}, "allowed": "可写短时警觉和纸滤与未过滤的血脂差别；醒神仅作近现代用语，不指定归经。"},
    "oat-milk": {"taste": {"sweet": ("M-IV", "燕麦饮的感官轻甜依配方改变。")}, "allowed": "仅写特定高纤维配方的短期试验，不推成普通商售品通用降脂功效。"},
    "kombucha": {"taste": {"sour": ("M-IV", "发酵酸味可能存在，残糖和发酵程度变化大。")}, "allowed": "小试验是线索，不写治疗糖尿病或稳定改善菌群。"},
    "sugar-free-cola": {"taste": {"sour": ("M-IV", "酸味剂与口感类比。"), "sweet": ("M-IV", "非糖甜味剂带来感官甜味，不等于传统甘味功效。")}, "allowed": "写替换含糖饮料可减少该次糖暴露，不写长期减重功效。"},
    "whey-protein-powder": {"allowed": "限定抗阻训练与基线摄入；不得把乳食传统作用移给分离粉。"},
}


def render(path: Path) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    slug = data["entry_id"]
    a = data["runs"][0]["native_answers"]
    note = NOTES[slug]
    lines = [f"# Mapping｜{slug}", "", "> 分类为 Jev v0.4 原生输出；M 是其后根据 research.md 独立评注。分数不是校准概率或证据等级。", "",
             "## Run metadata", "", "```yaml", f"entry_id: {slug}", f"research_ref: references/entries/{slug}/research.md",
             f"summary_ref: {data['summary_ref']}", f"summary_sha256: {data['summary_sha256']}",
             f"reasoning_version: {data['reasoning_version']}", f"five_shot_version: {data['five_shot_version']}",
             f"requested_model: {data['requested_model']}", f"actual_model: {data['runs'][0]['actual_model']}",
             f"repeat_count: {len(data['runs'])}", f"run_timestamp_utc: {data['run_timestamp_utc']}",
             f"native_result_ref: qa/jev-ten-batch/raw/{slug}.json", "```", "", "## 四气", "",
             "| 候选 | 原生 probability | M |", "|---|---:|---|" ]
    qi_m, qi_note = note.get("qi", ("M-0", "资料未支持把模型强制选出的平当作已证实的本草平性。"))
    for q in QI:
        lines.append(f"| {q} | {a['qi']['probabilities'][q]:.2f} | {qi_m if q == a['qi']['choice'] else 'M-0'} |")
    lines += ["", f"Jev Choice：**{a['qi']['choice']}**。{qi_note}", "", "## 五味", "",
              "| 候选 | 原生 Noul | M | 注释 |", "|---|---:|---|---|"]
    for key, label in TASTES.items():
        m, reason = note.get("taste", {}).get(key, ("M-0", "没有足够可追溯的本草映射依据。"))
        lines.append(f"| {label} | {a['taste_'+key]['noul']:.2f} | {m} | {reason} |")
    lines += ["", "## 五脏归经与各经主方向", "",
              "| 经 | Noul | Choice | 阴- | 阴+ | 阳- | 阳+ | M |", "|---|---:|---|---:|---:|---:|---:|---|"]
    for key, label in ORGANS.items():
        d = a[key+"_direction"]
        m, _ = note.get("meridian", {}).get(key, ("M-0", "无直接证候与传统归经证据。"))
        probs = " | ".join(f"{d['probabilities'][x]:.2f}" for x in DIRECTIONS)
        lines.append(f"| {label} | {a['meridian_'+key]['noul']:.2f} | {d['choice']} | {probs} | {m} |")
    lines += ["", "各经方向的原生分布均已保存；低归经分数的方向不进入读者层。0.5 只作展示线，不是 M 或证据门槛。", "",
              "## M 注释与写作交接", ""]
    for key, (m, reason) in note.get("meridian", {}).items():
        lines.append(f"- {ORGANS[key]}及{a[key+'_direction']['choice']}：Jev Noul {a['meridian_'+key]['noul']:.2f}；{m}。{reason}")
    lines += [f"- 四气：{qi_note}",
              "- 反证与替代解释：产品配方、加工、剂量、人群、对照与传统母本身份的差异，详见 research.md 和 summary.md。模型方向或感官相似不能补上临床证候证据。",
              f"- 正文最大表述强度：{note['allowed']}",
              "- 派生传统用词：本批次不自动接受；需同时具备归经、方向和语境，并符合 M 强度。", ""]
    target = ROOT / "references/entries" / slug / "mapping.md"
    target.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    paths = sorted(RAW.glob("*.json"))
    if len(paths) != 10:
        raise ValueError("Expected ten native result files")
    for path in paths:
        render(path)


if __name__ == "__main__":
    main()
