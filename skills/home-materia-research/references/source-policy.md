# Source & Search Policy

## 1. Source hierarchy by question

来源等级必须按“问题类型”选，不存在一个适合全部问题的固定排行榜。

### 人体健康效应
优先：

1. 权威系统综述 / 高质量 Meta-analysis；
2. 直接 RCT / 交叉试验；
3. 前瞻性队列；
4. 其他人体研究；
5. 机制资料。

### 食品成分 / 加工
优先：

1. 权威食品成分数据库 / 标准方法；
2. 直接分析研究；
3. 生产工艺 / 标准文件；
4. 商品标签（只代表对应商品，不外推全类别）。

### 安全
优先组合：

- 系统证据；
- 监管风险评估；
- 临床研究不良事件；
- 药物警戒；
- 病例报告；
- 相互作用机制。

### 天然产物身份
优先：

- 药典 / WHO / EMA/HMPC / 权威植物学来源；
- taxonomic databases；
- 原研究中的 voucher / authentication；
- 化学表征报告。

### 传统本草
优先：

- 原始文献；
- 可靠点校 / 影印本；
- 有版本信息的古籍数据库；
- 后世注解作为后世观点，不回写原作者。

---

## 2. Academic databases

根据可用权限选择。

优先考虑：

- PubMed / MEDLINE
- Cochrane Library
- Embase
- Web of Science / Scopus
- FSTA（食品科学）
- CAB Abstracts / AGRICOLA（相关时）
- 中文医学与学术数据库（中医 / 中国食品研究相关时）

不要因某数据库不可用就声称“没有研究”。

---

## 3. Official / structured sources

营养与食品：

- USDA NESR
- USDA FoodData Central（成分问题）
- EFSA
- FDA
- WHO
- Codex Alimentarius

草药 / 天然产物：

- WHO herbal monographs / quality-control materials
- EMA HMPC
- FDA Botanical Drug Development guidance
- national / regional pharmacopoeias
- PubChem / ChEMBL（成分、结构、bioactivity；不能替代人体疗效证据）

---

## 4. Search logging

每轮检索记录：

```yaml
database:
date:
query:
filters:
results_count:
purpose:
notes:
```

R1 可以简化；R2 / R3 必须保留可复现检索式。

---

## 5. Negative-search obligation

对每个核心健康命题，至少设计一次寻找反向证据的搜索，包括：

- null / no effect
- adverse / harm / safety
- heterogeneity
- conflicting
- dose response
- publication bias（综述层面）

不是机械加入英文词，而是确保研究过程真的寻找过“不支持我们预期”的资料。

---

## 6. Recency

优先找到最新高质量综述，但“新”不能替代“好”。

若近期综述建立在较弱研究上，而更早的关键试验设计更好，应保留关键原始研究。

必须记录系统综述的 **search cutoff**，而不只看发表年份。

---

## 7. Full text

关键结论优先全文核验。

允许 `abstract_only` 证据进入候选集，但：

- 不从摘要推断未报告的剂量、方法或不良事件；
- 不用 abstract-only 的单篇研究独立支撑高强度结论；
- R3 的核心争议尽量取得关键研究全文。

---

## 8. Preprints

可用于：

- 发现最新方向；
- 尚未正式发表的重要更新。

但必须标记 preprint，不与同行评议研究等同。

---

## 9. Industry funding

企业资助不是自动排除标准。

必须记录：

- funder；
- author conflicts；
- sponsor role（若报告）。

若资助与结果方向存在系统性疑虑，在证据综合中讨论，不用简单“企业资助 = 无效”替代方法学评价。

---

## 10. Citation integrity

禁止：

- AI 生成的虚构 DOI；
- 二手文章冒充原始论文；
- 只引用搜索摘要；
- 引用标题与正文结论不匹配；
- 论文已撤稿仍作为正常证据使用。

关键引用在完成前做 bibliographic verification。
