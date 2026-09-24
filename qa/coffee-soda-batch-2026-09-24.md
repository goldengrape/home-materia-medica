# QA Log — 第四批咖啡与碳酸饮品十条\n\n> 日期：2026-09-24\n> 研究深度：R1 定向检索，不是系统综述。\n> 证据截止：2026-09-24。\n\n## 本批目录顺序\n\n1. caramel-macchiato（焦糖玛奇朵）\n2. oat-latte（燕麦拿铁）\n3. coconut-latte（椰乳拿铁）\n4. instant-coffee（速溶咖啡）\n5. three-in-one-coffee（三合一咖啡）\n6. decaf-coffee（无咖啡因咖啡）\n7. cola（可乐）\n8. lemon-soda（柠檬汽水）\n9. soda-water（苏打水）\n10. sparkling-water（气泡水）\n
## 中间产物

- 搜：十份 references/entries/<id>/research.md；咖啡条链接 coffee-base，软饮条链接 soft-drink-base。
- 整：十份 summary.md 只复述底稿事实，不含 Jev、四气五味归经或 M。
- 冻结：qa/coffee-soda-summary-sha256.txt 与 qa/jev-coffee-soda-batch/pre-freeze/<id>.json 保存摘要 SHA-256 和原文。
- 判：workflow 使用 environment API_KEYS 与 secrets.JEV_API_KEY；首次 API 请求前校验 manifest 与快照；raw JSON 不加 M、不改分数。
- 写：Mapping 保存 probability/Noul、confidence、方向；正文回链 research、summary、mapping。参考文献保留英文题名与可核实 DOI。

## 身份红队

- 焦糖玛奇朵与 espresso macchiato 区分。
- 燕麦/椰乳拿铁与植物饮研究分层；奶基底不是成品临床试验。
- 纯速溶咖啡与三合一预混包分别立条。
- 常规可乐与已有无糖可乐条目分开。
- 柠檬汽水实验只代表指定品牌与体外条件。
- 苏打水按标签确认矿物盐/碳酸氢盐；气泡水区分原味与调味。
 
## 初次运行记录

- 2026-09-24，runs 35980464759、35980802729、35981400606 均在 Research Dossier 阶段因配置缺少 `queries` 字段中止；三次 `API_KEYS/JEV_API_KEY` 预检均成功。冻结、Jev 分类、Mapping 与正文阶段未执行，没有产生分类 raw JSON。补齐定向检索词后重跑。

## Actions 运行结果

- Workflow run: 35981638241, successful; API key sourced from Environment API_KEYS secret JEV_API_KEY.
- Artifact ID: 10800875453; name jev-coffee-soda-native-v0.4.
- Ten raw outputs match frozen summary hashes. Actual model(s): jev-1.13.0; each record has one run and 16 native answers.
- Per-file raw JSON SHA-256: qa/jev-coffee-soda-batch/native-json-sha256.txt.
- Ten Mapping files preserve probabilities, confidence and directions; ten bodies link research, summary and mapping and retain English paper titles and verified DOI links.

## 并行运行与工件保留

- Push 运行 35981632115 完成研究、冻结与分类，并上传原始结果工件 10799982550；写回分支时与 PR 运行并发，因 non-fast-forward 被拒。工件保留 30 天，未丢弃。
- PR 运行 35981638241 成功写回本批规范文件；原始结果工件 10800875453 与逐条 raw JSON 同时保留。Mapping、manifest 与正文均以此 run/artifact 为引用。
