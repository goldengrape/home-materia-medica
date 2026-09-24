# Mapping｜mocha

> Jev v0.4 是模型分类倾向；M 是随后根据 Research Dossier 所做的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

```yaml
entry_id: mocha
research_ref: references/entries/mocha/research.md
summary_ref: references/entries/mocha/summary.md
summary_sha256: 1f168edc233d586bc85fae8d40d794033fe1ba7bbe458cd4bbdc121f049a6e17
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T08:46:43.562135+00:00
workflow_run_id: 35977224331
workflow_artifact_id: 10798164414
native_result_ref: qa/jev-tea-coffee-batch/raw/mocha.json
```

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.96 | M-0 |
| 温 | 0.03 | M-0 |
| 热 | 0.01 | M-0 |

Jev Choice：**平**（Choice confidence 0.95）。模型必须选择一项，但共享母页、感官或饮用温度不足以证明本条成品四气。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.05 | M-0 | 没有稳定、可追溯到本条整体的映射依据。 |
| 苦 | 0.19 | M-IV | 咖啡/可可可产生苦味，配方影响强度，仅作类推。 |
| 甘 | 0.24 | M-IV | 牛乳、巧克力或糖浆可带来甜味，依产品变化，仅作类推。 |
| 辛 | 0.08 | M-0 | 没有稳定、可追溯到本条整体的映射依据。 |
| 咸 | 0.04 | M-0 | 没有稳定、可追溯到本条整体的映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.09 | 阳+ | 0.64 | 0.07 | 0.01 | 0.19 | 0.73 | M-0 |
| 肝 | 0.05 | 阳- | 0.33 | 0.27 | 0.02 | 0.49 | 0.22 | M-0 |
| 脾 | 0.05 | 阳+ | 0.19 | 0.38 | 0.14 | 0.09 | 0.39 | M-0 |
| 肺 | 0.05 | 阳- | 0.19 | 0.24 | 0.05 | 0.39 | 0.32 | M-0 |
| 肾 | 0.05 | 阴- | 0.17 | 0.37 | 0.08 | 0.25 | 0.30 | M-0 |

最高归经 Noul 及全部方向概率均保留；项目 0.5 只作读者层展示线，不隐藏原生输出，也不提高 M。方向 Choice 是模型回答，不表示已确认归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不等于已确证传统属性，制法/温度/配方不可自动替代证据。
- 五味：只有 dossier 明确记录感官依据的味作 M-IV 类推；不把感官推成传统功效。
- 五脏归经及方向：全部 M-0；本轮未建立可核验的直接桥梁。
- 证据距离：需区分英语 mocha/moka 在部分意大利咖啡研究中指 Moka 壶制法；该研究没有测试本条巧克力咖啡饮品。
- 正文最大表述强度：保留样品、设计、剂量或工艺限制，不写成已证实的临床防病/治疗效果。
- 原生 JSON 未添加 M、未改写分数；全部 native answers 与 usage 均保留在 `native_result_ref`。
