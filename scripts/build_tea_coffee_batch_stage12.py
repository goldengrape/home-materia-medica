#!/usr/bin/env python3
"""Build stage-1 R1 dossiers and stage-2 summaries for the next ten catalog items."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

COMMON_COFFEE = (
    '共享证据节点：`references/shared/coffee-base/research.md`。该页收录咖啡饮用的直接急性人体试验、'
    '观察性长期结果、睡眠/咖啡因安全与冲煮差异；本条按食品形态降低直接性，不能用泛咖啡研究代替本配方试验。'
)
COMMON_TEA = (
    '共享证据节点：`references/shared/tea-base/research.md`。该页收录普通茶浸液、咖啡因与有限人体证据；'
    '碳酸、低温长时间浸泡或工厂处理后的茶饮不能自动视为母页中的同一暴露。'
)

PROFILES = {
    "cold-brew-tea": {
        "name": "冷泡茶",
        "identity": "茶叶或茶包在冷水/低温水中浸泡后饮用的茶浸液；不含必须添加糖、果汁或乳品。冷藏浸泡、冰水短泡和商业冷泡瓶装品可能是不同工艺。",
        "variables": "茶类、叶水比、温度、浸泡时间、切碎程度、过滤、储存和是否添加甜味料都会改变实际成分与感官。冷饮温度不作为传统寒热结论。",
        "composition": "没有覆盖所有茶种与家庭/商业工艺的统一营养或咖啡因数值；成品咖啡因不应由热泡茶的单个样本直接代替。",
        "direct": "R1 未找到可确认冷泡茶整体长期临床效果的直接人体干预。Song 等的研究是特定茶样的工艺与实验室评价，不是消费者健康试验。",
        "specific": "Song 等比较 100°C 冲泡 7 分钟的热茶，与静置冷泡（13 h/4°C）、超声水浴（120 min/0°C）及超声粉碎处理等冷泡条件；各冷泡组多酚浓度与热泡组无显著差异，咖啡因较低。该结果只适用于研究茶样和工艺设置。20 名训练评审参与感官评价；高压处理后的储存观察也不能等同于普通家庭冷泡的保质期。",
        "safety": "使用清洁容器并冷藏浸泡；尽量按产品/食品卫生说明及时饮用。实验室的高压处理和货架期结论不可移植到未经处理的家制茶。",
        "queries": ["cold-brew tea caffeine polyphenol human trial", "cold brew tea microbiological quality shelf-life processing", "冷泡茶 咖啡因 茶多酚 低温浸泡"],
        "parent": COMMON_TEA,
        "specific_refs": [
            'Song YC, Bi X, Zhou M, et al. “Effect of combined treatments of ultrasound and high hydrostatic pressure processing on the physicochemical properties, microbial quality and shelf-life of cold brew tea.” *International Journal of Food Science & Technology*. 2021;56:5977–5988. DOI: [10.1111/ijfs.15245](https://doi.org/10.1111/ijfs.15245).',
        ],
        "body": "冷泡茶是茶叶以冷水或低温水浸泡所得；茶种、叶水比、时间与温度都会影响成品。一个工艺研究在特定茶样中观察到冷泡茶多酚与热泡相近、咖啡因较低，但不同冷泡方式和热泡参数不能推广成所有茶的一般规律。它没有测试长期健康效果。",
        "evidence_body": "Song 等的实验比较了冷泡茶工艺、微生物指标与储存，并非消费者健康试验。高压处理所得货架期不能代表普通家庭自制冷泡茶。",
        "care": "用清洁容器低温浸泡，按食品卫生建议及时饮用；茶叶种类、浸泡条件和总量决定实际咖啡因。",
        "body_refs": [
            'Song YC, Bi X, Zhou M, et al. “Effect of combined treatments of ultrasound and high hydrostatic pressure processing on the physicochemical properties, microbial quality and shelf-life of cold brew tea.” *International Journal of Food Science & Technology*. 2021;56:5977–5988. DOI: [10.1111/ijfs.15245](https://doi.org/10.1111/ijfs.15245).',
        ],
        "taste_m": {"苦": "冷泡茶感官苦味随茶种与浸泡条件变化，仅作感官类推。"},
    },
    "sparkling-tea": {
        "name": "气泡茶",
        "identity": "以茶浸液或茶提取物为主体、加入二氧化碳形成气泡的饮料；可以无糖，也可能含糖、果汁、酸味料或香料。",
        "variables": "茶基底、茶液浓度、气泡量、甜味剂、果汁、酸味剂、每份容量与咖啡因均不固定；商品名称无法单独说明真实配方。",
        "composition": "本轮 R1 未找到能代表整个气泡茶品类的营养抽样或标准化商品配方；应按标签核对糖、甜味剂和咖啡因。",
        "direct": "以气泡茶为固定食品的直接人体干预或长期结局研究，本轮 R1 未检得。普通茶、苏打水或含糖饮料研究各自对应不同对象，不能拼接成气泡茶的功效证据。",
        "specific": "检索主要用于核对产品身份和直接证据；未发现统一类别定义、足以量化成分范围的代表性抽样或气泡茶人体试验。未发现仅限于本轮检索范围，不代表全球不存在任何相关研究。",
        "safety": "查看具体每份的添加糖、甜味剂、咖啡因和酸味配料；不要把“茶饮”或“气泡”名称等同无糖、低咖啡因或特定健康效果。",
        "queries": ["sparkling tea beverage human intervention trial composition", "carbonated tea drink caffeine sugar survey", "气泡茶 二氧化碳 茶饮 人体 试验 配方"],
        "parent": COMMON_TEA,
        "specific_refs": [],
        "body": "气泡茶没有单一配方：茶底可搭配二氧化碳，也可能另加糖、果汁、甜味剂或酸味料。本轮 R1 检索未找到能代表全品类的营养抽样或直接人体试验，因此不套用普通茶、苏打水或汽水的健康结果。实际糖和咖啡因以每款标签为准。",
        "evidence_body": "产品之间的茶液浓度、甜味和气泡量差异较大；现有相邻饮料研究不能当作气泡茶的直接证据。",
        "care": "逐项核对糖、甜味剂、茶底与每份容量；“气泡”不说明咖啡因或糖含量。",
        "body_refs": [
            'Yong L, et al. “Quantitative probabilistic assessment of caffeine intake from tea in Chinese adult consumers based on nationwide caffeine content determination and tea consumption survey.” *Food and Chemical Toxicology*. 2022;165:113102. DOI: [10.1016/j.fct.2022.113102](https://doi.org/10.1016/j.fct.2022.113102). This measured tea-leaf samples, not sparkling tea.',
        ],
        "taste_m": {},
    },
    "espresso": {
        "name": "意式浓缩咖啡",
        "identity": "将热水在压力下通过细研磨咖啡粉获得的小份浓缩咖啡；单份/双份、豆种和设备设置会改变实际暴露。加水后的美式与加奶咖啡另列。",
        "variables": "豆种与拼配、烘焙、粉量、研磨、压粉、压力、温度、萃取时间和shot数都会改变咖啡因及其他成分。浓缩并不意味着每份咖啡因必定高于大杯滴滤咖啡。",
        "composition": "没有跨店铺通用的单份咖啡因值；共享咖啡母页引用的 EFSA 估算仅为代表性食用值，不能代替具体商品检测。",
        "direct": "Grioni 等 EPICOR 队列观察 43,249 名意大利成年人，平均随访 10.9 年；该研究以 30 mL 标准 espresso 杯估算意式咖啡摄入，超过 2 杯/日与较高冠心病发生率相关，但属于观察性关联，并非因果结论，也不是对单一浓缩配方的随机试验。",
        "specific": "Kuhn 等在商用机器下研究细研磨咖啡 espresso 的咖啡因与葫芦巴碱时序萃取，显示粉粒与压粉条件是实验因素，支持配方/操作改变萃取，不提供每家咖啡馆固定剂量。Wuerges 等仅用一种中度烘焙阿拉比卡咖啡、每条件 5 次制备，测得特定 espresso 样品的咖啡二萜；结果不能推广到不同豆种和设备。",
        "safety": "以实际shot数和产品咖啡因标签计算总摄入；敏感者、晚间饮用者及妊娠期应结合自身情况和权威咖啡因指导，不把杯数当成固定剂量。",
        "queries": ["espresso coffee caffeine extraction particle size tamping pressure human cohort", "Italian espresso coffee coronary heart disease cohort", "espresso coffee cafestol kahweol comparison preparation method"],
        "parent": COMMON_COFFEE,
        "specific_refs": [
            'Grioni S, Agnoli C, Sieri S, et al. “Espresso Coffee Consumption and Risk of Coronary Heart Disease in a Large Italian Cohort.” *PLOS ONE*. 2015;10(5):e0126550. DOI: [10.1371/journal.pone.0126550](https://doi.org/10.1371/journal.pone.0126550).',
            'Kuhn M, Lang S, Bezold F, Minceva M, Briesen H. “Time-resolved extraction of caffeine and trigonelline from finely-ground espresso coffee with varying particle sizes and tamping pressures.” *Journal of Food Engineering*. 2017;206:37–47. DOI: [10.1016/j.jfoodeng.2017.03.002](https://doi.org/10.1016/j.jfoodeng.2017.03.002).',
            'Wuerges KL, et al. “Kahweol and cafestol in coffee brews: comparison of preparation methods.” *Revista Ciência Agronômica*. 2020;51(1). DOI: [10.5935/1806-6690.20200005](https://doi.org/10.5935/1806-6690.20200005).',
        ],
        "body": "意式浓缩咖啡以压力热水通过细研磨咖啡粉制成；粉量、研磨、压粉、萃取时间与shot数都会改变一份的实际咖啡因。EPICOR 意大利队列以 30 mL 标准 espresso 杯估算意式咖啡摄入，观察到超过每日两杯者冠心病发生率较高；这是观察性关联，不能证明单一浓缩配方导致疾病。",
        "evidence_body": "实验室研究表明espresso萃取受粉粒和操作条件影响；意式队列结果是关联信号，不足以推成预防或致病结论。",
        "care": "按实际shot数、咖啡因信息和个人敏感性判断摄入；小杯不代表咖啡因含量固定。",
        "body_refs": [
            'Grioni S, Agnoli C, Sieri S, et al. “Espresso Coffee Consumption and Risk of Coronary Heart Disease in a Large Italian Cohort.” *PLOS ONE*. 2015;10(5):e0126550. DOI: [10.1371/journal.pone.0126550](https://doi.org/10.1371/journal.pone.0126550). The observational cohort used 30 mL standard espresso cups to estimate Italian coffee intake.',
            'Kuhn M, Lang S, Bezold F, Minceva M, Briesen H. “Time-resolved extraction of caffeine and trigonelline from finely-ground espresso coffee with varying particle sizes and tamping pressures.” *Journal of Food Engineering*. 2017;206:37–47. DOI: [10.1016/j.jfoodeng.2017.03.002](https://doi.org/10.1016/j.jfoodeng.2017.03.002).',
        ],
        "taste_m": {"苦": "浓缩咖啡有苦味感官依据；焙度、豆种和萃取改变感受，仅作类推。"},
    },
    "americano": {
        "name": "美式咖啡",
        "identity": "以一份或多份意式浓缩加入热水或冷水制成的黑咖啡；冰块、shot 数与杯量按门店而异。",
        "variables": "浓缩shot数、加水量、豆种、萃取参数与杯量决定实际咖啡因浓度和总量；加水会稀释浓度，但不能单独说明shot中咖啡因总量。",
        "composition": "R1 未找到代表美式咖啡整体的营养或咖啡因抽样；标签和店家配方比通用咖啡杯数更适合估算。",
        "direct": "本轮 R1 未找到美式咖啡为固定干预食品的直接人体试验。浓缩咖啡、通用黑咖啡或孤立咖啡因试验不等同于各种shot数和稀释比例的美式。",
        "specific": "美式属于浓缩加水的配方型黑咖啡；目前可用的浓缩咖啡萃取分析解释shot组成会随原料及操作改变。水量本身会改变浓度，但身体摄入总量还取决于shot数与实际萃取。",
        "safety": "计入所有shot与其他饮品、食物来源的咖啡因；对睡眠或焦虑敏感者按自身反应调整时段与份量。",
        "queries": ["Americano coffee caffeine clinical trial health effects", "Americano espresso water recipe caffeine dose research", "Americano coffee composition survey"],
        "parent": COMMON_COFFEE,
        "specific_refs": [
            'Kuhn M, Lang S, Bezold F, Minceva M, Briesen H. “Time-resolved extraction of caffeine and trigonelline from finely-ground espresso coffee with varying particle sizes and tamping pressures.” *Journal of Food Engineering*. 2017;206:37–47. DOI: [10.1016/j.jfoodeng.2017.03.002](https://doi.org/10.1016/j.jfoodeng.2017.03.002).',
        ],
        "body": "美式咖啡通常由意式浓缩加热水或冷水调制；杯量和shot数会因门店而变。水量会稀释浓度，但咖啡因总量还取决于浓缩份数与萃取条件。本轮未找到能代表美式全品类的营养抽样或直接人体试验。",
        "evidence_body": "浓缩萃取研究只能帮助理解其咖啡基底，不能替代实际美式商品的咖啡因测量。",
        "care": "按shot数量和产品配方确认咖啡因；大杯与高咖啡因不必然等义。",
        "body_refs": [
            'Kuhn M, Lang S, Bezold F, Minceva M, Briesen H. “Time-resolved extraction of caffeine and trigonelline from finely-ground espresso coffee with varying particle sizes and tamping pressures.” *Journal of Food Engineering*. 2017;206:37–47. DOI: [10.1016/j.jfoodeng.2017.03.002](https://doi.org/10.1016/j.jfoodeng.2017.03.002).',
        ],
        "taste_m": {"苦": "咖啡基底的苦味依萃取和稀释变化，仅作感官类推。"},
    },
    "hand-pour-coffee": {
        "name": "手冲咖啡",
        "identity": "以人工分段或连续注水穿过研磨咖啡粉和滤材制得的黑咖啡，滤材可为纸、布或金属。项目已有更窄的纸滤手冲子项 `paper-filtered-coffee`，本条覆盖目录级手冲类别并与其交叉引用。",
        "variables": "滤材、粉水比、研磨、注水速度、水温、焙度和冲煮器具都会影响咖啡浓度与脂溶性成分；只有纸滤方式可直接借用纸滤对照试验。",
        "composition": "不同滤材和咖啡配方没有统一每杯咖啡因或二萜值；已有纸滤子条的数值与结论限定于其配方边界。",
        "direct": "针对广义手冲咖啡的直接健康试验有限。Bak 与 Grobbee 的直接人体随机试验比较高量煮沸咖啡、纸滤咖啡和不饮咖啡，支持冲煮/过滤方式影响血脂；它不是对所有手冲壶、滤布或金属滤网的试验。",
        "specific": "共享纸滤子条引用的随机对照研究报告煮沸相较纸滤咖啡总胆固醇上升，而纸滤组与不饮咖啡组无显著差异；不得写成手冲咖啡本身降脂。非纸滤手冲的二萜含量可能不同，归入未解决变量。",
        "safety": "按豆种、粉量、杯量与饮用时段估算咖啡因；若使用布/金属滤材，不能直接套用纸滤对照的成分结论。",
        "queries": ["pour-over coffee paper cloth metal filter diterpenes trial", "filtered boiled coffee randomized serum cholesterol trial", "手冲咖啡 滤材 咖啡因 二萜"],
        "parent": COMMON_COFFEE,
        "specific_refs": [
            'Bak AAA, Grobbee DE. “The Effect on Serum Cholesterol Levels of Coffee Brewed by Filtering or Boiling.” *New England Journal of Medicine*. 1989;321:1432–1437. DOI: [10.1056/NEJM198911233212103](https://doi.org/10.1056/NEJM198911233212103).',
        ],
        "body": "手冲咖啡以人工注水经过咖啡粉与滤材制得；纸、布或金属滤材及冲煮参数会改变成分。随机人体对照支持高量煮沸咖啡相较纸滤咖啡升高血清胆固醇，但不能反推纸滤手冲能降脂，也不能把结果套给所有滤材。纸滤手冲的窄范围研究见[相关条目](paper-filtered-coffee.md)。",
        "evidence_body": "纸滤与煮沸咖啡的对照试验不是广义手冲各种器具的试验；细节见现有 paper-filtered-coffee 子项。",
        "care": "滤材与冲煮比例影响组成；咖啡因暴露还取决于粉量、杯量和时段。",
        "body_refs": [
            'Bak AAA, Grobbee DE. “The Effect on Serum Cholesterol Levels of Coffee Brewed by Filtering or Boiling.” *New England Journal of Medicine*. 1989;321:1432–1437. DOI: [10.1056/NEJM198911233212103](https://doi.org/10.1056/NEJM198911233212103).',
        ],
        "taste_m": {"苦": "无糖黑咖啡有苦味感官依据，烘焙与冲煮影响强度，仅作类推。"},
    },
    "cold-brew-coffee": {
        "name": "冷萃咖啡",
        "identity": "研磨咖啡在常温或冷水中浸泡一段时间后过滤所得咖啡；冷藏浸泡与室温浸泡不等价，冰镇热萃咖啡另属热萃后冷却。",
        "variables": "水温、时间、粉水比、研磨、豆种、烘焙、搅动和成品稀释都会改变咖啡因、绿原酸、酸度与口感；“冷萃”没有统一标准浓度。",
        "composition": "实验室与消费者调查显示冷萃定义和配方变异较大；咖啡因或酸度不能由冷热标签单独推定。实际产品以浓缩液稀释比例和标签为准。",
        "direct": "R1 未找到冷萃咖啡整体长期临床因果试验。现有直接研究主要是实验室成分、萃取、感官与微生物指标，不能说明冷萃比热咖啡更健康。",
        "specific": "Claassen 等的试点项目含消费者制备调查、感官及实验室样品研究，报告市售/自制做法高度不同，并指出冷泡产品的卫生管理值得关注；这些观察不是所有商品污染或患病风险的估计。Fuller 与 Rao 在特定豆样、研磨和浸泡条件下测咖啡因与 3-CGA 萃取，显示时间、焙度及研磨影响浓度；不构成通用杯量。",
        "safety": "冷萃是低温长时浸泡饮品；制作和保存应使用清洁器具、依标签冷藏，并遵守产品建议时限。实验室微生物筛查不是对所有冷萃产品的风险判定。",
        "queries": ["cold brew coffee composition caffeine extraction conditions human trial", "cold brew coffee microbial hazards ready-to-drink samples", "cold brew coffee acidity myth titratable acidity"],
        "parent": COMMON_COFFEE,
        "specific_refs": [
            'Claassen L, Rinderknecht M, Porth T, et al. “Cold Brew Coffee—Pilot Studies on Definition, Extraction, Consumer Preference, Chemical Characterization and Microbiological Hazards.” *Foods*. 2021;10(4):865. DOI: [10.3390/foods10040865](https://doi.org/10.3390/foods10040865).',
            'Fuller M, Rao NZ. “The Effect of Time, Roasting Temperature, and Grind Size on Caffeine and Chlorogenic Acid Concentrations in Cold Brew Coffee.” *Scientific Reports*. 2017;7:17979. DOI: [10.1038/s41598-017-18247-4](https://doi.org/10.1038/s41598-017-18247-4).',
        ],
        "body": "冷萃咖啡是咖啡粉经常温或冷水浸泡后过滤；水温、时间、粉水比、研磨与稀释都会改变成品。实验室和试点研究显示制法差异较大，咖啡因不能仅凭“冷萃”名称判断，也没有证据表明低温萃取本身带来临床健康优势。",
        "evidence_body": "已发表研究集中在配方、化学成分、感官和微生物条件，未建立冷萃咖啡特异的长期健康效果。",
        "care": "使用清洁器具并按产品说明冷藏保存；咖啡因按浓缩程度、稀释比例与杯量核对。",
        "body_refs": [
            'Claassen L, Rinderknecht M, Porth T, et al. “Cold Brew Coffee—Pilot Studies on Definition, Extraction, Consumer Preference, Chemical Characterization and Microbiological Hazards.” *Foods*. 2021;10(4):865. DOI: [10.3390/foods10040865](https://doi.org/10.3390/foods10040865).',
            'Fuller M, Rao NZ. “The Effect of Time, Roasting Temperature, and Grind Size on Caffeine and Chlorogenic Acid Concentrations in Cold Brew Coffee.” *Scientific Reports*. 2017;7:17979. DOI: [10.1038/s41598-017-18247-4](https://doi.org/10.1038/s41598-017-18247-4).',
        ],
        "taste_m": {"苦": "冷萃黑咖啡可能呈苦，强度受配方影响，仅作感官类推。"},
    },
    "nitro-cold-brew": {
        "name": "氮气冷萃",
        "identity": "冷萃咖啡经氮气注入或加压分配形成细密泡沫与特殊口感的饮料；基底浓度、氮气系统、杯量和是否另加糖奶不固定。",
        "variables": "咖啡品种、焙度、浸泡条件、研磨、氮气比例、压力与分配温度共同影响泡沫和香气；不同门店配方的咖啡因与添加物可能不同。",
        "composition": "未找到代表全品类的氮气冷萃营养抽样；具体咖啡因以冷萃基底、稀释、shot/浓缩液份量及商品标签为准。氮气形成的泡沫不说明咖啡因减少。",
        "direct": "R1 未找到氮气冷萃的直接人体健康试验。研究集中在泡沫稳定性、提取条件、消费者偏好和食品微生物学，不支持疾病预防或治疗结论。",
        "specific": "Yu 等实验室研究改变阿拉比卡/罗布斯塔、焙度、萃取温度、粉水比例、粒径及成品温度，发现氮气冷萃的起泡性与泡沫稳定性受这些条件显著影响。Claassen 等试点研究展示氮气分配作为冷萃呈现方式，并提出冷泡卫生管理边界。以上是产品物理/工艺观察，不是对人体作用的试验。",
        "safety": "按冷萃产品说明冷藏与保存；另看糖浆、奶和杯量。氮气带来的绵密口感不能用来推定咖啡因含量、营养或“更健康”。",
        "queries": ["nitro cold brew coffee human health trial caffeine content", "nitrogen-infused cold brew foam stability study", "nitro coffee consumer microbiological safety"],
        "parent": COMMON_COFFEE,
        "specific_refs": [
            'Yu M, et al. “Investigation of the factors affecting foamability and foam stability of cold brew coffee.” *Journal of the Science of Food and Agriculture*. 2022;102:5875–5882. DOI: [10.1002/jsfa.11937](https://doi.org/10.1002/jsfa.11937).',
            'Claassen L, Rinderknecht M, Porth T, et al. “Cold Brew Coffee—Pilot Studies on Definition, Extraction, Consumer Preference, Chemical Characterization and Microbiological Hazards.” *Foods*. 2021;10(4):865. DOI: [10.3390/foods10040865](https://doi.org/10.3390/foods10040865).',
        ],
        "body": "氮气冷萃是在冷萃咖啡中注入氮气，形成细密泡沫和较绵密口感。实验室研究发现豆种、烘焙、粉水比、研磨和温度会影响泡沫表现；这些是工艺/物理指标，不等于营养或健康优势。",
        "evidence_body": "目前 R1 找到的氮气冷萃研究关注泡沫、制备和产品微生物特征，没有验证直接人体临床结局。",
        "care": "按冷萃基底、稀释、杯量和附加配料核对实际暴露；氮气泡沫不代表低咖啡因。",
        "body_refs": [
            'Yu M, et al. “Investigation of the factors affecting foamability and foam stability of cold brew coffee.” *Journal of the Science of Food and Agriculture*. 2022;102:5875–5882. DOI: [10.1002/jsfa.11937](https://doi.org/10.1002/jsfa.11937).',
        ],
        "taste_m": {"苦": "咖啡基底可呈苦，氮气改变质地但不固定甜味，仅作感官类推。"},
    },
    "latte": {
        "name": "拿铁",
        "identity": "由意式浓缩咖啡与较多蒸汽牛乳/奶泡组成的咖啡饮品；商品规格、牛乳脂肪、杯量和糖浆会改变整体。植物饮与风味拿铁属于配方变体。",
        "variables": "浓缩shot数、奶量、乳脂、乳糖、植物饮类别、糖浆、杯量和温度都影响咖啡因、能量与糖；名称“拿铁”不足以确定营养。",
        "composition": "没有统一拿铁市场营养值。EPICOR 队列在其问卷计算中将拿铁/卡布奇诺近似按 20% 咖啡、80% 牛奶处理；这是研究估算规则，不是实际门店配方标准。",
        "direct": "本轮 R1 未找到可确认拿铁本身临床因果效果的直接随机试验。咖啡研究母页的黑咖啡试验对加奶拿铁只属间接证据；意式咖啡队列将奶咖按问卷比例估算，未给出拿铁单独效应。",
        "specific": "EPICOR 的饮食问卷把 cappuccino 与 café latte 设为 20% coffee/80% milk，以便总摄入估算；这一研究操作化有助于说明类别定义不固定，不足以代表各国/店铺配方。加奶红茶研究不是拿铁咖啡研究。",
        "safety": "查看奶基底、咖啡因shot数和糖浆；乳蛋白过敏与乳糖耐受取决于具体配料。无糖不等于无咖啡因。",
        "queries": ["caffe latte human randomized trial health outcome", "coffee milk latte cohort outcomes milk proportion", "latte coffee nutrition composition survey"],
        "parent": COMMON_COFFEE,
        "specific_refs": [
            'Grioni S, Agnoli C, Sieri S, et al. “Espresso Coffee Consumption and Risk of Coronary Heart Disease in a Large Italian Cohort.” *PLOS ONE*. 2015;10(5):e0126550. DOI: [10.1371/journal.pone.0126550](https://doi.org/10.1371/journal.pone.0126550).',
        ],
        "body": "拿铁通常以浓缩咖啡加牛乳和奶泡调制；shot数、奶量、奶种、杯量与糖浆会改变整杯成分。大型意大利咖啡队列在食物问卷中把拿铁和卡布奇诺近似按 20% 咖啡、80% 牛奶估算；这只是该研究的记录方法，不是通用配方，也未证明拿铁的单独健康效果。",
        "evidence_body": "现有咖啡人体研究多测黑咖啡或按问卷估算混合咖啡；本轮 R1 未找到拿铁本身的直接临床试验。",
        "care": "按具体奶基底、shot数、糖浆和容量核对；有乳过敏或乳糖耐受问题者查看配料。",
        "body_refs": [
            'Grioni S, Agnoli C, Sieri S, et al. “Espresso Coffee Consumption and Risk of Coronary Heart Disease in a Large Italian Cohort.” *PLOS ONE*. 2015;10(5):e0126550. DOI: [10.1371/journal.pone.0126550](https://doi.org/10.1371/journal.pone.0126550). The questionnaire estimated latte/cappuccino as 20% coffee and 80% milk; this was a study-specific assumption, not a universal recipe.',
        ],
        "taste_m": {"苦": "咖啡基底可能呈苦，牛乳、植物饮或糖浆改变风味，仅作感官类推。", "甘": "牛乳/植物饮与糖浆可产生甜感，具体产品不同，仅作感官类推。"},
    },
    "cappuccino": {
        "name": "卡布奇诺",
        "identity": "以意式浓缩咖啡、热牛乳和奶泡组合的咖啡饮品；传统比例与现代门店杯型并不统一。",
        "variables": "shot数、牛乳量、泡沫比例、乳脂、糖浆与杯量影响咖啡因及营养；外观泡沫不能准确推回咖啡基底份量。",
        "composition": "没有统一卡布奇诺营养值。EPICOR 队列将其与拿铁一起在饮食估算中假定为 20% 咖啡、80% 牛奶；该问卷比例不等同标准配方。",
        "direct": "本轮 R1 未找到卡布奇诺作为独立、配方固定干预的临床试验。对咖啡因和睡眠可参考咖啡母页的通用证据，但需按实际shot数调整直接性。",
        "specific": "EPICOR 研究将 cappuccino 和 café latte 一并按 20% coffee/80% milk 估算摄入，没有报告卡布奇诺独立结局。配方与杯型差异使该类队列估算不宜转成成品含量。",
        "safety": "核对杯型、浓缩份数、奶种与额外糖；不能仅凭泡沫量判断咖啡因。",
        "queries": ["cappuccino clinical trial health effects", "cappuccino coffee milk composition cohort", "cappuccino nutrition caffeine serving size research"],
        "parent": COMMON_COFFEE,
        "specific_refs": [
            'Grioni S, Agnoli C, Sieri S, et al. “Espresso Coffee Consumption and Risk of Coronary Heart Disease in a Large Italian Cohort.” *PLOS ONE*. 2015;10(5):e0126550. DOI: [10.1371/journal.pone.0126550](https://doi.org/10.1371/journal.pone.0126550).',
        ],
        "body": "卡布奇诺由浓缩咖啡、热牛乳和奶泡组合，店家杯型与比例并不统一。意大利队列曾把卡布奇诺和拿铁一起按 20% 咖啡、80% 牛奶估算摄入；这只是问卷估算值，未报告卡布奇诺单独健康结局，也不能作为营养标签。",
        "evidence_body": "本轮 R1 未找到固定配方卡布奇诺的直接临床试验；咖啡母页中的结果需按该配方降低直接性。",
        "care": "按实际shot数、奶量、糖浆和容量判断；泡沫多不等于咖啡因少。",
        "body_refs": [
            'Grioni S, Agnoli C, Sieri S, et al. “Espresso Coffee Consumption and Risk of Coronary Heart Disease in a Large Italian Cohort.” *PLOS ONE*. 2015;10(5):e0126550. DOI: [10.1371/journal.pone.0126550](https://doi.org/10.1371/journal.pone.0126550).',
        ],
        "taste_m": {"苦": "咖啡底可呈苦，乳与泡沫比例影响感官，仅作类推。", "甘": "牛乳带来甜润感，具体产品与加糖情况不同，仅作类推。"},
    },
    "mocha": {
        "name": "摩卡",
        "identity": "本条“摩卡”指咖啡馆常见的 espresso 加可可/巧克力与牛乳饮品；不指以 Moka 壶煮出的意式壶煮咖啡。不同商品可能再加糖浆、奶油或额外巧克力。",
        "variables": "咖啡shot数、巧克力种类与量、牛乳脂肪、糖浆、奶油和杯量都会改变咖啡因、糖与能量。",
        "composition": "本轮 R1 未找到代表摩卡全品类的营养抽样或标准配方；实际糖、可可、奶及咖啡因应按配方/标签确认。",
        "direct": "本轮 R1 未找到巧克力咖啡饮品本身的直接人体试验。Grioni 等意大利队列研究讨论的是 espresso 与 Moka 壶式咖啡，不是加巧克力的咖啡馆摩卡，不能移作本条的人体结局。",
        "specific": "EPICOR 观察性研究及意大利壶煮传统涉及的英文 mocha/moka 指 Moka 壶制法，不是含可可的 café mocha；两种身份必须分开。该队列没有分析本条成品。",
        "safety": "关注咖啡因总量、巧克力/糖浆添加糖与奶类过敏原；品名不能说明每份能量或咖啡因。",
        "queries": ["mocha coffee drink clinical trial health effects", "mocha espresso chocolate milk nutrition composition study", "espresso mocha Italian cohort outcome"],
        "parent": COMMON_COFFEE,
        "specific_refs": [
            'Grioni S, Agnoli C, Sieri S, et al. “Espresso Coffee Consumption and Risk of Coronary Heart Disease in a Large Italian Cohort.” *PLOS ONE*. 2015;10(5):e0126550. DOI: [10.1371/journal.pone.0126550](https://doi.org/10.1371/journal.pone.0126550).',
        ],
        "body": "本条摩卡指 espresso 加可可/巧克力与牛乳的饮品，不是 Moka 壶咖啡。糖浆、奶油和杯量会改变糖与能量。本轮未找到本条成品的直接人体试验；意大利咖啡队列中的 mocha/moka 指壶煮咖啡，不能移作巧克力摩卡证据。",
        "evidence_body": "需区分英语 mocha/moka 在部分意大利咖啡研究中指 Moka 壶制法；该研究没有测试本条巧克力咖啡饮品。",
        "care": "按实际巧克力、糖浆、奶油和浓缩份量查看标签；需控制糖、能量或咖啡因时不要只看饮品名称。",
        "body_refs": [
            'Grioni S, Agnoli C, Sieri S, et al. “Espresso Coffee Consumption and Risk of Coronary Heart Disease in a Large Italian Cohort.” *PLOS ONE*. 2015;10(5):e0126550. DOI: [10.1371/journal.pone.0126550](https://doi.org/10.1371/journal.pone.0126550). Its moka/“mocha” refers to pot-brewed coffee, not chocolate mocha.',
        ],
        "taste_m": {"苦": "咖啡/可可可产生苦味，配方影响强度，仅作类推。", "甘": "牛乳、巧克力或糖浆可带来甜味，依产品变化，仅作类推。"},
    },
}


def dossier(entry_id: str, p: dict) -> str:
    terms = "；".join(f"`{q}`" for q in p["queries"])
    refs = "\n".join(f"{i}. {r}" for i, r in enumerate(p["specific_refs"], 1))
    if not refs:
        refs = "本轮 R1 未检得可直接支持气泡茶品类健康效果的核心论文；检索边界与共享茶基底来源见上。"
    return f"""# Research Dossier — {p['name']}

