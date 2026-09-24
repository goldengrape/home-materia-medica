# Precedents & Methodological Sources

本 skill 为《居家本草》重新设计，未直接复制下列 skill 的正文。这里记录检索到的可借鉴设计与方法学来源，便于追溯设计依据。

## Agent / research skills

### K-Dense — scientific-agent-skills / literature-review

可借鉴：

- planning → search → screening → extraction/appraisal → synthesis → citation verification；
- 检索式和日期留痕；
- thematic synthesis，而非逐篇摘要；
- bibliographic verification。

Source:
https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/literature-review/SKILL.md

### K-Dense — research-lookup / citation-management

可借鉴：

- claim-to-source research packet；
- 把“快速证据检索”与正式系统综述区分；
- DOI / PMID 和参考文献核验。

Sources:
https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/research-lookup/SKILL.md
https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/citation-management/SKILL.md

### PangenomeAI — academic-skills-food-nutrition / food-research

可借鉴：

- food / nutrition 专用工作流；
- PECO/PICO 与 food matrix × factor × outcome；
- 食品科学数据库和食品安全 / 监管来源；
- 系统综述与普通 narrative/deep review 分流；
- 单独的 screening / extraction / risk-of-bias / synthesis。

Source:
https://github.com/pangenomeai/academic-skills-food-nutrition/blob/main/food-research/SKILL.md

### agentic-research / systematic-review skills

可借鉴：

- protocol-first；
- inclusion/exclusion criteria；
- search / dedupe / screen / extract / RoB / GRADE 的模块化；
- 对 LLM 不擅长的风险偏倚和数字核验设置 human gate；
- “系统综述”一词只用于真正满足可复现完整流程的工作。

Examples:
https://github.com/kurtvalcorza/agentic-research
https://github.com/SkillMedev/skills/blob/main/skills/systematic-review/SKILL.md

### Natural-product agent skills

检索到的天然产物 skill 多偏向药物发现、结构鉴定、ChEMBL / PubChem、docking、ADMET，而不是“食品作为实际摄入物”的临床证据综合。

可借鉴之处：

- identity-first；
- compound disambiguation；
- 天然产物化学表征；
- 不同研究阶段的证据不可混写。

Examples:
https://github.com/Ficere/phytomet-pharma-eval
https://github.com/mims-harvard/ToolUniverse/blob/main/skills/tooluniverse-drug-research/SKILL.md

本项目不采用“分子对接分数 → 食品功效”的药物发现式推断。

---

## Authoritative methodological sources

### USDA Nutrition Evidence Systematic Review (NESR)

用于食品 / 营养问题的：

- protocol-driven review；
- intervention / exposure / comparator / outcome；
- risk of bias；
- consistency / precision / directness / generalizability；
- evidence scans 与 full systematic review 的区分。

https://nesr.usda.gov/methodology-overview

### ConPhyMP

用于天然产物 / 植物提取物的：

- botanical material identity；
- extract definition；
- phytochemical characterization；
- 复杂混合物和批次可重复性。

Heinrich M, et al. Best Practice in the chemical characterisation of extracts used in pharmacological and toxicological research—The ConPhyMP Guidelines. Front Pharmacol. 2022.

### CONSORT herbal interventions

用于识别草药临床试验是否充分报告干预物身份与制备。

Gagnier JJ, et al. Reporting randomized, controlled trials of herbal interventions: an elaborated CONSORT statement. Ann Intern Med. 2006.

### CONSORT-CHM Formulas 2017

在中药复方临床研究中，补充考虑：

- TCM pattern；
- formula/intervention 描述；
- harms；
- generalizability。

Cheng CW, et al. Ann Intern Med. 2017.

### WHO quality control methods for herbal materials

用于植物材料质量、身份、污染物、加工和质量控制背景。

### FDA Botanical Drug Development Guidance (2016)

用于理解 botanical products 作为复杂混合物时的：

- identity；
- manufacturing consistency；
- chemical characterization；
- quality control；
- clinical-development linkage。

本项目只借鉴其科学原则，不把普通食品当作 botanical drug。
