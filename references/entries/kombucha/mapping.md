# Mapping｜kombucha

> 分类为 Jev v0.4 原生输出；M 是其后根据 research.md 独立评注。分数不是校准概率或证据等级。

## Run metadata

```yaml
entry_id: kombucha
research_ref: references/entries/kombucha/research.md
summary_ref: references/entries/kombucha/summary.md
summary_sha256: 9b0165c1419b59dec9df01718a0fb9574c603a4d020271833deba66d0d871c5f
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T07:09:10.805551+00:00
native_result_ref: qa/jev-ten-batch/raw/kombucha.json
```

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.01 | M-0 |
| 平 | 0.99 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**。资料未支持把模型强制选出的平当作已证实的本草平性。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.13 | M-IV | 发酵酸味可能存在，残糖和发酵程度变化大。 |
| 苦 | 0.08 | M-0 | 没有足够可追溯的本草映射依据。 |
| 甘 | 0.13 | M-0 | 没有足够可追溯的本草映射依据。 |
| 辛 | 0.06 | M-0 | 没有足够可追溯的本草映射依据。 |
| 咸 | 0.04 | M-0 | 没有足够可追溯的本草映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | Choice | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---|
| 心 | 0.05 | 阳- | 0.29 | 0.05 | 0.55 | 0.11 | M-0 |
| 肝 | 0.06 | 阴- | 0.49 | 0.03 | 0.42 | 0.06 | M-0 |
| 脾 | 0.09 | 阴- | 0.63 | 0.03 | 0.09 | 0.25 | M-0 |
| 肺 | 0.06 | 阴- | 0.45 | 0.13 | 0.38 | 0.04 | M-0 |
| 肾 | 0.06 | 阴- | 0.65 | 0.09 | 0.19 | 0.07 | M-0 |

各经方向的原生分布均已保存；低归经分数的方向不进入读者层。0.5 只作展示线，不是 M 或证据门槛。

## M 注释与写作交接

- 四气：资料未支持把模型强制选出的平当作已证实的本草平性。
- 反证与替代解释：产品配方、加工、剂量、人群、对照与传统母本身份的差异，详见 research.md 和 summary.md。模型方向或感官相似不能补上临床证候证据。
- 正文最大表述强度：小试验是线索，不写治疗糖尿病或稳定改善菌群。
- 派生传统用词：本批次不自动接受；需同时具备归经、方向和语境，并符合 M 强度。
