---
title: "UI & UX Architecture: thebranx-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: thebranx-com

## Overview & Design Identity
- **Target**: `thebranx-com` (**The branding agency for startups, AI & SaaS - The Branx**)
- **Production URL**: [https://thebranx.com](https://thebranx.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#050608` ink, `#0000ff` accent)
- **Summary**: The Branx builds category-defining brands and websites for AI, SaaS and B2B tech startups: strategy, identity, web design and motion, fro...
- **Total Clean CSS Variables Extracted**: `199` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Marcellus`
- **Body Font Stack**: `Helvetica Neue`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 48.96px`, `line-height: 47.9808px`, `font-weight: 300`, `letter-spacing: -1.4688px`); CSS variables `--bx-display-ls: -.01em`, `--bx-fs-display: clamp(44px, 5.6vw, 120px)`, `--bx-lh-display: 1.05`; rule `h1` (`font-size: var(--bx-fs-statement)`, `line-height: var(--bx-lh-statement)`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 48.96px`, `line-height: 49.9392px`, `font-weight: 300`, `letter-spacing: -0.4896px`); CSS variables `--bx-fs-h2: clamp(32px, 3.6vw, 72px)`, `--text-3xl: var(--bx-fs-h2)`, `--text-3xl--line-height: calc(2.25 / 1.875)`; rule `h2` (`font-size: var(--text-xl)`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`); CSS variables `--bx-fs-body: 16px`, `--bx-lh-body: 1.6`, `--leading-body: var(--bx-lh-body)`; rule `p` (`font-size: var(--bx-fs-lead)`, `line-height: var(--bx-lh-body)`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`); CSS variables `--bx-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace`, `--bx-fs-small: 15px`, `--font-mono: var(--bx-mono)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#050608` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffff00` | `.bg-yellow-200 { background-color: yellow }` (`#ffff00`) |
| **Interactive Accent / Highlight** | `#0000ff` | `.bx-btn--primary { background-color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#85888e` | `var(--bx-muted)` in `:root` |
| **Structural Hairline Border** | `#232426` | `var(--bx-line)` in `:root` |
| **Variable Token (`--bx-gray-1`)** | `#151618` | `var(--bx-gray-1)` in `:root` |
| **Variable Token (`--bx-gray-2`)** | `#202124` | `var(--bx-gray-2)` in `:root` |
| **Variable Token (`--bx-gray-3`)** | `#2c2d31` | `var(--bx-gray-3)` in `:root` |
| **Variable Token (`--bx-blue`)** | `#122ff7` | `var(--bx-blue)` in `:root` |
| **Variable Token (`--bx-accent`)** | `#326cff` | `var(--bx-accent)` in `:root` |
| **Variable Token (`--bx-success`)** | `#51e08a` | `var(--bx-success)` in `:root` |
| **Variable Token (`--bx-attention`)** | `#de8637` | `var(--bx-attention)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bx-ink` | `#fff` | Typography Ink Token |
| `--bx-ink-rgb` | `255, 255, 255` | Typography Ink Token |
| `--bx-paper` | `#050608` | Canvas / Surface Token |
| `--bx-paper-rgb` | `5, 6, 8` | Canvas / Surface Token |
| `--bx-muted` | `#85888e` | Color / Atmospheric Token |
| `--bx-line` | `#232426` | Color / Atmospheric Token |
| `--bx-gray-1` | `#151618` | Color / Atmospheric Token |
| `--bx-gray-2` | `#202124` | Color / Atmospheric Token |
| `--bx-gray-3` | `#2c2d31` | Color / Atmospheric Token |
| `--bx-blue` | `#122ff7` | Color / Atmospheric Token |
| `--bx-blue-ink` | `#fff` | Typography Ink Token |
| `--bx-cta-ink` | `#050608` | Typography Ink Token |
| `--bx-accent` | `#326cff` | Brand / Palette Token |
| `--bx-focus` | `var(--bx-accent)` | Design System Custom Token |
| `--bx-success` | `#51e08a` | Color / Atmospheric Token |
| `--bx-attention` | `#de8637` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.bx-navbar> — `thebranx-com`)**:
   - Landmark `<header class="bx-navbar">` (`1440x73px`) hosting `The branding agency for startups, AI` navigation (`Brand identity · Web design & dev. · Strategy & messaging · Motion design · Product naming`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-ch2css="true"`, `data-bx-nav`), and stylesheet rule `llus_b0edf5b9-module__eeLBqG__cla... { font-family:Marcellus,Marcellus Fallback;font-style:normal;font-weight:400 }`.
2. **Hero Stage & Focal Lead (<section.bx-imm> — `The tech branding agency for AI & `)**:
   - Landmark `<section class="bx-imm">` presenting display lead `The tech branding agency for AI & SaaS startups` and copy excerpt *"THE STARTUP BRANDING AGENCY"* over `#ffffff` canvas and `#050608` ink.
3. **Primary Showcase & Content Grid (<section.bx-section> — `The Branx turns complex tech into `)**:
   - Landmark `<section class="bx-section">` rendering section `The Branx turns complex tech into category-defini...` with copy *"The startup branding agency"*, asset references (`ec2f4458eb06f74e-s.p.217u6tza6bra...`, `0u5m-o-ck0mfs.css`, `44nobezqmqmh0.css`, `194ug3jq7qzm9.js`), and grid rule `ellus_b0edf5b9-module__eeLBqG__va... { --font-marcellus:"Marcellus", "Marcellus Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.bx-philosophy> — `AI made it easy to launch a brand.`)**:
   - Landmark `<section class="bx-philosophy">` framing `AI made it easy to launch a brand. It made it har...` and `Start with the identity. Add the rest when you're...` (*"The tech branding agency"*) with `#ffff00` surface cards, `#0000ff` accents, and `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.bx-footer> — `https://thebranx.com`)**:
   - Landmark `<footer class="bx-footer">` anchoring `The branding agency for startups` footer links (`Brand identity · Web design & dev. · Strategy & messaging · Motion design · Product naming`), copy *"for AI & SaaS startups"*, and `#232426` structural dividers.
