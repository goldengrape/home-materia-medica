#!/usr/bin/env python3
"""Write reader-facing entries from stage-2 summaries and stage-3 mappings."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "qa/jev-tea-batch/raw"
NAMES = {
    "fresh-milk-tea": "鲜奶茶",
    "milk-foam-tea": "奶盖茶",
    "fruit-tea": "水果茶",
    "cheese-tea": "芝士茶",
    "coconut-milk-tea": "椰乳茶",
    "oat-milk-tea": "燕麦奶茶",
    "brown-sugar-milk-tea": "黑糖奶茶",
    "matcha-latte": "抹茶拿铁",
    "hojicha-latte": "焙茶拿铁",
    "bottled-unsweetened-tea": "无糖瓶装茶",
}

CONTENT = {
    "fresh-milk-tea": {
        "opening": "鲜奶茶在本条中指茶浸液或浓缩茶加牛乳；菜单名称不总能保证用了鲜奶，奶精配方应另看。香港一项热饮奶茶调查测得当地茶餐厅式奶茶每份咖啡因均值 170 mg（范围 73–220 mg），但它不是鲜奶茶专属抽样，不能当作每杯鲜奶茶的定值。",
        "evidence": "人体研究主要测的是相邻对象。一项 17 人随机交叉试验比较热水、红茶和加奶红茶，观察血管替代指标，样本小且干预之间没有 washout；它不能证明现制鲜奶茶对心血管有稳定好处或伤害。另有 18 人短期研究发现加奶没有改变所测茶黄酮吸收，但这也不是临床健康结局。",
        "safety": "茶底浓度与杯量会改变咖啡因摄入；乳蛋白过敏和乳糖不耐受则取决于是否确含牛乳。糖量、奶量与容量最好按门店配方核对。",
        "references": [
            'Ahmad AF, Rich L, Koch H, et al. “Effect of adding milk to black tea on vascular function in healthy men and women: a randomised controlled crossover trial.” *Food & Function*. 2018;9(12):6307–6314. DOI: [10.1039/C8FO01019F](https://doi.org/10.1039/C8FO01019F). PMID: 30411751.',
            'Hollman PCH, van het Hof KH, Tijburg LBM, Katan MB. “Addition of milk does not affect the absorption of flavonols from tea in man.” *Free Radical Research*. 2001;34(3):297–300. DOI: [10.1080/10715760100300261](https://doi.org/10.1080/10715760100300261). PMID: 11264903.',
            'Hong Kong Centre for Food Safety. “Caffeine Content in Coffee and Milk Tea Prepared in Local Food Premises.” 2013. [Official report](https://www.cfs.gov.hk/english/programme/programme_rafs/programme_rafs_fci_01_04.html).',
        ],
    },
    "milk-foam-tea": {
        "opening": "奶盖茶通常由茶底和顶部泡沫组成；泡沫可能含乳制品、植脂、奶油、芝士、盐或糖浆，摇匀或分层饮用也会改变实际摄入。香港 2018 年抽样把“芝士奶盖/奶盖绿茶”合并统计，平均份量约 580 g，总糖 3.5 g/100 g（范围 1.4–5.6），能量 57 kcal/100 g（范围 40–74）。这组数据不能拆成芝士茶与普通奶盖茶各自的平均值。",
        "evidence": "本轮 R1 检索未找到以统一定义的奶盖茶为对象、可确认健康因果的直接人体试验。普通茶或加奶红茶研究没有测这层泡沫的配方和真实门店份量。",
        "safety": "泡沫与茶底的糖、能量、乳成分和咖啡因应分别看配方；名称“奶盖”本身不能说明具体奶源或过敏原。",
        "references": [
            'Hong Kong Centre for Food Safety and Consumer Council. “Sugar and Energy Contents of Common Non-Indigenous Tea-Based Beverages in Hong Kong.” 2018 sample survey, published 2019. [Official report](https://www.cfs.gov.hk/english/programme/programme_rafs/programme_rafs_n_01_26_abstract.html).',
            'Shi Z, Sun Z, Song Q, Qu M, Wang Z, Zang JJ. “Nutrient content of 122 kinds of retail handcrafted milk tea products in Shanghai.” *Journal of Environmental and Occupational Medicine*. 2023;40(7):756–760. DOI: [10.11836/JEOM22505](https://doi.org/10.11836/JEOM22505). 中文题名：上海122种市售现制奶茶中的营养成分。',
        ],
    },
    "fruit-tea": {
        "opening": "水果茶不是统一配方：有的含鲜果或果汁，有的主要是茶底、果味制品和糖浆。香港 2018 年抽样中，百香果红茶平均份量 530 g，总糖 7.1 g/100 g（4.7–11），能量 41 kcal/100 g；芒果绿茶平均份量 590 g，总糖 5.6 g/100 g（3.9–7.6），能量 37 kcal/100 g。这些是被测产品的结果，不代表所有水果茶。",
        "evidence": "本轮 R1 检索未找到能够把异质水果茶作为固定食品、并验证长期临床结局的直接人体试验。果汁、单个水果或茶叶研究都不能直接替代复合饮品；“无添加糖”也不等于水果本身没有糖。",
        "safety": "现制饮品需同时看甜味料、果汁/果泥、杯量和切配水果的卫生保存。实际成分应以标签或门店配方为准。",
        "references": [
            'Hong Kong Centre for Food Safety and Consumer Council. “Sugar and Energy Contents of Common Non-Indigenous Tea-Based Beverages in Hong Kong.” 2018 sample survey, published 2019. [Official report](https://www.cfs.gov.hk/english/programme/programme_rafs/programme_rafs_n_01_26_abstract.html).',
            'Shi Z, Sun Z, Song Q, Qu M, Wang Z, Zang JJ. “Nutrient content of 122 kinds of retail handcrafted milk tea products in Shanghai.” *Journal of Environmental and Occupational Medicine*. 2023;40(7):756–760. DOI: [10.11836/JEOM22505](https://doi.org/10.11836/JEOM22505). 中文题名：上海122种市售现制奶茶中的营养成分。',
        ],
    },
    "cheese-tea": {
        "opening": "芝士茶由茶底和乳酪/奶油类泡沫组成，常见配方还会加糖或盐。香港 2018 年检测将芝士奶盖与奶盖绿茶放在同一组，平均份量约 580 g，总糖 3.5 g/100 g（1.4–5.6），能量 57 kcal/100 g（40–74），因此这些数值不能专指芝士茶。",
        "evidence": "目前直接的人体干预证据不足。一项 32 只雄性小鼠、持续 21 天的研究报告：正常糖和半糖红茶芝士茶组的血糖高于水对照；无糖红茶芝士茶与半糖绿茶芝士茶组未见显著升高，体重没有显著变化。这是动物信号，不能推断人类糖尿病风险或治疗效果。",
        "safety": "乳品、盐、糖、茶底和杯量因产品而异；若有乳制品过敏或需要控制特定配料，应核对实际成分。",
        "references": [
            'Kurniati NF, Yuliani RAT. “The Effect of Green Tea and Black Tea in Cheese Tea Drinks on Body Weight and Diabetes Mellitus Risk in Male Swiss Webster Mice.” *Acta Pharmaceutica Indonesia*. 2022;47(1):43–47. DOI: [10.5614/api.v47i1.17043](https://doi.org/10.5614/api.v47i1.17043). Animal study.',
            'Hong Kong Centre for Food Safety and Consumer Council. “Sugar and Energy Contents of Common Non-Indigenous Tea-Based Beverages in Hong Kong.” 2018 sample survey, published 2019. [Official report](https://www.cfs.gov.hk/english/programme/programme_rafs/programme_rafs_n_01_26_abstract.html).',
        ],
    },
    "coconut-milk-tea": {
        "opening": "“椰乳茶”可能使用椰奶、椰味饮料、植脂配料或椰果；商品名不能确认椰乳的真实比例。本轮找到的香港饮料检测和上海现制奶茶调查都没有单列椰乳茶，因此不填入推算的糖、脂肪或能量均值，宜按具体标签和门店配方确认。",
        "evidence": "本轮 R1 检索未找到以椰乳茶整体为对象的直接人体干预研究。椰子、椰乳、茶或一般含糖饮品研究各自对应不同对象，不能拼成椰乳茶的功效证据。",
        "safety": "先辨认是否含真正椰乳、另加乳品、糖和过敏原；含咖啡因与否由茶底及用量决定。不同品牌不能按名称互换营养值。",
        "references": [
            'Hong Kong Centre for Food Safety and Consumer Council. “Sugar and Energy Contents of Common Non-Indigenous Tea-Based Beverages in Hong Kong.” 2018 sample survey, published 2019. [Official report](https://www.cfs.gov.hk/english/programme/programme_rafs/programme_rafs_n_01_26_abstract.html).',
            'Shi Z, Sun Z, Song Q, Qu M, Wang Z, Zang JJ. “Nutrient content of 122 kinds of retail handcrafted milk tea products in Shanghai.” *Journal of Environmental and Occupational Medicine*. 2023;40(7):756–760. DOI: [10.11836/JEOM22505](https://doi.org/10.11836/JEOM22505). 中文题名：上海122种市售现制奶茶中的营养成分。',
        ],
    },
    "oat-milk-tea": {
        "opening": "燕麦奶茶由茶浸液和一种具体配方的燕麦饮料混合而成；燕麦饮品牌、植物油、强化成分和加糖情况差异明显。本轮没有找到可代表全品类的市场营养抽样，因此不从普通燕麦饮或其他奶茶填入整杯数值。",
        "evidence": "两项燕麦奶茶模型研究分别使用稳定性和体外模拟消化方法，显示结果会随燕麦饮脂肪含量与茶多酚浓度变化。它们没有测实际饮用后的人体血糖、血脂或饱腹结局，不能写成燕麦奶茶的临床功效。",
        "safety": "查看具体燕麦饮的糖、油脂、强化营养素和过敏原信息；茶底的咖啡因与浓度也依配方而变。",
        "references": [
            'Qin S, Li R, Chen M, et al. “Oat Milk Tea Model System: Exploring the Stability of Milk Tea and the Bioaccessibility of Green Tea Polyphenols.” *Foods*. 2023;12(7):1402. DOI: [10.3390/foods12071402](https://doi.org/10.3390/foods12071402). PMID: 37048223. In vitro model.',
            'Qin S, Li R, McClements DJ, et al. “Macronutrient digestion and polyphenol bioaccessibility in oat milk tea products: an in vitro gastrointestinal tract study.” *Food & Function*. 2024;15(14):7478–7490. DOI: [10.1039/D4FO01439A](https://doi.org/10.1039/D4FO01439A). PMID: 38915263. In vitro model.',
        ],
    },
    "brown-sugar-milk-tea": {
        "opening": "黑糖奶茶通常是茶底、乳基底和黑糖/红糖或糖浆的组合，但“黑糖”名称不能量化加糖克数，也不能保证其他配料一致。本轮市场抽样没有提供黑糖奶茶专属的代表性均值，因此不借用珍珠奶茶或普通奶茶数据。",
        "evidence": "本轮 R1 检索未找到黑糖奶茶整体的人体临床试验。糖或咖啡因单独研究，以及其他奶茶配方研究，都不能证明黑糖奶茶的长期健康效果。",
        "safety": "关注整杯添加糖、容量、茶底咖啡因及奶源。少糖与换奶会改变暴露，但实际数值要看店家配方或标签。",
        "references": [
            'Hong Kong Centre for Food Safety and Consumer Council. “Sugar and Energy Contents of Common Non-Indigenous Tea-Based Beverages in Hong Kong.” 2018 sample survey, published 2019. [Official report](https://www.cfs.gov.hk/english/programme/programme_rafs/programme_rafs_n_01_26_abstract.html).',
            'Shi Z, Sun Z, Song Q, Qu M, Wang Z, Zang JJ. “Nutrient content of 122 kinds of retail handcrafted milk tea products in Shanghai.” *Journal of Environmental and Occupational Medicine*. 2023;40(7):756–760. DOI: [10.11836/JEOM22505](https://doi.org/10.11836/JEOM22505). 中文题名：上海122种市售现制奶茶中的营养成分。',
        ],
    },
    "matcha-latte": {
        "opening": "抹茶拿铁把整份抹茶粉与牛乳或植物饮混合；粉量、奶种和糖浆都影响整杯。香港 2018 年抽样的平均份量约 490 g，总糖 5.2 g/100 g（3.0–11），能量 56 kcal/100 g（38–74）；无添加糖组的总糖仍为 2.9 g/100 g（1.5–4.8）。这些是样本值，不是所有品牌的固定配方。",
        "evidence": "一项日本双盲平行先导试验让吸烟者连续两周每天喝两份实验用粉末抹茶拿铁或焙茶拿铁：18 人同意参加，13 人进入分析。状态焦虑和唾液皮质醇没有显著组间差异；唾液 α-淀粉酶的反应轨迹只是替代指标的探索性信号。试验产品由 Nestlé Japan 提供/协作，研究获抹茶与健康研究会资助，不能据此宣称抹茶拿铁已证实减压。另有 23 人的单次抹茶饮/食品棒研究，并非奶基抹茶拿铁，也未显示情绪量表稳定改善。",
        "safety": "抹茶粉被一并摄入，咖啡因暴露不能按淡泡绿茶猜测；需按粉量、产品和份量判断。",
        "references": [
            'Monobe M, Nomura S, Ema K. “Influence of Continuous Ingestion of Matcha Latte on Stress: A Preliminary Study.” *Tea Research Journal*. 2021;131:9–14. DOI: [10.5979/cha.2021.131_9](https://doi.org/10.5979/cha.2021.131_9). 中文题名：抹茶ラテの連続飲用がストレスへ与える影響についての予備的調査. Full text available.',
            'Dietz C, Dekker M, Piqueras-Fiszman B. “An intervention study on the effect of matcha tea, in drink and snack bar formats, on mood and cognitive performance.” *Food Research International*. 2017;99(Pt 1):72–83. DOI: [10.1016/j.foodres.2017.05.002](https://doi.org/10.1016/j.foodres.2017.05.002). PMID: 28784536.',
            'Hong Kong Centre for Food Safety and Consumer Council. “Sugar and Energy Contents of Common Non-Indigenous Tea-Based Beverages in Hong Kong.” 2018 sample survey, published 2019. [Official report](https://www.cfs.gov.hk/english/programme/programme_rafs/programme_rafs_n_01_26_abstract.html).',
        ],
    },
    "hojicha-latte": {
        "opening": "焙茶拿铁可以使用焙火茶浸液或焙茶粉，也可加牛乳/植物饮和糖浆。本轮未找到可代表全品类的营养或咖啡因抽样。",
        "evidence": "一项抹茶拿铁先导试验把焙茶拿铁当作比较饮品；该试验不是为验证焙茶拿铁效果而设计。该特定试验配方每天两份提供约 129.6 kcal、碳水 24.5 g、咖啡因 4.8 mg，仅能说明研究用产品，不能代表其他品牌或证明焙茶拿铁功效。",
        "safety": "粉末/浸液、茶量、奶基底和糖浆会改变成分；按具体产品确认咖啡因与糖。",
        "references": [
            'Monobe M, Nomura S, Ema K. “Influence of Continuous Ingestion of Matcha Latte on Stress: A Preliminary Study.” *Tea Research Journal*. 2021;131:9–14. DOI: [10.5979/cha.2021.131_9](https://doi.org/10.5979/cha.2021.131_9). Hojicha latte was the comparator beverage; this was not an efficacy trial of hojicha.',
        ],
    },
    "bottled-unsweetened-tea": {
        "opening": "无糖瓶装茶是预包装即饮茶，可能使用绿茶、红茶、乌龙茶等；“无糖”标签不能说明咖啡因含量。香港 2018 年调查的 11 款预包装茶饮跨多个类型，平均总糖约 15 g/份、能量 80 kcal/份，并未单独报告无糖瓶装茶，因此这些数值不适用于本条。",
        "evidence": "Kaku 等 2024 年的实验室筛查把 10 名参与者的稀释唾液接种到不同瓶装茶样品，部分近中性 pH 绿茶样品出现唾液细菌生长。这研究针对直接对瓶饮用后的剩余饮料，不是未开封产品的货架期试验，也没有消费者感染或疾病结局。茶叶咖啡因调查测的是原料茶叶，不能代替瓶装成品检测。",
        "safety": "按每瓶标签核对糖、甜味剂、份量和咖啡因；开封后遵循产品储存说明。实验室筛查结果不能推广到所有厂家或解释为瓶装茶普遍不安全。",
        "references": [
            'Kaku N, Kawachi M, Wakui A, et al. “Molecular microbiological profiling of bottled unsweetened tea beverages: A screening experiment.” *Journal of Oral Biosciences*. 2024;66(3):628–632. DOI: [10.1016/j.job.2024.07.006](https://doi.org/10.1016/j.job.2024.07.006). PMID: 39069173. Laboratory screening.',
            'Yong L, et al. “Quantitative probabilistic assessment of caffeine intake from tea in Chinese adult consumers based on nationwide caffeine content determination and tea consumption survey.” *Food and Chemical Toxicology*. 2022;165:113102. DOI: [10.1016/j.fct.2022.113102](https://doi.org/10.1016/j.fct.2022.113102). PMID: 35513285. Tea-leaf samples, not ready-to-drink bottled tea.',
            'Hong Kong Centre for Food Safety and Consumer Council. “Sugar and Energy Contents of Common Non-Indigenous Tea-Based Beverages in Hong Kong.” 2018 sample survey, published 2019. [Official report](https://www.cfs.gov.hk/english/programme/programme_rafs/programme_rafs_n_01_26_abstract.html).',
        ],
    },
}


def reader_layer(entry_id: str) -> str:
    data = json.loads((RAW / f"{entry_id}.json").read_text(encoding="utf-8"))
    a = data["runs"][0]["native_answers"]
    taste_labels = {"sour": "酸", "bitter": "苦", "sweet": "甘", "pungent": "辛", "salty": "咸"}
    tastes = sorted(((taste_labels[k.removeprefix("taste_")], v["noul"]) for k, v in a.items() if k.startswith("taste_")), key=lambda x: -x[1])
    organs = {"heart": "心", "liver": "肝", "spleen": "脾", "lung": "肺", "kidney": "肾"}
    max_meridian = max((a[f"meridian_{key}"]["noul"], label) for key, label in organs.items())
    mapping_lines = (ROOT / "references/entries" / entry_id / "mapping.md").read_text(encoding="utf-8").splitlines()
    section = ""
    qi_grades = {}
    taste_grades = {}
    for line in mapping_lines:
        if line == "## 四气":
            section = "qi"
        elif line == "## 五味":
            section = "taste"
        elif line.startswith("## 五脏"):
            section = ""
        elif section and line.startswith("|") and not line.startswith("|---"):
            cells = [x.strip() for x in line.split("|")]
            if section == "qi" and len(cells) >= 4 and cells[1] in {"寒", "凉", "平", "温", "热"}:
                qi_grades[cells[1]] = cells[3]
            elif section == "taste" and len(cells) >= 5 and cells[1] in set(taste_labels.values()):
                taste_grades[cells[1]] = cells[3]
    qi = a["qi"]
    taste_text = "、".join(f"{label} {score:.2f}" for label, score in tastes[:2])
    qi_m = qi_grades.get(qi["choice"], "M-0")
    mapped_tastes = [label for label, grade in taste_grades.items() if grade == "M-IV"]
    taste_m_text = "、".join(f"{x} M-IV" for x in mapped_tastes) if mapped_tastes else "各味 M-0"
    return (
        f"Jev v0.4 的四气 Choice 为**{qi['choice']}**（原生倾向分数 {qi['probabilities'][qi['choice']]:.2f}；Choice confidence {qi['confidence']:.2f}），该项 M：{qi_m}。"
        f"五味原生分数相对靠前的是{taste_text}；有感官依据的味只作 M-IV 类推（{taste_m_text}）。"
        f"最高归经 Noul 为{max_meridian[1]} {max_meridian[0]:.2f}，仍低于项目读者层展示线；所有方向 Choice 和概率保留在 mapping.md 与原始 JSON，五脏归经及方向 M-0。"
        "这些模型分数不是真实世界概率，也不能由高分推成临床效应。"
    )


def main() -> None:
    for entry_id, parts in CONTENT.items():
        if not (ROOT / "references/entries" / entry_id / "mapping.md").exists():
            raise FileNotFoundError(f"Build Mapping first: {entry_id}")
        body = f"""# {NAMES[entry_id]}\n\n{parts['opening']}\n\n{parts['evidence']}\n\n**安全与选择。** {parts['safety']}\n\n**本草按。** {reader_layer(entry_id)} 传统茶母本的记载只作历史来源；复合配方与现代加工的边界见研究底稿。\n\n研究底稿：[research.md](../references/entries/{entry_id}/research.md) · 冻结摘要：[summary.md](../references/entries/{entry_id}/summary.md) · Jev 与 M 记录：[mapping.md](../references/entries/{entry_id}/mapping.md)。\n\n**参考文献**\n\n"""
        body += "\n".join(f"{i}. {ref}" for i, ref in enumerate(parts["references"], 1)) + "\n"
        (ROOT / "entries" / f"{entry_id}.md").write_text(body, encoding="utf-8")
    print(f"Wrote {len(CONTENT)} reader-facing entries from frozen evidence and mappings.")


if __name__ == "__main__":
    main()
