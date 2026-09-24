---
type: Project Workflow
title: 条目从资料到正文的生产链
description: 快速查看一个条目从目录身份到 publish-ready 的标准顺序。
resource: ../../docs/生产流程.md
tags: [workflow, research, jev, mapping, writing, derived]
status: derived
source_ids: [PB-DEC-010, ARC-IF-004, ARC-IF-005, ARC-IF-006, ARC-IF-007]
---

# 搜 → 整 → 判 → 写

```text
Catalog entry
→ 搜：research.md
→ 整：summary.md
→ 判：Jev v0.4 → mapping.md → 逐项标 M
→ 写：entries/<entry-id>.md
→ QA
→ Publish ready
```

## Key boundaries

### 搜

收集来源、证据、安全、传统资料和反证；不预判最终分类。

### 整

把资料整理成连续、中立、可推理的 `summary.md`；不提前写 Jev 答案或 M。

### 判

Jev 先输出四气、五味、五脏归经和每经阴阳增减主方向；保存原生 score / probabilities 后，再依据 `research.md` 对分类逐项标 M。

### 写

正文读取资料和分类结果，不重新研究或重分类。缺资料返回“搜/整”，分类问题返回“判”。

# Citations

[1] [生产流程](../../docs/生产流程.md)  
[2] [Project Trace](../../docs/TRACE.md)  
[3] [编纂架构](../../docs/编纂架构.md)
