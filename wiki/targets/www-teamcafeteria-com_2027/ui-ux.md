---
title: "UI & UX Architecture: www-teamcafeteria-com_2027"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-teamcafeteria-com_2027

## Overview & Design Identity
- **Target**: `www-teamcafeteria-com_2027` (**2027 — a [cafeteria] report**)
- **Production URL**: [https://www.teamcafeteria.com/2027](https://www.teamcafeteria.com/2027)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×2616px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#0000ff`)
- **Summary**: 1,423 people told us what 2027 looks like. A scroll-driven [cafeteria] report.
- **Total Clean CSS Variables Extracted**: `216` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Satoshi 2027`
- **Body Font Stack**: `Satoshi 2027`
- **Monospace / Technical Font Stack**: `Rubik Mono One`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 81px`, `line-height: 89.1px`, `font-weight: 500`); rule `h1` (`font-size: clamp(2rem,5vw,3rem)`, `line-height: 1.1`, `font-weight: 700`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 57.6px`, `line-height: 63.36px`, `font-weight: 500`); rule `h2` (`font-size: clamp(1.5rem,3.5vw,2rem)`, `line-height: 1.2`, `font-weight: 700`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 500`); CSS variables `--font-size-vw-body: 1.5vw`, `--font-size-body: clamp(1.125rem, var(--font-size-vw-body), 1.5rem)`; rule `p` (`font-weight: 500`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 500`); CSS variables `--font-family-mono: "Roboto Mono", monospace`, `--mono: "Roboto Mono 2027",ui-monospace,Menlo,monospace`; rule `,.label` (`font-size: var(--font-size-lg)`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#fcfcfc` | live computed `footer` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#1d1b1b` | live computed `nav` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0000ff` | `.hover:hover>.btn-link { color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#686b6b` | `var(--c-text-mute)` in `:root` |
| **Structural Hairline Border** | `#232020` | `var(--c-border-strong)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-gray-100-rgb` | `252 252 252` | Brand / Palette Token |
| `--color-gray-200-rgb` | `248 248 249` | Brand / Palette Token |
| `--color-gray-300-rgb` | `241 241 247` | Brand / Palette Token |
| `--color-gray-400-rgb` | `224 226 231` | Brand / Palette Token |
| `--color-gray-500-rgb` | `215 216 222` | Brand / Palette Token |
| `--color-gray-600-rgb` | `178 188 189` | Brand / Palette Token |
| `--color-gray-700-rgb` | `100 113 121` | Brand / Palette Token |
| `--color-gray-800-rgb` | `48 48 50` | Brand / Palette Token |
| `--color-gray-900-rgb` | `35 32 32` | Brand / Palette Token |
| `--color-gray-1000-rgb` | `23 21 21` | Brand / Palette Token |
| `--color-green-200-rgb` | `203, 255, 218` | Brand / Palette Token |
| `--color-green-400-rgb` | `53 255 146` | Brand / Palette Token |
| `--color-green-500-rgb` | `37 100 66` | Brand / Palette Token |
| `--color-blue-100-rgb` | `160 216 255` | Brand / Palette Token |
| `--color-blue-500-rgb` | `37 99 235` | Brand / Palette Token |
| `--color-pink-100-rgb` | `255 223 254` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `www-teamcafeteria-com_2027`)**:
   - Landmark `<header class="site-header">` (`1440x58px`) hosting `2027 — a [cafeteria] report` navigation (`ask AI → · studies →`), DOM attributes (`data-nav-flow-ready="true"`, `data-nav-pill-ready="true"`, `data-cta-location="use_cases_menu"`, `data-track-cta`), and stylesheet rule `font-face { font-family:Anton;font-weight:100 900;font-display:swap;src:url(/_astro/... }`.
2. **Hero Stage & Focal Lead (<article.report-doc> — `2027 — a [cafeteria] report`)**:
   - Landmark `<article class="report-doc">` presenting display lead `2027 — a [cafeteria] report` and copy excerpt *"we asked 1,423 young consumers about the year ahead"* over `#000000` canvas and `#fcfcfc` ink.
3. **Primary Showcase & Content Grid (<section.fact> — `Shoes`)**:
   - Landmark `<section class="fact">` rendering section `Shoes` with copy *"Back to the experience"*, asset references (`favicon.svg`, `Satoshi-Medium.dlbj618m.woff2`, `Satoshi-Bold.BRirVCsc.woff2`, `Satoshi-Black.BWj4aoZT.woff2`), and grid rule `body.report2027-page .report2027 { line-height:normal }`.
4. **Interactive Detail & Feature Matrix (<section.fact:nth(2)> — `Spend`)**:
   - Landmark `<section class="fact">` framing `Spend` and `Collabs` (*"277 hours of conversation"*) with `#1d1b1b` surface cards, `#0000ff` accents, and `track { position:relative;width:1px;pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.teamcafeteria.com/2027`)**:
   - Landmark `<footer class="footer theme-dark">` anchoring `2027 — a [cafeteria] report` footer links (`ask AI → · studies →`), copy *"50% female · 48% male · median age 20"*, and `#232020` structural dividers.
