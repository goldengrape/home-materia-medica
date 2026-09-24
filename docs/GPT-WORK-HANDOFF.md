# GPT Work 交班文档

> 项目：居家本草 / Home Materia Medica  
> 仓库：`goldengrape/home-materia-medica`  
> 当前主分支：`main`  
> 交班时 main SHA：`4fdd5a9353693beb12fcf301da7ae7d2e76c5753`  
> 作用：让新的 GPT Work 在不依赖旧聊天记录的情况下，直接继续项目开发与批量生产准备。

---

# 0. 接手后先做什么

先按下面顺序阅读：

1. `docs/生产流程.md`
2. `docs/居家本草编纂凡例-v1.0.md`
3. `docs/执行路线图.md`
4. `docs/TRACE.md`
5. `skills/home-materia-research/SKILL.md`
6. `skills/home-materia-jev-mapping/SKILL.md`
7. `skills/home-materia-jev-mapping/references/runtime.md`
8. `docs/jev-rule-fewshot-pilot/RESULTS-v0.4.md`

如果这些文件与本交班文档有冲突，以这些当前权威文件为准，并同步修订本交班文档。

---

# 1. 项目目标

《居家本草》研究现代生活中常见食品、饮料、加工食品、复合食品及相关生活场景。

项目的核心不是“给每个食物强行定一个中医标签”，而是：

1. 收集可追溯资料；
2. 整理成中立、完整、可推理的说明文档；
3. 用 Jev 在固定 reasoning rules + five-shot 下做本草分类；
4. 把 Jev 分类与独立证据强度 M 并列；
5. 根据资料和分类结果写成可读正文。

重要原则：

- 传统资料、现代人体证据、机制、本草分类彼此分层；
- 现代生理指标不能直接翻译成中医术语；
- 允许 E-0、M-0 和低证据分类；
- Jev score 不是经过经验校准的真实概率；
- 下游不得为了写得好看而修改上游资料或证据等级。

---

# 2. 当前唯一生产主流程

已经冻结：

```text
搜 → 整 → 判 → 写
```

完整定义见：

`docs/生产流程.md`

## 2.1 搜｜收集资料

输出：

`references/entries/<entry-id>/research.md`

负责：

- 食品 / 制品身份；
- R1 / R2 / R3 研究深度；
- 核心问题与 PECOT；
- Search Log；
- Composition & Exposure；
- 传统来源；
- 现代人体证据；
- 安全资料；
- 加工、剂量、时机；
- 机制；
- 反证与冲突；
- Evidence Record；
- D0–D4 直接性；
- DOI / PMID / 古籍版本核验。

本阶段不得预设最终四气、五味、归经或阴阳增减答案。

## 2.2 整｜整理总结资料

输出：

`references/entries/<entry-id>/summary.md`

负责：

- Appraisal；
- Outcome synthesis；
- E-A ～ E-0；
- 必要 Concept Trace；
- 冲突、未知、替代解释；
- evidence-base overlap；
- evidence cutoff；
- stopping status / reason；
- Reference audit。

`summary.md` 是 Jev 的唯一正式生产输入。

### summary.md 禁止提前写入

- 最终四气；
- 最终五味；
- 最终归经；
- 最终阴- / 阴+ / 阳- / 阳+；
- Jev score；
- M grade；
- 为了引导模型而添加的答案导向句。

如果古籍原文自己明确写了某性味或归经，可以作为传统事实保留，并注明来源；不能把它伪装成现代食品的最终分类结论。

## 2.3 判｜Jev 分类 + M

顺序固定：

```text
summary.md
→ Jev v0.4
→ 保存原始 score / probabilities
→ 回查 research.md
→ 对分类命题逐项标 M
→ mapping.md
```

输出：

`references/entries/<entry-id>/mapping.md`

M 不在 Jev 之前充当 gate。

## 2.4 写｜根据资料 + 分类写正文

输入：

- `summary.md`
- `mapping.md`
- 必要时回查 `research.md`
- Safety / conflicts / unknowns
- Claim Ledger / sources

输出：

`entries/<entry-id>.md`

