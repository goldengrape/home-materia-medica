# 十项条目四阶段测试｜2026-09-24

## 批次与已保存的中间结果

| 条目 | 搜 `research.md` | 整 `summary.md` | 判 `mapping.md` | 写 `entries/*.md` |
|---|---|---|---|---|
| pistachio 开心果 | 既有 R2，ready | 本轮新增，待引用复核 | 未运行 | 未进入 |
| dark-chocolate 黑巧克力 | 既有 R3，ready | 本轮新增，待引用复核 | 未运行 | 未进入 |
| pearl-milk-tea 珍珠奶茶 | 既有 R2，ready | 本轮新增，待引用复核 | 未运行 | 未进入 |
| yogurt 酸奶 | 既有 R2，ready | 本轮新增，待引用复核 | 未运行 | 未进入 |
| instant-noodles 方便面 | 既有 R2，ready | 本轮新增，待引用复核 | 未运行 | 未进入 |
| paper-filtered-coffee 纸滤手冲黑咖啡 | 新增 R1，preliminary；另有共享母页 | 新增，未冻结 | 未运行 | 未进入 |
| oat-milk 燕麦奶 | 新增 R1，preliminary | 新增，未冻结 | 未运行 | 未进入 |
| kombucha 康普茶 | 新增 R1，preliminary | 新增，未冻结 | 未运行 | 未进入 |
| sugar-free-cola 无糖可乐 | 新增 R1，preliminary | 新增，未冻结 | 未运行 | 未进入 |
| whey-protein-powder 乳清蛋白粉 | 新增 R1，preliminary | 新增，未冻结 | 未运行 | 未进入 |

## 阶段门与实际阻塞

1. 新增五项只有首轮 R1 证据地图，尚未完成关键全文、安全与近年反证审计；不能标 `research_ready`。既有五份摘要也需按原底稿逐项校对后冻结并记录 hash。
2. `docs/生产流程.md` 的判阶段明确要求对冻结 `summary.md` 使用 Jev v0.4，保存 16 项原生输出、actual model 和全部概率，然后才评 M。本环境未配置 `JEV_API_KEY`；没有任何真实 API 输出。本批次不能生成 `mapping.md` 的数值或冒称 Jev 已运行。
3. 写阶段只能消费上述真实 mapping 与经核验的 research/summary。为遵守阶段门，尚未创建十篇正式正文；文中不把此前 pilot 中的 v0.3.1/v0.4 测试 fixture 结果移植到新摘要上。

## 下一执行顺序

逐项核源并冻结 summary → 保存 SHA-256 → 以每份 summary 作唯一目标文本执行 Jev v0.4（10 项各保留原生 JSON 和模型版本）→ 回查 research 为每个分类命题标 M → 写正文及 Claim Ledger → 十项交叉 QA。先完成五个既有底稿条目；新增五项在其研究门通过后继续。

本轮为十份说明文档保存了当前快照的 SHA-256：`qa/ten-entry-summary-sha256.txt`。`scripts/run_jev_ten_batch.py` 在读入该清单时会校验内容，一旦摘要变更必须重新生成清单；它仅在 `JEV_API_KEY` 可用时运行，并逐项保存原生 JSON，不自动生成 M 或正文。对新五项，当前 hash 只是工作快照，不代表已过“整 → 判”阶段门。
