# UI & UX Architecture: newminds-studio_concept-elune

## Overview & Design Identity
- **Target**: `newminds-studio_concept-elune` (**ELUNE Women's Health App UX/UI Concept · New Minds**)
- **Production URL**: [https://newminds.studio/concept-elune](https://newminds.studio/concept-elune)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#151a18` canvas, `#fff` ink, `#c9d1cc` accent)
- **Summary**: Women's health app UX/UI concept by New Minds: cycle tracking, bloodwork records and a separate pregnancy journey. Explore the complete c...
- **Total Clean CSS Variables Extracted**: `0` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted)
- **Body Font Stack**: `system-ui, -apple-system, sans-serif` (no custom `@font-face` extracted)
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(38px,6vw,76px)`, `line-height: 1.06`, `letter-spacing: -.045em`, `font-weight: 500`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(26px,3.5vw,42px)`, `line-height: 1.15`, `letter-spacing: -.03em`, `font-weight: 500`)
- **Body Copy**: rule `p` (`font-size: clamp(16px,1.7vw,20px)`, `line-height: 1.75`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11px`, `clamp(38px,6vw,76px)`, `clamp(16px,1.7vw,20px)`, `14px`, `clamp(26px,3.5vw,42px)`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#151a18` | `body { background: #151a18 }` |
| **Primary Typography Ink** | `#fff` | `body { color: #fff }` |
| **Elevated Surface / Card Substrate** | `#d5fc65` | `a { color: #d5fc65 }` |
| **Interactive Accent / Highlight** | `#c9d1cc` | `.case-context p { color: #c9d1cc }` |
| **Secondary / Muted Copy** | `#7e8c77` | `.case-actions a { border: #7e8c77 }` |
| **Structural Hairline Border** | `#a9b6ac` | `footer { color: #a9b6ac }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--newminds-studio--bg` | `#151a18` | Canvas Substrate (from `body { background: #151a18 }`) |
| `--newminds-studio--ink` | `#fff` | Primary Typography Ink (stylesheet-derived) |
| `--newminds-studio--surface` | `#d5fc65` | Surface Substrate (stylesheet-derived) |
| `--newminds-studio--accent` | `#c9d1cc` | Interactive Accent (stylesheet-derived) |
| `--newminds-studio--muted` | `#7e8c77` | Secondary Ink (stylesheet-derived) |
| `--newminds-studio--border` | `#a9b6ac` | Structural Border (stylesheet-derived) |
| `--newminds-studio--container` | `1400px` | Container Bound (stylesheet-derived) |
| `--newminds-studio--gap` | `15px` | Grid Gutter (stylesheet-derived) |
| `--newminds-studio--pad` | `24px` | Lateral Padding (stylesheet-derived) |
| `--newminds-studio--ease` | `cubic-bezier(0.25,0.1,0.25,1)` | Primary Easing Function |
| `--newminds-studio--radius` | `7px` | Corner Radius (stylesheet-derived) |
| `--newminds-studio--fs-base` | `11px` | Observed Font Size Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.skip-case> — `newminds-studio_concept-elune`)**:
   - Landmark `<header class="skip-case">` hosting `ELUNE Women's Health App UX/UI Conce` navigation (`More concepts`), DOM attributes (`data-target="newminds-studio_concept-elune"`), and stylesheet rule `body { margin:0;background:151a18;font:16px Arial;color:fff }`.
2. **Hero Stage & Focal Lead (<section.case-intro> — `Women's health, with room for cont`)**:
   - Landmark `<section class="case-intro">` presenting display lead `Women's health, with room for context.` and copy excerpt *"Skip to case study"* over `#151a18` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.case-context> — `Design scope and interactive proto`)**:
   - Landmark `<section class="case-context">` rendering section `Design scope and interactive prototype` with copy *"Try interactive prototype ↗"*, asset references (`concept-elune`, `elune-case-01.jpg (ELUNE, a fictional women’s health mob...)`, `elune-case-02.jpg (Product framing, design objectives an...)`, `elune-case-03.jpg (Cycle overview, calendar with dashed...)`), and grid rule `main { max-width:1400px;margin:auto }`.
4. **Interactive Detail & Feature Matrix (<section.case-context> — `Try interactive prototype ↗`)**:
   - Landmark `<section class="case-context">` framing `Try interactive prototype ↗` and `ELUNE / MOBILE APP UX/UI DESIGN CONCEPT` (*"ELUNE / MOBILE APP UX/UI DESIGN CONCEPT"*) with `#d5fc65` surface cards, `#c9d1cc` accents, and `img { display:block;width:100%;height:auto }`.
5. **Colophon & Global Directory Footer (<footer.case-context> — `https://newminds.studio/concept-elune`)**:
   - Landmark `<footer class="case-context">` anchoring `ELUNE Women's Health App UX/UI C` footer links (`More concepts`), copy *"ELUNE is an independent women's health app design concept by"*, and `#a9b6ac` structural dividers.
