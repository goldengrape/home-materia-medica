---
type: Decision
title: Jev 四气五味归经规则 + Five-shot Pilot
description: 当前采用自然语言说明文档 + 推理规则 + five-shot；Jev score 与 M grade 作为独立双轴并列展示。
resource: ../../docs/jev-rule-fewshot-pilot/DOMAIN-TRANSFER-RESULTS-v0.1.md
tags: [jev, materia-mapping, few-shot, reasoning, narrative, pilot, derived]
status: derived
source_ids: [URD-REQ-001, URD-REQ-002, URD-REQ-007, URD-REQ-008, DEC-011, DEC-012, DEC-014]
---

# Jev 判定 Pilot

当前路线：

```text
Research Dossier
→ 自然语言说明文档
→ 推理规则 + narrative five-shot
→ Jev 固定 questions
→ 原生概率
→ Materia mapping / Claim Ledger
```

不训练 Jev，不使用 post-hoc probability calibration function。

## 当前有效版本：v0.3.1

核心变化：

- rules 不再重复“只能选什么”等接口限制，只教如何推理；
- target 与 five-shot 都使用连续说明文档；
- 四气推理从证候寒热与纠偏强弱出发；
- 五味结合感官与“散/泄/补/收/软”等功能模式；
- 五脏归经先做功能群识别，再按五字段工作投影；
- 胃→脾、胆→肝、大肠→肺、小肠→心、膀胱→肾；三焦按具体语境。

v0.3.1 五个 reasoning-complete held-out，3 次重复：

- 四气：5/5 × 3；
- 五味 exact：5/5 × 3；
- 五脏归经 exact：5/5 × 3；
- 三类 micro-F1 均为 1.0 × 3。

这只说明在说明文档本身包含充分桥梁时，Jev 可以稳定执行规则；不代表现代食品生产准确率。

## 历史

- v0.1：验证 API / secret / 匿名化；输出空间设计错误。
- v0.2：封闭字段正确，但 target 仍是结构化 packet。
- v0.3 #11：narrative + reasoning 首测，发现 gold 投影和样本一致性 bug，判 invalid。
- v0.3.1 #14：修正后有效。

## Food domain transfer v0.1

使用开心果、黑巧克力、咖啡、酸奶、方便面五个现有 Research Dossier，冻结 v0.3.1 rules + five-shot。

主要发现：

- 黑巧克力、方便面没有被强行归经，与现有 M-0 边界兼容；
- 开心果被稳定推为脾、肾，明显高于项目当前归经证据门槛；
- 酸奶被稳定推为脾，而项目当前只允许“健脾”作 M-IV 类比，现代酸奶归经仍 M-0；
- 咖啡脾经约 0.49–0.52，在“健胃→脾”的映射边界上来回翻转。

这些结果显示 Jev 候选与项目证据强度可以明显分离；例如酸奶可记录 `脾 0.58–0.61｜M-0`。

## Next

现行策略不加入 M gate：Jev 按 frozen reasoning rules 给出候选和原生 score；Research Dossier 独立给 M-I～M-0。两者不互相修正，交由后续写作层并列呈现。
