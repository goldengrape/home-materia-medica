# Workflow

## Phase 0 — Load project state

先读取：

1. `docs/居家本草编纂凡例-v1.0.md`
2. `catalog/README.md`
3. 目标条目的目录位置、已有研究文件与相关母条。

若项目规则与本 skill 冲突，以项目凡例为准，并在底稿备注。

---

## Phase 1 — Identity

建立 **Identity Card**：

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
identity_confidence: high | medium | low
```

若为植物 / 天然产物，额外记录：

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

并非每个字段都适用；不适用写 N/A，未知写 unknown，不可猜测。

---

## Phase 2 — Scope

### 2.1 选研究深度

R1 / R2 / R3。

### 2.2 核心问题

原则上 3–8 个；R1 可更少。

优先顺序：

1. 最能定义条目的主要即时作用；
2. 与长期健康最相关的直接证据；
3. 加工 / 剂量 / 时机是否改变作用；
4. 主要不良反应；
5. 与本草性味 / 归经 / 食效最可能相关的人体功能；
6. 关键争议。

不要把“所有可能疾病结局”都列为核心问题。

### 2.3 结构化问题

人体效应用 PECO / PECOT：

- P：Population
- E/I：Exposure / Intervention
- C：Comparator
- O：Outcome
- T：Time

食品加工 / 成分问题可用：

> food matrix × processing/factor × measured outcome

---

## Phase 3 — Search

### 3.1 先宽后窄

首轮目标不是收齐论文，而是建立 landscape：

- 最新高质量综述；
- 主要术语与同义词；
- 主要结局；
- 关键争议；
- 综述检索截止日期。

### 3.2 再做直接问题检索

每个核心问题至少设计：

- 对象词；
- 结局词；
- 研究设计 / 人群词（必要时）；
- 安全性反向词。

保留完整检索式、数据库、日期和结果数。

### 3.3 Citation chaining

对真正关键的综述 / RCT：

- 查看重要参考文献；
- 查看后续引用；
- 查更正 / 撤稿 / 表达关注；
- 找综述截止日期后的更新研究。

---

## Phase 4 — Screen

每篇候选文献先问：

1. 研究的是我们这个食品 / 制品吗？
2. 剂量像真实食用量吗？
3. 人群适合正文要说的话吗？
4. 结局是我们关心的结局吗？
5. 是急性还是长期？
6. 是临床结局还是代理指标？
7. 是否只是孤立成分？
8. 是否有明显利益冲突 / 资金来源需要记录？

然后标记 D0–D4。

---

## Phase 5 — Extract

至少提取：

- Citation
- DOI / PMID
- 设计
- 国家 / 人群
- n
- 食品身份 / 配方 / 加工
- 剂量
- 对照
- 时间
- outcome
- effect estimate
- confidence interval
- 主要结果
- adverse events
- funding / COI
- risk-of-bias notes
- evidence distance
- full-text status
- supports
- does_not_support

不能从摘要得到的字段留空，不推测。

---

## Phase 6 — Appraise

### 单篇

做设计匹配的偏倚评价。

### 证据体

至少检查：

- Risk of bias
- Consistency
- Directness
- Precision
- Publication bias / missing evidence
- Generalizability

营养观察研究加查：

- dietary assessment validity；
- repeated vs baseline-only exposure；
- energy adjustment；
- substitution / comparator；
- residual confounding；
- reverse causality。

---

## Phase 7 — Synthesize

按核心问题 / outcome 综合。

每个 outcome 写：

1. 直接人体证据；
2. 结果一致还是冲突；
3. 效应大小是否具有实际意义；
4. 剂量 / 人群 / 加工限定；
5. D0–D4 分布；
6. E 等级；
7. 允许的文字强度；
8. 关键引用。

不要写成“论文 A 说……论文 B 说……”的流水账。

---

## Phase 8 — Mechanism

机制只回答：

- 是否能解释人体观察？
- 日常摄入剂量是否可达到？
- 食品基质会不会改变暴露？
- 有没有竞争机制 / 相反机制？
- 机制对 M 映射贡献多大？

若没有人体效应，只能写“机制假说”，不可倒推人体功效。

---

## Phase 9 — Materia mapping

对每个候选本草术语：

```text
候选术语：
拟映射对象：
直接人体事实：
传统理论桥梁：
机制辅助：
支持：
反证：
替代解释：
M 等级：
最大允许表述：
```

若存在两个同样合理的归经解释，不强行二选一，可列：

> 候选 A / 候选 B；目前 M-0 或 M-IV。

---

## Phase 10 — Safety

安全单独一节，避免被“总体有益”叙事淹没。

记录：

- common adverse effects
- serious signals
- dose relationship
- allergy
- pregnancy / lactation
- children / older adults
- disease-specific concern
- drug interactions
- regulatory warnings

病例报告可提供严重安全信号，但不估算常见发生率。

---

## Phase 11 — Stop

达到以下条件即可停止：

- 已找到当前较好的直接证据综合；
- 已检查截止日期后的重要研究；
- 支持、反向、安全证据均有覆盖；
- E 等级稳定；
- 新文献主要重复；
- 无未解决的重大矛盾。

记录：

```yaml
stopping_status: saturated | sparse_evidence | budget_reached | unresolved_conflict
stopping_reason:
evidence_cutoff:
```

---

## Phase 12 — Verify

逐条检查 Claim Ledger：

- Claim 是否被所引来源真正支持？
- 是否偷换了食品形态？
- 数值和单位是否一致？
- DOI / PMID 是否对应正确论文？
- 是否把统计显著写成临床重要？
- 是否把相关性写成因果？
- 是否把 D2 / D3 写成 D0 结论？
- 是否把 E 结论直接当作 M 结论？

完成后才能把底稿状态改为 `review_ready`。
