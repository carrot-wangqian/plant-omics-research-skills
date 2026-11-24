# Spatial and single-cell panels

| Panel type | Preserve | Check before comparison | Do not infer |
|---|---|---|---|
| Mass spectrometry imaging | Pixel geometry, optical context, masks, signal layer, units, and color range | Common normalization, comparable acquisition and scales, bounds or clipping, and any interpolation | Confirmed compound identity from a mass match alone; quantitative concentration from ion-image color |
| Single-cell or single-nucleus embedding | Observation type, key, labels, and disclosed transformed expression layer | Cell-to-sample grouping, whether visual scales agree, independent biological replicates | Physical distance from an embedding; biological replication from the number of points |
| Spatial transcriptomics | Coordinates, orientation, spatial unit, assay layer, and section identity | Scale and registration evidence; distinct versus shared domains and legends | Same-cell overlap from adjacent sections; measured signal from transfer alone |

For tissue images, keep tone or background adjustment identifiable rather than altering features selectively. Expose materially different transforms or scale limits in legends and captions. For source snapshots, retain only what is permitted and needed to reconstruct the rendered panel.

## Cross-group panels

Do not join a line across a missing or unaligned feature, and do not draw variability bars when the underlying independent replication or uncertainty is unavailable. Use independently scaled images to show within-image patterns only. For quantitative differences, refer to verified saved measurements and compatible transformations; disclose material differences in scale or mask in the caption. Prefer a focused panel or inset that answers a stated spatial question to a generic zoom.
