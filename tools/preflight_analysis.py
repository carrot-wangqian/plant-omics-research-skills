"""Release artwork metadata for the readiness and analysis routes."""

PREFLIGHT_ICON = '''
<g fill="none" stroke-linecap="round" stroke-linejoin="round">
  <path d="M97 35h-30a13 13 0 0 0-13 13v174a13 13 0 0 0 13 13h155a13 13 0 0 0 13-13V48a13 13 0 0 0-13-13h-34" fill="#f2eee3" stroke="#215c75" stroke-width="3"/>
  <rect x="66" y="48" width="157" height="174" rx="7" fill="#f8f6ef" stroke="#cad5d5" stroke-width="1.5"/>
  <path d="M102 38v-10a7 7 0 0 1 7-7h14a23 23 0 0 1 43 0h14a7 7 0 0 1 7 7v10a8 8 0 0 1-8 8h-69a8 8 0 0 1-8-8Z" fill="#e7eff0" stroke="#215c75" stroke-width="3"/>
  <circle cx="144.5" cy="18" r="3.1" fill="#215c75"/>
  <path d="M88 81h94M88 96h75" stroke="#cad5d5" stroke-width="3"/>
  <g stroke="#215c75" stroke-width="2.6">
    <rect x="88" y="117" width="19" height="19" rx="3" fill="#e7eff0"/>
    <rect x="88" y="153" width="19" height="19" rx="3" fill="#e7eff0"/>
    <rect x="88" y="189" width="19" height="19" rx="3" fill="#e7eff0"/>
    <path d="m92 126 4 5 8-10m-12 42 4 5 8-10m-11 41h9m20-72h60m-60 36h42m-42 36h50"/>
  </g>
  <path d="M272 174c18-15 43-48 44-85-34 3-65 19-79 49" stroke="#cad5d5" stroke-width="2" stroke-dasharray="4 7"/>
  <circle cx="240" cy="130" r="56" fill="#e7eff0" stroke="#173646" stroke-width="4.5"/>
  <circle cx="240" cy="130" r="47" fill="#f8f6ef" stroke="#cad5d5" stroke-width="1.4"/>
  <path d="M217 148c-9-23 7-43 47-48 0 37-17 56-42 52-1-1-3-2-5-4Z" fill="#ebeee6" stroke="#215c75" stroke-width="2.5"/>
  <path d="M210 158c16-17 31-29 48-49m-32 34-1-13m11 5 13-1m-8-5-1-12m10 2 8-1" stroke="#117964" stroke-width="2"/>
  <path d="m277 173 32 32a8 8 0 0 1-11 11l-32-32" fill="#e7eff0" stroke="#173646" stroke-width="4"/>
  <path d="m278 187 21 21" stroke="#215c75" stroke-width="2"/>
</g>
'''

ANALYSIS_ICON = '''
<g fill="none" stroke-linecap="round" stroke-linejoin="round">
  <path d="M35 189v28h29m225 0h28v-28M35 60V32h29m225 0h28v28" stroke="#cad5d5" stroke-width="2"/>
  <path d="m56 183 116-56 115 48-116 56-115-48Z" fill="#ebeee6" stroke="#215c75" stroke-width="3"/>
  <path d="M171 231v10l116-56v-10M56 183v10l115 48" stroke="#215c75" stroke-width="2"/>
  <path d="M95 180c21-17 47-28 75-28 21 1 39 9 64 23-25 9-48 20-66 29-28-3-54-12-73-24Z" fill="#f8f6ef" stroke="#117964" stroke-width="2"/>
  <path d="M100 180c35-1 89-3 134-5m-112 4 20-12m-5 12 24 11m3-13 24-13m2 14 17 7" stroke="#117964" stroke-width="1.8"/>
  <path d="M57 120v62m115-120v65m115-15v62M172 169v56" stroke="#215c75" stroke-width="1.6" stroke-dasharray="4 6"/>
  <path d="m56 118 116-56 115 48-116 56-115-48Z" fill="#e7eff0" stroke="#173646" stroke-width="3.3"/>
  <path d="M171 166v10l116-56v-10M56 118v10l115 48" stroke="#215c75" stroke-width="2"/>
  <path d="M94 115c20-15 46-27 73-27 22 1 38 7 68 22-27 9-49 21-68 28-28-3-52-11-73-23Z" fill="#f8f6ef" stroke="#215c75" stroke-width="2"/>
  <path d="m100 115 129-4m-107 4 19-12m-5 12 24 10m3-11 24-13m2 13 19 6" stroke="#cad5d5" stroke-width="1.8"/>
  <g fill="#215c75">
    <circle cx="117" cy="114" r="3.5"/><circle cx="132" cy="108" r="3"/><circle cx="143" cy="116" r="4.5"/><circle cx="151" cy="103" r="3.3"/><circle cx="158" cy="112" r="5"/><circle cx="166" cy="123" r="3.2"/><circle cx="172" cy="106" r="4"/><circle cx="182" cy="116" r="3"/><circle cx="195" cy="109" r="3.3"/><circle cx="210" cy="113" r="2.7"/>
  </g>
  <path d="M41 82h32m-16-16v32m216-39h32m-16-16v32" stroke="#117964" stroke-width="2"/>
  <circle cx="57" cy="82" r="5.8" fill="#f8f6ef" stroke="#117964" stroke-width="2"/>
  <circle cx="289" cy="59" r="5.8" fill="#f8f6ef" stroke="#117964" stroke-width="2"/>
</g>
'''

