---
type: Decision
title: Jev 四气五味归经规则 + Few-shot Pilot
description: 记录 Jev 封闭字段、强制分类、rule + five-shot 的 pilot 设计与 v0.2 结果。
resource: ../../docs/jev-rule-fewshot-pilot/RESULTS-v0.2.md
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

## v0.2

输出空间固定为：

- 四气：寒 / 凉 / 平 / 温 / 热，强制五选一；
- 五味：酸 / 苦 / 甘 / 辛 / 咸；
- 归经：心 / 肝 / 脾 / 肺 / 肾。

3 次重复、5 个新 held-out：

- 四气：三次均 4/5；干姜稳定误判为温而非热；
- 五味：三次均 5/5 exact，micro-F1 1.0；
- 五脏归经：exact set 1–2/5，micro-F1 0.720–0.769，主要问题是漏判。

v0.1 的十二经输出空间与项目契约不一致，只保留为工程历史记录。

完整结果与逐样本概率见 source document。

## Next

如继续，应升到 v0.3：强化温/热对比，并给五脏归经建立更明确的项目级 criteria / Concept Trace 桥梁。仍不引入概率修正函数。
