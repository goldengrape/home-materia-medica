#!/usr/bin/env python3
"""Create stage-3 mapping records from frozen native Jev responses.

Native JSON files remain byte-for-byte unchanged. M annotations below are
post-Jev editorial judgments based on each entry's Research Dossier.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "qa/jev-tea-batch/raw"
MANIFEST = ROOT / "qa/tea-drink-summary-sha256.txt"
TASTES = {
    "sour": "酸",
    "bitter": "苦",
    "sweet": "甘",
    "pungent": "辛",
    "salty": "咸",
}
ORGANS = {
    "heart": "心",
    "liver": "肝",
    "spleen": "脾",
    "lung": "肺",
    "kidney": "肾",
}
QI = ["寒", "凉", "平", "温", "热"]
DIRECTIONS = ["阴-", "阴+", "阳-", "阳+"]
WORKFLOW_RUN_ID = 35973926000
ARTIFACT_ID = 10797147988

# Sensory grades are M-IV analogies only. No M grade is inferred from a Jev score.
NOTES = {
    "fresh-milk-tea": {
        "taste": {
            "bitter": ("M-IV", "茶底可有苦涩；只是感官类推，不证明整杯具有传统苦味功效。"),
            "sweet": ("M-IV", "牛乳和可选糖可带来甜感；鲜奶比例与加糖因店而异。"),
        },
        "allowed": "限于茶底、鲜奶/奶精身份、糖和咖啡因暴露；不定整杯四气或归经。",
    },
    "milk-foam-tea": {
        "taste": {
            "bitter": ("M-IV", "茶底可有苦涩，奶盖会改变口感；配方差异大。"),
            "sweet": ("M-IV", "奶盖/糖浆可能带来甜感；不等于固定甘味功效。"),
            "salty": ("M-IV", "部分奶盖有咸感；不是所有奶盖配方均含盐。"),
        },
        "allowed": "只报告合并奶盖组的市场营养范围；不把芝士茶、奶盖茶或单杯门店配方互相代替。",
    },
    "fruit-tea": {
        "taste": {
            "bitter": ("M-IV", "茶底苦涩可能存在，取决于茶类与浓度。"),
            "sweet": ("M-IV", "水果、果汁或糖浆可带来甜感；总糖因配方而变。"),
            "sour": ("M-IV", "部分水果/果汁有酸感；不是全品类固定特征。"),
        },
        "allowed": "清楚限定被测百香果红茶与芒果绿茶的样本数据；不写整类疾病效果。",
    },
    "cheese-tea": {
        "taste": {
            "bitter": ("M-IV", "茶底可有苦涩，感官类推不等于临床功效。"),
            "sweet": ("M-IV", "奶盖或茶底可能加糖，含量依配方。"),
            "salty": ("M-IV", "部分芝士/咸奶盖可有咸感；配方并不统一。"),
        },
        "allowed": "动物实验只作 E-D 信号；不推成人体血糖或糖尿病因果结论。",
    },
    "coconut-milk-tea": {
        "taste": {
            "bitter": ("M-IV", "茶底的苦涩感随茶和浓度变化。"),
            "sweet": ("M-IV", "部分椰乳饮料或糖浆有甜感；名称不足以确定配方。"),
        },
        "allowed": "先核对椰乳、椰味饮料与椰果的实际身份；不补造营养均值或归经。",
    },
    "oat-milk-tea": {
        "taste": {
            "bitter": ("M-IV", "茶底可有苦涩，取决于冲泡浓度。"),
            "sweet": ("M-IV", "部分燕麦饮有轻甜感；是否加糖及品牌配方均会改变口感。"),
        },
        "allowed": "两篇体外模型不构成人体健康证据；不推成血糖、血脂或饱腹功效。",
    },
    "brown-sugar-milk-tea": {
        "taste": {
            "bitter": ("M-IV", "茶底可有苦涩，随配方浓度而变。"),
            "sweet": ("M-IV", "黑糖/糖浆带来甜感，但品名不能量化整杯糖暴露。"),
        },
        "allowed": "写实际糖、杯量与基底变量；不写黑糖的未经验证健康优势。",
    },
    "matcha-latte": {
        "taste": {
            "bitter": ("M-IV", "抹茶粉可带来苦味；粉量、品质、奶与糖改变整杯体验。"),
            "sweet": ("M-IV", "牛乳或糖浆可带来甜感；不代表所有抹茶拿铁均同甜度。"),
        },
        "allowed": "试验信号限于小样本、特定粉末配方与替代终点；不写成已证实减压或认知功效。",
    },
    "hojicha-latte": {
        "taste": {
            "bitter": ("M-IV", "焙茶底可有苦涩与焙火风味；粉末/浸液和浓度不同。"),
            "sweet": ("M-IV", "牛乳和可选糖浆可带甜感；配方不固定。"),
        },
        "allowed": "抹茶拿铁试验中的焙茶拿铁是对照饮品；对照组不证明焙茶疗效。",
    },
    "bottled-unsweetened-tea": {
        "qi": ("M-IV", "《本草纲目》茶条“茶苦而寒”仅作茶母本类推；现代瓶装茶的茶种、提取和产品配方有差异。"),
        "taste": {
            "bitter": ("M-IV", "无糖茶可呈苦涩，受茶种与浓度影响；不等于全类固定体验。"),
        },
        "allowed": "只谈具体标签、实际配方与直接对瓶饮用后的实验室筛查；不把无糖等同于无咖啡因。",
    },
}


def read_manifest() -> dict[str, tuple[str, str]]:
    result = {}
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        digest, relative = line.split("  ", 1)
        entry_id = Path(relative).parent.name
        result[entry_id] = (digest, relative)
    if len(result) != 10:
        raise ValueError(f"Expected ten frozen summaries, got {len(result)}")
    return result


def render(entry_id: str, digest: str, summary_ref: str) -> None:
    raw_path = RAW / f"{entry_id}.json"
    data = json.loads(raw_path.read_text(encoding="utf-8"))
    if data["entry_id"] != entry_id or data["summary_sha256"] != digest:
        raise ValueError(f"Entry/hash mismatch: {entry_id}")
    if hashlib.sha256((ROOT / summary_ref).read_bytes()).hexdigest() != digest:
        raise ValueError(f"Summary changed after Jev run: {entry_id}")
    if len(data["runs"]) != 1:
        raise ValueError(f"Expected one run: {entry_id}")
    answers = data["runs"][0]["native_answers"]
    note = NOTES[entry_id]
    qi_choice = answers["qi"]["choice"]
    qi_grade, qi_reason = note.get("qi", ("M-0", "茶叶母本或相似饮品不能自动确定复合成品的四气。"))

    lines = [
        f"# Mapping｜{entry_id}",
        "",
        "> Jev v0.4 是模型分类倾向；M 是随后根据 Research Dossier 所做的独立证据评注。分数不是校准概率，M 也不修正分数。",
        "",
        "## Run metadata",
        "",
        "```yaml",
        f"entry_id: {entry_id}",
        f"research_ref: references/entries/{entry_id}/research.md",
        f"summary_ref: {summary_ref}",
        f"summary_sha256: {digest}",
        f"reasoning_version: {data['reasoning_version']}",
        f"five_shot_version: {data['five_shot_version']}",
        f"requested_model: {data['requested_model']}",
        f"actual_model: {data['runs'][0]['actual_model']}",
        f"repeat_count: {len(data['runs'])}",
        f"run_timestamp_utc: {data['run_timestamp_utc']}",
        f"workflow_run_id: {WORKFLOW_RUN_ID}",
        f"workflow_artifact_id: {ARTIFACT_ID}",
        f"native_result_ref: qa/jev-tea-batch/raw/{entry_id}.json",
        "```",
        "",
        "## 四气",
        "",
        "| 候选 | 原生 probability | M |",
        "|---|---:|---|",
    ]
    for qi in QI:
        lines.append(f"| {qi} | {answers['qi']['probabilities'][qi]:.2f} | {qi_grade if qi == qi_choice else 'M-0'} |")
    lines += [
        "",
        f"Jev Choice：**{qi_choice}**（Choice confidence {answers['qi']['confidence']:.2f}）。{qi_reason}",
        "",
        "## 五味",
        "",
        "| 候选 | 原生 Noul | M | 注释 |",
        "|---|---:|---|---|",
    ]
    for key, label in TASTES.items():
        grade, reason = note.get("taste", {}).get(key, ("M-0", "没有足够可追溯的本草映射依据。"))
        lines.append(f"| {label} | {answers['taste_'+key]['noul']:.2f} | {grade} | {reason} |")

    lines += [
        "",
        "## 五脏归经与各经主方向",
        "",
        "| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |",
        "|---|---:|---|---:|---:|---:|---:|---:|---|",
    ]
    max_noul = max(answers["meridian_" + key]["noul"] for key in ORGANS)
    for key, label in ORGANS.items():
        direction = answers[key + "_direction"]
        probabilities = " | ".join(f"{direction['probabilities'][x]:.2f}" for x in DIRECTIONS)
        lines.append(
            f"| {label} | {answers['meridian_'+key]['noul']:.2f} | {direction['choice']} | "
            f"{direction['confidence']:.2f} | {probabilities} | M-0 |"
        )
    lines += [
        "",
        f"最高归经 Noul 为 {max_noul:.2f}；所有原生归经和方向结果均保留。五脏方向 Choice 是 Jev 对各经的原生回答，不代表已确认归经；本条无直接证候或传统归经桥梁，因此 M-0。项目的 0.5 只作为读者层展示线，不作为隐藏 Jev 原始输出或提升 M 的门槛。",
        "",
        "## M 注释与写作交接",
        "",
        f"- 四气：{qi_reason}",
        "- 五味：M-IV 仅在有明确配方/感官描述时表示感官类推，不表示传统功效；其他味 M-0。",
        "- 归经与方向：全部 M-0；模型倾向分数和方向分布保留，但不把低分强制 Choice 转成正文归经。",
        "- 反证与替代解释：配方、加工、糖/乳/植物饮、茶种、粉量、人群与研究终点差异见 research.md、summary.md。",
        f"- 正文最大表述强度：{note['allowed']}",
        "- 原生 JSON 未添加 M、未改写分数；全部 API 原始字段与 usage 见 native_result_ref。",
        "",
    ]
    out = ROOT / "references/entries" / entry_id / "mapping.md"
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    manifest = read_manifest()
    raw_files = {p.stem for p in RAW.glob("*.json")}
    if raw_files != set(manifest):
        raise ValueError(f"Raw file set differs from manifest: {raw_files ^ set(manifest)}")
    for entry_id, (digest, summary_ref) in manifest.items():
        render(entry_id, digest, summary_ref)
    print(f"Rendered {len(manifest)} post-Jev Mapping Records; raw JSON unchanged.")


if __name__ == "__main__":
    main()
