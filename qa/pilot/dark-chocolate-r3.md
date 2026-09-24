# Pilot QA — 黑巧克力 R3

> 日期：2026-09-23  
> 对应：`references/entries/dark-chocolate/research.md`

## 1. 是否完成

是。R3 核心问题达到当前证据饱和。

## 2. 本轮最重要的方法学发现

### QA-DC-001｜“研究质量”与“证据距离”必须分开

COSMOS 是大样本长期 RCT，但研究的是标准化 cocoa extract capsule。

因此：

> 高内部效度 ≠ 对目标食品高直接性。

D0–D4 不是附属字段，而是食品研究的核心维度。

### QA-DC-002｜系统综述也会偷换食品对象

2024 cardiometabolic meta-analysis 在同一个 pooled analysis 中纳入：

- cocoa extract；
- ≥70% dark chocolate。

所以“找到最新 Meta”之后仍必须看 inclusion criteria，不能只抄 abstract conclusion。

### QA-DC-003｜“疏肝”问题证明 M 与 E 必须分离

现代证据可以支持：

- negative affect；
- depression score；
- cortisol / epinephrine stress response。

但这些不同 outcome 不能被压成一个“疏肝”结论。

当前：

- mood effect：E-C；
- 疏肝解郁：M-IV；
- 归肝经：M-0。

这正好验证项目最初对归经证据链的要求。

### QA-DC-004｜安神不能从“情绪改善”顺手带出来

2024 direct RCT 对 sleep quality 没有显著改善。

而 dark chocolate 又含 caffeine / theobromine。

所以：

> mood positive signal ≠ 安神。

### QA-DC-005｜食品百分比不是药理剂量

85% 比 70% 在一项小 RCT 中出现更明显 mood effect，并不意味着：

> cocoa % 越高 → 功效线性越强。

cocoa percentage 不能替代：

- flavanol analysis；
- methylxanthine content；
- sugar；
- serving size；
- processing。

### QA-DC-006｜R3 停止规则基本有效

即使 cocoa/chocolate 文献非常多，只围绕 6 个核心问题工作，仍能停止。

继续追：

- 每种 polyphenol；
- 每条 NO pathway；
- microbiome taxa；
- neurotransmitters；

不会改变 E/M，因此应停。

## 3. 对模板的潜在改进

建议后续考虑新增两个字段，但先不立即修改全局模板：

1. `evidence_base_overlap`：标记多个 Meta 是否共享同一批试验；
2. `intervention_purity_vs_food_directness`：提醒标准化提取物可能“研究更干净、离食品更远”。

等奶茶 Pilot 后一起决定是否正式加入。

## 4. 黑巧克力 Pilot 的一句话结论

> 现代研究可以较有把握地说“高可可干预对部分心代谢指标有小幅影响”，也可以谨慎说“某些黑巧克力短期可能改善部分负性情绪”；但从这里走到“疏肝解郁”“安神”“归肝经”，证据链仍明显不够。
