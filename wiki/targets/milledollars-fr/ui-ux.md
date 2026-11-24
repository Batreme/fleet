---
title: "UI & UX Architecture: milledollars-fr"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: milledollars-fr

## Overview & Design Identity
- **Target**: `milledollars-fr` (**MilleDollars**)
- **Production URL**: [https://milledollars.fr/](https://milledollars.fr/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×4968px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#e0dee1` / `#00adef`)
- **Summary**: Creative bureau focused on high-end video production. Working worldwide.
- **Total Clean CSS Variables Extracted**: `132` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `ABCDiatype`
- **Body Font Stack**: `ABCDiatype`
- **Monospace / Technical Font Stack**: `Inconsolata`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 18px`, `line-height: 18px`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#e0dee1` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `header` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `var(--cc-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#00adef` | `areLink_module_shareButton__cb9... { color: #00adef }` |
| **Secondary / Muted Copy** | `#5e6266` | `var(--cc-secondary-color)` in `:root` |
| **Structural Hairline Border** | `#ffffff` | `var(--accent-border-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ease-in-quad` | `cubic-bezier(.55,.085,.68,.53)` | Motion / Easing Token |
| `--ease-in-cubic` | `cubic-bezier(.55,.055,.675,.19)` | Motion / Easing Token |
| `--ease-in-quart` | `cubic-bezier(.895,.03,.685,.22)` | Motion / Easing Token |
| `--ease-in-quint` | `cubic-bezier(.755,.05,.855,.06)` | Motion / Easing Token |
| `--ease-in-expo` | `cubic-bezier(.95,.05,.795,.035)` | Motion / Easing Token |
| `--ease-in-circ` | `cubic-bezier(.6,.04,.98,.335)` | Motion / Easing Token |
| `--ease-out-quad` | `cubic-bezier(.25,.46,.45,.94)` | Motion / Easing Token |
| `--ease-out-cubic` | `cubic-bezier(.215,.61,.355,1)` | Motion / Easing Token |
| `--ease-out-quart` | `cubic-bezier(.165,.84,.44,1)` | Motion / Easing Token |
| `--ease-out-quint` | `cubic-bezier(.23,1,.32,1)` | Motion / Easing Token |
| `--ease-out-expo` | `cubic-bezier(.19,1,.22,1)` | Motion / Easing Token |
| `--ease-out-circ` | `cubic-bezier(.075,.82,.165,1)` | Motion / Easing Token |
| `--ease-in-out-quad` | `cubic-bezier(.455,.03,.515,.955)` | Motion / Easing Token |
| `--ease-in-out-cubic` | `cubic-bezier(.645,.045,.355,1)` | Motion / Easing Token |
| `--ease-in-out-quart` | `cubic-bezier(.77,0,.175,1)` | Motion / Easing Token |
| `--ease-in-out-quint` | `cubic-bezier(.86,0,.07,1)` | Motion / Easing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.c-header> — `milledollars-fr`)**:
   - Landmark `<header class="c-header">` (`1440x64px`) hosting `MilleDollars` navigation (`Home · Works · Info · Contact`), DOM attributes (`data-hid="prismic-preview"`, `data-hid="jsonld-seo"`, `data-symbol="logo"`, `data-symbol="logo-mille"`), and stylesheet rule `.a-mask-lines_inner-mask { margin-bottom:-.2lh }`.
2. **Hero Stage & Focal Lead (<section.sr-only> — `MilleDollars`)**:
   - Landmark `<section class="sr-only">` presenting display lead `MilleDollars` and copy excerpt *"Creative bureau focused on high-end video production. Working wor"* over `#e0dee1` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.sr-only:nth(2)> — `The Dazzling Division`)**:
   - Landmark `<section class="sr-only">` rendering section `The Dazzling Division` with copy *"The Dazzling Division — Richard Mille (2026)"*, asset references (`fonts.googleapis.com`, `fonts.gstatic.com`, `prismic.min.js`, `css2`), and grid rule `.a-lines { --appear-y:var(--y,120%) }`.
4. **Interactive Detail & Feature Matrix (<section.sr-only:nth(3)> — `Ultimate Shield`)**:
   - Landmark `<section class="sr-only">` framing `Ultimate Shield` and `Eternal Snow` (*"Ultimate Shield — EviDenS de Beauté (2026)"*) with `#ffffff` surface cards, `#00adef` accents, and `.u-anim.is-inview .a-lines.-contr... { --appear-y:0 }`.
5. **Colophon & Global Directory Footer (<footer.c-preloader-logo-loop> — `https://milledollars.fr/`)**:
   - Landmark `<footer class="c-preloader-logo-loop">` anchoring `MilleDollars` footer links (`Home · Works · Info · Contact`), copy *"Eternal Snow — Richard Mille (2026)"*, and `#ffffff` structural dividers.
