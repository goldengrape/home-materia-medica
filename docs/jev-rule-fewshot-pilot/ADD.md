# Design Split — Jev 四气五味归经 Pilot v0.3.1

> 来源：`URD.md`

## 1. Functional Requirements

| ID | Functional Requirement |
|---|---|
| ADD-FR-001 | Jev 接收自然语言说明文档，而不是要求固定 Evidence Packet JSON schema。 |
| ADD-FR-002 | rules 教授从感官 / 功能 / 症候到四气、五味、五脏归经的推理链。 |
| ADD-FR-003 | five-shot 与 held-out 分离，且二者使用相同推理规则。 |
| ADD-FR-004 | question schema 固定输出空间；rules 不重复接口约束。 |
| ADD-FR-005 | 保存 Jev 原生概率并完成可复查评分。 |
| ADD-FR-006 | 五脏功能群投影在 rules、few-shot gold、held-out gold 三处保持一致。 |
| ADD-FR-007 | API key 仅通过 GitHub Environment Secret 注入。 |

## 2. Design Parameters

| ID | Design Parameter |
|---|---|
| ADD-DP-001 | `state` 是单一 Markdown string：reasoning rules + narrative five-shot + narrative target。 |
| ADD-DP-002 | `fixtures-v0.3.1.json` 中 reference / target 都以 `document` 字符串存说明文档，meta/gold 只供评分端。 |
| ADD-DP-003 | questions = 1 Choice（四气）+ 5 Noul（五味）+ 5 Noul（五脏归经）。 |
| ADD-DP-004 | rules 显式定义症候功能群、寒热强弱、五味功能模式及五脏功能群投影。 |
| ADD-DP-005 | runner 在发送前检查 held-out 药名与 URL 未进入 state。 |
| ADD-DP-006 | 同一 workflow run 内重复 3 次，逐次保存原生结果。 |
| ADD-DP-007 | GitHub Actions job 绑定 `environment: API_KEYS`。 |

## 3. Design Matrix

| FR \ DP | 001 | 002 | 003 | 004 | 005 | 006 | 007 |
|---|---:|---:|---:|---:|---:|---:|---:|
| FR-001 | X | X |  |  |  |  |  |
| FR-002 | X |  |  | X |  |  |  |
| FR-003 | X | X |  | X |  |  |  |
| FR-004 |  |  | X | X |  |  |  |
| FR-005 |  |  | X |  |  | X |  |
| FR-006 |  | X |  | X |  |  |  |
| FR-007 |  |  |  |  |  |  | X |

分类：**Decoupled，可接受。**  
推理知识、输入文档、输出 question schema 与 secret 管理分层。

## 4. 关键设计决定

### DEC-001｜不训练校准函数

Jev probability / Noul 原样保存。不做 Platt、isotonic、temperature scaling 或手工 probability transform。

### DEC-011｜rules 是推理知识，不是接口说明

rules 只回答：

- 怎么从热证 / 寒证区分四气；
- 怎么从功能模式与感官判断五味；
- 怎么把症状聚成脏腑功能群；
- 怎么处理同一症状同时影响四气和归经。

“只能输出哪几个 key”由 questions 保证，不写进 reasoning rules。

### DEC-012｜target 是自然语言说明文档

runner 不解析 target 文档结构，也不要求固定 headings。未来只要正式生产的说明文档能作为字符串传入，即可复用同一调用方式。

### DEC-013｜five-shot 同样是自然语言文档

示例不是字段化特征表，而是与 target 同一文体的说明文档，后接标准结果。

### DEC-014｜五脏功能群工作投影

产品只输出五脏，因此：

```text
胆 -> 肝
胃 -> 脾
大肠 -> 肺
小肠 -> 心
膀胱 -> 肾
三焦 -> 按具体语境
```

这是输出投影规则，不是传统归经等价关系。

### DEC-015｜reasoning-complete benchmark

本阶段中药样本必须满足“说明文档足以推出 gold”。目的在于验证 Jev 是否会遵循项目推理链，而不是考察缺失证据条件下的猜测能力。

## 5. 当前数据流

```text
Research source
    ↓
自然语言说明文档
    ↓
[ reasoning rules + five-shot + target document ]
    ↓
Jev questions
    ├─ 四气 Choice
    ├─ 五味 5 Noul
    └─ 五脏归经 5 Noul
    ↓
原生概率
    ↓
benchmark / future Materia mapping
```

## 6. 已接受限制

- 中药功能主治与传统性味归经并非独立生成，因此本测试只验证规则执行能力。
- reasoning-complete 文档会比未来真实现代食品 dossier 更容易推断。
- 真正的项目可行性要靠下一阶段现代食品 domain-transfer test，而不能由本轮 5/5 证明。
