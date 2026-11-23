---
title: "UI & UX Architecture: noravale-framer-website"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: noravale-framer-website

## Overview & Design Identity
- **Target**: `noravale-framer-website` (**Blankit – Ultimate Portfolio System for Framer**)
- **Production URL**: [https://noravale.framer.website/](https://noravale.framer.website/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×1510px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#ffffff` ink, `#0000ee` accent)
- **Summary**: The ultimate portfolio system for Framer. Build premium portfolio websites with components, templates and design foundations.
- **Total Clean CSS Variables Extracted**: `151` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geist Variable`
- **Body Font Stack**: `Hedvig Letters Serif`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: observed font-size ladder: `12px`, `14px`, `var(--font-size)`, `var(--framer-font-size)`, `16px`
- **Section Heading (`H2`)**: observed font-size ladder: `12px`, `14px`, `var(--font-size)`, `var(--framer-font-size)`, `16px`
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 14px`, `line-height: 17px`, `letter-spacing: -.02em`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); CSS variables `--letter-spacing: var(--framer-letter-spacing)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `p` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#999999` | `var(--selection-background-color)` in `:root` |
| **Interactive Accent / Highlight** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#181818` | `var(--border-color)` in `:root` (`var(--token-41c38424-a6db-4bde-b2...`) |
| **Variable Token (`--token-658e57be-7dc2-47f6-a641-0a3d91f5f0a7`)** | `#292929` | `var(--token-658e57be-7dc2-47f6-a641-0a3d91f5f0a7)` in `:root` |
| **Variable Token (`--token-7454ffba-6ef4-4d38-9965-d502f06ebc49`)** | `#0000` | `var(--token-7454ffba-6ef4-4d38-9965-d502f06ebc49)` in `:root` |
| **Variable Token (`--token-fab8f350-6af4-4276-a121-46955910532e`)** | `#fafafa` | `var(--token-fab8f350-6af4-4276-a121-46955910532e)` in `:root` |
| **Variable Token (`--token-7edb6191-4ddd-4bbc-96d5-e5e591d6ed9b`)** | `#f2f2f2` | `var(--token-7edb6191-4ddd-4bbc-96d5-e5e591d6ed9b)` in `:root` |
| **Variable Token (`--token-5f666cb9-74f6-4b15-aaed-8cf125fa4837`)** | `#0d0d0d` | `var(--token-5f666cb9-74f6-4b15-aaed-8cf125fa4837)` in `:root` |
| **Variable Token (`--token-58ed9133-56c7-4c1c-83a9-d6e40daeeb72`)** | `#080808` | `var(--token-58ed9133-56c7-4c1c-83a9-d6e40daeeb72)` in `:root` |
| **Variable Token (`--token-68cbe2e9-85cc-47c7-aa5a-bac039f90af2`)** | `#757575` | `var(--token-68cbe2e9-85cc-47c7-aa5a-bac039f90af2)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--token-835e5838-ad16-45ed-8524-d371a38640d4` | `#fff` | Color / Atmospheric Token |
| `--token-658e57be-7dc2-47f6-a641-0a3d91f5f0a7` | `#292929` | Color / Atmospheric Token |
| `--token-c9613b9a-ea67-4e25-b1ae-1822b810d41e` | `#fff` | Color / Atmospheric Token |
| `--token-7454ffba-6ef4-4d38-9965-d502f06ebc49` | `#0000` | Color / Atmospheric Token |
| `--token-fab8f350-6af4-4276-a121-46955910532e` | `#fafafa` | Color / Atmospheric Token |
| `--token-7edb6191-4ddd-4bbc-96d5-e5e591d6ed9b` | `#f2f2f2` | Color / Atmospheric Token |
| `--token-5f666cb9-74f6-4b15-aaed-8cf125fa4837` | `#0d0d0d` | Color / Atmospheric Token |
| `--token-c2a7bcb4-4b1e-42b6-859b-d5fb68f2e51c` | `#0d0d0d` | Color / Atmospheric Token |
| `--token-37582e93-848e-41c2-9a6a-be05b3cb724b` | `#000` | Color / Atmospheric Token |
| `--token-de44e4c4-2780-4f6a-920a-6573964b909b` | `#fff` | Color / Atmospheric Token |
| `--token-58ed9133-56c7-4c1c-83a9-d6e40daeeb72` | `#08080880` | Color / Atmospheric Token |
| `--token-43292462-1240-4872-bac6-680eed5be9b9` | `#000` | Color / Atmospheric Token |
| `--token-4f3e38f4-83ad-43b0-9e27-1d245f644e53` | `#000` | Color / Atmospheric Token |
| `--token-68cbe2e9-85cc-47c7-aa5a-bac039f90af2` | `#757575` | Color / Atmospheric Token |
| `--token-35adfe75-6afb-4a33-9225-016fa16ccba3` | `#000` | Color / Atmospheric Token |
| `--token-a0b6ff5f-d52f-4ed7-9c5e-cd9e56ee7714` | `#000` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `noravale-framer-website`)**:
   - Landmark `<header class="lenis">` (`1440px`) hosting `Blankit – Ultimate Portfolio System ` navigation (`Purchase`), DOM attributes (`data-framer-font-css`, `data-framer-css-ssr-minified`, `data-framer-components="framer-lib-cursors-ho..."`, `data-framer-css="true"`), and stylesheet rule `main { box-sizing:border-box;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<main.framer-17y96vw> — `Blankit – Ultimate Portfolio Syste`)**:
   - Landmark `<main class="framer-17y96vw">` presenting display lead `Blankit – Ultimate Portfolio System for Framer` and copy excerpt *"B u i l d i n g a l i f e s t y l e b r a n d r o o t e d i n c o"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<main.framer-17y96vw:nth(2)> — `Featured Work & Interactive Showca`)**:
   - Landmark `<main class="framer-17y96vw">` rendering section `Featured Work & Interactive Showcase` with copy *"A d i g i t a l - f i r s t i d e n t i t y f o r a f a s t - g r"*, asset references (`default-favicon-light.v1.png`, `default-favicon-dark.v1.png`, `default-touch-icon.v3.png`, `fonts.gstatic.com`), and grid rule `root { -webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale }`.
4. **Interactive Detail & Feature Matrix (<main.framer-17y96vw:nth(3)> — `Technical Architecture & Narrative`)**:
   - Landmark `<main class="framer-17y96vw">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"d i g i t a l - f i r s t"*) with `#999999` surface cards, `#0000ee` accents, and `button { font-family:sans-serif;font-size:12px }`.
5. **Colophon & Global Directory Footer (<footer.framer-RrLH2> — `https://noravale.framer.website/`)**:
   - Landmark `<footer class="framer-RrLH2">` anchoring `Blankit – Ultimate Portfolio Sys` footer links (`Purchase`), copy *"f a s t - g r o w i n g"*, and `#181818` structural dividers.
