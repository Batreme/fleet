---
title: "UI & UX Architecture: 21oaks-org"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: 21oaks-org

## Overview & Design Identity
- **Target**: `21oaks-org` (**21Oaks Student Apartments • USC & Williams-Brice**)
- **Production URL**: [https://21oaks.org/](https://21oaks.org/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#292929` ink, `#0082f3` accent)
- **Summary**: Freshly renovated student apartments minutes from Williams-Brice and USC. Modern living with pool, study spaces, and everything within re...
- **Total Clean CSS Variables Extracted**: `9` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Exposure`
- **Body Font Stack**: `Exposure`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 72px`, `line-height: 64.8px`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 93.6px`, `line-height: 102.96px`, `font-weight: 400`, `letter-spacing: -1.872px`)
- **Body Copy**: live computed `body` (`font-size: 14.4px`, `line-height: 14.4px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 18.72px`, `line-height: 18.72px`, `font-weight: 400`, `letter-spacing: -0.1872px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#292929` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffff00` | `mark { background: #ffff00 }` |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#999999` | `.w-select::placeholder { color: #999999 }` |
| **Structural Hairline Border** | `#e8ceff` | `var(--scribble-line-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--white` | `white` | Canvas / Surface Token |
| `--black` | `#292929` | Canvas / Surface Token |
| `--primary` | `#e8ceff` | Brand / Palette Token |
| `--icon` | `40px` | Dimension / Scale Token |
| `--shift-gap` | `0.25em` | Layout / Spatial Grid Token |
| `--dur` | `650ms` | Motion / Timing Token |
| `--ease` | `cubic-bezier(0.83, 0, 0.17, 1)` | Motion / Easing Token |
| `--scribble-line-color` | `#e8ceff` | Brand / Palette Token |
| `--ring-size` | `0.1em` | Layout / Spatial Grid Token |
| `--21oaks-org-bg` | `#ffffff` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--21oaks-org-ink` | `#292929` | Primary Typography Ink (computed-derived) |
| `--21oaks-org-surface` | `#ffff00` | Surface Substrate (computed-derived) |
| `--21oaks-org-accent` | `#0082f3` | Interactive Accent (computed-derived) |
| `--21oaks-org-muted` | `#999999` | Secondary Ink (computed-derived) |
| `--21oaks-org-border` | `#e8ceff` | Structural Border (computed-derived) |
| `--21oaks-org-container` | `1440px` | Container Bound (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `21oaks-org`)**:
   - Landmark `<header class="header">` (`1440x64px`) hosting `21Oaks Student Apartments • USC & Wi` navigation (`21Oaks · Home · Apartments · Amenities · Location`), DOM attributes (`data-wf-domain="21oaks.org"`, `data-wf-page="6a31483f3822b51654193a43"`, `data-wf-site="6a31483f3822b51654193a68"`, `data-appearance="horizontal"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Live better, closer to USC`)**:
   - Landmark `<section class="hero">` presenting display lead `Live better, closer to USC` and copy excerpt *"Click “Apply Now,” choose your lease term and floor plan, and com"* over `#ffffff` canvas and `#292929` ink.
3. **Primary Showcase & Content Grid (<section.dynamic_section> — `Everything student living should b`)**:
   - Landmark `<section class="dynamic_section">` rendering section `Everything student living should be` with copy *"Designed to recharge"*, asset references (`cdn.prod.website-files.com`, `21oakswebsite.webflow.shared.1884...`, `6a31483f3822b51654193afd_favicon.png`, `69fb54ec6fea40c496e176b6_favicon.png`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.dynamic_section:nth(2)> — `Designed to recharge`)**:
   - Landmark `<section class="dynamic_section">` framing `Designed to recharge` and `Comfort in every corner` (*"Comfort in every corner"*) with `#ffff00` surface cards, `#0082f3` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://21oaks.org/`)**:
   - Landmark `<footer class="footer">` anchoring `21Oaks Student Apartments • USC ` footer links (`21Oaks · Home · Apartments · Amenities · Location`), copy *"Little details matter"*, and `#e8ceff` structural dividers.