DATA = {
    "plant-omics-preflight": {
        "title": ["Plant Omics", "Preflight"],
        "promise": "Check readiness without running the analysis.",
        "gate": "Readiness is not execution permission.",
        "icon": PREFLIGHT_ICON,
        "stages": [
            ("Choose mode & scope", "Scope Review / Targeted\n(default) / Inventory", "Scope and allowed actions"),
            ("Bind inputs", "Objects, layers, samples", "Identity and provenance"),
            ("Check prerequisites", "Relevant modality only", "What was verified"),
            ("Classify readiness", "Ready / Conditional /\nBlocked / Not Applicable", "Next safe action"),
        ],
        "preview_title": "Readiness memo",
        "preview_id": "Question: can we compare paired regions and check their overlay?",
        "preview": [
            ("Ready", "Paired within-plant summary"),
            ("Conditional", "Condition test: one plant per condition"),
            ("Blocked", "Tissue overlay: missing coordinate transform"),
            ("Not Applicable", "Raw read yield: saved imaging-feature table"),
        ],
        "boundary": "Readiness is not permission to run.",
        "mermaid": '''flowchart LR
    scope["01 · Choose mode & limit scope"]
    scope --> modes["Scope Review / Targeted (default) / Inventory"]
    modes --> bind["02 · Bind inputs"]
    bind --> pre["03 · Check prerequisites"]
    pre --> branch["Inspect relevant modality only"]
    branch --> classify{"04 · Classify readiness"}
    classify --> ready["Ready"]
    classify --> conditional["Conditional"]
    classify --> blocked["Blocked"]
    classify --> na["Not Applicable"]
    ready --> stop["HARD STOP · Preflight is not execution permission"]
    conditional --> stop
    blocked --> stop
    na --> stop
    classDef block fill:#f3e3de,stroke:#a64239,color:#14262a;
    class blocked,stop block;
''',
    },
    "plant-spatial-omics-analysis": {
        "title": ["Plant Spatial", "Omics Analysis"],
        "promise": "Choose the next defensible comparison.",
        "gate": "Run only within authorized scope.",
        "icon": ANALYSIS_ICON,
        "stages": [
            ("Define comparison", "Question, groups, bio_n", "Unit and scope"),
            ("Verify baseline", "Actual layer and settings", "Data and parameters"),
            ("Compare options", "Authorization gate", "Run bounded / stop at plan"),
            ("Audit retention", "Denominators and exclusions", "Missing is not zero"),
            ("Record decision", "Evidence and tradeoffs", "Reuse limits"),
        ],
        "preview_title": "Paired regional decision",
        "preview_id": "Plant is the independent unit · Paired difference = A minus B",
        "preview": [
            ("P01", "A 8  |  B 6  |  Both pass  |  Difference 2"),
            ("P02", "A 11  |  B 7  |  Both pass  |  Difference 4"),
            ("P03", "A 5  |  B missing, not 0  |  No pair"),
            ("P04", "A 30  |  B 8  |  A fails QC  |  Excluded"),
            ("Summary", "2/4 eligible  |  Mean 3 signal units  |  No p-value"),
        ],
        "boundary": "MSI: a mass match is not a confirmed compound.",
        "mermaid": '''flowchart LR
    define["01 · Define comparison"] --> baseline["02 · Verify baseline"]
    baseline --> modality{"Select modality"}
    modality --> msi["MSI branch"]
    modality --> rna["scRNA / Spatial RNA / Cross-modality"]
    msi --> compare["03 · Compare options"]
    rna --> compare
    compare --> gate{"Authorization gate"}
    gate -- Authorized --> run["Run bounded comparison"]
    gate -- Unauthorized --> stop["Stop at plan"]
    run --> audit["04 · Audit retention: denominators; missing is not zero"]
    audit --> decide["05 · Record decision"]
    classDef block fill:#f3e3de,stroke:#a64239,color:#14262a;
    class stop block;
''',
    },
}
