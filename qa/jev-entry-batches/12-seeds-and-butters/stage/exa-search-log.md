# Exa 检索日志｜第 12 批：种子、籽类与坚果酱

- 检索日期：2026-09-24
- Exa 查询尝试：46（每条 query 计一次）
- 已归档结果卡：167（见同目录 `exa-results-preserved.json`，包含返回标题、链接和原始 highlights）
- 初始 10 条宽检索的首轮响应因解析器读取错误未单独存档，随后原样重跑并保留结果；一次 Chia 响应格式诊断也未保留原始返回，之后重试并保存完整结果。
- 14 条针对性检索中有 2 条遇 HTTP 429；错误文本保留，并逐条重试成功。搜索结果用于发现与筛查来源，正文只引用核验过的原始研究、同行评议综述或官方资料。

## 查询次数与结果数

| 阶段 | 查询尝试 | 已保存结果卡 | 说明 |
|---|---:|---:|---|
| 第一轮宽检索 | 10 | 0 单独归档 | 解析器未保存结果；相同 10 条逐条重跑，见下一行 |
| 宽检索重跑 | 10 | 50 | 每条 5 个结果 |
| Chia 格式诊断与重试 | 2 | 5 | 首次诊断未单独归档；最终响应完整保存 |
| 定向补查 | 14 | 60 | 12 条成功、2 条 429（0 卡） |
| 来源细节核验 | 8 | 42 | 其中一个查询返回 7 条，其余各 5 条 |
| 限流查询重试 | 2 | 10 | 每条 5 个结果 |
| **合计** | **46** | **167** | **只把已保存卡片计入 exa_hits** |

## 原始检索与来源筛查

### 01｜nut-fruit-mix｜initial broad pass

查询：`Nut and dried fruit mix snack direct human randomized controlled feeding trial cardiometabolic outcomes DOI composition product-specific evidence`
结果：response received but result parser stored zero cards; exact query rerun and retained in next pass
- 处理：没有将未保存的首轮结果写成已归档来源；相同查询随即重跑，保存结果见后续宽检索记录。
- 筛查：果干交叉试验不含坚果；配对综述不是混合成品随机试验。

### 02｜chia-seed｜initial broad pass

查询：`Chia seed supplementation randomized controlled trial adults cardiometabolic outcomes dose duration systematic review DOI primary human trial`
结果：response received but result parser stored zero cards; exact query rerun and retained in next pass
- 处理：没有将未保存的首轮结果写成已归档来源；相同查询随即重跑，保存结果见后续宽检索记录。
- 筛查：核对 2017、2024 年综述间的结局差异，并保留阳性单项 RCT 的 T2D/限能量饮食边界。

### 03｜flaxseed｜initial broad pass

查询：`Flaxseed supplementation randomized controlled trial adults blood pressure lipids glycemia systematic review meta-analysis primary study DOI ground whole flaxseed`
结果：response received but result parser stored zero cards; exact query rerun and retained in next pass
- 处理：没有将未保存的首轮结果写成已归档来源；相同查询随即重跑，保存结果见后续宽检索记录。
- 筛查：区分磨碎籽、整籽、油及木酚素；《本草纲目》将亚麻与胡麻/油麻分条。

### 04｜pumpkin-seeds｜initial broad pass

查询：`Whole pumpkin seed kernels human randomized clinical trial cardiometabolic outcomes distinguish pumpkin seed oil extract DOI`
结果：response received but result parser stored zero cards; exact query rerun and retained in next pass
- 处理：没有将未保存的首轮结果写成已归档来源；相同查询随即重跑，保存结果见后续宽检索记录。
- 筛查：直接人体结果仅来自小型大学论文比较籽仁与籽油，不是安慰剂试验。

### 05｜sunflower-seed-kernels｜initial broad pass

查询：`Sunflower seed kernels human randomized controlled trial direct consumption cardiometabolic outcomes nutrition composition DOI`
结果：response received but result parser stored zero cards; exact query rerun and retained in next pass
- 处理：没有将未保存的首轮结果写成已归档来源；相同查询随即重跑，保存结果见后续宽检索记录。
- 筛查：直接试验针对籽仁与杏仁的短期交叉比较；《本草纲目》“葵”条不直接投射为现代向日葵种仁。

### 06｜quinoa-crisps｜initial broad pass

查询：`Quinoa crisps puffed quinoa snack direct human clinical trial composition FoodData Central DOI distinguish whole quinoa`
结果：response received but result parser stored zero cards; exact query rerun and retained in next pass
- 处理：没有将未保存的首轮结果写成已归档来源；相同查询随即重跑，保存结果见后续宽检索记录。
- 筛查：藜麦强化饼干或膨化加工研究与藜麦脆成品不同，只标相邻/工艺资料。

### 07｜hemp-protein-food｜initial broad pass

查询：`Hemp seed protein human randomized trial muscle protein synthesis athletes compare whey soy dose DOI distinguish hemp seed foods`
结果：response received but result parser stored zero cards; exact query rerun and retained in next pass
- 处理：没有将未保存的首轮结果写成已归档来源；相同查询随即重跑，保存结果见后续宽检索记录。
- 筛查：把种仁蛋白粉与混合植物蛋白、CBD/THC 和火麻仁油分开。

### 08｜peanut-butter｜initial broad pass

查询：`Peanut butter randomized controlled trial adults human cardiometabolic weight outcomes direct peanut butter DOI`
结果：response received but result parser stored zero cards; exact query rerun and retained in next pass
- 处理：没有将未保存的首轮结果写成已归档来源；相同查询随即重跑，保存结果见后续宽检索记录。
- 筛查：花生酱试验为消防员短期睡前试点；整粒花生资料为相邻暴露。

### 09｜almond-butter｜initial broad pass

查询：`Almond butter human randomized controlled trial adults clinical health outcomes direct almond butter versus whole almonds DOI`
结果：response received but result parser stored zero cards; exact query rerun and retained in next pass
- 处理：没有将未保存的首轮结果写成已归档来源；相同查询随即重跑，保存结果见后续宽检索记录。
- 筛查：分别保留杏仁酱的饮食研究和急性交叉研究，避免外推到加糖/加盐商品。

### 10｜cashew-butter｜initial broad pass

