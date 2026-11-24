---
name: plant-spatial-omics-analysis
description: Plan, diagnose, or run a bounded comparison using plant omics data, with applied-parameter checks, filtering and retention review, and an MSI-specific branch. Use when choosing or evaluating a workflow, not to read papers, polish prose, or restyle an existing figure.
---

# Plant Spatial Omics Analysis

Start with the scientific question and the smallest useful comparison. Improvement means better evidence or fewer well-supported technical problems, not simply a cleaner plot or more significant results.

## Workflow

1. **Define Comparison.** Name the estimand or descriptive question, comparison groups, unit of observation, independent biological unit, intended output, and current authorization. Validate input identity, processing layer, and key prerequisites. If the project uses a preflight record, reuse a current, relevant one; otherwise document a minimal check here.
2. **Verify Baseline.** Bind the baseline to the actual data, processing order, software version, and effective parameters, including defaults that affect the result. Distinguish an existing result, a proposed analysis, an authorized trial, and a result reproduced in the current run. Inspect code or logs before describing settings as applied. An exported table does not support conclusions about unavailable raw data.
3. **Compare Options.** Diagnose whether the discrepancy arises from identification, coverage, measurement, transformation, model assumptions, or display. Mark the explanation as verified, plausible, or unknown. Propose a small number of defensible alternatives with comparable inputs and predeclared criteria. Run only comparisons within current authorization; otherwise stop at the plan. Check technical quality, repeatability, interpretability, and potential information loss rather than optimizing a single visual or statistical metric.
4. **Audit Retention.** For any filter, separate technical quality rules, feature eligibility, scope restrictions, and display-only choices. Preserve the rule order, denominators, affected IDs, and counts before and after each rule by meaningful group. Missing measurements are not zeros. Report if the surviving subset changes the question or excludes a meaningful group.
5. **Record Decision.** Summarize what changed, why it matters, which outputs can be reused, and what the evidence cannot support. Keep trial, recommended, and user-adopted states separate. Record important failures or tradeoffs. Stop if reasonable variants reverse the key claim; report its sensitivity rather than continuing to tune for a preferred result.

## Read only the branch needed

- For spatial mass spectrometry read [the MSI branch](references/msi.md).
- For cell/nucleus RNA, spatial transcriptomics, bulk or cross-modality comparisons, read [other comparison units](references/comparison-units.md).
- For retention decisions or analyst handoffs, use [the decision record and worked example](references/decision-record.md).

A descriptive result can still be useful when inference is unsupported. Do not silently exclude a whole biological sample, change a primary comparison, or report an exploratory finding as a confirmed conclusion. Keep sources read-only; write only approved derivatives. A plan, installation, or prior trial does not authorize a new execution.
