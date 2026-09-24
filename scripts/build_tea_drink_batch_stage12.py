#!/usr/bin/env python3
"""Create stage-1 and stage-2 dossiers/summaries for the next tea-drink batch.

The script records the batch-specific evidence already screened; it does not run Jev
or write final entry prose. Stage 3 native outputs are collected separately.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARENT = ROOT / "references/shared/tea-base"

PARENT_TEXT = """# Research Parent — 茶饮基底（Camellia sinensis）

> entry_id: tea-base  
> entry_type: research_parent  
> publication_status: not_a_direct_book_entry  
> research_depth: R1  
> status: review_ready  
> evidence_cutoff: 2026-09-24  
> last_updated: 2026-09-24

## 1. 研究对象与复用边界

本页整理普通茶叶/茶浸液共有的传统来源、咖啡因背景和有限人体证据，供奶茶、奶盖茶、果茶、抹茶、焙茶及瓶装茶等子项复用。它不是上述复合饮品的替代研究页。

茶饮的关键变量包括茶树品种、茶类与焙火/发酵程度、叶或粉末、浸泡比例、温度和时间、过滤方式、总份量及咖啡因。饮品中加入乳、植物饮、糖、果汁、奶盖、配料或气泡后，食品矩阵和暴露改变；不得把本页结果直接复制成其健康功效。

## 2. 传统来源

《本草纲目》茶条记李时珍所述“茶苦而寒”，并继续讨论茶的主治、饮法与禁忌。此处为茶叶/传统茶饮母本层的历史记载，不代表现代奶盖、果茶、抹茶拿铁、焙茶拿铁或瓶装茶已被古籍记载；母本关系只作来源比较，不能机械继承性味、归经或功效。

