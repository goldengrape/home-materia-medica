# Mapping｜cheese-tea

> Jev v0.4 是模型分类倾向；M 是随后根据 Research Dossier 所做的独立证据评注。分数不是校准概率，M 也不修正分数。

## Run metadata

```yaml
entry_id: cheese-tea
research_ref: references/entries/cheese-tea/research.md
summary_ref: references/entries/cheese-tea/summary.md
summary_sha256: c735631df206eac06927a67439c5b49c9d1182af8cb8a24a0995058bf2c9e47e
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T08:12:58.420844+00:00
workflow_run_id: 35973926000
workflow_artifact_id: 10797147988
native_result_ref: qa/jev-tea-batch/raw/cheese-tea.json
```

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.38 | M-0 |
| 凉 | 0.10 | M-0 |
| 平 | 0.52 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.40）。茶叶母本或相似饮品不能自动确定复合成品的四气。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.07 | M-0 | 没有足够可追溯的本草映射依据。 |
| 苦 | 0.51 | M-IV | 茶底可有苦涩，感官类推不等于临床功效。 |
| 甘 | 0.37 | M-IV | 奶盖或茶底可能加糖，含量依配方。 |
| 辛 | 0.08 | M-0 | 没有足够可追溯的本草映射依据。 |
| 咸 | 0.15 | M-IV | 部分芝士/咸奶盖可有咸感；配方并不统一。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.07 | 阳- | 0.77 | 0.09 | 0.03 | 0.83 | 0.05 | M-0 |
| 肝 | 0.08 | 阳- | 0.72 | 0.18 | 0.01 | 0.79 | 0.02 | M-0 |
| 脾 | 0.10 | 阴- | 0.39 | 0.54 | 0.10 | 0.23 | 0.13 | M-0 |
| 肺 | 0.17 | 阳- | 0.82 | 0.11 | 0.02 | 0.86 | 0.01 | M-0 |
| 肾 | 0.06 | 阳- | 0.24 | 0.41 | 0.11 | 0.43 | 0.05 | M-0 |

最高归经 Noul 为 0.17；所有原生归经和方向结果均保留。五脏方向 Choice 是 Jev 对各经的原生回答，不代表已确认归经；本条无直接证候或传统归经桥梁，因此 M-0。项目的 0.5 只作为读者层展示线，不作为隐藏 Jev 原始输出或提升 M 的门槛。

## M 注释与写作交接

- 四气：茶叶母本或相似饮品不能自动确定复合成品的四气。
- 五味：M-IV 仅在有明确配方/感官描述时表示感官类推，不表示传统功效；其他味 M-0。
- 归经与方向：全部 M-0；模型倾向分数和方向分布保留，但不把低分强制 Choice 转成正文归经。
- 反证与替代解释：配方、加工、糖/乳/植物饮、茶种、粉量、人群与研究终点差异见 research.md、summary.md。
- 正文最大表述强度：动物实验只作 E-D 信号；不推成人体血糖或糖尿病因果结论。
- 原生 JSON 未添加 M、未改写分数；全部 API 原始字段与 usage 见 native_result_ref。
