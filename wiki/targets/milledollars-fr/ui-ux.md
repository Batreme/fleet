# UI & UX Architecture: milledollars-fr

## Overview & Design Identity
- **Target**: `milledollars-fr` (**MilleDollars**)
- **Production URL**: [https://milledollars.fr/](https://milledollars.fr/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#c2a1c7` / `#fff`)
- **Summary**: Creative bureau focused on high-end video production. Working worldwide.
- **Total Clean CSS Variables Extracted**: `116` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Redacted Script`
- **Body Font Stack**: `ABCDiatype`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--font-size)`, `1.125rem`, `.625rem`, `1rem`, `.75rem`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--font-size)`, `1.125rem`, `.625rem`, `1rem`, `.75rem`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--font-size)`, `1.125rem`, `.625rem`, `1rem`, `.75rem`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--font-size)`, `1.125rem`, `.625rem`, `1rem`, `.75rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#c2a1c7` | `var(--color-action)` in `:root` |
| **Primary Typography Ink** | `#e0dee1` | `var(--bg-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#181818` | `var(--text-color)` in `:root` |
| **Interactive Accent / Highlight** | `#fff` | `var(--accent-bg-color)` in `:root` |
| **Secondary / Muted Copy** | `#2c2f31` | `var(--cc-primary-color)` in `:root` |
| **Structural Hairline Border** | `#5e6266` | `var(--cc-secondary-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--appear-y` | `var(--y,120%)` | Dimension / Scale Token |
| `--font-size` | `var(--font-size-top,.625rem)` | Typography / Scale Token |
| `--section-padding-y` | `6rem` | Layout / Spatial Grid Token |
| `--font-size-top` | `.75rem` | Typography / Scale Token |
| `--header-spacing-y` | `2rem` | Layout / Spatial Grid Token |
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

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.c-header> — `milledollars-fr`)**:
   - Landmark `<header class="c-header">` hosting `MilleDollars` navigation (`Home · Works · Info · Contact`), DOM attributes (`data-hid="prismic-preview"`, `data-hid="jsonld-seo"`, `data-symbol="logo"`, `data-symbol="logo-mille"`), and stylesheet rule `.a-mask-lines_inner-mask { margin-bottom:-.2lh }`.
2. **Hero Stage & Focal Lead (<section.sr-only> — `MilleDollars`)**:
   - Landmark `<section class="sr-only">` presenting display lead `MilleDollars` and copy excerpt *"✺ Creative bureau focused on high-end video production."* over `#c2a1c7` canvas and `#181818` ink.
3. **Primary Showcase & Content Grid (<section.sr-only> — `The Dazzling Division`)**:
   - Landmark `<section class="sr-only">` rendering section `The Dazzling Division` with copy *"Creative bureau focused on high-end video production. Working wor"*, asset references (`fonts.googleapis.com`, `fonts.gstatic.com`, `prismic.min.js`, `css2`), and grid rule `.a-lines { --appear-y:var(--y,120%) }`.
4. **Interactive Detail & Feature Matrix (<section.sr-only> — `Ultimate Shield`)**:
   - Landmark `<section class="sr-only">` framing `Ultimate Shield` and `Eternal Snow` (*"The Dazzling Division — Richard Mille (2026)"*) with `#181818` surface cards, `#fff` accents, and `.u-anim.is-inview .a-lines.-contr... { --appear-y:0 }`.
5. **Colophon & Global Directory Footer (<footer.c-preloader-logo-loop> — `https://milledollars.fr/`)**:
   - Landmark `<footer class="c-preloader-logo-loop">` anchoring `MilleDollars` footer links (`Home · Works · Info · Contact`), copy *"Ultimate Shield — EviDenS de Beauté (2026)"*, and `#5e6266` structural dividers.
