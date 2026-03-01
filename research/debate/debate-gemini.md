# Gemini's Debate Response: Where We Got It Right, Where They Got It Wrong, and What We All Missed

---

## 1. What My Report Uniquely Brought to the Table

Neither Claude nor Codex grappled seriously with the single most important question facing Merleau: **what happens when the moat evaporates?**

My report was the only one to conduct a rigorous risk analysis with probability-weighted timelines. I identified that Lovable, Bolt, and v0 adding video upload is HIGH probability within 12-18 months, and that Claude/Gemini adding native video-to-spec capabilities is VERY HIGH probability. Claude's report breezes past this -- it mentions the competitive landscape is "empty" as though that is a durable fact rather than a 6-month window. Codex ignores the question entirely, content to catalog legacy systems as though the demand side is the hard part. Demand is not the problem. Defensibility is the problem.

My report also provided the only concrete unit economics analysis. I calculated that Gemini 2.5 Flash costs roughly $0.01-$0.03 per 5-minute screencast analysis, yielding COGS of $0.30-$0.90 per Pro user at 30 analyses/month against a $29/month price point. That is 97%+ gross margin. Neither Claude nor Codex touched cost structure, which means neither of them actually modeled whether this business works financially. A strategy without a P&L is a wish list.

The Figma analogy was mine, and it is the most important strategic frame in any of the three reports. Figma deliberately abandoned code generation and doubled down on being the best design tool, building bridges to code rather than generating it. The parallel to Merleau is exact: be the best at video understanding, build bridges to code generation platforms, do not try to compete with Lovable's $200M ARR code generation engine. Claude gestures at this distinction but never commits to the analogy with the same force.

Finally, I was the only one to address the IP and legal risk of "app cloning" with specificity -- citing trade dress protection, copyright scope for UI elements, and the critical distinction between standard UI patterns and protectable design. Codex uses the word "cloning" freely throughout its report without once acknowledging the legal exposure this creates. That is reckless for a strategy document.

---

## 2. Where Claude and Codex Got It Wrong

### Claude's Overconfidence in the Competitive Vacuum

Claude states: "The competitive landscape is empty. No one offers a dedicated video-to-specification product." This is dangerously misleading. Google already demonstrated the exact Merleau pipeline -- video to spec to code -- using Gemini 2.5 Pro in their "Video to Learning App" demo. Kimi K2.5 from Moonshot AI turns video into working front-end code and is open-source. The `screenshot-to-code` project has experimental video support. The landscape is not empty. It is early. There is a critical difference between those two statements.

Claude also overstates the Thoughtworks precedent. Yes, their "Black Box to Blueprint" project validates the concept, but Claude frames it as "only a bespoke consulting engagement," implying it is far from productization. In reality, the Thoughtworks team used Gemini 2.5 Pro with a Playwright MCP agent -- off-the-shelf tools. If a five-person consulting team can build this in two weeks with existing tools, the barrier to entry for competitors is lower than Claude implies.

### Codex's Segment Analysis Is Wide but Shallow on Strategy

Codex produced an excellent catalog. The legacy system segments -- SAP GUI, Oracle Forms, AS/400 green screens, Lotus Notes -- are well-researched with genuine domain expertise. The concrete app examples (15 of them, tiered by complexity) are the most actionable artifact across all three reports. I did not produce anything comparable in terms of specific use cases, and I acknowledge that.

But Codex makes a fundamental strategic error: it recommends launching Phase 1 targeting developers with **code output** (React/Next.js components, Tailwind CSS). This directly contradicts the strongest finding across all three reports -- that end-to-end code generation is the wrong play. Codex's own data shows that existing code generators capture "maybe 60-70% of the design, missing interaction patterns, state management, responsive behavior, and edge cases." If purpose-built code generators from Lovable and Bolt, with hundreds of millions in funding, only hit 60-70%, why would Merleau -- a startup with a fraction of those resources -- do better by tacking code generation onto video understanding? Codex identifies the problem and then recommends walking straight into it.

Codex also cites Lovable's valuation at $6.6B and $206M ARR (from a later TechCrunch article), while my report cited the earlier $1.8B valuation and ~$50-100M ARR. The discrepancy suggests Lovable's growth has been even more explosive than I modeled, which **strengthens** the case for not competing with them on code generation. The faster Lovable grows, the worse the odds of out-generating them.

### Both Reports Underweight the "Thin Wrapper" Existential Risk

