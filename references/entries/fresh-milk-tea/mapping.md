# Mapping｜fresh-milk-tea

> Jev v0.4 是模型分类倾向；M 是随后根据 Research Dossier 所做的独立证据评注。分数不是校准概率，M 也不修正分数。

## Run metadata

```yaml
entry_id: fresh-milk-tea
research_ref: references/entries/fresh-milk-tea/research.md
summary_ref: references/entries/fresh-milk-tea/summary.md
summary_sha256: 9cdbd5a5737747435b72751fc41fa24370964e1b032f399bfe30694b6a05bc52
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T08:12:57.083424+00:00
workflow_run_id: 35973926000
workflow_artifact_id: 10797147988
native_result_ref: qa/jev-tea-batch/raw/fresh-milk-tea.json
```

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.26 | M-0 |
| 凉 | 0.06 | M-0 |
| 平 | 0.67 | M-0 |
| 温 | 0.01 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.59）。茶叶母本或相似饮品不能自动确定复合成品的四气。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.07 | M-0 | 没有足够可追溯的本草映射依据。 |
| 苦 | 0.47 | M-IV | 茶底可有苦涩；只是感官类推，不证明整杯具有传统苦味功效。 |
| 甘 | 0.35 | M-IV | 牛乳和可选糖可带来甜感；鲜奶比例与加糖因店而异。 |
| 辛 | 0.08 | M-0 | 没有足够可追溯的本草映射依据。 |
| 咸 | 0.05 | M-0 | 没有足够可追溯的本草映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.09 | 阳- | 0.68 | 0.06 | 0.08 | 0.76 | 0.10 | M-0 |
| 肝 | 0.07 | 阳- | 0.72 | 0.17 | 0.02 | 0.79 | 0.02 | M-0 |
| 脾 | 0.11 | 阴- | 0.09 | 0.32 | 0.29 | 0.18 | 0.21 | M-0 |
| 肺 | 0.13 | 阳- | 0.71 | 0.13 | 0.06 | 0.79 | 0.02 | M-0 |
| 肾 | 0.06 | 阳- | 0.23 | 0.32 | 0.20 | 0.42 | 0.06 | M-0 |

最高归经 Noul 为 0.13；所有原生归经和方向结果均保留。五脏方向 Choice 是 Jev 对各经的原生回答，不代表已确认归经；本条无直接证候或传统归经桥梁，因此 M-0。项目的 0.5 只作为读者层展示线，不作为隐藏 Jev 原始输出或提升 M 的门槛。

## M 注释与写作交接

- 四气：茶叶母本或相似饮品不能自动确定复合成品的四气。
- 五味：M-IV 仅在有明确配方/感官描述时表示感官类推，不表示传统功效；其他味 M-0。
- 归经与方向：全部 M-0；模型倾向分数和方向分布保留，但不把低分强制 Choice 转成正文归经。
- 反证与替代解释：配方、加工、糖/乳/植物饮、茶种、粉量、人群与研究终点差异见 research.md、summary.md。
- 正文最大表述强度：限于茶底、鲜奶/奶精身份、糖和咖啡因暴露；不定整杯四气或归经。
- 原生 JSON 未添加 M、未改写分数；全部 API 原始字段与 usage 见 native_result_ref。
