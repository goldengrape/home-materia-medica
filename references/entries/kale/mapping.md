# Mapping｜kale

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 17-modern-fruits-and-vegetables
entry_id: kale
research_ref: references/entries/kale/research.md
summary_ref: references/entries/kale/summary.md
summary_sha256: 93de403d34ba39b3bd8b009cae31605fe4caecf77ada35df1172d78d0d7aa3d6
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T05:57:24.598248+00:00
workflow_run_id: 36100718549
workflow_artifact_id: 10849536041
native_result_ref: qa/jev-entry-batches/17-modern-fruits-and-vegetables/raw/kale.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.02 | M-0 |
| 凉 | 0.06 | M-0 |
| 平 | 0.92 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.90）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.16 | M-IV | 羽衣甘蓝鲜叶有时带苦味或涩味，品种和成熟度会影响感官；仅记录食味。 |
| 甘 | 0.18 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.11 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.06 | 阳- | 0.19 | 0.30 | 0.23 | 0.40 | 0.07 | M-0 |
| 肝 | 0.10 | 阴- | 0.26 | 0.45 | 0.14 | 0.39 | 0.02 | M-0 |
| 脾 | 0.12 | 阴- | 0.42 | 0.56 | 0.11 | 0.05 | 0.28 | M-0 |
| 肺 | 0.09 | 阴+ | 0.19 | 0.37 | 0.40 | 0.20 | 0.03 | M-0 |
| 肾 | 0.07 | 阴- | 0.42 | 0.56 | 0.28 | 0.12 | 0.04 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：羽衣甘蓝粉食品棒对少数2型糖尿病患者的部分替代指标有一项小型随机试验（E-C）；样本少、退出较多、干预量大，普通鲜叶的长期临床效果仍不明确。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
