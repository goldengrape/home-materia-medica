#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CUTOFF = "2026-09-24"

def load_data(batch_id):
    path = ROOT / "scripts" / "entry_batches" / f"{batch_id}.json"
    cfg = json.loads(path.read_text(encoding="utf-8"))
    entries = cfg["entries"]
    if len(entries) != 10:
        raise ValueError(f"Expected 10 entries, found {len(entries)}")
    return cfg["batch"], entries

def evidence_cards(p):
    cards = []
    for n, e in enumerate(p.get("evidence_records", []), 1):
        cards.append(
            f"""### Evidence card {n} — source {e['ref']}

- **Design:** {e['design']}
- **Population:** {e['population']}
- **Exposure:** {e['exposure']}
- **Result:** {e['result']}
- **Limits:** {e['limits']}
- **Distance:** {e['distance']}
- **Reference:** {p['refs'][e['ref'] - 1]}
"""
        )
    return "\n".join(cards)

def dossier(entry_id, p):
    parent = p["shared_parent"]
    queries = "\n".join(f"- {q}" for q in p["queries"])
    logs = "\n".join(f"- {x}" for x in p["search_log"])
    refs = "\n".join(f"{n}. {x}" for n, x in enumerate(p["refs"], 1))
    tradition = p.get(
        "tradition",
        "本条是现代加工食品或复合食品。本轮未发现足以支持其特定配方与古籍条目一一对应的直接材料；传统食疗记录不转写为现代产品的药性或疗效。"
    )
    return f"""# Research Dossier — {p['name']}

> entry_id: {entry_id}
> entry_type: {p.get('entry_type', 'beverage')}
> research_depth: {p['research_depth']}
> status: research_ready_{p['research_depth']}
> evidence_cutoff: {CUTOFF}
> shared_parent: {parent}

## 1. 身份与边界

**本条定义：** {p['identity']}

**主要变量：** {p['variables']}

品牌、地区、加工、容量及配方会改变实际暴露；本底稿只讨论该目录类别的合理边界。邻近饮料或单一原料的研究不会自动视作本成品证据。

## 2. 核心问题与检索记录

**核心问题：** 产品身份与组成、直接人体结局、共享证据的可迁移距离，以及主要安全边界。

**定向检索词：**

{queries}

**本轮检索记录：**

{logs}

本条按照 {p['research_depth']} 深度作定向探索；按目录和研究类型核对 PubMed/PMC、期刊页面、官方机构资料及产品/营养信息。未检得只表示本轮检索范围，不声明全球不存在研究。体外、市场成分调查、风险评估与人体试验分开记录。

## 3. 共享证据与直接性

共享背景：references/shared/{parent}/research.md。

共享母页只提供类别背景；具体产品需再按直接性分层：D0 为同一明确成品，D1 为近似配方/制法，D2 为共享基底或相邻饮品，D3 为单一成分或机制，D4 为推测性外推。证据级别另按项目凡例执行，不以 D 距离替代研究质量。

## 4. 传统来源层级

{tradition}

## 5. 组成与暴露

{p['composition']}

决定实际暴露的项目：{p['variables']}

## 6. 本条证据卡

### 命题 A｜成品人体结局

{p['direct']}

### 命题 B｜产品、加工或成分

{p['specific']}

{evidence_cards(p)}

样品、产地、品牌、剂量、研究时间、比较组和终点不得超出原研究外推；体外或标签分析不升级为人群效应。若原文报告利益冲突或产品/菌株特异性，按限制项保留。

## 7. 安全与实用选择

{p['safety']}

以上为类别层面的阅读提示，不替代个体医疗建议；不把分类名、营销词或单一研究结果当成疗效承诺。

## 8. 本草映射候选

本阶段不预写 Jev 分类、四气五味归经或 M 等级。味觉描述只用于食品感官，不能推成传统药性或临床效果。

## 9. 未知与停止规则

仍未知：{p.get('unknowns', '品牌/地区配方分布、不同暴露剂量的结果，以及长期且本条特异的临床结局。')}

**停止规则：** 当前达到 {p['research_depth']} 定向检索范围；若出现新的同配方人体研究、代表性市场调查或重要安全资料，再按新证据重开。替代解释包括份量、配料、替代关系、饮食背景、研究人群、终点和随访时长。

## 10. 核心参考资料

{refs}
"""

