# Pilot QA — 珍珠奶茶 R2

> 日期：2026-09-23  
> 对应：`references/entries/pearl-milk-tea/research.md`

## 1. Pilot 结果

状态：**research_ready / sparse_evidence**

这是第一个因为“直接人体效应证据不足”而完成的 Pilot。

## 2. 关键方法学发现

### QA-MT-001｜Identity 必须能推翻 Pilot 自己的命名

原始样例写“奶茶”。检索后确认这不是稳定研究对象，因为鲜奶茶、植脂末奶茶、奶盖茶、珍珠奶茶差异过大。因此正式收窄为珍珠奶茶 / pearl milk tea。建议后续 registry 不保留泛化 `milk-tea` 主 entry。

### QA-MT-002｜现代食品有时“组成证据 > 疗效证据”

珍珠奶茶的长期临床 outcome 很少，但对糖、能量、caffeine、serving size、toppings 可以有非常直接的 D0 市场证据。这说明 Research Dossier 不应该只围绕“功效”组织。

### QA-MT-003｜E-0 不等于信息贫乏

可以同时成立：

- “这杯饮料通常含多少糖”——证据很强；
- “长期喝是否导致糖尿病”——直接证据 E-0。

如果没有 E / D 分离，很容易用前者偷换成后者。

### QA-MT-004｜generic SSB evidence 是 D2

珍珠奶茶常符合 SSB 定义，但 SSB meta-analysis 不等于 pearl milk tea-specific effect。

### QA-MT-005｜“炮制”概念在现代复合食品中很有解释力

少糖、去珍珠、换奶、杯量改变，会显著改变真实暴露。现代“炮制变量”可能比静态“这个食品是什么性”更有用。

### QA-MT-006｜“冰”不等于“寒”

冷饮温度是 serving condition；如果未来正文写“冰奶茶寒凉”，必须区分物理温度与本草性寒。

### QA-MT-007｜“甘腻生湿”最容易成为未经验证的套话

高糖、高脂、大份量确实存在，但直接写“甘腻碍脾、生湿生痰”仍跨过中间证据链。当前最多 M-IV。

## 3. 对全局模板的建议

经过前三个 Pilot，建议正式加入：

- `identity_revision`：研究是否改变了条目边界或 canonical ID；
- `evidence_base_overlap`：多个 Meta / review 是否共享同一批基础研究；
- `evidence_directness_note`：高质量研究是否因制剂/剂量离目标食品较远；
- 复合食品增加 `composition_evidence`；
- 复合食品增加 `processing_or_customization_variables`。

暂时不新增新的“组成证据等级”，避免系统膨胀；组成证据先按来源与直接性记录即可。

## 4. 一句话结论

> 珍珠奶茶这个条目最不该做的事，就是把“糖有风险、茶有多酚、奶有营养、咖啡因能提神”四套文献拼起来，假装我们已经研究过“珍珠奶茶本身”。