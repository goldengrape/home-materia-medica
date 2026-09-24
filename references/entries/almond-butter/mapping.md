# Mapping｜almond-butter

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 12-seeds-and-butters
entry_id: almond-butter
research_ref: references/entries/almond-butter/research.md
summary_ref: references/entries/almond-butter/summary.md
summary_sha256: b0dced32a271eb5d91df26957f197e61c6369e060794c6e57b37f97d80ce02df
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T13:36:16.069135+00:00
workflow_run_id: 36006762786
workflow_artifact_id: 10810717078
native_result_ref: qa/jev-entry-batches/12-seeds-and-butters/raw/almond-butter.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.99 | M-0 |
| 温 | 0.01 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.98）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.25 | M-IV | 巴旦木酱有坚果香与油润感；烘烤、去皮和添加糖盐改变口味。 |
| 辛 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.10 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.07 | 阴+ | 0.35 | 0.20 | 0.51 | 0.14 | 0.15 | M-0 |
| 肝 | 0.08 | 阴+ | 0.42 | 0.27 | 0.56 | 0.10 | 0.06 | M-0 |
| 脾 | 0.12 | 阴+ | 0.30 | 0.14 | 0.48 | 0.01 | 0.37 | M-0 |
| 肺 | 0.07 | 阴+ | 0.60 | 0.23 | 0.69 | 0.04 | 0.04 | M-0 |
| 肾 | 0.08 | 阴+ | 0.67 | 0.18 | 0.76 | 0.02 | 0.04 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：Spiller 等 38 人、4 周饮食试验含 D0 烘烤杏仁酱组，剂量 100 g/日、背景为心脏健康饮食；各组 LDL 较基线下降，杏仁酱组 TC 未显著变化且人数较少。Mori 等 14 人急性交叉试验含杏仁酱形式（E-C）。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
