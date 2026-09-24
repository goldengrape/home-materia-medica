# Research Dossier — 咖啡基础研究母页

> entry_id: coffee-base  
> pilot_original_id: coffee  
> entry_type: research_parent  
> research_depth: R3  
> status: research_ready  
> publication_status: not_a_direct_book_entry  
> evidence_cutoff: 2026-09-23  
> last_updated: 2026-09-23

## 1. Identity Revision

原 Pilot 使用 `coffee / 咖啡`。研究后认为它不适合作为纸书唯一主条目，因为正式目录已区分意式浓缩、美式、手冲、冷萃、氮气冷萃、拿铁、燕麦拿铁、速溶、三合一、无咖啡因咖啡等。

但大量现代证据只记录 generic coffee consumption，因此“咖啡”非常适合作为后台共享研究节点。

Identity Revision：

- changed: yes
- original_entry_id: coffee
- revised_entry_id: coffee-base
- revised_type: research_parent
- reason: generic epidemiology and core physiology are shared across many coffee child entries, while preparation/additions materially modify exposure
- catalog_action: keep specific book entries; add non-published research parent for shared evidence reuse

### 子条继承原则

可以从 coffee-base 继承：

- 咖啡因的一般急性作用背景；
- generic coffee prospective association background；
- 咖啡冲煮方式的重要变量；
- 咖啡因安全上限背景。

不能无条件继承：

- unfiltered coffee 的 LDL effect 给 paper-filtered hand brew；
- black coffee 数据给拿铁/三合一；
- caffeinated coffee 的 alertness 给 decaf；
- generic cohort 的 cup/day 直接给 espresso shot 或 cold brew 的精确剂量。

每个子条仍需重新标 D。

## 2. 研究对象

本母页把对象定义为：

> 不加糖奶的 brewed coffee，以含咖啡因为默认；冲煮方式与 caffeine dose 作为核心变量。无咖啡因、奶咖和复合咖啡作为子条/邻接条目。

### Composition & Exposure

关键真实暴露：

- caffeine：不同豆种、份量、萃取方式差异很大；
- diterpenes（cafestol/kahweol）：unfiltered 高，paper-filtered 很低；
- chlorogenic acids 等非咖啡因成分：受烘焙和萃取影响；
- serving size：cup 在队列研究里并非统一体积。

EFSA 的代表性估计给出约 200 mL filter coffee ~90 mg caffeine、60 mL espresso ~80 mg，但实际商品差异明显。

## 3. 核心问题

1. 一杯实际咖啡对警觉、注意、疲劳有哪些直接人体效应？
2. 咖啡与纯 caffeine 的证据哪些可以共用、哪些必须分开？
3. 饮用剂量与时辰怎样影响睡眠？
4. 冲煮方式是否足以改变健康效应，尤其是血脂？
5. 长期队列中“咖啡与较低疾病/死亡风险”的关联能写到什么强度？
6. 中医药资料中咖啡究竟是古代本草、近现代本草，还是现代类比？
7. 何时可以停止咖啡的巨大文献网络？

## 4. 检索策略与停止边界

R3 不按疾病名称穷举全部咖啡文献，而只围绕七个核心问题。

本轮使用：

- umbrella review 建长期 outcome evidence map；
- 2020 NEJM 综合评述作为跨领域更新导航；
- 直接 coffee RCT 处理 alertness 与 brewing method；
- caffeine timing RCT 作为 D3 睡眠证据；
- Mendelian randomization 用来红队观察性“保护效应”；
- FDA/EFSA 处理 caffeine safety；
- 现代中药资料处理咖啡的中医来源层次。

不继续逐病搜索癌症、帕金森、痛风、胆石等几十个 outcome；这些如未来正文需要，再从母页向特定 claim 展开。

## 5. 传统与近现代中医药来源

### 5.1 古代本草

本轮没有发现明清以前中国本草中对现代 coffee bean / coffee beverage 的可靠直接条目。咖啡进入中国日常与农业体系明显较晚，因此不应把现代中医师的性味推演伪装成古代共识。

### 5.2 近现代中药资料