def summary(entry_id, p):
    parent = p["shared_parent"]
    return f"""# Summary Document — {p['name']}

**身份。** {p['identity']}

**组成与暴露。** {p['composition']} **关键变量：** {p['variables']}

**直接人体证据。** {p['direct']}

**产品/成分证据。** {p['specific']}

**共享背景。** 参见 {parent}；共享结论不自动等于本成品结论。

**安全。** {p['safety']}

**传统来源。** {p.get('tradition', '现代加工食品资料不等于古籍对具体商品的专门分类。')}

本摘要只复述 Research Dossier 的可追溯事实，不预设 Jev 分类或 M 等级。未检得仅表示本轮 {p['research_depth']} 检索范围。
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch-id", required=True)
    args = ap.parse_args()
    batch, data = load_data(args.batch_id)
    out = ROOT / "references" / "entries"
    qa_dir = ROOT / "qa" / "entry-batches"
    qa_dir.mkdir(parents=True, exist_ok=True)

    ordered = list(data.items())
    for entry_id, p in ordered:
        d = out / entry_id
        d.mkdir(parents=True, exist_ok=True)
        (d / "research.md").write_text(dossier(entry_id, p), encoding="utf-8")
        (d / "summary.md").write_text(summary(entry_id, p), encoding="utf-8")

    # Keep a batch-local copy of each stage-1/2 output for artifacts and audit.
    stage_root = ROOT / "qa" / "jev-entry-batches" / args.batch_id / "stage"
    (stage_root / "research").mkdir(parents=True, exist_ok=True)
    (stage_root / "summary").mkdir(parents=True, exist_ok=True)
    for entry_id, _ in ordered:
        (stage_root / "research" / f"{entry_id}.md").write_bytes(
            (out / entry_id / "research.md").read_bytes()
        )
        (stage_root / "summary" / f"{entry_id}.md").write_bytes(
            (out / entry_id / "summary.md").read_bytes()
        )

    lines = [
        f"# QA Log — {batch['title']}（第 {batch['catalog_order']} 批）",
        "",
        f"> 日期：{CUTOFF}",
        f"> 研究深度：逐条按 R1/R2 配置定向检索，不是系统综述。",
        f"> 证据截止：{batch['research_cutoff']}。",
        f"> 检索记录：Exa {batch['exa_search_calls']} 次检索、{batch['exa_hits']} 条结果；另对可用原始研究、期刊页面及官方来源作题名、DOI、样本、剂量和结局核验。",
        "",
        "## 本批目录顺序",
        "",
    ]
    for n, (entry_id, p) in enumerate(ordered, 1):
        lines.append(f"{n}. {entry_id}（{p['name']}；{p['research_depth']}）")
    lines += ["", "## 搜与整的中间产物", ""]
    for entry_id, p in ordered:
        lines.append(f"### {entry_id}｜{p['name']}")
        lines.append("")
        lines.append("检索词：" + "；".join(p["queries"]))
        lines.append("")
        for item in p["search_log"]:
            lines.append(f"- {item}")
        lines.append("")
        lines.append(f"- 研究底稿：references/entries/{entry_id}/research.md")
        lines.append(f"- 整理摘要：references/entries/{entry_id}/summary.md")
        lines.append("")
    lines += [
        "## 后续步骤与保留路径",
        "",
        "- 判：先冻结摘要文本及 SHA-256，再读取 GitHub Environment API_KEYS 中的 JEV_API_KEY 发起 Jev v0.4 请求；原生 answers 不添加 M、不改写分数。",
        "- 写：逐条生成 Mapping 和读者正文；正文参考文献保留英文原题与已核验 DOI。",
        f"- 本批配置：scripts/entry_batches/{args.batch_id}.json。",
        f"- 冻结清单：qa/entry-batches/{args.batch_id}-summary-sha256.txt。",
        f"- 冻结快照：qa/jev-entry-batches/{args.batch_id}/pre-freeze/。",
        f"- 原生结果：qa/jev-entry-batches/{args.batch_id}/raw/；原始文件另存为 GitHub Actions artifact。",
        "",
        "## 身份红队",
        "",
    ]
    for note in batch.get("identity_red_team", []):
        lines.append(f"- {note}")
    if not batch.get("identity_red_team"):
        lines.append("- 按本批每个条目的身份、加工形态和相邻品类逐项核查，避免将共享原料或相似食品证据视为成品直接证据。")
    lines += [
        "",
        "## Actions 运行记录",
        "",
        "待补录 workflow run、artifact、模型版本、原始 JSON 哈希与 QA 结果。",
        "",
    ]
    (qa_dir / f"{args.batch_id}.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Built stage-1/2 dossiers and summaries for {len(ordered)} entries.")

if __name__ == "__main__":
    main()
