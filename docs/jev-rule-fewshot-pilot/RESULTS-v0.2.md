# RESULTS v0.2 — Jev 封闭字段强制分类 Pilot

> run: GitHub Actions `Jev TCM Rule Few-shot Pilot #8`
> prompt_version: `jev-tcm-rule-fewshot-v0.2`
> fixture_version: `jev-tcm-pilot-fixtures-v0.2`
> requested_model: `jev-latest`
> actual_model: `jev-1.13.0`
> repeats: 3
> run time: 2026-09-24 UTC
> 结论性质：技术 pilot，不是生产校准结果。

## 1. 本版输出契约

v0.2 使用强制封闭分类，没有 abstention。

```yaml
四气:
  - 寒
  - 凉
  - 平
  - 温
  - 热

五味:
  - 酸
  - 苦
  - 甘
  - 辛
  - 咸

归经:
  - 心
  - 肝
  - 脾
  - 肺
  - 肾
```

Jev response 必须且只能包含：

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

本次 run 的 schema oracle 全部通过。

## 2. Held-out

v0.2 使用新的 5 味中药，不与 five-shot demonstrations 重叠：

| 样本 | Gold 四气 | Gold 五味（schema 投影） | Gold 五脏归经（schema 投影） |
|---|---|---|---|
| 黄芩 | 寒 | 苦 | 肺、脾 |
| 菊花 | 凉 | 甘、苦 | 肺、肝 |
| 茯苓 | 平 | 甘 | 心、肺、脾、肾 |
| 细辛 | 温 | 辛 | 心、肺、肾 |
| 干姜 | 热 | 辛 | 心、脾、肺、肾 |

投影说明：

- 菊花原“微寒” → 凉；
- 茯苓原五味含“淡”，但 schema 无“淡”，所以 gold_projected 只保留“甘”；
- 黄芩、干姜原归经含五脏以外经名，但 schema 无对应字段，因此不进入 gold_projected。

## 3. 三次重复总体结果

| 指标 | Repeat 1 | Repeat 2 | Repeat 3 | 范围 |
|---|---:|---:|---:|---:|
| 四气 accuracy | 4/5 | 4/5 | 4/5 | 0.80–0.80 |
| 五味 exact set | 5/5 | 5/5 | 5/5 | 5–5 |
| 五味 micro-F1 | 1.000 | 1.000 | 1.000 | 1.000–1.000 |
| 五脏归经 exact set | 2/5 | 1/5 | 1/5 | 1–2 |
| 五脏归经 micro-F1 | 0.750 | 0.769 | 0.720 | 0.720–0.769 |

三次均保存 Jev 原生 probability / Noul；没有投票、平均、校准函数或后处理概率。

## 4. 逐样本稳定结果

### 黄芩

Gold：

```text
寒
苦
肺、脾
```

三次：

- 四气：寒 ×3；寒概率约 0.97–0.98；
- 五味：苦 ×3；苦约 0.95；
- 肺：0.55–0.58；
- 脾：0.75–0.79；
- 肝：0.40–0.51。

归经：

- Repeat 1：肺、脾，exact；
- Repeat 2/3：肝、脾、肺，多出肝。

肝是典型阈值附近不稳定字段。

### 菊花

Gold：

```text
凉
甘、苦
肺、肝
```

三次全部 exact：

- 凉：0.85–0.86；
- 甘：0.83–0.84；
- 苦：0.75–0.78；
- 肝：0.88–0.90；
- 肺：0.57–0.63。

这是 v0.2 最稳定的完整样本。

### 茯苓

Gold：

```text
平
甘
心、肺、脾、肾
```

三次：

- 四气：平 ×3；P=0.99；
- 五味：甘 ×3；甘=0.60–0.66；
- 心：0.81–0.83；
- 脾：0.94；
- 肺：0.11–0.13；
- 肾：0.19–0.21。

三次均只输出“心、脾”。

这里的漏判不是 0.5 附近随机波动，而是稳定漏掉肺、肾。

### 细辛

Gold：

```text
温
辛
心、肺、肾
```

三次：

- 四气：温 ×3；0.96–0.97；
- 五味：辛 ×3；0.94；
- 肺：0.84–0.85；
- 心：0.14–0.16；
- 肾：0.11–0.12。

三次均只输出“肺”。

同样属于稳定漏判心、肾，不是阈值抖动。

