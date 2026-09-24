# Mapping｜brazil-nut

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 11-tree-nut-snacks
entry_id: brazil-nut
research_ref: references/entries/brazil-nut/research.md
summary_ref: references/entries/brazil-nut/summary.md
summary_sha256: 83f905c1b5570736f0bc2319c825d6fb8e2d0456a3f26d624f59ac3a21cea087
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T12:58:19.892672+00:00
workflow_run_id: 36002836267
workflow_artifact_id: 10808628357
native_result_ref: qa/jev-entry-batches/11-tree-nut-snacks/raw/brazil-nut.json

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
| 酸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.16 | M-IV | 种仁有坚果香、油脂感和轻甜感；烘烤或盐渍会改变风味。 |
| 辛 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.06 | 阴+ | 0.13 | 0.14 | 0.34 | 0.31 | 0.21 | M-0 |
| 肝 | 0.07 | 阴+ | 0.16 | 0.27 | 0.36 | 0.29 | 0.08 | M-0 |
| 脾 | 0.07 | 阴+ | 0.27 | 0.24 | 0.45 | 0.03 | 0.28 | M-0 |
| 肺 | 0.05 | 阴+ | 0.20 | 0.32 | 0.40 | 0.19 | 0.09 | M-0 |
| 肾 | 0.09 | 阴+ | 0.37 | 0.24 | 0.53 | 0.10 | 0.13 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：随机证据主要显示硒状态/抗氧化标记变化；2022 年荟萃分析未见显著血脂合并效应。10 人急性试验与部分脱脂颗粒试验均受样本、形态和短期代理终点限制；巴西坚果不等同于硒补充剂（E-C）。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
