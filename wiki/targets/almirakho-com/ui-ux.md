# UI & UX Architecture: almirakho-com

## Overview & Design Identity
- **Target**: `almirakho-com` (**Almira Kho - Photographer and Director**)
- **Production URL**: [https://almirakho.com/](https://almirakho.com/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0a0a0a` canvas, `#fafafa` ink, `#3dd68c` accent)
- **Summary**: Almira Kho is a photographer and director based in Paris/London. Specialized in music industry and fashion. Film and digital.
- **Total Clean CSS Variables Extracted**: `91` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Archivo`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--display-font-name: "Archivo"`, `--display-font: var(--display-font-name), "Helvetica Neue", "Arial", sans-serif`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16rem`, `var(--rem)`, `13px`, `var(--vp-font-size)`, `var(--vp-font-size-sm)`)
- **Body Copy**: rule `,p` (`font-size: inherit`, `letter-spacing: inherit`, `font-weight: inherit`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16rem`, `var(--rem)`, `13px`, `var(--vp-font-size)`, `var(--vp-font-size-sm)`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0a0a0a` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fafafa` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#e45050` | `var(--color-red)` in `:root` |
| **Interactive Accent / Highlight** | `#3dd68c` | `var(--vp-primary)` in `:root` |
| **Secondary / Muted Copy** | `#2ec97a` | `var(--vp-primary-hover)` in `:root` |
| **Structural Hairline Border** | `#24b86e` | `var(--vp-primary-active)` in `:root` |
| **Variable Token (`--color-white-50`)** | `#ffffff80` | `var(--color-white-50)` in `:root` |
| **Variable Token (`--color-white-5`)** | `#ffffff0d` | `var(--color-white-5)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--vw` | `100vw` | Layout / Spatial Grid Token |
| `--vh` | `100vh` | Layout / Spatial Grid Token |
| `--ivh` | `100dvh` | Layout / Spatial Grid Token |
| `--rem` | `1px` | Dimension / Scale Token |
| `--main-font-name` | `"Archivo"` | Typography / Scale Token |
| `--display-font-name` | `"Archivo"` | Typography / Scale Token |
| `--main-font` | `var(--main-font-name), "Helvetica Neue", "Arial", sans-serif` | Typography / Scale Token |
| `--display-font` | `var(--display-font-name), "Helvetica Neue", "Arial", sans-serif` | Typography / Scale Token |
| `--color-black` | `#0a0a0a` | Canvas / Surface Token |
| `--color-white` | `#fafafa` | Canvas / Surface Token |
| `--color-white-50` | `#ffffff80` | Canvas / Surface Token |
| `--color-white-5` | `#ffffff0d` | Canvas / Surface Token |
| `--color-red` | `#e45050` | Brand / Palette Token |
| `--grid-margin` | `20rem` | Layout / Spatial Grid Token |
| `--grid-gutter` | `20rem` | Layout / Spatial Grid Token |
| `--grid-column` | `calc(var(--vw)/10 - var(--grid-gutter)*9/10 - var(--grid-margin)*2/10)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `almirakho-com`)**:
   - Landmark `<header class="header">` hosting `Almira Kho - Photographer and Direct` navigation (`Almira Kho · About · IG`), DOM attributes (`data-scroll="top"`, `data-v-app`, `data-v-edc13355`, `data-v-83432065`), and stylesheet rule `html { font-family:var(--main-font);letter-spacing:0;text-transform:uppercase;f... }`.
2. **Hero Stage & Focal Lead (<main.header> — `Almira Kho`)**:
   - Landmark `<main class="header">` presenting display lead `Almira Kho` and copy excerpt *"Photographer and director based in Paris/London. Specialized in m"* over `#0a0a0a` canvas and `#fafafa` ink.
3. **Primary Showcase & Content Grid (<main.home-link> — `Photographer and director based in`)**:
   - Landmark `<main class="home-link">` rendering section `Photographer and director based in Paris/London.` with copy *"Almira Kho"*, asset references (`entry.BkXJSryM.css`, `Cg0QnzOv.js`, `B_9E_aBj.js`, `HclGiUj8.js`), and grid rule `body::-moz-selection { background-color:var(--color-white);color:var(--color-black) }`.
4. **Interactive Detail & Feature Matrix (<main.router-link-active> — `almirakho-com Interactive Matrix`)**:
   - Landmark `<main class="router-link-active">` framing `almirakho-com Interactive Matrix` and `almirakho-com Archive & Directory` (*"Photographer and director based in Paris/London."*) with `#e45050` surface cards, `#3dd68c` accents, and `html::-moz-selection { background-color:var(--color-white);color:var(--color-black) }`.
5. **Colophon & Global Directory Footer (<footer.router-link-exact-active> — `https://almirakho.com/`)**:
   - Landmark `<footer class="router-link-exact-active">` anchoring `Almira Kho - Photographer and Di` footer links (`Almira Kho · About · IG`), copy *"almirakho-com Interactive Matrix"*, and `#24b86e` structural dividers.