公开可查询的《中华本草》转录资料把咖啡定义为茜草科小果咖啡、中果咖啡、大果咖啡的种子，并记：

- 性味：微苦、涩、平；
- 功能：醒神、利尿、健胃；
- 主治方向：精神倦怠、食欲不振等。

公开转录同时引《广西中药志》：“芳香，味苦”；并记“有兴奋利尿作用，经炒焙过的咖啡可助消化”。

来源层级必须写清楚：这些是**近现代中药文献**，不是古代本草。

当前公开入口：

- 国医小镇/中华本草转录：http://tcm360.cn/zycd/detail/yaocaitupu-44484.html
- 另一《中华本草》转录：https://zhongyaocai360.com/k/kafei.html

重要限制：本轮没有直接核到《中华本草》《广西中药志》纸本页码，因此正文引用时应标为“公开转录待版本页码补齐”，不能把网页本身当成古籍。

## 6. 现代证据地图

| Claim / Outcome | 主要证据 | D | 结论类型 | E |
|---|---|---:|---|---|
| 含咖啡因咖啡短期提高主观警觉、降低疲劳，并可改善部分简单注意任务 | direct coffee crossover RCT | D0 | 直接人体效应 | E-B |
| 咖啡对复杂任务表现的提升并不稳定 | direct coffee RCT | D0 | 情境依赖 | E-C |
| 晚间/高剂量 caffeine 会扰乱睡眠 | caffeine timing RCT | D3 | 对咖啡的成分级强背景 | E-C for coffee-specific claim |
| unfiltered/boiled coffee 可提高 TC/LDL，paper filter 大幅削弱该效应 | controlled coffee trials + trial meta | D0 | 冲煮方式特异 | E-A |
| 3–5 cups/day 与较低全因死亡、T2D、肝病等风险相关 | prospective meta/umbrella | D0 exposure, observational | 稳定关联而非因果 | E-B association / E-C causal inference |
| 咖啡可预防 CVD | observational inverse association vs MR null | D0 | 因果未证 | E-0 for prevention claim |
| 一般健康成人中适量 caffeine 通常可耐受 | EFSA/FDA risk assessment | D3 component + real coffee exposure | safety background | safety |
| “醒神”作为现代本草语言 | modern materia record + direct alertness human effect | D0 modern function | 本草映射 | M-II |
| 明确归某经 | 未找到可靠直接资料 | — | 不足 | M-0 |

## 7. Evidence-base overlap

- level: high for long-term observational summaries
- note: 大量 umbrella/meta 会重复纳入相同大型 prospective cohorts；不能以综述篇数重复计票。

对于长期疾病，真正有意义的是：

- 关联是否跨队列一致；
- 是否存在剂量形态；
- decaf 是否类似；
- smoking / reverse causation 是否充分处理；
- MR / 其他 causal inference 是否支持。

## 8. 核心证据卡

### COF-SRC-001｜Coffee health umbrella review

- citation: Poole R, et al. BMJ. 2017;359:j5024.
- doi: 10.1136/bmj.j5024
- design: umbrella review
- search_cutoff: 2017-07
- evidence: 201 meta-analyses of observational research / 67 unique outcomes; 17 meta-analyses of interventional research / 9 outcomes
- main pattern: coffee more often associated with benefit than harm; many observational curves lowest around 3–4 cups/day
- limitation: long-term evidence overwhelmingly observational; residual confounding and reverse causation remain
- directness: D0 for generic coffee exposure, but cup definition/preparation heterogeneous
- supports: stable association map
- does_not_support: recommending coffee to prevent disease
- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC5696634/

### COF-SRC-002｜NEJM synthesis

- citation: van Dam RM, Hu FB, Willett WC. N Engl J Med. 2020;383:369-378.
- doi: 10.1056/NEJMra1816604
- pmid: 32706535
- design: expert evidence review
- key distinction: coffee is not caffeine; coffee contains many compounds with potentially opposing effects
- key practical points: filtered vs unfiltered matters; moderate habitual intake not associated with higher CVD/cancer risk; evidence does not warrant recommending coffee for disease prevention
- url: https://www.nejm.org/doi/full/10.1056/NEJMra1816604

