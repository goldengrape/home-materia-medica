# Mapping｜chiffon-cake

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 08-cakes-frozen-desserts
entry_id: chiffon-cake
research_ref: references/entries/chiffon-cake/research.md
summary_ref: references/entries/chiffon-cake/summary.md
summary_sha256: 7f1795b6d88b680c2ef00ec5fff4364adda2f4310faca825c306982aaf365d23
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T11:33:55.450243+00:00
workflow_run_id: 35993741889
workflow_artifact_id: 10804164780
native_result_ref: qa/jev-entry-batches/08-cakes-frozen-desserts/raw/chiffon-cake.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 1.00 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.99）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.09 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.32 | M-IV | 通常加入糖，甜度会被可可、茶、奶油或果味夹馅改变。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳+ | 0.13 | 0.21 | 0.09 | 0.35 | 0.35 | M-0 |
| 肝 | 0.04 | 阳- | 0.28 | 0.38 | 0.04 | 0.45 | 0.13 | M-0 |
| 脾 | 0.06 | 阳+ | 0.35 | 0.36 | 0.08 | 0.05 | 0.51 | M-0 |
| 肺 | 0.04 | 阴- | 0.27 | 0.45 | 0.15 | 0.26 | 0.14 | M-0 |
| 肾 | 0.03 | 阴- | 0.34 | 0.50 | 0.19 | 0.16 | 0.15 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：可可戚风研究为 D1（单一配方组的实验室营养与感官比较）；其感官面板不等同于临床人体试验，目标成品长期健康结局证据未建立（E-0）。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
