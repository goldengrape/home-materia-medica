# Pilot 方法复盘 — 前三项

> checkpoint: RM-TASK-026  
> 日期：2026-09-23  
> 样例：开心果 R2 / 黑巧克力 R3 / 珍珠奶茶 R2

## 一、结论

前三个 Pilot 没有发现需要推倒 R/D/E/M 框架的问题。

相反，它们分别验证了三种不同研究生态：

| 条目 | 研究生态 | 停止方式 | 最关键的方法学发现 |
|---|---|---|---|
| 开心果 | 直接整食物 RCT 较多、传统资料也存在 | saturated | Meta 高度重叠；传统功用不等于归经 |
| 黑巧克力 | 文献极多、食品/提取物/单成分混杂 | saturated_for_R3_core_questions | 研究质量与食品直接性必须分开；E 与 M 必须分开 |
| 珍珠奶茶 | 组成证据丰富、直接长期人体结局稀少 | sparse_evidence | Identity 可推翻原条目名；组成证据强不等于疾病因果证据强 |

因此当前建议：

> **保留 R1/R2/R3、D0–D4、E-A–E-0、M-I–M-0 与现有停止规则，只做小幅模板升级。**

---

## 二、哪些规则已经通过测试

### REVIEW-001｜Identity first 必须保留，而且要有修改 Catalog 的权限

开心果纠正了“传统依据弱”的先验；珍珠奶茶更直接地证明了泛称“奶茶”不是稳定对象。

因此 Identify 阶段不能只是填写字段，而必须允许：

- 修改 canonical name；
- 拆分/合并条目；
- 把原主条目降为类别标签；
- 发现传统母本后补 parent relation。

研究对象改变时，要留下 `identity_revision`，而不是悄悄改名。

### REVIEW-002｜D0–D4 是食品研究核心，不是附加备注

黑巧克力最清楚：COSMOS 内部效度很高、样本极大，但可可提取物对黑巧克力仍是 D2。

珍珠奶茶同样显示：

- generic SSB = D2；
- pure caffeine = D3；
- 茶叶本草 = 复合食品的 D4 传统类比。

因此 D 不能被 study design 覆盖。

### REVIEW-003｜E 必须按 claim / outcome，而不是给食品打总分

一个条目可以同时有：

- 开心果：血脂 E-B、餐后血糖 E-C、长期疾病事件 E-0；
- 黑巧克力：部分心代谢 E-B、mood E-C、CVD event food claim E-0；
- 珍珠奶茶：直接组成证据强，但长期疾病因果 E-0。

这证明“一个食品一个证据等级”不可行。

### REVIEW-004｜M 与 E 分离是必要约束

黑巧克力是最佳压力测试：

- negative affect / stress signal 可以存在；
- 疏肝仍只能 M-IV；
- 安神 M-0；
- 归肝/心经 M-0。

开心果也显示：

- 古籍有调中、腰冷等传统功用；
- 仍不能从功用词自动补归经。

### REVIEW-005｜停止规则已能覆盖两种相反极端

**文献过多：** 黑巧克力在核心问题稳定后停止，不追每种 polyphenol。

**文献过少：** 珍珠奶茶在确认直接长期 evidence sparse 后停止，不用 sugar/caffeine/tea mechanisms 填空。

因此 `saturated` 和 `sparse_evidence` 应继续保留为并列的正常完成状态。

---

## 三、三个 Pilot 共同暴露出的模板缺口

### REVIEW-010｜缺少 Identity Revision

珍珠奶茶证明条目研究可能改变研究对象本身。

建议新增：

```yaml
identity_revision:
  changed: yes | no
  original_entry_id:
  revised_entry_id:
  reason:
  catalog_action:
```

### REVIEW-011｜缺少 Evidence-base Overlap

开心果出现多个 Meta-analysis 高度共享同一批 RCT。