### COF-SRC-003｜Direct coffee cognition/mood RCT

- citation: Haskell-Ramsay CF, et al. Nutrients. 2018;10(10):1386.
- doi: 10.3390/nu10101386
- design: randomized double-blind counterbalanced crossover
- population: 29 young adults + 30 older adults
- intervention: 220 mL regular brewed coffee with 100 mg caffeine
- comparator: decaf coffee ~5 mg caffeine and coffee-flavored placebo
- result: regular coffee increased alertness, reduced some reaction times, improved digit-vigilance accuracy vs decaf; decaf also increased subjective alertness vs placebo
- directness: D0
- limitations: acute laboratory outcomes; not every cognitive endpoint improved
- supports: short-term alertness/attention claim

### COF-SRC-004｜Realistic-task coffee RCT

- citation: van Bergen G, et al. 2024 preregistered double-blind randomized repeated-measures study
- intervention: ~98 mg caffeine regular coffee vs ~5 mg decaf, 125 mL
- population: 35 civil pilots
- result: no vigilance benefit in simple or multitask environments; some simple selective-attention accuracy benefit; sleepiness attenuation signals
- directness: D0
- importance: alertness/performance effect depends on task and context
- doi: 10.18174/683400

### COF-SRC-005｜Caffeine timing and sleep, 2013

- citation: Drake C, et al. J Clin Sleep Med. 2013;9:1195-1200.
- doi: 10.5664/jcsm.3170
- pmid: 24235903
- intervention: 400 mg caffeine pill at 0, 3, or 6 h before bedtime
- result: objective sleep disrupted even at 6 h
- evidence_distance: D3
- directness_note: isolated high-dose caffeine, not coffee; useful for timing mechanism/safety, not exact cup-level effect

### COF-SRC-006｜Dose × timing sleep RCT, 2025

- citation: Gardiner CL, et al. Sleep. 2025;48(4):zsae230.
- doi: 10.1093/sleep/zsae230
- n: 23 men
- intervention: 100 or 400 mg caffeine capsules at 12, 8, 4 h before bed
- result: 100 mg showed no significant sleep effect in tested intervals; 400 mg altered sleep when taken within 12 h, with larger effects closer to bedtime
- evidence_distance: D3
- importance: dose and timing interact; a universal 'no coffee after X pm' rule is too crude

### COF-SRC-007｜Filtered vs boiled coffee RCT

- citation: Bak AAA, Grobbee DE. N Engl J Med. 1989;321:1432-1437.
- doi: 10.1056/NEJM198911233212103
- n: 107
- intervention: 4–6 cups/day boiled vs filtered vs no coffee
- duration: 9-week intervention after run-in
- result: boiled coffee raised total cholesterol by about 0.48 mmol/L vs filtered; filtered did not differ significantly from no coffee
- directness: D0
- supports: brewing method can materially change physiological effect

### COF-SRC-008｜Coffee/lipids trial meta-analysis

- citation: Jee SH, et al. Am J Epidemiol. 2001;153:353-362.
- pmid: 11207153
- design: meta-analysis of controlled coffee trials
- finding: unfiltered/boiled coffee raised total and LDL cholesterol more; filtered coffee produced little increase
- directness: D0

### COF-SRC-009｜Coffee and CVD Mendelian randomization

- citation: Yuan S, et al. Nutrients. 2021;13:2218.
- doi: 10.3390/nu13072218
- design: Mendelian randomization using UK Biobank/FinnGen outcomes
- result: limited evidence that genetically predicted higher coffee consumption causally affects 15 cardiovascular outcomes
- role: red-team observational inverse associations
- limitation: MR instruments and linear assumptions do not perfectly represent changing real-world coffee intake
- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC8308456/

## 9. 分结局综合

### Outcome A｜警觉、注意与疲劳

直接 coffee RCT 支持含咖啡因咖啡短期提高主观 alertness、降低 tiredness，并改善部分简单注意/反应任务。但更复杂或现实 multitask 的 performance 改善并不稳定。

