# Visual checklist

## What goes where

For each Skill, prepare three complementary assets: a **1:1 card** to answer “Why would I use this?”, a **short flowchart** to answer “What happens next?”, and an **output preview** to answer “What do I get?”. Keep instructions, supported inputs, installation, links, and complete examples in searchable README text. Do not use images as the only source of instructions. All artwork labels and captions are English; bilingual README prose can link to the same assets.

The v1.0.0 [visual gallery](visual-gallery.md) groups these three assets for every Skill. Spatial Omics Paper Reading offers a compact example of how the card, workflow, and synthetic evidence preview work together.

## What each Skill shows

| Skill | Square card: main promise | Flowchart: what matters | Output preview: what to show | Keep in native text |
|---|---|---|---|---|
| Spatial Omics Paper Reading | Turn a plant spatial-omics paper into an evidence-linked reading brief. | Identify the source, check access, trace figures and methods, and record what could not be verified. Show the partial-source path only if it changes what can be reported. | A synthetic reading report excerpt with one evidence-linked claim, one figure reading note, and one unverified item. | How to provide sources; full report template; source-access limitations. |
| Plant Omics Preflight | Check readiness without starting the analysis. | Scope the task, check inputs, and route missing evidence or unauthorized execution to a stop or targeted request. | A compact readiness memo with one ready item, one blocker, and a decision status. | Required input manifest, scope vocabulary, and distinction between readiness and authorization. |
| Plant Spatial Omics Analysis | Choose the next defensible analysis for a plant spatial dataset. | Route the research question to the relevant modality, check evidence, then return a plan or proceed only within authorized scope. Do not draw independent modalities as mandatory serial steps. | A synthetic analysis plan entry showing a comparison, independent unit, and a success or stop rule. | Modality-specific checks, data caveats, and interpretation limits. |
| Analysis Explainer | Explain a saved figure without rerunning the analysis. | Locate evidence, explain the method, separate claims, and deliver the Figure Summary. | One synthetic Figure Summary row with an evidence pointer and a limitation. | Schema, missing-value conventions, and how to interpret n and uncertainty. |
| Scientific Figure Standard | Make a clearer, reproducible figure without changing results. | Lock the source, render the figure, review exports, and deliver figure plus QA. Keep a pending technical review distinct from scientific approval. | A schematic versioned output manifest showing preview, final export, and review status. Do not present the schematic as a checked rendering. | Export settings, modality-specific scale and orientation checks, and source/configuration records. |
| Plant Omics Thesis Writing | Turn verified outputs into evidence-aligned thesis prose. | Identify the requested section, map evidence to claims, draft, and verify numbers and citations. | A synthetic results paragraph with a visible link to the source table, paired with a bounded claim. | Citation rules, optional institution or journal formatting requirements, and the full draft. |

## Repository visuals

The [hero banner](../assets/release/hero-banner.png) is the repository-wide sharing image, separate from the six square cards. Its 1280 × 640 dimensions follow [GitHub’s social-preview guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview). The [suite map](../assets/release/suite-architecture.png) shows optional handoffs. The [card grid](../assets/release/cards-overview.png) provides a compact overview.

## Acceptance gates

- At phone width, readers can identify a card's title and outcome, and follow the diagram without zooming. Check light and dark surrounds. If labels become too small, reduce the amount of content rather than shrinking type.
- Verify diagram labels against the final Skill. Label meaningful branches, avoid crossing connectors, and never rely on color alone to communicate a decision.
- Keep editable source and browser-friendly exports. Give informative English alt text and a plain-text equivalent for any operational logic. Validate image links from both README versions.
- Use either clearly labeled synthetic demonstration outputs or factual, authorized public examples. The synthetic label belongs in the preview itself. Do not present example values as measured findings or fabricate metrics, claims, or citations.
- Check the rendered image and editable source against the corresponding Skill version. Use only material cleared for public use, and do not present preview visuals as proof of a Skill run or scientific approval.
