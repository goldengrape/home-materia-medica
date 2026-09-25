# QA Log — 训练后与运动补给场景（第 38 批）

> 日期：2026-09-25
> 研究深度：逐条按 R1/R2 配置定向检索，不是系统综述。
> 证据截止：2026-09-25。
> 检索记录：网页搜索 4 次、14 条查询；Exa 0 次、0 条结果；另核验原始研究、期刊页面及官方来源中的题名、DOI、样本、剂量和结局。

## 本批目录顺序

1. post-workout-protein-shake（训练后蛋白奶昔；R2）
2. sports-electrolyte-drink（电解质饮料配运动；R2）
3. high-protein-yogurt-snack（高蛋白酸奶加餐；R2）

## 搜与整的中间产物

### post-workout-protein-shake｜训练后蛋白奶昔

检索词：post exercise whey protein shake randomized crossover 25 g 8 healthy men 24870574；protein supplementation resistance training meta analysis 49 trials 1863 adults 28698222；ISSN position stand protein exercise 20 to 40 g dose 2017；post workout protein timing daily total intake resistance exercise meta analysis

- 检索同类训练场景的直接人体研究，并确认所研究的是饮料、食品或一般营养素。
- 核对原研究人群、运动形式、剂量、比较组、结局和随访时间。
- 区分急性肌肉蛋白合成指标、长期训练适应、体液指标和实际运动表现。
- None

- 研究底稿：references/entries/post-workout-protein-shake/research.md
- 整理摘要：references/entries/post-workout-protein-shake/summary.md

### sports-electrolyte-drink｜电解质饮料配运动

检索词：sports electrolyte drink randomized trial exercise heat sodium replacement plasma sodium 13 men 19295955；National Athletic Trainers Association fluid replacement physically active overhydration hyperhydration position statement 2017；personalized sodium replacement ultraendurance running heat randomized trial 9 participants 37944507；electrolyte sports drink short duration exercise water comparison adult trial

- 检索同类训练场景的直接人体研究，并确认所研究的是饮料、食品或一般营养素。
- 核对原研究人群、运动形式、剂量、比较组、结局和随访时间。
- 区分急性肌肉蛋白合成指标、长期训练适应、体液指标和实际运动表现。
- None

- 研究底稿：references/entries/sports-electrolyte-drink/research.md
- 整理摘要：references/entries/sports-electrolyte-drink/summary.md

### high-protein-yogurt-snack｜高蛋白酸奶加餐

检索词：high protein Greek yogurt snack randomized training trial 20g protein 12 weeks 31114790；Greek yogurt resistance training randomized trial thirty untrained young men DOI 10.3389/fnut.2019.00055；protein supplementation resistance training 49 studies meta analysis 1863 adults PMID 28698222；high protein yogurt sugar serving nutrition label composition brand comparison

- 检索同类训练场景的直接人体研究，并确认所研究的是饮料、食品或一般营养素。
- 核对原研究人群、运动形式、剂量、比较组、结局和随访时间。
- 区分急性肌肉蛋白合成指标、长期训练适应、体液指标和实际运动表现。
- None

- 研究底稿：references/entries/high-protein-yogurt-snack/research.md
- 整理摘要：references/entries/high-protein-yogurt-snack/summary.md

## 后续步骤与保留路径

- 判：先冻结摘要文本及 SHA-256，再读取 GitHub Environment API_KEYS 中的 JEV_API_KEY 发起 Jev v0.4 请求；原生 answers 不添加 M、不改写分数。
- 写：逐条生成 Mapping 和读者正文；正文参考文献保留英文原题与已核验 DOI。
- 本批配置：scripts/entry_batches/38-final-fitness-scenes.json。
- 冻结清单：qa/entry-batches/38-final-fitness-scenes-summary-sha256.txt。
- 冻结快照：qa/jev-entry-batches/38-final-fitness-scenes/pre-freeze/。
- 原生结果：qa/jev-entry-batches/38-final-fitness-scenes/raw/；原始文件另存为 GitHub Actions artifact。

## 身份红队

- 运动后乳清急性研究测量肌蛋白合成，不是长期增肌；长期训练研究涉及整日蛋白摄入和训练。
- 电解质饮料证据主要来自长时间运动和炎热环境；含钠饮料不能自动替代合理补液，也不能保证预防过度饮水。
- 希腊酸奶训练研究是多次补充与12周训练的组合，不能写成单次运动后酸奶试验。

## Actions 运行记录

待补录 workflow run、artifact、模型版本、原始 JSON 哈希与 QA 结果。
