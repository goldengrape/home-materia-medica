---
name: home-materia-jev-mapping
description: >
  为《居家本草》把已经完成研究整理的自然语言说明文档交给 Jev，
  按 v0.4 reasoning rules + five-shot 判断四气、五味、五脏归经，
  并为每个五脏归经给出阴-/阴+/阳-/阳+的主作用方向 Choice。
  保存 Jev 原生 score / probability，并与 Research Dossier 中独立评定的 M-I～M-0 证据等级并列输出。
  本 skill 不负责检索证据，不用 M 修改 Jev score，也不把 Jev score 当作证据强度。
---

# Home Materia Jev Mapping v0.4

## 目标

本 skill 负责 `docs/生产流程.md` 的第三阶段“判”。

正式输入是冻结的 `summary.md`；`research.md` 只用于 Jev 分类完成后的 M 证据标注。

它先输出四层原子分类：

```text
四气 = 全局寒热属性
五味 = 全局功能模式
归经 = 作用位置
阴阳± = 该位置上的主作用方向
```

传统习惯用词，如“疏肝、健脾、润肺、温中、化湿、生津”，属于后续派生表达，不作为一级分类字段。

必须保持：

```text
Jev score != M grade
```

Jev score 表示模型在固定规则、few-shot、说明文档和具体模型版本下的判断倾向；M grade 表示项目可追溯证据链强度。两者独立。

---

## 运行前必须读取

1. `docs/居家本草编纂凡例-v1.0.md`
2. `docs/生产流程.md`
3. 目标条目的 Summary Document：
   - `references/entries/<entry-id>/summary.md`
4. 对应 Research Dossier（只在分类后评 M 时读取）：
   - `references/entries/<entry-id>/research.md`
   - 或 `references/shared/<entry-id>/research.md`
5. `references/reasoning-rules-v0.4.md`
6. `references/five-shot-v0.4.md`
7. `references/output-contract-v0.4.md`
8. `references/runtime.md`

当前已验证实现：

- `experiments/jev-rule-fewshot-pilot/run_pilot_v04.py`
- `experiments/jev-rule-fewshot-pilot/fixtures-v0.4.json`
- `experiments/jev-rule-fewshot-pilot/run_domain_transfer_v04.py`

v0.3.1 文件保留为历史回归基线。

---

## 输入

### Summary Document

target 必须是阶段二冻结的 `references/entries/<entry-id>/summary.md`，不允许为了本次分类临时另造一份答案导向说明，也不要求拆成固定 JSON 特征字段。

允许包含：

- 感官特征；
- 传统功能 / 主治；
- 现代人体效应；
- 加工、剂量、时机；
- 机制辅助；
- 冲突、反证、替代解释；
- 脏腑功能群关系。

不得为了帮助 Jev 人工补写最终答案。

测试模式下，不发送：

- 最终四气 / 五味 / 归经；
- 主方向答案；
- M 等级；
- “暂不归经”；
- gold label。

---

## state

```text
# 判定方法
[reasoning-rules-v0.4.md]

# 参考示例
[five-shot-v0.4.md]

# 待判断说明文档
[target document]
```

rules 只负责推理，不重复 API 已经限定的输出字段。

---

## 语义上级连，计算上同步

逻辑顺序：

```text
说明文档
→ 判断归经位置
→ 判断该经主作用方向
```

API 实现：

> 归经与五个 direction Choice 在同一次 Jev request 中同时计算。

不先按归经 score 做 threshold，再启动第二次调用。

这样避免：

- 第一层漏经造成后级永久缺失；
- 0.49 / 0.51 边界波动改变 question schema；
- 重复发送同一说明文档；
- 把本来同源的“位置 + 方向”证据拆开。

---

## 固定 questions

总计 **16 个**。

### 四气

1 个 Choice：

- 寒
- 凉
- 平
- 温
- 热

### 五味

5 个独立 Noul：

- 酸
- 苦
- 甘
- 辛
- 咸

### 五脏归经

5 个独立 Noul：

- 心
- 肝
- 脾
- 肺
- 肾

### 每经主方向

5 个 Choice：

- `heart_direction`
- `liver_direction`
- `spleen_direction`
- `lung_direction`
- `kidney_direction`

每个 Choice 的固定备选：

```text
阴-
阴+
阳-
阳+
```

---

## 阴阳±工作定义

### 阳+

增加该经温煦、推动、活动、运化或其他功能性阳侧表现。

典型：

- 温；
- 助阳；
- 回阳；
- 健脾 / 健胃 / 助运；
- 对寒、虚寒、功能低下的纠偏。

### 阳-

减少该经热、火、亢进、升越或过强活动。

典型：

- 清热；
- 泻火；
- 平亢；
- 对热盛、火盛、亢奋的纠偏；
- 项目工作约定：`疏肝 → 肝阳-`。

### 阴+

增加该经滋养、津液、血、精、濡润、收摄等阴侧表现。

典型：

- 养阴；
- 生津；
- 润燥 / 润肺 / 润肠；
- 补血；
- 益精；
- 对津亏、阴虚、燥、精血不足的纠偏。

### 阴-

减少该经阴侧偏盛、停聚、积滞或壅滞。

典型：

- 化湿；
- 燥湿；
- 化痰；
- 利水；
- 消食 / 消积；
- 对寒湿、水停、痰湿、食积的纠偏。

