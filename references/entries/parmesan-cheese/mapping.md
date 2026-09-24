# Mapping｜parmesan-cheese

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 14-fermented-dairy-cheese
entry_id: parmesan-cheese
research_ref: references/entries/parmesan-cheese/research.md
summary_ref: references/entries/parmesan-cheese/summary.md
summary_sha256: 0c63a5fa2cee7bf1dfb3c4682c447db34c2b269bb56d36e5dbff760aa0156e78
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T14:42:56.597747+00:00
workflow_run_id: 36014763775
workflow_artifact_id: 10813364495
native_result_ref: qa/jev-entry-batches/14-fermented-dairy-cheese/raw/parmesan-cheese.json

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
| 苦 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.13 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.26 | M-IV | 咸、鲜与熟成香随熟成、产区和份量不同，仅为感官描述。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.08 | 阳- | 0.41 | 0.12 | 0.07 | 0.56 | 0.25 | M-0 |
| 肝 | 0.05 | 阳- | 0.30 | 0.33 | 0.04 | 0.48 | 0.15 | M-0 |
| 脾 | 0.08 | 阳+ | 0.22 | 0.38 | 0.15 | 0.05 | 0.42 | M-0 |
| 肺 | 0.05 | 阴- | 0.29 | 0.47 | 0.21 | 0.16 | 0.16 | M-0 |
| 肾 | 0.07 | 阴- | 0.23 | 0.42 | 0.20 | 0.23 | 0.15 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：帕玛森本品直接人体结局未检得（E-0）。Grana Padano小型交叉先导试验为近邻熟成硬质奶酪证据（D1；n=30、30 g/d、2月期），不得改写成帕玛森试验或通用降压功效。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
