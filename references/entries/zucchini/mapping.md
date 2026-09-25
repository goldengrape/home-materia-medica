# Mapping｜zucchini

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 17-modern-fruits-and-vegetables
entry_id: zucchini
research_ref: references/entries/zucchini/research.md
summary_ref: references/entries/zucchini/summary.md
summary_sha256: 8909d394c1d7c4c03b64b4a627c3cec5b1685e13341a6d68078184b9af8a8ef3
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T05:57:25.801128+00:00
workflow_run_id: 36100718549
workflow_artifact_id: 10849536041
native_result_ref: qa/jev-entry-batches/17-modern-fruits-and-vegetables/raw/zucchini.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.01 | M-0 |
| 凉 | 0.02 | M-0 |
| 平 | 0.97 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.96）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.10 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.23 | M-IV | 西葫芦通常味淡，嫩果可略带清甜；品种和成熟度影响感官，只作食味记录。 |
| 辛 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阴- | 0.31 | 0.48 | 0.13 | 0.31 | 0.08 | M-0 |
| 肝 | 0.06 | 阴- | 0.63 | 0.73 | 0.04 | 0.20 | 0.03 | M-0 |
| 脾 | 0.10 | 阴- | 0.73 | 0.80 | 0.07 | 0.01 | 0.12 | M-0 |
| 肺 | 0.06 | 阴- | 0.55 | 0.66 | 0.25 | 0.06 | 0.03 | M-0 |
| 肾 | 0.06 | 阴- | 0.76 | 0.82 | 0.13 | 0.03 | 0.02 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：西葫芦整果的人体健康结局证据不足（E-0）；强烈异常苦味对应的葫芦素风险有官方食品安全说明。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
