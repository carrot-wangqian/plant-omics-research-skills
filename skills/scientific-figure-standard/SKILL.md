---
name: scientific-figure-standard
description: Create, restyle, export, or technically audit scientific figures from existing results. Use for figure design, versioned output, provenance, and visual quality checks without silently changing data, statistics, or biological claims; not for biological interpretation alone or rerunning upstream analyses.
---

# Scientific Figure Standard

Make the figure easier to read without changing what was measured, estimated, or compared. Work from saved results or explicitly supplied images. Use the journal or user's specifications when given.

## Lock the source

Record the figure ID and version, source table or image, units, observation level, grouping, layer or transformation, statistical and uncertainty sources, and actual plotting configuration. Determine what is comparable before sharing a scale or combining panels. Resolve what is necessary for the requested figure, not unrelated project issues. Use a new output path; do not overwrite source data or prior figures.

## Render the figure

Reuse a working renderer if available. Select marks, spacing, type sizes, and labels for the target output size, not the editor zoom. Match the style and legend to the actual statistics. Keep orientation, aspect ratio, and registration intact; add a scale bar only with calibrated units. Use a common color scale only when variables, units, transformations, and ranges support comparison; label independent scales. Cite the original annotation evidence and do not promote a candidate match to confirmed identity. Read [spatial panels](references/spatial-panels.md) for modality-specific checks.

Prefer a vector PDF for publication and a PNG for preview when the destination has no other requirement. Keep text and axes vector where possible; identify necessary raster layers. Record physical dimensions, raster resolution, real fonts, units, software versions, and export options. A style edit must not rerun normalization, mapping, clustering, differential testing, or smoothing. Propose such changes separately if they appear necessary.

## Review exports

Check nonempty readable files, intended dimensions and resolution, font rendering, and font embedding when relevant. Open the actual preview and a render of the final format; check labels, scales, crop, panel order, contrast, aspect ratio, and consistency with source data at the target viewing size. Fix layout or wrapping before shrinking text. Record review scope and exceptions with version or output checksums; a new export needs its own visual check. When visual or font verification is unavailable, say what was checked and name the exact missing export or evidence. A supported caption-only change can proceed without marking the missing final image as reviewed.

## Deliver figure + QA

Provide the versioned exports, source/configuration references or an approved bounded data snapshot, and a technical review record. Record the state as technical pass, review pending, or fail. Technical pass is not scientific approval or publication readiness. Include or link a [Figure Summary](references/figure-summary.md) using the same `figure_id`, and keep exact quantitative claims tied to saved evidence. For a figure-only task, a compact summary and unresolved review items are enough; do not redraw or recalculate merely to fill missing fields.
