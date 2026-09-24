# Jev Output Contract

## 固定判定字段

### 四气

Jev Choice：

- 寒
- 凉
- 平
- 温
- 热

保存：

- selected choice；
- 五个原始 probabilities。

### 五味

五个独立 Noul：

- 酸
- 苦
- 甘
- 辛
- 咸

每项保存 0–1 原始值。

### 五脏归经

五个独立 Noul：

- 心
- 肝
- 脾
- 肺
- 肾

每项保存 0–1 原始值。

## Jev score 的含义

Jev score 是：

> 在当前 state、reasoning rules、five-shot、question schema 和具体 Jev model 下的模型判定倾向。

它不是：

- 经过经验校准的真实概率；
- 证据等级；
- M 等级；
- 临床置信度。

不要把 `0.76` 写成“76% 概率真实归肾”。

推荐写：

> Jev score 0.76

或多次运行：

> Jev score 0.75–0.76（3 次）

## M grade 的含义

M-I ～ M-0 来自 Research Dossier 的独立证据评价。

M grade 与 Jev score 并列，不互相修正。

允许：

```text
脾：Jev 0.58–0.61｜M-0
```

不允许：

```text
Jev 0.60，所以 M 从 M-0 升到 M-II
```

也不允许：

```text
M-0，所以把 Jev 0.60 改写成 0.20
```

## 重复运行

评估、方法学研究或重要条目推荐 3 次。

保存：

```yaml
score:
  values: [0.58, 0.60, 0.61]
  min: 0.58
  max: 0.61
  repeat_count: 3
```

不得只保留最好的一次。

## 0.5

Noul 的 0.5 可以用于：

- 快速显示“主要候选”；
- benchmark exact-set 计算。

0.5 不是：

- M 门槛；
- 证据门槛；
- 经验证的生产置信阈值。

研究记录中应保留五味和五脏所有原始 scores，包括 <0.5 项。

## 版本字段

每次判定至少记录：

```yaml
reasoning_version:
five_shot_version:
requested_model:
actual_model:
repeat_count:
target_document_ref:
target_document_hash:
```

若 reasoning rules、five-shot 或 actual model 改变，不应把新旧结果视为完全相同实验条件。
