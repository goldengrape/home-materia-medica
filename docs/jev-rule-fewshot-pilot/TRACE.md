# Project Map — Jev 四气五味归经 Pilot

> 本文件只追踪本 pilot，不替代项目根级 `docs/TRACE.md`。

## 1. Requirement → Design → Test

| Requirement | Design | Test |
|---|---|---|
| URD-REQ-001 结构化判定 | ADD-DP-003 | TDD-TEST-002 |
| URD-REQ-002 规则 + few-shot，无训练 | ADD-DP-002 / DEC-001 | TDD-TEST-004 |
| URD-REQ-003 原生概率 | ADD-DP-004 / DEC-001 | TDD-TEST-003 |
| URD-REQ-004 测试与示例分离、匿名 | ADD-DP-001 / DEC-002 / DEC-003 | TDD-TEST-001 / TDD-NEG-002 |
| URD-REQ-005 保留不确定性 | DEC-006 | TDD-TEST-002 |
| URD-CON-001 记录模型版本 | ADD-DP-006 | TDD-TEST-007 |
| URD-CON-002 Secret 不入库 | ADD-DP-005 | TDD-TEST-005 / TDD-NEG-001 |
| URD-CON-004 可复跑 | ADD-DP-006 | TDD-TEST-007 |

## 2. Planned Artifacts

| Artifact | Role |
|---|---|
| `experiments/jev-rule-fewshot-pilot/fixtures.json` | few-shot + 5 个 held-out 测试夹具，gold 与 packet 分离 |
| `experiments/jev-rule-fewshot-pilot/run_pilot.py` | 构造 Jev requests、检查泄漏、保存原生概率、评分 |
| `.github/workflows/jev-rule-fewshot-pilot.yml` | 通过 API_KEYS Environment 运行 pilot |
| Actions artifact `jev-rule-fewshot-results` | 单次 run 的 `results.json` |
| `docs/jev-rule-fewshot-pilot/RESULTS-v0.1.md` | 实际 run 后的人类可读结果 |

## 3. Build Order

```text
URD / ADD / TDD
  -> fixtures
  -> runner
  -> workflow
  -> run
  -> inspect results
  -> RESULTS-v0.1
  -> root TRACE / CHANGELOG / OKF minimal update
```

## 4. Stop Conditions

- target state 出现 gold 或真实药名；
- Jev response schema 与预期不符；
- secret 在日志或仓库中明文出现；
- 5 个样本未全部完成；
- prompt 在同一次评分中途发生变化。

发生任一情况，本次 run 标记 invalid，不报告准确率。

## 5. 下一阶段触发条件

只有在本 pilot 管道完整、结果可解析且未发生泄漏后，才考虑：

1. 用完整 Research Dossier 替换药典去标签 packet；
2. 扩大到独立 calibration set；
3. 决定人工复核阈值；
4. 再讨论是否接入正式 Materia mapping / Claim Ledger。