### + / - 只表示作用方向

```text
阴- != 伤阴
阳- != 损阳
阴+ != 滋腻
阳+ != 上火
```

副作用和过量效应另属 Safety。

---

## 病机状态 != 食材作用方向

先识别被处理的状态，再识别食材造成的变化。

例如：

```text
心火亢盛
= 原始状态偏心阳过盛

清心泻火
= 食材作用方向：心阳-
```

同理：

```text
肾阳虚 + 补火助阳 → 肾阳+
肺燥 + 润肺生津 → 肺阴+
痰湿 + 化痰燥湿 → 对应经阴-
```

不得把病机状态本身当成食材方向。

---

## 混合效应

同一经可能同时具有多个方向。

v0.4 一级输出仍只选一个 **主方向**，但保存四个 Choice probabilities。

例如：

```text
肺阴+ 0.55
肺阳- 0.40
```

记录为：

> 肺经主方向阴+；同时存在较明显阳-次方向。

不得只保存 selected choice 而丢弃完整 probabilities。

---

## 五脏工作投影

当前产品只输出五脏：

- 胆 → 肝胆功能群 → 肝；
- 胃 → 脾胃功能群 → 脾；
- 大肠 → 肺与大肠功能群 → 肺；
- 小肠 → 心与小肠功能群 → 心；
- 膀胱 → 肾与膀胱功能群 → 肾；
- 三焦按具体上 / 中 / 下焦语境判断，不固定投影。

这是五字段工作投影，不等于传统理论中的经脉等同。

---

## Jev score 与 M grade

顺序固定：

```text
summary.md
→ Jev 分类
→ 保存原始 score / probabilities
→ 回查 research.md
→ 对已经出现的分类命题逐项评 M
→ mapping.md
```

M 不在 Jev 之前控制 Jev 是否输出候选。

允许：

```text
酸奶
脾：Jev 0.61｜M-0
主方向：阳+（0.40–0.45）
```

不允许：

- 因 M-0 把 Jev 0.61 改低；
- 因 Jev score 高把 M-IV 升成 M-II；
- 把 Jev probability 写成校准后的“真实概率”。

---

## 传统习惯用词作为派生层

后期维护轻量 lexicon：

```text
primitive classification
→ conventional wording
```

示例：

```text
肝 + 阳- → 疏肝 / 平肝等候选
脾 + 阳+ → 健脾 / 温中等候选
肺 + 阴+ → 润肺 / 生津等候选
脾 + 阴- → 化湿 / 消食等候选
```

不是严格一对一。最终用哪个词由正文语境决定。

Jev 原始分类永远保留，不被派生词反向修改。

---

## 保存原生结果

不得：

- Platt scaling；
- isotonic regression；
- temperature scaling；
- 手工改分；
- 因 M 等级改变 score；
- 多次运行后只选最好的一次。

普通生产调用可运行 1 次。

方法学测试、重要条目和边界样本推荐 3 次，保存每次原生值以及 min / max。

---

## 当前验证状态

### 中药 reasoning-complete regression

v0.4 有效回归：

- 5 个 held-out；
- 3 次重复；
- 四气：5/5 ×3；
- 五味 exact：5/5 ×3；
- 五脏归经 exact：5/5 ×3；
- 10 个有效归经的主方向：10/10 ×3；
- actual model：`jev-1.13.0`。

### 现代食品 domain transfer

冻结 v0.4 后：

- 开心果：脾阳+、肾阳+；
- 咖啡：脾阳+；
- 酸奶：脾阳+，但 direction 分布较分散；
- 黑巧克力：无主归经；
- 方便面：无主归经。

这些仍与 M grade 独立。

---

## 与前后阶段的接口

```text
home-materia-research
↓
research.md
↓
summary.md
↓
home-materia-jev-mapping
↓
Jev 四气 / 五味 / 归经 / 每经主方向
+ native scores
↓
回查 research.md，逐项标 M
↓
mapping.md
↓
writing
```

Research skill 拥有资料事实、D/E、安全和 Summary Document。

本 skill 拥有 Jev 原始分类，并负责在分类后把 M 证据强度附到这些分类命题上。

writing 层读取 `summary.md + mapping.md`，根据资料与分类选择读者熟悉的传统表达；不得重新分类。

---

## 输出格式

使用：

`templates/jev-mapping-result.md`

默认输出到：

`references/entries/<entry-id>/mapping.md`

至少保存：

1. `summary.md` ref / hash；
2. reasoning version；
3. five-shot version；
4. requested model；
5. actual model；
6. 四气完整 probabilities；
7. 五味 5 个 Noul；
8. 五脏 5 个 Noul；
9. 五个 direction Choice + 完整 probabilities；
10. repeat count；
11. M grade；
12. 支持、反证、替代解释。

---

## 完成前检查

- [ ] 输入来自已完成 Research Dossier？
- [ ] 没有为 Jev 补写答案导向句？
- [ ] 使用 v0.4 rules / five-shot / contract？
- [ ] 保存 Choice 全部 probabilities？
- [ ] 保存五味 / 归经全部 Noul？
- [ ] 区分病机状态和食材作用方向？
- [ ] Jev score 与 M grade 独立？
- [ ] 没把习惯术语当一级分类？
- [ ] 没把 Jev probability 解释成校准后的真实概率？
- [ ] 记录 actual model？
