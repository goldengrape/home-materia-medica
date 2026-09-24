# Project Map — Jev 四气五味归经 Pilot

> 当前有效版本：v0.3.1  
> 本文件只追踪本 pilot，不替代项目根级 `docs/TRACE.md`。

## 1. Requirement → Design → Test

| Requirement | Design | Test |
|---|---|---|
| URD-REQ-001 说明文档判定 | ADD-DP-001/002 | TDD-TEST-001/004 |
| URD-REQ-002 rule + five-shot，无训练 | DEC-001 / DEC-011 / DEC-013 | TDD-TEST-002 |
| URD-REQ-003 原生概率 | DEC-001 / ADD-DP-006 | TDD-TEST-006/007 |
| URD-REQ-004 匿名 held-out | ADD-DP-002/005 | TDD-TEST-003/008 |
| URD-REQ-005 封闭输出字段 | ADD-DP-003 | TDD-TEST-005 |
| URD-REQ-006 重复稳定性 | ADD-DP-006 | TDD-TEST-007 |
| URD-REQ-007 rules 只承担推理 | DEC-011 | TDD-TEST-002 |
| URD-REQ-008 target 为自然语言 | DEC-012 | TDD-TEST-001 |
| 五脏功能群投影一致 | DEC-014 | TDD-TEST-012 |
| Secret 不入库 | ADD-DP-007 | TDD-TEST-010 |

## 2. 当前权威 artifacts

| Artifact | Role |
|---|---|
| `docs/jev-rule-fewshot-pilot/URD.md` | 当前需求与输入 / 输出契约 |
| `docs/jev-rule-fewshot-pilot/ADD.md` | 当前设计拆分 |
| `docs/jev-rule-fewshot-pilot/TDD.md` | 当前测试与 invalid-run 规则 |
| `docs/jev-rule-fewshot-pilot/V0.3.1-DESIGN-CORRECTION.md` | v0.3 → v0.3.1 修正原因 |
| `experiments/jev-rule-fewshot-pilot/fixtures-v0.3.1.json` | narrative five-shot + held-out + gold |
| `experiments/jev-rule-fewshot-pilot/run_pilot_v031.py` | reasoning rules、Jev 调用、重复和评分 |
| `.github/workflows/jev-rule-fewshot-pilot.yml` | API_KEYS environment workflow |
| `docs/jev-rule-fewshot-pilot/RESULTS-v0.3.1.md` | 当前有效结果 |

## 3. 历史版本

- v0.1：API / secret / anonymous pipeline proof；归经输出空间错误，历史记录。
- v0.2：封闭字段正确，但 target 仍是结构化 packet；归经 recall 低。
- v0.3 #11：首次 narrative + reasoning rules；发现 test-contract 不一致，标记 invalid。
- v0.3.1 #14：修正五脏功能群投影和 reasoning-complete held-out，当前有效。

## 4. 当前数据流

```text
Research Dossier
  → 自然语言说明文档
  → reasoning rules
  + narrative five-shot
  → Jev fixed questions
  → native probabilities
  → Materia mapping / Claim Ledger
```

## 5. Stop Conditions

- state 泄漏 gold / held-out identity；
- five-shot 与 test 重合；
- 文档无法从内部推出 gold；
- rules / gold 使用不同归经投影；
- response schema 改变；
- model alias / actual version 未记录；
- secret 泄漏。

任一发生则 benchmark invalid。

## 6. 下一阶段

**domain-transfer test**：

从现有现代食品 Research Dossier 生成与未来生产一致的说明文档，不为 Jev 另造结构化 packet，再用 frozen v0.3.1 reasoning rules + five-shot 进行判断。
