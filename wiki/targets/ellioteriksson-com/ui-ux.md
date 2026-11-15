# UI & UX Architecture: ellioteriksson-com

## Overview & Design Identity
- **Target**: `ellioteriksson-com` (**Elliot Eriksson — UI/UX, web & brand design, Stockholm & Åland**)
- **Production URL**: [https://ellioteriksson.com/](https://ellioteriksson.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#c6f432` canvas, `#0c0c0c` ink, `#ff5a36` accent)
- **Summary**: Elliot Eriksson is a digital designer in Stockholm, designing clear, accessible websites and interfaces from first sketch to final polish.
- **Total Clean CSS Variables Extracted**: `45` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Gossip Fallback`
- **Body Font Stack**: `wordmark`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: CSS variables `--fs-display: clamp(36px, 4vw, 72px)`
- **Section Heading (`H2`)**: CSS variables `--fs-lg: clamp(24px, 2.4vw, 40px)`
- **Body Copy**: CSS variables `--fs-body: 16px`
- **Metadata & Labels**: CSS variables `--font-mono: var(--font-mono-face,"Geist Mono"), ui-monospace, Menlo, monospace`, `--font-mono-face: "Geist Mono", "Geist Mono Fallback"`; rule `,.mono` (`font-size: 12px`, `line-height: 1.4`, `letter-spacing: .02em`, `font-weight: 400`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#c6f432` | `var(--accent)` in `:root` |
| **Primary Typography Ink** | `#0c0c0c` | `var(--on-accent)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ff6fae` | `var(--kind-client)` in `:root` |
| **Interactive Accent / Highlight** | `#ff5a36` | `var(--kind-personal)` in `:root` |
| **Secondary / Muted Copy** | `#fff` | `var(--bg)` in `:root` |
| **Structural Hairline Border** | `#6b6b6b` | `var(--muted)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--accent` | `#c6f432` | Brand / Palette Token |
| `--on-accent` | `#0c0c0c` | Brand / Palette Token |
| `--highlight` | `#c6f432` | Canvas / Surface Token |
| `--on-highlight` | `#0c0c0c` | Canvas / Surface Token |
| `--kind-agency` | `var(--highlight)` | Design System Custom Token |
| `--kind-client` | `#ff6fae` | Color / Atmospheric Token |
| `--kind-personal` | `#ff5a36` | Color / Atmospheric Token |
| `--font-wordmark` | `var(--font-wordmark-face,"Gossip"), Georgia, serif` | Typography / Scale Token |
| `--font-mono` | `var(--font-mono-face,"Geist Mono"), ui-monospace, Menlo, monospace` | Typography / Scale Token |
| `--gutter` | `3vw` | Layout / Spatial Grid Token |
| `--gap` | `11px` | Layout / Spatial Grid Token |
| `--header-h` | `52px` | Layout / Spatial Grid Token |
| `--section` | `clamp(96px, 11vw, 180px)` | Dimension / Scale Token |
| `--fs-body` | `16px` | Dimension / Scale Token |
| `--fs-md` | `clamp(20px, 1.8vw, 30px)` | Dimension / Scale Token |
| `--fs-lg` | `clamp(24px, 2.4vw, 40px)` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `ellioteriksson-com`)**:
   - Landmark `<header class="site-header">` hosting `Elliot Eriksson — UI/UX, web & brand` navigation (`Home H o m e · Cases C a s e s · EN E N – English · SV S V – Svenska`), DOM attributes (`data-precedence="next"`, `data-href="/_next/static/immutab..."`, `data-sdkn="@vercel/analytics/next"`, `data-sdkv="2.0.1"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.hero> — `I’m Elliot , an award winning desi`)**:
   - Landmark `<section class="hero">` presenting display lead `I’m Elliot , an award winning designer creating i...` and copy excerpt *"Elliot Eriksson E l l i o t E r i k s s o n"* over `#c6f432` canvas and `#0c0c0c` ink.
3. **Primary Showcase & Content Grid (<section.showcase> — `Selected work Selected work`)**:
   - Landmark `<section class="showcase showcase--roomy">` rendering section `Selected work Selected work` with copy *"E l l i o t E r i k s s o n"*, asset references (`1dm-4pi_h5ujm.js`, `41lrt_djk18al.js`, `1x62cbew_54xo.js`, `2jqd0dpb7brv_.js`), and grid rule `img { max-width:100%;height:auto;display:block }`.
4. **Interactive Detail & Feature Matrix (<section.projects> — `More projects`)**:
   - Landmark `<section class="projects">` framing `More projects` and `Strand Properties` (*"Currently in Stockholm 20 : 22"*) with `#ff6fae` surface cards, `#ff5a36` accents, and `button { font:inherit;letter-spacing:inherit;color:inherit;cursor:pointer;backgro... }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://ellioteriksson.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Elliot Eriksson — UI/UX, web & b` footer links (`Home H o m e · Cases C a s e s · EN E N – English · SV S V – Svenska`), copy *"Contact C o n t a c t"*, and `#6b6b6b` structural dividers.
