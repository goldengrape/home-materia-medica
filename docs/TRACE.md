# 《居家本草》Project Trace

> 版本：v1.0-draft
> 作用：把项目目标 → 工作块 → 验收 → 执行任务连起来，只保留高价值追踪。

## 一、项目目标追踪

| Project Brief | 架构 / 数据 | QA | Roadmap |
|---|---|---|---|
| PB-GOAL-001 现代本草 | ARC-WS-001~008 | QA-CHECK-001~043 | RM-PHASE-010~080 |
| PB-GOAL-002 可读 | ARC-WS-005/007 | QA-CHECK-030~035 | RM-PHASE-030/060/080 |
| PB-GOAL-003 有边界研究 | ARC-WS-002/004 | QA-CHECK-011~019 | RM-PHASE-020/050 |
| PB-AC-001 方法一致 | ARC-WS-002 | QA-CHECK-002/014/017 | RM-PHASE-010/020 |
| PB-AC-002 来源可追溯 | CM-OBJ-002~007 | QA-CHECK-012/020~022/035 | RM-PHASE-020/070 |
| PB-AC-003 身份唯一 | ARC-WS-001 / CM-OBJ-001 | QA-CHECK-001/040 | RM-TASK-011/012 |
| PB-AC-004 研究写作分离 | ARC-IF-004/005 | QA-CHECK-003/034 | RM-PHASE-030 |
| PB-AC-005 允许未知 | ARC-WS-002/004 | QA-CHECK-018 | RM-PHASE-020 |
| PB-AC-006 规模可完成 | R1/R2/R3 + STOP | QA-CHECK-011/019 | RM-PHASE-020/050 |
| PB-AC-007 可维护 | CM 状态与 IDs | QA-CHECK-002/043 | RM-PHASE-040/070 |
| PB-CON-007/008 数字发布与无图片 | ARC-WS-007 | QA-CHECK-050~055 | RM-PHASE-080 |

## 二、当前仓库组件

| 组件 | 角色 | 下游 |
|---|---|---|
| `catalog/收录总目录.md` | 正式收录范围 | registry / research |
| `catalog/README.md` | 编目规则 | catalog metadata |
| `docs/居家本草编纂凡例-v1.0.md` | 研究规则 | research skill / dossier |
| `skills/home-materia-research/` | 研究执行器 | dossier |
| `skills/.../tcm-concepts-and-databases.md` | 中医资料路由 | concepts / dossier |

计划建立：

| 组件 | 任务 |
|---|---|
| `okf/` | RM-TASK-002（已建立最小项目地图） |
| `concepts/` | RM-TASK-003/010 |
| `catalog/entries.yaml` | RM-TASK-011 |
| `references/entries/` | RM-PHASE-020 |
| `skills/home-materia-writing/` | RM-PHASE-030 |
| `entries/` / `scenes/` | RM-PHASE-030/060 |
| `qa/` | RM-PHASE-040/070 |

## 三、标准生产链

```text
Catalog entry
  → Scope / R level
  → Identity Card
  → Core questions
  → Search log
  → Evidence records + D
  → Outcome synthesis + E
  → Concept Trace
  → Materia mapping + M
  → Safety
  → Claim Ledger
  → Research ready
  → Draft entry
  → QA
  → Publish ready
```

## 四、变更路由

- 同一食品重复 → Catalog；
- R/D/E/M 规则问题 → 凡例；
- 中医词义不清 → Concepts；
- 某条研究不完整 → Dossier；
- 正文夸大 → Entry；
- 多条共同漂移 → QA 提交项目级问题；
- skill 行为错误 → 先确认规则属于哪一层，再修拥有规则的来源。

## 五、当前任务

| Task | 状态 | 输出 |
|---|---|---|
| RM-TASK-001 项目级规划 | done | `docs/*.md` |
| RM-TASK-002 最小 OKF | done | `okf/` |
| RM-TASK-003 中医概念骨架 | next | `concepts/` |
| RM-TASK-011 Entry Registry | queued | `catalog/entries.yaml` |
| RM-TASK-012 Pilot 范围 | done | `docs/Pilot测试计划-v1.md` + `catalog/pilot-v1.yaml` |
| RM-TASK-020 开心果 R2 | done | `references/entries/pistachio/research.md` |
| RM-TASK-021 黑巧克力 R3 | done | `references/entries/dark-chocolate/research.md` |
| RM-TASK-022 珍珠奶茶 R2 | done | `references/entries/pearl-milk-tea/research.md` |
| RM-TASK-026 前三项 Pilot 方法复盘 | done | `qa/pilot/first-three-review.md` |
| RM-TASK-023 咖啡 research parent R3 | done | `references/shared/coffee-base/research.md` |
| RM-TASK-024 酸奶 R2 | next | `references/entries/yogurt/research.md` |
| RM-TASK-025 方便面 R2 | queued | `references/entries/instant-noodles/research.md` |

## 六、追踪原则

- 不创建没有实际用途的 ID；
- 一个事实只保留一个权威来源；
- 下游引用上游，不复制上游整段内容；
- 未来机器 trace 应由文档和实体 metadata 派生，不另造一套真相。