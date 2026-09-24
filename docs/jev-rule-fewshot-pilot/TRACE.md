# Project Map — Jev Pilot

> 当前有效版本：v0.4  
> 本文件只追踪 Jev pilot。

## Requirement → Design → Test

| Requirement | Design | Test |
|---|---|---|
| 自然语言说明文档 | DEC-012 | TDD-001/014 |
| rule + five-shot | DEC-011 | TDD-002/011 |
| 原生 probability / Noul | DEC-001 | TDD-006~010 |
| 匿名 held-out | fixture separation | TDD-003/011 |
| 封闭四气/五味/五脏 | fixed questions | TDD-005~008 |
| 每经阴阳±主方向 | DEC-018 | TDD-008/016/017 |
| 语义级连、计算同步 | DEC-017 | v0.4 runner |
| 五脏功能群投影 | DEC-014 | TDD-015 |
| Jev / M 双轴 | project policy | domain transfer |
| Secret | API_KEYS | TDD-013 |

## 当前权威 artifacts

| Artifact | Role |
|---|---|
| `URD.md` | 当前需求 |
| `ADD.md` | 当前设计 |
| `TDD.md` | 当前测试 |
| `V0.4-YINYANG-VECTOR-DESIGN.md` | v0.4 设计说明 |
| `RESULTS-v0.4.md` | 当前有效结果 |
| `fixtures-v0.4.json` | v0.4 five-shot + held-out |
| `run_pilot_v04.py` | 16-question regression runner |
| `run_domain_transfer_v04.py` | 现代食品迁移 |
| `skills/home-materia-jev-mapping/` | 当前生产 skill |

## 历史

- v0.1：API / secret proof；十二经 schema 不兼容当前项目。
- v0.2：封闭字段正确，但 target 仍为结构化 packet。
- v0.3：narrative first pass，test-contract 有 bug。
- v0.3.1：自然语言 + reasoning rules + five-shot 稳定。
- v0.4 early draft：20 个 direction Noul，后废弃。
- v0.4 current：每经一个阴-/阴+/阳-/阳+主方向 Choice。

## 当前数据流

```text
Research Dossier
→ natural-language description
→ v0.4 reasoning rules + five-shot
→ Jev 16 questions
→ 四气 / 五味 / 五脏归经 / 每经主方向
→ native scores
→ 与 M grade 并列
→ conventional wording
→ Claim Ledger / writing
```

## Valid runs

### 中药

```text
Jev Yin-Yang Vector v0.4 Pilot #7
四气 5/5×3
五味 5/5×3
归经 5/5×3
方向 10/10×3
```

### 现代食品

```text
Jev Food Domain Transfer v0.4 #2
```

主要方向：

- 开心果：脾阳+、肾阳+
- 咖啡：脾阳+
- 酸奶：脾阳+为主、分布较混合
- 黑巧克力 / 方便面：无主归经

## Stop Conditions

- state 泄漏 gold；
- five-shot/test 重合；
- response keys 不是 16 个；
- direction Choice 不是固定四类；
- rules 与 gold 的投影/方向定义不同；
- model version 未记录；
- secret 泄漏。

任一发生则本次 benchmark invalid。