查询：`Cashew butter human randomized controlled trial direct cashew butter clinical outcomes DOI distinguish whole cashews`
结果：response received but result parser stored zero cards; exact query rerun and retained in next pass
- 处理：没有将未保存的首轮结果写成已归档来源；相同查询随即重跑，保存结果见后续宽检索记录。
- 筛查：结果主要为整粒腰果试验或加工/配方论文，没有将整粒腰果结果写成腰果酱直接证据。

### 11｜chia-seed｜initial response-shape diagnostic

查询：`Chia seed supplementation randomized controlled trial adults cardiometabolic outcomes dose duration systematic review DOI primary human trial`
结果：duplicate check was made; individual response not retained in the earlier log; captured again at call 46
- 筛查：核对 2017、2024 年综述间的结局差异，并保留阳性单项 RCT 的 T2D/限能量饮食边界。

### 12｜nut-fruit-mix｜broad rerun after parser correction

查询：`Nut and dried fruit mix snack direct human randomized controlled feeding trial cardiometabolic outcomes DOI composition product-specific evidence`
结果：success; retained 5 result cards

检索结果：
- Dried fruit consumption and cardiometabolic health: a randomized crossover trial — https://pmc.ncbi.nlm.nih.gov/articles/PMC7554183/
- Original Research Article Consuming pecans as a snack improves lipids/lipoproteins and diet quality compared with usual diet in adults at increased risk of cardiometabolic diseases: a randomized controlled trial — https://www.sciencedirect.com/science/article/pii/S0002916525000577
- Pairing nuts and dried fruit for cardiometabolic health | Nutrition Journal | Springer Nature Link — https://link.springer.com/article/10.1186/s12937-016-0142-4
- Pairing nuts and dried fruit for cardiometabolic health — https://doi.org/10.1186/s12937-016-0142-4
- Effect of Dried Fruit on Cardiometabolic Risk Factors — https://clinicaltrials.gov/study/NCT03020758
- 筛查：果干交叉试验不含坚果；配对综述不是混合成品随机试验。

### 13｜chia-seed｜broad rerun after parser correction

查询：`Chia seed supplementation randomized controlled trial adults cardiometabolic outcomes dose duration systematic review DOI primary human trial`
结果：success; retained 5 result cards

检索结果：
- The Effect of Chia Seed on Blood Pressure, Body Composition, and Glycemic Control: A GRADE-Assessed Systematic Review and Dose-Response Meta-Analysis of Randomized Controlled Trials — https://doi.org/10.1093/nutrit/nuae113
- Clinical evidence on dietary supplementation with chia seed (Salvia hispanica L.): a systematic review and meta-analysis — https://doi.org/10.1093/nutrit/nux071
- Effects of chia (Salvia hispanica. L) on anthropometric measures and other cardiometabolic risk factors: A systematic review and dose-response meta-analysis — https://doi.org/10.1016/j.ctim.2024.103086
- The impact of chia seeds on diabetes, blood pressure, lipid profile, and obesity indicators: Systematic review and meta-regression analysis of 14 randomized controlled trials — https://pubmed.ncbi.nlm.nih.gov/39299649/
- Effects of chia seed (Salvia hispanica L.) supplementation on cardiometabolic health in overweight subjects: a systematic review and meta-analysis of RCTs — https://doi.org/10.1186/s12986-024-00847-3
- 筛查：核对 2017、2024 年综述间的结局差异，并保留阳性单项 RCT 的 T2D/限能量饮食边界。

### 14｜flaxseed｜broad rerun after parser correction

查询：`Flaxseed supplementation randomized controlled trial adults blood pressure lipids glycemia systematic review meta-analysis primary study DOI ground whole flaxseed`
结果：success; retained 5 result cards

检索结果：
- Comparisons of the effects of different flaxseed products consumption on lipid profiles, inflammatory cytokines and anthropometric indices in patients with dyslipidemia related diseases: systematic review and a dose–response meta-analysis of randomized controlled trials - PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC8504108/
- Flaxseed supplementation on glucose control and insulin sensitivity: a systematic review and meta-analysis of 25 randomized, placebo-controlled trials — https://doi.org/10.1093/nutrit/nux052
- Effect of flaxseed supplementation on blood pressure: a systematic review, and dose–response meta-analysis of randomized clinical trials - Food & Function (RSC Publishing) — https://pubs.rsc.org/en/content/articlelanding/2023/fo/d2fo02566c
- Effects of flaxseed supplementation on weight loss, lipid profiles, glucose, and high‐sensitivity C‐reactive protein in patients with coronary artery disease: A systematic review and meta‐analysis of randomized controlled trials — https://doi.org/10.1002/clc.24211
- Flaxseed Consumption May Reduce Blood Pressure: A Systematic Review and Meta-Analysis of Controlled Trials — https://doi.org/10.3945/jn.114.205302
- 筛查：区分磨碎籽、整籽、油及木酚素；《本草纲目》将亚麻与胡麻/油麻分条。

### 15｜pumpkin-seeds｜broad rerun after parser correction

查询：`Whole pumpkin seed kernels human randomized clinical trial cardiometabolic outcomes distinguish pumpkin seed oil extract DOI`
结果：success; retained 5 result cards

检索结果：
- Effect of Pumpkin Seed Oil or Pumpkin Seeds on Blood Pressure and Menopausal Symptoms in Postmenopausal Women — https://clinicaltrials.gov/study/NCT02727036
- Pumpkin Seeds or Oil Lower Serum Triglyceride Levels in Individuals With Hyperlipidaemia — https://clinicaltrials.gov/study/NCT07123844
- Therapeutic and Preventive Roles of Pumpkin Seeds in Lifestyle Disorders — https://doi.org/10.9734/ajfrn/2026/v5i1360
- Effect of Hypoenergetic Diet Combined With Pumpkin Seed Flour Consumption on Obese Women — https://doi.org/10.36660/ijcs.20220134
- 筛查：直接人体结果仅来自小型大学论文比较籽仁与籽油，不是安慰剂试验。

### 16｜sunflower-seed-kernels｜broad rerun after parser correction

查询：`Sunflower seed kernels human randomized controlled trial direct consumption cardiometabolic outcomes nutrition composition DOI`
结果：success; retained 5 result cards

