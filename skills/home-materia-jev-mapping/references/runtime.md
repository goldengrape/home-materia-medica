# Jev Runtime Contract

## API

当前验证过的调用：

```text
POST https://api.typesafe.ai/v1/systemone
Authorization: Bearer $JEV_API_KEY
Content-Type: application/json
```

模型请求默认：

```text
jev-latest
```

必须记录 response 返回的实际 model，例如：

```text
jev-1.13.0
```

不要把 alias 和 actual model 当成同一字段。

## Secret

API key：

```text
JEV_API_KEY
```

只能从环境变量或 GitHub Actions Secret 注入。

当前 GitHub Actions 环境：

```text
Environment: API_KEYS
Secret: JEV_API_KEY
```

禁止：

- 把 key 写进仓库；
- 写入 `.env` 后提交；
- 在日志打印 Authorization header；
- 在结果文件保存 secret。

## Request

请求的核心结构：

```json
{
  "state": "<完整 Markdown / 自然语言说明文档上下文>",
  "model": "jev-latest",
  "questions": {
    "qi": "...",
    "taste_sour": "...",
    "taste_bitter": "...",
    "taste_sweet": "...",
    "taste_pungent": "...",
    "taste_salty": "...",
    "meridian_heart": "...",
    "meridian_liver": "...",
    "meridian_spleen": "...",
    "meridian_lung": "...",
    "meridian_kidney": "..."
  }
}
```

state 的内容顺序：

```text
判定方法
→ five-shot
→ 待判断说明文档
```

## Response validation

预期 answer keys 恰好为：

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
```

四气：

- answer type = choice；
- choice ∈ 寒/凉/平/温/热；
- 保存全部 choice probabilities。

五味、归经：

- answer type = noul；
- `0 <= noul <= 1`；
- 保存全部值。

如果 schema 改变、缺 key 或 value 超范围，本次结果应判 invalid，不要自行补值。

## Repeats

普通生产调用：

- 可以 1 次；
- 结果注明 `repeat_count: 1`。

方法学测试、重要条目或不稳定边界：

- 推荐 3 次；
- 保存每次原生结果；
- 报告 min/max；
- 不取“最好的一次”。

## 当前回归基线

中药 reasoning-complete：

- `run_pilot_v031.py`
- `fixtures-v0.3.1.json`

现代食品 domain transfer：

- `run_domain_transfer_v01.py`
- `domain-transfer-fixtures-v0.1.json`

这些是回归测试资产，不是出版正文数据源。
