# CHANGELOG

记录《居家本草》项目结构、方法和编纂系统的重要变化。单篇论文更新写入对应 research dossier，不在这里逐条记录。

## 2026-09-23

### Added

- 初始化 GitHub 仓库与 README。
- 建立《居家本草编纂凡例》v1.0 工作稿。
- 建立 E（现代人体证据）与 M（本草映射）双轨分级。
- 建立 R1/R2/R3 研究深度与证据饱和停止规则。
- 重整正式目录，采用唯一主条目 + 多标签。
- 建立 traditional parent index 与候选扩展文件。
- 建立 `home-materia-research` skill。
- 建立 `home-materia-jev-mapping` skill：以自然语言说明文档 + reasoning rules + five-shot 调用 Jev，输出四气、五味、五脏归经原生 score，并与独立 M grade 并列。
- 增加 D0–D4 证据距离。
- 增加中医 Concept Trace 与中医药公共数据库指南。
- 取消强制独立人工复审门槛，改为公开、可追溯的参考资料链。
- 参考 `goldengrape/vibe-coding-skill` 建立项目级规划体系。
- 建立最小 `okf/` 项目地图，索引项目目标、权威层级、标准生产链与当前路线。
- 冻结发布契约：GitHub Pages 网页电子书 + GitHub Release Markdown 包 + EPUB；全书不设图片。

- 完成 Pilot v1 六个样例：开心果、黑巧克力、珍珠奶茶、咖啡共享研究母页、酸奶、方便面。
- Pilot v1 总复盘通过：保留 R/D/E/M 与停止规则。
- 根据 Pilot 正式加入 Identity Revision、Composition & Exposure、Evidence-base overlap、Research Parent、Claim Mode 与消费者端服食法/加工变量。
- 建立 Jev 四气五味归经 rule + few-shot 技术 pilot：匿名 held-out、gold 隔离、原生概率留存、GitHub Actions secret 注入。
- Jev v0.1 保留为工程历史记录；其十二经输出空间与项目真实封闭契约不一致，不再用 v0.1 归经指标评价方案。
- 完成 Jev pilot v0.2：封闭输出字段正确，但 target 仍为结构化 packet；归经 recall 偏低。
- 重构 Jev pilot v0.3/v0.3.1：rules 改为症候→功能群→四气/五味/五脏归经的推理链，target 与 five-shot 改为自然语言说明文档；v0.3 #11 因 gold 投影和样本说明一致性问题标记 invalid。
- 完成 Jev pilot v0.3.1：采用五脏功能群工作投影并修正 reasoning-complete held-out，Actions #14 三次重复均达到四气 5/5、五味 5/5 exact、五脏归经 5/5 exact；不把该结果解释为生产准确率。
- 完成 Jev 现代食品 domain-transfer v0.1：冻结 v0.3.1 rules + five-shot，测试开心果、黑巧克力、咖啡、酸奶、方便面。确认 Jev 判定倾向与 M 证据等级应采用双轴展示：例如酸奶可同时记录“脾 Jev 0.58–0.61｜M-0”；不使用 M gate 压低或隐藏 Jev 结果，也不因 Jev score 提升 M。
- 完成 Jev v0.4：在每个五脏归经后增加一个 `阴- / 阴+ / 阳- / 阳+` 主方向 Choice；采用“语义上级连、计算上同步”的单次调用结构。5 味中药 held-out 三次重复中四气、五味、归经均 5/5，10 个有效归经主方向 10/10；现代食品迁移中开心果得到脾阳+/肾阳+，咖啡与酸奶得到脾阳+，黑巧克力与方便面无主归经。传统“疏肝、健脾、润肺、温中、化湿、生津”等下沉为原子分类后的派生用词。

### Current

- RM-TASK-001 项目级规划：done。
- RM-TASK-002 最小 OKF：done。
- Jev mapping current candidate：v0.4。
- 下一任务：建立精简后的原子概念骨架与 Entry Registry；随后进入正文 Pilot。