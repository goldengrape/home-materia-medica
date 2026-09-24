# Mapping｜sugar-coated-nuts

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 11-tree-nut-snacks
entry_id: sugar-coated-nuts
research_ref: references/entries/sugar-coated-nuts/research.md
summary_ref: references/entries/sugar-coated-nuts/summary.md
summary_sha256: 67fb7ed49ed018ea3b6c8b932ca3d4a0dc9c6f9e2da7bf0489e936ba48ca5761
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T12:58:20.566474+00:00
workflow_run_id: 36002836267
workflow_artifact_id: 10808628357
native_result_ref: qa/jev-entry-batches/11-tree-nut-snacks/raw/sugar-coated-nuts.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.98 | M-0 |
| 温 | 0.01 | M-0 |
| 热 | 0.01 | M-0 |

Jev Choice：**平**（Choice confidence 0.97）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.61 | M-IV | 糖衣增加甜味和脆壳口感，坚果种仁本身仍提供油脂香；糖衣厚薄影响实际甜度。 |
| 辛 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳+ | 0.12 | 0.23 | 0.22 | 0.21 | 0.34 | M-0 |
| 肝 | 0.05 | 阴- | 0.17 | 0.38 | 0.15 | 0.25 | 0.22 | M-0 |
| 脾 | 0.09 | 阳+ | 0.17 | 0.34 | 0.26 | 0.03 | 0.37 | M-0 |
| 肺 | 0.04 | 阴- | 0.19 | 0.40 | 0.34 | 0.12 | 0.14 | M-0 |
| 肾 | 0.05 | 阴- | 0.18 | 0.39 | 0.30 | 0.08 | 0.23 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：直接成品临床结局未建立（E-0）。FDC ID 170656 为 D0（一个具体糖衣杏仁营养记录），不是市场代表性抽样或人体干预；不由营养成分单独推导临床结果。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