来源：李时珍《本草纲目》卷三十二（四库全书本）茶条，[维基文库转录](https://zh.wikisource.org/zh-hans/本草纲目_(四库全书本)/卷32)。本轮核对公开转录；纸本版次、页码及标点校勘未独立核验。

## 3. 现代人体与安全证据

### 3.1 血脂与血压

Igho-Osagie 等对茶饮 RCT 作系统综述与 Meta 分析，纳入 4–24 周干预；结论为短期饮茶在健康或有风险成人中似乎不会显著改变血压或血脂。研究食品多为茶饮而非本批完整复合配方，且对一些结果的统计效能有限。可用于“普通茶饮并未稳定显示短期降压/降脂”的背景，不能证明每一种茶饮长期无效或有害。

### 3.2 加奶红茶的短期血管指标

Ahmad 等 2018 年随机交叉试验纳入 17 名年轻健康成年人，分别饮用热水、红茶及加奶红茶，每种干预 4 周，期间无 washout。相较热水，红茶组肱动脉 FMD 增加；加奶红茶组 FMD 较红茶及热水低，并出现小幅血压差异。样本极小、无 washout、仅为替代终点且人群年轻；只能作为纯红茶加牛奶的有限近直接信号（对本批通常 D1–D2），不可写成奶茶治疗或损害心血管的确定结论。

另有 18 人、三天、每天 8 杯的研究发现，在红茶中添加 15 mL 牛奶未改变血浆槲皮素或山柰酚浓度曲线下面积。这是特定类黄酮吸收指标，既不验证临床健康获益，也不与 FMD 研究构成简单正反裁决。两者考察的问题不同。

### 3.3 抹茶认知试验

Dietz 等随机、安慰剂对照、单盲试验纳入 23 名抹茶消费者，单次饮用或食用各含 4 g 抹茶粉的测试品。对照后主要在部分基础注意和心理运动速度任务上观察到轻微改善，其他认知结局差异很少，POMS 情绪无显著变化。试验对象为抹茶茶饮/棒，不是牛奶和糖组成的抹茶拿铁；后者按 D1 解释，不能写成改善情绪或认知的稳定功效。

### 3.4 咖啡因与卫生

香港食物安全中心在 2013 年检测 30 份热饮港式茶餐厅奶茶和 10 份热饮台式奶茶，平均每份咖啡因分别约 170 mg（范围 73–220 mg）和 130 mg（100–160 mg）。这是特定地点、年代和配方的市场抽样；对鲜奶茶等只可作 D1–D2 暴露背景，不能作为固定含量。

中国 17 个省收集的 1,398 份茶叶样本研究测定了绿茶、红茶、黑茶、茉莉花茶、乌龙茶、白茶、黄茶等原料咖啡因，并建立成人摄入估算；该研究测的是茶叶，不是现制或瓶装成品，属于 D2。具体成品应优先看标签或其自身检测。

香港 CFS 的公开食品安全指引指出，4–60°C 温区可能使细菌较快繁殖；对预切水果与鲜榨果汁，建议尽快食用，暂存时冷藏，并限制在高于 4°C 的放置时间。这是一般操作建议，不是本条商品抽检结果。

## 4. 证据卡与引用

1. Igho-Osagie E, et al. “Short-Term Tea Consumption Is Not Associated with a Reduction in Blood Lipids or Pressure: A Systematic Review and Meta-Analysis of Randomized Controlled Trials.” *The Journal of Nutrition*. 2020;150(12):3269–3279. DOI: [10.1093/jn/nxaa295](https://doi.org/10.1093/jn/nxaa295). PMID: 33188386. abstract_only for this dossier.
2. Ahmad AF, Rich L, Koch H, et al. “Effect of adding milk to black tea on vascular function in healthy men and women: a randomised controlled crossover trial.” *Food & Function*. 2018;9(12):6307–6314. DOI: [10.1039/C8FO01019F](https://doi.org/10.1039/C8FO01019F). PMID: 30411751. abstract_only; PubMed structured abstract checked.
3. Hollman PCH, van het Hof KH, Tijburg LBM, Katan MB. “Addition of milk does not affect the absorption of flavonols from tea in man.” *Free Radical Research*. 2001;34(3):297–300. DOI: [10.1080/10715760100300261](https://doi.org/10.1080/10715760100300261). PMID: 11264903. abstract_only.
4. Dietz C, Dekker M, Piqueras-Fiszman B. “An intervention study on the effect of matcha tea, in drink and snack bar formats, on mood and cognitive performance.” *Food Research International*. 2017;99(Pt 1):72–83. DOI: [10.1016/j.foodres.2017.05.002](https://doi.org/10.1016/j.foodres.2017.05.002). PMID: 28784536. abstract_only.
5. Yong L, et al. “Quantitative probabilistic assessment of caffeine intake from tea in Chinese adult consumers based on nationwide caffeine content determination and tea consumption survey.” *Food and Chemical Toxicology*. 2022;165:113102. DOI: [10.1016/j.fct.2022.113102](https://doi.org/10.1016/j.fct.2022.113102). PMID: 35513285. abstract_only.
6. Hong Kong Centre for Food Safety. “Caffeine Content in Coffee and Milk Tea Prepared in Local Food Premises.” 2013. [Official report](https://www.cfs.gov.hk/english/programme/programme_rafs/programme_rafs_fci_01_04.html).
7. Hong Kong Centre for Food Safety. “Food Safety Day 2024 reminds public to pay attention to the importance of keeping food at safe temperatures.” 2024. [Official guidance](https://www.cfs.gov.hk/english/press/20240607_11013.html).
8. Hong Kong Centre for Food Safety. “Safe Preparation of Pre-Cut Fruits and Fruit Juices.” [Official guidance](https://www.cfs.gov.hk/english/multimedia/multimedia_pub/multimedia_pub_fsf_225_02.html).

## 5. 综合、未知与停止

茶叶母本有传统记载；现代人体证据只对特定茶类、剂量、人群和终点成立。小型短期研究、代理终点、混合食品差异和市场抽样异质性均限制推论。证据不支持把茶多酚、咖啡因或绿茶提取物单独研究当作整杯现代饮品的功效。

本页停止状态：R1 shared parent ready。已覆盖本批所需的茶母本背景、加奶红茶小试验、抹茶单次试验、咖啡因与现制冷饮卫生。新增研究须能改变某子项的真实配方、关键暴露、安全结论或直接人体证据判断；否则暂不扩展为茶的一般性疾病综述。
"""

PROFILES = [
    {
        "id":"fresh-milk-tea","name":"鲜奶茶","ingredients":"茶浸液或浓缩茶 + 牛乳；有些门店另加糖或糖浆，不应把奶精配方算入原型。",
        "target_search":"`(\"fresh milk tea\" OR \"fresh-milk tea\") (human trial OR randomized OR clinical)`；仅作 R1 探索检索。",
        "processing":"冲泡/萃取茶后与鲜牛乳混合；冷、热以及茶浓度、奶量和甜度因门店定制而变。",
        "typical":"中杯至大杯单份；没有跨品牌统一容量或鲜奶比例。按菜单标注和实物配方记录。",
        "variables":"鲜奶比例、茶类/浓度、加糖、冰量、杯量；鲜奶 vs 奶精是关键身份边界。",
        "confidence":"中；名称表达奶来源但市场命名不总能保证鲜奶比例。",
        "composition":"上海 122 款调查含现制奶茶类别，但没有把鲜奶茶与奶精款完全分开。香港 CFS 2013 年热饮港式奶茶咖啡因均值 170 mg/份、范围 73–220 mg，样本配方并非本条限定的鲜奶原型，只作 D2 暴露背景。",
        "direct":"一项 17 人随机交叉试验研究了加奶红茶而非商售鲜奶茶；另有 18 人短期研究看类黄酮吸收。两者问题不同，不能据此判定鲜奶茶对血管或整体健康的净影响。",
        "safety":"若确实含牛乳，乳蛋白过敏和乳糖耐受是个体层面的组成相关问题；确认乳品和含糖量以门店说明为准。茶基底的咖啡因差异可能很大，奶并不消除咖啡因。",
        "senses":"甜味取决于加糖与乳量，茶感可能苦/涩；应以具体样品感官为准，不把饮用温度判作本草寒热。",
        "composition_table":"| 茶+鲜牛乳 | 奶量和茶浓度未统一 | 门店配方/营养标示 | 不以港式奶茶抽样冒充鲜奶配方 |\n| 糖和咖啡因 | 未有本条统一数值；CFS 港式奶茶 170 mg/份（73–220）仅作远近背景 | 香港 CFS 2013 | 地区、年代、配方不同；D2 |",
        "extra":"鲜奶茶与传统茶有母子关系，但乳与糖改变了食品矩阵。"
    },
    {
        "id":"milk-foam-tea","name":"奶盖茶","ingredients":"茶饮底 + 奶油/乳制品或植脂配制的泡沫顶层；具体茶底、泡沫原料和糖浆随店不同。",
        "target_search":"`(\"milk foam tea\" OR \"cheese milk foam tea\") (human trial OR randomized OR clinical)`；仅作 R1 探索检索。",
        "processing":"先制茶底并打发/混合乳脂泡沫覆于表面；冷饮较常见，冷热和混合饮用方式不同。",
        "typical":"通常为单杯现制饮品；市场检测中的平均份量约 580 g，但该值来自香港被测奶盖组，非全市场标准。",
        "variables":"奶盖配方、是否含芝士、奶油/乳粉/植脂、茶底、糖浆和饮用时是否摇匀。",
        "confidence":"中低；“奶盖”涵盖差异较大的顶部泡沫配方。",
        "composition":"香港 CFS 2018 年将“芝士奶盖/奶盖绿茶”合并抽样，平均份量 580 g、平均总糖 3.5 g/100 g（范围 1.4–5.6），平均能量 57 kcal/100 g（范围 40–74）。样品不能区分所有奶盖配方。上海 122 款调查也涵盖奶盖茶，但为上海特定品牌与年份。",
        "direct":"没有找到以统一定义的奶盖茶为对象、可确认健康因果的直接人体临床试验。纯茶或牛奶试验都没有奶盖层、配方脂肪及实际门店份量，不能等同本条。",
        "safety":"糖和能量取决于泡沫与茶底；含奶制品时留意乳成分。易腐配料按 CFS 公共食品安全指引保存；该指引提供一般管理原则，不对具体门店作安全判断。",
        "senses":"奶盖可增加乳脂口感和咸/甜感，茶底可能苦涩；产品间差异大，不能从名称固定味性。",
        "composition_table":"| 奶盖茶（香港 CFS 合并样本） | 580 g/份均值；糖 3.5 g/100 g（1.4–5.6）；能量 57 kcal/100 g（40–74） | CFS/Consumer Council，2018 | 直接市场样本；与个体门店不等同 |\n| 上海现制奶盖茶 | 2018/2021 年 13 品牌抽样，含于 122 款总体 | JEOM 2023 | 地区/品牌代表性有限 |",
        "extra":"样品中芝士奶盖与普通奶盖合并报告，不能据此给两个类别分别提供含量。"
    },
    {
        "id":"fruit-tea","name":"水果茶","ingredients":"茶浸液 + 鲜果/果汁/果泥、糖浆或果味制品；并非每款含真实鲜果。",
        "target_search":"`(\"fruit tea\" OR \"fruit-infused tea beverage\") (human intervention OR randomized trial)`；仅作 R1 探索检索。",
        "processing":"现制冷饮/热饮，水果和甜味料可混合或作配料；果种、果量、甜度、冰量差异显著。",
        "typical":"单杯，检测样本常约 500–600 g；不同产品不宜套用固定份量。",
        "variables":"果种、鲜果 vs 浓缩汁/糖浆、茶底、加糖、果粒、冰量、食用速度与是否带固体配料。",
        "confidence":"中低；“水果茶”不是统一配方，有些产品为果味茶、有些含水果。",
        "composition":"香港 CFS 2018 年样品中，百香果红茶平均份量 530 g，总糖 7.1 g/100 g（4.7–11），能量 41 kcal/100 g；芒果绿茶平均份量 590 g，总糖 5.6 g/100 g（3.9–7.6），能量 37 kcal/100 g。上海 122 款现制饮品调查也包含水果茶。非加糖版本仍可能含果汁/水果本身糖，标签“无添加糖”不等于无糖。",
        "direct":"未找到能够把异质水果茶作为固定食品并研究长期临床结局的直接人体试验。成分检测能说明部分产品的糖/能量暴露，不等于疾病因果；果汁、单个水果或茶叶的试验不直接代表复合杯饮。",
        "safety":"水果切配、果汁和固体配料的卫生与冷藏是现制饮品的独立安全变量。糖和总能量需看实际标签/甜度；某些水果/果汁带来的天然糖不由“无添加糖”消失。",
        "senses":"酸、甜、茶苦涩随果种和甜度变化，可描述具体产品，不把某一味固定到全类别。",
        "composition_table":"| 百香果红茶 | 530 g/份均值；总糖 7.1 g/100 g（4.7–11）；41 kcal/100 g | 香港 CFS/CC，2018 | 直接为被测样本，不代表所有果茶 |\n| 芒果绿茶 | 590 g/份均值；总糖 5.6 g/100 g（3.9–7.6）；37 kcal/100 g | 香港 CFS/CC，2018 | 直接为被测样本，不代表所有果茶 |\n| 水果茶品类 | 纳入上海 122 款产品调查 | Shi et al., JEOM 2023 | 不能给每种水果配方相同数值 |",
        "extra":"CFS 的样品有含果汁/果味类别且包括鲜果产品；不能把所有水果茶当成果汁饮料。"
    },
    {
        "id":"cheese-tea","name":"芝士茶","ingredients":"茶浸液 + 含乳酪/奶油等乳品的顶部泡沫；门店配方常加入糖、盐或调味粉。",
        "target_search":"`(\"cheese tea\" OR \"cheese foam tea\") human clinical trial`；R1 检索另找到 Kurniati & Yuliani 2022 小鼠实验，不是人体研究。",
        "processing":"泡沫打发后覆于茶饮；泡沫和茶底可分层饮用或混合，配方及食用方式改变实际摄入。",
        "typical":"单杯现制，香港 CFS 合并奶盖组平均份量约 580 g；并非芝士茶全品类定值。",
        "variables":"芝士/奶酪种类、奶油和乳粉、盐糖、泡沫厚度、茶底、杯量与混合饮法。",
        "confidence":"中；概念可识别但配方边界并不统一。",
        "composition":"香港 CFS 2018 将“芝士奶盖/奶盖绿茶”作为合并类型：均份约 580 g，总糖均值 3.5 g/100 g（1.4–5.6），能量 57 kcal/100 g（40–74）。该合并组不单列芝士茶，不能把范围解释为专门的芝士配方。上海市场调查包括奶盖茶，但同样未对芝士层逐一分解。",
        "direct":"未找到芝士茶的人体干预试验。一项 32 只雄性小鼠的 21 天实验比较了绿茶/红茶、芝士泡沫和不同糖配方；部分组的血糖结果有差异，但小鼠结果不能推断人类长期血糖或糖尿病风险。加奶红茶试验也没有芝士泡沫、盐、糖及真实商业份量。",
        "specific_evidence_card":"### CHEESE-SRC-001｜芝士茶动物研究\n\nKurniati 与 Yuliani 使用 32 只雄性 Swiss Webster 小鼠，设水对照、葡萄糖阳性对照及不同含糖比例的绿茶/红茶芝士茶组，连续 21 天口服。摘要报告正常糖及半糖红茶芝士茶组的血糖高于水对照；无糖红茶芝士茶和半糖绿茶芝士茶组未见显著升高；各处理未显示体重效应。该研究是动物实验，不是人体研究，不能据此推断人类糖尿病风险。\n\n- evidence_distance: 对实验配方为 D0；对人体健康结论的间接性极高\n- full_text_status: abstract_only; title, metadata, DOI, and abstract checked\n- E: E-D animal signal; no human clinical inference\n- funding/conflicts: 本轮可见摘要未提供完整资助/利益冲突信息。",
        "extra_refs":["Kurniati NF, Yuliani RAT. “The Effect of Green Tea and Black Tea in Cheese Tea Drinks on Body Weight and Diabetes Mellitus Risk in Male Swiss Webster Mice.” *Acta Pharmaceutica Indonesia*. 2022;47(1):43–47. DOI: [10.5614/api.v47i1.17043](https://doi.org/10.5614/api.v47i1.17043). Animal study."] ,
        "safety":"乳制品和糖/脂肪含量受配方影响。现制冷饮中的乳类配料需按易腐食品指引妥善冷藏；公共食品安全建议避免长时间处于利于细菌繁殖的温区。",
        "senses":"产品可能兼有茶的苦涩、乳酪的咸香及糖带来的甜感，但幅度和组合依配方变化。",
        "composition_table":"| 芝士奶盖/奶盖绿茶合并组 | 均份 580 g；总糖 3.5 g/100 g（1.4–5.6）；能量 57 kcal/100 g（40–74） | 香港 CFS/CC，2018 | 组合类别，不能区分芝士与普通泡沫 |\n| 上海奶盖茶 | 122 款现制茶饮中的子类之一 | JEOM 2023 | 不等于独立芝士茶分析 |",
        "extra":"原料清单可确认乳酪/奶油时按该具体配方讨论，不能对整个商品名预设。"
    },
    {
        "id":"coconut-milk-tea","name":"椰乳茶","ingredients":"茶浸液 + 椰乳/椰奶类制品；市场命名也可能指椰味乳饮料、植脂配料或椰果配料。",
        "target_search":"`site:pubmed.ncbi.nlm.nih.gov \"coconut milk tea\" (trial OR human)`；检索结果未见与本条整体相符的人体试验，检索为 R1 探索性。",
        "processing":"将椰乳饮料或椰奶加入茶底，可再加糖、糖浆、椰果或奶制品；椰乳浓度和商品定义不一致。",
        "typical":"单杯现制或预包装产品；本轮未找到可代表全类的统一份量/含量调查。",
        "variables":"椰乳真含量、椰奶与椰味饮料差异、含水比例、糖、椰果、是否另含乳、茶底与杯量。",
        "confidence":"低至中；商品名称不保证主要脂肪或原料来自椰乳。",
        "composition":"本轮查到的上海 122 款调查涵盖奶茶、奶盖和水果茶，并不单独报告椰乳茶；香港 CFS 抽样也没有单列椰乳茶。故不提供推算的糖、脂肪或能量数值；需按标签或具体门店配方核验。",
        "direct":"没有找到以椰乳茶整体为对象的直接临床干预研究。椰子、椰乳、茶或一般含糖饮品的研究分别属于不同对象，不可合并成椰乳茶功效。",
        "safety":"标签上区分椰乳、椰味饮料、乳成分、糖和过敏原信息；含咖啡因与否取决于茶底。冷制现饮的卫生/冷链按现制饮品常规注意。",
        "senses":"椰香、甜度、茶苦涩由实际椰制品及甜味料决定，不足以推出传统性味。",
        "composition_table":"| 椰乳茶 | 本轮未找到可靠的类别级营养检测 | — | 不用椰子或相似奶茶数值填补 |\n| 个体商品 | 按实际标签/配方记录糖、脂肪、咖啡因及份量 | 商品标签/门店信息 | 品牌具体，不能概括整个条目 |",
        "extra":"椰乳饮料和椰奶脂肪/水分构成不同，研究须以成分表确认对象。"
    },
    {
        "id":"oat-milk-tea","name":"燕麦奶茶","ingredients":"茶浸液 + 燕麦饮料（oat drink）；可含植物油、酶解燕麦、稳定剂或糖；也可能额外加糖浆。",
        "target_search":"`site:pubmed.ncbi.nlm.nih.gov \"oat milk tea\" (trial OR human)`；检出两项体外模型研究（2023、2024），未检出直接人体临床试验；检索为 R1 探索性。",
        "processing":"将茶与一种具体品牌/配方燕麦饮料混合；“无糖”与甜味燕麦饮料需区分。",
        "typical":"单杯现制或家制；容量、燕麦饮用量和咖啡因均依配方，未发现统一市场均值。",
        "variables":"燕麦饮料品牌与强化营养素、是否加糖、茶底浓度、份量、是否另加乳品/植脂。",
        "confidence":"中低；类别可定义但燕麦饮料配方差异较大。",
        "composition":"本轮现制茶饮抽样未独立统计燕麦奶茶；上海报告的奶茶总类不能说明植物奶子类。普通燕麦饮料营养成分只代表具体品牌。不能从燕麦食品或燕麦奶单品试验直接推导这杯茶饮的血脂、饱腹或血糖效应。",
        "direct":"本轮未发现燕麦奶茶整体的人体临床试验。两项燕麦奶茶模型体系研究使用体外稳定性/模拟消化方法，发现结果会随燕麦饮脂肪及茶多酚浓度变化；它们不是人体结局，不能推出实际饮用后的血糖、血脂或饱腹效应。含茶饮料叠加燕麦饮料，也不等于燕麦单品RCT或茶叶单品试验；本条长期疾病功效命题 E-0。",
        "specific_evidence_map_row":"| 燕麦奶茶模拟消化/多酚可及性 | Qin et al. 2023、2024 体外模型 | D0 to tested model mixtures; D1–D2 to market products | 配方参数会改变实验室结果，无人体临床结局 | E-D |",
        "specific_evidence_card":"### OAT-SRC-001｜燕麦奶茶模型体系研究\n\nQin 等 2023 年将燕麦饮料与绿茶提取物制成模型体系，测量稳定性及模拟消化后茶多酚可及性；结果随燕麦饮脂肪比例与绿茶提取物浓度变化。2024 年同组研究用模拟口腔、胃和小肠的体外消化模型，发现较高茶多酚浓度会改变燕麦饮中葡萄糖、游离脂肪酸释放及胃阶段蛋白消化，并受脂肪含量影响。\n\n- directness: D0 to tested model mixtures; D1–D2 to market products\n- evidence_type: in vitro simulated digestion; no human clinical outcome\n- full_text_status: PubMed abstracts checked; full text not assessed in this review\n- E: E-D mechanism/model signal only; not evidence of a clinical effect",
        "extra_refs":[
            'Qin S, Li R, Chen M, et al. “Oat Milk Tea Model System: Exploring the Stability of Milk Tea and the Bioaccessibility of Green Tea Polyphenols.” *Foods*. 2023;12(7):1402. DOI: [10.3390/foods12071402](https://doi.org/10.3390/foods12071402). PMID: 37048223. In vitro model.',
            'Qin S, Li R, McClements DJ, et al. “Macronutrient digestion and polyphenol bioaccessibility in oat milk tea products: an in vitro gastrointestinal tract study.” *Food & Function*. 2024;15(14):7478–7490. DOI: [10.1039/D4FO01439A](https://doi.org/10.1039/D4FO01439A). PMID: 38915263. In vitro model.'
        ],
        "safety":"查看燕麦饮料配方中的添加糖、油脂、强化成分以及可能的交叉污染提示；茶底可能含咖啡因。燕麦饮料与乳品营养不可按名称互换。",
        "senses":"燕麦饮料可带谷物甜香，茶感随茶底改变；感官描述应以具体饮品为准。",
        "composition_table":"| 燕麦奶茶 | 未找到类别级直接营养检测/临床数据 | — | 不将燕麦奶数据当作整杯数据 |\n| 燕麦饮料单品 | 依品牌标签 | 产品标签 | 作为配方核对，不是健康效应证据 |",
        "extra":"先核实是无糖燕麦饮料还是含糖款，再记录整杯体积。"
    },
    {
        "id":"brown-sugar-milk-tea","name":"黑糖奶茶","ingredients":"茶浸液 + 牛乳/奶精等乳基底 + 黑糖、红糖或糖浆；“黑糖”商品名不保证原料及加糖量相同。",
        "target_search":"`site:pubmed.ncbi.nlm.nih.gov \"brown sugar milk tea\" human clinical study`；检索为 R1 探索性，未找到与本条整体相符的人体研究。",
        "processing":"糖浆或糖块与热茶/奶基底混合；可加入珍珠、奶盖等，但加入这些配料后已是另一复合配方。",
        "typical":"单杯现制；本轮未找到可代表本类别的单杯均量或糖含量。",
        "variables":"糖源类别、糖浆克数、配方中乳品/奶精、珍珠/奶盖、茶底和杯量。",
        "confidence":"中低；名字稳定地提示黑糖风味，但配方边界和实际糖量不稳定。",
        "composition":"CFS 的珍珠奶茶、芋香奶茶等类别和上海奶茶调查能说明现制奶茶普遍存在明显糖量差异，但均未给出黑糖奶茶专门含量。本轮没有足够的直接抽样支持一个类别均值，不能借用珍珠奶茶或百香果茶的数值。",
        "direct":"没有找到黑糖奶茶整体的人体临床试验。糖或咖啡因单独摄入、珍珠奶茶、普通奶茶试验均不等于黑糖奶茶，疾病因果结论 E-0。",
        "safety":"若含糖浆，整杯添加糖可能是主要暴露；实际数值应看标签/门店营养信息。茶基底有咖啡因的可能，乳品过敏与易腐配料的冷饮卫生按公共食品安全指引处理。",
        "senses":"甜味通常显著但实际浓度需按配方确认；黑糖焦香是风味描述，不能直接作为传统温热属性依据。",
        "composition_table":"| 黑糖奶茶 | 本轮未找到类别级直接检测 | — | 不从珍珠奶茶/普通奶茶均值移植 |\n| 单品配方 | 记录整杯总糖、总量、咖啡因及乳基底 | 菜单/标签/品牌检测 | 同名不同配方需单独编码 |",
        "extra":"不要把“黑糖”当作未经检测的特定糖剂量或健康优势标签。"
    },
    {
        "id":"matcha-latte","name":"抹茶拿铁","ingredients":"抹茶粉（粉末茶叶）+ 牛乳或植物饮料 + 可选糖浆/糖；抹茶粉被摄入而不只是茶浸液。",
        "target_search":"`\"Influence of Continuous Ingestion of Matcha Latte on Stress\"`；J-STAGE 全文可得，发现一项小样本人体先导干预，另检索抹茶饮/食品棒试验。",
        "processing":"抹茶粉分散于水/奶中，冷/热均可；奶种、粉量、糖和份量是主要变量。",
        "typical":"香港 CFS 样品平均份量约 490 g；该数字来自 2018 年样本，不是标准杯量。",
        "variables":"抹茶粉克数与品质、牛乳/植物奶、糖浆、冰/热、份量；抹茶粉饮用不同于泡茶滤叶。",
        "confidence":"中；名称确定核心原料，但粉量、奶与糖变化大。",
        "composition":"香港 CFS 2018 抹茶拿铁样本平均份量 490 g，平均总糖 5.2 g/100 g（范围 3.0–11），能量 56 kcal/100 g（38–74）；“无添加糖”组平均总糖 2.9 g/100 g（1.5–4.8）。另有一项日本 2021 年粉末抹茶拿铁研究饮品，每日两份、连续两周，单日供给能量 125.7 kcal、碳水 23.3 g、咖啡因 81.0 mg；属于单一实验配方，不代表市场平均。",
        "direct":"一项日本小样本双盲平行试验让吸烟者连续两周每天饮用两份实验用粉末抹茶拿铁，以焙茶拿铁作对照；18 人同意参加，13 人进入分析。主观状态焦虑和唾液皮质醇未见两组显著差异；唾液 α-淀粉酶反应只有探索性信号，且为替代指标。另一项 23 人单次抹茶饮/棒试验观察到少数注意与心理运动速度任务的轻微差异，但情绪量表无显著变化。小样本、短期、特定配方和不同研究终点均不支持稳定减压、情绪改善或认知功效。",
        "specific_evidence_card":"### MATCHA-SRC-001｜连续抹茶拿铁小试验\n\nMonobe 等 2021 年双盲平行先导干预，18 名吸烟者同意参加，13 人纳入分析；试验饮品为 Nestlé Japan 粉末抹茶拿铁或焙茶拿铁，每天各饮两份、连续两周。抹茶拿铁的咖啡因+EGCG与茶氨酸+精氨酸摩尔比为 2.3。两组状态焦虑量表及唾液皮质醇没有显著差异；作者依据唾液 α-淀粉酶反应轨迹提出可能的交感神经反应信号。样本小，部分受试者未纳入，终点是实验压力下的替代指标；产品由企业提供/协作，研究由抹茶与健康研究会资助。不得写成已证明的减压效果。\n\n- directness: 对该实验粉末抹茶拿铁 D0；对市场上其他配方 D1–D2\n- full_text_status: full_text_available; J-STAGE PDF checked\n- outcome-specific E: 状态焦虑与皮质醇改善 E-0（组间未见显著差异）；唾液 α-淀粉酶轨迹至多 E-C（小样本替代指标的探索性信号）\n\nDietz 等另一项 23 人单次抹茶研究使用每份 4 g 抹茶粉的茶饮/食品棒，不含本条常见奶基底；仅作 D1 背景。",
        "extra_refs":["Monobe M, Nomura S, Ema K. “Influence of Continuous Ingestion of Matcha Latte on Stress: A Preliminary Study.” *Tea Research Journal*. 2021;131:9–14. DOI: [10.5979/cha.2021.131_9](https://doi.org/10.5979/cha.2021.131_9). 中文题名：抹茶ラテの連続飲用がストレスへ与える影響についての予備的調査。 Full text available."] ,
        "safety":"抹茶粉会把整片研磨茶叶一并摄入，摄入量受粉重与浓度影响；咖啡因量不能按淡泡绿茶猜测。若含乳或糖，另按标签核验。",
        "senses":"抹茶可有明显茶苦/鲜味，甜度与奶量改变口感；具体分类以实际样品，不从颜色或冷热推出性味。",
        "composition_table":"| 抹茶拿铁（香港 CFS） | 490 g/份均值；糖 5.2 g/100 g（3.0–11）；能量 56 kcal/100 g（38–74） | CFS/CC，2018 | 直接市场样本；配方异质 |\n| 无添加糖版本 | 糖 2.9 g/100 g（1.5–4.8） | 同上 | 不是零糖；乳等原料仍可能含天然糖 |\n| 抹茶茶饮单次试验 | 每测试品含 4 g 抹茶粉 | Dietz et al., 2017 | D1；不是拿铁配方 |",
        "extra":"抹茶的单品研究对象是粉末茶饮，不可自动转成加奶加糖商品的长期效果。"
    },
    {
        "id":"hojicha-latte","name":"焙茶拿铁","ingredients":"焙火茶叶/焙茶粉或浸液 + 牛乳/植物饮料，可加糖浆；不同门店可能使用粉末或浓缩茶液。",
        "target_search":"`\"hojicha latte\" human trial`；R1 定向检索仅确认其作为抹茶拿铁试验对照，不把对照组当作焙茶疗效试验。",
        "processing":"茶叶焙火后冲泡或研粉，与奶类混合；焙火程度和粉/浸液形态会改变风味与成分。",
        "typical":"单杯现制；未找到可代表全类的统一份量或咖啡因检测。",
        "variables":"茶叶种类、焙火程度、粉末/浸液、奶基底、糖浆、份量及冲泡浓度。",
        "confidence":"中低；焙茶相关产品与商品配方差别较大。",
        "composition":"本轮未发现焙茶拿铁的类别级直接营养抽样或可靠咖啡因含量数据。作为比较饮品，一项日本小型抹茶拿铁试验使用的单一粉末焙茶拿铁配方每日两份供给约 129.6 kcal、碳水 24.5 g、咖啡因 4.8 mg；样本是试验用 Nestlé 配方，不代表其他品牌。普通茶叶的咖啡因调查无法替代焙茶成品；抹茶拿铁或绿茶产品糖能量也不能移用。",
        "direct":"上述两周试验将粉末焙茶拿铁作为抹茶拿铁的对照，因此有一款试验配方的真实人体摄入资料，但不是独立设计来验证焙茶功效的试验；不能从其对照组推断焙茶效果。普通茶或抹茶单次研究也不匹配焙火茶+奶的完整矩阵。焙茶拿铁健康效果当前没有可靠的类别级人体证据。",
        "extra_refs":["Monobe M, Nomura S, Ema K. “Influence of Continuous Ingestion of Matcha Latte on Stress: A Preliminary Study.” *Tea Research Journal*. 2021;131:9–14. DOI: [10.5979/cha.2021.131_9](https://doi.org/10.5979/cha.2021.131_9). Hojicha latte used as the control beverage; not an efficacy trial of hojicha."] ,
        "safety":"若含茶树原料通常需把咖啡因列为待查暴露；实际含量取决于茶粉/浸液和份量。查看是否含奶、植物饮及糖浆。",
        "senses":"焙火带来的烘烤香、茶苦涩与奶甜可描述为感官特点，不等于本草温性判断。",
        "composition_table":"| 焙茶拿铁 | 本轮未找到直接类别级抽样 | — | 不用抹茶拿铁数据代替 |\n| 个体产品 | 按菜单/标签核对粉量、奶、糖、咖啡因和杯量 | 品牌信息 | 商品特异，更新时保留日期 |",
        "extra":"焙茶（hojicha）不等同抹茶，粉末/浸液方式也会改变摄入。"
    },
    {
        "id":"bottled-unsweetened-tea","name":"无糖瓶装茶","ingredients":"预包装即饮茶，标签声明无糖/无添加糖；可使用绿茶、红茶、乌龙或其他茶，配方需以标签确认。",
        "target_search":"`site:pubmed.ncbi.nlm.nih.gov \"bottled unsweetened tea\" (trial OR human)`；检出一项饮后瓶装茶唾液细菌生长的实验室筛查，不是临床安全结局。",
        "processing":"工厂萃取/调配、热处理或其他商业稳定化并密封包装；其组成与现泡茶和现制奶茶不同。",
        "typical":"单瓶/罐，具体容量按商品标签；“无糖”不是咖啡因零含量，也不自动等于不含其他添加成分。",
        "variables":"茶种/浓度、瓶容量、糖声明法律含义、甜味剂、香料、咖啡因标示及生产批次。",
        "confidence":"中；预包装与声明有明确边界，但商品成分差异仍大。",
        "composition":"香港 CFS 2018 的 11 份预包装茶饮样本平均糖约 15 g/份、能量约 80 kcal/份；该小样本混合多个产品，未单独报告无糖瓶装茶，因此不能用于本条数值。中国茶叶咖啡因研究测的是原料茶叶而非瓶装成品。本轮未找到足以代表无糖瓶装茶全市场的咖啡因/营养抽样。优先按单瓶标签及具体产品成分表记录。",
        "direct":"没有找到将‘无糖瓶装茶’作为统一类别并验证长期健康结局的直接临床证据。普通茶的短期血脂/血压综述与单次抹茶试验都不是瓶装无糖成品；不写疾病预防功效。",
        "specific_evidence_map_row":"| 直接对瓶饮用后剩余瓶装茶的微生物筛查 | Kaku et al. 2024 实验室唾液接种 | D0 to tested beverage/saliva-inoculation scenario | 部分近中性 pH 绿茶样品出现唾液细菌生长；非未开封货架期或临床感染结果 | E-D |",
        "specific_evidence_card":"### BOTTLED-SRC-001｜饮后瓶装茶微生物筛查\n\nKaku 等 2024 年把 10 名参与者的稀释唾液接种到不同厂家瓶装茶中，观察饮用剩余瓶内细菌生长；部分近中性 pH 绿茶饮料支持唾液细菌增长。研究针对“直接对瓶饮用后剩余饮料”的体外筛查，不是未开封产品货架期测试，也没有消费者感染或疾病结局。\n\n- directness: D0 to tested beverage/saliva-inoculation scenario; no inference to all brands\n- evidence_type: laboratory microbiology screening\n- full_text_status: PubMed abstract checked; full text not assessed in this review\n- E: E-D safety signal only; follow product storage directions and do not treat as proof of harm",
        "safety":"核对每瓶份量、总糖/碳水、甜味剂和咖啡因信息。若产品没有标咖啡因，不能据“无糖”推断不含咖啡因。一项实验室接种筛查显示，直接对瓶饮用后，部分近中性 pH 绿茶样品可支持唾液细菌生长；它不测试未开封货架期或真实感染风险，也不能据此设定各品牌的开封后保存时限。开封后按标签储存。",
        "extra_refs":[
            'Kaku N, Kawachi M, Wakui A, et al. “Molecular microbiological profiling of bottled unsweetened tea beverages: A screening experiment.” *Journal of Oral Biosciences*. 2024;66(3):628–632. DOI: [10.1016/j.job.2024.07.006](https://doi.org/10.1016/j.job.2024.07.006). PMID: 39069173. Laboratory screening.'
        ],
        "senses":"无糖描述的是糖/配方声明而非无苦、无涩或特定寒热；味觉由茶种、浓度和配方决定。",
        "composition_table":"| 香港预包装茶饮（11 份混合样本） | 均糖 15 g/份、均能量 80 kcal/份 | CFS/CC，2018 | 包含不同类型，不是无糖茶专属数据 |\n| 茶叶原料咖啡因 | 1,398 份、17 省、多个茶类 | Yong et al., 2022 | D2；不是即饮成品 |\n| 无糖瓶装茶具体商品 | 按瓶身每份/每瓶标签登记 | 产品标签 | 最适合该商品，不代表品类 |",
        "extra":"区分无添加糖、总糖低和使用非糖甜味剂等标签表述，避免把市场营销用语合并为单一组成。"
    }
]

COMMON_REFS = [
    'Shi Z, Sun Z, Song Q, Qu M, Wang Z, Zang JJ. “Nutrient content of 122 kinds of retail handcrafted milk tea products in Shanghai.” *Journal of Environmental and Occupational Medicine*. 2023;40(7):756–760. DOI: [10.11836/JEOM22505](https://doi.org/10.11836/JEOM22505). 中文题名：上海122种市售现制奶茶中的营养成分。',
    'Hong Kong Centre for Food Safety and Consumer Council. “Sugar and Energy Contents of Common Non-Indigenous Tea-Based Beverages in Hong Kong.” 2018 sample survey, published 2019. [Official report](https://www.cfs.gov.hk/english/programme/programme_rafs/programme_rafs_n_01_26_abstract.html).',
    'Hong Kong Centre for Food Safety. “Caffeine Content in Coffee and Milk Tea Prepared in Local Food Premises.” 2013. [Official report](https://www.cfs.gov.hk/english/programme/programme_rafs/programme_rafs_fci_01_04.html).',
    'Hong Kong Centre for Food Safety. “Food Safety Day 2024 reminds public to pay attention to the importance of keeping food at safe temperatures.” 2024. [Official guidance](https://www.cfs.gov.hk/english/press/20240607_11013.html).',
    'Hong Kong Centre for Food Safety. “Safe Preparation of Pre-Cut Fruits and Fruit Juices.” [Official guidance](https://www.cfs.gov.hk/english/multimedia/multimedia_pub/multimedia_pub_fsf_225_02.html).',
    'Igho-Osagie E, et al. “Short-Term Tea Consumption Is Not Associated with a Reduction in Blood Lipids or Pressure: A Systematic Review and Meta-Analysis of Randomized Controlled Trials.” *The Journal of Nutrition*. 2020;150(12):3269–3279. DOI: [10.1093/jn/nxaa295](https://doi.org/10.1093/jn/nxaa295). PMID: 33188386.',
    'Ahmad AF, Rich L, Koch H, et al. “Effect of adding milk to black tea on vascular function in healthy men and women: a randomised controlled crossover trial.” *Food & Function*. 2018;9(12):6307–6314. DOI: [10.1039/C8FO01019F](https://doi.org/10.1039/C8FO01019F). PMID: 30411751.',
    'Hollman PCH, van het Hof KH, Tijburg LBM, Katan MB. “Addition of milk does not affect the absorption of flavonols from tea in man.” *Free Radical Research*. 2001;34(3):297–300. DOI: [10.1080/10715760100300261](https://doi.org/10.1080/10715760100300261). PMID: 11264903.',
    'Dietz C, Dekker M, Piqueras-Fiszman B. “An intervention study on the effect of matcha tea, in drink and snack bar formats, on mood and cognitive performance.” *Food Research International*. 2017;99(Pt 1):72–83. DOI: [10.1016/j.foodres.2017.05.002](https://doi.org/10.1016/j.foodres.2017.05.002). PMID: 28784536.',
    'Yong L, et al. “Quantitative probabilistic assessment of caffeine intake from tea in Chinese adult consumers based on nationwide caffeine content determination and tea consumption survey.” *Food and Chemical Toxicology*. 2022;165:113102. DOI: [10.1016/j.fct.2022.113102](https://doi.org/10.1016/j.fct.2022.113102). PMID: 35513285.'
]

for p in PROFILES:
    eid = p["id"]
    entry_dir = ROOT / "references/entries" / eid
    entry_dir.mkdir(parents=True, exist_ok=True)
    research = f"""# Research Dossier — {p['name']}

> entry_id: {eid}  
> research_depth: R1  
> status: review_ready  
> evidence_cutoff: 2026-09-24  
> researcher: Codex  
> last_updated: 2026-09-24

## 1. 条目身份

### 1.1 定义
- 条目：{p['name']}
- 类型：现制或预包装复合茶饮，见身份卡限定。
- 主目录：卷一「饮品部—茶饮新制」
- 传统母条：茶叶；按具体配方可能另含牛乳或植物饮料。
- 研究对象：{p['ingredients']}
- 常见变体：{p['processing']}

### 1.2 Identity Card

- ingredients: {p['ingredients']}
- processing: {p['processing']}
- typical_serving: {p['typical']}
- key_variables: {p['variables']}
- identity_confidence: {p['confidence']}

### 1.3 Identity Revision

未改变目录名称；研究时将条目操作化为上述配方边界。若实际商品超出该边界，归为邻接产品，不把含量或效应并入本条。

## 2. 研究范围

### 核心问题
1. 本条实际由哪些食物基质构成，商品间关键暴露如何变化？
2. 是否有同一饮品的人体试验、可用的直接成分调查或安全资料？
3. 茶叶母本资料与现代复合饮品之间哪些可以比较、哪些不能继承？

### 明确不在本轮解决的问题
- 对所有品牌作排名或推断统一营养成分；
- 用单一营养素、提取物、传统母本或相似饮品替代整杯食品；
- 对长期疾病风险作无直接证据的因果判断。

## 3. 检索日志

| 日期 | 来源 | 检索式/检查项 | 用途 |
|---|---|---|---|
| 2026-09-24 | PubMed/MEDLINE | 条目名英文/中文 + tea, beverage, trial, human, safety | 查直接人体研究及负向/无效研究；R1 探索检索，未系统计数 |
| 2026-09-24 | DOI/Crossref、PubMed | 核对题名、作者、年份、期刊、DOI、PMID | 参考文献审计 |
| 2026-09-24 | Hong Kong CFS / Consumer Council | tea-based beverages, sugar, energy, caffeine; public food-safety guidance for perishable ingredients | 产品组成与一般食品安全建议 |
| 2026-09-24 | Sinomed / JEOM | 现制奶茶、奶盖茶、水果茶营养成分 | 核对中国市场产品类别和研究对象 |
| 2026-09-24 | 维基文库公开转录 | 本草纲目卷32 茶条 | 传统母本定位；标记版本局限 |

**本条定向查询：** {p.get('target_search', '按条目中英文名与人体研究、试验及安全相关词做 R1 探索检索；不是系统综述。')} 检索结果用于定位候选文献；“未找到”仅代表本轮 R1 范围，不证明全球不存在研究。

## 4. 传统文献

| 来源 | 时代/版本 | 原文位置 | 可确认内容 | 身份对应问题 |
|---|---|---|---|---|
| 李时珍《本草纲目》 | 明代；四库全书本公开转录 | 卷三十二「茶」条 | 记“茶苦而寒”并讨论茶的饮用和主治 | 对象是茶叶/传统茶饮，不是现代的 {p['name']} 复合配方；只作母本背景 |

传统结论：可以确认茶叶母本有明确记载；不能由此推出本条成品的四气、五味、归经或特定功效。

## 5. 中医概念溯源

| 概念 | 来源 | 现代工作说明 | 本轮处理 |
|---|---|---|---|
| 苦、寒 | 《本草纲目》茶条 | 历史文本对茶的传统描述 | 仅作茶母本事实；现代复合饮品不自动继承 |
| 甜、酸、咸、苦涩 | 具体配方与饮用感受 | 感官描述，不等同功效、证候或脏腑归经 | 不预设最终分类 |
| 温度 | 冷饮/热饮服务条件 | 物理温度可影响饮用体验，但不是本草四气 | 与食性分开 |

## 6. 组成与真实暴露

{p['composition_table']}

**本条组成综述：** {p['composition']}

若无直接市场检测，则按具体标签/配方记录，不用相近饮品填数。

## 7. 现代证据地图

| Claim / Outcome | 主要证据 | D | 方向与限制 | E |
|---|---|---:|---|---|
| 本条实际糖、能量或咖啡因暴露 | {p['composition']} | D0–D2，按来源匹配度 | 只描述已测样品；不代表所有商品 | 组成资料，不作健康效应分级 |
| 普通茶短期血脂/血压 | Igho-Osagie et al. tea RCT 系统综述/Meta | D1–D2 | 4–24 周的茶饮研究，不是本条统一配方；未显示稳定显著改善 | E-C（对本条间接） |
| 加奶红茶短期血管替代指标 | Ahmad et al.，17 人交叉试验 | D1–D2 | 小样本、年轻健康人、无 washout、替代终点；不等于疾病结果 | E-C |
| 本条预防或治疗长期疾病 | 本轮未发现同一对象可靠直接因果证据 | — | 不从成分或茶母本外推 | E-0 |
{p.get('specific_evidence_map_row', '')}

本条特异结果：{p['direct']}

### Evidence-base overlap

{chr(96)*3}yaml
evidence_base_overlap:
  level: moderate
  note: 茶饮系统综述、单项茶试验和配方研究对应不同暴露/结局；不能按论文篇数累加为本条直接证据。
{chr(96)*3}


## 8. 核心证据卡

### TEA-SRC-001｜现制饮料组成

{p['composition']}

- directness: 对调查中被定义和采样的商品为 D0；对身份不同的本条产品按 D1–D2 或不可外推。
- does_not_support: 长期疾病因果、所有品牌统一成分、固定传统属性。

### TEA-SRC-002｜普通茶 RCT Meta

Igho-Osagie et al. 2020 汇总短期茶饮 RCT。abstract_only。报告结论为 4–24 周饮茶似乎没有显著改变健康或有风险成人的血脂/血压；本批复合饮品的添加物和茶品未被统一控制。

- evidence_distance: D1–D2
- supports: 对茶饮短期代理终点的有限背景
- does_not_support: 具体商品长期防病或治疗

### TEA-SRC-003｜茶加奶研究

Ahmad et al. 2018，17 名健康志愿者随机交叉，热水、红茶和加奶红茶各 4 周，无 washout。加奶红茶在 FMD/血压指标上出现与对照不同的结果；研究作者指出仍需更大、更长试验。abstract_only。

- evidence_distance: 对只有茶+牛乳的鲜奶茶 D1；对含奶盖、果料、糖浆或植物奶者 D2–D4
- supports: 加奶会改变受测短期指标的可能性
- does_not_support: 稳定临床获益/伤害或成品全类结论

### TEA-SRC-004｜安全性

- 咖啡因：茶类、浓度和份量影响摄入；香港地区样品值不代表本条固定量。
- 现制冷饮：易腐乳品、果料和配料的储存与卫生是可变安全因素；参照 CFS 公共食品安全指南。
- 甜味和添加物：按实际配方或每份标签确认。

{p.get('specific_evidence_card', '')}

## 9. 分结局综合

### Outcome A｜组成和摄入量

**事实：** {p['composition']}

**直接性：** 以被测样品为 D0；同一名称的未测配方不能拿样本均值代替。

**正文最大允许表述：** 报告来源、年份、地点、样本和实测范围；未测信息明说未找到。

### Outcome B｜短期人体效应

**人体证据：** {p['direct']}

**反向/冲突：** 小型加奶红茶试验的 FMD 方向与普通茶 RCT Meta 的整体血脂/血压“无稳定显著变化”并非同一终点；Hollman 等研究仅说明特定黄酮吸收没有改变。不能把不同结局折成健康净效应。

**E 等级：** 对本条整体有益/有害长期效应 E-0；茶或茶+奶短期替代终点为间接 E-C。

### Outcome C｜传统母本与本条映射

**母本事实：** 茶叶在《本草纲目》中有苦寒记载。

**身份距离：** 本条是 {p['name']}；{p['extra']}。

**最大允许表述：** 呈现来源关系及加工边界；现代效应或口味不能单独推出归经和脏腑功效。

## 10. 安全性

- 咖啡因：{p['safety']}
- 过敏/耐受：依本条实际乳品、植物饮或其他配料判断。
- 糖与能量：按具体每份而非只看“少糖/无糖/黑糖”等名称。
- 微生物：对现制冷饮关注配料储存与清洁；预包装产品另按标签储存。
- 药物相互作用/特殊人群：本轮 R1 未针对每一配方做专门临床相互作用综述；避免从茶成分机制直接下药物建议。

## 11. 机制与成分

| 因素 | 证据类型 | 可支持到什么程度 | 不支持什么 |
|---|---|---|---|
| 茶中咖啡因、茶多酚 | 茶叶/茶饮研究 | 可解释咖啡因暴露或提出机制问题 | 不能替代整杯商品的人体结局 |
| 牛乳、椰乳或燕麦饮 | 配方标签及各自独立食品研究 | 核验具体基底组成 | 不能将基底试验直接转成复合饮品功效 |
| 糖、果料、奶盖/糖浆 | 直接配方或抽样 | 描述真实摄入 | 不直接证明疾病因果 |

## 12. 本草映射候选（供第三阶段回查，不作结论）

- 可核验的历史桥梁：茶叶母本传统记录；具体复合配方的母本来源另按成分确认。
- 直接人体事实：限定于研究所用普通茶、加奶茶或抹茶试验，并按 D 标明；不能凭口感替代证候数据。
- 反证/替代解释：配方、糖、份量、咖啡因、乳基底和受试者差异；感官甜酸苦涩随商品变动。
- 本阶段不预写四气、五味、归经、阴阳增减或 M 等级。

## 13. 冲突与未知

### 主要冲突

茶+奶的 FMD 小试验、茶饮短期血脂/血压 Meta 与黄酮吸收研究衡量不同终点，方向不能简单合并。

### 仍未知
- 本条产品在实际市场上的标准配方、每份糖和咖啡因分布；无直接抽样者尤其如此。
- 同一配方长期、临床重要结局的直接人体效应。
- 历史文本的其他版本差异以及茶母本属性向现代制品迁移的边界。

### 不应声称
- “本条降压/护心/减肥/改善情绪”作为已经确证的功效；
- “无糖所以无咖啡因”或“无糖所以零能量”；
- 茶叶传统记载自动等于整个复合饮品的分类。

## 14. Claim Ledger

| ID | 正文候选命题 | 允许措辞 | E/性质 | D |
|---|---|---|---|---|
| {eid}-C01 | 配方与商品间暴露有差异 | 明确来源和样本的描述；未测则说明未知 | 组成事实 | D0–D2 |
| {eid}-C02 | 本条能预防/治疗长期疾病 | 当前资料不足以建立本条特异因果关系 | E-0 | — |
| {eid}-C03 | 茶母本有传统记载 | 明确限定为历史茶叶/茶饮母本，并说明现代复合食品边界 | 传统史料 | D4 类比于现代本条 |

## 15. 停止判断

{chr(96)*3}yaml
stopping_status: stopped_for_R1
stopping_reason: 已覆盖身份、直接成分资料、关键茶/加奶/抹茶人体资料、安全和明确负向搜索；本条长期临床证据稀疏，进一步泛茶研究预计不会改变本条结论。
evidence_cutoff: 2026-09-24
{chr(96)*3}


若出现同一配方的大型直接人体试验、可靠的本条代表性营养/咖啡因调查或重要食品安全警报，重开对应问题。

## 16. 参考资料清单

"""
    all_refs = COMMON_REFS + p.get("extra_refs", [])
    refs = "\n".join(f"{i+1}. {s}" for i, s in enumerate(all_refs))
    (entry_dir / "research.md").write_text(research + refs + "\n", encoding="utf-8")
    if eid == "bottled-unsweetened-tea":
        safety_extra = ""
    elif eid in {"milk-foam-tea", "fruit-tea", "cheese-tea", "coconut-milk-tea", "brown-sugar-milk-tea", "bottled-unsweetened-tea"}:
        safety_extra = ""
    else:
        safety_extra = "若含乳品或切配水果等易腐原料，按公共食品安全指引妥善保存并尽快饮用；这是一般管理建议，不代表具体商品不安全。"
    safety_extra_md = f"\n\n{safety_extra}" if safety_extra else ""
    summary = f"""# Summary Document — {p['name']}

**身份。** 本条主要指{p['ingredients'].lstrip().rstrip('。')}。制备方式：{p['processing'].lstrip().rstrip('。')}。常见份量/规格：{p['typical'].lstrip().rstrip('。')}。关键差异：{p['variables'].lstrip().rstrip('。')}。身份信心：{p['confidence'].lstrip().rstrip('。')}。

**组成与实际暴露。** {p['composition']}

没有类别级检测的配方不推估统一数值；优先按具体商品标签或门店配方记录。

**人体证据。** {p['direct']}

茶饮共享证据只提供有限背景：一项短期茶饮系统综述没有显示血脂或血压稳定显著改善；一项加奶红茶小型交叉试验观察的是血管替代指标，样本小、期间无 washout。不同研究对象和结局不可合并为本条的健康净效应。目前资料不足以确认本条预防或治疗长期疾病的因果效应（E-0）；相近茶饮或单一成分研究不能代表整杯。

**安全与局限。** {p['safety']}{safety_extra_md}

研究地点、年代和配方有限，结论不能无条件推广至所有品牌。

**传统背景。** 《本草纲目》茶条有“茶苦而寒”的母本记载，所指是历史茶叶/传统茶饮。{p['extra']}

具体饮品的甜、酸、苦、咸等感官印象可随配方记录，但不自动证明复合饮品的四气、归经或脏腑功效；冷热是服务温度，不是本草寒热结论。"""
    (entry_dir / "summary.md").write_text(summary + "\n", encoding="utf-8")

PARENT.mkdir(parents=True, exist_ok=True)
(PARENT / "research.md").write_text(PARENT_TEXT, encoding="utf-8")
print(f"Wrote {len(PROFILES)} dossiers and summaries plus shared tea parent.")
