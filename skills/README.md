# skills/

本目录保存《居家本草》的可复用编纂工作流。

## 当前 skills

- [home-materia-research](./home-materia-research/SKILL.md)：单个食品 / 饮品 / 现代加工品 / 生活场景的科研检索、证据评估、本草映射准备与研究底稿生成。
- [home-materia-jev-mapping](./home-materia-jev-mapping/SKILL.md)：读取已经完成的自然语言说明文档，用 Jev v0.4 reasoning rules + five-shot 输出四气、五味、五脏归经及每经阴-/阴+/阳-/阳+主方向，并与独立 M 等级并列记录。

## 设计原则

研究与写作分离：

1. **research skill** 负责对象定义、检索、证据卡、风险偏倚、E 等级、M 映射候选、停止判断；
2. **Jev mapping skill** 可以在 Research Dossier 完成后生成模型判定分数；Jev score 与 M grade 必须分开，不得反向修改研究证据等级；
3. 后续 **writing skill** 再把经审核的研究底稿和 Jev/M 双轴结果写成正文；
4. 不允许为了正文好看而反向修改研究结论。
