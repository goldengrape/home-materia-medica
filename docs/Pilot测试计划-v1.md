# 《居家本草》Pilot 测试计划 v1

> 目标：先用少量差异明显的条目测试方法、Research Dossier、R/D/E/M、停止规则和后续写作接口，不追求代表全部目录。

## 一、Pilot 原则

第一轮只选 6 个样例。选择标准不是“最重要的六种食品”，而是“最能暴露方法问题的六种对象”。

要覆盖：

1. 文献极多；
2. 直接证据与成分证据容易混淆；
3. 复合食品；
4. 发酵与微生物；
5. 高度加工食品；
6. 相对单纯的整食物证据。

Pilot 期间允许修改：

- Research Dossier 字段；
- D0–D4 定义细节；
- E / M 实际操作说明；
- R1 / R2 / R3 工作量边界；
- Concept Trace 的最小字段；
- 停止规则；
- Claim Ledger 接口。

Pilot 期间不做：

- 批量研究整个目录；
- 批量正文生成；
- GitHub Pages / EPUB 构建；
- 重型自动化。

---

## 二、第一轮 6 个样例

### PILOT-001｜黑巧克力

- entry_id: dark-chocolate
- research_depth: R3

为什么选：

- “食品”与“可可”“可可黄烷”“表儿茶素”等证据容易偷换；
- 有情绪、心血管、代谢等多种研究方向，适合测试问题限界；
- 可以直接测试“现代情绪效应”与“疏肝 / 安神”等本草术语之间的映射距离；
- 黑巧克力、牛奶巧克力、白巧克力之间边界清楚，适合测试母子条目与加工差异。

第一轮核心问题：

1. 日常食用形态的黑巧克力有哪些较稳定的人体效应？
2. 黑巧克力与可可 / 黄烷提取物的证据应如何分开？
3. 情绪、主观愉悦或压力相关证据实际支持到什么程度？
4. 糖、脂肪、可可含量和份量怎样改变结论？
5. 哪些现代结果可进入本草映射，哪些只能停留在机制层？

主要压力测试：

- D0–D4
- E 与 M 分离
- 高文献量停止规则
- “疏肝”概念映射

---

### PILOT-002｜咖啡

- entry_id: coffee
- research_depth: R3

为什么选：

- 文献量巨大，非常适合测试“证据饱和”和停止规则；
- 咖啡与纯咖啡因的证据经常混用；
- 急性警觉、睡眠、长期队列结局属于不同时间尺度；
- 剂量、饮用时辰、烘焙、过滤方式、是否加糖奶都会影响实际对象。

第一轮核心问题：

1. 咖啡最可靠的急性人体效应是什么？
2. 咖啡与咖啡因哪些证据可以互相借用，哪些不能？
3. 饮用时间与睡眠 / 警觉之间有哪些较直接证据？
4. 对长期健康结局，本书应写到什么强度才不过度？
5. 什么情况下应停止继续追踪咖啡的巨大文献网络？

主要压力测试：

- R3 工作量上限
- evidence cutoff
- acute vs chronic
- dose / timing
- coffee vs caffeine identity

---

### PILOT-003｜珍珠奶茶（由“奶茶”在 Identity 阶段收窄）

- entry_id: pearl-milk-tea
- pilot_original_id: milk-tea
- research_depth: R2

为什么选：

- 是典型现代复合食品；
- 茶、奶、糖、珍珠、奶盖、咖啡因等成分证据不能简单相加；
- “奶茶本身”的直接人体研究可能远少于组成成分研究；
- 非常适合测试“证据稀少时要敢于停止”。

第一轮核心问题：

1. “奶茶”是否足够成为一个稳定条目？若不足，应收窄到什么对象？
2. 奶茶本身有哪些直接人体研究？
3. 茶、糖、乳、珍珠等间接证据最多能外推到什么程度？
4. 一杯的常见份量、糖量和咖啡因暴露如何进入判断？
5. 如果直接证据很少，应如何明确写 E-0 / E-C，而不是用成分机制填空？

主要压力测试：

- composite food identity
- sparse-evidence stopping rule
- D2 / D3 外推限制
- 实际份量

---

### PILOT-004｜酸奶

- entry_id: yogurt
- research_depth: R2

为什么选：

- 发酵使其与牛乳形成清楚的加工差异；
- “酸奶”“益生菌”“特定菌株”“发酵代谢物”容易混在一起；
- 肠道和代谢研究丰富，可测试“肠道效应 ≠ 自动健脾”的规则；
- 原味、加糖、高蛋白、希腊酸奶差异明显。

第一轮核心问题：

1. 酸奶作为整食物有哪些直接人体证据？
2. 一般酸奶与特定益生菌制剂的证据如何区分？
3. 发酵给食品身份和效应带来哪些可确认变化？
4. 原味 / 加糖 / 高蛋白等产品差异是否足以改变结论？
5. 肠道相关现代结果与“健脾”等概念之间的证据桥梁能走多远？

