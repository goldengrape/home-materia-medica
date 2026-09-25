# Mapping｜grapefruit

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 16-berries-and-tropical-fruits
entry_id: grapefruit
research_ref: references/entries/grapefruit/research.md
summary_ref: references/entries/grapefruit/summary.md
summary_sha256: 491f4b378dd5ff25b21d8b92dca9f10f02e911b91b91abe148a22db2240fa2af
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T05:31:44.151324+00:00
workflow_run_id: 36098927772
workflow_artifact_id: 10848946258
native_result_ref: qa/jev-entry-batches/16-berries-and-tropical-fruits/raw/grapefruit.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.01 | M-0 |
| 凉 | 0.12 | M-0 |
| 平 | 0.87 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.84）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.21 | M-IV | 西柚果肉一般带酸味，品种、成熟度和苦味程度会影响感官记录；不据此推导药性。 |
| 苦 | 0.12 | M-IV | 部分西柚果肉和白色内皮有苦味，随品种和食用部位变化；不据此推导药性。 |
| 甘 | 0.31 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.10 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.06 | 阴+ | 0.14 | 0.23 | 0.36 | 0.31 | 0.10 | M-0 |
| 肝 | 0.09 | 阳- | 0.20 | 0.34 | 0.21 | 0.40 | 0.05 | M-0 |
| 脾 | 0.10 | 阴- | 0.31 | 0.48 | 0.29 | 0.04 | 0.19 | M-0 |
| 肺 | 0.07 | 阴+ | 0.52 | 0.19 | 0.64 | 0.14 | 0.03 | M-0 |
| 肾 | 0.05 | 阴- | 0.29 | 0.47 | 0.38 | 0.11 | 0.04 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：减重效应未显示西柚组相对水组的优势（E-C）。试验是在能量限制饮食中进行，样本为肥胖成人；不能推成西柚具有独立减重作用。药物相互作用是独立安全问题。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
