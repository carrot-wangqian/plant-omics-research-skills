# Panel and methods record

## Panel card

Collect the identifiers a second reader needs to check your reading, not a separate index for every sentence:

- Panel, comparison, independent sample and observation unit
- Visible encoding: axes, units, scale or color range, legend and statistical marks
- Analysis: input, major transformation, method and output
- Claim: observed result first, author's interpretation second
- Evidence: caption, methods, supplement or public code actually inspected
- Boundary: an inference the panel does not support; any relevant missing material

Common boundaries: neighboring pixels are not independent biological replicates; adjacent sections are not the same cells; pseudotime is an inferred ordering, not elapsed time; colocalization is not causality; exact-mass matches are candidate annotations, not compound identifications. For reference mapping, distinguish inferred labels from direct measurements.

## Method card and cross-paper use

Save a method record when the source provides usable detail. Include method ID, task, input and unit, preprocessing, software and version, parameters and units, QC checks, output, limitations, paper and source locator, and verification status. Give each distinct published variant its own settings. Leave undocumented values as "not reported." A reuse suggestion should name the necessary input, one quick quality check, and the assumption that may not transfer.

For cross-paper comparisons, compare purpose and inputs before thresholds. Report adoption frequencies only against a denominator of inspected, eligible papers. Unread or inaccessible is not the same as absent.

## Optional handoff

If asked to save continuity, record the source identifier and version, reading basis, report reference, methods consulted, open questions, corrections, reader decisions, and next step. Keep stages separate: source obtained, content inspected, method recorded, report delivered. A reading report should not change a project plan without a separate decision. Do not overwrite a prior report or create a shared database unless requested.

## Synthetic example

A fictional leaf atlas panel shows three plants per condition and several tissue locations per plant. A heatmap displays a normalized gene score by location. Report a regional difference in the score if the panel supports it, but do not infer a treatment effect from the number of spots. If the caption names a model without explaining its sampling unit or uncertainty, mark these details as unverified.

## Capturing a reporting convention

When using a paper as a writing model, record what it does to make the evidence legible: how it names sources, defines the denominator, marks ambiguity, reports scale, or separates measured observations from interpretations. Record panel or section locators and what transfers to a new study. Do not import the original claims, parameters, or wording as defaults.
