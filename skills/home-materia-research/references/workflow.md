# Research Workflow — 搜 + 整

> 本文件只覆盖 `docs/生产流程.md` 的前两阶段。  
> 主流程：**搜 → 整 → 判 → 写**。

# A｜搜：收集资料

## A0 — Load

读取：

1. `docs/居家本草编纂凡例-v1.0.md`
2. `docs/生产流程.md`
3. `catalog/README.md`
4. 目标条目的 Catalog / Entry Registry；
5. 已有 Research Parent 或历史 dossier。

## A1 — Identity

建立 Identity Card：

```yaml
entry_id:
name:
entry_type:
research_object:
common_variants:
ingredients:
processing:
typical_serving:
key_variables:
traditional_parent:
identity_confidence:
```

植物 / 天然产物按需要补：

```yaml
scientific_name:
family:
plant_part:
origin_or_cultivar:
fresh_or_dried:
processing:
extract_solvent:
drug_extract_ratio:
standardization_marker:
chemical_characterization:
voucher_or_authentication:
```

检索若证明 Catalog 对象边界有误，记录 Identity Revision，不为了保留旧名称研究一个不稳定对象。

## A2 — Scope

选择 R1 / R2 / R3。

列 3–8 个核心问题；R1 可更少。

人体效应优先用 PECOT：

- P Population
- E/I Exposure / Intervention
- C Comparator
- O Outcome
- T Time

复合食品先做 Composition & Exposure：

- common serving；
- sugar / sodium / caffeine / alcohol 等真实暴露；
- 产品差异；
- 配方和加工；
- customization；
- 直接检测或权威市场调查。

## A3 — Search

分层检索：

### A3.1 Evidence synthesis

优先：

- systematic review / meta-analysis；
- Cochrane；
- 权威机构证据综合；
- FDA / EFSA / WHO / USDA NESR / Codex 等。

作用：建立 landscape、找到关键词、确定综述 search cutoff。

### A3.2 Direct human evidence

寻找：

- RCT / crossover；
- prospective cohort；
- 其他直接人体研究；
- 剂量 / 时机 / 加工差异。

### A3.3 Safety

独立检索：

- adverse effects；
- allergy；
- interactions；
- special populations；
- regulatory warnings；
- case reports / series。

### A3.4 Traditional sources

尽量回到原文：

- 书名、时代、版本；
- 卷次 / 页码；
- 原文和上下文；
- 身份、物种、部位、炮制对应。

### A3.5 Mechanism

只用于：

- 解释已观察到的人体效应；
- 解释加工差异；
- 为后续分类提供可审计的辅助背景。

没有人体效应时，不用机制制造人体功效。

## A4 — Screen + D

每篇资料先判断：

1. 是目标食品 / 制品吗？
2. 剂量和形态接近日常暴露吗？
3. 人群适用吗？
4. outcome 对题吗？
5. 急性还是长期？
6. 临床结局还是代理指标？
7. 是否只是孤立成分？
8. 有无重要 COI / funding？

关键现代证据标 D0–D4。

## A5 — Extract

Evidence Record 至少保留：

- Citation；
- DOI / PMID；
- design；
- population / n；
- food identity；
- dose；
- comparator；
- time；
- outcome；
- effect estimate / CI；
- adverse events；
- funding / COI；
- risk-of-bias note；
- D；
- full_text_status；
- supports / does_not_support。

不从摘要得出的字段留空，不猜。

# B｜整：整理总结资料

## B1 — Appraise

按设计选择适当方法学框架：

- RCT → RoB 2；
- 非随机干预 → ROBINS-I；
- 营养观察 → ROBINS-E 思路；
- 系统综述 → 检查检索、纳入、偏倚、异质性、发表偏倚。

证据体固定检查：

- Risk of bias；
- Consistency；
- Directness；
- Precision；
- Publication bias / missing evidence；
- Generalizability。

## B2 — Evidence-base overlap

多个 Meta / review 共享同一批基础研究时记录：

```yaml
evidence_base_overlap:
  level:
  note:
```

不能把“有四篇 Meta”写成四套独立重复证据。

## B3 — Synthesize + E

按 outcome / claim 综合，不逐篇流水账。

每个 outcome 写：

1. 直接人体证据；
2. 一致 / 冲突；
3. 实际效应大小；
4. 剂量 / 人群 / 加工限定；
5. D 分布；
6. E-A ～ E-0；
7. 可允许的事实表述；
8. 关键引用。

E 只评价人体效应，不评价四气、五味或归经。

## B4 — Mechanism

机制只解释：

- 是否与人体观察一致；
- 日常摄入能否达到；
- 食品基质 / 加工是否改变暴露；
- 是否存在相反机制。

## B5 — Concept Trace

遇到真正影响后续推理的底层概念时做 Concept Trace：

- 四气；
- 五味；
- 归经；
- 心 / 肝 / 脾 / 肺 / 肾；
- 阴 / 阳；
- + / -；
- 五脏 / 六腑功能群投影；
- 炮制 / 配伍。

“疏肝、健脾、润肺、温中、化湿、生津”等传统习惯词不要求在本阶段先确定；它们可在写作层根据原子分类与语境派生。

## B6 — Conflicts / Unknowns

必须保留：

- 相反结果；
- 替代解释；
- 研究空白；
- 身份 / 加工差异；
- 不能外推的 D2–D4；
- 安全不确定性。

整理不是“只留下支持结论的资料”。

## B7 — Stop

满足项目预算后停止：

```yaml
stopping_status: saturated | sparse_evidence | budget_reached | unresolved_conflict
stopping_reason:
evidence_cutoff:
```

“还有论文没读”不是继续研究的充分理由。

## B8 — Reference Audit

核验：

- title / author / year / journal；
- DOI / PMID / PMCID；
- 更正 / 撤稿；
- 传统版本与位置；
- 数字和单位；
- 食品形态；
- association / effect 不偷换。

## B9 — Write Summary Document

从 `research.md` 生成：

`references/entries/<entry-id>/summary.md`

要求：

- 连续自然语言；
- 可独立阅读；
- 包含 Jev 推理真正需要的事实桥梁；
- 保留支持、反证、限制、替代解释；
- 不要求固定 feature schema。

禁止：

- 预写最终四气 / 五味 / 归经；
- 预写阴-/阴+/阳-/阳+；
- 写 Jev score；
- 写 M grade；
- 为了让模型得到某答案而新增 research.md 中没有的桥梁。

# C｜Handoff：整 → 判

完成 `summary.md` 后，本 skill 停止。

下一步调用：

`skills/home-materia-jev-mapping/SKILL.md`

顺序固定：

```text
summary.md
→ Jev v0.4 分类
→ 保存原始 scores
→ 回查 research.md
→ 对分类逐项标 M
→ mapping.md
```

M 不在 Jev 之前充当分类 gate。

# 完成检查

- [ ] Identity 稳定？
- [ ] R 预算明确？
- [ ] Composition / Exposure 必要时已完成？
- [ ] 支持、反向、安全都检索过？
- [ ] 关键证据有 D？
- [ ] 人体 outcome 有 E？
- [ ] 机制没有越级？
- [ ] Concept Trace 只做必要底层概念？
- [ ] 冲突、未知和替代解释保留？
- [ ] evidence cutoff / stop reason 完整？
- [ ] `summary.md` 忠实于 `research.md`？
- [ ] `summary.md` 没有提前写分类或 M？

若直接人体证据不存在，允许明确写：

> 目前无足够直接人体证据；停止扩张间接机制检索。
