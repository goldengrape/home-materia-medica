# QA Log — 第二批茶饮十条

> 日期：2026-09-24  
> 当前阶段：搜、整、判、写完成；已保留冻结输入、Actions 原始输出、Mapping 与正文。  
> 研究深度：R1，探索性检索，不是系统综述。  
> 证据截止：2026-09-24。

## 本批条目

1. `fresh-milk-tea`（鲜奶茶）
2. `milk-foam-tea`（奶盖茶）
3. `fruit-tea`（水果茶）
4. `cheese-tea`（芝士茶）
5. `coconut-milk-tea`（椰乳茶）
6. `oat-milk-tea`（燕麦奶茶）
7. `brown-sugar-milk-tea`（黑糖奶茶）
8. `matcha-latte`（抹茶拿铁）
9. `hojicha-latte`（焙茶拿铁）
10. `bottled-unsweetened-tea`（无糖瓶装茶）

## 中间产物与冻结记录

- 搜：十份 `references/entries/<id>/research.md` 与共享父级 `references/shared/tea-base/research.md`；保留身份边界、检索词、证据卡、E/D、冲突、安全与停止理由。
- 整：十份 `references/entries/<id>/summary.md`，只概括 Research Dossier 支持的事实，不含 Jev 分类或 M。
- 冻结输入：`qa/tea-drink-summary-sha256.txt`；每份冻结摘要原文与 SHA-256 快照位于 `qa/jev-tea-batch/pre-freeze/<id>.json`。
- Jev 原生结果写入 `qa/jev-tea-batch/raw/<id>.json`。正式调用由 `.github/workflows/jev-tea-drink-batch.yml` 完成；工作流将 `secrets.JEV_API_KEY` 从 `API_KEYS` environment 注入，不把密钥写入日志、文件或参数。
- 判：mapping 保留原始 probabilities/Noul，再独立标 M；十条原始输出均为 Jev v0.4 请求、`jev-1.13.0` 实际模型、每条 16 个原生答案。
- 写：十篇正文引用具体研究并保留英文论文题名；有 DOI 的论文以 DOI 链接优先，并可并列中文题名。

冻结 manifest 共 10 条。摘要哈希见 manifest 与对应 pre-freeze JSON；运行器会在首次 API 调用前校验十条摘要文本与哈希完全一致。

## 本轮检索发现与边界

- **抹茶拿铁：** Monobe、Nomura 与 Ema 2021 年小样本双盲平行先导试验，18 人同意参加、13 人纳入分析；每天两份粉末抹茶拿铁或焙茶拿铁、持续两周。状态焦虑与唾液皮质醇没有显著组间差异；唾液 α-淀粉酶只提供探索性替代指标信号。正文不写成已证明的减压效果。英文题名及 DOI 留在 research 与 entry 参考文献。
- **芝士茶：** Kurniati 与 Yuliani 2022 年 32 只小鼠实验；只作为 E-D 动物线索，不推成人体血糖或糖尿病效果。
- **燕麦奶茶：** Qin 等 2023、2024 年模型体系/体外消化研究，结果依赖模型配方；不是饮用人体试验，按 E-D 机制或模型信号收录。
- **无糖瓶装茶：** Kaku 等 2024 年实验室筛查，在部分近中性 pH 绿茶样品中观察到接种唾液细菌生长。该实验不测未开封产品货架期，也没有消费者疾病终点；不能据此泛化到所有商品。
- **其他复合品类：** 香港 CFS/Consumer Council 2018 样本可说明若干具体市场品类的组成范围，但混合奶盖组、特定果茶样本及混合预包装茶样本均未被误写为全市场或目标子类的统一值。
- 所有“本轮未找到”仅指 R1 探索范围，不表述为全球不存在研究。共享茶叶证据保留为间接背景，不移植到复合饮品。

## 搜、整检查

- [x] 十份 identity、配方变量、组成/实际暴露及身份不确定性已写入 research。
- [x] 保留传统茶母本并明确它不是现代复合饮品的直接古籍记载。
- [x] 保留支持、阴性/未显著、替代解释和特殊设计限制。
- [x] 新增抹茶拿铁先导试验、小鼠芝士茶、燕麦奶茶体外模型与瓶装茶微生物筛查的准确证据距离。
- [x] 关键现代论文保留英文题名；存在 DOI 时附 DOI 链接；摘要/全文可得范围单独说明。
- [x] 冻结前已运行 Python 语法检查与摘要快照生成。
- [x] Jev v0.4 原生结果完整性与实际模型版本：10/10 原始 JSON；各含 1 次运行、16 项原生答案；实际模型均为 `jev-1.13.0`。
- [x] 十份 mapping 的 M 后置评注与写作交接：十份均含完整四气、五味、五脏归经/方向原始分布、M 注释、summary SHA 与 raw 引用；未改写原始 JSON。
- [x] 十份正文和跨层追溯检查：每篇均连到 research、summary、mapping；参考文献保留英文题名，有 DOI 者附 DOI 链接。
- [x] 自动化验收：manifest、冻结摘要文本/SHA 快照与 raw 输入 SHA 逐项一致；五个生产脚本 Python 语法检查通过。

## Actions 运行结果

- Workflow：`Jev tea drink batch v0.4`，run `35973926000`，结论 `success`，head commit `194ebfeb3ed65c8660322f4c17f570119752d569`。
- Artifact：`jev-tea-drink-native-v0.4`，ID `10797147988`，SHA-256 `453f855355f13f0151b1fd59e333029a333f86aade41b8cfc77eb9fb35b49584`。
- 原始输出：10 个 JSON，10/10 的 `summary_sha256` 与 manifest 和 pre-freeze 快照一致；每条有 16 项原生答案、`actual_model: jev-1.13.0`。
- 未记录或提交 API secret；secret 仅由 GitHub `API_KEYS` environment 注入 Actions。
