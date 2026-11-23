---
title: "UI & UX Architecture: www-ataccama-com_fwrd2026"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-ataccama-com_fwrd2026

## Overview & Design Identity
- **Target**: `www-ataccama-com_fwrd2026` (**Ataccama FWRD 2026: Press play on what's next in data trust · Ataccama**)
- **Production URL**: [https://www.ataccama.com/fwrd2026](https://www.ataccama.com/fwrd2026)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#f10090`)
- **Summary**: Rewind through the shifts in data quality, agentic data management, and governed context that shaped trusted AI in 2026, then fast-forwar...
- **Total Clean CSS Variables Extracted**: `323` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Poppins`
- **Body Font Stack**: `Poppins`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 56px`, `line-height: 67.2px`, `font-weight: 600`); rule `,.h1` (`font-size: clamp(2.75rem,2.4vw + 1.58rem...`, `line-height: 1.2`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 44px`, `line-height: 52.8px`, `font-weight: 600`); rule `,.h2` (`font-size: clamp(1.75rem,1.6vw + .97rem,...`, `line-height: 1.2`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--bs-body-font-size: 1rem`, `--bs-body-font-weight: 400`, `--bs-body-line-height: 1.5`; rule `p` (`font-size: 18px`, `line-height: 1.5`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `small` (`font-weight: normal`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1a0c42` | live computed `h2` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#dddddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Interactive Accent / Highlight** | `#f10090` | `var(--bs-link-color)` in `:root` |
| **Secondary / Muted Copy** | `#f771c1` | `var(--bs-pink-60)` in `:root` |
| **Structural Hairline Border** | `#e9ecef` | `var(--bs-light-border-subtle)` in `:root` |
| **Variable Token (`--wp-block-synced-color`)** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color`)** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-10`)** | `#006ba1` | `var(--wp-admin-theme-color-darker-10)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-20`)** | `#005a87` | `var(--wp-admin-theme-color-darker-20)` in `:root` |
| **Variable Token (`--bs-blue`)** | `#0d6efd` | `var(--bs-blue)` in `:root` |
| **Variable Token (`--bs-indigo`)** | `#6610f2` | `var(--bs-indigo)` in `:root` |
| **Variable Token (`--bs-red`)** | `#dc3545` | `var(--bs-red)` in `:root` |
| **Variable Token (`--bs-orange`)** | `#fd7e14` | `var(--bs-orange)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--wp-block-synced-color` | `#7a00df` | Brand / Palette Token |
| `--wp-block-synced-color--rgb` | `122,0,223` | Brand / Palette Token |
| `--wp-bound-block-color` | `var(--wp-block-synced-color)` | Brand / Palette Token |
| `--wp-editor-canvas-background` | `#ddd` | Canvas / Surface Token |
| `--wp-admin-theme-color` | `#007cba` | Brand / Palette Token |
| `--wp-admin-theme-color--rgb` | `0,124,186` | Brand / Palette Token |
| `--wp-admin-theme-color-darker-10` | `#006ba1` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-10--rgb` | `0,107,160.5` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-20` | `#005a87` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-20--rgb` | `0,90,135` | Canvas / Surface Token |
| `--wp-admin-border-width-focus` | `2px` | Layout / Spatial Grid Token |
| `--wp-admin--admin-bar--position-offset` | `var(--wp-admin--admin-bar--height,0px)` | Dimension / Scale Token |
| `--bs-blue` | `#0d6efd` | Color / Atmospheric Token |
| `--bs-indigo` | `#6610f2` | Color / Atmospheric Token |
| `--bs-red` | `#dc3545` | Color / Atmospheric Token |
| `--bs-orange` | `#fd7e14` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.position-relative> — `www-ataccama-com_fwrd2026`)**:
   - Landmark `<header class="position-relative pt-md-96">` (`1440x96px`) hosting `Ataccama FWRD 2026: Press play on wh` navigation (`Register now`), DOM attributes (`data-hubspot-styled-components`, `data-wp-strategy="defer"`, `data-nosnippet`, `data-template="overlay"`), and stylesheet rule `.a0-footer { display: none; }`.
2. **Hero Stage & Focal Lead (<section.py-56> — `Press play on what’s next in data `)**:
   - Landmark `<section class="py-56 py-sm-120">` presenting display lead `Press play on what’s next in data trust` and copy excerpt *"Join hundreds of data leaders at our biggest event of the year. L"* over `#ffffff` canvas and `#1a0c42` ink.
3. **Primary Showcase & Content Grid (<section.pb-56> — `Hear from the leaders moving data `)**:
   - Landmark `<section class="pb-56 pb-sm-120">` rendering section `Hear from the leaders moving data and AI FWRD` with copy *"NOV 5 · 10 AM ET · VIRTUAL"*, asset references (`main-qGdQcxOC.css`, `cdnjs.cloudflare.com`, `feed`, `embed`), and grid rule `a0-widget .a0-zocial.a0-wp-login { background-color: 490050; }`.
4. **Interactive Detail & Feature Matrix (<section.bg-navy> — `Camilla Björkqvist`)**:
   - Landmark `<section class="bg-navy py-56">` framing `Camilla Björkqvist` and `Chantale Boulanger` (*"You're joining speakers and attendees from:"*) with `#dddddd` surface cards, `#f10090` accents, and `wp-login-form-wrapper { display: none; }`.
5. **Colophon & Global Directory Footer (<footer.page-id-13449> — `https://www.ataccama.com/fwrd2026`)**:
   - Landmark `<footer class="page-id-13449">` anchoring `Ataccama FWRD 2026: Press play o` footer links (`Register now`), copy *"Get an inside look at how data and AI strategies are evolvin"*, and `#e9ecef` structural dividers.