检索结果：
- Markers of Cardiovascular Risk in Postmenopausal Women with Type 2 Diabetes Are Improved by the Daily Consumption of Almonds or Sunflower Kernels: A Feeding Study — https://pmc.ncbi.nlm.nih.gov/articles/PMC4045277/
- Effect of Sunflower Seed Consumption on Blood Cholesterol Levels in Adults — https://clinicaltrials.gov/study/NCT07231367
- EFFECTS OF SUNFLOWER SEEDS ON CHOLESTEROL AND LOW-DENSITY LIPOPROTEIN LEVELS IN PATIENTS WITH DYSLIPIDEMIA — https://doi.org/10.22159/ajpcr.2019.v12i3.31032
- N/A — http://fmhr.org/index.php/fmhr/article/download/375/367/745
- Lipid profile of hyperlipidemic males after supplementation of ... — https://pmc.ncbi.nlm.nih.gov/articles/PMC8196128/
- 筛查：直接试验针对籽仁与杏仁的短期交叉比较；《本草纲目》“葵”条不直接投射为现代向日葵种仁。

### 17｜quinoa-crisps｜broad rerun after parser correction

查询：`Quinoa crisps puffed quinoa snack direct human clinical trial composition FoodData Central DOI distinguish whole quinoa`
结果：success; retained 5 result cards

检索结果：
- Physical, chemical and nutritional characteristics of puffed quinoa — https://ifst.onlinelibrary.wiley.com/doi/10.1111/ijfs.14290
- Fluidized thermal treatment for developing a whole quinoa snack — https://doi.org/10.21203/rs.3.rs-7040302/v1
- Novel quinoa-enriched biscuits improve CVD risk markers in older adults: a randomised crossover trial with a novel food product — https://www.cambridge.org/core/journals/proceedings-of-the-nutrition-society/article/novel-quinoaenriched-biscuits-improve-cvd-risk-markers-in-older-adults-a-randomised-crossover-trial-with-a-novel-food-product/5B89469CA1249B070D44D613821665E0
- Quinoa Snack Production at an Industrial Level: Effect of Extrusion and Baking on Digestibility, Bioactive, Rheological, and Physical Properties — https://www.mdpi.com/2304-8158/11/21/3383
- Food Search | USDA FoodData Central — https://fdc.nal.usda.gov/food-search
- 筛查：藜麦强化饼干或膨化加工研究与藜麦脆成品不同，只标相邻/工艺资料。

### 18｜hemp-protein-food｜broad rerun after parser correction

查询：`Hemp seed protein human randomized trial muscle protein synthesis athletes compare whey soy dose DOI distinguish hemp seed foods`
结果：success; retained 5 result cards

检索结果：
- The Benefits of Hemp Protein Supplementation During Resistance Training — https://clinicaltrials.gov/study/NCT02529917
- The benefits of hemp powder supplementation during resistance training — https://www.researchgate.net/publication/315038556_The_benefits_of_hemp_powder_supplementation_during_resistance_training
- Plant Protein Blend Ingestion Stimulates Postexercise Myofibrillar Protein Synthesis Rates Equivalently to Whey in Resistance-Trained Adults — https://doi.org/10.1249/mss.0000000000003432
- Hemp seed protein and its hydrolysate compared with casein protein consumption in adults with hypertension: a double-blind crossover study — https://pmc.ncbi.nlm.nih.gov/articles/PMC11251217/
- Protein Supplementation Has Minimal Effects on Muscle Adaptations during Resistance Exercise Training in Young Men: A Double-Blind Randomized Clinical Trial 1 2 3 — https://www.sciencedirect.com/science/article/pii/S0022316623006910
- 筛查：把种仁蛋白粉与混合植物蛋白、CBD/THC 和火麻仁油分开。

### 19｜peanut-butter｜broad rerun after parser correction

查询：`Peanut butter randomized controlled trial adults human cardiometabolic weight outcomes direct peanut butter DOI`
结果：success; retained 5 result cards

检索结果：
- Effects of Peanut Consumption on Cardiometabolic Risk Factors in a Chinese Population: A Randomized, Controlled Trial (P08-041-19) — https://pmc.ncbi.nlm.nih.gov/articles/PMC6818951/
- Effect of peanut butter supplementation on physical and ... - PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC11381714/
- A Pilot Randomized, Controlled Trial of Nighttime Peanut ... — https://www.mdpi.com/2079-9721/14/4/135
- Effect of Peanut Consumption on Cardiovascular Risk Factors: A Randomized Clinical Trial and Meta-Analysis — https://doi.org/10.3389/fnut.2022.853378
- Effects of peanut processing on body weight and fasting plasma lipids — https://doi.org/10.1017/s0007114510000590
- 筛查：花生酱试验为消防员短期睡前试点；整粒花生资料为相邻暴露。

### 20｜almond-butter｜broad rerun after parser correction

查询：`Almond butter human randomized controlled trial adults clinical health outcomes direct almond butter versus whole almonds DOI`
结果：success; retained 5 result cards

检索结果：
- Acute and second-meal effects of almond form in impaired glucose tolerant adults: a randomized crossover trial — https://pmc.ncbi.nlm.nih.gov/articles/PMC3042001/
- Effects of plant-based diets high in raw or roasted almonds, or roasted almond butter on serum lipoproteins in humans — https://pubmed.ncbi.nlm.nih.gov/12805245/
- Acute and second-meal effects of almond form in impaired glucose tolerant adults: a randomized crossover trial | Nutrition & Metabolism | Springer Nature Link — https://link.springer.com/article/10.1186/1743-7075-8-6
- A Pilot Study of the Effect of Evening Almond Butter Consumption on Overnight and Fasting Interstitial Glucose — https://doi.org/10.3390/diabetology3040038
- Snacking on whole almonds for 6 weeks improves endothelial function and lowers LDL cholesterol but does not affect liver fat and other cardiometabolic risk factors in healthy adults: the ATTIS study, a randomized controlled trial — https://pmc.ncbi.nlm.nih.gov/articles/PMC7266688/
- 筛查：分别保留杏仁酱的饮食研究和急性交叉研究，避免外推到加糖/加盐商品。

### 21｜cashew-butter｜broad rerun after parser correction

查询：`Cashew butter human randomized controlled trial direct cashew butter clinical outcomes DOI distinguish whole cashews`
结果：success; retained 5 result cards

