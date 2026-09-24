# Jev Runtime Contract — v0.4

## API

当前验证调用：

```text
POST https://api.typesafe.ai/v1/systemone
Authorization: Bearer $JEV_API_KEY
Content-Type: application/json
```

默认模型 alias：

```text
jev-latest
```

必须记录 response 中 actual model，例如：

```text
jev-1.13.0
```

## Secret

```text
Environment: API_KEYS
Secret: JEV_API_KEY
```

禁止把 key 写进仓库、日志、结果文件或已提交的 `.env`。

## state

```text
reasoning-rules-v0.4
→ five-shot-v0.4
→ target natural-language document
```

## questions

共 16 个：

```text
qi

taste_sour
taste_bitter
taste_sweet
taste_pungent
taste_salty

meridian_heart
meridian_liver
meridian_spleen
meridian_lung
meridian_kidney

heart_direction
liver_direction
spleen_direction
lung_direction
kidney_direction
```

### qi

Choice：

```text
寒 / 凉 / 平 / 温 / 热
```

### taste / meridian

Noul，保存 0–1 原始值。

### direction

Choice：

```text
阴- / 阴+ / 阳- / 阳+
```

保存 selected choice 与四项完整 probabilities。

方向对五经都会返回，但只有对应归经具有实际解释意义时才进入读者层。

## Response validation

必须满足：

- answer keys 恰好等于上述 16 项；
- qi type = choice；
- taste / meridian type = noul；
- direction type = choice；
- qi probabilities keys 恰好为寒凉平温热；
- direction probabilities keys 恰好为阴-/阴+/阳-/阳+；
- 所有 Noul 和 probabilities 均在 0–1。

schema 不符则本次 invalid，不自行补值。

## Repeats

普通生产：

```text
repeat_count = 1
```

方法学测试 / 关键条目 / 边界样本：

```text
repeat_count = 3
```

保存全部原始运行；不投票、不平均成“修正值”、不挑最好一次。

## Transient overload

Jev 偶尔可能返回：

```text
HTTP 529 / system_overloaded
```

允许有限指数式短重试，例如 2s / 4s / 8s。

只对明确的暂时性服务过载重试；prompt/schema 错误不得无限重试。

## 当前回归基线

### 中药

- `run_pilot_v04.py`
- `fixtures-v0.4.json`
- 3 次：四气 / 五味 / 归经全对；主方向 10/10 ×3。

### 现代食品

- `run_domain_transfer_v04.py`
- `domain-transfer-fixtures-v0.1.json`

当前实际模型：

```text
jev-1.13.0
```

回归文件是方法学资产，不是出版正文事实来源。
