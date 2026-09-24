# Mapping｜honey-roasted-nuts

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 11-tree-nut-snacks
entry_id: honey-roasted-nuts
research_ref: references/entries/honey-roasted-nuts/research.md
summary_ref: references/entries/honey-roasted-nuts/summary.md
summary_sha256: b2e5732b3d4c0411994c59c974e832c133bc65b5fecae68f3ec912a52b420bac
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T12:58:20.381553+00:00
workflow_run_id: 36003283893
workflow_artifact_id: 10809600316
native_result_ref: qa/jev-entry-batches/11-tree-nut-snacks/raw/honey-roasted-nuts.json

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
| 甘 | 0.40 | M-IV | 蜂蜜或糖浆涂层增加甜味，烘烤坚果则带坚果香；具体甜度由配方决定。 |
| 辛 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阴+ | 0.26 | 0.16 | 0.44 | 0.17 | 0.23 | M-0 |
| 肝 | 0.05 | 阴- | 0.07 | 0.30 | 0.20 | 0.27 | 0.23 | M-0 |
| 脾 | 0.08 | 阴+ | 0.23 | 0.20 | 0.43 | 0.03 | 0.34 | M-0 |
| 肺 | 0.04 | 阴+ | 0.42 | 0.27 | 0.57 | 0.08 | 0.08 | M-0 |
| 肾 | 0.05 | 阴+ | 0.39 | 0.29 | 0.55 | 0.06 | 0.10 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：蜂蜜涂层树坚果的直接临床证据未建立（E-0）。2014 年花生风味随机试验为 D2（豆科基底且配方不同），不据此推断蜂蜜坚果结局；配料和糖含量应回到具体产品标签。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
