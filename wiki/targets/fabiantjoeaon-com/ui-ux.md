---
title: "UI & UX Architecture: fabiantjoeaon-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: fabiantjoeaon-com

## Overview & Design Identity
- **Target**: `fabiantjoeaon-com` (**Fabian Tjoe-A-On — Creative technologist**)
- **Production URL**: [https://fabiantjoeaon.com](https://fabiantjoeaon.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×872px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#f3f3ef` ink, `#99ff99` accent)
- **Summary**: Creative and technical direction, analog heart with exceptional digitalism.
- **Total Clean CSS Variables Extracted**: `30` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Suisse Intl`
- **Body Font Stack**: `Suisse Intl`
- **Monospace / Technical Font Stack**: `Space Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 29.9693px`, `line-height: 36.8622px`, `font-weight: 500`, `letter-spacing: -1.04892px`)
- **Section Heading (`H2`)**: observed font-size ladder: `29.9693px`, `16px`, `9.5px`, `14.2416px`, `clamp(110px, 15vw, 260px)`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `body` (`font-weight: var(--w-regular)`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--font-mono: ui-monospace, monospace`, `--meta-font-size: clamp(9.5px, 0.64vw, 12px)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f3f3ef` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#a2e2e1` | `::selection { background: #a2e2e1 }` |
| **Interactive Accent / Highlight** | `#99ff99` | `.touch-debug { color: #99ff99 }` |
| **Secondary / Muted Copy** | `#a3a6a7` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#353939` | `var(--rule)` in `:root` (`rgba(220, 237, 239, 0.24)`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-family` | `Arial, sans-serif` | Typography / Scale Token |
| `--font-mono` | `ui-monospace, monospace` | Typography / Scale Token |
| `--w-light` | `400` | Canvas / Surface Token |
| `--w-regular` | `400` | Design System Custom Token |
| `--w-book` | `400` | Design System Custom Token |
| `--w-medium` | `500` | Design System Custom Token |
| `--page-gutter` | `clamp(20px, 3vw, 64px)` | Layout / Spatial Grid Token |
| `--nav-inset` | `clamp(20px, 2.1vw, 44px)` | Layout / Spatial Grid Token |
| `--text` | `#f3f3ef` | Typography Ink Token |
| `--muted` | `#a3a6a7` | Color / Atmospheric Token |
| `--rule` | `rgba(220, 237, 239, 0.24)` | Color / Atmospheric Token |
| `--type-scale` | `0.86` | Typography / Scale Token |
| `--nav-font-size` | `calc(clamp(16px, 1.15vw, 24px) * var(--type-scale))` | Typography / Scale Token |
| `--meta-font-size` | `clamp(9.5px, 0.64vw, 12px)` | Typography / Scale Token |
| `--digit-height` | `1.1em` | Layout / Spatial Grid Token |
| `--size` | `18px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.no-webgpu-header> — `fabiantjoeaon-com`)**:
   - Landmark `<header class="no-webgpu-header">` (`1354x41px`) hosting `Fabian Tjoe-A-On — Creative technolo` navigation (`About`), DOM attributes (`data-mono`), and stylesheet rule `.loader-grid { position: absolute; inset: 0; width: 100%; height: 100%; display: block; }`.
2. **Hero Stage & Focal Lead (<section.no-webgpu-body> — `This portfolio is a real-time WebG`)**:
   - Landmark `<section class="no-webgpu-body">` presenting display lead `This portfolio is a real-time WebGPU experience.` and copy excerpt *"Creative technologist"* over `#000000` canvas and `#f3f3ef` ink.
3. **Primary Showcase & Content Grid (<section.no-webgpu-body:nth(2)> — `Creative technologist`)**:
   - Landmark `<section class="no-webgpu-body">` rendering section `Creative technologist` with copy *"Creative and technical direction, analog heart with exceptional d"*, asset references (`SuisseIntl-Regular.otf`, `SpaceMono-Regular.ttf`, `favicon.ico`, `favicon.svg`), and grid rule `.loader-mask { display: block; overflow: hidden; }`.
4. **Interactive Detail & Feature Matrix (<section.no-webgpu-body:nth(3)> — `Creative and technical direction, `)**:
   - Landmark `<section class="no-webgpu-body">` framing `Creative and technical direction, analog heart w` and `WebGPU is available, but no compatible graphics ` (*"WebGPU is available, but no compatible graphics adapter was found"*) with `#a2e2e1` surface cards, `#99ff99` accents, and `.loader-mask > span { display: block; will-change: transform; }`.
5. **Colophon & Global Directory Footer (<footer.no-webgpu-footer> — `https://fabiantjoeaon.com`)**:
   - Landmark `<footer class="no-webgpu-footer">` anchoring `Fabian Tjoe-A-On — Creative tech` footer links (`About`), copy *"WSJ Iconic Mints The Wall Street Journal, 2022"*, and `#353939` structural dividers.
