# Design Split — Jev Pilot v0.4

> 来源：`URD.md`

## Functional Requirements

| ID | Requirement |
|---|---|
| ADD-FR-001 | 输入为自然语言说明文档。 |
| ADD-FR-002 | rules 教授四气、五味、脏腑功能群与阴阳增减方向推理。 |
| ADD-FR-003 | five-shot / held-out 分离。 |
| ADD-FR-004 | schema 限定输出；rules 不重复接口约束。 |
| ADD-FR-005 | 保存 Jev 原生 probabilities / Noul。 |
| ADD-FR-006 | 五脏工作投影在 rules、demo、gold 一致。 |
| ADD-FR-007 | 每经一个主方向 Choice。 |
| ADD-FR-008 | Jev 与 M 双轴独立。 |
| ADD-FR-009 | Secret 只从 GitHub Environment 注入。 |

## Design Parameters

| ID | Parameter |
|---|---|
| ADD-DP-001 | state = reasoning rules + narrative five-shot + narrative target。 |
| ADD-DP-002 | fixtures-v0.4.json 保存 demo / held-out；meta/gold 不进入 state。 |
| ADD-DP-003 | questions = 1 qi Choice + 5 taste Noul + 5 meridian Noul + 5 direction Choice。 |
| ADD-DP-004 | direction values = 阴-/阴+/阳-/阳+。 |
| ADD-DP-005 | 语义上先归经后方向；API 一次同步调用。 |
| ADD-DP-006 | direction Choice 保存四项 probabilities，允许显示次方向。 |
| ADD-DP-007 | 同一冻结版本重复 3 次。 |
| ADD-DP-008 | 暂时性 529 overload 可短重试。 |

## 关键设计决定

### DEC-001｜不训练校准函数

原生 Jev score / probability 不做后处理。

### DEC-011｜rules 只教推理

输出空间由 questions 保证。

### DEC-012｜target 是自然语言

生产输入不要求特征 JSON。

### DEC-014｜五脏功能群投影

```text
胆→肝
胃→脾
大肠→肺
小肠→心
膀胱→肾
三焦→按语境
```

### DEC-016｜习惯术语不是一级分类

```text
归经 + 阴阳增减 + 语境
→ 疏肝 / 健脾 / 润肺 / 温中 / 化湿 / 生津……
```

派生词不得反向改变原始分类。

### DEC-017｜语义级连、计算同步

不使用“第一轮归经 threshold → 第二轮 direction API”。

### DEC-018｜每经一个主方向 Choice

早期 20 个 direction Noul draft 已被替代。

Choice 保持单一主分类，同时用 probability 分布保留混合方向。

## 数据流

```text
Research Dossier
→ natural-language description
→ reasoning rules + five-shot
→ Jev 16 questions
→ 四气 / 五味 / 归经 / 主方向
→ native scores
→ 与 M grade 并列
→ conventional wording
```
