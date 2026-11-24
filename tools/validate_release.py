#!/usr/bin/env python3
"""Offline structural, metadata, and privacy checks for the public release.

Requires Python 3.10+, PyYAML and Pillow. If the repository contains a PDF,
Poppler's pdftotext is also required. Set RELEASE_DENYLIST_FILE to a private
UTF-8 file outside this repository, with one forbidden literal per line, to
check owner-specific strings without adding those strings to the repository.
"""

import argparse
import json
import os
import re
import shutil
import struct
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree as ET

import yaml
from PIL import Image

BASE = Path(__file__).resolve().parents[1]
SKILLS = BASE / "skills"
ASSETS = BASE / "assets" / "release"
NS = "{http://www.w3.org/2000/svg}"
SKILL_IDS = (
    "spatial-omics-paper-reading",
    "plant-omics-preflight",
    "plant-spatial-omics-analysis",
    "analysis-explainer",
    "scientific-figure-standard",
    "plant-omics-thesis-writing",
)
ROOTS = {
    ".claude-plugin", ".gitignore", "CITATION.cff", "LICENSE",
    "README.md", "README.zh-CN.md", "assets", "docs", "skills", "tools",
}
PROJECT = "Plant Omics Research Skills"
PLUGIN = "plant-omics-research-skills"
OWNER = "Qian Wang"
RELEASE = "1.0.0"
REPO = f"https://github.com/carrot-wangqian/{PLUGIN}"
KEYWORDS = {
    "plant-omics", "spatial-omics", "mass-spectrometry-imaging", "single-cell",
    "agent-skills", "reproducible-research",
}
BOUNDARIES = {
    "analysis-explainer": "not for reading external published papers or redrawing figures.",
    "scientific-figure-standard": "not for biological interpretation alone or rerunning upstream analyses.",
}
# Keep complete rejected phrases out of the public source being checked.
FORMER_ASSET_DIR = "visual" + "-pilot"
DRAFT_MARKERS = (
    "no open-source license " + "has been assigned",
    "GitHub publication is not part " + "of this handoff",
    "尚未指定" + "开源许可证",
    "本次交付不包含 " + "GitHub 发布",
    FORMER_ASSET_DIR,
    "release " + "candidate",
    "发布" + "候选版",
    "cloud " + "workspace",
    "private source documents " + "inspected separately",
    "no license " + "assigned",
    "do not " + "push",
)
SUITE = {
    "hero-banner": (1280, 640),
    "suite-architecture": (1600, 900),
    "cards-overview": (1680, 1136),
}
ITEMS = {"card": (1080, 1080), "workflow": (1400, 900), "report-preview": (1200, 840)}
FONT_STACKS = {
    ('DejaVu Serif', 'Georgia', 'Times New Roman', 'serif'),
    ('DejaVu Sans', 'Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Helvetica', 'Arial', 'sans-serif'),
    ('DejaVu Sans Mono', 'ui-monospace', 'SFMono-Regular', 'Menlo', 'Consolas', 'monospace'),
}
PRIVATE_PATTERNS = {
    "absolute local path": r"(?i)(?:(?<![A-Z0-9])(?:[A-Z]:[\\/](?![\\/]))(?:[^\s\"'<>]|\\ )+|(?<![A-Za-z0-9.:/-])/(?:home|Users|workspace|mnt|user_notes)/[^\s\"'<>]+|file:\/\/[^\s\"'<>]+)",
    "email address": r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",
    "internal service identifier": r"(?i)\b(?:libfile_|sediment://|ccarenv_|sentinel_)[\w.-]+",
    "API credential": r"\b(?:sk-(?:proj-)?[A-Za-z0-9_-]{16,}|gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[A-Z0-9]{16})\b",
    "private key": r"-----BEGIN (?:[A-Z0-9]+ )*PRIVATE KEY-----",
}
LINK_RE = re.compile(r'\]\(\s*(<[^>]+>|(?:[^()\s]+|\([^()]*\))+)(?:\s+[\'"][^\n]*?[\'"])?\s*\)')
REFERENCE_RE = re.compile(r'^\s{0,3}\[[^\]\n]+\]:\s*(<[^>]+>|\S+)', re.M)
HTML_LINK_RE = re.compile(r'\b(?:href|src)\s*=\s*(["\'])(.*?)\1', re.I)
TEXT_TYPES = {".md", ".mmd", ".py", ".svg", ".txt", ".tsv", ".csv", ".json", ".yml", ".yaml", ".toml", ".html", ".cff"}
PUBLIC_TEXT_NAMES = {".gitignore", "LICENSE"}


