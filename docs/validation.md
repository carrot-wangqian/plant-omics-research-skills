# Validation

The Skills provide evidence-linked research workflows and guardrails. They are not a software pipeline or a substitute for scientific review. The research examples below use fictional inputs.

## Offline release checks

From the repository root, run:

```sh
python tools/validate_release.py
```

The validator checks the release layout, license, citation and Marketplace metadata, default Skill directories, Skill frontmatter, Markdown links, shared Figure Summary fixtures, visual formats and dimensions, and known private-data and draft-text patterns. Passing it does not establish scientific correctness or compatibility with a particular AI host.

## Remote installation and host discovery

Both [README installation routes](../README.md#quick-install) were tested on Windows on 2026-11-24. Each route started with a fresh project, an isolated user directory and an empty installer cache. The test used Node.js 24.15.0, Skills CLI 1.9.0, Codex CLI 0.171.0-alpha.13 and Claude Code 2.1.142.

| Version | Skills CLI installed | Codex enabled project Skills | Claude Code new-session commands | Claude Code plugin details |
| --- | ---: | ---: | ---: | ---: |
| [v1.0.0](https://github.com/carrot-wangqian/plant-omics-research-skills/releases/tag/v1.0.0) | 6 | 6 | 6 | 12 (each name twice) |
| [v1.0.1](https://github.com/carrot-wangqian/plant-omics-research-skills/releases/tag/v1.0.1) | 6 | 6 | 6 | 6 (each name once) |

The Codex check installed all six Skills with `npx skills add` and queried the app server's `skills/list` method for the project. The Claude Code check registered the remote marketplace, installed the plugin, queried `claude plugin details plant-omics-research-skills@plant-omics-research-skills` and read the command list from a new session. Both hosts reported zero Skills from this repository before installation. Each installed copy contained all six `SKILL.md` files and all 13 reference files, byte-for-byte identical to the tested revision.

In v1.0.0, Claude Code scanned the default `skills/` directory and also counted the six paths listed in the marketplace entry. The v1.0.1 entry uses the default scan alone. The first v1.0.1 remote installations used the same [implementation commit](https://github.com/carrot-wangqian/plant-omics-research-skills/commit/760196a17850e9197d9037134e34ecec95e26f74). Restoring the old path list in a disposable copy caused the offline validator to fail as expected. The [v1.0.1 release notes](https://github.com/carrot-wangqian/plant-omics-research-skills/releases/tag/v1.0.1) identify the final tested commit and archive checksum.

## Six documented dry runs

Reviewers followed the Skill instructions with synthetic inputs and checked what the instructions allowed them to conclude. These were task-level dry runs, not software reruns or tests of automatic Skill discovery.

| Skill | Synthetic input | Observed behavior |
| --- | --- | --- |
| [Paper Reading](../skills/spatial-omics-paper-reading/SKILL.md) | Usable untitled abstract; no figures | Marked the paper identity and figure details unverified; continued only with the supplied material. |
| [Preflight](../skills/plant-omics-preflight/SKILL.md) | Valid aggregate table; no overlay transform | Supported the aggregate description but blocked the spatial overlay. |
| [Spatial Omics Analysis](../skills/plant-spatial-omics-analysis/SKILL.md) | Reliable match, unmatched feature, measured zero, and alternative display scales | Kept the three feature states separate; changing the display contrast did not change the underlying values. |
| [Analysis Explainer](../skills/analysis-explainer/SKILL.md) | Resized screenshot and separate saved table | Reported the exact values as table facts; required a matching figure version and data layer before attributing them to the displayed panel. |
| [Scientific Figure Standard](../skills/scientific-figure-standard/SKILL.md) | Caption-only request with a missing final image | Checked the available evidence without rerunning or inventing an export; did not issue a technical pass. |
| [Thesis Writing](../skills/plant-omics-thesis-writing/SKILL.md) | Mismatched old/new totals and a proposed analysis in a Results draft | Required feature-set reconciliation before explaining the totals and kept proposed work separate from completed results. |

## Five reproducible smoke tests

To check behavior in your own AI host, start a fresh session, load the named Skill, give it the indicated material and request, and compare the result to the expectation. The checks are manual; they do not execute an analysis. Record your host/version and whether you explicitly loaded the Skill.

| Test | Input and request | Expected result |
| --- | --- | --- |
| 1. Preflight | Give the [four-row readiness example](../skills/plant-omics-preflight/references/readiness-record.md) and ask for a readiness memo, with no execution. | Keep the paired summary available, block the overlay because the transform is missing, and preserve Conditional and Not Applicable. Do not start analysis. |
| 2. Spatial analysis | Give the [paired-region decision example](../skills/plant-spatial-omics-analysis/references/decision-record.md) and ask which pairs enter the comparison and what the saved results support. | Report two of four eligible pairs, differences 2 and 4, and mean 3. Distinguish the missing pair from the QC exclusion. Do not replace missing with zero or report a p-value. |
| 3. Explainer and figure audit | Give the [synthetic TSV](../skills/analysis-explainer/references/synthetic-summary-source.tsv) and [Figure Summary example](../skills/analysis-explainer/references/figure-summary.md). Ask the explainer for a reading guide; separately ask the figure Skill to audit an export that has not been supplied. | The explainer reports 1.4 as the outer/inner ratio of mean relative signal, with biological n = 1 and no inferential claim. No rerender. The figure audit marks the missing export pending. |
| 4. Paper reading | Supply only this fictional excerpt: “In this fictional study, two leaf regions showed different signal patterns.” Ask for a brief including figure and method evidence. | Use only the text provided. Mark figures, detailed methods, and bibliographic identifiers unverified; do not fabricate any. |
| 5. Thesis writing | Use the [adjacent-section example](../skills/plant-omics-thesis-writing/references/claims-and-chapter-logic.md). Add “a stored table reports 4 of 6 comparisons; a shared mechanism is proposed,” and ask for a Results sentence plus a Discussion note. | Preserve the supplied count as a table fact, keep the proposed mechanism separate, and do not infer cell-level colocalization or invent a citation. |

To see the synthetic output previews alongside their workflows, use the [visual gallery](visual-gallery.md).
