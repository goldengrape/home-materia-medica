# TCM Concepts, Skills & Public Databases

> 用途：为《居家本草》研究中的中医概念、传统母本、本草原文、方剂关联、中药身份与现代中药研究提供检索入口。  
> 检查日期：2026-09-23  
> 原则：数据库是**检索与发现工具**。凡涉及古籍原意、现代人体效应、性味或归经结论，应回到相应原始来源；数据库中的预测靶点、网络关系和自动映射不得直接当作事实结论。

---

## 一、中医概念的研究方式

《居家本草》会频繁使用“性、味、归经、升降浮沉、脏腑、证候、功效、配伍、炮制”等概念。不要假设这些概念在所有时代含义完全一致。

遇到核心概念时，建立 **Concept Trace**：

```yaml
term:
modern_working_definition:
early_sources: []
later_systematization: []
modern_textbook_definition:
disputed_or_variant_uses: []
project_usage:
source_notes:
```

### 三层来源必须分开

1. **原典 / 早期用语**  
   某一时代的原文到底如何使用该词。

2. **后世理论化 / 注家解释**  
   后世医家如何重新解释、归纳或系统化。

3. **现代教材 / 标准化定义**  
   现代中医学教材、标准或工具书如何定义。

正文如果使用的是现代标准化概念，应写成现代解释，不要倒写成“古人自古即如此定义”。

---

## 二、可借鉴的中医 Agent Skills

这些 skill 只借鉴**资料组织和可追溯设计**，不把其医家立场、诊疗规则或具体结论当作《居家本草》的学术依据。

### 1. YuanZHAO321 / TCM.Skill

https://github.com/YuanZHAO321/TCM.Skill

可借鉴：

- 教材层 → 经典层 → 医家层分层；
- 中药、方剂、诊断、经典原文之间建立互链；
- 明确区分教材转述与原典原文；
- 现代结论保留经典溯源入口。

局限：

- 主要面向中医知识与实际问答，不是食品证据综合；
- 部分剂量 / 安全信息依赖特定教材版本；
- 本项目只借其**知识层级与路由思想**。

### 2. zhongyishijia-skill

https://github.com/erikgqp8645/zhongyishijia-skill

可借鉴：

- evidence cards；
- 原文 → 蒸馏卡 → 查询结果的多层结构；
- card / chunk 级来源追溯；
- 关键词 0 命中时回到更原始数据层；
- 历代文献按时代排列，避免把不同时期观点混成一个“传统结论”；
- 截断或异文时重新取回原始文本，而不是补写。

局限：

- 基础数据来自特定网站的离线整理；
- 蒸馏数据和原始文献版本仍需读者自行判断；
- 本项目借用的是**原文可回取、朝代分层和证据卡**方法。

### 3. nihaixia-tcm / 相关课程型 skills

例如：

- https://github.com/JuneYaooo/nihaixia-tcm
- https://github.com/qmzz/ni-haisha-tcm-skill

可借鉴：

- 模块索引；
- PDF / 原文证据定位；
- “课程观点”和一般中医知识分开标记。

局限：

- 属于特定医家 / 课程体系；
- 不能作为《居家本草》对一般中医理论的优先权威来源。

---

# 三、公开古籍与传统文献入口

## A1. 国家中医药古籍数字图书馆

- 机构：中国中医科学院中医药信息研究所
- URL: http://www.cintcm.com/
- 类型：中医药古籍数字资源
- 用途：
  - 古典医籍；
  - 本草；
  - 方书；
  - 版本目录；
  - 民国文献；
  - 传统知识资源。
- 项目用法：优先用于**寻找原书、版本、影像或原文语境**。
- 证据角色：传统文献发现 / 原文核对。

### 注意

数据库检索结果不是“古籍共识”。必须记录具体书名、时代、版本和原文位置。

---

## A2. Chinese Text Project / 中国哲学书电子化计划

- URL: https://ctext.org/
- 类型：开放古籍全文与扫描资源
- 特点：
  - 大规模先秦至后世古籍；
  - 可全文检索；
  - 部分有扫描底本；
  - 医学类古籍也有收录。
