# skills/

本目录保存《居家本草》的可复用编纂工作流。

## 当前 skills

- [home-materia-research](./home-materia-research/SKILL.md)：单个食品 / 饮品 / 现代加工品 / 生活场景的科研检索、证据评估、本草映射准备与研究底稿生成。
- [home-materia-qi-channel-estimator](./home-materia-qi-channel-estimator/SKILL.md)：读取研究底稿，按已校准的文本算法估计四气分布与归经编辑置信度，并把主候选、次候选及不确定性传给正文写作层。

## 设计原则

研究与写作分离：

1. **research skill** 负责对象定义、检索、证据卡、风险偏倚、E 等级、M 映射候选、停止判断；
2. **qi-channel estimator** 在研究底稿之上估计四气与归经置信度，不自行补造研究证据；
3. 后续 **writing skill** 再把研究结果写成正文；
4. 不允许为了正文好看而反向修改研究结论。
