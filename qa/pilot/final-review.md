# Pilot v1 总复盘

> checkpoint: RM-TASK-027  
> 日期：2026-09-23  
> 样例：开心果 / 黑巧克力 / 珍珠奶茶 / 咖啡 / 酸奶 / 方便面

## 一、总判定

**Pilot v1：通过。**

六个样例覆盖了足够不同的研究生态，没有发现需要推倒重来的框架性问题。

正式冻结：

- R1 / R2 / R3 研究深度；
- D0–D4 证据距离；
- E-A–E-0 现代人体效应等级；
- M-I–M-0 本草映射等级；
- saturated / sparse_evidence 等停止逻辑；
- 研究与正文分离；
- Concept Trace；
- 公开参考资料、读者自行复核。

需要正式吸收的只有少量结构改进：

1. `research_parent` 共享研究母页；
2. `claim_mode`，防止 association / composition 被写成 effect；
3. Identity Revision；
4. Composition-first；
5. Evidence-base overlap；
6. 消费者最终调味、过滤、去料、喝汤等“服食法”作为可改变暴露的加工变量。

---

## 二、六个样例各自证明了什么

| 样例 | 主要压力 | 最终状态 | 最重要结论 |
|---|---|---|---|
| 开心果 R2 | 整食物 RCT + 传统来源 | saturated | 传统证据比预想强；功用不等于归经；Meta 会高度重叠 |
| 黑巧克力 R3 | whole food vs extract vs ingredient | saturated_for_R3_core_questions | 大样本 extract 仍可只是 D2；mood E-C 不能直接变疏肝 |
| 珍珠奶茶 R2 | 复合食品、直接结局稀少 | sparse_evidence | Identity 可被推翻；composition 强而 disease causality 仍 E-0 |
| 咖啡 R3 | 文献海量、多个具体子条 | saturated_for_R3_core_questions | 需要 research parent；过滤方式直接改变 LDL effect；醒神可到 M-II |
| 酸奶 R2 | fermentation / probiotic / microbiome | saturated | 活菌乳糖消化 E-A，但健脾仍 M-IV；specific strain 不能冒充普通酸奶 |
| 方便面 R2 | 加工食品 + 观察性混杂 | saturated_for_R2_available_evidence | 横断面大样本仍不是因果；调味包/汤汁改变暴露；加工食品不等于必然有害 |

---

## 三、框架经受住的关键压力测试

### REVIEW-FINAL-001｜E 强，不代表 M 强

最强例子是酸奶：

- 活菌酸奶改善 lactose digestion：E-A；
- “健脾”：M-IV。

这说明现代人体效应与中医解释必须继续独立。

### REVIEW-FINAL-002｜研究越高级，不代表越接近食品

- COSMOS cocoa extract：大样本长期 RCT，但对黑巧克力仍 D2；
- caffeine capsule sleep RCT：设计直接，但对 coffee 仍 D3；
- generic noodle MR：统计方法高级，但对 instant noodles 不是 D0。

D0–D4 必须永久保留。

### REVIEW-FINAL-003｜Composition 与 Effect 是两种不同的知识

珍珠奶茶和方便面都显示：

- 糖、钠、咖啡因、份量、油炸方式可以很确定；
- 长期疾病因果却可能完全不确定。

因此不能因为组成很清楚，就把疾病效应写成确定。

### REVIEW-FINAL-004｜加工不是一个标签，而是因果变量

至少有三个强例子：

- coffee paper filtration → diterpene exposure / LDL effect 改变；
- yogurt fermentation + live cultures → lactose digestion 改变；
- instant noodles seasoning/soup handling → sodium exposure 改变。

《居家本草》的“炮制”应覆盖：

1. 工业加工；
2. 厨房制备；
3. 消费者最后一步定制与食用法。

### REVIEW-FINAL-005｜停止规则同时适用于“太多”和“太少”

- 黑巧克力、咖啡：文献太多时按核心问题停止；
- 珍珠奶茶：直接证据太少时按 sparse-evidence stop 停止。

停止不是“论文搜完”，而是“继续搜不再改变当前版本正文”。

### REVIEW-FINAL-006｜传统资料必须按时代分层

六项里出现三种情况：

- 开心果：有古代直接记录；
- 酸奶：有近似传统母本“酪”，但非同一标准制品；
- 咖啡：只有近现代中药资料，不应伪装成古代本草；
- 黑巧克力/珍珠奶茶/方便面：基本属于现代食品。

因此“传统有无依据”不是二元字段，而要保留时代和身份对应。

---

