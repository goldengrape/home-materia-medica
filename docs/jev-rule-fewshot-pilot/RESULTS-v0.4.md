# RESULTS v0.4 — 五脏归经 + 阴阳增减主方向

> 状态：validated candidate  
> architecture：语义上级连，计算上同步  
> prompt_version：`jev-tcm-rule-fewshot-v0.4`  
> fixture_version：`jev-tcm-pilot-fixtures-v0.4`  
> reasoning_version：`jev-tcm-reasoning-v0.4`  
> requested model：`jev-latest`  
> actual model：`jev-1.13.0`

## 1. v0.4 schema

一次 Jev request 共 16 个 questions：

```text
1 四气 Choice
5 五味 Noul
5 五脏归经 Noul
5 五脏主方向 Choice
```

每个 direction Choice 固定为：

```text
阴-
阴+
阳-
阳+
```

逻辑上：

```text
先归经
→ 再解释该经主方向
```

API 层不做两次级连，所有 questions 同步计算。

## 2. 为什么从 20 个 direction Noul 改成 5 个 Choice

早期 v0.4 draft 曾对每经设置：

```text
阴- / 阴+ / 阳- / 阳+
```

四个独立 Noul，共 20 个 direction fields。

design-check 发现：

- 同一经容易同时出现多个过 0.5 的方向；
- 虽然信息丰富，但一级 schema 变得臃肿；
- 与“先做原子分类，再附加传统习惯用词”的目标不一致。

因此最终 v0.4 改为：

> 每个归经一个四选一主方向 Choice，同时保留四项 probabilities。

混合效应仍可从 probability 分布看到。

## 3. 中药 regression

有效 run：

```text
Jev Yin-Yang Vector v0.4 Pilot #7
GitHub Actions run 35961677721
```

5 个 held-out，冻结配置重复 3 次。

| 指标 | Repeat 1 | Repeat 2 | Repeat 3 |
|---|---:|---:|---:|
| 四气 | 5/5 | 5/5 | 5/5 |
| 五味 exact | 5/5 | 5/5 | 5/5 |
| 五脏归经 exact | 5/5 | 5/5 | 5/5 |
| 有效归经主方向 | 10/10 | 10/10 | 10/10 |

说明新增 direction Choice 没有破坏 v0.3.1 已经稳定的四气、五味和归经分类。

### Held-out 主方向 gold

| 药物 | 归经主方向 |
|---|---|
| 胖大海 | 肺阳- |
| 余甘子 | 肺阴+、脾阴- |
| 黄精 | 脾阳+、肺阴+、肾阴+ |
| 草豆蔻 | 脾阳+ |
| 吴茱萸 | 肝阳+、脾阳+、肾阳+ |

### 胖大海设计修正

最初人工 gold 写成肺阴+。

Choice 首轮持续给出：

```text
肺阳- 0.53–0.57
肺阴+ 0.43–0.47
```

重新检查 target 文档：

```text
清热润肺
肺热
以清解肺热和缓解燥热为核心
```

因此主方向修订为肺阳-；肺阴+作为明确的次方向保留在 probability 分布。

这一例也说明 Choice 比单一硬标签更合适：可以保留“清热 + 润肺”的混合结构。

## 4. 现代食品 domain transfer

有效 run：

```text
Jev Food Domain Transfer v0.4 #2
GitHub Actions run 35961867966
```

第一次 run 因 Jev HTTP 529 `system_overloaded` 失败；加入仅针对暂时性过载的 2s / 4s / 8s 短重试后成功。

仍使用原有 5 个真实 Research Dossier，不修改 M grade。

### 开心果

三次：

```text
四气：温
五味：甘

脾：0.71–0.73
  主方向：阳+
  阳+：0.91–0.92

肾：0.75–0.76
  主方向：阳+
  阳+：0.86–0.88
```

对应说明文档中的“调中顺气、腰冷、肾虚痿弱”等功能方向。

归经证据等级仍按原 dossier 独立处理，不因方向稳定而升级 M。

### 黑巧克力

三次：

```text
四气：平
五味：无主要候选
五脏归经：无 >0.5 主候选
```

五个 direction Choice 仍有后台结果，但因为没有主归经，不在读者层解释。

### 咖啡

三次：

```text
四气：平
五味：苦

脾：0.59–0.63
  主方向：阳+
  阳+：0.91–0.92
```

与说明文档中的“健胃、食欲不振”功能方向一致。

现有 M grade 仍独立。

### 酸奶

三次：

```text
四气：平
五味：甘稳定；酸仍有重复波动

脾：0.61–0.63
  主方向：阳+
```

但 direction 分布明显比咖啡 / 开心果分散：

```text
阳+：0.40–0.45
阴-：0.29–0.35
阴+：0.25–0.26
阳-：0
```

这很符合其说明文档的混合性质：

- 发酵后更易消化 / 耐受 → 脾阳+方向；
- 消化乳糖 / 减少不耐受负担 → 可带阴-解释；
- 传统“酪”润燥、补虚背景 → 可带阴+解释。

因此读者层可显示“脾阳+为主”，研究层应保留完整方向 probabilities。

### 方便面

三次：

```text
四气：平
五味：无主要候选
五脏归经：无 >0.5 主候选
```

方向不进入读者层。

## 5. 当前解释

v0.4 支持以下分层：

```text
说明文档
↓
四气 / 五味
↓
五脏归经位置
↓
该经阴阳增减主方向
↓
传统习惯用词
```

例如：

```text
肝 + 阳-
→ 后续可派生“疏肝 / 平肝”等表达

脾 + 阳+
→ 后续可派生“健脾 / 温中”等表达
```

这些习惯词不再需要作为一级分类 ontology。

## 6. 与 M grade

不变：

```text
Jev score != M grade
```

例如：

```text
酸奶：
脾 0.61–0.63
主方向 阳+
M-0
```

可以同时成立。

Jev 表示模型在固定规则下如何分类；
M 表示当前证据链有多强。

## 7. 结论

v0.4 已完成：

- 中药 reasoning-complete 回归；
- 现代食品 domain transfer；
- direction schema 从 20 Noul 简化为 5 Choice；
- 529 暂时性过载重试；
- Jev score / M grade 双轴保持不变。

当前建议将 v0.4 作为 `home-materia-jev-mapping` 的现行分类版本。