### 干姜

Gold：

```text
热
辛
心、脾、肺、肾
```

三次：

- 五味：辛 ×3；0.93；
- 脾：0.78–0.79；
- 肺：0.80–0.82；
- 心：0.47–0.53；
- 肾：0.43–0.46。

四气三次均错误：

```text
预测：温
温 = 0.84–0.87
热 = 0.13–0.16
```

这是稳定的“温 / 热”系统性混淆，不能归因于随机边界波动。

归经：

- Repeat 1：脾、肺；
- Repeat 2：心、脾、肺；
- Repeat 3：脾、肺。

心处于边界，肾稳定偏低。

## 5. v0.2 说明了什么

### 5.1 封闭 JSON 设计正确

v0.1 把十二经都开放成输出字段，与项目真实契约不一致。

v0.2 已修正：

- 没有胃经、胆经等 schema 外输出；
- 没有淡、涩；
- 没有“证据不足”；
- 四气强制五选一；
- 五味与五脏归经固定字段全部返回。

因此 v0.2 才是后续方案应继承的接口形态。

### 5.2 五味在本轮表现很好

固定五味字段下，3 次 × 5 样本均 exact。

尤其茯苓 packet 有明显“味淡”，但 schema 不存在“淡”，Jev 仍在规定字段中选择“甘”，说明“封闭字段 + 分层 sensory + five-shot”至少在本轮有效阻止了 schema 外扩张。

这一结果只适用于当前小样本，不等于生产准确率 100%。

### 5.3 四气出现一个稳定错误：热 → 温

干姜三次全部被判温，而且概率差距较大。

这说明 v0.3 若要修改，应针对“温 / 热的判别边界”修改 criteria 或 contrastive demonstration，而不是用概率修正函数把 0.85 温硬改成热。

### 5.4 五脏归经仍是主要问题

当前错误以**召回不足**为主：

- Repeat 1：precision 1.00 / recall 0.60；
- Repeat 2：precision 0.909 / recall 0.667；
- Repeat 3：precision 0.900 / recall 0.60。

也就是说 Jev 相对保守，常能抓到最显著的脏腑，但会漏掉药典中同时存在、却没有在功能主治文字中显著出现的归经。

最典型：

- 茯苓：抓到心、脾，漏肺、肾；
- 细辛：抓到肺，漏心、肾；
- 干姜：抓到脾、肺，肾稳定偏低。

这个结果提示一个方法学问题：

> 如果去掉药名和直接归经标签，只提供功能、主治和感官资料，药典中的某些归经可能并不能从这些资料中唯一恢复。

这不一定表示 Jev 本身失败，也可能表示当前 Evidence Packet 缺少项目定义下完成归经映射所需要的桥梁证据。

## 6. 下一版本边界

v0.2 prompt / fixtures 已冻结，不能再根据本轮错例修改后仍称 v0.2。

若继续：

### v0.3 可以改

- 四气 criteria：专门强化温 vs 热的边界；
- five-shot：增加温/热对比，而不是只各给一个普通正例；
- 五脏归经：给每个脏建立明确的项目级判定 criteria，而不是仅写“传统功能、主治足以支持”；
- Evidence Packet：加入《居家本草》Concept Trace / M 映射桥梁字段，测试归经是否因此提高 recall。

### v0.3 仍不建议做

- 概率修正函数；
- 把多次结果投票伪装成单次概率；
- 用 v0.2 这 5 个 held-out 继续调完再报告同一批成绩。

如进入 v0.3，应再换新的 held-out。

## 7. 数据来源

Gold 与传统功能 / 主治按《中国药典 2025 年版》公开展示条目核对：

- 黄芩：https://www.antpedia.com/codex-cn-2025/1/0480_%E9%BB%84%E8%8A%A9.html
- 菊花：https://www.antpedia.com/codex-cn-2025/1/0492_%E8%8F%8A%E8%8A%B1.html
- 茯苓：https://www.antpedia.com/codex-cn-2025/1/0376_%E8%8C%AF%E8%8B%93.html
- 细辛：https://www.antpedia.com/codex-cn-2025/1/0359_%E7%BB%86%E8%BE%9B.html
- 干姜：https://wsj.yueyang.gov.cn/75523/75526/content_2359165.html

正式出版引用仍应以纸质药典为准。
