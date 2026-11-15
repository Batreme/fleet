---
title: "UI Prompt Blueprint: biipmk-com"
date: 2026-11-15
target: "[[overview|biipmk-com]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#2e2e2f` ink, `#f0f0f1` accent)"
---

# UI Design System & Master Generation Blueprint: biipmk-com

> **biipmk** (https://biipmk.com/) — French art director and keycap designer with 10+ years experience. Specializing in mechanical keyboard design, custom keycap sets, and vi...

![Desktop Viewport Capture (1440x4344)](file:///root/projects/fleet/wiki/targets/biipmk-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **biipmk** (`https://biipmk.com/`). French art director and keycap designer with 10+ years experience. Specializing in mechanical keyboard design, custom keycap sets, and vi...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#2e2e2f` ink, `#f0f0f1` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--token-a58b3a81-59cc-45f7-ae05-091785ff903e)` in `:root`) paired with `#2e2e2f` primary typography and `#f0f0f1` accents.
  - **Extracted Typographic Hierarchy**: Pairs `IBM Plex Mono` for display copy (`M e c h a n i c a l k e y b o a r d `) with `Inter` and `IBM Plex Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1279px` container bounds (`gap: 12px`, padding `4px`) with `cubic-bezier(0.4,1.2,0.6,1)` easing and Lenis Smooth Scroll (`data-lenis`), Framer Motion Layout Physics.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/biipmk-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×4344px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1279px` extracted from `biipmk-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `4px` lateral canvas padding with `12px` grid gap.
- **Border Radius Scale**: `8px`, `15px`, `12px`, `10px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1279px`, `gap: 12px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `4px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:1279px) and (min-width:810px)`, `@media (max-width:809px) and (min-width:0)`, `@media (min-width:810px) and (max-width:1279.98px)`, `@media (max-width:809.98px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--token-a58b3a81-59cc-45f7-ae05-091785ff903e)` in `:root` |
| **Primary Typography Ink** | `#2e2e2f` | `var(--token-9a61cb06-3a3a-4375-8be8-66b9dda45d4e)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff9` | `var(--token-1ef64e56-8935-4468-b341-7e1dc51bb63d)` in `:root` |
| **Interactive Accent / Highlight** | `#f0f0f1` | `var(--token-b3a4db72-7cd5-441a-86c3-f810b7cadc92)` in `:root` |
| **Secondary / Muted Copy** | `#d2d2d2` | `var(--token-f56b1214-00aa-4536-9ffd-154101bb6be0)` in `:root` |
| **Structural Hairline Border** | `#bcbcbd` | `var(--token-63ff77c2-576f-40e9-b4c2-5caf21c4f1e9)` in `:root` |
| **Variable Token (`--token-d752c2e3-4387-4d99-8931-9ec888af3ba1`)** | `#9d9d9f` | `var(--token-d752c2e3-4387-4d99-8931-9ec888af3ba1)` in `:root` |
| **Variable Token (`--token-bc378e3e-7ff2-44fd-a6d1-b4984d382cfe`)** | `#8a8a8c` | `var(--token-bc378e3e-7ff2-44fd-a6d1-b4984d382cfe)` in `:root` |
| **Variable Token (`--token-8a478efd-d44a-4177-9d88-c7291b9d6b8f`)** | `#6d6d6f` | `var(--token-8a478efd-d44a-4177-9d88-c7291b9d6b8f)` in `:root` |
| **Variable Token (`--token-cd0db9f3-e04f-469f-bf1c-a192982ebe5f`)** | `#636365` | `var(--token-cd0db9f3-e04f-469f-bf1c-a192982ebe5f)` in `:root` |
| **Variable Token (`--token-a4711fc1-f7ea-49d6-acf3-e384c36b6979`)** | `#4d4d4f` | `var(--token-a4711fc1-f7ea-49d6-acf3-e384c36b6979)` in `:root` |
| **Variable Token (`--token-ead8cd39-f167-4cb4-a750-94b1094ca9b4`)** | `#3c3c3d` | `var(--token-ead8cd39-f167-4cb4-a750-94b1094ca9b4)` in `:root` |
| **Variable Token (`--token-8dfa6ef2-fdbc-4c8e-8f62-36db9261f81d`)** | `#252526` | `var(--token-8dfa6ef2-fdbc-4c8e-8f62-36db9261f81d)` in `:root` |
| **Variable Token (`--token-2ef8ddb3-0f66-468d-abb6-13d65e017e32`)** | `#d2d2d280` | `var(--token-2ef8ddb3-0f66-468d-abb6-13d65e017e32)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--token-a58b3a81-59cc-45f7-ae05-091785ff903e` | `#fff` | Color / Atmospheric Token |
| `--token-9a61cb06-3a3a-4375-8be8-66b9dda45d4e` | `#2e2e2f` | Color / Atmospheric Token |
| `--token-1ef64e56-8935-4468-b341-7e1dc51bb63d` | `#fff9` | Color / Atmospheric Token |
| `--token-b3a4db72-7cd5-441a-86c3-f810b7cadc92` | `#f0f0f1` | Color / Atmospheric Token |
| `--token-f56b1214-00aa-4536-9ffd-154101bb6be0` | `#d2d2d2` | Color / Atmospheric Token |
| `--token-63ff77c2-576f-40e9-b4c2-5caf21c4f1e9` | `#bcbcbd` | Color / Atmospheric Token |
| `--token-d752c2e3-4387-4d99-8931-9ec888af3ba1` | `#9d9d9f` | Color / Atmospheric Token |
| `--token-bc378e3e-7ff2-44fd-a6d1-b4984d382cfe` | `#8a8a8c` | Color / Atmospheric Token |
| `--token-8a478efd-d44a-4177-9d88-c7291b9d6b8f` | `#6d6d6f` | Color / Atmospheric Token |
| `--token-cd0db9f3-e04f-469f-bf1c-a192982ebe5f` | `#636365` | Color / Atmospheric Token |
| `--token-a4711fc1-f7ea-49d6-acf3-e384c36b6979` | `#4d4d4f` | Color / Atmospheric Token |
| `--token-ead8cd39-f167-4cb4-a750-94b1094ca9b4` | `#3c3c3d` | Color / Atmospheric Token |
| `--token-8dfa6ef2-fdbc-4c8e-8f62-36db9261f81d` | `#252526` | Color / Atmospheric Token |
| `--token-2ef8ddb3-0f66-468d-abb6-13d65e017e32` | `#d2d2d280` | Color / Atmospheric Token |
| `--token-d5e104ff-e396-4ea1-8a79-0d0dbbc87b4d` | `#fff` | Color / Atmospheric Token |
| `--text-decoration-skip-ink` | `var(--framer-text-decoration-skip-ink)` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `IBM Plex Mono`.
- **Primary Body Stack**: `Inter`.
- **Technical / Metadata Stack**: `IBM Plex Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: calc(var(--framer-root-font-s...`, `line-height: 140%`, `letter-spacing: 0em`, `font-weight: 400`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `var(--font-size)`, `var(--framer-font-size)`, `16px`, `93.75%`).
- **Body Copy**: rule `p` (`font-size: calc(var(--framer-root-font-s...`, `line-height: 120%`, `letter-spacing: 0em`, `font-weight: 700`).
- **Metadata & Navigation Labels**: CSS variables `--letter-spacing: var(--framer-letter-spacing)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.4,1.2,0.6,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `#__framer-editorbar-label`**: `transition: opacity 0.4s ease-out` extracted from `biipmk-com` stylesheet.
- **Selector `style]`**: `transition: background 0.2s` extracted from `biipmk-com` stylesheet.
- **Selector `style]`**: `transition: left 0.2s cubic-bezier(0.4,1.2,0.6,1)` extracted from `biipmk-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.4,1.2,0.6,1)`)**: Governs interactive state transitions across `<nav.framer-yfoBI>` and `<article.framer-sbufwg>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — biipmk                                     │
│ ====================================================================== │
│ [ <nav.framer-yfoBI>       | Home · Works · About · Contact         ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <article.framer-sbufwg>                              |   │
│ | H1: M e c h a n i c a l k e y b o a r d s & k e y c a...         |   │
│ | Substrate: #fff       | Ink: #2e2e2f    | Accent: #f0f0f1        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<article.framer-sbufwg>   ) max-w: 1279px         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | S e l e c t e d w o r k s    |  | PBT RAW                      | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 12px  ) | │
│ | [<nav.framer-yfoBI>] -> [<article.framer-sb] -> [<article.framer-sb] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.framer-geIks> ) | https://biipmk.com/                │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.framer-yfoBI> — `biipmk-com`)**:
   - Landmark `<nav class="framer-yfoBI framer-1rw6cnj">` hosting `biipmk` navigation (`Home · Works · About · Contact`), DOM attributes (`data-redirect-timezone="1"`, `data-framer-font-css`, `data-framer-css-ssr-minified`, `data-framer-components="framer-lib-cursors-ho..."`), and stylesheet rule `main { box-sizing:border-box;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<article.framer-sbufwg> — `M e c h a n i c a l k e y b o a r `)**:
   - Landmark `<article class="framer-sbufwg">` presenting display lead `M e c h a n i c a l k e y b o a r d s & k e y c a...` and copy excerpt *"Strasbourg, France."* over `#fff` canvas and `#2e2e2f` ink.