def require(condition, detail):
    if not condition:
        raise ValueError(str(detail))


def fmt(path):
    return path.relative_to(BASE).as_posix()


def files():
    return sorted(p for p in BASE.rglob("*") if p.is_file() and ".git" not in p.relative_to(BASE).parts)


def md_links(path):
    content = path.read_text(encoding="utf-8")
    # Fenced and inline code are examples, not Markdown links.
    content = re.sub(r'(?ms)^\s{0,3}(`{3,}|~{3,})[^\n]*\n.*?^\s{0,3}\1[ \t]*$', '', content)
    content = re.sub(r'`+[^`\n]+`+', '', content)
    targets = LINK_RE.findall(content)
    targets += REFERENCE_RE.findall(content)
    targets += [dest for _, dest in HTML_LINK_RE.findall(content)]
    # Include local inline links whose destination contains literal spaces.
    targets += re.findall(r'\]\(\s*([^<>"\'()\n]+[ \t][^<>"\'()\n]+)\s*\)', content)
    checked = 0
    for dest in set(targets):
        dest = dest.strip()
        if dest.startswith("<") and dest.endswith(">"):
            dest = dest[1:-1]
        if dest.startswith(("http://", "https://", "#")):
            continue
        uri = urlsplit(dest)
        require(not uri.netloc and not uri.scheme and not uri.path.startswith(("/", "\\")),
                f"{fmt(path)}: nonrelative link {dest!r}")
        resolved = (path.parent / unquote(uri.path)).resolve()
        require(resolved.is_relative_to(BASE) and resolved.exists(), f"{fmt(path)}: broken link {dest!r}")
        checked += 1
    return checked


def check_tree():
    entries = {p.name for p in BASE.iterdir()} - {".git"}
    require(entries == ROOTS, f"Top-level entries: missing {sorted(ROOTS - entries)}; unexpected {sorted(entries - ROOTS)}")
    require((BASE / "docs" / "validation.md").is_file(), "Missing public validation guide")
    require(not any((BASE / "docs" / n).exists() for n in ("review-record.md", "release-guide.md")),
            "Obsolete internal guide present")
    require({p.name for p in SKILLS.iterdir()} == set(SKILL_IDS), "Wrong Skill set")
    require(not (BASE / "assets" / FORMER_ASSET_DIR).exists(), "Legacy V1 visual pilot still exists")
    for p in BASE.rglob("*"):
        if ".git" not in p.relative_to(BASE).parts:
            require(not p.is_symlink(), f"{fmt(p)}: unexpected symlink")
    for name in SKILL_IDS:
        root = SKILLS / name
        p = root / "SKILL.md"
        parts = p.read_text(encoding="utf-8").split("---", 2)
        require(len(parts) == 3 and not parts[0].strip() and parts[2].strip(), f"{fmt(p)}: bad front matter")
        fm = yaml.safe_load(parts[1])
        require(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) and len(name) <= 64,
                f"{fmt(p)}: invalid name")
        require(isinstance(fm, dict) and fm.get("name") == name and
                isinstance(fm.get("description"), str) and 1 <= len(fm["description"].strip()) <= 1024,
                f"{fmt(p)}: invalid name or description metadata")
        if name in BOUNDARIES:
            require(fm["description"].strip().casefold().endswith(BOUNDARIES[name]),
                    f"{fmt(p)}: missing trigger boundary")
        for item in root.rglob("*"):
            if item.is_file():
                require(item.suffix.lower() not in {".png", ".svg", ".mmd", ".pdf", ".jpg", ".jpeg", ".webp", ".gif"},
                        f"{fmt(item)}: visual asset in Skill folder")
    for locale, other in [("README.md", "README.zh-CN.md"), ("README.zh-CN.md", "README.md")]:
        rendered = (BASE / locale).read_text(encoding="utf-8")
        require(f"({other})" in rendered, f"{locale}: missing translation link")
        for name in SKILL_IDS:
            require(f"(skills/{name}/SKILL.md)" in rendered, f"{locale}: missing link to {name}")
    for item in ("figure-summary.md", "synthetic-summary-source.tsv"):
        explainer = SKILLS / "analysis-explainer" / "references" / item
        figure = SKILLS / "scientific-figure-standard" / "references" / item
        require(explainer.read_bytes() == figure.read_bytes(), f"Shared fixture differs: {item}")
    return sum(md_links(p) for p in files() if p.suffix.lower() == ".md")


