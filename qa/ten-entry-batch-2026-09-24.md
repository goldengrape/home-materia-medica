# 十项条目四阶段测试｜2026-09-24

## 批次与已保存的中间结果

| 条目 | 搜 `research.md` | 整 `summary.md` | 判 `mapping.md` | 写 `entries/*.md` |
|---|---|---|---|---|
| pistachio 开心果 | 既有 R2 | 冻结 | 完成 | 工作稿 |
| dark-chocolate 黑巧克力 | 既有 R3 | 冻结 | 完成 | 工作稿 |
| pearl-milk-tea 珍珠奶茶 | 既有 R2 | 冻结 | 完成 | 工作稿 |
| yogurt 酸奶 | 既有 R2 | 冻结 | 完成 | 工作稿 |
| instant-noodles 方便面 | 既有 R2 | 冻结 | 完成 | 工作稿 |
| paper-filtered-coffee 纸滤手冲黑咖啡 | R1；复用共享母页并重评 D | 冻结 | 完成 | 工作稿 |
| oat-milk 燕麦奶 | R1 | 冻结 | 完成 | 工作稿 |
| kombucha 康普茶 | R1 | 冻结 | 完成 | 工作稿 |
| sugar-free-cola 无糖可乐 | R1 | 冻结 | 完成 | 工作稿 |
| whey-protein-powder 乳清蛋白粉 | R1 | 冻结 | 完成 | 工作稿 |

## 初始阶段门与阻塞（已续跑）

1. 新增五项只有首轮 R1 证据地图，尚未完成关键全文、安全与近年反证审计；不能标 `research_ready`。既有五份摘要也需按原底稿逐项校对后冻结并记录 hash。
2. `docs/生产流程.md` 的判阶段明确要求对冻结 `summary.md` 使用 Jev v0.4，保存 16 项原生输出、actual model 和全部概率，然后才评 M。本环境未配置 `JEV_API_KEY`；没有任何真实 API 输出。本批次不能生成 `mapping.md` 的数值或冒称 Jev 已运行。
3. 写阶段只能消费上述真实 mapping 与经核验的 research/summary。为遵守阶段门，尚未创建十篇正式正文；文中不把此前 pilot 中的 v0.3.1/v0.4 测试 fixture 结果移植到新摘要上。

## 原定执行顺序（已完成至工作稿）

逐项核源并冻结 summary → 保存 SHA-256 → 以每份 summary 作唯一目标文本执行 Jev v0.4（10 项各保留原生 JSON 和模型版本）→ 回查 research 为每个分类命题标 M → 写正文及 Claim Ledger → 十项交叉 QA。先完成五个既有底稿条目；新增五项在其研究门通过后继续。

本轮为十份说明文档保存了当前快照的 SHA-256：`qa/ten-entry-summary-sha256.txt`。`scripts/run_jev_ten_batch.py` 在读入该清单时会校验内容，一旦摘要变更必须重新生成清单；它仅在 `JEV_API_KEY` 可用时运行，并逐项保存原生 JSON，不自动生成 M 或正文。对新五项，当前 hash 只是工作快照，不代表已过“整 → 判”阶段门。

## 2026-09-24｜环境 secret 接入后的续跑

用户已在 GitHub `API_KEYS` environment 配置 `JEV_API_KEY`。分支 `feat/ten-entry-batch-2026-09-24` 的 workflow 以 `environment: API_KEYS` 和 `${{ secrets.JEV_API_KEY }}` 将密钥只交给步骤环境；不提交密钥。第一轮输入未冻结的结果保留在 `qa/jev-ten-batch/pre-freeze/`，只作方法对照。

新增五项按 R1 限定核心问题、标记摘要可得文献和稀疏证据的停止范围；十份 summary 随后冻结，哈希清单更新。正式输入运行：[GitHub Actions #35968069070](https://github.com/goldengrape/home-materia-medica/actions/runs/35968069070)。十份原生响应保存在 `qa/jev-ten-batch/raw/`，逐项通过输入 hash、16 字段和 actual model `jev-1.13.0` 核对。一次生产调用，不作挑选、平均或校准。

每项 `mapping.md` 保存五项四气概率、五味和五脏 Noul、每经方向四概率，并在原生结果之后独立评 M。正文在 `entries/`；交接核对见 `qa/ten-entry-claim-ledger.md`。这是十项流程测试的工作稿，新增 R1 条目仅覆盖限定问题，不代表出版审定。