检索结果：
- Metabolizable Energy from Cashew Nuts is Less than ... - PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC6356908/
- Consumption of cashew nuts does not influence blood ... — https://ajcn.nutrition.org/article/S0002-9165(22)03106-9/fulltext
- Effects of Daily Consumption of Cashews on Oxidative Stress and Atherogenic Indices in Patients with Type 2 Diabetes: A Randomized, Controlled-Feeding Trial — https://doi.org/10.5812/ijem.70744
- Proximate composition microbial and sensory analyses of ... — https://innspub.net/proximate-composition-microbial-and-sensory-analyses-of-butter-made-from-cashew-kernel-pieces/
- Cashew consumption reduces total and LDL cholesterol: a randomized, crossover, controlled-feeding trial 1 , 2 — https://www.sciencedirect.com/science/article/pii/S0002916522048742
- 筛查：结果主要为整粒腰果试验或加工/配方论文，没有将整粒腰果结果写成腰果酱直接证据。

### 22｜nut-fruit-mix｜targeted follow-up

查询：`Pairing nuts and dried fruit for cardiometabolic health randomized trial mixed nuts dried fruit DOI 2016`
结果：success; retained 5 result cards

检索结果：
- Pairing nuts and dried fruit for cardiometabolic health — https://doi.org/10.1186/s12937-016-0142-4
- Pairing nuts and dried fruit for cardiometabolic health - PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC4779204/
- Pairing nuts and dried fruit for cardiometabolic health — https://link.springer.com/article/10.1186/s12937-016-0142-4
- Crossmark — https://crossmark.crossref.org/dialog/?doi=10.1186%2Fs12937-016-0142-4
- Effect of Dried Fruit on Cardiometabolic Risk Factors — https://clinicaltrials.gov/study/NCT03020758
- 筛查：果干交叉试验不含坚果；配对综述不是混合成品随机试验。

### 23｜chia-seed｜targeted follow-up

查询：`Salba chia randomized controlled trial overweight obese type 2 diabetes 77 adults 30 g 1000 kcal 6 months DOI`
结果：success; retained 5 result cards

检索结果：
- Salba-chia (Salvia hispanica L.) in the treatment of overweight and obese patients with type 2 diabetes: A double-blind randomized controlled trial — https://doi.org/10.1016/j.numecd.2016.11.124
- Salba-chia (Salvia hispanica L.) in the treatment of overweight and obese patients with type 2 diabetes: A double-blind randomized controlled trial - Nutrition, Metabolism and Cardiovascular Diseases — https://www.nmcd-journal.com/article/S0939-4753(16)30329-5/abstract
- Salba-chia (Salvia hispanica L.) in the treatment of ... — https://pubmed.ncbi.nlm.nih.gov/28089080/
- Effect of Salba‐Chia ( Salvia Hispanica L), an Ancient Seed, in the Treatment of Overweight and Obese Patients with Type 2 Diabetes: A Double‐blind, Parallel, Randomized Controlled Trial — https://doi.org/10.1096/fasebj.30.1_supplement.126.2
- Effectiveness and Safety of Salba on Weight Loss in Overweight Individuals With Type 2 Diabetes — https://clinicaltrials.gov/study/NCT01403571
- 筛查：核对 2017、2024 年综述间的结局差异，并保留阳性单项 RCT 的 T2D/限能量饮食边界。

### 24｜flaxseed｜targeted follow-up

查询：`flaxseed supplementation randomized trial 30 g daily 6 months blood pressure lipids adults DOI ground flaxseed`
结果：success; retained 5 result cards

检索结果：
- Potent Antihypertensive Action of Dietary Flaxseed in Hypertensive Patients | Hypertension — https://www.ahajournals.org/doi/10.1161/hypertensionaha.113.02094
- Dietary flaxseed independently lowers circulating cholesterol and lowers it beyond the effects of cholesterol-lowering medications alone in patients with peripheral artery disease — https://pubmed.ncbi.nlm.nih.gov/25694068/
- Effects of flaxseed on blood pressure, body mass index, and total cholesterol in hypertensive patients: A randomized clinical trial — https://doi.org/10.1016/j.explore.2021.05.003
- Flaxseed Consumption Reduces Blood Pressure in ... — https://www.ahajournals.org/doi/10.1161/hypertensionaha.114.03179
- Dietary Flaxseed Reduces Central Aortic Blood Pressure Without Cardiac Involvement but Through Changes in Plasma Oxylipins | Hypertension — https://www.ahajournals.org/doi/10.1161/HYPERTENSIONAHA.116.07834
- 筛查：区分磨碎籽、整籽、油及木酚素；《本草纲目》将亚麻与胡麻/油麻分条。

### 25｜pumpkin-seeds｜targeted follow-up

查询：`NCT02727036 pumpkin seed versus pumpkin seed oil published results randomized trial postmenopausal women blood pressure DOI`
结果：success; retained 5 result cards

检索结果：
- Effect of supplementation with pumpkin seed oil versus ... — https://twu-ir.tdl.org/items/839a4eb3-7fd9-4aab-8241-51ccfcf22b4f
- Effect of Pumpkin Seed Oil or Pumpkin Seeds on Blood Pressure and Menopausal Symptoms in Postmenopausal Women — https://clinicaltrials.gov/study/NCT02727036
- Effect of Supplementation with Pumpkin Seed Oil Versus Pumpkin - DocsLib — https://docslib.org/doc/2497531/effect-of-supplementation-with-pumpkin-seed-oil-versus-pumpkin
- Pumpkin seed oil and Pumpkin seeds in Hypertension and Dyslipidemia - Clinical Trials Registry - ICH GCP — https://ichgcp.net/clinical-trials-registry/NCT02727036
- The effects of pumpkin seed oil supplementation on arterial ... — https://pubmed.ncbi.nlm.nih.gov/31445363/
- 筛查：直接人体结果仅来自小型大学论文比较籽仁与籽油，不是安慰剂试验。

### 26｜sunflower-seed-kernels｜targeted follow-up

查询：`sunflower kernels feeding study 22 postmenopausal women type 2 diabetes randomized crossover DOI results`
结果：rate limited (HTTP 429); no result cards, retried at calls 44–45
- 处理：限流消息不作为文献结论；使用同一查询逐条重试。
- 筛查：直接试验针对籽仁与杏仁的短期交叉比较；《本草纲目》“葵”条不直接投射为现代向日葵种仁。

### 27｜quinoa-crisps｜targeted follow-up

查询：`USDA FoodData Central quinoa puffs crisped quinoa nutrition composition human trial quinoa snack`
结果：success; retained 5 result cards