def unique_json_object(pairs):
    data = {}
    for key, value in pairs:
        require(key not in data, "Duplicate marketplace JSON key")
        data[key] = value
    return data


def check_metadata():
    license_text = (BASE / "LICENSE").read_text(encoding="utf-8")
    flat_license = " ".join(license_text.split())
    require(license_text.strip().startswith("MIT License") and
            f"Copyright (c) 2026 {OWNER}" in license_text and
            all(clause in flat_license for clause in (
                "Permission is hereby granted, free of charge",
                "The above copyright notice and this permission notice",
                'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND',
                "OTHER DEALINGS IN THE SOFTWARE.",
            )), "LICENSE: missing MIT text or approved copyright")

    cff = yaml.safe_load((BASE / "CITATION.cff").read_text(encoding="utf-8"))
    require(isinstance(cff, dict), "CITATION.cff: expected YAML mapping")
    for field, expected in {
        "cff-version": "1.2.0", "title": PROJECT, "version": RELEASE, "license": "MIT",
        "date-released": "2026-11-24", "repository-code": REPO,
    }.items():
        actual = cff.get(field)
        if field == "date-released":
            actual = str(actual)
        require(actual == expected, f"CITATION.cff: wrong {field}")
    require(isinstance(cff.get("message"), str) and cff["message"].strip(),
            "CITATION.cff: missing citation message")
    require(cff.get("authors") == [{"family-names": "Wang", "given-names": "Qian"}],
            "CITATION.cff: author must contain approved name only")
    keywords = cff.get("keywords")
    require(isinstance(keywords, list) and all(isinstance(v, str) for v in keywords) and
            set(keywords) == KEYWORDS and len(keywords) == len(KEYWORDS),
            "CITATION.cff: wrong domain keywords")

    index = BASE / ".claude-plugin" / "marketplace.json"
    market = json.loads(index.read_text(encoding="utf-8"), object_pairs_hook=unique_json_object)
    owners = ({"name": OWNER}, {"name": OWNER, "url": REPO.rsplit("/", 1)[0]})
    require(isinstance(market, dict) and market.get("name") == PLUGIN and
            market.get("owner") in owners, "Marketplace: wrong name or owner")
    plugins = market.get("plugins")
    require(isinstance(plugins, list) and len(plugins) == 1 and isinstance(plugins[0], dict),
            "Marketplace: expected one plugin record")
    plugin = plugins[0]
    for field, expected in {
        "name": PLUGIN, "version": RELEASE, "author": {"name": OWNER},
        "license": "MIT", "repository": REPO, "source": "./",
    }.items():
        require(plugin.get(field) == expected, f"Marketplace plugin: wrong {field}")
    require(isinstance(plugin.get("description"), str) and plugin["description"].strip(),
            "Marketplace plugin: missing description")
    source_root = (index.parent.parent / plugin["source"]).resolve()
    require(source_root == BASE and source_root.is_dir(),
            "Marketplace plugin: relative source must resolve to repository root")
    expected_paths = {f"./skills/{slug}" for slug in SKILL_IDS}
    skills = plugin.get("skills")
    require(isinstance(skills, list) and all(isinstance(v, str) for v in skills) and
            len(skills) == len(expected_paths) and set(skills) == expected_paths,
            "Marketplace plugin: expected the six distinct local Skill paths")
    for ref in skills:
        target = (source_root / ref).resolve()
        require(target.parent == SKILLS and target.is_dir() and (target / "SKILL.md").is_file(),
                f"Marketplace plugin: invalid Skill path {ref!r}")