值得注意的是 decaf 在部分研究中也改善主观 alertness，提示：

- 期待/感官条件；
- 非咖啡因成分；
- caffeine withdrawal reversal；

都可能参与。

**E-B：短期主观警觉与部分简单 attention outcome。**

**E-C：复杂工作表现的普遍提升。**

允许：

> 一杯含咖啡因咖啡通常能短时提高警觉、减少困倦，但并不保证所有复杂认知任务都表现更好。

不允许：

> 咖啡提高智力或全面增强认知。

### Outcome B｜睡眠与时辰

直接、高质量的 dose × timing 证据主要来自 isolated caffeine，因此对咖啡是 D3。

这些试验清楚证明：

- dose 很重要；
- timing 很重要；
- 个体感知可能低估客观 sleep disruption；
- 400 mg 一次性高剂量远不能等同普通单杯咖啡。

**咖啡特异正向/负向 sleep claim：E-C**，因为主要因果证据来自 D3 caffeine。

正文应写：

> 咖啡对睡眠的影响更适合按“咖啡因剂量 × 距离睡眠时间 × 个体敏感性”理解，而不是给所有人规定同一个晚间禁饮时刻。

### Outcome C｜冲煮方式与血脂

这是咖啡证据里最接近明确因果的一块。

多项 controlled trials 一致显示：

- boiled / unfiltered coffee 可提高 TC/LDL；
- paper filtration 大幅去除相关脂溶性 diterpenes；
- filtered coffee 的升胆固醇作用很小或不明显。

**E-A：高量 unfiltered vs paper-filtered 对血脂的方向性差异。**

这个结论直接说明：

> “咖啡的食性/效应”不能脱离加工方式讨论。

### Outcome D｜长期死亡、CVD、T2D、肝病等

prospective observational literature 非常庞大，且多个 meta/umbrella 在许多 outcome 上观察到 U/J 型或 inverse associations，常见低风险区间约 3–5 cups/day。

但 causal inference 没有同样整齐：

- MR 对 CVD 等多个 outcome 多为 null / inconclusive；
- long-term randomized disease-endpoint trial 基本不存在；
- decaf 与 caffeinated 常有相似 association，说明不能只归因于 caffeine。

因此必须拆成两个 claim：

**“长期咖啡摄入与较低若干疾病/死亡风险相关”——E-B（association）。**

**“咖啡预防这些疾病”——E-0 / E-C，不足以确立因果。**

本书正文应使用“与……较低风险相关”，不写“预防”。

### Outcome E｜急性血压

caffeine 与 coffee 的 acute pressor effect 会受 habitual use、剂量、人群和 comparator 影响。部分 hypertensive/nonhabitual 研究可见短时 BP 上升；habitual coffee trial 未必出现显著差异。

这再次说明 caffeine pill 不能直接替代 coffee。

当前不作为正文主功效，只放宜慎与剂量语境。

## 10. 安全性

### Caffeine 总量

FDA 与 EFSA 都把一般健康成人约 400 mg/day caffeine 作为通常不引发安全担忧的数量级，而个体敏感性差异明显。

EFSA：

- single dose up to 200 mg：一般健康成人通常无安全担忧；
- daily up to 400 mg：一般健康成人通常无安全担忧；
- pregnancy：up to 200 mg/day from all sources。

这些是总 caffeine，不是“咖啡杯数”，因为一杯 caffeine 差异很大。

### Sleep / anxiety / jitteriness

咖啡因敏感者、晚间、高剂量或低耐受人群更容易出现：

- insomnia / sleep disruption；
- jitteriness；
- anxiety-like symptoms；
- palpitations。

### Pregnancy

本条只引用权威 caffeine guidance，不把一般成人的 400 mg/day 套给孕期。

### Withdrawal / habituation

habitual caffeine use 可形成 tolerance 与 withdrawal。若研究要求短期禁咖啡，实验中的“获益”可能部分是解除 withdrawal，而非从中性基线提升。

这也是 alertness literature 的重要解释变量。

## 11. 机制与成分

