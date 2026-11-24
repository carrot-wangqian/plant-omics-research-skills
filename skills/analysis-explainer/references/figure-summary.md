# Figure Summary v1

Use the same figure ID across a figure export, its technical review, and its interpretation. A summary can be prepared without changing the figure. Start with a Markdown note; add a matching TSV for multi-panel or structured handoff use. This is a record of evidence, not a certification.

## Identity and rows

Keep `figure_id`, `figure_version`, `row_id`, `kind`, `panel_id`, `observation_unit`, `bio_n`, `comparison`, `value`, `unit`, `evidence`, and `limit`. Use unique row IDs within a figure version. Use one `overview` row with panel `ALL`, a `panel` row for each actual panel, and separate `result` rows for distinct comparisons or outcomes. A single unpaneled image needs only an overview and any relevant result rows. Retain absolute source paths only in authorized internal deliverables; prefer task-relative locations in shared ones.

Record the figure source, actually applied parameters, and export/review state in accompanying notes. For each number, point to the actual table row/field or a documented bounded extraction from saved results. When possible, record the exact inspected source version or checksum. If a number cannot be verified, use `unavailable`; an undocumented parameter is `unknown`; a field that has no role is `not applicable`. None of these means zero.

## Synthetic example

The table below demonstrates the record format. No result represents an experiment. The referenced fixture is bundled in this Skill.

| figure_id | figure_version | row_id | kind | panel_id | observation_unit | bio_n | comparison | value | unit | evidence | limit |
|---|---|---|---|---|---|---|---|---|---|---|---|
| demo-ion | 1 | r1 | overview | ALL | pixel | 1 | unavailable | not applicable | not applicable | [fixture](synthetic-summary-source.tsv) | One fictional section; no biological inference |
| demo-ion | 1 | r2 | panel | A | pixel | 1 | not applicable | not applicable | Relative signal | [fixture](synthetic-summary-source.tsv), row s1 | Fictional region signal panel |
| demo-ion | 1 | r3 | result | A | pixel | 1 | Outer versus inner | 1.4 | Ratio of mean relative signal | [fixture](synthetic-summary-source.tsv), row s1 | Descriptive comparison only |

An acceptable summary is “The outer region showed a higher mean relative signal than the inner region in this synthetic section.” The source cannot establish concentration, chemical identity, or across-plant reproducibility.

Before attributing an exact table value to a displayed panel, verify that the table belongs to the same figure version and input layer. If that link is missing or inconsistent, report values as table facts only, mark panel attribution unavailable, and describe only what the image independently supports.
