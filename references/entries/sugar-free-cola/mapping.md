# Mapping｜sugar-free-cola

> 分类为 Jev v0.4 原生输出；M 是其后根据 research.md 独立评注。分数不是校准概率或证据等级。

## Run metadata

```yaml
entry_id: sugar-free-cola
research_ref: references/entries/sugar-free-cola/research.md
summary_ref: references/entries/sugar-free-cola/summary.md
summary_sha256: f58d205f3de210b5ccca3fc6bc0c796fd9a4d3ac16a5d6bd031b548a9c06e1f5
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T07:09:11.255953+00:00
native_result_ref: qa/jev-ten-batch/raw/sugar-free-cola.json
```

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.02 | M-0 |
| 凉 | 0.09 | M-0 |
| 平 | 0.89 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**。资料未支持把模型强制选出的平当作已证实的本草平性。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.35 | M-IV | 酸味剂与口感类比。 |
| 苦 | 0.07 | M-0 | 没有足够可追溯的本草映射依据。 |
| 甘 | 0.33 | M-IV | 非糖甜味剂带来感官甜味，不等于传统甘味功效。 |
| 辛 | 0.05 | M-0 | 没有足够可追溯的本草映射依据。 |
| 咸 | 0.04 | M-0 | 没有足够可追溯的本草映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | Choice | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---|
| 心 | 0.07 | 阳+ | 0.13 | 0.02 | 0.40 | 0.45 | M-0 |
| 肝 | 0.05 | 阳- | 0.36 | 0.03 | 0.53 | 0.08 | M-0 |
| 脾 | 0.08 | 阴- | 0.59 | 0.05 | 0.15 | 0.21 | M-0 |
| 肺 | 0.05 | 阳- | 0.37 | 0.12 | 0.39 | 0.12 | M-0 |
| 肾 | 0.05 | 阴- | 0.59 | 0.15 | 0.21 | 0.05 | M-0 |

各经方向的原生分布均已保存；低归经分数的方向不进入读者层。0.5 只作展示线，不是 M 或证据门槛。

## M 注释与写作交接

- 四气：资料未支持把模型强制选出的平当作已证实的本草平性。
- 反证与替代解释：产品配方、加工、剂量、人群、对照与传统母本身份的差异，详见 research.md 和 summary.md。模型方向或感官相似不能补上临床证候证据。
- 正文最大表述强度：写替换含糖饮料可减少该次糖暴露，不写长期减重功效。
- 派生传统用词：本批次不自动接受；需同时具备归经、方向和语境，并符合 M 强度。
