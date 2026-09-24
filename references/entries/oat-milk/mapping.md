# Mapping｜oat-milk

> 分类为 Jev v0.4 原生输出；M 是其后根据 research.md 独立评注。分数不是校准概率或证据等级。

## Run metadata

```yaml
entry_id: oat-milk
research_ref: references/entries/oat-milk/research.md
summary_ref: references/entries/oat-milk/summary.md
summary_sha256: 3540b3bac93184c5da49bb2d31025dbbc4b804d434d9a3bda77ec62816313489
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T07:09:10.330187+00:00
native_result_ref: qa/jev-ten-batch/raw/oat-milk.json
```

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 1.00 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**。资料未支持把模型强制选出的平当作已证实的本草平性。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.05 | M-0 | 没有足够可追溯的本草映射依据。 |
| 苦 | 0.05 | M-0 | 没有足够可追溯的本草映射依据。 |
| 甘 | 0.30 | M-IV | 燕麦饮的感官轻甜依配方改变。 |
| 辛 | 0.05 | M-0 | 没有足够可追溯的本草映射依据。 |
| 咸 | 0.05 | M-0 | 没有足够可追溯的本草映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | Choice | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---|
| 心 | 0.12 | 阴- | 0.39 | 0.15 | 0.29 | 0.17 | M-0 |
| 肝 | 0.07 | 阴- | 0.49 | 0.08 | 0.35 | 0.08 | M-0 |
| 脾 | 0.14 | 阳+ | 0.37 | 0.18 | 0.01 | 0.44 | M-0 |
| 肺 | 0.06 | 阴+ | 0.35 | 0.52 | 0.05 | 0.08 | M-0 |
| 肾 | 0.06 | 阴- | 0.56 | 0.28 | 0.04 | 0.11 | M-0 |

各经方向的原生分布均已保存；低归经分数的方向不进入读者层。0.5 只作展示线，不是 M 或证据门槛。

## M 注释与写作交接

- 四气：资料未支持把模型强制选出的平当作已证实的本草平性。
- 反证与替代解释：产品配方、加工、剂量、人群、对照与传统母本身份的差异，详见 research.md 和 summary.md。模型方向或感官相似不能补上临床证候证据。
- 正文最大表述强度：仅写特定高纤维配方的短期试验，不推成普通商售品通用降脂功效。
- 派生传统用词：本批次不自动接受；需同时具备归经、方向和语境，并符合 M 强度。
