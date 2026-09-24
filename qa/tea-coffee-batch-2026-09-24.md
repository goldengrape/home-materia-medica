# QA Log — 第三批茶与咖啡十条

> 日期：2026-09-24  
> 当前阶段：搜、整已完成；十份 summary 已冻结；Jev、M 与正文待 Actions 原始结果。
> 研究深度：R1 定向检索，不是系统综述。  
> 证据截止：2026-09-24。

## 本批目录顺序

1. `cold-brew-tea`（冷泡茶）
2. `sparkling-tea`（气泡茶）
3. `espresso`（意式浓缩咖啡）
4. `americano`（美式咖啡）
5. `hand-pour-coffee`（手冲咖啡）
6. `cold-brew-coffee`（冷萃咖啡）
7. `nitro-cold-brew`（氮气冷萃）
8. `latte`（拿铁）
9. `cappuccino`（卡布奇诺）
10. `mocha`（咖啡馆巧克力摩卡）

## 中间产物

- 搜：十份 `references/entries/<id>/research.md`，茶饮链接 `references/shared/tea-base/research.md`，咖啡链接 `references/shared/coffee-base/research.md`。每份记身份边界、检索式、直接/共享证据距离、D/E、安全、替代解释与停止理由。
- 整：十份 `summary.md` 只复述 dossier 中可追溯事实，不含 Jev 分类、四气五味、归经、score、Choice 或 M。
- 冻结：`qa/tea-coffee-summary-sha256.txt` 与 `qa/jev-tea-coffee-batch/pre-freeze/<id>.json`，快照逐份保留原文及 SHA-256。
- 判（待 Actions）：`.github/workflows/jev-tea-coffee-batch.yml` 使用 `environment: API_KEYS` 和 `${{ secrets.JEV_API_KEY }}`；runner 在首次 API 调用前逐份核验 manifest 与快照。原始输出将保存在 `qa/jev-tea-coffee-batch/raw/`，不在 raw 上加 M 或改分数。
- 写（待 Mapping）：十份 mapping 保存完整 probability/Noul、confidence 和方向分布；正文逐条回链 research、summary、mapping。论文引用保留英文题名，能核实 DOI 的附 DOI 链接，中文题名可并列。

## 证据边界与身份红队

- **冷泡茶：** Song 等 2021 年研究比较特定茶样的热泡与多个冷泡/超声处理方案，并研究高压加工下的微生物和储存属性。研究结果只适用于对应茶样、温度、时间与设备；不是消费者健康试验，不能把高压处理后的货架期移作家制冷泡茶。
- **气泡茶：** R1 未找到可代表全品类的成品营养抽样或直接人体试验。普通茶、苏打水及甜饮研究不拼接成气泡茶功效；茶叶咖啡因研究标明测量对象不是气泡成品。
- **意式浓缩：** EPICOR 观察队列对意式咖啡消费的关联不能证明因果；浓缩咖啡萃取化学研究说明粉粒和压粉设置会影响结果，不提供统一每份咖啡因量。
- **美式：** 按目录定义为浓缩加水。水量改变浓度；shot 数与实际萃取决定摄入量。R1 未找到以标准化美式为对象的直接人体试验。
- **手冲：** 目录级条目覆盖多种滤材；现有 `paper-filtered-coffee` 是纸滤子型。煮沸与纸滤的血脂随机试验不外推为所有布滤、金属滤手冲的结论，也不写成纸滤咖啡“降脂”。
- **冷萃/氮气冷萃：** 可得研究集中于萃取、组成、感官、泡沫与微生物，不是临床健康效应。变异较大，冷泡、冷藏或氮气不能自动说明低咖啡因或更健康。
- **拿铁/卡布奇诺：** EPICOR 食物问卷按 20% 咖啡、80% 牛奶估算两者，是该研究的记录规则，不是统一门店配方，也没有单独产品结局。
- **摩卡：** 本目录指 café mocha（espresso、牛乳、可可/巧克力），不指 Moka 壶制咖啡。意大利论文里的 moka/mocha 壶煮分类不得移作巧克力摩卡证据。

## 搜、整检查

- [x] 十份 R1 dossier 与十份 stage-2 summary 建立并完成语法检查。
- [x] 共享茶基底/咖啡母页只作背景，具体制法和配方重新评 D。
- [x] 定向检索关键工艺研究、意式咖啡队列、咖啡因萃取、冷萃/氮气泡沫和安全信息。
- [x] 论文参考文献保留英文题名；有 DOI 的研究链接到 DOI。
- [x] 十份冻结快照原文、manifest 与摘要 SHA-256 一致；summary 未夹带 Jev/M 分类。
- [ ] Jev 原始结果完整性、actual_model 与 workflow/artifact 元数据（待 Actions）。
- [ ] 十份 post-Jev Mapping 与 M 写作交接（待 raw）。
- [ ] 十篇正文及逐层追溯检查（待 Mapping）。

## Actions 运行结果

待补录 workflow run、结论、actual_model、artifact ID/digest、10 个 JSON 的原生答案数及冻结摘要哈希核验。
