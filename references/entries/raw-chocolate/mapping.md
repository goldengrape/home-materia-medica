# Mapping｜raw-chocolate

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 06-nuts-cocoa-chocolate
entry_id: raw-chocolate
research_ref: references/entries/raw-chocolate/research.md
summary_ref: references/entries/raw-chocolate/summary.md
summary_sha256: 3d46ea0774ad5ef1a84570d90e152f7b0f0a9b364ef2779c700fa133455797ae
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T10:44:21.648558+00:00
workflow_run_id: 35988940964
workflow_artifact_id: 10803037445
native_result_ref: qa/jev-entry-batches/06-nuts-cocoa-chocolate/raw/raw-chocolate.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.98 | M-0 |
| 温 | 0.01 | M-0 |
| 热 | 0.01 | M-0 |

Jev Choice：**平**（Choice confidence 0.97）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.16 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.49 | M-IV | 巧克力与鲜奶油配方通常带明显甜味和奶香，按产品而异，仅作感官描述。 |
| 辛 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.05 | 阴+ | 0.27 | 0.15 | 0.45 | 0.18 | 0.22 | M-0 |
| 肝 | 0.05 | 阴- | 0.11 | 0.33 | 0.23 | 0.33 | 0.11 | M-0 |
| 脾 | 0.07 | 阴+ | 0.41 | 0.28 | 0.55 | 0.03 | 0.14 | M-0 |
| 肺 | 0.04 | 阴+ | 0.37 | 0.31 | 0.53 | 0.10 | 0.06 | M-0 |
| 肾 | 0.05 | 阴+ | 0.41 | 0.30 | 0.55 | 0.07 | 0.08 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：未找到日式生巧克力成品的临床功效试验。可可粉或黑巧克力研究不能直接转给含奶油、糖和水分的冷藏甜品。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