def number(v):
    return float(re.sub(r"px$", "", v or ""))


def dimension(v, target):
    try:
        return number(v) == target
    except ValueError:
        return v == "100%"


def style(node):
    css = {}
    for s in (node.get("style") or "").split(";"):
        key, sep, value = s.partition(":")
        if sep:
            css[key.strip()] = value.strip()
    return {**node.attrib, **css}


def rect_fill(root, size, stem, stempath):
    hero = stem == "hero-banner"
    accepted = {"#112d35", "#173c43"} if hero else {"#f8f6ef"}
    # The backing rectangle must precede actual SVG content.
    graphical = next((n for n in root if n.tag not in {
        NS + "title", NS + "desc", NS + "defs", NS + "style", NS + "metadata"
    }), None)
    require(graphical is not None and graphical.tag == NS + "rect", f"{stempath}: missing first background rect")
    d = style(graphical)
    require(d.get("fill", "").lower() in accepted and number(d.get("x", "0")) == 0 and
            number(d.get("y", "0")) == 0 and all(dimension(d.get(k), s) for k, s in zip(("width","height"),size)) and
            number(d.get("opacity", "1")) == 1 and number(d.get("fill-opacity", "1")) == 1,
            f"{stempath}: first background rect is not full-size and opaque with approved fill")
    if hero:
        return
    for rt in root.iter(NS + "rect"):
        d = style(rt)
        if d.get("stroke", "").lower() != "#cad5d5":
            continue
        if number(d.get("stroke-width", "1")) != 1 or number(d.get("stroke-opacity", "1")) != 1:
            continue
        for inset in (0, 0.5):
            if (number(d.get("x", "0")) == number(d.get("y", "0")) == inset and
               dimension(d.get("width"), size[0] - 2 * inset) and
               dimension(d.get("height"), size[1] - 2 * inset)):
                return
    raise ValueError(f"{stempath}: missing 1 px #cad5d5 perimeter rect")


