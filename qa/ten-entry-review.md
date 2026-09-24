# 十项试写复核｜2026-09-24

## 输入与运行

- 10 个 ID 唯一，各有 `research.md`、冻结 `summary.md`、`mapping.md` 和正文。
- `summary.md` 哈希与正式 Jev artifact 中逐项一致；16 个答案键齐全，五气 Choice、五味/五脏 Noul、五经四方向 Choice 的原生分布均保存。
- Actions [run #35968069070](https://github.com/goldengrape/home-materia-medica/actions/runs/35968069070) 成功；requested model `jev-latest`，actual model `jev-1.13.0`；每项 1 次。此前 [run #35967877115](https://github.com/goldengrape/home-materia-medica/actions/runs/35967877115) 使用未冻结版本，保留在 `pre-freeze/`，不用于正式 mapping。
- 原生结果先保存，随后根据研究底稿逐项评 M；生成脚本没有按 M 改动 Jev score。

## 本轮方法观察

| 指标 | 本轮结果 | 解释边界 |
|---|---|---|
| 四气主要 Choice | 开心果温；其余九项平 | Choice 必须选一项；“平”常伴 M-0，不当作已经证实的食性 |
| 五脏 Noul ≥0.5 | 仅开心果脾 0.59 | 0.5 是展示线；其 M-0，未成为正文中的确定归经 |
| 低分方向 | 五经全部保留四项分布 | 低归经分数下的方向不写入读者结论 |
| 传统直录 | 开心果古籍有相异味性记录 | 传统事实与现代商品类推分层呈现 |

## 正文 QA

- 对每条正文检查本地 research/mapping 链接、食品身份与加工范围、支持与反证、安全提示、E/M 措辞；所有正文均为无图 Markdown。
- `qa/ten-entry-claim-ledger.md` 记录二十项核心命题及其 D/E/M 或事实类型。
- 原生输出是一次模型判断，不代表重复稳定性或经验校准概率。R1 新条目限其核心问题；引用全文未取得者按摘要可得处理，今后发现新关键试验应从“搜/整”重新开始并重新运行 Jev。
- 本批次是写作结构和流程的工作稿，尚未进行出版版式、EPUB 或全卷术语统一验收。