主要压力测试：

- fermentation
- food vs probiotic strain
- processing identity
- microbiome / TCM mapping

---

### PILOT-005｜方便面

- entry_id: instant-noodles
- research_depth: R2

为什么选：

- 代表高度加工、复合、真实生活中高频出现的食品；
- 营养组成很容易让研究者直接做“高钠 / 高脂 / 精制淀粉”的成分推断；
- 直接食品暴露研究多为观察性，适合测试混杂、饮食模式和生活方式问题；
- 也能检验“加工 = 有害”这种先入结论。

第一轮核心问题：

1. 方便面应作为怎样的复合食品定义？
2. 有哪些直接以方便面摄入为暴露的人体研究？
3. 观察性关联中，哪些混杂因素最关键？
4. 钠、脂肪、精制碳水等成分证据最多能支持什么？
5. 不同产品、汤料摄入与食用频率是否显著改变判断？

主要压力测试：

- ultra/processed food reasoning
- observational confounding
- direct food vs nutrient inference
- safety / dose / frequency

---

### PILOT-006｜开心果

- entry_id: pistachio
- research_depth: R2

为什么选：

- 是相对清楚的整食物对象，可作为前面复杂案例的“对照组”；
- 有一定营养与代谢人体研究，但不像咖啡那样无穷无尽；
- 原味、盐焗、糖衣等加工变体容易定义；
- 可以测试一个普通坚果条目是否能在合理工作量内稳定完成。

第一轮核心问题：

1. 开心果作为整食物有哪些较稳定的人体效应？
2. 研究剂量与现实份量是否接近？
3. 坚果整体研究能否外推到开心果，证据距离是多少？
4. 盐焗、糖衣等加工何时需要拆成独立子条？
5. 在传统直接母本较弱时，本草映射是否应保持 M-IV / M-0？

主要压力测试：

- standard R2 workload
- whole-food evidence
- family-level extrapolation
- processing variants
- sparse traditional mapping

---

## 三、为什么暂不把其他候选放进第一轮

### 无糖可乐

很适合测试甜味剂与饮料整体之间的关系，但与奶茶在“复合饮品 + 成分外推”上部分重叠。可作为第二轮。

### 蛋白粉

很适合测试“食品 / 补充剂”边界和运动营养，但第一轮已有足够多不同方法问题，可在 Pilot v2 加入。

### 火锅

非常适合生活场景 / 食方，但它同时涉及大量组合、时长、行为与社会场景变量。建议等单品 Research Dossier 跑通后，再把它作为 Scene Pilot。

### 康普茶

很适合发酵与安全性，但和酸奶在第一轮的“发酵压力测试”有一定重叠。若酸奶不足以暴露问题，再换入康普茶。

---

## 四、执行顺序

建议不是按目录顺序，而是按方法学风险：

1. **开心果**：先跑一个相对干净的 R2，检查基础流程是不是过重；
2. **黑巧克力**：测试 D0–D4 和 E/M；
3. **奶茶**：测试证据稀少和复合食品；
4. **咖啡**：测试 R3 与停止规则；
5. **酸奶**：测试发酵、微生物和中医映射；
6. **方便面**：测试观察性研究、加工食品和混杂。

如果前 3 个已经暴露出结构性问题，应先修凡例 / skill，再继续后 3 个。

---

## 五、Pilot 成功标准

第一轮不是看“写出了六篇漂亮文章”，而是看：

- Research Dossier 是否足够但不过度；
- D0–D4 是否能稳定区分直接与间接证据；
- E 是否能按 outcome 稳定工作；
- M 是否能阻止过快的中医映射；
- Concept Trace 是否够用；
- R1/R2/R3 是否真的能控制工作量；
- 停止规则是否能让咖啡类题目停下来；
- 稀疏证据是否能自然得到 E-0 / M-0；
- Claim Ledger 是否足以支持后续正文；
- 六类不同对象是否都能在同一套框架中处理。

达到这些条件后，才进入更大规模的条目研究。


---

## 六、执行记录

### 2026-09-23｜PILOT-006 / 开心果 R2

状态：**research_ready**

产物：

- `references/entries/pistachio/research.md`
- `qa/pilot/pistachio-r2.md`

关键发现：

1. 传统资料强于 Pilot 预设：阿月浑子 / 必思答有明确古籍记录。
2. 有传统功用记录，但不等于有明确归经；当前仍“暂不归经”。
3. 多篇 Meta-analysis 高度共享同一批 RCT，不能按篇数重复计票。
4. 综述截止后的 2024 阴性 RCT 与 2025 阳性 RCT 显示糖代谢效应明显依赖人群、时机和对照。
5. R2 研究预算和证据饱和规则在本条目上基本可用。


### 2026-09-23｜PILOT-002 / 黑巧克力 R3

状态：**research_ready**

产物：

- `references/entries/dark-chocolate/research.md`
- `qa/pilot/dark-chocolate-r3.md`