3. **Primary Showcase & Content Grid (<article.framer-sbufwg> — `S e l e c t e d w o r k s`)**:
   - Landmark `<article class="framer-sbufwg">` rendering section `S e l e c t e d w o r k s` with copy *"M e c h a n i c a l"*, asset references (`pmry2NqhXUH8l6AL2sqCWz37mfA.png`, `KonkIH5joVcpFDiWUIosk62WxE8.png`, `02sP8aoNizSrkiNxivI6fvFyU.png`, `framerusercontent.com`), and grid rule `root { -webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale }`.
4. **Interactive Detail & Feature Matrix (<article.framer-sbufwg> — `PBT RAW`)**:
   - Landmark `<article class="framer-sbufwg">` framing `PBT RAW` and `PBTfans No Signal` (*"PBT RAW Year 2022 Type PBT Dye sub keycaps Status Completed"*) with `#fff9` surface cards, `#f0f0f1` accents, and `button { font-family:sans-serif;font-size:12px }`.
5. **Colophon & Global Directory Footer (<footer.framer-geIks> — `https://biipmk.com/`)**:
   - Landmark `<footer class="framer-geIks framer-VygiK">` anchoring `biipmk` footer links (`Home · Works · About · Contact`), copy *"PBTfans No Signal 2 Year 2025 Type PBT Dye sub keycaps Statu"*, and `#bcbcbd` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: biipmk-com (biipmk)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `biipmk-com` (**biipmk** — `https://biipmk.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#2e2e2f` ink, `#f0f0f1` accent).
