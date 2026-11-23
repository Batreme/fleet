---
title: "UI & UX Architecture: noho-ink"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: noho-ink

## Overview & Design Identity
- **Target**: `noho-ink` (**Noho**)
- **Production URL**: [https://noho.ink](https://noho.ink)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#0082f3`)
- **Summary**: E n e r g y u s a g e E n e r g y u s a g e
- **Total Clean CSS Variables Extracted**: `41` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Switzer`
- **Body Font Stack**: `Switzer Variable`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `canvas-modal-luma` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | `mark { color: #000000 }` |
| **Elevated Surface / Card Substrate** | `#f1eee9` | `var(--bg-page)` in `:root` |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#3c3c3c` | `var(--text-form-header-active)` in `:root` |
| **Structural Hairline Border** | `#e2e2e2` | `blockquote { border-left: #e2e2e2 }` |
| **Variable Token (`--bg-switch`)** | `#d7d1c7` | `var(--bg-switch)` in `:root` |
| **Variable Token (`--transperent`)** | `#0000` | `var(--transperent)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg-page` | `#f1eee9` | Canvas / Surface Token |
| `--txt-main` | `#3c3c3c` | Color / Atmospheric Token |
| `--bg-form-element` | `white` | Canvas / Surface Token |
| `--raven-black-100` | `#3c3c3c` | Canvas / Surface Token |
| `--bg-switch` | `#d7d1c7` | Canvas / Surface Token |
| `--bg-inner-switch` | `white` | Canvas / Surface Token |
| `--bg-btn-pm` | `#3c3c3c` | Canvas / Surface Token |
| `--txt-btn-pm` | `white` | Design System Custom Token |
| `--bg-btn-sc` | `white` | Canvas / Surface Token |
| `--txt-btn-sc` | `#3c3c3c` | Color / Atmospheric Token |
| `--bg-btn-big` | `#3c3c3c` | Canvas / Surface Token |
| `--txt-btn-big` | `white` | Design System Custom Token |
| `--transperent` | `#0000` | Color / Atmospheric Token |
| `--raven-black-40` | `#3c3c3c66` | Canvas / Surface Token |
| `--offbeat` | `#d7d1c7` | Color / Atmospheric Token |
| `--white` | `white` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `noho-ink`)**:
   - Landmark `<header class="header section">` (`1440px`) hosting `Noho` navigation (`A b o u t A b o u t · P r i c e P r i c e · B l o g B l o g · F A Q F A Q · About`), DOM attributes (`data-wf-domain="noho-a7a5a8.webflow.io"`, `data-wf-page="667aaef1d0489a9d5183ef5d"`, `data-wf-site="667aaef1d0489a9d5183ef56"`, `data-wf-status="1"`), and stylesheet rule `.w-container { max-width:728px }`.
2. **Hero Stage & Focal Lead (<section.switch> — `Noho`)**:
   - Landmark `<section class="switch">` presenting display lead `Noho` and copy excerpt *"E n e r g y u s a g e E n e r g y u s a g e"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.switch:nth(2)> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="switch">` rendering section `Featured Work & Interactive Showcase` with copy *"Dark mode and reduce animation options allow you to save about 35"*, asset references (`webflow.shared.min.css`, `6a4e44ce6ee465198645089f_favicon-...`, `6a4e444d307c1e077753f979_favicon-...`, `6a4e44ceccf875bb9d22c7cd_favicon-...`), and grid rule `.w-hidden-main { display:inherit!important }`.
4. **Interactive Detail & Feature Matrix (<section.hero-section-parent> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="hero-section-parent">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Dark mode and reduce animation options allow you to save 35% of y"*) with `#f1eee9` surface cards, `#0082f3` accents, and `.w-hidden-medium { display:none!important }`.
5. **Colophon & Global Directory Footer (<footer.footer-parent> — `https://noho.ink`)**:
   - Landmark `<footer class="footer-parent">` anchoring `Noho` footer links (`A b o u t A b o u t · P r i c e P r i c e · B l o g B l o g · F A Q F A Q · About`), copy *"Using dark mode can save energy consumption on devices with "*, and `#e2e2e2` structural dividers.
