# Jev Materia Mapping Result

## Run metadata

```yaml
entry_id:
research_ref:
summary_ref:
summary_hash:
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model:
repeat_count:
run_date:
```

## 四气

| 候选 | Jev probability | M grade | 说明 |
|---|---:|---|---|
| 寒 |  |  |  |
| 凉 |  |  |  |
| 平 |  |  |  |
| 温 |  |  |  |
| 热 |  |  |  |

Jev Choice：

主要解释：

反证 / 替代解释：

## 五味

| 五味 | Jev score | M grade | 说明 |
|---|---:|---|---|
| 酸 |  |  |  |
| 苦 |  |  |  |
| 甘 |  |  |  |
| 辛 |  |  |  |
| 咸 |  |  |  |

## 五脏归经与主方向

| 归经 | Meridian score | 主方向 | 阴- | 阴+ | 阳- | 阳+ | M grade | 说明 |
|---|---:|---|---:|---:|---:|---:|---|---|
| 心 |  |  |  |  |  |  |  |  |
| 肝 |  |  |  |  |  |  |  |  |
| 脾 |  |  |  |  |  |  |  |  |
| 肺 |  |  |  |  |  |  |  |  |
| 肾 |  |  |  |  |  |  |  |  |

说明：

- `Meridian score` 是归经 Noul；
- `主方向` 是对应 direction Choice；
- 四个方向列保存 Choice probabilities；
- 低归经 score 的 direction 仍保留在研究记录，但通常不进入读者速查。

## 派生传统用词

```yaml
derived_wording:
  candidates: []
  rationale:
  status: draft | accepted
```

这里只根据：

```text
归经 + 主方向 + 原文语境
```

选择“疏肝、健脾、润肺、温中、化湿、生津”等习惯用词。

不得让派生用词反向修改 Jev 原始结果。

## Reader-facing summary

> 四气候选：  
> 五味候选：  
> 归经与主方向：  
> Jev score / probability 反映模型判断倾向；M grade 反映可追溯证据链强度，两者不是同一指标。

## M annotation

M 在 Jev 原始分类保存后评定。每个主要分类命题至少记录：

```yaml
mapping_claim:
jev_value:
jev_score_or_probability:
m_grade:
support:
contrary_evidence:
alternative_explanations:
allowed_wording:
```

不得用 M 修改 Jev 原始值，也不得用 Jev 高分提升 M。

## Claim Ledger handoff

- 可以记录的 Jev 原始分类：
- 派生传统用词：
- 低 M 但模型倾向明确的候选：
- 主要反证 / 替代解释：
- 不可把 Jev probability 写成真实证据概率：
- 不可因 Jev 结果提升的 M claims：