> entry_id: {entry_id}  
> entry_type: catalog beverage  
> research_depth: R1  
> status: research_ready_R1  
> evidence_cutoff: 2026-09-24  
> shared_parent: {'tea-base' if entry_id in {'cold-brew-tea','sparkling-tea'} else 'coffee-base'}

## 1. 身份与边界

本条定义：{p['identity']}

主要变量：{p['variables']}

身份信心：中；各地/品牌配方名称并非统一标准。复合品只在上列定义内纳入，邻接的加糖、加奶或瓶装品按真实配方判定。

## 2. 核心问题与检索

核心问题：成品的实际成分是什么；是否有以本条为对象的直接人体结果；共享茶/咖啡证据能迁移到什么距离；加工、剂量和配方带来哪些安全差异。

2026-09-24 定向检索词：{terms}。

检索范围为 R1 定向探索，核对出版社、PubMed/PMC、开放期刊或官方机构页面可得的摘要/正文；未找到仅表示本次策略与范围的结果，不声明全球不存在研究。产品配方抽样与人体结局分开记录。

## 3. 共享证据与直接性

{p['parent']}

共享证据不能自动补足本条的配方或健康结局。对本条特异数据按 D0（同一明确产品）、D1（近似制法/组成）、D2（共享基底或不同制品）、D3（单一成分/机制）重新判断。