- 项目用法：
  - 跨书检索某术语早期用法；
  - 比较词义时代变化；
  - 辅助定位原文。
- 证据角色：古籍检索入口。

### 注意

OCR、Wiki 文本及 AI 翻译不能视为校勘本。重要引文尽量回到扫描影像或可靠整理本。

---

# 四、中药身份、植物、药材、方剂的公共资源

## B1. 香港浸会大学 Chinese Medicine Digital Projects

总入口：
https://scm.hkbu.edu.hk/en/knowledge-transfer/Chinese-Medicine-Digital-Project.html

包含：

### Medicinal Plant Images Database

- 药用植物图像与植物信息；
- 适合核对植物学身份和原植物。

### Chinese Medicinal Material Images Database

- 常见中药材高清图像；
- 来源、产地、性状、品质、性味、功效、炮制品等；
- 适合研究“原植物 → 药材 → 炮制品”的身份链。

### Phytochemical Image Database

- 中草药化学成分；
- 结构、理化信息、分析方法和谱图等；
- 适合成分身份与分析学线索。

### Chinese Medicine Formulae Images Database

- 常见方剂组成、制法 / 剂型、功效、主治等；
- 适合方剂查找与配伍发现。

### Chinese Medicine Specimen Database

- 实物标本与相关信息。

### Chinese Medicine Diet and Health Images Database

- 传统中医饮食 / 食疗展示；
- 可用于发现传统食材组合，但不作为现代临床证据。

**证据角色：身份与教学型结构化资料。**

---

# 五、中药 / 方剂 / 成分 / 靶点 / 疾病数据库

## C1. ETCM 2.0 — Encyclopedia of Traditional Chinese Medicine

- URL: http://www.tcmip.cn/ETCM2/front/#/
- 公开可查询。
- 内容包括：
  - 大量古籍方剂；
  - 中成药；
  - 中药材；
  - 化学成分；
  - 已知 / 潜在靶点；
  - 疾病关系；
  - 部分质量标志物 / 定量信息。
- 适合：
  - 方剂—药材—成分交叉检索；
  - 发现传统方剂来源；
  - 机制研究入口。

**项目定位：发现工具。预测靶点不能直接支持人体效应或归经。**

---

## C2. HERB 2.0

- URL: http://herb.ac.cn/v2
- 公开可查询。
- 特色：
  - 中药、成分、靶点、疾病；
  - 高通量实验；
  - 文献人工整理；
  - 临床试验与 Meta-analysis 信息；
  - 知识图谱。
- 适合：
  - 快速发现某中药相关的人体研究 / 综述；
  - 找现代实验和机制文献入口；
  - 追踪 herb / ingredient / disease 关系。

**项目定位：文献发现优先级较高，但临床结论仍回到原论文。**

---

## C3. SymMap

- URL: https://www.symmap.org/
- 公开查询并提供下载。
- 特色组件：
  - herb；
  - syndrome；
  - TCM symptom；
  - modern-medicine symptom；
  - ingredient；
  - target；
  - disease。
- 特别价值：
  - 中医症状与现代症状映射；
  - herb–TCM symptom 等关系。

**项目定位：概念和症状映射的探索工具。**

### 特别警告

“TCM symptom ↔ modern symptom”是数据库映射，不代表两个概念完全等价。  
不得用 SymMap 的映射直接证明某现代功能 = 某中医证候 / 脏腑功能。

---

## C4. TCMBank

- URL: https://www.tcmbank.cn/
- 公开、可下载部分数据。
- 内容：
  - herbs；
  - ingredients；
  - targets；
  - diseases；
  - 多种关系网络。
- 适合：
  - 大范围中药 / 成分交叉查询；
  - 下载结构化数据进行批量分析。

**项目定位：大规模结构化发现工具。**

---

## C5. TCMSP

- URL: https://www.tcmsp-e.com/tcmsp.php
- 可公开查询，并提供部分数据库下载。
- 特色：
  - 中药；
  - 成分；
  - 靶点；
  - 疾病；
  - OB、drug-likeness、BBB、Caco-2 等预测 / ADME 指标。