写作层只负责表达，不重新研究、不重分类、不提升 E/M。

如果发现缺资料：

```text
写 → 回到整 / 搜
```

如果发现分类问题：

```text
写 → 回到判
```

不要在正文里静默补结论。

---

# 3. 研究方法中的 R / D / E / M

## R｜研究深度

- R1：简明；
- R2：标准，默认；
- R3：重点 / 高文献密度 / 方法示范。

R 控制研究预算，不代表证据质量。

## D｜证据距离

D0–D4 用于标记现代证据距离目标食品有多远。

原则：

- D0 / D1：直接或近直接；
- D2：明显间接，需要降格；
- D3：孤立成分，主要用于机制；
- D4：相似食品 / 理论类比，只能提供假说。

## E｜现代人体效应证据

按具体 outcome 评：

- E-A：较强；
- E-B：中等；
- E-C：有限；
- E-D：机制或信号；
- E-0：不足。

不要给整个食品一个总 E。

## M｜本草映射证据强度

M-I ～ M-0 表示本草分类命题的证据强度。

当前流程中：

> 先 Jev 分类，再对分类命题逐项标 M。

最重要的式子：

```text
Jev score != M grade
```

允许：

```text
酸奶
脾：Jev 0.62
主方向：阳+
M：M-0
```

禁止：

- M-0 就压低 / 隐藏 Jev score；
- Jev 高分就提高 M；
- 把 Jev score 写成“真实概率”。

---

# 4. Jev v0.4 当前分类方法

权威 skill：

`skills/home-materia-jev-mapping/SKILL.md`

当前 v0.4 一次调用共 16 个 questions。

## 4.1 四气

1 个 Choice：

```text
寒 / 凉 / 平 / 温 / 热
```

保存 selected choice + 全部 probabilities。

## 4.2 五味

5 个独立 Noul：

```text
酸
苦
甘
辛
咸
```

保存全部 0–1 原始值。

## 4.3 五脏归经

5 个独立 Noul：

```text
心
肝
脾
肺
肾
```

保存全部 0–1 原始值。

## 4.4 每经主方向

5 个 Choice：

```text
heart_direction
liver_direction
spleen_direction
lung_direction
kidney_direction
```

固定四选一：

```text
阴-
阴+
阳-
阳+
```

每个 Choice 保存：

- selected choice；
- 四项完整 probabilities。

### 阴阳±工作语义

**阳+**

增加该经温煦、推动、活动、运化或功能性阳侧表现。

典型：

- 温；
- 助阳；
- 回阳；
- 健脾 / 健胃 / 助运；
- 纠正虚寒 / 功能低下。

**阳-**

减少该经热、火、亢进、升越或过强活动。

典型：

- 清热；
- 泻火；
- 平亢；
- 项目约定中：`疏肝 → 肝阳-`。

**阴+**

增加滋养、津液、血、精、濡润、收摄。

典型：

- 养阴；
- 生津；
- 润燥 / 润肺 / 润肠；
- 补血；
- 益精。

**阴-**

减少阴侧偏盛、停聚、积滞或壅滞。

典型：

- 化湿；
- 燥湿；
- 化痰；
- 利水；
- 消食 / 消积。

### + / - 不是好坏

```text
阴- != 伤阴
阳- != 损阳
阴+ != 滋腻
阳+ != 上火
```

它们只表示作用方向。

---

# 5. Jev 架构：语义上级连，计算上同步

逻辑上：

```text
先判断归经位置
→ 再判断该经主方向
```

API 实现上：

> 归经和 5 个 direction Choice 在同一次 Jev request 中同步计算。

不要做：

```text
Call 1：先判归经
→ threshold
→ Call 2：只对过阈值归经再判方向
```

原因：

- 第一层漏经会永久丢失方向；
- 0.49 / 0.51 边界会改变第二次 schema；
- 同一组证据常同时说明位置和方向；
- 两次调用会放大随机性与成本。

---

# 6. 传统习惯用词的位置

“疏肝、健脾、安神、润燥、清热、温中、化湿、生津”等不再作为底层一级分类。

底层先保持：

