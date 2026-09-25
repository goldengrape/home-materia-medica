# Mapping｜arugula

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 17-modern-fruits-and-vegetables
entry_id: arugula
research_ref: references/entries/arugula/research.md
summary_ref: references/entries/arugula/summary.md
summary_sha256: fad1e290f28ea11997a1af76c92b4daacc0f3cbc0b3bf1c0582fabfdd2386e6a
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T05:57:24.774199+00:00
workflow_run_id: 36100718549
workflow_artifact_id: 10849536041
native_result_ref: qa/jev-entry-batches/17-modern-fruits-and-vegetables/raw/arugula.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.03 | M-0 |
| 凉 | 0.11 | M-0 |
| 平 | 0.86 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.82）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.12 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.10 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.13 | M-IV | 芝麻菜叶片常有辛香或胡椒样感官特征；本条只把它记为食味，不推为传统药味。 |
| 咸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.08 | 阳- | 0.63 | 0.08 | 0.07 | 0.72 | 0.13 | M-0 |
| 肝 | 0.08 | 阳- | 0.45 | 0.32 | 0.05 | 0.59 | 0.04 | M-0 |
| 脾 | 0.07 | 阴- | 0.32 | 0.49 | 0.12 | 0.16 | 0.23 | M-0 |
| 肺 | 0.07 | 阳- | 0.22 | 0.32 | 0.21 | 0.41 | 0.06 | M-0 |
| 肾 | 0.07 | 阴- | 0.36 | 0.51 | 0.07 | 0.35 | 0.07 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：芝麻菜有一项小型急性交叉研究，干预为硝酸盐定量饮品、观察时间为5小时（E-D）；对日常鲜叶份量和长期疾病结局的证据不足。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