关键发现：

1. 高质量、大样本试验若研究的是可可提取物，仍然只是黑巧克力的 D2 证据。
2. 最新系统综述也可能混合 dark chocolate 与 cocoa extract，必须检查纳入对象。
3. 短期 mood / stress 研究有正信号，但不足以把“疏肝解郁”提升到确定功效。
4. “安神”缺乏直接支持，归经也无可靠依据。
5. R3 只围绕核心问题工作，可以在 cocoa/chocolate 的巨大文献量中达到停止条件。

### 2026-09-23｜PILOT-003 / 珍珠奶茶 R2

状态：**research_ready / sparse_evidence**

产物：

- `references/entries/pearl-milk-tea/research.md`
- `qa/pilot/pearl-milk-tea-r2.md`

关键发现：

1. 泛称“奶茶”不是稳定研究对象，已收窄为“珍珠奶茶”。
2. 现代复合食品中，直接组成与实际暴露证据可以很强，而长期疾病因果证据仍是 E-0。
3. 一般 sugar-sweetened beverage 研究对珍珠奶茶属于 D2，只能提供风险背景。
4. 少糖、去珍珠、杯量等定制变量可实质改变暴露，适合纳入现代“炮制/加工”框架。
5. 冰饮温度不能直接等同本草“性寒”；高糖高脂也不能直接翻译为“生湿”。
6. sparse-evidence stop 成功阻止了用糖、茶多酚、咖啡因等成分文献填补不存在的食品直接证据。
### 2026-09-23｜前三项 Pilot 方法 checkpoint

状态：**pass**

详见：`qa/pilot/first-three-review.md`

决定：

- 保留 R1/R2/R3；
- 保留 D0–D4；
- 保留 E-A–E-0；
- 保留 M-I–M-0；
- 保留 saturated / sparse_evidence 等停止状态；
- Research Dossier 增加 Identity Revision、Composition & Exposure、Evidence-base overlap、directness note；
- research skill 增加复合食品 composition-first 与食用温度/本草寒热分离规则；
- 下一项继续咖啡 R3。
### 2026-09-23｜PILOT-004 / 咖啡 R3

状态：**research_ready / shared research parent**

产物：

- `references/shared/coffee-base/research.md`
- `qa/pilot/coffee-r3.md`

关键发现：

1. 泛称“咖啡”不应成为纸书单条，但适合作为多个具体咖啡条目的共享 Research Parent。
2. 咖啡与纯咖啡因必须分别标 D；高质量 caffeine RCT 不能原样替代 coffee。
3. boiled/unfiltered vs paper-filtered 的血脂差异提供了“加工/炮制改变作用”的强 D0 人体例证。
4. 长期较低慢病/死亡风险主要来自 observational association；MR 对 CVD 等因果关系并未同样支持。
5. 近现代中药资料“醒神”与直接 alertness RCT 可形成 M-II 候选；归经仍 M-0。
6. R3 通过严格限制核心问题，可以在咖啡海量文献中达到停止条件。
### 2026-09-23｜PILOT-005 / 酸奶 R2

状态：**research_ready / saturated**

产物：

- `references/entries/yogurt/research.md`
- `qa/pilot/yogurt-r2.md`

关键发现：

1. 活菌标准酸奶改善 lactose maldigestion 人群对酸奶中乳糖的消化，可到 E-A。
2. 特定 probiotic strain 的产品结果不能自动继承给普通酸奶，通常至少 D2。
3. 直接 microbiome 研究更多支持短暂检测到 yogurt-derived bacteria，而不是广泛持久“重塑菌群”。
4. 即使 lactose digestion 是 E-A，“健脾”仍最多 M-IV：乳糖酶缺乏不等于脾虚证。
5. 古代“酪”可作为传统发酵乳母本，但不是现代标准 yogurt 的同一制品。
6. 发酵 + 活菌构成强有力的“现代炮制改变耐受性”案例。
### 2026-09-23｜PILOT-006 / 方便面 R2

状态：**research_ready**

产物：

- `references/entries/instant-noodles/research.md`
- `qa/pilot/instant-noodles-r2.md`

关键发现：

1. 多个韩国大样本研究反复观察到高频摄入与代谢风险相关，但主要为横断面，长期因果 claim 仍 E-0。
2. 方便面的钠、油炸/非油炸脂肪、调味包与汤汁暴露，可以用直接 composition evidence 很清楚地研究。
3. generic noodle Mendelian randomization 不是 instant-noodle-specific D0，不能因方法高级而越过直接性。
4. ramyeon 的 GI 并非必然极高；实际份量与 glycemic load 比单看 GI 更重要。
5. 少调味、少喝汤属于能实质改变暴露的“服食法/后端炮制变量”。
6. “燥热/湿热”最多 M-IV，“伤脾胃”和归经 M-0。
7. 第一轮六项 Pilot 至此全部完成，下一步进入总复盘。