# catalog/

本目录维护《居家本草》的收录边界与条目身份。

## 文件分工

- `收录总目录.md`：纸书阅读顺序与正式收录范围。
- `传统母条索引.md`：已有传统本草 / 食疗记录、主要用于参照的基础食材。
- `候选扩展.md`：尚未正式纳入主目录的候选方向。

## 主条目与标签

纸书目录采用单一路径；研究后台允许多标签。

例如：

- 康普茶：主条目归“乳酪与发酵部 / 发酵食品”，同时可标记 `饮品`、`茶`、`发酵`。
- 冻酸奶：主条目归“乳酪与发酵部 / 乳与酸乳”，同时可标记 `冷甜`、`乳品`、`发酵`。
- 燕麦拿铁：主条目归“饮品部 / 咖啡诸品”，后台可同时关联咖啡、燕麦奶和早餐 / 通勤场景。

这样避免同一食品因多个分类重复建立研究资料。

## 后续元数据建议

每个正式条目最终建议有稳定 ID，并记录：

```yaml
id:
name:
aliases:
volume:
section:
tags: []
entry_type: ingredient | processed_food | composite_food | beverage | supplement | scene
parent_entries: []
related_entries: []
research_depth: R1 | R2 | R3
status: planned | researching | drafting | review | published
evidence_cutoff:
entry_path:
```

研究深度和证据规则见 `docs/居家本草编纂凡例-v1.0.md`。
