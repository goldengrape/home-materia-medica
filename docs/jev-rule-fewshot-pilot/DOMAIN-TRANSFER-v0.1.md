# Domain Transfer v0.1 — 现有食材 Research Dossier → Jev

> task: RM-TASK-031  
> status: implementation  
> frozen judge: Jev v0.3.1 reasoning rules + five-shot + fixed questions

## 1. 目的

验证已经在中药 reasoning-complete 样本上跑通的 v0.3.1，能否迁移到《居家本草》真实现代食材资料。

本轮不再构造已知 gold answer。

测试对象直接来自项目 Pilot v1 已完成的 Research Dossier：

1. 开心果；
2. 黑巧克力；
3. 咖啡；
4. 酸奶；
5. 方便面。

## 2. 输入原则

### 使用

只使用现有 Research Dossier 已支持的信息：

- 食品身份与加工边界；
- 现代直接人体效应；
- 传统来源或近现代中药来源中与功能 / 主治有关的资料；
- 与理论映射有关但不直接等于答案的事实；
- 关键冲突和限制。

### 不使用

target document 不写入：

- dossier 已经给出的最终四气 / 五味标签；
- `M-0 暂不归经`、`M-IV` 等最终映射结论；
- Claim Ledger 中直接说“归某经 / 不归某经”的答案；
- 为了让 Jev 更容易得到预期结果而新增仓库外知识。

因此这是“从 dossier 事实 → Jev 映射”的测试，而不是让 Jev复述 dossier 的既有结论。

## 3. 为什么没有 accuracy

现代食品并不存在与药典中药一样的 gold 四气五味归经。

因此本轮只报告：

### A. Repeatability

同一文档重复 3 次：

- 四气 Choice 是否稳定；
- 五味 Noul 是否跨 0.5；
- 五脏归经 Noul 是否跨 0.5；
- 概率是否集中或接近边界。

### B. Boundary compatibility

把 Jev 输出与当前 dossier 已有的证据边界比较，不把 dossier 边界当成“真值”。

重点检查：

- 开心果：有传统功用和性味来源，但 dossier 明确警惕“功用 ≠ 归经”；
- 黑巧克力：疏肝仅 M-IV，归经 M-0；
- 咖啡：醒神 M-II，近现代资料存在，但归经 M-0；
- 酸奶：健脾仅 M-IV，现代酸奶归经 M-0；
- 方便面：燥热 / 生湿仅可按具体配方作 M-IV 类比，“伤脾胃 / 归经” M-0。

如果 Jev 在这些 M-0 场景给出非常高的某经概率，记录为 **over-mapping signal**，不是简单记“错”。

## 4. 冻结项

本轮不得修改：

- `run_pilot_v031.py` 中的 `REASONING_RULES`；
- v0.3.1 five-shot；
- 四气 / 五味 / 五脏 questions。

Domain test runner 直接加载 v0.3.1 代码和示例，避免复制后悄悄漂移。

## 5. 五个 target 文档

target 均为自然语言连续文本，直接由现有 dossier 压缩，不要求固定字段。

### DT01 开心果

保留传统“诸痢、去冷气、腰冷、肾虚痿弱、调中顺气”等功能语境与现代人体证据；不直接发送“辛温涩 / 甘”或“暂不归经”。

### DT02 黑巧克力

保留无传统直接母条、短期 mood / stress 人体信号、睡眠未证实、甲基黄嘌呤等边界；不发送“疏肝 M-IV / 归经 M-0”。

### DT03 咖啡

保留近现代资料“醒神、利尿、健胃”、芳香味苦，以及直接 alertness RCT、brewing method 等事实；不发送近现代资料中的“平”标签，也不发送“归经 M-0”。

### DT04 酸奶

保留现代普通活菌酸奶对 lactose maldigestion 的直接人体证据、发酵改变耐受、传统“酪”的润燥 / 利肠 / 止渴 / 补虚背景以及身份差异；不发送“甘酸微寒”“健脾 M-IV”“暂不归经”。

### DT05 方便面

保留高钠、调味 / 汤汁 / 油炸变量、GI 并非必然极高，以及高脂高能量/辣味/油腻只能产生类比、没有传统直接母条的事实；不发送“燥热 M-IV / 伤脾胃 M-0 / 暂不归经”。

## 6. 输出

不计算 accuracy。

保存：

- 3 次逐样本原生 Choice/Noul；
- 四气三次选择和 probability；
- 五味 / 五脏每项的 min / max；
- 0.5 跨界字段；
- 与 dossier boundary 的人工评注。

## 7. Stop Rule

本轮结果出来后，不根据这 5 个食品立即修改 v0.3.1 rules。

先判断问题属于：

1. source document 本身缺桥梁；
2. rules 不适合现代证据；
3. five-shot 只教会了传统主治语境；
4. Jev 本身过度映射；
5. 五字段输出契约本身造成信息损失。

若要修改 rules，另开 domain-transfer v0.2，并换或扩充测试集。
