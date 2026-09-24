# Mapping｜pickled-cucumber

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 15-fermented-foods-and-avocado
entry_id: pickled-cucumber
research_ref: references/entries/pickled-cucumber/research.md
summary_ref: references/entries/pickled-cucumber/summary.md
summary_sha256: ec5e4b8c93045134d77e17be4f7ce95d8415031a4895b09a8dbcff2ed49679b4
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T15:14:22.065668+00:00
workflow_run_id: 36019837801
workflow_artifact_id: 10816226594
native_result_ref: qa/jev-entry-batches/15-fermented-foods-and-avocado/raw/pickled-cucumber.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.02 | M-0 |
| 凉 | 0.07 | M-0 |
| 平 | 0.91 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.89）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.54 | M-IV | 酸味可由乳酸发酵或外加醋酸形成。 |
| 苦 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.34 | M-IV | 盐水和品牌配方决定钠与咸度。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阴- | 0.29 | 0.47 | 0.06 | 0.35 | 0.12 | M-0 |
| 肝 | 0.06 | 阴- | 0.39 | 0.54 | 0.05 | 0.38 | 0.03 | M-0 |
| 脾 | 0.12 | 阴- | 0.67 | 0.76 | 0.02 | 0.03 | 0.19 | M-0 |
| 肺 | 0.06 | 阴- | 0.51 | 0.64 | 0.10 | 0.22 | 0.04 | M-0 |
| 肾 | 0.06 | 阴- | 0.78 | 0.83 | 0.06 | 0.07 | 0.04 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：普通酸黄瓜的人体健康结局证据不足（E-0）。腌菜/L. brevis试验为D2（n=44、30 g/day、2周、非黄瓜特异），部分结果在灭活菌组出现；不构成本条临床功效证据。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
