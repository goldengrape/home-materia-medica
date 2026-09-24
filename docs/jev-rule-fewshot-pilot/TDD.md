# Check Plan — Jev 四气五味归经 Pilot

> 来源：`URD.md`、`ADD.md`

## 1. Test Oracles

| ID | 对应需求 | 测试 | Oracle |
|---|---|---|---|
| TDD-TEST-001 | URD-REQ-004 / AC-003 | 检查发送给 Jev 的 target | JSON state 中不存在 `gold` 字段，也不存在 5 个测试药真实名称。 |
| TDD-TEST-002 | URD-REQ-001 / AC-001 | 对 5 个 target 调用 Jev | 5/5 返回 HTTP 200；每个都有 1 Choice + 10 Noul，且 answer keys 精确匹配封闭 schema。 |
| TDD-TEST-003 | URD-REQ-003 / AC-002 | 检查结果保存 | Choice 的 `probabilities` 与所有 Noul 数值原样写入 results；无概率变换字段。 |
| TDD-TEST-004 | URD-REQ-002 | 检查 prompt 结构 | 每次 request state 都含同一 `rules` 与同一 5 个 `reference_examples`，target 单独替换。 |
| TDD-TEST-005 | URD-CON-002 / AC-004 | 检查 Actions secret | workflow 使用 `environment: API_KEYS`；日志仅出现 `JEV_API_KEY: ***` 或不显示值。 |
| TDD-TEST-006 | URD-AC-005 | 检查评分 | results summary 至少包含四气 correct/5、五味 micro P/R/F1、归经 micro P/R/F1、逐样本 predicted vs gold。 |
| TDD-TEST-007 | URD-CON-001 / CON-004 | 检查复现信息 | results 中包含实际返回 model、prompt_version、fixture_version。 |
| TDD-TEST-008 | URD-AC-006 | 检查结论边界 | 报告不得根据 5 个样本确定生产阈值，不得写“已校准”。 |
| TDD-TEST-009 | URD-REQ-006 / AC-007 | 重复运行稳定性 | 冻结 prompt / fixtures / model alias 后在同一 runner 内重复 3 次；逐次保留原生结果，报告分数范围及跨 0.5 标签变化。 |
| TDD-TEST-010 | URD-REQ-005 | 输出 key 精确匹配 | answers 只能有 11 个固定 keys：1 个 qi + 5 个 taste + 5 个 meridian。 |
| TDD-TEST-011 | URD-REQ-005 | 四气强制分类 | qi criteria 恰好为寒/凉/平/温/热，不含证据不足、未知、其他。 |
| TDD-TEST-012 | URD-REQ-005 | schema 外标签不可输出 | question construction 中不得出现淡、涩或五脏之外的归经字段。 |
| TDD-TEST-013 | URD-REQ-004 | held-out / few-shot 不重合 | v0.2 五个 held-out 药名与 five-shot demo 药名交集为空。 |

## 2. Pilot Scoring

### 四气

- 取 Choice 返回的 `choice`；
- 与 normalized gold 精确比较；
- 记录完整 choice probabilities；
- 额外记录是否错在相邻档（例如 寒↔凉、温↔热），但不把相邻错算成正确。

### 五味

对酸、苦、甘、辛、咸分别使用 Noul：

```text
noul >= 0.5 -> predicted positive
noul < 0.5  -> predicted negative
```

计算：

- per-sample exact set match；
- micro precision；
- micro recall；
- micro F1。

0.5 只是 pilot 评分规则，不是生产置信阈值。

### 归经

只对心、肝、脾、肺、肾 5 个固定字段使用相同的临时 0.5 二值规则，计算：

- per-sample exact set match；
- micro precision；
- micro recall；
- micro F1。

### 重复运行稳定性

v0.2 对同一冻结配置在同一 workflow run 内执行 3 次重复。重复运行不做投票、不平均原生概率，也不产生“修正后的概率”；只回答两个问题：

1. 总体指标在重复运行间是否稳定；
2. 哪些标签会在 0.5 两侧翻转。

若差异集中在接近 0.5 的 Noul，报告为边界不稳定；若高概率标签也频繁翻转，则视为更严重的可靠性问题。

## 3. Safety / Negative Tests

### TDD-NEG-001｜Secret 不得入库

仓库文件不得包含真实 `JEV_API_KEY` 值。

### TDD-NEG-002｜Gold leakage

runner 在发请求前执行断言：

- state JSON 不含 `gold` key；
- state JSON 不含测试样本真实药名；
- state JSON 不含测试样本的 source URL title 中药名。

任一命中则停止，不调用 API。

### TDD-NEG-003｜API failure

HTTP 非 200 时：

- 不伪造结果；
- runner 退出非零；
- workflow 失败；
- 错误输出不得打印 Authorization header。

### TDD-NEG-004｜Schema failure

若 Jev 缺少预期 answer、type 不匹配、Noul 不在 0–1：

- 判定本次 run 无效；
- 不计算成绩。

## 4. 人工复核点

run 完成后人工看三类异常：

1. 四气明显正确，但五味或归经概率大面积接近 0.5；
2. 五脏字段出现稳定漏判、假阳性或低召回；
3. 模型通过功能词面机械复制器官名称，而没有体现 few-shot / rules 的约束。

这些观察写入 pilot 结果，不在同一 run 中修改 prompt 后重跑并把结果混在一起。若修改 prompt，必须升 `prompt_version`。

## 5. 本轮不设的测试

- 不测试跨模型比较；
- 不测试 rule-only vs few-shot A/B；
- 不测试 post-hoc probability calibration；
- 不测试完整现代食品 Research Dossier。

这些如果需要，作为下一轮独立实验，避免 pilot 一次承担太多问题。