检索结果：
- Food Search | USDA FoodData Central — https://fdc.nal.usda.gov/food-search
- CRISPY QUINOA PUFFS — https://warehousemanager.us/storage/spec/1632/Spec_1684405504.pdf
- Physical, chemical and nutritional characteristics of puffed quinoa — https://ifst.onlinelibrary.wiley.com/doi/10.1111/ijfs.14290
- Survey Foods - Food Search | USDA FoodData Central — https://fdc.nal.usda.gov/food-search?type=Experimental
- Nutrition Facts for  Kretschmer - Puffed Quinoa — https://tools.myfooddata.com/nutrition-facts/1933229/wt1
- 筛查：藜麦强化饼干或膨化加工研究与藜麦脆成品不同，只标相邻/工艺资料。

### 28｜hemp-protein-food｜targeted follow-up

查询：`NCT02529917 hemp powder 8 week resistance training results peer reviewed publication DOI`
结果：success; retained 5 result cards

检索结果：
- Effects of hemp supplementation during resistance training ... — https://pubmed.ncbi.nlm.nih.gov/37847288/
- The Benefits of Hemp Protein Supplementation During Resistance Training — https://clinicaltrials.gov/study/NCT02529917
- Fatigue | Effects of hemp supplementation during resistance training in trained young adults | springermedicine.com — https://www.springermedicine.com/fatigue/effects-of-hemp-supplementation-during-resistance-training-in-tr/26191622
- The benefits of hemp powder supplementation during ... — https://www.researchgate.net/publication/315038556_The_benefits_of_hemp_powder_supplementation_during_resistance_training
- Effects of hemp supplementation during resistance training in trained young adults - ProQuest — https://search.proquest.com/openview/d9b691a66398f7c57e29213a89ca0271/1?cbl=55471&pq-origsite=gscholar
- 筛查：把种仁蛋白粉与混合植物蛋白、CBD/THC 和火麻仁油分开。

### 29｜peanut-butter｜targeted follow-up

查询：`2026 pilot randomized controlled trial nighttime peanut butter firefighters blood pressure body composition DOI results`
结果：success; retained 5 result cards

检索结果：
- A Pilot Randomized, Controlled Trial of Nighttime Peanut Butter Supplementation in Firefighters: Blood Pressure and Body Composition Outcomes — https://doi.org/10.3390/diseases14040135
- A Pilot Randomized, Controlled Trial of Nighttime Peanut ... — https://www.mdpi.com/2079-9721/14/4/135
- Blood Pressure and Body Composition Outcomes — https://pubmed.ncbi.nlm.nih.gov/42041627/
- A Pilot Randomized, Controlled Trial of Peanut Butter Supplementation in Firefighters: Blood Pressure and Body Composition Outcomes — https://doi.org/10.17605/osf.io/8xs5h
- EFFECTS OF CONSUMING PEANUT BUTTER FOR 7-WEEKS ON BODY COMPOSITION IN FIREFIGHTERS — https://digitalcommons.wku.edu/ijesab/vol16/iss3/73
- 筛查：花生酱试验为消防员短期睡前试点；整粒花生资料为相邻暴露。

### 30｜almond-butter｜targeted follow-up

查询：`almond butter randomized trial 14 impaired glucose tolerance adults acute second meal DOI 38 hypercholesterolemic serum lipoproteins DOI`
结果：success; retained 5 result cards

检索结果：
- Acute and second-meal effects of almond form in impaired glucose tolerant adults: a randomized crossover trial — https://doi.org/10.1186/1743-7075-8-6
- Acute and second-meal effects of almond form in impaired ... — https://pmc.ncbi.nlm.nih.gov/articles/PMC3042001/
- Acute and second-meal effects of almond form in impaired glucose tolerant adults: a randomized crossover trial - PubMed — https://pubmed.ncbi.nlm.nih.gov/21276226/
- Acute and second-meal effects of almond form in impaired glucose tolerant adults: a randomized crossover trial | Nutrition & Metabolism | Springer Nature Link — https://link.springer.com/article/10.1186/1743-7075-8-6
- Acute and Second-Meal Effects of Almond Form in Impaired Glucose Tolerant Adults: A Randomized Crossover Trial — https://docs.lib.purdue.edu/cgi/viewcontent.cgi?article=1001&context=fnpubs
- 筛查：分别保留杏仁酱的饮食研究和急性交叉研究，避免外推到加糖/加盐商品。

### 31｜cashew-butter｜targeted follow-up

查询：`cashew butter human clinical trial randomized controlled feeding glycemic blood lipid study DOI direct product`
结果：success; retained 5 result cards

检索结果：
- Effects of Daily Consumption of Cashews on Oxidative Stress and Atherogenic Indices in Patients with Type 2 Diabetes: A Randomized, Controlled-Feeding Trial — https://doi.org/10.5812/ijem.70744
- Cashew Nut Consumption Increases HDL Cholesterol and Reduces Systolic Blood Pressure in Asian Indians with Type 2 Diabetes: A 12-Week Randomized Controlled Trial — https://www.sciencedirect.com/science/article/pii/S0022316622108667
- Consumption of cashew nuts does not influence blood ... — https://ajcn.nutrition.org/article/S0002-9165(22)03106-9/fulltext
- Cashew consumption reduces total and LDL cholesterol: a randomized, crossover, controlled-feeding trial - PubMed — https://pubmed.ncbi.nlm.nih.gov/28356271
- Cashew consumption reduces total and LDL cholesterol: a randomized, crossover, controlled-feeding trial 1 , 2 — https://www.sciencedirect.com/science/article/pii/S0002916522048742
- 筛查：结果主要为整粒腰果试验或加工/配方论文，没有将整粒腰果结果写成腰果酱直接证据。

### 32｜hemp-protein-food｜targeted follow-up

查询：`FDA hemp seed-derived ingredients hulled hemp seed hemp seed protein powder GRAS notice official food human consumption`
结果：success; retained 5 result cards

