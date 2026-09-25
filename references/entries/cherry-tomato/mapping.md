# Mapping｜cherry-tomato

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 17-modern-fruits-and-vegetables
entry_id: cherry-tomato
research_ref: references/entries/cherry-tomato/research.md
summary_ref: references/entries/cherry-tomato/summary.md
summary_sha256: 21f1fe318eef24f07aa4344f9e2dd2aee563f1327d557273bc7c060637b7f835
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T05:57:25.617314+00:00
workflow_run_id: 36100718549
workflow_artifact_id: 10849536041
native_result_ref: qa/jev-entry-batches/17-modern-fruits-and-vegetables/raw/cherry-tomato.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.02 | M-0 |
| 凉 | 0.14 | M-0 |
| 平 | 0.84 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.80）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.16 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.26 | M-IV | 成熟樱桃番茄通常有甜味并伴酸味，品种和成熟度影响平衡；只记录食味。 |
| 辛 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.06 | 阳- | 0.28 | 0.16 | 0.33 | 0.47 | 0.04 | M-0 |
| 肝 | 0.07 | 阳- | 0.34 | 0.28 | 0.19 | 0.51 | 0.02 | M-0 |
| 脾 | 0.09 | 阴+ | 0.23 | 0.29 | 0.43 | 0.16 | 0.12 | M-0 |
| 肺 | 0.07 | 阴+ | 0.37 | 0.18 | 0.53 | 0.28 | 0.01 | M-0 |
| 肾 | 0.06 | 阴+ | 0.26 | 0.33 | 0.45 | 0.20 | 0.02 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：樱桃番茄单品的人体健康结局证据不足（E-0至E-C）；现有番茄膳食试验包含多种品种和加工形态，不能单独归因。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
