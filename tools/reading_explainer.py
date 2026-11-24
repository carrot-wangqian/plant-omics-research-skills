"""Editorial visual content for paper reading and result interpretation."""

# Each illustration occupies a 480 x 290 local coordinate system.
# Colors follow the approved release palette; no external assets or fonts.
ICONS = {
    "spatial-omics-paper-reading": '''
<g fill="none" stroke-linejoin="round">
  <path d="M67 23H319L363 67V241H67Z" fill="#f2eee3" stroke="#cad5d5" stroke-width="3"/>
  <path d="M49 36H301L345 80V254H49Z" fill="#f8f6ef" stroke="#215c75" stroke-width="4"/>
  <path d="M301 36V80H345" stroke="#215c75" stroke-width="4"/>
  <path d="M74 72H257M74 89H222" stroke="#173646" stroke-width="5" stroke-linecap="round"/>
  <rect x="75" y="110" width="126" height="100" fill="#e7eff0" stroke="#cad5d5" stroke-width="2"/>
  <path d="M85 139H192M85 167H192M85 195H192M105 120V202M131 120V202M157 120V202M183 120V202" stroke="#cad5d5" stroke-width="1.5"/>
  <path d="M94 184Q99 149 183 131Q169 183 124 191Q105 194 94 184Z" fill="#ebeee6" stroke="#215c75" stroke-width="3"/>
  <path d="M86 201Q115 175 167 143M116 177L118 156M136 163L160 169" stroke="#117964" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M74 225H200M220 117H312M220 138H297M220 159H309M220 180H280M220 201H312M220 225H295" stroke="#cad5d5" stroke-width="3" stroke-linecap="round"/>
  <path d="M325 179L371 228" stroke="#f8f6ef" stroke-width="23" stroke-linecap="round"/>
  <path d="M325 179L371 228" stroke="#173646" stroke-width="13" stroke-linecap="round"/>
  <circle cx="288" cy="143" r="59" fill="#f8f6ef" stroke="#215c75" stroke-width="6"/>
  <path d="M255 164Q260 127 323 112Q318 151 279 170Q268 175 255 164Z" fill="#e7eff0" stroke="#215c75" stroke-width="3"/>
  <path d="M249 172L307 127M270 156L275 137M287 143L308 147" stroke="#117964" stroke-width="3" stroke-linecap="round"/>
  <path d="M375 68H431M403 40V96" stroke="#cad5d5" stroke-width="2"/>
  <circle cx="404" cy="68" r="16" stroke="#cad5d5" stroke-width="2"/>
</g>''',
    "analysis-explainer": '''
<g fill="none" stroke-linecap="round" stroke-linejoin="round">
  <rect x="30" y="89" width="133" height="116" rx="5" fill="#e7eff0" stroke="#215c75" stroke-width="3.5"/>
  <path d="M43 126H150M43 150H150M43 174H150M60 112V191M83 112V191M106 112V191M129 112V191" stroke="#cad5d5" stroke-width="1.3"/>
  <path d="M49 172Q63 145 88 149Q112 155 143 120" stroke="#117964" stroke-width="4"/>
  <path d="M51 185Q70 160 92 163Q119 168 145 137" stroke="#215c75" stroke-width="2.3"/>
  <g fill="#215c75">
    <circle cx="63" cy="154" r="3"/><circle cx="77" cy="161" r="3"/><circle cx="90" cy="153" r="3"/>
    <circle cx="104" cy="147" r="3"/><circle cx="119" cy="141" r="3"/><circle cx="134" cy="130" r="3"/>
  </g>
  <path d="M163 147H188M182 141L188 147L182 153" stroke="#117964" stroke-width="3"/>
  <rect x="189" y="97" width="116" height="105" rx="5" fill="#f8f6ef" stroke="#215c75" stroke-width="3.5"/>
  <path d="M189 124H305V150H189Z" fill="#e7eff0"/>
  <path d="M211 97V202M248 97V202M276 97V202M189 124H305M189 150H305M189 175H305" stroke="#cad5d5" stroke-width="2"/>
  <circle cx="259" cy="137" r="6" fill="#117964"/>
  <path d="M305 137H325Q338 137 338 124V112H353M347 106L353 112L347 118" stroke="#117964" stroke-width="3"/>
  <rect x="354" y="60" width="91" height="177" rx="5" fill="#f2eee3" stroke="#215c75" stroke-width="3.5"/>
  <path d="M366 86H426" stroke="#173646" stroke-width="4"/>
  <rect x="366" y="103" width="66" height="20" rx="2" fill="#e7eff0" stroke="#215c75" stroke-width="2"/>
  <path d="M369 141H429M369 165H429M369 189H414M369 213H418" stroke="#cad5d5" stroke-width="3"/>
  <path d="M30 246H445M76 246V259M238 246V259M406 246V259" stroke="#cad5d5" stroke-width="2"/>
</g>''',
}