def check_svg(path, size, stem):
    label = fmt(path)
    root = ET.parse(path).getroot()
    require(root.tag == NS + "svg", f"{label}: not SVG")
    require(all(dimension(root.get(k), s) and root.get(k) != "100%" for k, s in zip(("width","height"),size)),
            f"{label}: expected {size[0]}×{size[1]}")
    box = root.get("viewBox")
    if box:
        require(tuple(map(float, re.split(r"[\s,]+", box.strip()))) == (0, 0, *size), f"{label}: viewBox mismatch")
    desc = root.find(NS + "desc")
    require(desc is not None and "".join(desc.itertext()).strip(), f"{label}: missing nonempty <desc>")
    rect_fill(root, size, stem, label)
    declared = []
    for node in root.iter():
        for key in ("href", "{http://www.w3.org/1999/xlink}href"):
            val = node.get(key)
            require(not val or val.startswith("#"), f"{label}: external or embedded SVG dependency")
        require(node.tag not in {NS + "script", NS + "foreignObject", NS + "image"},
                f"{label}: unsupported non-vector or executable SVG node")
        family = style(node).get("font-family")
        if family:
            declared.append(family)
        if node.tag == NS + "style":
            declared += re.findall(r"font-family\s*:\s*([^;}]+)", node.text or "")
    require(declared, f"{label}: no font stacks declared")
    for family in declared:
        normalized = tuple(x.strip().strip("'\"") for x in family.split(","))
        require(normalized in FONT_STACKS, f"{label}: incomplete or unapproved font stack: {family!r}")
    text = " ".join("".join(n.itertext()) for n in root.iter(NS + "text"))
    require(text.strip(), f"{label}: no editable text")
    require(not re.search(r"[\u3400-\u9fff\u3040-\u30ff\uac00-\ud7af]", text),
            f"{label}: visible text must be English")
    if stem == "report-preview":
        marker = re.sub(r"\s+", " ", text).upper()
        require("SYNTHETIC EXAMPLE · NOT REAL DATA" in marker, f"{label}: synthetic preview marker missing")
    if stem == "workflow":
        require(not re.search(r"\b(?:leaf edge|P0[1-4]|demo-ion|synthetic panel 2B)\b", text, re.I),
                f"{label}: synthetic example embedded in a general workflow")


def check_png(path, size):
    label = fmt(path)
    with path.open("rb") as stream:
        header = stream.read(24)
    require(len(header) == 24 and header[:8] == b"\x89PNG\r\n\x1a\n" and
            header[8:16] == b"\x00\x00\x00\x0dIHDR" and struct.unpack(">II", header[16:24]) == size,
            f"{label}: invalid PNG header or dimensions, expected {size}")
    with Image.open(path) as img:
        img.verify()
    with Image.open(path) as img:
        require(img.convert("RGBA").getchannel("A").getextrema() == (255, 255), f"{label}: PNG is not opaque")
        if path.stem != "hero-banner":
            rgb = img.convert("RGB")
            w, h = rgb.size
            border = ((202, 202), (213, 213), (213, 213))
            edges = ((0, 0, w, 1), (0, h - 1, w, h), (0, 0, 1, h), (w - 1, 0, w, h))
            require(all(rgb.crop(edge).getextrema() == border for edge in edges),
                    f"{label}: missing the approved #cad5d5 PNG perimeter")


def check_mermaid(path):
    label = fmt(path)
    src = path.read_text(encoding="utf-8-sig")
    require(re.search(r"^\s*(?:flowchart|graph)\s+(?:LR|RL|TB|TD|BT)\s*$", src, re.M) and
            re.search(r"(?:-->|-\.->|==>)", src), f"{label}: malformed or empty Mermaid graph source")


def check_assets():
    expected = set()
    for stem, size in SUITE.items():
        for suffix in ("svg", "png"):
            expected.add(f"{stem}.{suffix}")
        check_svg(ASSETS / f"{stem}.svg", size, stem)
        check_png(ASSETS / f"{stem}.png", size)
    for name in SKILL_IDS:
        for stem, size in ITEMS.items():
            for suffix in ("svg", "png"):
                expected.add(f"{name}/{stem}.{suffix}")
            check_svg(ASSETS / name / f"{stem}.svg", size, stem)
            check_png(ASSETS / name / f"{stem}.png", size)
    diagrams = ["suite-architecture.mmd", *(f"{name}/workflow.mmd" for name in SKILL_IDS)]
    for diagram in diagrams:
        expected.add(diagram)
        check_mermaid(ASSETS / diagram)
    actual = {p.relative_to(ASSETS).as_posix() for p in ASSETS.rglob("*") if p.is_file() and p.suffix.lower() != ".pdf"}
    require(actual == expected, f"Unexpected or missing visual assets: {sorted(actual ^ expected)}")
    return len(SUITE) + len(SKILL_IDS) * len(ITEMS), len(diagrams)