保留到足够解释现象即可：

- caffeine：adenosine receptor antagonism，与 alertness / sleep 最相关；
- cafestol / kahweol：解释 unfiltered coffee 与 LDL；
- chlorogenic acids 等：可能参与代谢与血管效应。

停止追踪：

- 每个 polyphenol pathway；
- 每个 microbiome taxon；
- 每种 roast-generated molecule。

因为不会改变当前 E/M。

## 12. 本草映射

### 候选 A｜醒神

支持链：

1. 近现代《中华本草》公开转录明确用“醒神”；
2. direct coffee RCT 显示短时 alertness ↑、tiredness ↓、部分 attention 改善；
3. 食品对象与现代日常咖啡较接近。

限制：

- 这不是古代咖啡本草传统；
- “醒神”工作定义仍需进入 concepts 统一；
- 复杂 cognitive performance 并非普遍改善。

**M-II：可作为较强的现代本草功能映射候选。**

建议正文措辞：

> 若用现代本草语言概括，咖啡最有根据的一项是“醒神”：这一说法既见于近现代中药资料，也与直接人体警觉研究相符。

### 候选 B｜利尿

近现代中药资料有“利尿”；caffeine 有肾脏/尿量相关人体药理背景，但 habitual tolerance、液体摄入等使日常咖啡情境更复杂。

本轮不作为核心 M 结论，暂列 M-II/M-III 边界，待未来 Concept Trace。

### 候选 C｜健胃

现代中药资料有“健胃 / 炒焙助消化”的记录，但本轮没有建立对应的人体 clinical function evidence。

**M：traditional-modern record only；现代拟证据不足。**

### 归经

本轮可核的近现代资料转录没有提供可靠、可追溯的明确归经。网络上常见“苦入心”“红入心黑入肾”“咖啡归心肺”等推理，正属于项目禁止的机械类推。

**M-0：暂不归经。**

## 13. 冲突与未知

### 主要冲突

1. observational long-term benefit 与 MR causal evidence 并不完全一致；
2. caffeine pill 的 acute BP/sleep effect 往往强于现实单杯 coffee；
3. generic coffee cohort 不记录冲煮方式，而 controlled trials 明确显示 brewing method 可改效果；
4. cup/day 不是标准药理剂量；
5. modern materia medica record 与网络五味归经推演必须分开。

### 仍未知

- 特定 brewing child entry 能继承 generic cohort evidence 到什么程度；
- cold brew / espresso / Americano 的 caffeine exposure 如何在实际商品层标准化；
- 长期 observational inverse associations 多少是 causal；
- “醒神”的项目 Concept Trace 最终工作定义。

### 不应声称

- 咖啡预防心血管病 / 糖尿病 / 癌症；
- 所有咖啡都降风险；
- 咖啡因研究就是咖啡研究；
- 一杯咖啡固定等于 100 mg caffeine；
- 咖啡“苦入心”所以归心经；
- 冰咖啡性寒、热咖啡性热；
- 深焙一定更热、浅焙一定更寒，除非有独立证据链。

## 14. Claim Ledger

| ID | 正文候选命题 | 允许措辞 | E/M | D |
|---|---|---|---|---|
| coffee-base-CLM-001 | 含咖啡因咖啡短时提高警觉 | 通常提高主观警觉、减少困倦，部分简单注意任务改善 | E-B | D0 |
| coffee-base-CLM-002 | 咖啡全面提升复杂工作能力 | 证据不稳定，不应泛化 | E-C | D0 |
| coffee-base-CLM-003 | caffeine dose/timing 影响睡眠 | 高剂量、接近睡眠更易扰乱；精确 cutoff 不能简单按一杯咖啡外推 | E-C coffee-specific | D3 |
| coffee-base-CLM-004 | unfiltered coffee 提高 LDL/TC | 高量 boiled/unfiltered 相对 paper-filtered 有明确升脂效应 | E-A | D0 |
| coffee-base-CLM-005 | 中等咖啡摄入与较低多种慢病/死亡风险相关 | 只写关联，不写预防 | E-B association | D0 observational |
| coffee-base-CLM-006 | 咖啡预防 CVD | 因果证据不足 | E-0 | D0 observational + causal red-team |
| coffee-base-CLM-007 | 醒神 | 近现代中药记录 + direct human alertness 相符 | M-II | D0 |
| coffee-base-CLM-008 | 归心经/肝经等 | 无可靠直接依据，暂不归经 | M-0 | — |

