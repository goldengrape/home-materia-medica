---
name: home-materia-jev-mapping
description: >
  为《居家本草》把已经完成研究整理的自然语言说明文档交给 Jev，
  按固定 reasoning rules + five-shot 判断四气、五味和五脏归经，
  保存 Jev 原生 score，并与 Research Dossier 中独立评定的 M-I～M-0 证据等级并列输出。
  适用于“根据这份食材说明判断四气五味归经”“运行 Jev 本草映射”“给现有 dossier 增加 Jev 判定”等任务。
  本 skill 不负责检索研究证据，不用 M 等级修正 Jev score，也不把 Jev score 当作证据强度。
---

# Home Materia Jev Mapping

## 目标

本 skill 位于 Research Dossier 之后。

它回答两个彼此独立的问题：

1. **Jev inference**：按照固定推理规则阅读当前说明文档后，Jev 倾向于把该食材判成什么四气、五味和五脏归经？
2. **Evidence strength**：支持这些本草映射的项目证据链当前处于 M-I ～ M-0 哪一级？

必须保持：

```text
Jev score != M grade
```

高 Jev score 不自动意味着高 M；M-0 也不要求隐藏 Jev 的候选判断。

---

## 运行前必须读取

1. `docs/居家本草编纂凡例-v1.0.md`
2. 目标条目的 Research Dossier：
   - `references/entries/<entry-id>/research.md`
   - 或 `references/shared/<entry-id>/research.md`
3. `references/reasoning-rules.md`
4. `references/five-shot-v0.3.1.md`
5. `references/output-contract.md`

若当前仓库自动化可用，Jev v0.3.1 的已验证参考实现为：

- `experiments/jev-rule-fewshot-pilot/run_pilot_v031.py`
- `experiments/jev-rule-fewshot-pilot/fixtures-v0.3.1.json`

Domain-transfer 参考实现：

- `experiments/jev-rule-fewshot-pilot/run_domain_transfer_v01.py`

Skill 文档定义工作流；实验代码用于可复现调用和回归测试。

---

## 输入

### 1. 必须有自然语言说明文档

给 Jev 的 target 应是一段连续说明文档，而不是为了模型临时拼出的特征 JSON。

说明文档可以来自 Research Dossier 的综合整理，允许包含：

- 感官特征；
- 传统来源中的功能 / 主治；
- 现代人体效应；
- 加工、剂量、时机；
- 机制辅助；
- 冲突、反证和替代解释；
- 与脏腑功能群有关的解释。

### 2. 不把最终答案写进 target

不得为了帮助 Jev 而在 target 中直接写：

- “性寒 / 性温 / 性平”等最终四气答案；
- “五味为……”；
- “归脾 / 归肾……”；
- `M-I`～`M-0`；
- “暂不归经”；
- Claim Ledger 中已经完成的最终本草映射结论。

如果传统原始来源本身明确记载性味 / 归经，应在 Research Dossier 中保留为传统事实；是否把该直接标签放入 Jev target，应根据任务目的决定：

- **测试推理能力**：隐藏直接答案；
- **生产判定**：可保留真实说明文档原有事实，但结果必须注明其来源为直接传统记录，而非 Jev 独立推断。

### 3. 不强求结构化字段

禁止要求输入一定拆成：

```text
organoleptic_sensory
traditional_functions
traditional_indications
...
```

未来生产输入就是项目正式形成的说明文档。

---

## Jev 判定方法

### Step 1｜构造 state

state 使用以下顺序：

```text
# 判定方法

[references/reasoning-rules.md]

# 参考示例

[references/five-shot-v0.3.1.md]

# 待判断说明文档

[target document]
```

rules 只教授推理，不重复“必须选一个”“只能输出这些字段”等 API 约束。

### Step 2｜固定 questions

四气：

- Choice：寒 / 凉 / 平 / 温 / 热

五味：

- 酸
- 苦
- 甘
- 辛
- 咸

每味为独立 Noul。

五脏归经：

- 心
- 肝
- 脾
- 肺
- 肾

每经为独立 Noul。

Jev question schema 已经限定输出空间，因此 reasoning rules 不需要再次描述“只能选什么”。

### Step 3｜保存原生 score

不得：

- Platt scaling；
- isotonic regression；
- temperature scaling；
- 手工把 0.7 改成 0.4；
- 因 M 等级低而压低 Jev score；
- 因多次运行结果不同而只保留最好的一次。

推荐在评估 / 重要条目中重复 3 次，并保存：

```yaml
values: [0.58, 0.60, 0.61]
min: 0.58
max: 0.61
```

单次生产调用也允许，但必须标明只有单次 score。

---

## Evidence strength：M 等级独立评定

M 等级继续使用项目现有定义。

它不控制 Jev 能不能给候选，只描述映射证据链强弱。

