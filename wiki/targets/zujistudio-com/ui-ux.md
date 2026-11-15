# UI & UX Architecture: zujistudio-com

## Overview & Design Identity
- **Target**: `zujistudio-com` (**zuji studio - index**)
- **Production URL**: [https://zujistudio.com/](https://zujistudio.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#080809` / `#b1b1bf`)
- **Summary**: Independent design studio creating brand systems and digital experiences rooted in precision. Based in Washington, working worldwide.
- **Total Clean CSS Variables Extracted**: `64` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Roobertmonotrial`
- **Body Font Stack**: `Roobert Mono`
- **Monospace / Technical Font Stack**: `Roobertmonotrial`
- **Hero Display (`H1`)**: CSS variables `--real-h1: 5rem`, `--h1-spacing: -.03em`, `--h1: 4rem`; rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: CSS variables `--h2: 2.5rem`; rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: CSS variables `--main-paragraph: .9rem`; rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: CSS variables `--letter-spacing: -.012em`, `--mono: .8rem`, `--mono-spacing: -.02em`; rule `small` (`font-size: 80%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#080809` | `var(--color-800)` in `:root` |
| **Primary Typography Ink** | `#e8e8f2` | `var(--color-100)` in `:root` |
| **Elevated Surface / Card Substrate** | `#2c2c2f` | `var(--color-700)` in `:root` |
| **Interactive Accent / Highlight** | `#b1b1bf` | `var(--color-500)` in `:root` |
| **Secondary / Muted Copy** | `#c5c5d8` | `var(--color-200)` in `:root` |
| **Structural Hairline Border** | `#454549` | `var(--color-600)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-800` | `#080809` | Brand / Palette Token |
| `--color-100` | `#e8e8f2` | Brand / Palette Token |
| `--real-h1` | `5rem` | Typography / Scale Token |
| `--h1-spacing` | `-.03em` | Typography / Scale Token |
| `--h1` | `4rem` | Typography / Scale Token |
| `--h2` | `2.5rem` | Typography / Scale Token |
| `--letter-spacing` | `-.012em` | Typography / Scale Token |
| `--h3` | `1.666rem` | Typography / Scale Token |
| `--mono` | `.8rem` | Typography / Scale Token |
| `--mono-spacing` | `-.02em` | Typography / Scale Token |
| `--grid-gap` | `1.25rem` | Layout / Spatial Grid Token |
| `--main-paragraph` | `.9rem` | Typography / Scale Token |
| `--hunnid` | `100%` | Dimension / Scale Token |
| `--global-padding` | `1.25rem` | Layout / Spatial Grid Token |
| `--space-small` | `2rem` | Layout / Spatial Grid Token |
| `--border-radius` | `.4rem` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.w-mod-js> — `zujistudio-com`)**:
   - Landmark `<header class="w-mod-js">` hosting `zuji studio - index` navigation (`studio, · visual feed · contact · see visual feed [+]`), DOM attributes (`data-wf-domain="www.zujistudio.com"`, `data-wf-page="6a37365f2cb2a2b0994025f6"`, `data-wf-site="6a37365f2cb2a2b099402610"`, `data-barba="wrapper"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<div.transition> — `zuji studio`)**:
   - Landmark `<div class="transition">` presenting display lead `zuji studio` and copy excerpt *"purposeful experiences"* over `#080809` canvas and `#e8e8f2` ink.
3. **Primary Showcase & Content Grid (<div.transition> — `select works`)**:
   - Landmark `<div class="transition">` rendering section `select works` with copy *"independent studio."*, asset references (`cdn.prod.website-files.com`, `zujistudio.webflow.shared.21d1844...`, `6a40cf63d130ed9881baa0d1_Frame%20...`, `6a40cf636da9030b77fa9c00_Frame%20...`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<div.transition> — `Apollo Atomics`)**:
   - Landmark `<div class="transition">` framing `Apollo Atomics` and `S-2K` (*"based in washington, usa."*) with `#2c2c2f` surface cards, `#b1b1bf` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.lenis-smooth> — `https://zujistudio.com/`)**:
   - Landmark `<footer class="lenis-smooth">` anchoring `zuji studio - index` footer links (`studio, · visual feed · contact · see visual feed [+]`), copy *"designs brand systems and digital experiences"*, and `#454549` structural dividers.
