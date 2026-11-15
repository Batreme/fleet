# UI & UX Architecture: awards-racing

## Overview & Design Identity
- **Target**: `awards-racing` (**Awards Racing**)
- **Production URL**: [https://awards.racing](https://awards.racing)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#f00000` canvas, `#fff` ink, `#c60000` accent)
- **Summary**: Customize your car and race through parody award shows and galleries in Awards Racing (also known as Versus Racing and Versus: Design Gra...
- **Total Clean CSS Variables Extracted**: `57` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Druk Wide Cy TT`
- **Body Font Stack**: `Druk Wide Cy TT`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `9px`, `clamp(9px,1.04167vw,10px)`, `clamp(10px,.72917vw,16px)`, `clamp(14px,3.125vw,24px)`, `clamp(24px,1.5625vw,48px)`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `9px`, `clamp(9px,1.04167vw,10px)`, `clamp(10px,.72917vw,16px)`, `clamp(14px,3.125vw,24px)`, `clamp(24px,1.5625vw,48px)`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `9px`, `clamp(9px,1.04167vw,10px)`, `clamp(10px,.72917vw,16px)`, `clamp(14px,3.125vw,24px)`, `clamp(24px,1.5625vw,48px)`)
- **Metadata & Labels**: CSS variables `--small-size: 50px`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f00000` | `var(--color-theme)` in `:root` |
| **Primary Typography Ink** | `#c00000` | `var(--color-theme-dark)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--color-line-1)` in `:root` |
| **Interactive Accent / Highlight** | `#c60000` | `var(--color-line-3)` in `:root` |
| **Secondary / Muted Copy** | `#ff6464` | `var(--color-line-4)` in `:root` |
| **Structural Hairline Border** | `#ffc500` | `var(--color-accent)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--size` | `50px` | Layout / Spatial Grid Token |
| `--offset` | `4px` | Dimension / Scale Token |
| `--icon-width` | `20px` | Layout / Spatial Grid Token |
| `--icon-height` | `14px` | Layout / Spatial Grid Token |
| `--border-width` | `3px` | Layout / Spatial Grid Token |
| `--font-primary` | `"Druk Wide Cy TT",sans-serif` | Brand / Palette Token |
| `--base-font-size` | `16px` | Typography / Scale Token |
| `--color-theme` | `#f00000` | Brand / Palette Token |
| `--color-theme-dark` | `#c00000` | Canvas / Surface Token |
| `--color-theme-overlay` | `rgba(166,33,55,.44)` | Brand / Palette Token |
| `--color-theme-selection` | `rgba(255,6,6,.6)` | Brand / Palette Token |
| `--color-line-1` | `#fff` | Brand / Palette Token |
| `--color-line-2` | `#f00000` | Brand / Palette Token |
| `--color-line-3` | `#c60000` | Brand / Palette Token |
| `--color-line-4` | `#ff6464` | Brand / Palette Token |
| `--color-accent` | `#ffc500` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.macos> — `awards-racing`)**:
   - Landmark `<header class="macos">` hosting `Awards Racing` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-theme="green"`, `data-onloadfired="true"`, `data-nuxt-data="nuxt-app"`, `data-ssr="true"`), and stylesheet rule `.options { gap:clamp(4px,3.33333vw,16px) }`.
2. **Hero Stage & Focal Lead (<div.desktop> — `awards racing`)**:
   - Landmark `<div class="desktop">` presenting display lead `awards racing` and copy excerpt *"Customize your car and race through parody award shows and galler"* over `#f00000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<div.landscape> — `Awards Racing Primary Showcase`)**:
   - Landmark `<div class="landscape">` rendering section `Awards Racing Primary Showcase` with copy *"awards racing"*, asset references (`entry.BqrIyN9y.css`, `index.B6ocAFgr.css`, `shareState.CxNBlIw1.css`, `useWaitlistAvailable.C-zekLsB.css`), and grid rule `.options__button { --border-width:clamp(3px,.50403vw,5px) }`.
4. **Interactive Detail & Feature Matrix (<div.view> — `awards-racing Interactive Matrix`)**:
   - Landmark `<div class="view">` framing `awards-racing Interactive Matrix` and `awards-racing Archive & Directory` (*"Awards Racing Primary Showcase"*) with `#fff` surface cards, `#c60000` accents, and `.options__button img { border-radius:50%;display:block;height:100%;-o-object-fit:cover;object-f... }`.
5. **Colophon & Global Directory Footer (<footer.preloader> — `https://awards.racing`)**:
   - Landmark `<footer class="preloader">` anchoring `Awards Racing` footer links (`Overview · Index · Archive · About · Contact`), copy *"awards-racing Interactive Matrix"*, and `#ffc500` structural dividers.
