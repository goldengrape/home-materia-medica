# skills/

本目录保存《居家本草》的可复用编纂工作流。

## 当前 skills

- [home-materia-research](./home-materia-research/SKILL.md)：执行“搜 + 整”，生成 `research.md` 与 Jev-ready `summary.md`。
- [home-materia-jev-mapping](./home-materia-jev-mapping/SKILL.md)：读取已经完成的自然语言说明文档，用 Jev v0.4 reasoning rules + five-shot 输出四气、五味、五脏归经及每经阴-/阴+/阳-/阳+主方向，并与独立 M 等级并列记录。

## 设计原则

统一生产流程：

```text
搜 → 整 → 判 → 写
```

1. **research skill** 负责“搜 + 整”：对象定义、检索、证据卡、D/E、安全、Concept Trace、停止判断和 `summary.md`；
2. **Jev mapping skill** 负责“判”：读取冻结的 `summary.md`，运行 Jev v0.4，再对分类逐项标 M，输出 `mapping.md`；
3. 后续 **writing skill** 负责“写”：根据资料与分类撰写正文，不重新研究或重分类；
4. 下游不得为了正文好看而反向修改上游事实、Jev 原始结果或 M。
