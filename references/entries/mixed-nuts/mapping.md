# Mapping｜mixed-nuts

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 11-tree-nut-snacks
entry_id: mixed-nuts
research_ref: references/entries/mixed-nuts/research.md
summary_ref: references/entries/mixed-nuts/summary.md
summary_sha256: 833fba4e957800455caf1cd79461da7e429a804d77d9c0e9fcfc2ff9a5140e42
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T12:58:21.087771+00:00
workflow_run_id: 36003283893
workflow_artifact_id: 10809600316
native_result_ref: qa/jev-entry-batches/11-tree-nut-snacks/raw/mixed-nuts.json

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
| 苦 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.16 | M-IV | 混合坚果整体有多种坚果香与油脂感；果干、糖衣或盐焗会显著改变甜咸味。 |
| 辛 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.09 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.05 | 阳+ | 0.05 | 0.21 | 0.27 | 0.24 | 0.28 | M-0 |
| 肝 | 0.05 | 阴+ | 0.13 | 0.24 | 0.35 | 0.27 | 0.14 | M-0 |
| 脾 | 0.08 | 阳+ | 0.34 | 0.28 | 0.19 | 0.03 | 0.50 | M-0 |
| 肺 | 0.05 | 阴+ | 0.19 | 0.39 | 0.39 | 0.12 | 0.10 | M-0 |
| 肾 | 0.06 | 阴+ | 0.37 | 0.27 | 0.54 | 0.06 | 0.13 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：两项研究均为 D0（固定混合坚果配方）短期替代性干预，人数分别 48 与 29；血脂结果多为阴性，观察到的代理指标变化不等于临床事件，不能外推至所有零售混合包或额外加食（E-C）。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
