---
title: "UI & UX Architecture: duda-works"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: duda-works

## Overview & Design Identity
- **Target**: `duda-works` (**Duda Lima**)
- **Production URL**: [http://duda.works](http://duda.works)
- **Final Redirected URL**: [https://www.duda.works/](https://www.duda.works/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#060403` canvas, `#ffffff` ink, `#ffffff` accent)
- **Summary**: Production web application and digital experience at http://duda.works.
- **Total Clean CSS Variables Extracted**: `5` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Aeonik Pro`
- **Body Font Stack**: `Aeonik Pro`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: observed font-size ladder: `16px`, `11px`, `13.3333px`, `15px`, `12px`
- **Section Heading (`H2`)**: observed font-size ladder: `16px`, `11px`, `13.3333px`, `15px`, `12px`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#060403` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `.custom-cursor.is-dot { background: #ffffff }` |
| **Interactive Accent / Highlight** | `#ffffff` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#ffffff` | secondary opacity step of live computed `main` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#1f1d1c` | `var(--border)` in `:root` (`rgba(255, 255, 255, 0.1)`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#060403` | Canvas / Surface Token |
| `--text` | `#fff` | Typography Ink Token |
| `--text-dim` | `rgba(255, 255, 255, 0.62)` | Typography Ink Token |
| `--border` | `rgba(255, 255, 255, 0.1)` | Elevation / Border Token |
| `--border-strong` | `rgba(255, 255, 255, 0.28)` | Elevation / Border Token |
| `--duda-works-bg` | `#060403` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--duda-works-ink` | `#ffffff` | Primary Typography Ink (computed-derived) |
| `--duda-works-surface` | `#ffffff` | Surface Substrate (computed-derived) |
| `--duda-works-accent` | `#ffffff` | Interactive Accent (computed-derived) |
| `--duda-works-muted` | `#ffffff` | Secondary Ink (computed-derived) |
| `--duda-works-border` | `#1f1d1c` | Structural Border (computed-derived) |
| `--duda-works-container` | `1440px` | Container Bound (computed-derived) |
| `--duda-works-gap` | `normal` | Grid Gutter (computed-derived) |
| `--duda-works-pad` | `71px` | Lateral Padding (computed-derived) |
| `--duda-works-ease` | `cubic-bezier(0.22,1,0.36,1)` | Primary Easing Function |
| `--duda-works-radius` | `8px` | Corner Radius (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `duda-works`)**:
   - Landmark `<header class="site-header">` (`1440x78px`) hosting `Duda Lima` navigation (`P r o j e c t s · A b o u t`), DOM attributes (`data-char="P"`, `data-char="r"`, `data-char="o"`, `data-char="j"`), and stylesheet rule `view-transition { navigation: auto; }`.
2. **Hero Stage & Focal Lead (<section.mwg_effect107> — `Duda Lima`)**:
   - Landmark `<section class="mwg_effect107">` presenting display lead `Duda Lima` and copy excerpt *"Production web application and digital experience at http://duda."* over `#060403` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.mwg_effect107:nth(2)> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="mwg_effect107">` rendering section `Featured Work & Interactive Showcase` with copy *"Duda Lima"*, asset references (`hotjar-6782564.js`, `modules.07f6e16cfaafa9e41bab.js`, `02.png`, `24.png`), and grid rule `html { background: var(--bg); }`.
4. **Interactive Detail & Feature Matrix (<section.mwg_effect107:nth(3)> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="mwg_effect107">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#ffffff` surface cards, `#ffffff` accents, and `.wordmark svg { display: block; filter: drop-shadow(0 1px 4px rgba(0, 0, 0, 0.75)) drop-... }`.
5. **Colophon & Global Directory Footer (<footer.icon-menu> — `http://duda.works`)**:
   - Landmark `<footer class="icon-menu">` anchoring `Duda Lima` footer links (`P r o j e c t s · A b o u t`), copy *"Technical Architecture & Narrative"*, and `#1f1d1c` structural dividers.
