# UI & UX Architecture: www-unbelievablycrap-com

## Overview & Design Identity
- **Target**: `www-unbelievablycrap-com` (**Liubomyr Ulytskyi - Digital Designer**)
- **Production URL**: [https://www.unbelievablycrap.com/](https://www.unbelievablycrap.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#afafaf`)
- **Summary**: Liubomyr Ulytskyi — Digital Designer, award-winning UI/UX Designer, art director, conceptualist.
- **Total Clean CSS Variables Extracted**: `86` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `PP Supply Sans`
- **Body Font Stack**: `PP Supply Mono`
- **Monospace / Technical Font Stack**: `PP Supply Mono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--ui-10)`, `var(--hud-size)`, `12vw`, `clamp(2.75rem, 6.7vw, 8rem)`, `64px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--ui-10)`, `var(--hud-size)`, `12vw`, `clamp(2.75rem, 6.7vw, 8rem)`, `64px`)
- **Body Copy**: rule `p` (`font-size: var(--ui-10)`, `line-height: 10px`, `letter-spacing: -0.4px`)
- **Metadata & Labels**: CSS variables `--font-mono: 'PP Supply Mono',ui-monospace,'SF Mono','Roboto Mono',monospace`, `--c-label: #636363`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | `var(--about-ground)` in `:root` |
| **Primary Typography Ink** | `#C8C8C8` | `var(--about-ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ffffff` | `var(--c-white)` in `:root` |
| **Interactive Accent / Highlight** | `#afafaf` | `var(--c-fog)` in `:root` |
| **Secondary / Muted Copy** | `#6e6e6e` | `var(--c-slate)` in `:root` |
| **Structural Hairline Border** | `#636363` | `var(--c-label)` in `:root` |
| **Variable Token (`--c-fade`)** | `#c3c3c3` | `var(--c-fade)` in `:root` |
| **Variable Token (`--c-ink`)** | `#393939` | `var(--c-ink)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--about-ground` | `#000000` | Color / Atmospheric Token |
| `--about-ink` | `#C8C8C8` | Typography Ink Token |
| `--about-dim` | `rgba(200,200,200,.5)` | Color / Atmospheric Token |
| `--grain-blend` | `lighten` | Design System Custom Token |
| `--grain-opacity` | `.06` | Design System Custom Token |
| `--grain-brightness` | `100%` | Dimension / Scale Token |
| `--grain-contrast` | `50%` | Dimension / Scale Token |
| `--grain-size` | `1em` | Layout / Spatial Grid Token |
| `--font-main` | `'PP Supply Sans','Neue Haas Grotesk Text','Inter',-apple-system,` | Typography / Scale Token |
| `--font-mono` | `'PP Supply Mono',ui-monospace,'SF Mono','Roboto Mono',monospace` | Typography / Scale Token |
| `--c-white` | `#ffffff` | Canvas / Surface Token |
| `--c-fog` | `#afafaf` | Color / Atmospheric Token |
| `--c-slate` | `#6e6e6e` | Color / Atmospheric Token |
| `--c-label` | `#636363` | Color / Atmospheric Token |
| `--c-fade` | `#c3c3c3` | Color / Atmospheric Token |
| `--c-ink` | `#393939` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.ftr__nav> — `www-unbelievablycrap-com`)**:
   - Landmark `<nav class="ftr__nav">` hosting `Liubomyr Ulytskyi - Digital Designer` navigation (`index · work · gallery · 404`), DOM attributes (`data-err-src="ERR_ART"`, `data-err-src="ERR_CARD"`, `data-mesh-var="FIGURE_LITE"`, `data-mesh-var="LOGO_MESH"`), and stylesheet rule `.about__figure canvas { position: absolute; inset: 0; display: block; width: 100%; height: 100%; }`.
2. **Hero Stage & Focal Lead (<main.gate> — `find your way out of here`)**:
   - Landmark `<main class="gate">` presenting display lead `find your way out of here` and copy excerpt *"the crap experience is best viewed with a desktop"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<main.gate__bg> — `the crap experience is best viewed`)**:
   - Landmark `<main class="gate__bg">` rendering section `the crap experience is best viewed with a deskto` with copy *"CASE FILE: THE MAN BEHIND THE IMAGE"*, asset references (`favicon.ico`, `favicon-32x32.png`, `favicon-16x16.png`, `apple-touch-icon.png`), and grid rule `.about__stage { position: absolute; inset: 0; z-index: 3; overflow: hidden; cursor: defa... }`.
4. **Interactive Detail & Feature Matrix (<main.gate__logo> — `CASE FILE: THE MAN BEHIND THE IMAG`)**:
   - Landmark `<main class="gate__logo">` framing `CASE FILE: THE MAN BEHIND THE IMAGE` and `The first mistake was assuming Liubomyr was look` (*"The first mistake was assuming Liubomyr was looking for something"*) with `#ffffff` surface cards, `#afafaf` accents, and `.about__column { transition: none; }`.
5. **Colophon & Global Directory Footer (<footer.bar> — `https://www.unbelievablycrap.com/`)**:
   - Landmark `<footer class="bar">` anchoring `Liubomyr Ulytskyi - Digital Desi` footer links (`index · work · gallery · 404`), copy *"He was 0looking for what 3was hiding."*, and `#636363` structural dividers.