检索结果：
- Three GRAS Notices for Hemp Seed-Derived Ingredients ... — https://www.fda.gov/food/hfp-constituent-updates/fda-responds-three-gras-notices-hemp-seed-derived-ingredients-use-human-food
- GRAS notice 765 for Hulled hemp seed — https://www.fda.gov/files/food/published/GRAS-Notice-765.pdf
- GRAS Notices (GRN) 765, 771, 778 - Supplement — https://www.fda.gov/media/164016/download
- GRAS notice 771 for Hemp seed protein — https://www.fda.gov/files/food/published/GRN771-web2.pdf
- GRAS Notice 765, Dehulled hemp seed — https://www.fda.gov/media/119427/download
- 筛查：把种仁蛋白粉与混合植物蛋白、CBD/THC 和火麻仁油分开。

### 33｜pumpkin-seeds｜targeted follow-up

查询：`《本草纲目》 南瓜子 原文 南瓜子味甘性温 本草拾遗 原典`
结果：rate limited (HTTP 429); no result cards, retried at calls 44–45
- 处理：限流消息不作为文献结论；使用同一查询逐条重试。
- 筛查：直接人体结果仅来自小型大学论文比较籽仁与籽油，不是安慰剂试验。

### 34｜flaxseed｜targeted follow-up

查询：`《本草纲目》 亚麻子 胡麻 亚麻籽 植物身份 原文 Wikisource`
结果：success; retained 5 result cards

检索结果：
- 本草綱目/穀之一 — https://zh.wikisource.org/wiki/%E6%9C%AC%E8%8D%89%E7%B6%B1%E7%9B%AE/%E7%A9%80%E4%B9%8B%E4%B8%80
- 本草纲目·谷部·亚麻原文翻译文及拼音 - 李时珍 - 云对雨古诗网 — https://www.yunduiyu.com/poetry-125138.html
- 本草綱目 (四庫全書本) - 维基文库，自由的图书馆 — https://zh.wikisource.org/zh/%E6%9C%AC%E8%8D%89%E7%B6%B1%E7%9B%AE_(%E5%9B%9B%E5%BA%AB%E5%85%A8%E6%9B%B8%E6%9C%AC)
- 亚麻_谷部_《本草纲目》完整版_本草纲目在线阅读 — https://zhongyibaodian.com/bcgm/yama.html
- 《本草纲目(金陵本)》第二十二卷 谷部（一） - 中医中药 — http://www.huofanwen.com/zhongyi/chapter/26573.html
- 筛查：区分磨碎籽、整籽、油及木酚素；《本草纲目》将亚麻与胡麻/油麻分条。

### 35｜sunflower-seed-kernels｜targeted follow-up

查询：`《本草纲目》 向日葵子 葵花籽 原文 本草 古籍`
结果：success; retained 5 result cards

检索结果：
- 葵_草部_《本草纲目》完整版_本草纲目在线阅读 — http://www.zhongyibaodian.com/bcgm/kui.html
- 本草綱目 (四庫全書本) - 维基文库，自由的图书馆 — https://zh.wikisource.org/zh/%E6%9C%AC%E8%8D%89%E7%B6%B1%E7%9B%AE_(%E5%9B%9B%E5%BA%AB%E5%85%A8%E6%9B%B8%E6%9C%AC)
- 葵_草部_《本草纲目》图文版在线阅读【中医宝典】 — https://zhongyibaodian.com/bencaogangmu/kui.html
- 本草纲目-古今图书集成·草木典全文原文-识典古籍 — https://www.shidianguji.com/book/GJTS20/chapter/1lp7rhm1sc46r
- 向日葵子_中华本草-植物提取物百科 — https://www.zwwiki.cn/html/1690489254311622.html
- 筛查：直接试验针对籽仁与杏仁的短期交叉比较；《本草纲目》“葵”条不直接投射为现代向日葵种仁。

### 36｜sunflower-seed-kernels｜title/result verification

查询：`Markers of Cardiovascular Risk in Postmenopausal Women with Type 2 Diabetes Improved by Daily Almonds or Sunflower Kernels feeding study DOI 22 dose results`
结果：success; retained 5 result cards

检索结果：
- Markers of Cardiovascular Risk in Postmenopausal Women with Type 2 Diabetes Are Improved by the Daily Consumption of Almonds or Sunflower Kernels: A Feeding Study — https://doi.org/10.5402/2013/626414
- Markers of cardiovascular risk in postmenopausal women ... — https://pubmed.ncbi.nlm.nih.gov/24959542/
- Clinical Study Markers of Cardiovascular Risk in PostmenopausalWomen with Type 2 Diabetes Are Improved by the Daily Consumption — http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.804.6793
- Almonds and Sunflower Kernels Equally Beneficial for Type II Diabetics: If Anything, There is s Small Advantage For Sunflower + Grape See Oil vs. Almonds + Olive Oil — https://suppversity.blogspot.com/2014/01/almonds-and-sunflower-kernels-equally.html
- Effects of Daily Almond Consumption on... : Journal of the American Heart Association — https://www.ovid.com/jnls/jotha/fulltext/10.1161/jaha.114.000993~effects-of-daily-almond-consumption-on-cardiometabolic-risk
- 筛查：直接试验针对籽仁与杏仁的短期交叉比较；《本草纲目》“葵”条不直接投射为现代向日葵种仁。

### 37｜pumpkin-seeds｜title/result verification

查询：`Madhura Maiya pumpkin seed oil versus pumpkin seeds blood pressure menopausal symptoms dissertation 2017 sample 4.1 g results DOI`
结果：success; retained 7 result cards