```text
归经 + 阴阳增减 + 语境
```

再在写作层派生习惯表达。

示例：

```text
肝 + 阳-
→ 疏肝 / 平肝等候选

脾 + 阳+
→ 健脾 / 温中等候选

肺 + 阴+
→ 润肺 / 生津等候选

脾 + 阴-
→ 化湿 / 消食等候选
```

不是严格一对一，最终词语仍看上下文。

不要重新建立一个庞大的“功效词一级 ontology”。

---

# 7. Jev v0.4 已完成的验证

结果文件：

`docs/jev-rule-fewshot-pilot/RESULTS-v0.4.md`

## 7.1 中药回归

有效 run：

```text
Jev Yin-Yang Vector v0.4 Pilot #7
GitHub Actions run 35961677721
actual model: jev-1.13.0
```

5 个 held-out，3 次重复：

- 四气：5/5 ×3；
- 五味 exact：5/5 ×3；
- 五脏归经 exact：5/5 ×3；
- 10 个有效归经主方向：10/10 ×3。

注意：

> 这只是小样本 reasoning-complete 回归，不是生产准确率估计。

## 7.2 现代食品 domain transfer

有效 run：

```text
Jev Food Domain Transfer v0.4 #2
GitHub Actions run 35961867966
```

测试：

- 开心果；
- 黑巧克力；
- 咖啡；
- 酸奶；
- 方便面。

主要结果：

- 开心果：脾阳+、肾阳+；
- 咖啡：脾阳+；
- 酸奶：脾阳+为主，但方向 probabilities 较分散；
- 黑巧克力：无主归经；
- 方便面：无主归经。

---

# 8. JEV API KEY：本项目正确的获取 / 使用方法

这里必须区分：

1. **最初从 Jev / TypeSafe 账号获得 API Key**；
2. **本项目运行时怎样取得这个 key**。

## 8.1 本项目已经配置好的 key 在哪里

当前仓库已经配置：

```text
GitHub Environment: API_KEYS
Environment Secret: JEV_API_KEY
```

GPT Work **不需要，也不应该读取这个 secret 的明文**。

GitHub Secret 的正确用途是：

> 由 GitHub Actions 在运行时把 secret 注入 job 的环境变量。

不要尝试：

- 从仓库文件中搜索 key；
- 从 GitHub API 读取 secret 明文；
- 要求用户把已有 key 粘贴到聊天；
- 把 key 写进代码；
- 把 key 写进提交的 `.env`；
- 把 key 打印到 Actions 日志；
- 把 key 保存进 JSON artifact。

## 8.2 GitHub Actions 的正确写法

job 必须声明：

```yaml
jobs:
  run-jev:
    runs-on: ubuntu-latest
    environment: API_KEYS
```

然后在需要 Jev 的 step 里注入：

```yaml
env:
  JEV_API_KEY: ${{ secrets.JEV_API_KEY }}
  JEV_MODEL: jev-latest
```

Python 中：

```python
import os

api_key = os.environ.get("JEV_API_KEY")
if not api_key:
    raise RuntimeError("JEV_API_KEY is unavailable")
```

## 8.3 API 调用

当前验证 endpoint：

```text
POST https://api.typesafe.ai/v1/systemone
```

认证：

```http
Authorization: Bearer <JEV_API_KEY>
Content-Type: application/json
```

默认请求模型：

```text
jev-latest
```

必须同时记录 response 返回的 actual model，例如：

```text
jev-1.13.0
```

alias 和 actual model 不是同一个字段。

## 8.4 现有 workflow 示例

直接参考：

```text
.github/workflows/jev-yinyang-vector-v04.yml
.github/workflows/jev-domain-transfer-v04.yml
```

注意：

这两个 workflow 的 push branch filter 是历史 feature branch，但都带 `workflow_dispatch`。

如果 Work 要做新的生产任务，更合适的方式通常是：

- 新建面向 `main` 或明确生产分支的 workflow；
- 或通过 `workflow_dispatch` 手动运行现有 workflow；
- 不要为了拿 secret 而改成仓库明文配置。

## 8.5 如果 Actions 报 JEV_API_KEY unavailable

