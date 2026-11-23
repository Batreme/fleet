---
title: "UI & UX Architecture: santalarch-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: santalarch-com

## Overview & Design Identity
- **Target**: `santalarch-com` (**Santalarch**)
- **Production URL**: [https://santalarch.com](https://santalarch.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f0f0f0` / `#007aff`)
- **Summary**: Architectural studio built on uncompromising precision and intent.
- **Total Clean CSS Variables Extracted**: `103` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `lil-gui`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `.title` (`line-height: calc(var(--title-heig...`, `font-weight: 600`)
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 33px`, `line-height: 35.64px`, `font-weight: 400`, `letter-spacing: -0.99px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`); CSS variables `--font-family-mono: Menlo, Monaco, Consolas, "Droid Sans Mono", monospace`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f0f0f0` | live computed `main` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0f0f0f` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `:hover { background-color: white }` (`#ffffff`) |
| **Interactive Accent / Highlight** | `#007aff` | `:root { color: #007aff }` |
| **Secondary / Muted Copy** | `#ebebeb` | `var(--text-color)` in `:root` |
| **Structural Hairline Border** | `#f9f9f9` | `ui .controller.color .display:h... { border: #f9f9f9 }` |
| **Variable Token (`--c-base-line-highlight`)** | `#f2f0f0` | `var(--c-base-line-highlight)` in `:root` |
| **Variable Token (`--c-pure-black`)** | `#000000` | `var(--c-pure-black)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--viewport-width` | `1440` | Layout / Spatial Grid Token |
| `--viewport-height` | `800` | Layout / Spatial Grid Token |
| `--font-helvetica` | `"Helvetica",sans-serif` | Typography / Scale Token |
| `--ease-out` | `cubic-bezier(.25,1,.5,1)` | Motion / Easing Token |
| `--transition` | `.5s var(--ease-out)` | Motion / Easing Token |
| `--transition-fast` | `.3s var(--ease-out)` | Motion / Easing Token |
| `--transition-slow` | `.8s var(--ease-out)` | Motion / Easing Token |
| `--c-base-light-primary` | `#f0f0f0` | Canvas / Surface Token |
| `--c-base-line-highlight` | `#f2f0f033` | Canvas / Surface Token |
| `--c-base-line-dark-bg` | `#f2f0f00d` | Canvas / Surface Token |
| `--c-pure-black` | `#000` | Canvas / Surface Token |
| `--c-pure-white` | `#fff` | Canvas / Surface Token |
| `--c-pure-black-rgb` | `0,0,0` | Canvas / Surface Token |
| `--c-pure-black-0` | `rgba(var(--c-pure-black-rgb),0)` | Canvas / Surface Token |
| `--c-light-primary` | `var(--c-base-light-primary)` | Canvas / Surface Token |
| `--c-light-secondary` | `#f2f0f066` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `santalarch-com`)**:
   - Landmark `<header class="header difference">` (`1440x450px`) hosting `Santalarch` navigation (`Works Works · Services Services · Process Process · Company Company · Contact Contact`), DOM attributes (`data-theme="light"`, `data-v-fd5224ce`, `data-v-211bdc1c`, `data-v-52d76f34`), and stylesheet rule `before { box-sizing:border-box;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Intent Before Image`)**:
   - Landmark `<section class="hero">` presenting display lead `Intent Before Image` and copy excerpt *"This site uses cookies."* over `#f0f0f0` canvas and `#0f0f0f` ink.
3. **Primary Showcase & Content Grid (<section.cubes-wrap> — `Engineering as Foundation`)**:
   - Landmark `<section class="cubes-wrap">` rendering section `Engineering as Foundation` with copy *"Architectural studio built on uncompromising precision and intent"*, asset references (`entry.D7X7o5bn.css`, `CI8pdcr7.js`, `03be9e1c-9e63-48c6-b4db-59a6b0167...`, `ad.B18i8NGa.svg`), and grid rule `video { border:0;font-size:100%;font:inherit;margin:0;padding:0;vertical-align:b... }`.
4. **Interactive Detail & Feature Matrix (<section.approach> — `Material Intelligence`)**:
   - Landmark `<section class="approach grid-container">` framing `Material Intelligence` and `Detail as Discipline` (*"Architecture Shapes Perception"*) with `#ffffff` surface cards, `#007aff` accents, and `svg { display:block }`.
5. **Colophon & Global Directory Footer (<footer.c2-sb> — `https://santalarch.com`)**:
   - Landmark `<footer class="c2-sb">` anchoring `Santalarch` footer links (`Works Works · Services Services · Process Process · Company Company · Contact Contact`), copy *"Bold presence. Quiet execution."*, and `#f9f9f9` structural dividers.
