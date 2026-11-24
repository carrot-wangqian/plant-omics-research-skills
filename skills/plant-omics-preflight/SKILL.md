---
name: plant-omics-preflight
description: Review scope and verify inputs, sample identity, and method prerequisites before a plant omics analysis or figure refresh. Use for a new dataset, changed sample map, unclear data layer, or a read-only authorization check. Do not use for execution or prose-only editing.
---

# Plant Omics Preflight

Determine whether the requested comparison is supportable from the available evidence. A successful preflight is not permission to execute and is not a scientific result.

## Choose a mode and limit scope

- **Scope Review:** Check the user's requested action, approved inputs, and intended output without reading scientific data.
- **Targeted Preflight (default):** Inspect only the records on which the current task depends.
- **Inventory or Refresh:** Use only when asked to establish an inventory or incorporate changes. A partial check does not replace a full inventory or prove that unobserved files were deleted.

If the request is only to restyle a figure, identify the exact source table and the display transformation without scanning unrelated datasets. Reuse relevant verified evidence after checking that its scope and source versions still match.

## Workflow

1. **Define Scope.** State the question, intended comparison, independent biological unit, allowed actions, and output location. Separate method approval, execution permission, and adoption of a conclusion. Never infer one from another.
2. **Bind Inputs.** Identify the named data objects and layers, sample and replicate mapping, modality, processing status, reference versions where relevant, and provenance. Resolve identity with the user's manifest or acquisition record; a file suffix or directory name is not evidence of a replicate or stage.
3. **Check Prerequisites.** Start with sample tables, small exports, headers, logs and static code. Record what was listed, read, spot-checked, or independently verified. A header does not verify all values; serialization formats may require a full object load. Do not run existing analysis code just to discover inputs. Consult [modality-specific checks](references/modality-checks.md) only for the modality at issue.
4. **Record Readiness.** Classify each requested step as **Ready**, **Conditional**, **Blocked**, or **Not Applicable**. Report the smallest next check, why it matters, and what remains safe to do. Without independent biological replicates, retain appropriately bounded description instead of treating cells, spots, pixels, or sections as independent replicates.

Use the [readiness record](references/readiness-record.md) for complex or reproducibility-sensitive tasks. For a routine review, a short table in the reply is enough. Keep source material unchanged. A prior decision is reusable only within its original scope and while its evidence remains current. Ask about unresolved decisions only if their answer changes the next step.

## Stop point

Stop after the readiness report unless execution is separately requested and authorized. Do not install dependencies, upload material, overwrite source files, or quietly replace data, thresholds, or methods. When a dependency is blocked, complete independent checks rather than turning the whole review into a failure.
