# UI & UX Architecture: fabiantjoeaon-com

## Overview & Design Identity
- **Target**: `fabiantjoeaon-com` (**Fabian Tjoe-A-On — Creative technologist**)
- **Production URL**: [https://fabiantjoeaon.com](https://fabiantjoeaon.com)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f3f3ef` canvas, `#000` ink, `#e8fffd` accent)
- **Summary**: Creative and technical direction, analog heart with exceptional digitalism.
- **Total Clean CSS Variables Extracted**: `30` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Arial`
- **Body Font Stack**: `clamp(9.5px`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(110px, 15vw, 260px)`, `var(--meta-font-size)`, `clamp(26px, 2.5vw, 46px)`, `clamp(11px, 0.8vw, 15px)`, `13px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(110px, 15vw, 260px)`, `var(--meta-font-size)`, `clamp(26px, 2.5vw, 46px)`, `clamp(11px, 0.8vw, 15px)`, `13px`)
- **Body Copy**: rule `body` (`font-weight: var(--w-regular)`)
- **Metadata & Labels**: CSS variables `--font-mono: ui-monospace, monospace`, `--meta-font-size: clamp(9.5px, 0.64vw, 12px)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f3f3ef` | `var(--text)` in `:root` |
| **Primary Typography Ink** | `#a3a6a7` | `var(--muted)` in `:root` |
| **Elevated Surface / Card Substrate** | `#000` | `.entry-loader { background: #000 }` |
| **Interactive Accent / Highlight** | `#e8fffd` | `ollapsible > .list-item-cell:fi... { color: #e8fffd }` |
| **Secondary / Muted Copy** | `#d4d6d4` | `ollapsible > .list-item-cell:fi... { color: #d4d6d4 }` |
| **Structural Hairline Border** | `#9aa0a0` | `ollapsible > .list-item-cell:fi... { color: #9aa0a0 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--digit-height` | `1.1em` | Layout / Spatial Grid Token |
| `--size` | `18px` | Layout / Spatial Grid Token |
| `--font-family` | `Arial, sans-serif` | Typography / Scale Token |
| `--font-mono` | `ui-monospace, monospace` | Typography / Scale Token |
| `--w-light` | `400` | Canvas / Surface Token |
| `--w-regular` | `400` | Design System Custom Token |
| `--w-book` | `400` | Design System Custom Token |
| `--w-medium` | `500` | Design System Custom Token |
| `--segment-reveal` | `0` | Design System Custom Token |
| `--aside` | `calc(var(--project-left) - var(--page-gutter))` | Design System Custom Token |
| `--main` | `var(--project-mediaWidth)` | Design System Custom Token |
| `--rest` | `minmax(0, 1fr)` | Dimension / Scale Token |
| `--next-gap` | `48px` | Layout / Spatial Grid Token |
| `--line-reveal` | `0` | Design System Custom Token |
| `--corner` | `calc(14px * var(--line-reveal))` | Dimension / Scale Token |
| `--page-gutter` | `clamp(20px, 3vw, 64px)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.no-webgpu-header> — `fabiantjoeaon-com`)**:
   - Landmark `<header class="no-webgpu-header">` hosting `Fabian Tjoe-A-On — Creative technolo` navigation (`About`), DOM attributes (`data-mono`), and stylesheet rule `.loader-grid { position: absolute; inset: 0; width: 100%; height: 100%; display: block; }`.
2. **Hero Stage & Focal Lead (<section.no-webgpu-body> — `This portfolio is a real-time WebG`)**:
   - Landmark `<section class="no-webgpu-body">` presenting display lead `This portfolio is a real-time WebGPU experience.` and copy excerpt *"Creative technologist"* over `#f3f3ef` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.no-webgpu-body> — `Creative technologist`)**:
   - Landmark `<section class="no-webgpu-body">` rendering section `Creative technologist` with copy *"Creative and technical direction, analog heart with exceptional d"*, asset references (`SuisseIntl-Regular.otf`, `SpaceMono-Regular.ttf`, `favicon.ico`, `favicon.svg`), and grid rule `.loader-mask { display: block; overflow: hidden; }`.
4. **Interactive Detail & Feature Matrix (<section.no-webgpu-body> — `Creative and technical direction, `)**:
   - Landmark `<section class="no-webgpu-body">` framing `Creative and technical direction, analog heart w` and `WebGPU is available, but no compatible graphics ` (*"WebGPU is available, but no compatible graphics adapter was found"*) with `#000` surface cards, `#e8fffd` accents, and `.loader-mask > span { display: block; will-change: transform; }`.
5. **Colophon & Global Directory Footer (<footer.no-webgpu-footer> — `https://fabiantjoeaon.com`)**:
   - Landmark `<footer class="no-webgpu-footer">` anchoring `Fabian Tjoe-A-On — Creative tech` footer links (`About`), copy *"WSJ Iconic Mints The Wall Street Journal, 2022"*, and `#9aa0a0` structural dividers.
