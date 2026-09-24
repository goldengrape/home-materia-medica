# Mapping｜hojicha-latte

> Jev v0.4 是模型分类倾向；M 是随后根据 Research Dossier 所做的独立证据评注。分数不是校准概率，M 也不修正分数。

## Run metadata

```yaml
entry_id: hojicha-latte
research_ref: references/entries/hojicha-latte/research.md
summary_ref: references/entries/hojicha-latte/summary.md
summary_sha256: 8c640a0a1464544b7a0ed81f996b8d8f87ecf03413219cf7d3216590f51a9656
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T08:13:00.622640+00:00
workflow_run_id: 35973926000
workflow_artifact_id: 10797147988
native_result_ref: qa/jev-tea-batch/raw/hojicha-latte.json
```

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.30 | M-0 |
| 凉 | 0.04 | M-0 |
| 平 | 0.60 | M-0 |
| 温 | 0.06 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.50）。茶叶母本或相似饮品不能自动确定复合成品的四气。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.07 | M-0 | 没有足够可追溯的本草映射依据。 |
| 苦 | 0.55 | M-IV | 焙茶底可有苦涩与焙火风味；粉末/浸液和浓度不同。 |
| 甘 | 0.29 | M-IV | 牛乳和可选糖浆可带甜感；配方不固定。 |
| 辛 | 0.08 | M-0 | 没有足够可追溯的本草映射依据。 |
| 咸 | 0.05 | M-0 | 没有足够可追溯的本草映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.07 | 阳- | 0.80 | 0.06 | 0.02 | 0.85 | 0.07 | M-0 |
| 肝 | 0.08 | 阳- | 0.72 | 0.15 | 0.01 | 0.79 | 0.05 | M-0 |
| 脾 | 0.08 | 阴- | 0.13 | 0.34 | 0.06 | 0.28 | 0.32 | M-0 |
| 肺 | 0.10 | 阳- | 0.68 | 0.14 | 0.04 | 0.76 | 0.06 | M-0 |
| 肾 | 0.06 | 阳- | 0.44 | 0.26 | 0.05 | 0.57 | 0.12 | M-0 |

最高归经 Noul 为 0.10；所有原生归经和方向结果均保留。五脏方向 Choice 是 Jev 对各经的原生回答，不代表已确认归经；本条无直接证候或传统归经桥梁，因此 M-0。项目的 0.5 只作为读者层展示线，不作为隐藏 Jev 原始输出或提升 M 的门槛。

## M 注释与写作交接

- 四气：茶叶母本或相似饮品不能自动确定复合成品的四气。
- 五味：M-IV 仅在有明确配方/感官描述时表示感官类推，不表示传统功效；其他味 M-0。
- 归经与方向：全部 M-0；模型倾向分数和方向分布保留，但不把低分强制 Choice 转成正文归经。
- 反证与替代解释：配方、加工、糖/乳/植物饮、茶种、粉量、人群与研究终点差异见 research.md、summary.md。
- 正文最大表述强度：抹茶拿铁试验中的焙茶拿铁是对照饮品；对照组不证明焙茶疗效。
- 原生 JSON 未添加 M、未改写分数；全部 API 原始字段与 usage 见 native_result_ref。
