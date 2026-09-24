# Mapping｜pistachio

> 分类为 Jev v0.4 原生输出；M 是其后根据 research.md 独立评注。分数不是校准概率或证据等级。

## Run metadata

```yaml
entry_id: pistachio
research_ref: references/entries/pistachio/research.md
summary_ref: references/entries/pistachio/summary.md
summary_sha256: 438a6ca5b062e2134fbca4476ecfdfe14b2474ec3c734ab87b215aa7a06faa3d
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T07:09:07.742383+00:00
native_result_ref: qa/jev-ten-batch/raw/pistachio.json
```

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.16 | M-0 |
| 温 | 0.84 | 传统直录；现代形态类推 M-IV |
| 热 | 0.00 | M-0 |

Jev Choice：**温**。《本草拾遗》经《本草纲目》转引有温；《饮膳正要》未定寒温，且研究未测证候。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.22 | M-0 | 没有足够可追溯的本草映射依据。 |
| 苦 | 0.05 | M-0 | 没有足够可追溯的本草映射依据。 |
| 甘 | 0.76 | 传统直录；现代类推 M-IV | 《饮膳正要》记甘。 |
| 辛 | 0.64 | 传统直录；现代类推 M-IV | 《本草拾遗》转引记辛，另记涩。 |
| 咸 | 0.07 | M-0 | 没有足够可追溯的本草映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | Choice | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---|
| 心 | 0.11 | 阳+ | 0.06 | 0.06 | 0.15 | 0.73 | M-0 |
| 肝 | 0.13 | 阳+ | 0.17 | 0.07 | 0.11 | 0.65 | M-0 |
| 脾 | 0.59 | 阳+ | 0.10 | 0.01 | 0.00 | 0.89 | M-0 |
| 肺 | 0.07 | 阳+ | 0.24 | 0.10 | 0.05 | 0.61 | M-0 |
| 肾 | 0.12 | 阳+ | 0.13 | 0.12 | 0.02 | 0.73 | M-0 |

各经方向的原生分布均已保存；低归经分数的方向不进入读者层。0.5 只作展示线，不是 M 或证据门槛。

## M 注释与写作交接

- 脾及阳+：Jev Noul 0.59；M-0。传统有调中、去冷气及诸痢记录，但没有可核实的明确脾经原文；现代代谢指标不能证明归经。
- 四气：《本草拾遗》经《本草纲目》转引有温；《饮膳正要》未定寒温，且研究未测证候。
- 反证与替代解释：产品配方、加工、剂量、人群、对照与传统母本身份的差异，详见 research.md 和 summary.md。模型方向或感官相似不能补上临床证候证据。
- 正文最大表述强度：可以并列呈现古籍辛温涩与甘的不同记载；脾阳+仅作为 Jev 的分类倾向，不写成确定功效。
- 派生传统用词：本批次不自动接受；需同时具备归经、方向和语境，并符合 M 强度。