- **Identity & Domain Context**: French art director and keycap designer with 10+ years experience. Specializing in mechanical keyboard design, custom keycap sets, and vi...
- **Primary Substrate**: `#fff` (`var(--token-a58b3a81-59cc-45f7-ae05-091785ff903e)` in `:root`), **Primary Ink**: `#2e2e2f`, **Accent / Highlight**: `#f0f0f1`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--token-a58b3a81-59cc-45f7-ae05-091785ff903e)` in `:root`) paired with `#2e2e2f` primary typography and `#f0f0f1` accents.
  - **Extracted Typographic Hierarchy**: Pairs `IBM Plex Mono` for display copy (`M e c h a n i c a l k e y b o a r d `) with `Inter` and `IBM Plex Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1279px` container bounds (`gap: 12px`, padding `4px`) with `cubic-bezier(0.4,1.2,0.6,1)` easing and Lenis Smooth Scroll (`data-lenis`), Framer Motion Layout Physics.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `biipmk-com` in your global stylesheet:

:root {
  /* biipmk (biipmk-com) — Ground-Truth Extracted CSS Variables */
  --token-a58b3a81-59cc-45f7-ae05-091785ff903e: #fff; /* Color / Atmospheric Token (biipmk-com) */
  --token-9a61cb06-3a3a-4375-8be8-66b9dda45d4e: #2e2e2f; /* Color / Atmospheric Token (biipmk-com) */
  --token-1ef64e56-8935-4468-b341-7e1dc51bb63d: #fff9; /* Color / Atmospheric Token (biipmk-com) */
  --token-b3a4db72-7cd5-441a-86c3-f810b7cadc92: #f0f0f1; /* Color / Atmospheric Token (biipmk-com) */
  --token-f56b1214-00aa-4536-9ffd-154101bb6be0: #d2d2d2; /* Color / Atmospheric Token (biipmk-com) */
  --token-63ff77c2-576f-40e9-b4c2-5caf21c4f1e9: #bcbcbd; /* Color / Atmospheric Token (biipmk-com) */
  --token-d752c2e3-4387-4d99-8931-9ec888af3ba1: #9d9d9f; /* Color / Atmospheric Token (biipmk-com) */
  --token-bc378e3e-7ff2-44fd-a6d1-b4984d382cfe: #8a8a8c; /* Color / Atmospheric Token (biipmk-com) */
  --token-8a478efd-d44a-4177-9d88-c7291b9d6b8f: #6d6d6f; /* Color / Atmospheric Token (biipmk-com) */
  --token-cd0db9f3-e04f-469f-bf1c-a192982ebe5f: #636365; /* Color / Atmospheric Token (biipmk-com) */
  --token-a4711fc1-f7ea-49d6-acf3-e384c36b6979: #4d4d4f; /* Color / Atmospheric Token (biipmk-com) */
  --token-ead8cd39-f167-4cb4-a750-94b1094ca9b4: #3c3c3d; /* Color / Atmospheric Token (biipmk-com) */
  --token-8dfa6ef2-fdbc-4c8e-8f62-36db9261f81d: #252526; /* Color / Atmospheric Token (biipmk-com) */
  --token-2ef8ddb3-0f66-468d-abb6-13d65e017e32: #d2d2d280; /* Color / Atmospheric Token (biipmk-com) */
  --token-d5e104ff-e396-4ea1-8a79-0d0dbbc87b4d: #fff; /* Color / Atmospheric Token (biipmk-com) */
  --text-decoration-skip-ink: var(--framer-text-decoration-skip-ink); /* Typography Ink Token (biipmk-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fff` — grounded in `var(--token-a58b3a81-59cc-45f7-ae05-091785ff903e)` in `:root`
- **Primary Typography Ink**: `#2e2e2f` — grounded in `var(--token-9a61cb06-3a3a-4375-8be8-66b9dda45d4e)` in `:root`
- **Elevated Surface / Card Substrate**: `#fff9` — grounded in `var(--token-1ef64e56-8935-4468-b341-7e1dc51bb63d)` in `:root`
- **Interactive Accent / Highlight**: `#f0f0f1` — grounded in `var(--token-b3a4db72-7cd5-441a-86c3-f810b7cadc92)` in `:root`
- **Secondary / Muted Copy**: `#d2d2d2` — grounded in `var(--token-f56b1214-00aa-4536-9ffd-154101bb6be0)` in `:root`
- **Structural Hairline Border**: `#bcbcbd` — grounded in `var(--token-63ff77c2-576f-40e9-b4c2-5caf21c4f1e9)` in `:root`
- **Variable Token (`--token-d752c2e3-4387-4d99-8931-9ec888af3ba1`)**: `#9d9d9f` — grounded in `var(--token-d752c2e3-4387-4d99-8931-9ec888af3ba1)` in `:root`
- **Variable Token (`--token-bc378e3e-7ff2-44fd-a6d1-b4984d382cfe`)**: `#8a8a8c` — grounded in `var(--token-bc378e3e-7ff2-44fd-a6d1-b4984d382cfe)` in `:root`
- **Variable Token (`--token-8a478efd-d44a-4177-9d88-c7291b9d6b8f`)**: `#6d6d6f` — grounded in `var(--token-8a478efd-d44a-4177-9d88-c7291b9d6b8f)` in `:root`
- **Variable Token (`--token-cd0db9f3-e04f-469f-bf1c-a192982ebe5f`)**: `#636365` — grounded in `var(--token-cd0db9f3-e04f-469f-bf1c-a192982ebe5f)` in `:root`
- **Variable Token (`--token-a4711fc1-f7ea-49d6-acf3-e384c36b6979`)**: `#4d4d4f` — grounded in `var(--token-a4711fc1-f7ea-49d6-acf3-e384c36b6979)` in `:root`
- **Variable Token (`--token-ead8cd39-f167-4cb4-a750-94b1094ca9b4`)**: `#3c3c3d` — grounded in `var(--token-ead8cd39-f167-4cb4-a750-94b1094ca9b4)` in `:root`
- **Variable Token (`--token-8dfa6ef2-fdbc-4c8e-8f62-36db9261f81d`)**: `#252526` — grounded in `var(--token-8dfa6ef2-fdbc-4c8e-8f62-36db9261f81d)` in `:root`
- **Variable Token (`--token-2ef8ddb3-0f66-468d-abb6-13d65e017e32`)**: `#d2d2d280` — grounded in `var(--token-2ef8ddb3-0f66-468d-abb6-13d65e017e32)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×4344px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1279px` extracted from `biipmk-com` stylesheet
- **Padding & Gutters**: `4px` lateral canvas padding with `12px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1279px`, `gap: 12px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `4px` horizontal padding
- **Media Queries**: `@media (max-width:1279px) and (min-width:810px)`, `@media (max-width:809px) and (min-width:0)`, `@media (min-width:810px) and (max-width:1279.98px)`, `@media (max-width:809.98px)`
- **Corner Radii**: `8px`, `15px`, `12px`, `10px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `IBM Plex Mono`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **H1 Display Rule**: rule `h1` (`font-size: calc(var(--framer-root-font-s...`, `line-height: 140%`, `letter-spacing: 0em`, `font-weight: 400`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `var(--font-size)`, `var(--framer-font-size)`, `16px`, `93.75%`)
- **Body Copy Rule**: rule `p` (`font-size: calc(var(--framer-root-font-s...`, `line-height: 120%`, `letter-spacing: 0em`, `font-weight: 700`)
- **Metadata & Index Rule**: CSS variables `--letter-spacing: var(--framer-letter-spacing)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `biipmk-com` (`biipmk`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.framer-yfoBI> — `biipmk-com`)**:
   - DOM & Selectors: Landmark `<nav class="framer-yfoBI framer-1rw6cnj">` hosting `biipmk` navigation (`Home · Works · About · Contact`), DOM attributes (`data-redirect-timezone="1"`, `data-framer-font-css`, `data-framer-css-ssr-minified`, `data-framer-components="framer-lib-cursors-ho..."`), and stylesheet rule `main { box-sizing:border-box;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.framer-yfoBI> — `biipmk-com`)` (`biipmk-com`) adapts across `@media (max-width:1279px) and (min-width:810px)`, `@media (max-width:809px) and (min-width:0)`, `@media (min-width:810px) and (max-width:1279.98px)`, `@media (max-width:809.98px)` with `cubic-bezier(0.4,1.2,0.6,1)` transitions and links `Home · Works · About · Contact`.
2. **Hero Stage & Focal Lead (<article.framer-sbufwg> — `M e c h a n i c a l k e y b o a r `)**:
   - DOM & Selectors: Landmark `<article class="framer-sbufwg">` presenting display lead `M e c h a n i c a l k e y b o a r d s & k e y c a...` and copy excerpt *"Strasbourg, France."* over `#fff` canvas and `#2e2e2f` ink.
   - Responsive Contract: Hero stage (`1440×4344px` desktop / `390×2400px` mobile) sets `#fff` background with `#2e2e2f` headline `M e c h a n i c a l k e y b o a r d s & k e y c a...`.
3. **Primary Showcase & Content Grid (<article.framer-sbufwg> — `S e l e c t e d w o r k s`)**:
   - DOM & Selectors: Landmark `<article class="framer-sbufwg">` rendering section `S e l e c t e d w o r k s` with copy *"M e c h a n i c a l"*, asset references (`pmry2NqhXUH8l6AL2sqCWz37mfA.png`, `KonkIH5joVcpFDiWUIosk62WxE8.png`, `02sP8aoNizSrkiNxivI6fvFyU.png`, `framerusercontent.com`), and grid rule `root { -webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<article.framer-sbufwg> — `S e l e c t e d w o r k s`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1279px`, `gap: 12px`) on desktop and Single-column vertical stack at `390px` viewport width with `4px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.framer-sbufwg> — `PBT RAW`)**:
   - DOM & Selectors: Landmark `<article class="framer-sbufwg">` framing `PBT RAW` and `PBTfans No Signal` (*"PBT RAW Year 2022 Type PBT Dye sub keycaps Status Completed"*) with `#fff9` surface cards, `#f0f0f1` accents, and `button { font-family:sans-serif;font-size:12px }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.framer-sbufwg> — `PBT RAW`)` uses `8px`, `15px`, `12px`, `10px` radii, `#f0f0f1` highlights, and assets (pmry2NqhXUH8l6AL2sqCWz37mfA.png, KonkIH5joVcpFDiWUIosk62WxE8.png, 02sP8aoNizSrkiNxivI6fvFyU.png).
5. **Colophon & Global Directory Footer (<footer.framer-geIks> — `https://biipmk.com/`)**:
   - DOM & Selectors: Landmark `<footer class="framer-geIks framer-VygiK">` anchoring `biipmk` footer links (`Home · Works · About · Contact`), copy *"PBTfans No Signal 2 Year 2025 Type PBT Dye sub keycaps Statu"*, and `#bcbcbd` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.framer-geIks> — `https://biipmk.com/`)` aligns to `1279px` extracted from `biipmk-com` stylesheet with `4px` lateral canvas padding with `12px` grid gap and attributes (data-redirect-timezone="1", data-framer-font-css, data-framer-css-ssr-minified).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Strasbourg, France."*
- Copy Excerpt 2: *"M e c h a n i c a l"*
- Copy Excerpt 3: *"PBT RAW Year 2022 Type PBT Dye sub keycaps Status Completed"*
- Copy Excerpt 4: *"PBTfans No Signal 2 Year 2025 Type PBT Dye sub keycaps Status Currently available"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.4,1.2,0.6,1)`
- **Extracted Stylesheet Rules (`biipmk-com`)**:
- `main { box-sizing:border-box;margin:0;padding:0 }`
- `root { -webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale }`
- `button { font-family:sans-serif;font-size:12px }`
- `body { --framer-will-change-override:transform }`
- `.framer-text.framer-image { display:var(--text-truncation-display-inline-for-safari-16,revert) }`
- **Per-Selector Transition Rules**:
- **Selector `#__framer-editorbar-label`**: `transition: opacity 0.4s ease-out` extracted from `biipmk-com` stylesheet.
- **Selector `style]`**: `transition: background 0.2s` extracted from `biipmk-com` stylesheet.
- **Selector `style]`**: `transition: left 0.2s cubic-bezier(0.4,1.2,0.6,1)` extracted from `biipmk-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.4,1.2,0.6,1)`)**: Governs interactive state transitions across `<nav.framer-yfoBI>` and `<article.framer-sbufwg>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `biipmk-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
