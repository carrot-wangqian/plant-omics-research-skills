# Visual references and design rationale

The [v1.0.0 visual gallery](visual-gallery.md) uses original illustrations and combines journal-style evidence layouts, restrained plant-tissue line art, and route-map diagrams where branching decisions need to be shown. The linked examples informed design principles, not reused graphics.

| Source | How it informed the design |
| --- | --- |
| [nf-core/eager workflow overview](https://github.com/nf-core/eager/blob/master/docs/images/usage/eager2_workflow.png) and [its technical map](https://github.com/nf-core/eager/blob/master/docs/images/usage/eager2_metromap_complex.png) | Put the main route where the eye starts; keep details that are not needed for the decision outside the map. The transit treatment borrows route grammar, not their artwork. |
| [nf-core/scrnaseq decision tree](https://github.com/nf-core/scrnaseq/blob/master/README.md#decision-tree-for-users) | Show a choice only if it changes what happens. The selected access route determines what the reading report can verify. |
| [Minimal Terminal Card contact sheet](https://github.com/banozz0/minimal-terminal-card/blob/main/examples/example-contact-sheet.png) | Use one repeatable square grid and a consistent reading order. Do not put a README inside a tile. |
| [Figma's FigJam video tutorial and transcript](https://www.figma.com/figjam/how-to-use-figjam-to-make-diagrams/) and [draw.io's flowchart guide](https://www.drawio.com/docs/getting-started/basic-flowchart/) | Use different shapes for actions and decisions, attach labeled connectors and keep the sequence explicit. |
| [Cathryn Lavery's design examples](https://github.com/cathrynlavery/diagram-design) and [her public LinkedIn walkthrough](https://www.linkedin.com/posts/cathryn-lavery_free-claude-skill-every-time-i-asked-claude-activity-7493050687396941824-mcb_) | Separate a visually disciplined editorial treatment from light and dark alternatives. Use one accent, strong alignment and no decorative shadows. |
| [GitHub's Mermaid documentation](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams) | Supply a simple source diagram and plain-language description as well as styled graphics. This repository does not require Mermaid to read the PNGs. |

The gallery pairs browsable PNGs with editable SVGs and, for workflows, Mermaid sources. English text descriptions accompany the images so that visual styling is not required to understand the decision paths.