检索结果：
- Effect of supplementation with pumpkin seed oil versus ... — https://twu-ir.tdl.org/items/839a4eb3-7fd9-4aab-8241-51ccfcf22b4f
- Effect of Pumpkin Seed Oil or Pumpkin Seeds on Blood Pressure and Menopausal Symptoms in Postmenopausal Women — https://clinicaltrials.gov/study/NCT02727036
- Effect of Supplementation with Pumpkin Seed Oil Versus Pumpkin - DocsLib — https://docslib.org/doc/2497531/effect-of-supplementation-with-pumpkin-seed-oil-versus-pumpkin
- Pumpkin seed oil and Pumpkin seeds in Hypertension and Dyslipidemia - Clinical Trials Registry - ICH GCP — https://ichgcp.net/clinical-trials-registry/NCT02727036
- Doctor of Philosophy - Nutrition, Texas Woman's University, Houston TX, Dec. 2017 (GPA 3.9) Certification in Applied statistics, Texas A&M, College Station, August 2011 Master of Science - Food Science and Nutrition, Colorado State University (CSU), Fort Collins, CO, Dec. 2005. (GPA – 3.71) Master of Science, Nutrition and Dietetics, Bangalore University, India, - May 2002. Bachelor of Science, Nutrition and Dietetics, Chemistry, and Zoology, Bangalore University, India – April 2000. Jan 2019 – Present: Adjunct Faculty, Department of Nutrition & Food Science, Texas Woman's University, Houston TX. Teaching: NFS 5314 (Nutrition and Human Metabolism), NFS 5473 (Advance Preventive Nutrition), and NFS 5063 (Food Toxicology). May 2015 – Present Assistant Director, Office of Research and Sponsored Programs, Texas Woman's University, Houston TX. Doctoral Dissertation Title: Effect of supplementation with pumpkin seed oil versus pumpkin seeds on blood pressure and menopausal symptoms in non-hypertensive postmenopausal women. (October 2017) This randomized trial aimed to compare the effect of supplementation of pumpkin seeds (1½ teaspoons/ 4.1 grams a day) versus pumpkin seed oil (2g/day) for 12 weeks on blood pressure, endothelial function, plasma lipids, C-rective protein (CRP) concentrations, and menopausal symptoms in non hypertensive postmenopausal women. Work Experience — https://www.uttyler.edu/academics/colleges-schools/health-professions/files/madhura-maiya-cv.pdf
- 筛查：直接人体结果仅来自小型大学论文比较籽仁与籽油，不是安慰剂试验。

### 38｜hemp-protein-food｜title/result verification

查询：`Kaviani Shaw Candow Effects of hemp supplementation during resistance training in trained young adults 2023 DOI sample results`
结果：success; retained 5 result cards

检索结果：
- Effects of hemp supplementation during resistance training in trained young adults — https://doi.org/10.1007/s00421-023-05337-7
- Fatigue | Effects of hemp supplementation during resistance training in trained young adults | springermedicine.com — https://www.springermedicine.com/fatigue/effects-of-hemp-supplementation-during-resistance-training-in-tr/26191622
- Effects of hemp supplementation during resistance training in trained young adults - ProQuest — https://search.proquest.com/openview/d9b691a66398f7c57e29213a89ca0271/1?cbl=55471&pq-origsite=gscholar
- The benefits of hemp powder supplementation during resistance training — https://www.researchgate.net/publication/315038556_The_benefits_of_hemp_powder_supplementation_during_resistance_training
- The Benefits of Hemp Protein Supplementation During Resistance Training — https://clinicaltrials.gov/study/NCT02529917
- 筛查：把种仁蛋白粉与混合植物蛋白、CBD/THC 和火麻仁油分开。

### 39｜peanut-butter｜title/result verification

查询：`Kohler 2026 A Pilot Randomized Controlled Trial of Nighttime Peanut Butter Supplementation in Firefighters 40 participants 7 weeks dose outcomes DOI`
结果：success; retained 5 result cards

检索结果：
- A Pilot Randomized, Controlled Trial of Nighttime Peanut Butter Supplementation in Firefighters: Blood Pressure and Body Composition Outcomes — https://doi.org/10.3390/diseases14040135
- A Pilot Randomized, Controlled Trial of Nighttime Peanut ... — https://www.mdpi.com/2079-9721/14/4/135
- Blood Pressure and Body Composition Outcomes — https://pubmed.ncbi.nlm.nih.gov/42041627/
- A Pilot Randomized, Controlled Trial of Peanut Butter Supplementation in Firefighters: Blood Pressure and Body Composition Outcomes — https://doi.org/10.17605/osf.io/8xs5h
- EFFECTS OF CONSUMING PEANUT BUTTER FOR 7-WEEKS ON BODY COMPOSITION IN FIREFIGHTERS — https://digitalcommons.wku.edu/ijesab/vol16/iss3/73
- 筛查：花生酱试验为消防员短期睡前试点；整粒花生资料为相邻暴露。

### 40｜almond-butter｜title/result verification

查询：`Effects of plant-based diets high in raw or roasted almonds or roasted almond butter on serum lipoproteins in humans 2003 DOI results 38 participants`
结果：success; retained 5 result cards

检索结果：
- Effects of Plant-Based Diets High in Raw or Roasted Almonds, or Roasted Almond Butter on Serum Lipoproteins in Humans — https://doi.org/10.1080/07315724.2003.10719293
- Effects of plant-based diets high in raw or roasted almonds ... — https://pubmed.ncbi.nlm.nih.gov/12805245/
- Tree nuts and the lipid profile: a review of clinical studies — https://doi.org/10.1017/bjn20061866
- Nuts Reduce Cardiovascular Disease Risk | 2007-03-01… | Clinician.com — https://www.clinician.com/articles/101958-nuts-reduce-cardiovascular-disease-risk
- Effects of Nut Consumption on Blood Lipids and Lipoproteins: A Comprehensive Literature Update — https://www.mdpi.com/2072-6643/15/3/596
- 筛查：分别保留杏仁酱的饮食研究和急性交叉研究，避免外推到加糖/加盐商品。

### 41｜nut-fruit-mix｜title/result verification

查询：`nuts dried fruit combination randomized controlled feeding cardiometabolic trial adults snack exact product not review`
结果：success; retained 5 result cards

检索结果：
- Dried fruit consumption and cardiometabolic health: a randomized crossover trial — https://pmc.ncbi.nlm.nih.gov/articles/PMC7554183/
- Effect of Dried Fruit on Cardiometabolic Risk Factors — https://clinicaltrials.gov/study/NCT03020758
- Pairing nuts and dried fruit for cardiometabolic health - PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC4779204/
- Pairing nuts and dried fruit for cardiometabolic health ... — https://link.springer.com/article/10.1186/s12937-016-0142-4
- Mixed Nut Consumption May Improve Cardiovascular Disease Risk Factors in Overweight and Obese Adults - PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC6683273/
- 筛查：果干交叉试验不含坚果；配对综述不是混合成品随机试验。

### 42｜quinoa-crisps｜title/result verification

查询：`quinoa-enriched biscuits improve cardiovascular risk markers older adults randomized crossover trial DOI 2018 participants results`
结果：success; retained 5 result cards

