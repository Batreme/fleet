---
title: "UI & UX Architecture: almirakho-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: almirakho-com

## Overview & Design Identity
- **Target**: `almirakho-com` (**Almira Kho - Photographer and Director**)
- **Production URL**: [https://almirakho.com/](https://almirakho.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fafafa` canvas, `#0a0a0a` ink, `#2ec97a` accent)
- **Summary**: Almira Kho is a photographer and director based in Paris/London. Specialized in music industry and fashion. Film and digital.
- **Total Clean CSS Variables Extracted**: `91` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Archivo`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 13px`, `line-height: 13px`, `font-weight: 500`); CSS variables `--display-font-name: "Archivo"`, `--display-font: var(--display-font-name), "Helvetica Neue", "Arial", sans-serif`
- **Section Heading (`H2`)**: observed font-size ladder: `13px`, `16px`, `40px`, `16rem`, `var(--rem)`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 16px`, `font-weight: 500`); rule `,p` (`font-size: inherit`, `letter-spacing: inherit`, `font-weight: inherit`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 13px`, `line-height: 13px`, `font-weight: 500`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fafafa` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0a0a0a` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `body::-moz-selection { background-color: white }` (`#ffffff`) |
| **Interactive Accent / Highlight** | `#2ec97a` | `var(--vp-primary-hover)` in `:root` |
| **Secondary / Muted Copy** | `#ffffff` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#ffffff` | hairline divider derived from live computed `p` `color` (`computed_styles.json`) |
| **Variable Token (`--color-red`)** | `#e45050` | `var(--color-red)` in `:root` |

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
   - Landmark `<header class="header">` (`1440x76px`) hosting `Almira Kho - Photographer and Direct` navigation (`Almira Kho · About · IG`), DOM attributes (`data-scroll="top"`, `data-v-app`, `data-v-edc13355`, `data-v-83432065`), and stylesheet rule `html { font-family:var(--main-font);letter-spacing:0;text-transform:uppercase;f... }`.
2. **Hero Stage & Focal Lead (<main.header> — `ALMIRA KHO`)**:
   - Landmark `<main class="header">` presenting display lead `ALMIRA KHO` and copy excerpt *"Photographer and director based in Paris/London. Specialized in m"* over `#fafafa` canvas and `#0a0a0a` ink.
3. **Primary Showcase & Content Grid (<main.home-link> — `Almira Kho`)**:
   - Landmark `<main class="home-link">` rendering section `Almira Kho` with copy *"ALMIRA KHO"*, asset references (`entry.BkXJSryM.css`, `Cg0QnzOv.js`, `B_9E_aBj.js`, `HclGiUj8.js`), and grid rule `body::-moz-selection { background-color:var(--color-white);color:var(--color-black) }`.
4. **Interactive Detail & Feature Matrix (<main.router-link-active> — `almirakho-com Interactive Matrix`)**:
   - Landmark `<main class="router-link-active">` framing `almirakho-com Interactive Matrix` and `almirakho-com Archive & Directory` (*"Almira Kho"*) with `#ffffff` surface cards, `#2ec97a` accents, and `html::-moz-selection { background-color:var(--color-white);color:var(--color-black) }`.
5. **Colophon & Global Directory Footer (<footer.router-link-exact-active> — `https://almirakho.com/`)**:
   - Landmark `<footer class="router-link-exact-active">` anchoring `Almira Kho - Photographer and Di` footer links (`Almira Kho · About · IG`), copy *"almirakho-com Interactive Matrix"*, and `#ffffff` structural dividers.
