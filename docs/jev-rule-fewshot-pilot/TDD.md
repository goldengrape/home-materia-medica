# Check Plan — Jev 四气五味归经 Pilot v0.3.1

> 来源：`URD.md`、`ADD.md`

## 1. Test Oracles

| ID | 对应需求 | 测试 | Oracle |
|---|---|---|---|
| TDD-TEST-001 | URD-REQ-008 | 检查 state 类型 | 发给 Jev 的 state 是单一自然语言 / Markdown string，不是 target feature JSON。 |
| TDD-TEST-002 | URD-REQ-007 | 检查 reasoning rules | rules 主要描述证候、功能群、四气强弱、五味功能模式和五脏投影，不写“必须选一个”等接口层约束。 |
| TDD-TEST-003 | URD-REQ-004 | Gold leakage | state 不含 held-out 药名、source URL 或 gold。 |
| TDD-TEST-004 | URD-REQ-001 | API 完整性 | 5/5 held-out 返回 HTTP 200；每个 response 可解析。 |
| TDD-TEST-005 | URD-REQ-005 | Output schema | answers 恰好包含 1 qi + 5 taste + 5 meridian keys。 |
| TDD-TEST-006 | URD-REQ-003 | 原生概率 | Choice probabilities 与 Noul 原样保存，不存在 calibration transform 字段。 |
| TDD-TEST-007 | URD-REQ-006 | 重复稳定性 | 同一冻结配置在一个 workflow run 内重复 3 次；逐次保存结果。 |
| TDD-TEST-008 | URD-REQ-004 | 样本分离 | five-shot 与 held-out 药物集合无交集。 |
| TDD-TEST-009 | URD-CON-001 | 模型追踪 | 结果记录 requested model alias 与 actual model。 |
| TDD-TEST-010 | URD-AC-004 | Secret | workflow 使用 `environment: API_KEYS`；日志不暴露 JEV_API_KEY。 |
| TDD-TEST-011 | URD-REQ-008 / ASM-004 | reasoning completeness | 人工复核每个 held-out 文档，确认 gold 所需主要桥梁在文本内可找到。 |
| TDD-TEST-012 | URD-REQ-005 / ADD-FR-006 | 五脏投影一致性 | rules、few-shot gold、held-out gold 均采用同一五脏功能群投影。 |
| TDD-TEST-013 | URD-AC-007 | 结论边界 | 结果文档不得把 reasoning-complete 5/5 当成生产准确率或“已校准”。 |

## 2. Pilot Scoring

### 四气

- Jev 返回 Choice；
- 与 gold 精确比较；
- 保存五个 choice probabilities；
- 特别记录寒↔凉、温↔热的相邻概率差。

### 五味

酸、苦、甘、辛、咸 5 个 Noul：

```text
noul >= 0.5 -> positive
noul < 0.5 -> negative
```

计算：

- per-sample exact set；
- micro precision / recall / F1。

0.5 仅用于 pilot 评分，不是生产阈值。

### 五脏归经

心、肝、脾、肺、肾 5 个 Noul，使用同一临时 0.5 切分。

gold 使用五脏功能群工作投影：

- 胃→脾；
- 胆→肝；
- 大肠→肺；
- 小肠→心；
- 膀胱→肾；
- 三焦按具体语境。

## 3. Invalid-run 规则

以下情况整次 benchmark 标记 invalid：

- target 文档直接出现 gold；
- target 药名 / source URL 泄漏；
- five-shot 与 held-out 重合；
- answer schema 改变；
- held-out 说明文档缺乏 gold 所需的核心推理桥梁；
- rules 和评分 gold 使用不同投影方法；
- prompt 在一次 benchmark 中途变化。

### v0.3 #11

Actions #11 标记为 **design-check / invalid benchmark**：

- 余甘子 rules 按脾胃功能群推到脾，但 gold 错误地只保留肺；
- 紫苏子说明文档没有足够温性桥梁。

因此 #11 不作为准确率证据。

## 4. v0.3.1 Valid Run

Actions #14：

- 5 个 held-out；
- 3 次重复；
- 四气 5/5 × 3；
- 五味 exact 5/5 × 3；
- 五脏归经 exact 5/5 × 3；
- 三类 micro-F1 = 1.0 × 3。

结果见 `RESULTS-v0.3.1.md`。

## 5. 人工复核点

即使 exact 全对，也继续检查：

1. 寒 / 凉与温 / 热是否存在窄概率差；
2. true/false Noul 是否大面积贴近 0.5；
3. 文档是否写得过于接近答案，导致 benchmark 只测试关键词复述；
4. rules 是否能迁移到现代食品的真实证据说明，而不是只适合传统中药功效主治。

## 6. 下一阶段

下一阶段不再继续在中药 reasoning-complete 样本上追求更高分。

应使用项目真实现代食品 Research Dossier 生成正式风格说明文档，进行 domain-transfer test。
