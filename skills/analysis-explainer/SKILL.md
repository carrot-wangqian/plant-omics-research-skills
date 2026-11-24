---
name: analysis-explainer
description: Explain or audit existing omics results and scientific figures. Use for evidence-linked result interpretation, figure walkthroughs, reproducibility notes, or limited next-step recommendations without rerunning analyses or redrawing figures; not for reading external published papers or redrawing figures.
---

# Analysis Explainer

Help the reader understand why the analysis was done, what it actually found, and what it cannot show. Use the smallest scope that answers the current question. Distinguish explanation, quality review, and next-step planning; users need not name a mode.

## Locate evidence

Trace the supplied inputs, processing, saved results, figure, and execution logs. Read only the relevant bounded artifacts. Prefer source tables and current renderings; a planned run, old report, or script is not proof of execution. Identify the analysis status as reused, rechecked, not run, or unavailable. If a conflict matters, show both sources and their scope rather than treating the newer file as correct. Do not run historical scripts or modify the supplied materials.

## Explain the method

Begin with the question and main finding in plain language. Explain the actual method, inputs, observation unit, independent biological replicates, parameters that affect interpretation, and why the method fits the question. An unrecorded parameter stays unknown. To teach one figure, describe each panel's axes, units, marks, color, uncertainty, and reading order; give one concrete way the figure could be misread. Check the current rendering before judging visual quality.

## Separate claims

Distinguish direct observation, inference from a completed statistical analysis, biological interpretation, and hypotheses requiring validation. Link each material claim to a row, panel, field, or execution record. For an inferential claim, report the comparison, experimental unit, effect and uncertainty, statistical test, and multiplicity correction as available. Keep cells, spots, pixels, technical repeats, and biological replicates distinct. Do not infer exact numbers from colors alone, make up missing statistics, or treat co-occurrence as mechanism.

For before/after annotation totals, check the eligible denominator and count distinct observed features separately from candidate rows. Distinguish within-image patterns from quantitative comparisons and distinguish an unmatched feature from a measured zero. If a comparison is proposed but not present in execution records, report it as a proposed next step, not a result.

For a quality review, judge data, method, statistics, visualization, and reproducibility separately. Base each judgment on checked evidence, or mark it unassessed. For next steps, propose the smallest useful comparison or check, what success would look like, and when to stop. A recommendation does not authorize a rerun.

## Deliver the Figure Summary

For one figure, deliver a brief reading guide with a [Figure Summary](references/figure-summary.md). For a full analysis, provide the top-line finding, scope, per-figure notes, gaps, and a reproduction index. Distinguish a result someone can verify, a figure someone can redraw from saved outputs, and an analysis someone can recompute from source data. Record command or script references and their status without executing them. Keep editable text; export and visually check a matching PDF when requested. Do not claim a missing format or unavailable evidence was checked.
