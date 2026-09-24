# Check Plan — Jev Pilot v0.4

> 来源：`URD.md`、`ADD.md`

## Test Oracles

| ID | Test | Oracle |
|---|---|---|
| TDD-TEST-001 | state 类型 | 单一自然语言 / Markdown string。 |
| TDD-TEST-002 | rules 内容 | 教推理，不写“必须选哪个字段”等接口约束。 |
| TDD-TEST-003 | leakage | held-out 药名、URL、gold 不进入 state。 |
| TDD-TEST-004 | API | 5/5 held-out 正常返回。 |
| TDD-TEST-005 | answer schema | 恰好 16 keys。 |
| TDD-TEST-006 | qi | Choice keys = 寒/凉/平/温/热。 |
| TDD-TEST-007 | taste / meridian | 10 个 Noul 均在 0–1。 |
| TDD-TEST-008 | direction | 5 个 Choice keys = 阴-/阴+/阳-/阳+。 |
| TDD-TEST-009 | native scores | 不存在 calibration transform。 |
| TDD-TEST-010 | repeats | 冻结配置重复 3 次。 |
| TDD-TEST-011 | sample separation | five-shot 与 held-out 不重合。 |
| TDD-TEST-012 | model trace | 记录 requested alias + actual model。 |
| TDD-TEST-013 | secret | API_KEYS / JEV_API_KEY 不泄漏。 |
| TDD-TEST-014 | reasoning completeness | gold 主要桥梁存在于说明文档。 |
| TDD-TEST-015 | 五脏投影 | rules / demo / gold 投影一致。 |
| TDD-TEST-016 | 病机/作用方向 | 不把“火旺、阳虚”等原始状态直接当成食材作用方向。 |
| TDD-TEST-017 | mixed effect | direction Choice 保存完整 probabilities。 |
| TDD-TEST-018 | domain transfer | 真实食材 dossier 不发送 M / final mapping。 |

## Scoring

### 四气

Choice exact accuracy。

### 五味

5 个 Noul，pilot 临时使用 0.5 转标签，计算 exact set / micro P/R/F1。

### 五脏归经

5 个 Noul，同上。

### 主方向

只在 gold 的有效归经上评分 direction Choice。

例如：

```text
gold meridians = 肺、脾
→ 只评分 lung_direction / spleen_direction
```

未归该经时 direction 仍保存，但不作为该样本方向准确率。

这是因为 direction 的语义是：

> 如果讨论该经，主要向哪个方向作用。

## v0.4 Valid Regression

Workflow：

```text
Jev Yin-Yang Vector v0.4 Pilot #7
run 35961677721
```

三次重复：

- 四气：5/5 ×3；
- 五味 exact：5/5 ×3；
- 五脏归经 exact：5/5 ×3；
- 10 个有效归经主方向：10/10 ×3；
- actual model：`jev-1.13.0`。

## Design-check 历史

v0.4 早期曾测试 20 个 direction Noul。

该 schema 被废弃，因为：

- 同一经会产生多个同时过阈值的一级标签；
- 一级输出过于臃肿；
- 与“原子分类 → 派生传统用词”的目标不符。

这些 run 只作为 design-check，不作为当前 schema benchmark。

## Food Domain Transfer

Workflow：

```text
Jev Food Domain Transfer v0.4 #2
run 35961867966
```

测试：

- 开心果；
- 黑巧克力；
- 咖啡；
- 酸奶；
- 方便面。

不计算 gold accuracy。

检查：

- 原有四气 / 五味 / 归经趋势是否稳定；
- direction Choice 是否可解释；
- 混合效应是否由 probabilities 显示；
- Jev 输出是否继续与 M grade 独立。

第一次 domain run 因 HTTP 529 system overload 失败，属于服务暂时过载；第二次在有限短重试后成功。

## 结论边界

不得从 5 个中药样本推出生产准确率。

不得从 direction Choice 推导 M grade。

不得把 Choice probability 写成真实世界概率。
