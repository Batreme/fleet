# UI & UX Architecture: crl-2026-webflow-io

## Overview & Design Identity
- **Target**: `crl-2026-webflow-io` (**Creative Reference Library · CRL**)
- **Production URL**: [https://crl-2026.webflow.io/](https://crl-2026.webflow.io/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#c6fb50` / `#d9d9d9`)
- **Summary**: CRL® is a curated library of creative references — music, film, books, and writing that shape how ideas are developed, tested, and made....
- **Total Clean CSS Variables Extracted**: `158` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Neue Haas Grotesk Text Pro`
- **Body Font Stack**: `Oswald`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_text-style---l...`, `font-weight: var(--_text-s...`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_text-style---l...`, `font-weight: var(--_text-s...`)
- **Body Copy**: rule `p` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_text-style---l...`, `font-weight: var(--_text-s...`)
- **Metadata & Labels**: CSS variables `--_text-style---letter-spacing: var(--_typography---letter-spacing--0-01em)`, `--max-width--small: 80rem`, `--radius--small: .5rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#c6fb50` | `var(--swatch--brand)` in `:root` |
| **Primary Typography Ink** | `#a1a098` | `var(--swatch--dark)` in `:root` |
| **Elevated Surface / Card Substrate** | `#000` | `var(--swatch--black)` in `:root` |
| **Interactive Accent / Highlight** | `#d9d9d9` | `var(--swatch--grey)` in `:root` |
| **Secondary / Muted Copy** | `#0000` | `a { background-color: #0000 }` |
| **Structural Hairline Border** | `#ff0` | `mark { background: #ff0 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--_theme---background` | `var(--swatch--light)` | Canvas / Surface Token |
| `--_text-style---font-family` | `var(--_typography---font--primary-family)` | Typography Ink Token |
| `--_theme---text` | `var(--swatch--black)` | Typography Ink Token |
| `--_text-style---font-size` | `var(--_typography---font-size--text-main)` | Typography Ink Token |
| `--_text-style---line-height` | `var(--_typography---line-height--1)` | Typography Ink Token |
| `--_text-style---font-weight` | `var(--_typography---font--primary-medium)` | Typography Ink Token |
| `--_text-style---letter-spacing` | `var(--_typography---letter-spacing--0-01em)` | Typography Ink Token |
| `--_spacing---space--gap--6` | `var(--size--2rem)` | Layout / Spatial Grid Token |
| `--size--0-5rem` | `.5rem` | Layout / Spatial Grid Token |
| `--_spacing---space--gap--2` | `var(--size--0-5rem)` | Layout / Spatial Grid Token |
| `--_spacing---space--gap--1` | `var(--size--0-25rem)` | Layout / Spatial Grid Token |
| `--_spacing---space--gap--4` | `var(--size--1rem)` | Layout / Spatial Grid Token |
| `--_spacing---space--gap--7` | `var(--size--3rem)` | Layout / Spatial Grid Token |
| `--max-width--full` | `100%` | Layout / Spatial Grid Token |
| `--max-width--small` | `80rem` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.w-mod-js> — `crl-2026-webflow-io`)**:
   - Landmark `<header class="w-mod-js">` hosting `Creative Reference Library · CRL` navigation (`Index · Library · About · Library (20) · Instagram`), DOM attributes (`data-wf-domain="crl-2026.webflow.io"`, `data-wf-page="6a0fce3b3983a9d8a80eb4d1"`, `data-wf-site="6a0fce3b3983a9d8a80eb4d0"`, `data-page="home"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.home_hero> — `Creative Reference Library`)**:
   - Landmark `<section class="home_hero">` presenting display lead `Creative Reference Library` and copy excerpt *"Creative Reference Library®"* over `#c6fb50` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.home_hero> — `crl®`)**:
   - Landmark `<section class="home_hero">` rendering section `crl®` with copy *"(1) CRL® is a curated library of creative references, built from "*, asset references (`cdn.prod.website-files.com`, `crl-2026.shared.1c24320b9.min.css`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.home_hero> — `/V.01`)**:
   - Landmark `<section class="home_hero">` framing `/V.01` and `(2026)` (*"(2) The library spans a range of formats, including interviews, f"*) with `#000` surface cards, `#d9d9d9` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.wf-oswald-n7-active> — `https://crl-2026.webflow.io/`)**:
   - Landmark `<footer class="wf-oswald-n7-active">` anchoring `Creative Reference Library · CRL` footer links (`Index · Library · About · Library (20) · Instagram`), copy *"CRL® is a curated library of creative references, built from"*, and `#ff0` structural dividers.
