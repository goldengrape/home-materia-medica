---
type: Decision
title: Jev 四气五味归经 + 阴阳增减主方向
description: 当前采用自然语言说明文档 + v0.4 reasoning rules + five-shot；每个五脏归经增加阴-/阴+/阳-/阳+主方向 Choice；Jev score 与 M grade 独立。
resource: ../../docs/jev-rule-fewshot-pilot/RESULTS-v0.4.md
tags: [jev, materia-mapping, few-shot, reasoning, yin-yang, pilot, derived]
status: derived
source_ids: [URD-REQ-001, URD-REQ-008, URD-REQ-009, URD-REQ-010, URD-REQ-011, DEC-017, DEC-018]
---

# Jev 判定

当前生产候选：

```text
Research Dossier
→ 自然语言说明文档
→ v0.4 reasoning rules + five-shot
→ Jev 16 questions
→ 四气 / 五味 / 五脏归经
→ 每经 阴-/阴+/阳-/阳+ 主方向
→ native probabilities
→ 与 M grade 并列
→ 派生传统用词
```

## 设计决定

### 语义级连、计算同步

语义：

```text
先归经
→ 再判断该经主方向
```

实现：

> 一次 Jev request 同时计算归经和五个 direction Choice。

不使用 threshold 后第二次 API 级连。

### 主方向 Choice

每经固定：

```text
阴-
阴+
阳-
阳+
```

只输出一个主方向，同时保存四项 probabilities，以保留混合效应。

### 传统用词下沉

“疏肝、健脾、润肺、温中、化湿、生津”等不是一级分类。

示例：

```text
肝 + 阳- → 疏肝等候选表达
脾 + 阳+ → 健脾 / 温中等候选表达
肺 + 阴+ → 润肺 / 生津等候选表达
```

最终用词仍取决于语境。

### Jev / M 双轴

```text
Jev score != M grade
```

M 不修改 Jev；
Jev 不提升 M。

## 验证

### 中药

v0.4 regression，3 次：

- 四气：5/5；
- 五味：5/5；
- 五脏归经：5/5；
- 10 个有效归经主方向：10/10。

actual model：`jev-1.13.0`。

### 现代食品

- 开心果：脾阳+、肾阳+；
- 咖啡：脾阳+；
- 酸奶：脾阳+为主，但 probability 较分散；
- 黑巧克力 / 方便面：无主归经。

## 历史

- v0.1：API proof，旧十二经 schema。
- v0.2：封闭输出，但结构化 target。
- v0.3.1：自然语言 + reasoning rules 稳定。
- v0.4 early：20 direction Noul，已废弃。
- v0.4 current：5 direction Choice。
