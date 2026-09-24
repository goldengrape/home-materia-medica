# Mapping｜paper-filtered-coffee

> 分类为 Jev v0.4 原生输出；M 是其后根据 research.md 独立评注。分数不是校准概率或证据等级。

## Run metadata

```yaml
entry_id: paper-filtered-coffee
research_ref: references/entries/paper-filtered-coffee/research.md
summary_ref: references/entries/paper-filtered-coffee/summary.md
summary_sha256: 3068c12ed84d927370987d205f02d24d4dfce5b4e94ae6552fa1a1362961f4eb
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T07:09:09.896529+00:00
native_result_ref: qa/jev-ten-batch/raw/paper-filtered-coffee.json
```

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.01 | M-0 |
| 凉 | 0.03 | M-0 |
| 平 | 0.71 | M-0 |
| 温 | 0.23 | M-0 |
| 热 | 0.02 | M-0 |

Jev Choice：**平**。资料未支持把模型强制选出的平当作已证实的本草平性。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.08 | M-0 | 没有足够可追溯的本草映射依据。 |
| 苦 | 0.48 | M-IV | 纸滤黑咖啡的感官苦味，烘焙与萃取影响强度。 |
| 甘 | 0.07 | M-0 | 没有足够可追溯的本草映射依据。 |
| 辛 | 0.18 | M-0 | 没有足够可追溯的本草映射依据。 |
| 咸 | 0.04 | M-0 | 没有足够可追溯的本草映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | Choice | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---|
| 心 | 0.34 | 阳+ | 0.02 | 0.00 | 0.08 | 0.90 | M-0 |
| 肝 | 0.12 | 阳+ | 0.20 | 0.01 | 0.31 | 0.48 | M-0 |
| 脾 | 0.08 | 阳+ | 0.40 | 0.01 | 0.13 | 0.46 | M-0 |
| 肺 | 0.10 | 阳+ | 0.25 | 0.02 | 0.21 | 0.52 | M-0 |
| 肾 | 0.09 | 阳+ | 0.38 | 0.01 | 0.18 | 0.43 | M-0 |

各经方向的原生分布均已保存；低归经分数的方向不进入读者层。0.5 只作展示线，不是 M 或证据门槛。

## M 注释与写作交接

- 四气：资料未支持把模型强制选出的平当作已证实的本草平性。
- 反证与替代解释：产品配方、加工、剂量、人群、对照与传统母本身份的差异，详见 research.md 和 summary.md。模型方向或感官相似不能补上临床证候证据。
- 正文最大表述强度：可写短时警觉和纸滤与未过滤的血脂差别；醒神仅作近现代用语，不指定归经。
- 派生传统用词：本批次不自动接受；需同时具备归经、方向和语境，并符合 M 强度。