## 15. 停止判断

- stopping_status: saturated_for_R3_core_questions
- evidence_cutoff: 2026-09-23
- stopping_reason: 已覆盖 generic long-term evidence map、direct coffee alertness RCT、caffeine timing/sleep 的证据距离、brewing method 的直接因果试验、causal-inference red team、权威 caffeine safety、近现代中药资料与归经问题。继续逐病、逐机制扩张不会改变本母页核心结论。

### R3 为什么现在可以停

咖啡文献仍然极多，但新增论文已经不会改变这几个框架级判断：

1. 警觉是最可靠的即时功能之一；
2. sleep 主要取决于 caffeine dose × timing × sensitivity；
3. brewing method 可实质改变 lipid effect；
4. long-term benefit 主要是 observational association；
5. coffee 与 caffeine 不能等同；
6. 近现代资料可支持“醒神”，不能凭五味自动补归经。

若正文未来要写某个具体 child entry，再做定向更新，而不是重开整个 coffee universe。

## 16. 参考资料

1. Poole R, et al. Coffee consumption and health: umbrella review of meta-analyses of multiple health outcomes. BMJ. 2017;359:j5024. DOI 10.1136/bmj.j5024. https://pmc.ncbi.nlm.nih.gov/articles/PMC5696634/
2. van Dam RM, Hu FB, Willett WC. Coffee, Caffeine, and Health. N Engl J Med. 2020;383:369-378. PMID 32706535. DOI 10.1056/NEJMra1816604.
3. Haskell-Ramsay CF, et al. The Acute Effects of Caffeinated Black Coffee on Cognition and Mood in Healthy Young and Older Adults. Nutrients. 2018;10:1386. DOI 10.3390/nu10101386.
4. van Bergen G, et al. Caffeine effects of a cup of coffee on vigilance and attention in a realistic scenario. DOI 10.18174/683400.
5. Drake C, et al. Caffeine Effects on Sleep Taken 0, 3, or 6 Hours before Going to Bed. J Clin Sleep Med. 2013;9:1195-1200. PMID 24235903. DOI 10.5664/jcsm.3170.
6. Gardiner CL, et al. Dose and timing effects of caffeine on subsequent sleep: a randomized clinical crossover trial. Sleep. 2025;48(4):zsae230. DOI 10.1093/sleep/zsae230.
7. Bak AAA, Grobbee DE. The Effect on Serum Cholesterol Levels of Coffee Brewed by Filtering or Boiling. N Engl J Med. 1989. DOI 10.1056/NEJM198911233212103.
8. Jee SH, et al. Coffee consumption and serum lipids: a meta-analysis of randomized controlled clinical trials. Am J Epidemiol. 2001;153:353-362. PMID 11207153.
9. Yuan S, et al. Coffee Consumption and Cardiovascular Diseases: A Mendelian Randomization Study. Nutrients. 2021;13:2218. DOI 10.3390/nu13072218. https://pmc.ncbi.nlm.nih.gov/articles/PMC8308456/
10. FDA. Spilling the Beans: How Much Caffeine is Too Much? https://www.fda.gov/consumers/consumer-updates/spilling-beans-how-much-caffeine-too-much
11. EFSA. Scientific Opinion on the safety of caffeine. EFSA Journal. 2015;13:4102. DOI 10.2903/j.efsa.2015.4102.
12. 《中华本草》咖啡公开转录入口：http://tcm360.cn/zycd/detail/yaocaitupu-44484.html

> 本页是共享 Research Parent，不直接作为纸书条目。以后意式浓缩、美式、手冲、冷萃、无咖啡因等正文条目应引用本页，再对各自的冲煮、剂量与配方重新评 D。