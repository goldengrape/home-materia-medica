# Mapping｜fried-chicken-burger

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 25-fish-tofu-meals
entry_id: fried-chicken-burger
research_ref: references/entries/fried-chicken-burger/research.md
summary_ref: references/entries/fried-chicken-burger/summary.md
summary_sha256: f81b5d597843f34001adda05af76f43e2ad668cfeb58c3fdc23879bd609a3e8d
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T07:43:02.006480+00:00
workflow_run_id: 36109049026
workflow_artifact_id: 10852585965
native_result_ref: qa/jev-entry-batches/25-fish-tofu-meals/raw/fried-chicken-burger.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.97 | M-0 |
| 温 | 0.01 | M-0 |
| 热 | 0.02 | M-0 |

Jev Choice：**平**（Choice confidence 0.96）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.09 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.18 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳+ | 0.32 | 0.24 | 0.02 | 0.25 | 0.49 | M-0 |
| 肝 | 0.04 | 阴- | 0.17 | 0.38 | 0.02 | 0.34 | 0.26 | M-0 |
| 脾 | 0.07 | 阳+ | 0.35 | 0.42 | 0.01 | 0.06 | 0.51 | M-0 |
| 肺 | 0.04 | 阴- | 0.29 | 0.47 | 0.04 | 0.25 | 0.24 | M-0 |
| 肾 | 0.03 | 阴- | 0.34 | 0.50 | 0.04 | 0.11 | 0.35 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：证据来自商品成分分析、短期随机试验、连锁菜单调查或全国饮食调查；研究设计、样本和食品类别限制按原研究保留。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
