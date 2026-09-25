# Mapping｜frozen-dumplings

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 22-prepared-foods-crisps
entry_id: frozen-dumplings
research_ref: references/entries/frozen-dumplings/research.md
summary_ref: references/entries/frozen-dumplings/summary.md
summary_sha256: 66b9d1e634f0382d3e84a1b2793672f8a9774354b7054a984993e185ed234f80
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T07:07:03.176300+00:00
workflow_run_id: 36106030119
workflow_artifact_id: 10850124615
native_result_ref: qa/jev-entry-batches/22-prepared-foods-crisps/raw/frozen-dumplings.json

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
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.16 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.12 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳+ | 0.35 | 0.22 | 0.04 | 0.22 | 0.52 | M-0 |
| 肝 | 0.04 | 阴- | 0.25 | 0.45 | 0.02 | 0.31 | 0.22 | M-0 |
| 脾 | 0.12 | 阳+ | 0.62 | 0.25 | 0.02 | 0.02 | 0.71 | M-0 |
| 肺 | 0.04 | 阴- | 0.26 | 0.44 | 0.06 | 0.10 | 0.40 | M-0 |
| 肾 | 0.04 | 阴- | 0.34 | 0.51 | 0.06 | 0.08 | 0.35 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：资料包括官方商品抽检和10人的住院单餐比较，受商品、样本和烹调方式限制。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
