# Readiness record

Capture only what another reader needs to reproduce the decision.

- **Request:** question, action and permitted scope.
- **Evidence:** dataset label, exact object/sheet/field and version or run reference; relationship among samples, sections, and observations.
- **Inspection:** listed / read / spot-checked / independently verified / unknown.
- **Decision:** Ready / Conditional / Blocked / Not Applicable, for a named next step.
- **Limitation:** what must be supplied, what claim cannot yet be supported, and what work can continue independently.

## Synthetic example

**Question:** Can already-saved signals from two regions be compared across plants, and can their tissue overlay be checked?

| Requested step | Evidence | Status | Implication |
| --- | --- | --- | --- |
| Summarize within-plant region differences | The fictional table contains one row for each region and plant, with both measurements on the same stated scale. | Ready | A paired description is supported for plants with observations in both regions. |
| Test a condition effect | Only one independent plant is present in each condition; a section count is not another plant. | Conditional | An inference requires a defensible replicate design. A descriptive summary can proceed without requiring it. |
| Check the tissue overlay | The image is present, but the fictional export lacks the coordinate transform. | Blocked | Do not infer orientation or fill it from visual similarity. |
| Compare raw read yield | This input is a saved imaging-feature table; raw read yield is outside the task. | Not Applicable | Omit this check. |

This example is fabricated and is not intended as a statistical recommendation about minimum sample size.
