# Mapping｜cocoa-coated-nuts

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 11-tree-nut-snacks
entry_id: cocoa-coated-nuts
research_ref: references/entries/cocoa-coated-nuts/research.md
summary_ref: references/entries/cocoa-coated-nuts/summary.md
summary_sha256: d40cc170b4fd1329476d1b83055443c90178427358e2ab7e78915b783463b40e
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T12:58:20.741041+00:00
workflow_run_id: 36002836267
workflow_artifact_id: 10808628357
native_result_ref: qa/jev-entry-batches/11-tree-nut-snacks/raw/cocoa-coated-nuts.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 1.00 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 1.00）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.09 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.24 | M-IV | 坚果香与可可/巧克力苦甜并存，甜度取决于糖衣和巧克力配方。 |
| 辛 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳- | 0.15 | 0.29 | 0.13 | 0.37 | 0.21 | M-0 |
| 肝 | 0.05 | 阳- | 0.26 | 0.37 | 0.07 | 0.45 | 0.11 | M-0 |
| 脾 | 0.06 | 阴- | 0.24 | 0.43 | 0.09 | 0.06 | 0.42 | M-0 |
| 肺 | 0.04 | 阴- | 0.24 | 0.43 | 0.21 | 0.27 | 0.09 | M-0 |
| 肾 | 0.05 | 阴- | 0.20 | 0.39 | 0.26 | 0.20 | 0.15 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：可可涂层树坚果直接证据未建立（E-0）。Lee 等喂养试验为 D2/D3（杏仁与可可/黑巧克力分开提供或组合），不等同涂层产品；不把成分组合结论改写为可可坚果疗效。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