因此以下结果完全合法：

```text
归经候选：脾
Jev score：0.58–0.61
M：M-0
```

含义是：

> Jev 在当前规则和说明文档下倾向于脾；但项目目前缺少足够独立证据把“现代酸奶归脾”作为强证据结论。

同理：

```text
归经候选：肾
Jev score：0.75–0.76
M：M-0
```

不能改写成“已有较强证据归肾”。

### M 不反向修改 score

禁止：

> M-0，所以把 Jev 0.76 改成 0.30。

也禁止：

> Jev 0.95，所以把 M-IV 升成 M-II。

二者必须独立。

---

## 结果组织

### 四气

记录：

- Jev Choice；
- 五个 Choice probabilities；
- 重复运行的选择稳定性；
- 对应 M grade；
- 证据说明。

例如：

```text
四气候选：温
Jev score：0.61–0.66
M：M-IV
```

### 五味

五个字段都保留 score。

面向正文或表格时，可突出较高候选，但不要丢弃原始结果。

例如：

```text
甘：0.64–0.66｜M-IV
辛：0.23–0.24｜M-0
苦：0.05–0.06｜M-0
酸：0.04–0.05｜M-0
咸：0.04–0.05｜M-0
```

### 五脏归经

五个字段均保留。

例如：

```text
脾：0.58–0.61｜M-0
肾：0.10–0.11｜M-0
肺：0.07–0.08｜M-0
心：0.05–0.06｜M-0
肝：0.04–0.05｜M-0
```

不要因为某项低于 0.5 就从研究记录中删除。

0.5 仅可作为展示“主要候选”的方便切点，不是项目证据阈值。

---

## 五脏工作投影

因为当前产品输出只保留心、肝、脾、肺、肾，说明文档中的六腑相关信息按功能群处理：

- 胆 → 肝胆功能群 → 肝；
- 胃 → 脾胃功能群 → 脾；
- 大肠 → 肺与大肠功能群 → 肺；
- 小肠 → 心与小肠功能群 → 心；
- 膀胱 → 肾与膀胱功能群 → 肾；
- 三焦不固定映射，按上焦 / 中焦 / 下焦具体语境判断。

这是五字段输出的工作投影，不表示传统理论中两者等同。

---

## 与 research skill 的接口

推荐顺序：

```text
home-materia-research
    ↓
Research Dossier
    ↓
形成自然语言说明文档
    ↓
home-materia-jev-mapping
    ↓
Jev 四气 / 五味 / 五脏归经 scores
    +
Dossier M grades
    ↓
Claim Ledger / writing
```

Research skill 负责：

- 证据检索；
- E 等级；
- Concept Trace；
- M 等级；
- 支持 / 反证 / 替代解释。

本 skill 负责：

- 将说明文档交给 Jev；
- 按固定推理方法得到候选；
- 保存原生 scores；
- 与 M 等级并列呈现。

不得让 Jev 结果反向改写 Research Dossier 的事实证据。

---

## 已知行为与边界

已验证的中药 reasoning-complete benchmark 中，v0.3.1 可稳定执行规则。

现代食品 domain-transfer v0.1 显示：

- 开心果：Jev 可给出脾、肾较高 score，而项目证据仍为 M-0；
- 酸奶：Jev 可稳定倾向脾，而项目证据仍为 M-0；
- 咖啡：脾 score 可在约 0.5 附近波动；
- 黑巧克力、方便面可以保持五脏 score 较低。

这些结果说明：

> Jev inference 与 M evidence grade 应并列展示，而不是互相覆盖。

---

## 输出格式

使用 `templates/jev-mapping-result.md`。

至少保存：

1. target document 版本或 hash；
2. reasoning version；
3. five-shot version；
4. requested Jev model alias；
5. actual Jev model；
6. 四气完整 probabilities；
7. 五味 5 项 Noul；
8. 五脏 5 项 Noul；
9. repeat count；
10. 每项对应 M grade；
11. 支持、反证和替代解释；
12. 一句面向读者的解释。

---

## 完成前检查

- [ ] 输入是否来自已经完成的 Research Dossier / 正式说明文档？
- [ ] 是否没有为了 Jev 人工补写答案导向句？
- [ ] rules 是否使用当前版本？
- [ ] five-shot 是否使用当前版本？
- [ ] 是否保存 Jev 原生 score？
- [ ] 是否把 Jev score 与 M grade 分开？
- [ ] 是否避免把 Jev score 解释成经过校准的真实概率？
- [ ] 是否保留低 score，而不是只保存 >0.5 的标签？
- [ ] 是否保留反证和替代解释？
- [ ] 是否记录 actual model version？
- [ ] 是否没有让 Jev 结果反向提升 M 等级？

只要最后两轴仍然分离，允许输出：

> **模型倾向明确，但证据等级很低。**
