# UI & UX Architecture: www-teamcafeteria-com_2027

## Overview & Design Identity
- **Target**: `www-teamcafeteria-com_2027` (**2027 — a [cafeteria] report**)
- **Production URL**: [https://www.teamcafeteria.com/2027](https://www.teamcafeteria.com/2027)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#171515` / `#8a8f90`)
- **Summary**: 1,423 people told us what 2027 looks like. A scroll-driven [cafeteria] report.
- **Total Clean CSS Variables Extracted**: `216` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Satoshi 2027`
- **Body Font Stack**: `Anton`
- **Monospace / Technical Font Stack**: `Rubik Mono One`
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(2rem,5vw,3rem)`, `line-height: 1.1`, `font-weight: 700`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(1.5rem,3.5vw,2rem)`, `line-height: 1.2`, `font-weight: 700`)
- **Body Copy**: CSS variables `--body: #b4bcbd`, `--font-size-vw-body: 1.5vw`, `--font-size-body: clamp(1.125rem, var(--font-size-vw-body), 1.5rem)`; rule `p` (`font-weight: 500`)
- **Metadata & Labels**: CSS variables `--meta: #8a8f90`, `--mono: "Roboto Mono 2027",ui-monospace,Menlo,monospace`, `--font-family-mono: "Roboto Mono", monospace`; rule `,.label` (`font-size: var(--font-size-lg)`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#171515` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#f4f4f5` | `var(--white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#eff0f6` | `var(--paper)` in `:root` |
| **Interactive Accent / Highlight** | `#8a8f90` | `var(--meta)` in `:root` |
| **Secondary / Muted Copy** | `#b4bcbd` | `var(--body)` in `:root` |
| **Structural Hairline Border** | `#2f6bff` | `var(--blue)` in `:root` |
| **Variable Token (`--bg`)** | `#000` | `var(--bg)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#171515` | Typography Ink Token |
| `--white` | `#f4f4f5` | Canvas / Surface Token |
| `--paper` | `#eff0f6` | Canvas / Surface Token |
| `--meta` | `#8a8f90` | Color / Atmospheric Token |
| `--body` | `#b4bcbd` | Color / Atmospheric Token |
| `--blue` | `#2f6bff` | Color / Atmospheric Token |
| `--fg` | `#f4f4f5` | Typography Ink Token |
| `--bg` | `#000` | Canvas / Surface Token |
| `--pad` | `clamp(16px,2.6vw,40px)` | Layout / Spatial Grid Token |
| `--mono` | `"Roboto Mono 2027",ui-monospace,Menlo,monospace` | Typography / Scale Token |
| `--sans` | `"Satoshi 2027",system-ui,-apple-system,"Helvetica Neue",Arial,sans-serif` | Typography / Scale Token |
| `--mw` | `15em` | Dimension / Scale Token |
| `--rg` | `rgba(255,255,255,.1)` | Color / Atmospheric Token |
| `--page-bg` | `#000` | Canvas / Surface Token |
| `--nav-w` | `80%` | Layout / Spatial Grid Token |
| `--c-nav-bg` | `rgba(255, 255, 255, .66)` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `www-teamcafeteria-com_2027`)**:
   - Landmark `<header class="site-header">` hosting `2027 — a [cafeteria] report` navigation (`ask AI → · studies →`), DOM attributes (`data-nav-flow-ready="true"`, `data-nav-pill-ready="true"`, `data-cta-location="use_cases_menu"`, `data-track-cta`), and stylesheet rule `font-face { font-family:Anton;font-weight:100 900;font-display:swap;src:url(/_astro/... }`.
2. **Hero Stage & Focal Lead (<article.report-doc> — `2027 — a [cafeteria] report`)**:
   - Landmark `<article class="report-doc">` presenting display lead `2027 — a [cafeteria] report` and copy excerpt *"Read this report as text"* over `#171515` canvas and `#f4f4f5` ink.
3. **Primary Showcase & Content Grid (<section.fact> — `Shoes`)**:
   - Landmark `<section class="fact">` rendering section `Shoes` with copy *"solutions always-on data S/NTH → Always-on Gen Next data. Ask a q"*, asset references (`favicon.svg`, `Satoshi-Medium.dlbj618m.woff2`, `Satoshi-Bold.BRirVCsc.woff2`, `Satoshi-Black.BWj4aoZT.woff2`), and grid rule `body.report2027-page .report2027 { line-height:normal }`.
4. **Interactive Detail & Feature Matrix (<section.fact> — `Spend`)**:
   - Landmark `<section class="fact">` framing `Spend` and `Collabs` (*"always-on data S/NTH → Always-on Gen Next data. Ask a question, g"*) with `#eff0f6` surface cards, `#8a8f90` accents, and `track { position:relative;width:1px;pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.teamcafeteria.com/2027`)**:
   - Landmark `<footer class="footer theme-dark">` anchoring `2027 — a [cafeteria] report` footer links (`ask AI → · studies →`), copy *"Always-on Gen Next data. Ask a question, get an answer cited"*, and `#2f6bff` structural dividers.
