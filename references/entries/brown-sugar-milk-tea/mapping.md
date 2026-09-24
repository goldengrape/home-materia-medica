# Mapping｜brown-sugar-milk-tea

> Jev v0.4 是模型分类倾向；M 是随后根据 Research Dossier 所做的独立证据评注。分数不是校准概率，M 也不修正分数。

## Run metadata

```yaml
entry_id: brown-sugar-milk-tea
research_ref: references/entries/brown-sugar-milk-tea/research.md
summary_ref: references/entries/brown-sugar-milk-tea/summary.md
summary_sha256: 84901692201872fcb5f6062cac0ebe3ffbb9fbd29acd50fdf4e367564c473870
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T08:12:59.755021+00:00
workflow_run_id: 35973926000
workflow_artifact_id: 10797147988
native_result_ref: qa/jev-tea-batch/raw/brown-sugar-milk-tea.json
```

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.14 | M-0 |
| 凉 | 0.03 | M-0 |
| 平 | 0.80 | M-0 |
| 温 | 0.02 | M-0 |
| 热 | 0.01 | M-0 |

Jev Choice：**平**（Choice confidence 0.75）。茶叶母本或相似饮品不能自动确定复合成品的四气。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.06 | M-0 | 没有足够可追溯的本草映射依据。 |
| 苦 | 0.37 | M-IV | 茶底可有苦涩，随配方浓度而变。 |
| 甘 | 0.46 | M-IV | 黑糖/糖浆带来甜感，但品名不能量化整杯糖暴露。 |
| 辛 | 0.09 | M-0 | 没有足够可追溯的本草映射依据。 |
| 咸 | 0.04 | M-0 | 没有足够可追溯的本草映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.08 | 阳- | 0.65 | 0.08 | 0.06 | 0.73 | 0.13 | M-0 |
| 肝 | 0.06 | 阳- | 0.60 | 0.22 | 0.02 | 0.70 | 0.06 | M-0 |
| 脾 | 0.10 | 阳+ | 0.22 | 0.25 | 0.17 | 0.16 | 0.42 | M-0 |
| 肺 | 0.15 | 阳- | 0.81 | 0.09 | 0.03 | 0.86 | 0.02 | M-0 |
| 肾 | 0.06 | 阴- | 0.14 | 0.36 | 0.15 | 0.29 | 0.20 | M-0 |

最高归经 Noul 为 0.15；所有原生归经和方向结果均保留。五脏方向 Choice 是 Jev 对各经的原生回答，不代表已确认归经；本条无直接证候或传统归经桥梁，因此 M-0。项目的 0.5 只作为读者层展示线，不作为隐藏 Jev 原始输出或提升 M 的门槛。

## M 注释与写作交接

- 四气：茶叶母本或相似饮品不能自动确定复合成品的四气。
- 五味：M-IV 仅在有明确配方/感官描述时表示感官类推，不表示传统功效；其他味 M-0。
- 归经与方向：全部 M-0；模型倾向分数和方向分布保留，但不把低分强制 Choice 转成正文归经。
- 反证与替代解释：配方、加工、糖/乳/植物饮、茶种、粉量、人群与研究终点差异见 research.md、summary.md。
- 正文最大表述强度：写实际糖、杯量与基底变量；不写黑糖的未经验证健康优势。
- 原生 JSON 未添加 M、未改写分数；全部 API 原始字段与 usage 见 native_result_ref。
