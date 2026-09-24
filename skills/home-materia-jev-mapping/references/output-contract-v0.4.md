# Jev Output Contract v0.4-draft

> 基于 v0.3.1；新增五脏阴阳增减向量。
> 状态：draft，尚未替换 production baseline。

## 1. 四气

Choice：

- 寒
- 凉
- 平
- 温
- 热

保存 selected choice 与全部 probabilities。

## 2. 五味

五个独立 Noul：

- 酸
- 苦
- 甘
- 辛
- 咸

## 3. 五脏归经

五个独立 Noul：

- 心
- 肝
- 脾
- 肺
- 肾

## 4. 五脏阴阳方向

每个脏分别增加四个独立 Noul。

### 心

- `heart_yin_decrease`
- `heart_yin_increase`
- `heart_yang_decrease`
- `heart_yang_increase`

### 肝

- `liver_yin_decrease`
- `liver_yin_increase`
- `liver_yang_decrease`
- `liver_yang_increase`

### 脾

- `spleen_yin_decrease`
- `spleen_yin_increase`
- `spleen_yang_decrease`
- `spleen_yang_increase`

### 肺

- `lung_yin_decrease`
- `lung_yin_increase`
- `lung_yang_decrease`
- `lung_yang_increase`

### 肾

- `kidney_yin_decrease`
- `kidney_yin_increase`
- `kidney_yang_decrease`
- `kidney_yang_increase`

## 5. 为什么不用一个四选一 Choice

四个方向允许同时成立。

例如一个对象可能同时：

- 滋阴：阴+；
- 清热：阳-。

因此各方向独立保留原生 score。

## 6. 推理与展示

模型调用：

```text
同步
```

一次 request 同时输出归经和全部方向。

展示：

```text
可级连
```

例如：

```text
肝：0.82
  阳-：0.76
  阴+：0.18
  阴-：0.12
  阳+：0.09
```

低归经 score 的方向可以在读者界面折叠，但研究记录必须保留。

## 7. 结构一致性 QA

如果出现：

```text
某经 < 0.5
但该经某一阴阳方向 >= 0.5
```

记录：

```text
location_direction_disagreement: true
```

不自动修改任一 Jev 原始 score。

## 8. Jev score 与 M grade

规则不变：

```text
Jev score != M grade
```

例如：

```text
脾：Jev 0.61｜M-0
脾阳+：Jev 0.68｜M-IV
```

允许同时存在。

## 9. 后续习惯术语

“疏肝、健脾、安神、润燥、清热、温中、化湿、生津”等不作为一级 Jev 输出。

后续单独维护：

```text
五脏位置 + 阴阳方向
→ 习惯术语
```

该派生层不得改写原始 Jev score。