按顺序检查：

1. job 是否写了：

```yaml
environment: API_KEYS
```

2. step 是否写了：

```yaml
JEV_API_KEY: ${{ secrets.JEV_API_KEY }}
```

3. Environment 名是否严格是：

```text
API_KEYS
```

4. Secret 名是否严格是：

```text
JEV_API_KEY
```

如果这些都正确但 secret 仍不可用，再检查 GitHub Environment 是否有 deployment protection / approval 要求。

不要改成“请用户把 key 贴出来”作为默认解决办法。

## 8.6 如果真的需要新建 / 轮换 Jev API Key

这个动作发生在 Jev / TypeSafe 账号侧，不在本仓库完成。

本仓库只约定：

> 新 key 最终仍写入 GitHub Environment `API_KEYS` 的 `JEV_API_KEY` secret。

不要把新 key 提交到 git。

当前仓库文档只验证了 API 使用方式，并没有冻结 TypeSafe Console 的具体 UI 菜单路径；如果需要新建 / 轮换 key，应以 TypeSafe 当时的官方 Console / 文档为准，不要根据记忆猜按钮位置。

---

# 9. Jev 的运行契约

权威文件：

`skills/home-materia-jev-mapping/references/runtime.md`

## 普通生产

```text
repeat_count = 1
```

## 方法学测试 / 关键条目 / 边界样本

```text
repeat_count = 3
```

保存每次原始结果。

不要：

- 投票成“正确答案”；
- 平均成校准后的概率；
- 只挑最好的一次；
- 训练 post-hoc calibration function。

## HTTP 529

Jev 偶尔可能返回：

```text
HTTP 529
system_overloaded
```

允许只针对明确暂时性过载做有限短重试，例如：

```text
2s → 4s → 8s
```

不要对 schema / prompt / auth 错误无限重试。

---

# 10. 当前仓库状态

交班时：

```text
main SHA:
4fdd5a9353693beb12fcf301da7ae7d2e76c5753
```

最近已合并的重要 PR：

- PR #18：Jev v0.3.1 + domain transfer + mapping skill；
- PR #19：Jev v0.4 五脏阴阳增减主方向；
- PR #20：冻结“搜 → 整 → 判 → 写”四阶段生产流程。

当前 open PR：

- PR #14：`skills: 加入 general-writing-standard`
  - 仍为历史 Draft / deferred；
  - 不要默认把它当成当前 writing skill；
  - 正式 writing skill 应在 RM-PHASE-030 按当前四阶段接口重新设计。

旧的概率校准 / qi-channel estimator 路线已经废弃，不要复活：

- 不训练修正函数；
- 不用人工 calibration 覆盖 Jev 原始 score。

---

# 11. 当前最重要的下一步

路线图见：

`docs/执行路线图.md`

当前还没有完成的核心基础设施：

## 11.1 第一版 Concept skeleton

建立：

`concepts/`

优先底层概念：

- 四气；
- 五味；
- 归经；
- 心 / 肝 / 脾 / 肺 / 肾；
- 阴 / 阳；
- + / -；
- 五脏 / 六腑功能群投影；
- 炮制；
- 配伍。

不要把“疏肝、健脾、润肺、温中、化湿、生津”等全部做成一级概念页。

这些是后续派生用词。

## 11.2 Entry Registry

建立：

`catalog/entries.yaml`

先纳入：

- 6 个 Pilot；
- coffee research parent 与直接子条；
- 第一批准备进入生产的 10–25 个条目。

至少需要：

- entry ID；
- name；
- entry_type；
- parent / related；
- R depth；
- status；
- publish / volume / section 等必要元数据。

## 11.3 跑 3 个完整四阶段正文 Pilot

完整链：

```text
research.md
→ summary.md
→ mapping.md
→ entry.md
```

要验证：

- summary 没有偷渡分类；
- Jev/M 没有反向污染 research facts；
- writing 不重新研究、不重分类；
- E/M 强度进入正文后不升级；
- 传统习惯词派生是否自然。

之前讨论中过一个合适组合：