## 四、正式新增：Research Parent

### 定义

`research_parent` 是**不直接发布给读者**、用于多个正式条目共享证据的研究节点。

典型例子：

- `coffee-base` → espresso / Americano / pour-over / cold brew / decaf；
- 未来可能有 `cocoa-base`、`tea-base`，但只有真正减少重复研究时才建立。

### 规则

- publish: false；
- 放在 `references/shared/<id>/research.md`；
- 子条引用母页时必须重新判断 D；
- research parent 不能因为“共用”而覆盖子条自己的加工/配方差异；
- 不为了抽象漂亮而大量建立 parent。

---

## 五、正式新增：Claim Mode

Pilot 反复出现“事实类型被写错语气”的风险。

Claim 建议增加：

```yaml
claim_mode: effect | association | composition | safety | traditional | mapping
```

### effect

干预/因果效应命题，例如：

> 活菌酸奶改善特定人群对酸奶中乳糖的消化。

### association

观察性关联，例如：

> 中等咖啡摄入与较低某些疾病风险相关。

不得在写作层自动转换成“预防”。

### composition

真实组成/暴露，例如：

> 某类珍珠奶茶一杯可含数十克糖。

不需要硬塞 E 等级。

### safety

过敏、相互作用、钠/咖啡因暴露等安全命题。

### traditional

历史文献确有的性味、功用、制法。

### mapping

现代拟性味、拟食效、拟归经等 M 命题。

---

## 六、正式新增：消费者端“服食法”变量

Pilot 显示最终入口暴露不仅由厂家决定。

必须记录：

- coffee 是否 paper-filter；
- 奶茶少糖/去珍珠；
- 方便面使用多少 seasoning / 是否喝汤；
- 食用时辰；
- 一次份量；
- 与其他食物的替代关系。

因此项目里的“炮制/加工”应理解为：

> 从原料到入口之前，所有足以改变实际暴露和作用的处理。

这比只把“油炸、发酵、烘焙”叫炮制更完整。

---

## 七、暂时不新增的复杂度

### 不新增 Composition-A/B/C 等级

直接食品检测、官方市场调查、商品标签的可信度可以用来源类型和 D 描述，暂时没必要再造一个等级。

### 不新增 Microbiome 等级

保留现有禁止推断：

> microbiome change ≠ clinical benefit ≠ 健脾。

### 不为每种食品建立 research parent

只有实际存在大量共享证据、能够明显减少重复工作时才建立。

### 不新增“传统身份距离”第二套 D

传统母本关系继续用文字说明物种、制法、时代与对应问题，不复制现代 D 系统。

---

## 八、Pilot 暴露出的写作接口要求

下一阶段 writing skill 至少要做到：

1. 读取 Claim Ledger，不直接读论文后自由发挥；
2. 尊重 `claim_mode`：association 不能变 prevention；
3. 尊重 allowed wording；
4. M-IV 必须保持推测语气；
5. M-0 不得为了条目完整而补归经；
6. Composition 可以写得很具体，但不能偷偷转成 health effect；
7. 传统文献按时代标注；
8. 允许“这个问题目前不知道”成为正文内容。

---

## 九、是否进入批量研究

**还不进入。**

Pilot 证明研究方法可用，但项目路线中仍有两个基础治理任务没有正式完成：

- RM-TASK-010：中医概念骨架；
- RM-TASK-011：正式机器可读 Entry Registry。

建议下一步：

1. 根据六个 Pilot 实际使用到的术语，建立第一批 Concept Trace，而不是先写 25 个抽象概念；
2. 建 `catalog/entries.yaml`，先纳入六个 Pilot、coffee 子条和其直接相关条目；
3. 然后进入 RM-PHASE-030 正文 Pilot，优先写开心果、黑巧克力、珍珠奶茶三种不同证据生态的样章；
4. 样章稳定后再设计 `home-materia-writing` skill。

---

## 十、Pilot v1 最终判定

```yaml
pilot_version: v1
status: passed
samples_completed: 6
framework:
  R: keep
  D: keep
  E: keep
  M: keep
  stopping_rules: keep
new_structures:
  - research_parent
  - claim_mode
  - identity_revision
  - composition_exposure
  - evidence_base_overlap
  - consumer_side_processing
next:
  - tcm_concept_skeleton
  - entry_registry
  - writing_pilot
```

> 六个 Pilot 最终证明的，不是“本草语言可以给所有现代食品找到答案”，恰恰相反：这套方法的价值在于它能稳定地区分——哪些可以较强地说，哪些只能类比，哪些应当明确说不知道。