## 4. 传统来源层级

{'茶叶母页保留《本草纲目》茶条的历史记载；冷泡方式是现代饮用/制备变量，不代表原文专指冷泡。' if entry_id in {'cold-brew-tea','sparkling-tea'} else '咖啡母页中的“醒神”等记录来自近现代中药资料公开转录，不作为古代本草共识；目前不将一般咖啡记录自动扩展为本条每种现代配方的直接传统属性。'}

## 5. 组成与暴露

{p['composition']}

本条可能影响真实暴露的关键项：{p['variables']}

## 6. 本条直接证据卡

### 命题 A｜本条特异的人体效果

{p['direct']}

- 直接性：按本条/相邻配方分别为 D0–D3；不得把机制或配料研究写成成品临床试验。
- E：对本条预防/治疗慢性疾病的因果效果，本轮为 E-0（未建立）；共享母页的短时警觉/睡眠结论按实际配方降低直接性。

### 命题 B｜本条工艺、化学或暴露特点

{p['specific']}

- 证据性质：{('实验室工艺与组成研究' if entry_id in {'cold-brew-tea','espresso','cold-brew-coffee','nitro-cold-brew','hand-pour-coffee'} else '配方身份与共享研究边界')}。
- 直接性：研究中被定义/制备的特定样品 D0；对不同品牌与配方为 D1–D3。
- 限制：样本、产地、工艺、人群/研究终点不能超出原研究外推。

