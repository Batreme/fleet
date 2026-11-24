---
title: "UI & UX Architecture: namaha-healthcare"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: namaha-healthcare

## Overview & Design Identity
- **Target**: `namaha-healthcare` (**Namaha Healthcare**)
- **Production URL**: [https://namaha.healthcare](https://namaha.healthcare)
- **Final Redirected URL**: [https://www.namaha.healthcare/](https://www.namaha.healthcare/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fffbf6` canvas, `#0000ee` ink, `#0082f3` accent)
- **Summary**: With over seventy years in healthcare, the Kapadia family has nurtured a legacy built on trust, compassion, and clinical integrity.
- **Total Clean CSS Variables Extracted**: `0` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Victorserif 50`
- **Body Font Stack**: `Helvetica Neue`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 42px`, `line-height: 46.2px`, `font-weight: 500`, `letter-spacing: -0.924px`); rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: live computed `body` (`font-size: 14px`, `line-height: 20px`, `font-weight: 400`); rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 20px`, `font-weight: 400`); rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fffbf6` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `.slick-loading .slick-list { background: #ffffff }` |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#a05941` | live computed `h2` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e2e2e2` | `blockquote { border-left: #e2e2e2 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--namaha-healthcar-bg` | `#fffbf6` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--namaha-healthcar-ink` | `#0000ee` | Primary Typography Ink (computed-derived) |
| `--namaha-healthcar-surface` | `#ffffff` | Surface Substrate (computed-derived) |
| `--namaha-healthcar-accent` | `#0082f3` | Interactive Accent (computed-derived) |
| `--namaha-healthcar-muted` | `#a05941` | Secondary Ink (computed-derived) |
| `--namaha-healthcar-border` | `#e2e2e2` | Structural Border (computed-derived) |
| `--namaha-healthcar-container` | `1411px` | Container Bound (computed-derived) |
| `--namaha-healthcar-gap` | `7px` | Grid Gutter (computed-derived) |
| `--namaha-healthcar-pad` | `5px` | Lateral Padding (computed-derived) |
| `--namaha-healthcar-ease` | `cubic-bezier(.645,.045,.355,1)` | Primary Easing Function |
| `--namaha-healthcar-radius` | `3px` | Corner Radius (computed-derived) |
| `--namaha-healthcar-fs-base` | `42px` | Observed Font Size Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.w-mod-js> — `namaha-healthcare`)**:
   - Landmark `<header class="w-mod-js">` (`1440px`) hosting `Namaha Healthcare` navigation (`1 Our Philosophy · 2 Our Team · 3 Departments · 5 Our Facilities · 6 Guides`), DOM attributes (`data-wf-domain="www.namaha.healthcare"`, `data-wf-page="68949db83756970449601627"`, `data-wf-site="68949db8375697044960161c"`, `data-w-id="2086974e-b9c8-7268-e0..."`), and stylesheet rule `.slick-list { position: relative; display: block; overflow: hidden; margin: 0; padding... }`.
2. **Hero Stage & Focal Lead (<section.headersection> — `Namaha Healthcare`)**:
   - Landmark `<section class="headersection scrolled-over">` presenting display lead `Namaha Healthcare` and copy excerpt *"Our lines are available 24/7. Reach out to us to get in touch wit"* over `#fffbf6` canvas and `#0000ee` ink.
3. **Primary Showcase & Content Grid (<section.header> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="header">` rendering section `Featured Work & Interactive Showcase` with copy *"Your well-being matters to us. We are here to assist you with car"*, asset references (`cdn.prod.website-files.com`, `namaha-v2.webflow.shared.a69184c8...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `.slick-list:focus { outline: none; }`.
4. **Interactive Detail & Feature Matrix (<section.hero_section> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="hero_section gsapherosection">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Women are at the centre of family and relationships. At Namaha, w"*) with `#ffffff` surface cards, `#0082f3` accents, and `.slick-list.dragging { cursor: pointer; cursor: hand; }`.
5. **Colophon & Global Directory Footer (<footer.wf-active> — `https://namaha.healthcare`)**:
   - Landmark `<footer class="wf-active">` anchoring `Namaha Healthcare` footer links (`1 Our Philosophy · 2 Our Team · 3 Departments · 5 Our Facilities · 6 Guides`), copy *"Consult with the best specialists in every field. We assure "*, and `#e2e2e2` structural dividers.