def privacy_checks(repository_files, supplementary_pdfs=()):
    deny = []
    deny_file = os.environ.get("RELEASE_DENYLIST_FILE")
    if deny_file:
        path = Path(deny_file).expanduser().resolve()
        require(not path.is_relative_to(BASE), "Owner denylist must remain outside repository")
        deny = [item.strip().casefold() for item in path.read_text(encoding="utf-8").splitlines() if item.strip()]
    patterns = {label: re.compile(pattern) for label, pattern in PRIVATE_PATTERNS.items()}
    draft_markers = [marker.casefold() for marker in DRAFT_MARKERS]
    scanned = 0
    for p in dict.fromkeys((*repository_files, *supplementary_pdfs)):
        local = p.is_relative_to(BASE)
        label_path = fmt(p) if local else p.name
        require(p.suffix.lower() in TEXT_TYPES | {".png", ".pdf"} or p.name in PUBLIC_TEXT_NAMES,
                f"{label_path}: unapproved release file type")
        if local:
            require(not any(part.lower() in {"private", ".local", "staging", "scratch"} for part in p.relative_to(BASE).parts),
                    f"{label_path}: local-only path in release")
        value = label_path
        if p.suffix.lower() in TEXT_TYPES or p.name in PUBLIC_TEXT_NAMES:
            value += "\n" + p.read_text(encoding="utf-8-sig")
        elif p.suffix.lower() == ".png":
            with Image.open(p) as img:
                value += "\n" + "\n".join(v for v in img.info.values() if isinstance(v, str))
        elif p.suffix.lower() == ".pdf":
            pdftotext = shutil.which("pdftotext")
            require(pdftotext is not None, "pdftotext is required to scan the review PDF")
            out = subprocess.run([pdftotext, "-layout", str(p), "-"], check=True, capture_output=True)
            value += "\n" + out.stdout.decode("utf-8", errors="replace")
            pdfinfo = shutil.which("pdfinfo")
            if pdfinfo:
                out = subprocess.run([pdfinfo, str(p)], check=True, capture_output=True)
                value += "\n" + out.stdout.decode("utf-8", errors="replace")
        for label, pattern in patterns.items():
            require(not pattern.search(value), f"{label_path}: possible {label} (matched content hidden)")
        normal = value.casefold()
        for literal in deny:
            require(literal not in normal, f"{label_path}: owner denylist match (matched content hidden)")
        if local:
            collapsed = " ".join(normal.split())
            require(not any(marker in collapsed for marker in draft_markers),
                    f"{label_path}: legacy draft wording or path")
        scanned += 1
    return scanned, len(deny)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--review-pdf", type=Path, action="append", default=[],
                        help="also scan a separately delivered review PDF")
    opts = parser.parse_args()
    pdfs = [p.resolve() for p in opts.review_pdf]
    require(all(p.is_file() and p.suffix.lower() == ".pdf" for p in pdfs), "Missing or invalid review PDF")
    link_count = check_tree()
    check_metadata()
    pair_count, mermaid_count = check_assets()
    scanned, deny_count = privacy_checks(files(), pdfs)
    print("PASS: approved MIT license, CFF v1.2.0, and Marketplace metadata for v1.0.0 (6 local Skills)")
    print("PASS: 6 Skill folders, both README editions, and shared fixtures")
    print(f"PASS: {link_count} Markdown relative link targets")
    print(f"PASS: {pair_count} SVG/PNG pairs: dimensions, desc, font stacks, backing, border and opacity")
    print(f"PASS: {mermaid_count} editable Mermaid sources; V1 visual pilots absent")
    print("PASS: no legacy draft wording or paths in release files")
    print(f"PASS: private-string scan across {scanned} files ({deny_count} optional owner denylist entries)")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, ET.ParseError, subprocess.CalledProcessError, yaml.YAMLError) as error:
        sys.exit(f"FAIL: {error}")
