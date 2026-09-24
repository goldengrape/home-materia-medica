# Mapping｜fruit-tea

> Jev v0.4 是模型分类倾向；M 是随后根据 Research Dossier 所做的独立证据评注。分数不是校准概率，M 也不修正分数。

## Run metadata

```yaml
entry_id: fruit-tea
research_ref: references/entries/fruit-tea/research.md
summary_ref: references/entries/fruit-tea/summary.md
summary_sha256: 3ac047d5d3604ccf95bd22b98738d866540cdd9e889badf5629f64b635f9e813
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T08:12:57.997165+00:00
workflow_run_id: 35973926000
workflow_artifact_id: 10797147988
native_result_ref: qa/jev-tea-batch/raw/fruit-tea.json
```

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.22 | M-0 |
| 凉 | 0.05 | M-0 |
| 平 | 0.73 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.66）。茶叶母本或相似饮品不能自动确定复合成品的四气。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.19 | M-IV | 部分水果/果汁有酸感；不是全品类固定特征。 |
| 苦 | 0.38 | M-IV | 茶底苦涩可能存在，取决于茶类与浓度。 |
| 甘 | 0.40 | M-IV | 水果、果汁或糖浆可带来甜感；总糖因配方而变。 |
| 辛 | 0.08 | M-0 | 没有足够可追溯的本草映射依据。 |
| 咸 | 0.04 | M-0 | 没有足够可追溯的本草映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.06 | 阳- | 0.76 | 0.10 | 0.03 | 0.82 | 0.05 | M-0 |
| 肝 | 0.07 | 阳- | 0.61 | 0.23 | 0.05 | 0.71 | 0.01 | M-0 |
| 脾 | 0.09 | 阴- | 0.38 | 0.53 | 0.10 | 0.24 | 0.13 | M-0 |
| 肺 | 0.13 | 阳- | 0.72 | 0.13 | 0.07 | 0.79 | 0.01 | M-0 |
| 肾 | 0.05 | 阳- | 0.25 | 0.40 | 0.11 | 0.44 | 0.05 | M-0 |

最高归经 Noul 为 0.13；所有原生归经和方向结果均保留。五脏方向 Choice 是 Jev 对各经的原生回答，不代表已确认归经；本条无直接证候或传统归经桥梁，因此 M-0。项目的 0.5 只作为读者层展示线，不作为隐藏 Jev 原始输出或提升 M 的门槛。

## M 注释与写作交接

- 四气：茶叶母本或相似饮品不能自动确定复合成品的四气。
- 五味：M-IV 仅在有明确配方/感官描述时表示感官类推，不表示传统功效；其他味 M-0。
- 归经与方向：全部 M-0；模型倾向分数和方向分布保留，但不把低分强制 Choice 转成正文归经。
- 反证与替代解释：配方、加工、糖/乳/植物饮、茶种、粉量、人群与研究终点差异见 research.md、summary.md。
- 正文最大表述强度：清楚限定被测百香果红茶与芒果绿茶的样本数据；不写整类疾病效果。
- 原生 JSON 未添加 M、未改写分数；全部 API 原始字段与 usage 见 native_result_ref。
