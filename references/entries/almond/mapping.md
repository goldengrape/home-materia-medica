# Mapping｜almond

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 10-confections-nuts
entry_id: almond
research_ref: references/entries/almond/research.md
summary_ref: references/entries/almond/summary.md
summary_sha256: 38acc89e6c8331be345490b7e2a5f65bd0afb87a86482482657c07fc8bc49b5e
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T12:07:10.983239+00:00
workflow_run_id: 35998620791
workflow_artifact_id: 10807635500
native_result_ref: qa/jev-entry-batches/10-confections-nuts/raw/almond.json

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
| 苦 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.33 | M-IV | 甜扁桃仁带坚果香与油脂感；烘烤/盐焗改变香气和营养组成。 |
| 辛 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.08 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.05 | 阴+ | 0.18 | 0.23 | 0.38 | 0.16 | 0.23 | M-0 |
| 肝 | 0.06 | 阴+ | 0.29 | 0.31 | 0.47 | 0.11 | 0.11 | M-0 |
| 脾 | 0.10 | 阳+ | 0.23 | 0.21 | 0.35 | 0.02 | 0.42 | M-0 |
| 肺 | 0.07 | 阴+ | 0.52 | 0.27 | 0.64 | 0.05 | 0.04 | M-0 |
| 肾 | 0.07 | 阴+ | 0.47 | 0.28 | 0.61 | 0.04 | 0.07 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：Huang 等随机试验为 D0（甜扁桃仁直接干预），但限定糖尿病风险升高成人、每日2盎司生杏仁及16周；血糖组间结果为阴性，饮食质量为次要指标。传统杏仁母本对巴旦木的直接性不足，映射不继承（E-C；传统 M 暂不映射）。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