如果不记录，很容易形成“4 篇 Meta 都支持”的虚假重复感。

建议在证据综合层新增：

```yaml
evidence_base_overlap:
  level: low | moderate | high | unknown
  note:
```

不要求每篇论文计算 citation overlap，只要求在结论可能受重复基础研究影响时标记。

### REVIEW-012｜缺少 Directness Note

黑巧克力说明：一个标准化提取物试验可以设计得非常干净，却离日常食品更远。

建议证据卡除 `evidence_distance` 外增加一句：

```yaml
directness_note:
```

避免新建复杂的第二套 directness 评分。

### REVIEW-013｜复合食品需要 Composition-first

珍珠奶茶说明，对某些现代食品：

> “里面实际有什么、多少、差异多大”

比“有没有临床功效”更先决定正文。

建议模板在现代证据地图之前增加可选的 `Composition & exposure` 小节，记录：

- serving size；
- sugar / sodium / caffeine / alcohol 等关键暴露；
- 产品间变异；
- 配方和 toppings；
- 直接检测来源。

这些资料**不强行塞进 E 分级**。E 继续只负责人体健康 effect claim。

### REVIEW-014｜加工/定制变量需要独立记录

三个条目都出现：

- 开心果：原味 / 盐焗 / 糖衣；
- 黑巧克力：可可比例 / 糖 / 加工；
- 珍珠奶茶：甜度 / 珍珠 / 奶精 / 杯量。

建议 Identity Card 增加：

```yaml
processing_or_customization_variables: []
```

这比把所有差异都塞进 `key_variables` 更容易支持后续“炮制”讨论。

---

## 四、暂时不新增的新系统

### 不新增“组成证据 A/B/C”分级

理由：三个 Pilot 已表明直接检测、官方市场调查和食品成分数据库可以在文字中清楚描述可信度；现在再造一套 Cmp-A/Cmp-B 会增加复杂度。

### 不新增第二套 Directness 分数

D0–D4 已足够。只需要 `directness_note` 解释为什么。

### 不改变 M 分级

目前 M-IV 与 M-0 的区分有效，尤其适合阻止“现代指标 → 中医术语”的跳跃。

### 不修改 R2/R3 的数字预算

开心果 R2 和黑巧克力 R3 都能停下来；先等咖啡再测试真正极端的文献规模。

---

## 五、对 Research Skill 的小幅升级

建议正式写入 skill：

1. Identify 阶段可以修改 entry identity，并必须记录修改原因；
2. 多个 review/meta 结论一致时，检查底层研究是否高度重叠；
3. 对复合食品，先查 composition / real-world exposure，再判断有没有足够直接的人体 outcome；
4. 高质量提取物研究仍按 D 等级处理，不能因为样本大自动提高食品直接性；
5. 冷/热食用温度与本草寒热分开；
6. 传统母成分资料不能机械相加给复合食品。

---

## 六、是否可以继续后三个 Pilot

可以。

没有发现阻断性问题。建议顺序仍为：

1. 咖啡 R3 — 专门测试极高文献密度、timing 与 coffee/caffeine distinction；
2. 酸奶 R2 — 测试 fermentation、food vs strain、microbiome → 健脾映射；
3. 方便面 R2 — 测试 observational confounding、processing 与 nutrient-to-food inference。

咖啡完成后再看是否需要调整 R3 工作量；酸奶完成后再判断是否需要独立的 microbiome 规则；方便面完成后才决定是否需要对观察性食品暴露加更多固定字段。

---

## 七、Checkpoint 判定

- framework_status: pass
- R_system: keep
- D_system: keep
- E_system: keep
- M_system: keep
- stopping_rules: keep
- template_change: minor
- next_pilot: coffee

> 前三项 Pilot 的最大收获不是“证明这套方法正确”，而是证明它会在不同对象上得出不同类型的答案：有时结论强，有时只够类比，有时最重要的答案就是“直接证据没有这么多”。