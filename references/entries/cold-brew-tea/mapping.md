# Mapping｜cold-brew-tea

> Jev v0.4 是模型分类倾向；M 是随后根据 Research Dossier 所做的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

```yaml
entry_id: cold-brew-tea
research_ref: references/entries/cold-brew-tea/research.md
summary_ref: references/entries/cold-brew-tea/summary.md
summary_sha256: fc79e81156fb59d28e57f3d63abadd1f8fd2aa3ad2d79033dbf2970b7de9c467
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T08:46:39.798769+00:00
workflow_run_id: 35977224331
workflow_artifact_id: 10798164414
native_result_ref: qa/jev-tea-coffee-batch/raw/cold-brew-tea.json
```

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.01 | M-0 |
| 凉 | 0.04 | M-0 |
| 平 | 0.95 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.94）。模型必须选择一项，但共享母页、感官或饮用温度不足以证明本条成品四气。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.06 | M-0 | 没有稳定、可追溯到本条整体的映射依据。 |
| 苦 | 0.20 | M-IV | 冷泡茶感官苦味随茶种与浸泡条件变化，仅作感官类推。 |
| 甘 | 0.10 | M-0 | 没有稳定、可追溯到本条整体的映射依据。 |
| 辛 | 0.09 | M-0 | 没有稳定、可追溯到本条整体的映射依据。 |
| 咸 | 0.04 | M-0 | 没有稳定、可追溯到本条整体的映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.06 | 阳- | 0.59 | 0.19 | 0.06 | 0.70 | 0.05 | M-0 |
| 肝 | 0.06 | 阳- | 0.58 | 0.27 | 0.02 | 0.69 | 0.02 | M-0 |
| 脾 | 0.06 | 阴- | 0.45 | 0.59 | 0.08 | 0.18 | 0.15 | M-0 |
| 肺 | 0.08 | 阳- | 0.29 | 0.29 | 0.22 | 0.47 | 0.02 | M-0 |
| 肾 | 0.05 | 阴- | 0.36 | 0.52 | 0.12 | 0.33 | 0.03 | M-0 |

最高归经 Noul 及全部方向概率均保留；项目 0.5 只作读者层展示线，不隐藏原生输出，也不提高 M。方向 Choice 是模型回答，不表示已确认归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不等于已确证传统属性，制法/温度/配方不可自动替代证据。
- 五味：只有 dossier 明确记录感官依据的味作 M-IV 类推；不把感官推成传统功效。
- 五脏归经及方向：全部 M-0；本轮未建立可核验的直接桥梁。
- 证据距离：Song 等的实验比较了冷泡茶工艺、微生物指标与储存，并非消费者健康试验。高压处理所得货架期不能代表普通家庭自制冷泡茶。
- 正文最大表述强度：保留样品、设计、剂量或工艺限制，不写成已证实的临床防病/治疗效果。
- 原生 JSON 未添加 M、未改写分数；全部 native answers 与 usage 均保留在 `native_result_ref`。