DATA = {
    "spatial-omics-paper-reading": {
        "number": "01",
        "title": ["Spatial Omics", "Paper Reading"],
        "promise": "Turn a paper into an evidence-linked reading brief.",
        "gate": "Published method ≠ project plan",
        "workflow_title": "Paper Reading Workflow",
        "workflow_subtitle": "Verify source access, inspect panels, and record reusable methods.",
        "stages": [
            ("Verify source", "Check source access", "Source and access"),
            ("Trace design", "Find units and contrasts", "Design summary"),
            ("Read figures", "Read panels and captions", "Evidence locations"),
            ("Capture methods", "Record settings and gaps", "Methods log"),
            ("Save report", "Separate facts and views", "Reading report"),
        ],
        "access": [
            ("Full text", "Use methods, panels, captions.", "Continue"),
            ("Partial", "Use available evidence; label gaps.", "Continue"),
            ("Absent", "Request a usable source.", "STOP"),
        ],
        "footer": "Optional handoff: save open questions and next steps on request.",
        "preview_title": "Reading Evidence from Panel 2B",
        "preview_id": "Synthetic Panel 2B",
        "boundary": "Visual signal is not a measured difference.",
        "preview": [
            ("Source basis", "Mock panel 2B and caption only.\nNo real paper, DOI, or raw data."),
            ("Observation", "The leaf edge looks brighter.\nThis is a visual comparison only."),
            ("Method gap", "A shared intensity scale is shown.\nAcquisition and preprocessing are unknown."),
            ("Claim limit", "No molecular identity,\nenrichment, or cause is established."),
            ("Reuse check", "Check the scale and independent samples\nbefore comparing real panels."),
        ],
        "preview_desc": "A fictional reading report separates visual observations, missing methods, and the limits of the claim.",
    },
    "analysis-explainer": {
        "number": "04",
        "title": ["Analysis", "Explainer"],
        "promise": "Explain saved results and their evidence limits.",
        "gate": "No rerun, no redraw",
        "workflow_title": "Analysis Explanation Workflow",
        "workflow_subtitle": "Explain stored results and claim limits without rerunning.",
        "stages": [
            ("Locate evidence", "Check tables and renders", "Evidence locations"),
            ("Explain method", "Unit, bio_n, parameters", "Method notes"),
            ("Separate claims", "Observation, inference,\ninterpretation, hypothesis", "Bounded claims"),
            ("Deliver Figure Summary", "Bind values to version", "Figure Summary"),
        ],
        "footer": "STOP: No rerun, no redraw.",
        "preview_title": "Figure Summary: demo-ion v1",
        "preview_id": "demo-ion v1 · Panel A",
        "boundary": "Descriptive only. No identity or concentration claim.",
        "preview": [
            ("Source", "Saved example table (row s1); panel A, v1."),
            ("Observation", "Mean relative signal: outer 14, inner 10.\nOuter / inner ratio: 1.4."),
            ("Units & scope", "Pixels in one fictional section.\nbio_n = 1; descriptive only."),
            ("Claim limit", "No inferential test. The result does not\nestablish identity or concentration."),
            ("Reuse check", "Match the table to the figure version.\nIf unverified, report table values separately."),
        ],
        "preview_desc": "A fictional Figure Summary identifies the stored evidence, relative ratio, independent biological sample count, and claim limits.",
    },
}

for _slug, _spec in DATA.items():
    _spec["icon"] = '<g transform="translate(2 29) scale(.70)">' + ICONS[_slug] + '</g>'

DATA["spatial-omics-paper-reading"]["mermaid"] = '''flowchart LR
 A["01 Verify source"] --> G{"Usable source?"}
 G -->|Full text| F["Use methods, panels, and captions"]
 G -->|Partial| P["Use available evidence; label gaps"]
 G -->|Absent| S["Request the source; STOP"]
 F --> B["02 Trace design"]
 P --> B
 B --> C["03 Read figures"]
 C --> D["04 Capture methods"]
 D --> E["05 Save report"]
 E -.-> H["Optional handoff on request"]
'''
DATA["analysis-explainer"]["mermaid"] = '''flowchart LR
 A["01 Locate evidence · read-only"] --> B["02 Explain method · unit, bio_n, parameters"]
 B --> C["03 Separate claims"]
 C --> D["04 Deliver Figure Summary"]
 D --> S["STOP · No rerun, no redraw"]
'''
