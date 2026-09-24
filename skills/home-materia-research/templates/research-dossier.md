# Research Dossier — {{entry_name}}

> entry_id: {{entry_id}}  
> research_depth: R1 / R2 / R3  
> status: researching / review_ready  
> evidence_cutoff: YYYY-MM-DD  
> researcher:  
> last_updated: YYYY-MM-DD

## 1. 条目身份

### 1.1 定义
- 条目：
- 类型：
- 主目录：
- 传统母条：
- 研究对象：
- 常见变体：

### 1.2 Identity Card

```yaml
ingredients:
processing:
typical_serving:
key_variables:
processing_or_customization_variables: []
identity_confidence:
```

### 1.3 Identity Revision（若研究改变条目边界）

```yaml
identity_revision:
  changed: no
  original_entry_id:
  revised_entry_id:
  reason:
  catalog_action:
```

若 `changed: yes`，必须同步建议 Catalog 如何处理；不得只在 dossier 中悄悄改名。

### 1.4 天然产物附加信息（适用时）

```yaml
scientific_name:
plant_part:
origin_or_cultivar:
processing:
extract_solvent:
drug_extract_ratio:
standardization_marker:
chemical_characterization:
voucher_or_authentication:
```

---

## 2. 研究范围

### 核心问题

1.
2.
3.

### 明确不在本轮解决的问题

-

---

## 3. 检索日志

| 日期 | 数据库 / 来源 | 检索式 | 结果数 | 用途 |
|---|---|---|---:|---|

---

## 4. 传统文献

| 来源 | 时代 / 版本 | 原文位置 | 可确认内容 | 身份对应问题 |
|---|---|---|---|---|

### 传统结论

-

---

## 5. 中医概念溯源

| 概念 | 原典 / 早期用法 | 后世理论化 | 现代工作定义 | 异说 / 限制 | 本项目采用方式 |
|---|---|---|---|---|---|

### Concept Trace

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

### 使用过的中医数据库 / 资源

| 数据库 / 资源 | 检索日期 | 查询词 | relation type | 用途 | 是否回到原始来源 |
|---|---|---|---|---|---|

---

## 6. 组成与真实暴露（复合食品或产品差异较大时）

> 本节记录“实际吃进去什么”，不强行使用 E 等级。

| 变量 | 典型范围 / 份量 | 产品差异 | 直接来源 | 备注 |
|---|---|---|---|---|

---

## 7. 现代证据地图

### Evidence-base overlap（适用时）

```yaml
evidence_base_overlap:
  level: low | moderate | high | unknown
  note:
```

多个 Meta / review 一致时，先判断是否高度共享同一批基础研究，避免按综述篇数重复计票。

| Claim / Outcome | 主要证据 | D | Risk of bias | 方向 | E | 备注 |
|---|---|---:|---|---|---|---|

---

## 8. 核心证据卡

### Study / Review 1

```yaml
citation:
doi:
pmid:
design:
population:
n:
food_or_exposure:
dose:
comparator:
duration:
outcomes:
effect_estimate:
confidence_interval:
adverse_events:
funding:
conflicts:
risk_of_bias:
evidence_distance:
directness_note:
full_text_status:
supports:
does_not_support:
```

---

## 9. 分结局综合

### Outcome A

**人体证据：**

**直接性：**

**剂量 / 加工 / 人群限定：**

**反向或冲突证据：**

**E 等级：**

**正文最大允许表述：**

**关键引用：**

---

## 10. 安全性

### 常见不良反应
-

### 严重安全信号
-

### 药物相互作用
-

### 特殊人群
-

### 监管 / 权威风险评估
-

---

## 11. 机制与成分

> 仅作为解释层，不代替人体效应。

| 机制 / 成分 | 证据类型 | 剂量可达性 | 与人体结果是否一致 | D | 可支持到什么程度 |
|---|---|---|---|---:|---|

---

## 12. 本草映射候选

### 候选 1：{{term}}

- 拟映射对象：
- 直接人体事实：
- 传统理论桥梁：
- 机制辅助：
- 支持：
- 反证：
- 替代解释：
- M 等级：
- 最大允许表述：

---

## 13. 冲突与未知

### 主要冲突
-

### 仍未知
-

### 不应声称
-

---

## 14. Claim Ledger

| ID | Claim mode | 正文候选命题 | 允许措辞 | E | M | D 范围 | 核心来源 |
|---|---|---|---|---|---|---|---|

---

## 15. 停止判断

```yaml
stopping_status:
stopping_reason:
evidence_cutoff:
```

### 为什么现在可以停止

-

### 什么新证据会触发重开研究

-

---

## 16. 参考资料清单（供作者 / 读者复核）

### 传统文献
-

### 现代人体研究
-

### 安全性
-

### 机制与成分
-

### 数据库入口
-

> 本节的目的不是声明这些来源已经过独立人工复审，而是让关键判断具有公开、可追踪、可自行审核的来源链。