检索结果：
- Novel quinoa-enriched biscuits improve CVD risk markers in older adults: a randomised crossover trial with a novel food product — https://doi.org/10.1017/s0029665118001155
- Novel quinoa-enriched biscuits improve CVD risk markers in older adults: a randomised crossover trial with a novel food product — https://www.cambridge.org/core/journals/proceedings-of-the-nutrition-society/article/novel-quinoaenriched-biscuits-improve-cvd-risk-markers-in-older-adults-a-randomised-crossover-trial-with-a-novel-food-product/5B89469CA1249B070D44D613821665E0
- Modest improvement in CVD risk markers in older adults ... — https://pubmed.ncbi.nlm.nih.gov/31919583/
- Modest improvement in CVD risk markers in older adults following quinoa (Chenopodium quinoa Willd.) consumption: a randomized-controlled crossover study with a novel food product — https://doi.org/10.1007/s00394-019-02169-0
- Modest improvement in CVD risk markers in older adults following quinoa (Chenopodium quinoa Willd.) consumption: a randomized-controlled crossover study with a novel food product | springermedicine.com — https://www.springermedicine.com/modest-improvement-in-cvd-risk-markers-in-older-adults-following/20942538
- 筛查：藜麦强化饼干或膨化加工研究与藜麦脆成品不同，只标相邻/工艺资料。

### 43｜flaxseed｜title/result verification

查询：`Flaxseed dietary intervention trial blood pressure peripheral artery disease 110 patients 30 g/day 6 months DOI Hypertension 2013`
结果：success; retained 5 result cards

检索结果：
- Potent Antihypertensive Action of Dietary Flaxseed in ... — https://www.ahajournals.org/doi/10.1161/hypertensionaha.113.02094
- Potent antihypertensive action of dietary flaxseed in ... — https://pubmed.ncbi.nlm.nih.gov/24126178/
- Flaxseed may reduce blood pressure, early findings show — https://www.reuters.com/article/business/healthcare-pharmaceuticals/flaxseed-may-reduce-blood-pressure-early-findings-show-idUSBRE9A00R6/
- Flaxseed Consumption Reduces Blood Pressure in Patients With Hypertension by Altering Circulating Oxylipins via an α-Linolenic Acid–Induced Inhibition of Soluble Epoxide Hydrolase | Hypertension — https://www.ahajournals.org/doi/10.1161/HYPERTENSIONAHA.114.03179
- Impressive Antihypertensive Effect With Flaxseed — https://www.medscape.com/viewarticle/773981
- 筛查：区分磨碎籽、整籽、油及木酚素；《本草纲目》将亚麻与胡麻/油麻分条。

### 44｜sunflower-seed-kernels｜rate-limit retry

查询：`Sunflower seed kernels human randomized controlled trial direct consumption cardiometabolic outcomes nutrition composition DOI`
结果：success; retained 5 result cards

检索结果：
- Markers of Cardiovascular Risk in Postmenopausal Women with Type 2 Diabetes Are Improved by the Daily Consumption of Almonds or Sunflower Kernels: A Feeding Study — https://pmc.ncbi.nlm.nih.gov/articles/PMC4045277/
- Effect of Sunflower Seed Consumption on Blood Cholesterol Levels in Adults — https://clinicaltrials.gov/study/NCT07231367
- EFFECTS OF SUNFLOWER SEEDS ON CHOLESTEROL AND LOW-DENSITY LIPOPROTEIN LEVELS IN PATIENTS WITH DYSLIPIDEMIA — https://doi.org/10.22159/ajpcr.2019.v12i3.31032
- N/A — http://fmhr.org/index.php/fmhr/article/download/375/367/745
- Lipid profile of hyperlipidemic males after supplementation of ... — https://pmc.ncbi.nlm.nih.gov/articles/PMC8196128/
- 筛查：直接试验针对籽仁与杏仁的短期交叉比较；《本草纲目》“葵”条不直接投射为现代向日葵种仁。

### 45｜pumpkin-seeds｜rate-limit retry

查询：`《本草纲目》 南瓜子 原文 南瓜子味甘性温 本草拾遗 原典`
结果：success; retained 5 result cards

检索结果：
- 本草纲目拾遗-卷八 诸蔬部 南瓜蒂 — http://www.wenxue100.com/book_ZhongYi/518_646.thtml
- 南瓜·菜部·本草纲目 — http://www.wenxue360.com/guji/1939.html
- 本草纲目·南瓜 - 原文 译文 - 诗词汇 — https://www.shicihui.com/book/bencaogangmu/1939
- 本草纲目·菜部·南瓜原文翻译文及拼音 - 李时珍 - 云对雨古诗网 — https://www.yunduiyu.com/poetry-125140.html
- 南瓜（图）_中医药书籍汇集【中药材大全】 — https://www.zhongyaocai360.com/zhongyao/nangua.html
- 筛查：可核验材料涉及南瓜蒂/瓜瓤而非籽仁；不用于证明籽仁传统性味。
- 筛查：直接人体结果仅来自小型大学论文比较籽仁与籽油，不是安慰剂试验。

### 46｜chia-seed｜response-shape retry

查询：`Chia seed supplementation randomized controlled trial adults cardiometabolic outcomes dose duration systematic review DOI primary human trial`
结果：success; retained 5 result cards

检索结果：
- The Effect of Chia Seed on Blood Pressure, Body Composition, and Glycemic Control: A GRADE-Assessed Systematic Review and Dose-Response Meta-Analysis of Randomized Controlled Trials — https://doi.org/10.1093/nutrit/nuae113
- Effects of chia (Salvia hispanica. L) on anthropometric measures and other cardiometabolic risk factors: A systematic review and dose-response meta-analysis — https://doi.org/10.1016/j.ctim.2024.103086
- Clinical evidence on dietary supplementation with chia seed (Salvia hispanica L.): a systematic review and meta-analysis — https://doi.org/10.1093/nutrit/nux071
- Effects of chia seed (Salvia hispanica L.) supplementation on cardiometabolic health in overweight subjects: a systematic review and meta-analysis of RCTs — https://doi.org/10.1186/s12986-024-00847-3
- Review The Effects of Chia Seed ( Salvia hispanica  L.) Consumption on Blood Pressure and Body Composition in Adults: A Systematic Review and Meta-analysis of Randomized Controlled Trials — https://www.sciencedirect.com/science/article/abs/pii/S0149291824003564
- 筛查：核对 2017、2024 年综述间的结局差异，并保留阳性单项 RCT 的 T2D/限能量饮食边界。
