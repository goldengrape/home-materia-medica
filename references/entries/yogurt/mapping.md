# Mapping｜yogurt

> 分类为 Jev v0.4 原生输出；M 是其后根据 research.md 独立评注。分数不是校准概率或证据等级。

## Run metadata

```yaml
entry_id: yogurt
research_ref: references/entries/yogurt/research.md
summary_ref: references/entries/yogurt/summary.md
summary_sha256: 9814c02e7e4e01f4e9bd7a60c3a3dfa0d8b4a07d71f894e5411a06eb455f64d1
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T07:09:09.026744+00:00
native_result_ref: qa/jev-ten-batch/raw/yogurt.json
```

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.01 | M-0 |
| 凉 | 0.07 | M-0 |
| 平 | 0.92 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**。资料未支持把模型强制选出的平当作已证实的本草平性。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.40 | M-IV | 发酵酸味及传统酪的近似记载，食品身份不完全相同。 |
| 苦 | 0.07 | M-0 | 没有足够可追溯的本草映射依据。 |
| 甘 | 0.40 | M-IV | 牛乳母本与原味酸奶口感类比。 |
| 辛 | 0.06 | M-0 | 没有足够可追溯的本草映射依据。 |
| 咸 | 0.06 | M-0 | 没有足够可追溯的本草映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | Choice | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---|
| 心 | 0.12 | 阴+ | 0.21 | 0.37 | 0.20 | 0.22 | M-0 |
| 肝 | 0.06 | 阴- | 0.51 | 0.12 | 0.24 | 0.13 | M-0 |
| 脾 | 0.36 | 阳+ | 0.42 | 0.13 | 0.01 | 0.44 | M-0 |
| 肺 | 0.06 | 阴+ | 0.41 | 0.44 | 0.06 | 0.09 | M-0 |
| 肾 | 0.07 | 阴+ | 0.38 | 0.52 | 0.02 | 0.08 | M-0 |

各经方向的原生分布均已保存；低归经分数的方向不进入读者层。0.5 只作展示线，不是 M 或证据门槛。

## M 注释与写作交接

- 四气：资料未支持把模型强制选出的平当作已证实的本草平性。
- 反证与替代解释：产品配方、加工、剂量、人群、对照与传统母本身份的差异，详见 research.md 和 summary.md。模型方向或感官相似不能补上临床证候证据。
- 正文最大表述强度：只写活菌产品对乳糖消化不良者的限定作用；健脾最多是类比，不作本条定论。
- 派生传统用词：本批次不自动接受；需同时具备归经、方向和语境，并符合 M 强度。