## 7. 分结局综合与证据等级

### 组成/咖啡因

{p['composition']} 未测成分应标未知，不能拿普通茶、黑咖啡或另一杯型补数。

### 人体健康结果

{p['direct']}

共享母页的短期咖啡/茶人体试验并非本条完整配方的直接试验；长期队列是相关性研究。当前允许描述研究样品、研究设计及其限制；不允许写成“本条防病/治疗”。

### 工艺与感官

{p['specific']}

感官变化可作为食品描述，不自动证明临床效果或传统概念。

## 8. 安全与实用选择

{p['safety']}

一般咖啡因指导见共享母页；数值按所有来源合计，不换算为所有杯型通用的“几杯”。过敏与乳糖问题只在真实含乳配方下适用。

## 9. 本草映射候选（供第三阶段回查，不作结论）

- 茶饮：共享茶叶母本只作来源层级；温度与浸泡形式不是本草四气的直接证据。
- 咖啡：共享咖啡母页记录现代资料中的功能语言；它不自动决定四气、五味、归经或方向。
- 配方变化可能改变感官；感觉不等于药性、脏腑功能或疗效。
- 本阶段不预写分类、模型结果或 M 等级；待冻结摘要完成分类后，再逐项回 Research Dossier 评注。

## 10. 未知、冲突与停止规则

