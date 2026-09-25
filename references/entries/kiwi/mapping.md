# Mapping｜kiwi

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 16-berries-and-tropical-fruits
entry_id: kiwi
research_ref: references/entries/kiwi/research.md
summary_ref: references/entries/kiwi/summary.md
summary_sha256: d59226a84fcaabaf51790d2e004c5ffcc9b5aab68fe4e432bc546a51766c5a6c
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T05:31:44.781123+00:00
workflow_run_id: 36098927772
workflow_artifact_id: 10848946258
native_result_ref: qa/jev-entry-batches/16-berries-and-tropical-fruits/raw/kiwi.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.80 | M-0 |
| 凉 | 0.16 | M-0 |
| 平 | 0.04 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**寒**（Choice confidence 0.75）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.86 | M-IV | 猕猴桃常带酸甜味，品种和成熟度对酸度影响明显；只记录感官，不推成传统药味。 |
| 苦 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.86 | M-IV | 成熟猕猴桃有甜味，品种和成熟度会影响甜度；只记录感官，不推成传统药味。 |
| 辛 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.08 | 阴+ | 0.27 | 0.10 | 0.46 | 0.42 | 0.02 | M-0 |
| 肝 | 0.10 | 阳- | 0.42 | 0.16 | 0.26 | 0.56 | 0.02 | M-0 |
| 脾 | 0.56 | 阴- | 0.57 | 0.67 | 0.11 | 0.14 | 0.08 | M-0 |
| 肺 | 0.10 | 阴+ | 0.41 | 0.16 | 0.55 | 0.28 | 0.01 | M-0 |
| 肾 | 0.09 | 阴+ | 0.32 | 0.21 | 0.49 | 0.28 | 0.02 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：每日2枚特定绿肉猕猴桃对便秘人群的排便频率和胃肠舒适度有随机试验证据（E-B至E-C，结局限于4周）。心代谢证据仅6项RCT且多数终点不显著，不能合并为全面健康功效。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
