# Mapping｜macadamia

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 11-tree-nut-snacks
entry_id: macadamia
research_ref: references/entries/macadamia/research.md
summary_ref: references/entries/macadamia/summary.md
summary_sha256: 42dcc47efe733438fb99cd7e21dc7943807ca517414ed1856c2e1c22e05b51b3
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T12:58:19.407960+00:00
workflow_run_id: 36002479730
workflow_artifact_id: 10809010717
native_result_ref: qa/jev-entry-batches/11-tree-nut-snacks/raw/macadamia.json

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
| 甘 | 0.14 | M-IV | 果仁通常有轻甜感与油脂香；烘烤和调味会改变感官表现。 |
| 辛 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳+ | 0.13 | 0.21 | 0.27 | 0.18 | 0.34 | M-0 |
| 肝 | 0.05 | 阴+ | 0.17 | 0.30 | 0.38 | 0.16 | 0.16 | M-0 |
| 脾 | 0.07 | 阴+ | 0.13 | 0.29 | 0.34 | 0.03 | 0.34 | M-0 |
| 肺 | 0.04 | 阴+ | 0.33 | 0.29 | 0.50 | 0.10 | 0.11 | M-0 |
| 肾 | 0.06 | 阴+ | 0.35 | 0.29 | 0.51 | 0.08 | 0.12 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：Jones 等为 D0（夏威夷果直接摄入）随机交叉试验，限 35 名腹部肥胖成人、约 15% 能量、每阶段 8 周；主要体重与血糖结局组间无显著差异，血脂变化未显著。长期疾病结局未验证（E-C）。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