Claude mentions that the MCP server for Gemini video understanding already exists (`@ugarchance/mcp-gemini-video-understanding`) and notes it "bridges Gemini's video API into Claude Code's workflow." But Claude does not follow this thread to its conclusion: if anyone can pip-install a bridge between Gemini's video API and Claude Code, then Merleau's core pipeline is replicable in an afternoon. My report explicitly called this the "thin wrapper" threat and outlined five specific mitigation strategies (proprietary spec templates, data flywheel, workflow depth, integration network effects, brand/community). Claude acknowledges the technology overlap but does not treat it as the existential concern it is.

---

## 3. Where the Others Were Stronger

### Claude: Superior Landscape Architecture

Claude's report is the best of the three as a landscape overview. The side-by-side comparison table of coding agents (Claude Code, Codex, Copilot, Cursor/Windsurf, Devin) with their input methods, autonomy levels, and best-use cases is something I should have produced. My report jumped straight to strategic analysis without adequately mapping the ecosystem players. Claude's architecture diagram showing the hybrid spec-to-integration pipeline is also cleaner and more actionable than my phased roadmap.

Claude also identified a competitor I missed: **Stitch by Google Labs**, a text/images/wireframes-to-UI tool powered by Gemini. If Google Labs is already building in adjacent space, the probability of Google productizing a video-to-spec tool just went up further.

### Codex: The Legacy Modernization Angle Is a Goldmine

Codex identified the legacy modernization market ($20.55 billion in 2025, projected to $81.24 billion by 2034) as the highest-value application for Merleau. This is the single most important insight across all three reports that I underweighted. My report focused on developer tools and agency workflows -- valuable but crowded. Codex's insight that government legacy systems "often have no documentation, no source code access, and no original developers available" and that "the only way to understand what the system does may be to record someone using it" is a perfect product-market fit argument for video-to-spec. Video is not just a better input modality in this context -- it is the **only viable** input modality.

Codex's persona analysis is also more nuanced than mine. The distinction between coders wanting code components and non-coders wanting PRDs -- with the "same engine, different interface" framing -- is elegant and practical. I treated the coder/non-coder divide as a sequencing question (who to target first) without adequately addressing how the product experience should differ between them.

The specific examples (SAP transaction ME21N, Oracle Forms inventory management, Bloomberg Terminal workflows) make the abstract opportunity concrete in a way my report does not. A pitch deck drawing from Codex's examples would be more compelling than one drawing from my strategic frameworks.

---

## 4. Revised Thesis

Reading all three reports together, here is what I would change:

**The synthesis missed the enterprise legacy modernization positioning.** All three reports converge on "start with developers, expand to non-coders, eventually reach enterprise." But Codex's legacy systems data suggests a parallel track that none of us fully articulated: **Merleau should pursue enterprise legacy modernization as a second beachhead from month 6, not month 12+.** The $81 billion legacy modernization market does not care about $29/month developer subscriptions. It cares about $50,000+ project-based engagements where video-to-spec replaces two weeks of consulting discovery. The unit economics are completely different and dramatically more favorable.

**The pricing model should be bifurcated earlier than any report suggested.** Developer PLG at $29/month AND enterprise project-based pricing at $5,000-$20,000 per legacy system analysis should launch in parallel, not sequentially. These are different buyers, different channels, different value propositions. The developer tier builds brand and community. The enterprise tier builds revenue and defensibility.

**The data flywheel is the only real moat, and all three reports underinvest in it.** My report mentioned it. Claude's report did not. Codex's report did not. But the data flywheel -- learning which spec structures produce the best downstream code, which video analysis patterns correlate with user satisfaction, which component taxonomies are most useful -- is the only asset that gets more defensible over time. Everything else (integrations, brand, community) is replicable. A curated dataset of "video -> optimal spec -> successful app" triples is not. The product roadmap should be designed from day one to capture this data, with explicit feedback loops from downstream code generation results back into spec quality optimization.

**The name "app cloning" should be killed immediately.** Codex uses it liberally. Claude is more careful but still flirts with it. My report explicitly recommended against it, and I double down: the product should never use the word "clone." The positioning is "video-to-spec" or "screencast analysis for development." Legal risk aside, "cloning" implies commoditization and invites dismissal. "Analysis" implies intelligence and invites premium pricing.

The bottom line: Merleau's real opportunity is not building a better screenshot-to-code tool with video input. It is becoming the **standard interface between human-demonstrated workflows and the entire AI coding ecosystem** -- the Figma of video understanding for software development. That requires owning the spec layer, not the code generation layer, and building data assets that compound over time. The three reports converge on this thesis. The debate is about emphasis, timing, and how honestly we face the risks.

---

*Gemini Agent -- February 2026*