仍未知：不同店铺/家庭的真实配方与份量分布；本条长期人体健康结局；具体产品的咖啡因/糖/能量检测值；不同冲煮/滤材是否改变个体反应。

替代解释：豆种/茶种、烘焙或加工、液体份量、含糖奶料、摄入时段、习惯化、研究对象和结局不同。

本轮停止状态：`R1_scope_met`。已覆盖食品身份、可得的本条直接工艺/人群研究、共享母页证据、安全和核心未知。若出现同配方的大型人体试验、代表性成品调查或重要安全警报，再定向重开。

## 11. 核心参考资料

{refs}

完整共享证据与来源边界见：`references/shared/{'tea-base' if entry_id in {'cold-brew-tea','sparkling-tea'} else 'coffee-base'}/research.md`。
"""


def summary(entry_id: str, p: dict) -> str:
    tradition = (
        "茶叶母页有传统历史记载，但这不是古籍对低温浸泡方式的专门记录。"
        if entry_id in {"cold-brew-tea", "sparkling-tea"}
        else "咖啡的共享资料来自近现代文献；不能将其当作古代本草对本条现代制品的直接记录。"
    )
    common = (
        "普通茶母页的成分和有限人体资料只作共享背景；加入气泡、低温长时间浸泡或改变工业处理后，不能自动视为同一暴露。"
        if entry_id in {"cold-brew-tea", "sparkling-tea"}
        else "咖啡共享母页显示咖啡因与冲煮会影响短时警觉、睡眠和成分；特定产品与母页样品不同，长期风险关联不等于本条有因果防病效果。"
    )
    return f"""# Summary Document — {p['name']}

**身份。** {p['identity']}

**配方与实际暴露。** {p['composition']} {p['variables']}

**本条研究。** {p['direct']}

**工艺/产品证据。** {p['specific']}

**共享背景。** {common}

**安全。** {p['safety']} 需按实际份量、配料与产品说明判断，不把相邻饮品研究当作本条固定剂量或风险数据。

**传统来源。** {tradition} 感官、服务温度、加工和现代临床结果分别描述，不拼接为传统分类或健康结论。

现有资料的地点、产品和方法有限；未检得只代表本轮 R1 探索范围。本摘要只总结 Research Dossier 可追溯的事实，不预设后续分类。
"""


def main() -> None:
    out = ROOT / "references/entries"
    for entry_id, profile in PROFILES.items():
        directory = out / entry_id
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "research.md").write_text(dossier(entry_id, profile), encoding="utf-8")
        (directory / "summary.md").write_text(summary(entry_id, profile), encoding="utf-8")
    print(f"Wrote {len(PROFILES)} R1 dossiers and stage-2 summaries.")


if __name__ == "__main__":
    main()
