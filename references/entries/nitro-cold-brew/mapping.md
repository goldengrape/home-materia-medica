# Mapping｜nitro-cold-brew

> Jev v0.4 是模型分类倾向；M 是随后根据 Research Dossier 所做的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

```yaml
entry_id: nitro-cold-brew
research_ref: references/entries/nitro-cold-brew/research.md
summary_ref: references/entries/nitro-cold-brew/summary.md
summary_sha256: 8c475b9afc6e8207f562329ce07a075006f70616edacce73ebeed676ea27c2f3
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T08:46:42.411338+00:00
workflow_run_id: 35977224331
workflow_artifact_id: 10798164414
native_result_ref: qa/jev-tea-coffee-batch/raw/nitro-cold-brew.json
```

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.01 | M-0 |
| 平 | 0.98 | M-0 |
| 温 | 0.01 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.97）。模型必须选择一项，但共享母页、感官或饮用温度不足以证明本条成品四气。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.05 | M-0 | 没有稳定、可追溯到本条整体的映射依据。 |
| 苦 | 0.18 | M-IV | 咖啡基底可呈苦，氮气改变质地但不固定甜味，仅作感官类推。 |
| 甘 | 0.07 | M-0 | 没有稳定、可追溯到本条整体的映射依据。 |
| 辛 | 0.09 | M-0 | 没有稳定、可追溯到本条整体的映射依据。 |
| 咸 | 0.04 | M-0 | 没有稳定、可追溯到本条整体的映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.11 | 阳+ | 0.58 | 0.07 | 0.01 | 0.23 | 0.69 | M-0 |
| 肝 | 0.05 | 阳- | 0.39 | 0.28 | 0.01 | 0.54 | 0.17 | M-0 |
| 脾 | 0.05 | 阴- | 0.21 | 0.40 | 0.02 | 0.22 | 0.36 | M-0 |
| 肺 | 0.05 | 阳- | 0.20 | 0.30 | 0.03 | 0.40 | 0.27 | M-0 |
| 肾 | 0.05 | 阴- | 0.26 | 0.45 | 0.03 | 0.34 | 0.18 | M-0 |

最高归经 Noul 及全部方向概率均保留；项目 0.5 只作读者层展示线，不隐藏原生输出，也不提高 M。方向 Choice 是模型回答，不表示已确认归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不等于已确证传统属性，制法/温度/配方不可自动替代证据。
- 五味：只有 dossier 明确记录感官依据的味作 M-IV 类推；不把感官推成传统功效。
- 五脏归经及方向：全部 M-0；本轮未建立可核验的直接桥梁。
- 证据距离：目前 R1 找到的氮气冷萃研究关注泡沫、制备和产品微生物特征，没有验证直接人体临床结局。
- 正文最大表述强度：保留样品、设计、剂量或工艺限制，不写成已证实的临床防病/治疗效果。
- 原生 JSON 未添加 M、未改写分数；全部 native answers 与 usage 均保留在 `native_result_ref`。
