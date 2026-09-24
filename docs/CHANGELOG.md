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
- 完成 Jev pilot v0.1：四气 5/5，五味 micro-F1 0.857，归经 micro-F1 0.824；暂不设生产阈值，不引入概率修正函数。

### Current

- 当前工作分支：`plan/project-roadmap-v1`
- RM-TASK-001 项目级规划：done。
- RM-TASK-002 最小 OKF：done。
- 下一任务：RM-TASK-010 / RM-TASK-003 中医概念骨架；随后建立正式 Entry Registry。