- 开心果；
- 黑巧克力；
- 珍珠奶茶。

这个组合不是不可更改的硬规则，但它覆盖：

- 传统资料较强；
- 现代证据复杂；
- 现代复合食品 / 稀疏直接证据。

## 11.4 设计正式 writing skill

目标：

`skills/home-materia-writing/`

它应该只消费：

- summary.md；
- mapping.md；
- 必要时 research.md；
- Claim Ledger / sources。

它不得：

- 自己重新搜索；
- 改 E/D；
- 改 Jev 分类；
- 改 M；
- 为了行文完整强行填满性味归经。

## 11.5 最小批量 QA

只做真正需要的自动检查：

- duplicate entry ID；
- entry status；
- research / summary / mapping 文件是否齐全；
- evidence cutoff；
- Jev model/version metadata；
- M 是否后置；
- Claim Ledger；
- TRACE completeness。

不要现在建设重型平台。

---

# 12. 什么时候可以开始批量生产

满足：

1. Concept skeleton 可用；
2. `catalog/entries.yaml` 可用；
3. 至少 3 个完整四阶段 Pilot 跑通；
4. 最小 QA 可用。

之后进入：

```text
每批 10–25 条
搜 → 整 → 判 → 写
```

优先核心 R2 + 少量 R3。

不要一次把约 369 条全部铺开。

---

# 13. 已完成 Pilot

研究 Pilot 已完成：

- 开心果 R2；
- 黑巧克力 R3；
- 珍珠奶茶 R2；
- 咖啡 R3；
- 酸奶 R2；
- 方便面 R2。

这些现有 `research.md` 是后续补 `summary.md` / `mapping.md` / 正文 Pilot 的最佳起点。

不要重复从零研究它们，除非：

- evidence cutoff 需要更新；
- identity 被重新定义；
- 现有 dossier 有明确缺口。

---

# 14. 给 GPT Work 的执行纪律

## 必须

- 以仓库 current docs 为 source of truth；
- 修改方法时同步 docs / skill / TRACE；
- 保存中间结果；
- 保留支持和反证；
- 记录版本、model、cutoff；
- 使用 feature branch；
- 运行必要 QA / workflow；
- PR 中写清楚改变了什么方法规则。

## 不要

- 根据旧聊天印象覆盖仓库现行规则；
- 把实验结果直接变成生产结论；
- 把 Jev score 当成真实概率；
- 在 Jev 前用 M gate 隐藏候选；
- 用 M 修改 Jev score；
- 因 Jev 高分提升 M；
- 把现代机制直接翻译成中医术语；
- 把传统母成分机械相加成现代复合食品本草结论；
- 把 serving temperature 当成本草寒热；
- 暴露 / 打印 / 提交 API key；
- 复活旧的人工 probability calibration 路线；
- 没跑通流程就建设复杂自动化。

---

# 15. 推荐的接手顺序

GPT Work 接手后，建议直接按：

```text
A. 检查 main / docs / open PR
↓
B. 建 concepts/ 最小原子骨架
↓
C. 建 catalog/entries.yaml
↓
D. 选 3 个 Pilot
↓
E. 对每个 Pilot：
   research.md
   → summary.md
   → Jev v0.4
   → mapping.md + M
   → entry.md
↓
F. 设计 writing skill
↓
G. 做最小 QA
↓
H. 开第一批 10–25 条
```

如果在 Pilot 中发现流程问题：

> 先修规则和 skill，再批量。

不要在错误流程上扩大规模。

---

# 16. 一句话交班

> 《居家本草》现在已经完成研究方法 Pilot、Jev v0.4 和四阶段生产流程冻结。下一位 GPT Work 不需要重新设计研究方法，应该先完成 Concept skeleton + Entry Registry，然后用现有 6 个 Pilot 中的 3 个跑通 `research.md → summary.md → mapping.md → entry.md`，再进入每批 10–25 条的规模化生产。JEV_API_KEY 已经存在 GitHub Environment `API_KEYS` 的 Secret `JEV_API_KEY` 中；通过 GitHub Actions 注入使用，不要尝试读取或要求用户粘贴明文。