**项目定位：历史上使用广泛的系统药理数据库。**

### 注意

- 数据库主体较老；
- ADME 筛选阈值和预测模型不是“活性成分已证实有效”的同义词；
- 不允许用 OB/DL 筛选结果直接推出食效或人体功效。

---

## C6. HIT 2.0

- URL: http://hit2.badd-cao.net/ （论文公布入口；可用性需实际访问时再检查）
- 内容：
  - herbal ingredient–target；
  - PubMed 文献描述的成分—靶点关系；
  - 质量指标和来源摘要。
- 适合：
  - 某个天然成分的靶点文献追踪；
  - 机制证据的来源定位。

**项目定位：成分级机制检索，不代表整味食品。**

---

## C7. BATMAN-TCM 2.0

- URL: http://bionet.ncpsb.org.cn/batman-tcm/
- 公开数据库 / 分析工具。
- 内容：
  - 已知 ingredient–target；
  - 大规模预测 ingredient–target；
  - pathway / disease enrichment；
  - 网络分析。
- 适合：
  - 机制假说；
  - 发现后续实验检索方向。

**项目定位：D3 / 机制假说工具。预测关系必须明确标记 predicted。**

---

## C8. TCMID

- URL: http://www.megabionet.org/tcmid/
- 老牌综合中医药数据库。
- 目前仍可作为历史数据或交叉核对入口。

**项目定位：备用。较老的数据优先用更新数据库交叉核对。**

---

# 六、安全与毒性

## D1. TCMToxDB

- URL: https://www.sdu-idea.cn/TCMToxDB
- 2026 年公开发布的中药毒理数据库。
- 内容侧重：
  - formulas / herbs / ingredients 的毒性资料；
  - 毒性表现；
  - 毒性靶点；
  - 文献记录；
  - 预测工具。
- 适合：
  - 中药 / 成分毒性安全扫描；
  - 找安全文献入口；
  - 发现潜在毒性机制。

**项目定位：安全性发现工具；严重安全判断仍优先回到原始病例、人体研究、监管资料。**

---

# 七、数据库使用时的证据标记

从结构化数据库获得的关系，应注明 relation provenance：

```yaml
database:
database_version_or_checked_date:
entity_a:
relation:
entity_b:
relation_type: curated | literature_mined | integrated | predicted | mapped
source_reference:
direct_evidence_retrieved: yes | no
notes:
```

### 使用强度

- **curated + 可回原文**：可作为文献发现和交叉核对；
- **literature_mined**：必须回到被挖掘的原论文；
- **integrated**：检查原始数据库来源；
- **predicted**：只能作机制假说；
- **mapped**：只能作概念桥梁或检索扩展。

---

# 八、《居家本草》建议的中医资料检索顺序

涉及中医概念或传统母本时：

1. **确定概念 / 药物 / 方剂名称与同义词**；
2. 国家中医药古籍数字图书馆 / CText 找原典；
3. 记录时代、版本、原文和上下文；
4. HKBU 数字项目核对植物 / 药材 / 方剂身份；
5. ETCM / HERB / TCMBank / SymMap 找结构化关联和现代研究线索；
6. PubMed / 其他学术数据库回到现代原始论文；
7. 安全问题额外查 TCMToxDB 和监管 / 临床资料；
8. 只有完成上述分层后，才进行 M 等级本草映射。

---

# 九、不采用的快捷推断

数据库出现：

> 某药 → 某靶点 → 某疾病

不能写成：

> 某药“治疗”该病。

数据库出现：

> 某中医症状 ↔ 某现代症状

不能写成：

> 二者是同一个概念。

数据库出现：

> 某成分预测靶向某通路

不能写成：

> 含该成分的食品具有对应中医功效。

数据库出现：

> 某药在整理表中“归肝经”

不能证明：

> 某现代食品因含此药 / 此成分也归肝经。

数据库的价值是**找到值得继续查的证据**，而不是缩短论证链。
