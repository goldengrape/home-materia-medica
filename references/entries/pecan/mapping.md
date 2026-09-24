# Mapping｜pecan

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 10-confections-nuts
entry_id: pecan
research_ref: references/entries/pecan/research.md
summary_ref: references/entries/pecan/summary.md
summary_sha256: 527a32f1d008bc262f821c18eec24bdaa8c49f7364bef53ab118f3e0ebd295d1
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T12:07:11.326861+00:00
workflow_run_id: 35998620791
workflow_artifact_id: 10807635500
native_result_ref: qa/jev-entry-batches/10-confections-nuts/raw/pecan.json

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
| 酸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.21 | M-IV | 碧根果种仁常带甜香与油脂感；烘烤或加糖调味会改变口味和实际摄入。 |
| 辛 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.09 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.11 | 阳- | 0.13 | 0.13 | 0.24 | 0.35 | 0.28 | M-0 |
| 肝 | 0.08 | 阴+ | 0.20 | 0.22 | 0.40 | 0.24 | 0.14 | M-0 |
| 脾 | 0.10 | 阳+ | 0.18 | 0.31 | 0.25 | 0.06 | 0.38 | M-0 |
| 肺 | 0.05 | 阴+ | 0.38 | 0.24 | 0.55 | 0.10 | 0.11 | M-0 |
| 肾 | 0.08 | 阴+ | 0.44 | 0.22 | 0.58 | 0.09 | 0.11 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：McKay 等研究为 D0（碧根果饮食直接干预），但为26人的4周小型控制喂养试验，限超重/肥胖且中心性脂肪人群，结局为胰岛素抵抗等代理指标。临床疾病结局与额外加食效应未验证（E-C）。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
