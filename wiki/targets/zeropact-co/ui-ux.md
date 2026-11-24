---
title: "UI & UX Architecture: zeropact-co"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: zeropact-co

## Overview & Design Identity
- **Target**: `zeropact-co` (**ZeroPact · LCA, Product Carbon Footprint, DPP, GLEC & EmpCo**)
- **Production URL**: [https://zeropact.co](https://zeropact.co)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#4d67fc`)
- **Summary**: LCA, Product Carbon Footprint, Digital Product Passport (DPP), GLEC and EmpCo intelligence and solutions for PIM and PXM companies servin...
- **Total Clean CSS Variables Extracted**: `148` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Zalando Sans Expanded`
- **Body Font Stack**: `DM Sans`
- **Monospace / Technical Font Stack**: `DM Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 112px`, `line-height: 112px`, `font-weight: 600`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 52px`, `line-height: 56.16px`, `font-weight: 600`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 1.25rem`, `letter-spacing: -.01em`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`line-height: var(--leading-relaxed)`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-mono: "DM Mono", ui-monospace, SFMono-Regular, monospace`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`; rule `small` (`font-size: 10px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0000ff` | `#company .text-signal { color: blue }` (`#0000ff`) |
| **Elevated Surface / Card Substrate** | `#000000` | `80 { background-color: black }` (`#000000`) |
| **Interactive Accent / Highlight** | `#4d67fc` | `.tf-tower-comet-b { stroke: #4d67fc }` |
| **Secondary / Muted Copy** | `#800080` | `.text-violet-2 { color: purple }` (`#800080`) |
| **Structural Hairline Border** | `#ffda76` | `.mi-method-chain li:last-child { border-color: #ffda76 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--radius` | `.375rem` | Elevation / Border Token |
| `--background` | `oklch(15% .007 271)` | Canvas / Surface Token |
| `--foreground` | `oklch(94.6% 0 0)` | Typography Ink Token |
| `--card` | `oklch(18.6% .009 264.3)` | Color / Atmospheric Token |
| `--card-foreground` | `oklch(94.6% 0 0)` | Typography Ink Token |
| `--popover` | `oklch(18.6% .009 264.3)` | Color / Atmospheric Token |
| `--popover-foreground` | `oklch(94.6% 0 0)` | Typography Ink Token |
| `--primary` | `oklch(79.7% .101 168.5)` | Brand / Palette Token |
| `--primary-foreground` | `oklch(15% .007 271)` | Typography Ink Token |
| `--secondary` | `oklch(21.3% .013 264.3)` | Brand / Palette Token |
| `--secondary-foreground` | `oklch(94.6% 0 0)` | Typography Ink Token |
| `--muted` | `oklch(21.3% .013 264.3)` | Color / Atmospheric Token |
| `--muted-foreground` | `oklch(68.9% 0 0)` | Typography Ink Token |
| `--accent` | `oklch(58.3% .222 270.3)` | Brand / Palette Token |
| `--accent-foreground` | `oklch(97.3% .003 106.4)` | Typography Ink Token |
| `--destructive` | `oklch(65.8% .231 35)` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.inset-x-0> — `zeropact-co`)**:
   - Landmark `<header class="inset-x-0 top-0">` (`1440x73px`) hosting `ZeroPact · LCA, Product Carbon Footp` navigation (`Explore · Intelligence ▾ · Product · Mobility · Platform & APIs`), DOM attributes (`data-precedence="default"`, `data-precedence="default"`, `data-artifact-kind="dwl_content_hash"`, `data-artifact-id="ab2d1433faa58eadc83ca..."`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.climate-hero> — `ZeroPact.`)**:
   - Landmark `<section class="climate-hero bg-paper">` presenting display lead `ZeroPact.` and copy excerpt *"DEEPTECH / CLIMATE DATA INTELLIGENCE"* over `#ffffff` canvas and `#0000ff` ink.
3. **Primary Showcase & Content Grid (<section.border-line> — `ZeroPact .`)**:
   - Landmark `<section class="border-line py-24">` rendering section `ZeroPact .` with copy *"Deeptech / Climate data intelligence"*, asset references (`zeropact-logotype.png`, `climate-data-landscape-light-CJil...`, `climate-data-landscape-digital-B-...`, `wired_logo.png`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.bg-paper> — `Product footprints, green claims a`)**:
   - Landmark `<section class="bg-paper py-24">` framing `Product footprints, green claims and transport em...` and `Environmental intelligence, built into your platf...` (*"From climate data to decisions."*) with `#000000` surface cards, `#4d67fc` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.border-line> — `https://zeropact.co`)**:
   - Landmark `<footer class="border-line bg-ink">` anchoring `ZeroPact · LCA, Product Carbon F` footer links (`Explore · Intelligence ▾ · Product · Mobility · Platform & APIs`), copy *"Audit-grade AI intelligence that transforms complex environm"*, and `#ffda76` structural dividers.
