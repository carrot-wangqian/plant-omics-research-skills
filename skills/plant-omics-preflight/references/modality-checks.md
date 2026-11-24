# Modality-specific preflight checks

Use the row relevant to the requested action. These are checks of available data and metadata, not prescribed acquisition, analysis, or filtering protocols.

| Input | Bind before comparing | Bound the claim when unavailable |
| --- | --- | --- |
| Mass spectrometry imaging (MSI) | Section to biological sample; coordinate origin, axis and units; ion-mode metadata; observed feature identifiers; ROI mask; whether values are raw, normalized, or display-transformed; comparable color scales. Keep matching error separate from any alignment tolerance. | An observed feature or candidate annotation is not confirmed identity. Do not claim tissue concentration, registered overlap, or cross-image intensity comparability without supporting data. |
| Single-cell or single-nucleus RNA sequencing | Cell or nucleus, source sample, independent replicates and batch; matrix orientation; counts versus transformed or integrated layers; expected metadata and reference/annotation version. | Treat cluster labels as annotations. Cell counts do not replace design-level replicates, and sampling proportions do not establish tissue composition. |
| Spatial transcriptomics | Section identity, spot/bin/cell semantics, coordinate units and orientation, image and coordinate linkage, aggregation level, and registration evidence if used. | Grid width does not prove biological resolution. A mapped reference label or mixed spot does not establish direct cell identity. |
| Bulk plant omics | Sample-level metadata, measurement scale, feature identifiers and transformation history; distinguish batch from treatment. | Do not attribute effects to a biological variable confounded with batch. |
| Cross-modality comparison | Whether data share a plant, specimen, same section, adjacent sections or only a condition; common resolution and comparison unit; source of observed versus inferred labels. | Shared labels do not establish pairing, neighboring sections do not imply one-to-one cells, and co-distribution does not demonstrate mechanism. |

If coordinates are missing, for example, a comparison of valid aggregate counts may still be possible while the spatial overlay remains blocked. If a color scale differs, existing figures may still be described separately, but not used as a quantitative cross-image comparison.

## Alignment and availability gate

Before a spatial overlay or a cross-group summary that depends on spatial correspondence or masks, check that row identifiers map one-to-one to spatial coordinates and the intended mask; record orientation, registration evidence, eligible coverage, and the zero-versus-missing policy. An independently assigned cluster ID does not prove that two sections share that cluster. If key checks fail, mark the comparison blocked or conditional without blocking unrelated descriptive work.
