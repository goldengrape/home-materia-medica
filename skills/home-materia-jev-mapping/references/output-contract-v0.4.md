# Jev Output Contract v0.4-draft

> 语义上级连，计算上同步。
> 每个五脏归经新增一个主方向 Choice。

## 四气

`qi`：Choice

- 寒
- 凉
- 平
- 温
- 热

## 五味

5 个独立 Noul：

- `taste_sour`
- `taste_bitter`
- `taste_sweet`
- `taste_pungent`
- `taste_salty`

## 五脏归经

5 个独立 Noul：

- `meridian_heart`
- `meridian_liver`
- `meridian_spleen`
- `meridian_lung`
- `meridian_kidney`

## 每经主方向

5 个 Choice：

- `heart_direction`
- `liver_direction`
- `spleen_direction`
- `lung_direction`
- `kidney_direction`

每个 Choice 的固定值：

- 阴-
- 阴+
- 阳-
- 阳+

保存：

- selected choice；
- 四个原生 probabilities。

## 解释规则

归经 Noul = 位置倾向。

direction Choice = 如果讨论该经，最主要的作用方向。

两者在同一个 request 中计算，但展示时按归经组织。

例如：

```yaml
liver:
  meridian_score: 0.82
  direction:
    choice: 阳-
    probabilities:
      阴-: 0.10
      阴+: 0.12
      阳-: 0.70
      阳+: 0.08
```

如果 `meridian_liver` 很低，仍保存 `liver_direction`，但不把该方向单独当成读者结论。

## 混合效应

同一经可能同时具有多个方向。

v0.4 一级 schema 仍只选“主方向”，其余方向通过 Choice probabilities 保留。

因此：

```text
肺阴+ 0.55
肺阳- 0.40
```

可以解释为：

> 肺经主方向偏阴+，同时有较明显阳-次方向。

不需要 20 个独立 Noul。

## Jev score 与 M

继续：

```text
Jev score != M grade
```

不做 post-hoc probability correction。
