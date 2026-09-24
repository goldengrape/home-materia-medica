---
type: Decision
title: Jev 四气五味归经规则 + Few-shot Pilot
description: 记录 Jev 不微调、不做概率修正的 pilot 设计与首轮结果。
resource: ../../docs/jev-rule-fewshot-pilot/RESULTS-v0.1.md
tags: [jev, materia-mapping, few-shot, pilot, derived]
status: derived
source_ids: [URD-REQ-001, URD-REQ-002, URD-REQ-003, DEC-001, DEC-005, URD-AC-006]
---

# Jev 判定 Pilot

当前路线：

```text
Research / evidence packet
→ 固定规则
→ few-shot 示例
→ Jev 原生概率
→ 人工/规则层消费
```

不训练 Jev，不使用 post-hoc probability calibration function。

## v0.1

5 个匿名 held-out 中药样本：

- 四气：5/5；
- 五味 exact set：4/5，micro-F1 0.857；
- 归经 exact set：1/5，micro-F1 0.824。

归经仍是主要难点。首轮错误显示：

- 功能词里的脏腑名称可能被过度提升成归经；
- 感官味觉可能干扰传统五味；
- 0.5 附近的 Noul 不适合直接理解成生产结论。

完整结果、逐样本概率和限制见 source document。

## Next

先改 packet schema 与 contrastive few-shot，再扩大独立 held-out set。  
在更大样本前，不设生产阈值，不写“已校准”。
