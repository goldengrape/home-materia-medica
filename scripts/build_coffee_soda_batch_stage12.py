#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/"scripts/coffee_soda_profiles.json").read_text(encoding="utf-8"))
IDS=list(DATA)
def dossier(i,p):
 family="coffee-base" if p["family"]=="coffee" else "soft-drink-base"
 parent="咖啡共享母页只提供通用咖啡、咖啡因和冲煮背景；复合配方与脱因加工需重新评直接性。" if p["family"]=="coffee" else "碳酸与软饮母页区分加糖软饮、酸性配方与无糖碳酸水；产品不能相互转移营养值或人体效应。"
 tradition="咖啡共享传统资料来自近现代文献，不是现代加奶、加糖或脱因制品的古籍专属记录。" if p["family"]=="coffee" else "本条为现代加工饮料；传统饮水资料不等于对当前工业配方的专门记载。"
 q="；".join(p["queries"]); refs="\n".join(f"{n}. {x}" for n,x in enumerate(p["refs"],1))
 return f"""# Research Dossier — {p['name']}

> entry_id: {i}
> entry_type: catalog beverage
> research_depth: R1
> status: research_ready_R1
> evidence_cutoff: 2026-09-24
> shared_parent: {family}

## 1. 身份与边界

本条定义：{p['identity']}

主要变量：{p['variables']}

品牌、国家、配方和杯型存在差异；目录相邻条目依明确配料与制法区分。

## 2. 核心问题与检索

核心问题：本条组成、直接人体结局、共享证据可迁移距离及安全边界。
定向检索词：{q}。
本轮为 R1 定向探索，核对出版社、PubMed/PMC、大学机构库或官方商品页。未检得仅指本次范围，不声明全球不存在相关研究。成分检测、实验室材料研究与人体试验分开评价。

## 3. 共享证据与直接性

共享证据节点：references/shared/{family}/research.md。{parent}

本条研究须按成品匹配度重新分级：D0 同一明确成品；D1 近似配方/制法；D2 共享基底或相邻饮品；D3 单一成分或机制。

## 4. 传统来源层级

{tradition}

## 5. 组成与暴露

{p['composition']}
影响实际暴露的关键项：{p['variables']}

## 6. 本条直接证据卡

### 命题 A｜本条特异的人体效果

{p['direct']}

直接性：未检得本条固定配方临床证据时，母页/相邻食品按 D1–D3 降级。对本条长期因果效果不写作已建立。

### 命题 B｜产品、加工或成分

{p['specific']}

样品产地、品牌、份量、年代与实验方案不得超出原研究外推；体外数据不升级为人群效应。

## 7. 安全与实用选择

{p['safety']}

## 8. 本草映射候选

本阶段不预写 Jev 分类、四气五味归经或 M 等级。味觉描述只用于食品感官，不能推成传统药性或临床效果。

## 9. 未知与停止规则

仍未知：不同品牌/地区配方分布与长期本条特异结局。替代解释包括杯量、剂量、甜味来源、奶基底、总体饮食、口腔暴露频率与研究终点。

停止状态：R1_scope_met。若出现代表性市场调查、同配方人体试验或重要安全警报，再定向重开。

## 10. 核心参考资料

{refs}

"""
def summary(i,p):
 family="咖啡母页只提供基底背景；奶种、糖浆、粉包配方与脱因加工会改变产品身份或暴露。" if p["family"]=="coffee" else "软饮母页提示含糖量、酸度和碳酸水身份须按实际成分区分。"
 tradition="咖啡共享传统资料来自近现代文献，不能据此称现代配方为古籍直接分类。" if p["family"]=="coffee" else "本条为现代饮料，传统饮水资料不等于对当前工业配方的专门记载。"
 return f"""# Summary Document — {p['name']}

**身份。** {p['identity']}

**组成与暴露。** {p['composition']} {p['variables']}

**本条研究。** {p['direct']}

**产品/工艺证据。** {p['specific']}

**共享背景。** {family}

**安全。** {p['safety']}

**传统来源。** {tradition}

本摘要只复述 Research Dossier 可追溯事实，不预设模型分类或 M 等级。未检得只表示本轮 R1 探索范围。
"""
def main():
 out=ROOT/"references/entries"
 for i,p in DATA.items():
  d=out/i; d.mkdir(parents=True,exist_ok=True)
  (d/"research.md").write_text(dossier(i,p),encoding="utf-8")
  (d/"summary.md").write_text(summary(i,p),encoding="utf-8")
 sp=ROOT/"references/shared/soft-drink-base/research.md"; sp.parent.mkdir(parents=True,exist_ok=True)
 sp.write_text("""# Shared Research — 碳酸与软饮基础

> scope: background node, not a standalone health conclusion
> evidence_cutoff: 2026-09-24

可乐、柠檬汽水、含矿物盐苏打水与气泡水是不同对象。是否加糖、酸味剂、钠盐、咖啡因与香料须按标签区分。

Ebbeling 等随机干预研究纳入 224 名超重/肥胖青少年常饮含糖饮料者，干预目标为减少多种 SSB。一年时 BMI 增幅较小，但两年主要终点没有显著组间差异。该研究不是可乐单一品牌，也不能迁移给无糖饮料或碳酸水。

Zimmer 等将牛牙釉质/牙本质样本在特定饮料中连续浸泡七天；体外比较不代表真实人群长期剂量。Brown 等针对英国市场调味气泡水测得低 pH 与体外侵蚀潜力；对象不是无添加原味气泡水。Ryu 等测试家用苏打机碳酸水对预处理牙釉质材料的影响，不等于正常完整牙齿的日常饮水试验。

## Core references

1. Ebbeling CB, Feldman HA, Chomitz VR, et al. “A Randomized Trial of Sugar-Sweetened Beverages and Adolescent Body Weight.” New England Journal of Medicine. 2012;367:1407–1416. DOI: https://doi.org/10.1056/NEJMoa1203388.
2. Zimmer S, Kirchner G, Bizhang M, Benedix M. “Influence of Various Acidic Beverages on Tooth Erosion: Evaluation by a New Method.” PLOS ONE. 2015;10(6):e0129462. DOI: https://doi.org/10.1371/journal.pone.0129462.
3. Brown CJ, Smith G, Shaw L, Parry J, Smith AJ. “The Erosive Potential of Flavoured Sparkling Water Drinks.” International Journal of Paediatric Dentistry. 2007;17(2):86–91. DOI: https://doi.org/10.1111/j.1365-263X.2006.00784.x.
4. Ryu H, Kim Y, Heo S, Kim S. “Effect of Carbonated Water Manufactured by a Soda Carbonator on Etched or Sealed Enamel.” The Korean Journal of Orthodontics. 2018;48(1):48–56. DOI: https://doi.org/10.4041/kjod.2018.48.1.48.

Each child entry must independently judge identity, dose and directness. No single soft-drink study establishes a class-wide clinical effect.
""",encoding="utf-8")
 qa="# QA Log — 第四批咖啡与碳酸饮品十条\\n\\n> 日期：2026-09-24\\n> 研究深度：R1 定向检索，不是系统综述。\\n> 证据截止：2026-09-24。\\n\\n## 本批目录顺序\\n\\n"+ "".join(f"{n}. {i}（{p['name']}）\\n" for n,(i,p) in enumerate(DATA.items(),1))+"""
## 中间产物

- 搜：十份 references/entries/<id>/research.md；咖啡条链接 coffee-base，软饮条链接 soft-drink-base。
- 整：十份 summary.md 只复述底稿事实，不含 Jev、四气五味归经或 M。
- 冻结：qa/coffee-soda-summary-sha256.txt 与 qa/jev-coffee-soda-batch/pre-freeze/<id>.json 保存摘要 SHA-256 和原文。
- 判：workflow 使用 environment API_KEYS 与 secrets.JEV_API_KEY；首次 API 请求前校验 manifest 与快照；raw JSON 不加 M、不改分数。
- 写：Mapping 保存 probability/Noul、confidence、方向；正文回链 research、summary、mapping。参考文献保留英文题名与可核实 DOI。

## 身份红队

- 焦糖玛奇朵与 espresso macchiato 区分。
- 燕麦/椰乳拿铁与植物饮研究分层；奶基底不是成品临床试验。
- 纯速溶咖啡与三合一预混包分别立条。
- 常规可乐与已有无糖可乐条目分开。
- 柠檬汽水实验只代表指定品牌与体外条件。
- 苏打水按标签确认矿物盐/碳酸氢盐；气泡水区分原味与调味。
 
## 初次运行记录

- 2026-09-24，workflow run 35981400606 首次尝试在 Research Dossier 阶段因配置缺少 `queries` 字段中止；`API_KEYS/JEV_API_KEY` 预检通过，冻结、Jev 分类、Mapping 与正文阶段均未执行，因此没有产生原始分类结果。修复配置后重跑。

## Actions 与写作 QA

待补录 workflow run、artifact、raw 哈希、模型版本、答案数与正文检查结果。
"""
 (ROOT/"qa/coffee-soda-batch-2026-09-24.md").write_text(qa,encoding="utf-8")
 print(f"Built {len(DATA)} stage-1/2 records.")
if __name__=="__main__": main()
