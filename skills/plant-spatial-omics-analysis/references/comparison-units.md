# Comparison units in plant omics

Use only the branch relevant to the question.

| Modality | Decision that changes interpretation |
| --- | --- |
| Cell or nucleus RNA | Distinguish the independent specimen from profiled cells or nuclei. Record which layer is used for each operation. Low-dimensional neighborhoods and pseudotime are model-based structures, not direct measurements of physical distance or chronological time. Check how labels and composition change by specimen and processing choice. |
| Spatial RNA | Preserve the analysis unit (spot, bin, segmented cell, or region) and its physical definition. A finer display grid does not improve underlying resolution. Audit area and capture differences before comparing counts or proportions across regions. |
| Bulk omics | Confirm independent sample level, balances, and transformations. Use sample-level diagnostics for possible technical failures; distance in a projection alone is not an exclusion rule. |
| Cross-modality comparison | A condition match is weaker than a same-specimen match; an adjacent section is not the same section. State how values were aggregated or registered, and what evidence is measured versus inferred. Investigate disagreement rather than forcing the same label or ranking. |

When using established diagnostics or method defaults, copy their effective settings from current logs, provenance, or documented software versions. Do not treat a convention from one organism, platform, or dataset as universally valid.
