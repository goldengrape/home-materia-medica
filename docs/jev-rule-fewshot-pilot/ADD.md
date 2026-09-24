# Design Split — Jev 四气五味归经 Pilot

> 来源：`docs/jev-rule-fewshot-pilot/URD.md`

## 1. Functional Requirements

| ID | Functional Requirement |
|---|---|
| ADD-FR-001 | 测试资料必须与 gold 分离，发送给 Jev 的 target 不得含答案或药名。 |
| ADD-FR-002 | Jev 必须按同一套项目规则和固定 few-shot 示例判断所有 target。 |
| ADD-FR-003 | 四气、五味、归经必须使用适合其结构的 Jev question type。 |
| ADD-FR-004 | 保存 Jev 原生概率并生成可复查的 pilot 评分。 |
| ADD-FR-005 | API key 只能从 GitHub Environment Secret 注入。 |
| ADD-FR-006 | 实验必须可复跑，并记录模型、prompt、fixtures 版本。 |

## 2. Design Parameters

| ID | Design Parameter |
|---|---|
| ADD-DP-001 | 单一 `fixtures-v0.2.json`，将 `packet` 与 `gold` 分字段保存；runner 只把 `packet` 送给 Jev。 |
| ADD-DP-002 | 一个共享 structured state：`rules + reference_examples + target`；参考例与 target 明确分区。 |
| ADD-DP-003 | 四气 = 1 个五选一 Choice；五味 = 5 个固定 Noul；归经 = 心/肝/脾/肺/肾 5 个固定 Noul。 |
| ADD-DP-004 | runner 直接记录 Choice probabilities 与 Noul 值，再以 0.5 临时切分计算指标。 |
| ADD-DP-005 | GitHub Actions job 绑定 `environment: API_KEYS`，通过 `${{ secrets.JEV_API_KEY }}` 注入。 |
| ADD-DP-006 | 结果 JSON 保存 `model`、`prompt_version`、`fixture_version`、逐样本原始答案和 summary。 |

## 3. Design Matrix

`X` 表示主要依赖：

| FR \ DP | 001 | 002 | 003 | 004 | 005 | 006 |
|---|---:|---:|---:|---:|---:|---:|
| FR-001 | X |  |  |  |  |  |
| FR-002 |  | X |  |  |  |  |
| FR-003 |  |  | X |  |  |  |
| FR-004 |  |  | X | X |  | X |
| FR-005 |  |  |  |  | X |  |
| FR-006 | X | X |  |  |  | X |

### 分类

**Decoupled，可接受。**

评分必然依赖 question 输出格式，因此 FR-004 同时依赖 DP-003 / DP-004 / DP-006；这是按数据流顺序发生的显式依赖，不要求拆成伪独立模块。

## 4. 关键设计决定

### DEC-001｜不训练校准函数

Jev 原生概率原样保存。pilot 不使用 Platt scaling、isotonic regression、temperature scaling 或其他概率变换。

### DEC-002｜Few-shot 与测试样本严格分离

v0.2 reference examples 使用黄连、薄荷、山药、桂枝、附子 5 个药物；v0.2 held-out 使用黄芩、菊花、茯苓、细辛、干姜，两组不重叠。

### DEC-003｜target 匿名化

target 使用 `V2-T01`–`V2-T05`，发送给 Jev 的内容不含真实药名、拉丁名和直接性味归经字段。gold 只供本地评分。

### DEC-004｜规则放在 structured state

Jev API 没有 request-level system prompt。为避免把同一 five-shot 重复塞进 11 个 question，统一把：

```text
rules
reference_examples
target
```

放进 `state`，每个 question 只说明“依据 state 中规则与示例，仅判断 target”。

### DEC-005｜五味、归经按 multi-label 处理

五味和归经不能用互斥 Choice。每个标签单独使用 Noul，允许多个同时成立。

### DEC-006｜强制封闭分类

四气必须在寒、凉、平、温、热五类中选一个，不设“证据不足”。  
五味必须只在酸、苦、甘、辛、咸五字段内输出 Noul。  
归经必须只在心、肝、脾、肺、肾五字段内输出 Noul。  
schema 外概念没有输出位置，也不参与评分。

## 5. Shared State 规则

runner 发送给 Jev 的核心规则：

1. 只评估 `target`；`reference_examples` 只用于学习本项目判断方式。
2. 不尝试恢复被隐藏的药名，不把可能猜出的身份当作证据。
3. 四气按 pilot 五档归一：寒 / 凉 / 平 / 温 / 热；必须五选一。
4. 五味是传统本草属性，不等同于入口时字面味觉；感官只能作为一项证据。
5. 归经只允许心、肝、脾、肺、肾五个字段；传统功能、主治和脏腑语境可以支持，但单一词面对应不足以自动证明。
6. 资料冲突、桥梁不足或存在同等合理解释时降低概率，不为了“给答案”而提高确信。
7. 不使用任何 post-hoc 校准函数。

## 6. Few-shot 选择

| demo | 来源药物（不发送名称） | 主要覆盖 |
|---|---|---|
| V2-D01 | 黄连 | 寒；苦；心/肝/脾 |
| V2-D02 | 薄荷 | 凉；辛；肺/肝 |
| V2-D03 | 山药 | 平；甘；脾/肺/肾 |
| V2-D04 | 桂枝 | 温；辛/甘；心/肺 |
| V2-D05 | 附子 | 热；辛/甘；心/脾/肾；并展示“感官咸麻 ≠ 五味咸” |

目的不是覆盖全部组合，而是给 Jev 展示：

- 多味并存；
- 多经并存；
- 四气是单一主分类；
- 不同功能语境如何对应不同标签。

## 7. 已接受限制

### ADD-COUP-001｜传统功能与 gold 性味归经并非独立生成

这些资料来自同一中药知识体系，功能 / 主治与性味归经本来存在理论关联，因此本 pilot 测的是“能否从去标签资料恢复标准标签”，不是证明四气五味归经具有独立现代生物学可预测性。

风险控制：

- target 匿名；
- gold 不发送；
- 后续必须用现代食品完整 dossier 做外域测试，不能把本 pilot 成绩直接当生产准确率。
