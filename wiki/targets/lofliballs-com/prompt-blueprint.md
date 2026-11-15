---
title: "UI Prompt Blueprint: lofliballs-com"
date: 2026-11-15
target: "[[overview|lofliballs-com]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#FDFBEE` / `#F5E9A9`)"
---

# UI Design System & Master Generation Blueprint: lofliballs-com

> **LoFli Balls—Innovative Training Tools for Youth Athletes – Lofli** (http://lofliballs.com) — LoFli Balls are weighted training tools with emulated stitching to mimic the feel of a real ball. Flying about half the distance of a sta...

![Desktop Viewport Capture (1440x7969)](file:///root/projects/fleet/wiki/targets/lofliballs-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **LoFli Balls—Innovative Training Tools for Youth Athletes – Lofli** (`http://lofliballs.com`). LoFli Balls are weighted training tools with emulated stitching to mimic the feel of a real ball. Flying about half the distance of a sta...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#FDFBEE` / `#F5E9A9`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#FDFBEE` (`var(--color-yellow-5)` in `:root`) paired with `#F4DF6C` primary typography and `#F5E9A9` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Alumni Sans` for display copy (`Shop All`) with `Albert Sans` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `var(--page-width)` container bounds (`gap: var(--space-8)`, padding `var(--space-16)`) with `cubic-bezier(.34,1.56,.64,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/lofliballs-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×7969px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `var(--page-width)` extracted from `lofliballs-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--space-16)` lateral canvas padding with `var(--space-8)` grid gap.
- **Border Radius Scale**: `4px`, `var(--radius)`, `var(--radius-full)`, `var(--radius-xs)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--page-width)`, `gap: var(--space-8)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--space-16)` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (forced-colors:active)`, `@media screen and (width<=750px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:749px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#FDFBEE` | `var(--color-yellow-5)` in `:root` |
| **Primary Typography Ink** | `#F8F4D9` | `var(--color-yellow-50)` in `:root` |
| **Elevated Surface / Card Substrate** | `#F6EEC2` | `var(--color-yellow-100)` in `:root` |
| **Interactive Accent / Highlight** | `#F5E9A9` | `var(--color-yellow-200)` in `:root` |
| **Secondary / Muted Copy** | `#F4E48D` | `var(--color-yellow-300)` in `:root` |
| **Structural Hairline Border** | `#F4DF6C` | `var(--color-yellow-400)` in `:root` |
| **Variable Token (`--color-yellow-500`)** | `#F4DA40` | `var(--color-yellow-500)` in `:root` |
| **Variable Token (`--color-yellow-600`)** | `#C9940D` | `var(--color-yellow-600)` in `:root` |
| **Variable Token (`--color-yellow-700`)** | `#8E5A0B` | `var(--color-yellow-700)` in `:root` |
| **Variable Token (`--color-yellow-800`)** | `#5D3309` | `var(--color-yellow-800)` in `:root` |
| **Variable Token (`--color-yellow-900`)** | `#361C08` | `var(--color-yellow-900)` in `:root` |
| **Variable Token (`--color-cyan-5`)** | `#F1FDFF` | `var(--color-cyan-5)` in `:root` |
| **Variable Token (`--color-cyan-50`)** | `#D4EDF5` | `var(--color-cyan-50)` in `:root` |
| **Variable Token (`--color-cyan-100`)** | `#B8E2EF` | `var(--color-cyan-100)` in `:root` |
| **Variable Token (`--color-cyan-200`)** | `#9BD8EA` | `var(--color-cyan-200)` in `:root` |
| **Variable Token (`--color-cyan-300`)** | `#7BCEE7` | `var(--color-cyan-300)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-yellow-5` | `#FDFBEE` | Brand / Palette Token |
| `--color-yellow-50` | `#F8F4D9` | Brand / Palette Token |
| `--color-yellow-100` | `#F6EEC2` | Brand / Palette Token |
| `--color-yellow-200` | `#F5E9A9` | Brand / Palette Token |
| `--color-yellow-300` | `#F4E48D` | Brand / Palette Token |
| `--color-yellow-400` | `#F4DF6C` | Brand / Palette Token |
| `--color-yellow-500` | `#F4DA40` | Brand / Palette Token |
| `--color-yellow-600` | `#C9940D` | Brand / Palette Token |
| `--color-yellow-700` | `#8E5A0B` | Brand / Palette Token |
| `--color-yellow-800` | `#5D3309` | Brand / Palette Token |
| `--color-yellow-900` | `#361C08` | Brand / Palette Token |
| `--color-cyan-5` | `#F1FDFF` | Brand / Palette Token |
| `--color-cyan-50` | `#D4EDF5` | Brand / Palette Token |
| `--color-cyan-100` | `#B8E2EF` | Brand / Palette Token |
| `--color-cyan-200` | `#9BD8EA` | Brand / Palette Token |
| `--color-cyan-300` | `#7BCEE7` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Alumni Sans`.
- **Primary Body Stack**: `Albert Sans`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `clamp(var(--font-size-96)`, `clamp(var(--font-size-40)`, `clamp(var(--font-size-32)`, `var(--font-size-32)`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: calc(var(--kl-reviews-reviews...`, `line-height: 122%`, `font-weight: calc(var(--kl...`).
- **Body Copy**: CSS variables `--gw-ball-body: var(--bg-brand)`, `--font-body: Assistant, sans-serif`; rule `p` (`font-size: medium`, `line-height: normal`, `letter-spacing: normal`, `font-weight: normal`).
- **Metadata & Navigation Labels**: rule `small` (`font-size: calc(var(--kl-reviews-reviews...`, `font-weight: var(--kl-revi...`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.34,1.56,.64,1)`, `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.55,0,.68,.3)`.

### Per-Element Transition & Choreography Rules
- **Selector `.shopify-payment-button__button`**: `transition: background .2s ease-in-out` extracted from `lofliballs-com` stylesheet.
- **Selector `.gw-model__poster`**: `transition: opacity .3s` extracted from `lofliballs-com` stylesheet.
- **Selector `media(prefers-reduced-motion:reduce)`**: `transition: none` extracted from `lofliballs-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.34,1.56,.64,1)`)**: Governs interactive state transitions across `<header.gw-header>` and `<section.gw-hero>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — LoFli Balls—Innovative Training Tools for  │
│ ====================================================================== │
│ [ <header.gw-header>       | Shop · Shop All · LoFli Baseball · LoF ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.shopify-section>                            |   │
│ | H1: Shop All                                                     |   │
│ | Substrate: #FDFBEE    | Ink: #F4DF6C    | Accent: #F5E9A9        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.gw-hero>         ) max-w: var(--page-wid |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | LoFli Baseball               |  | LoFli Softball               | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.gw-header>] -> [<section.shopify-s] -> [<section.gw-hero>]  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.gw-footer>    ) | http://lofliballs.com              │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.gw-header> — `lofliballs-com`)**:
   - Landmark `<header class="gw-header gw-header--dark">` hosting `LoFli Balls—Innovative Training Tool` navigation (`Shop · Shop All · LoFli Baseball · LoFli Softball · About`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shop-id="77292208214"`, `data-venmo-supported="false"`, `data-environment="production"`), and stylesheet rule `.shopify-payment-button__button--... { visibility:hidden }`.
2. **Hero Stage & Focal Lead (<section.shopify-section> — `Shop All`)**:
   - Landmark `<section class="shopify-section">` presenting display lead `Shop All` and copy excerpt *"Shop Shop Shop All LoFli Baseball LoFli Baseball LoFli Softball L"* over `#FDFBEE` canvas and `#F4DF6C` ink.
3. **Primary Showcase & Content Grid (<section.gw-hero> — `LoFli Baseball`)**:
   - Landmark `<section class="gw-hero color-scheme-1">` rendering section `LoFli Baseball` with copy *"Shop LoFli Baseball LoFli Baseball LoFli Softball LoFli Softball "*, asset references (`destination`, `1129077949490951`, `fbevents.js`, `lofli-favicon.png`), and grid rule `opify-payment-button__button--unb... { background-color:1990c6;padding:1em 2em }`.
4. **Interactive Detail & Feature Matrix (<section.shopify-section> — `LoFli Softball`)**:
   - Landmark `<section class="shopify-section">` framing `LoFli Softball` and `Swing hard Fly low` (*"Hits like a real ball, but travels about half as far."*) with `#F6EEC2` surface cards, `#F5E9A9` accents, and `ptions.shopify-payment-button__sk... { width:50%;margin-left:25%;margin-right:25%;border-radius:4px!important;h... }`.
5. **Colophon & Global Directory Footer (<footer.gw-footer> — `http://lofliballs.com`)**:
   - Landmark `<footer class="gw-footer gw-footer--black">` anchoring `LoFli Balls—Innovative Training ` footer links (`Shop · Shop All · LoFli Baseball · LoFli Softball · About`), copy *"We built the LoFli ball to fly like a real baseball when thr"*, and `#F4DF6C` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: lofliballs-com (LoFli Balls—Innovative Training Tools for Youth Athletes – Lofli)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `lofliballs-com` (**LoFli Balls—Innovative Training Tools for Youth Athletes – Lofli** — `http://lofliballs.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#FDFBEE` / `#F5E9A9`).
- **Identity & Domain Context**: LoFli Balls are weighted training tools with emulated stitching to mimic the feel of a real ball. Flying about half the distance of a sta...
- **Primary Substrate**: `#FDFBEE` (`var(--color-yellow-5)` in `:root`), **Primary Ink**: `#F4DF6C`, **Accent / Highlight**: `#F5E9A9`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#FDFBEE` (`var(--color-yellow-5)` in `:root`) paired with `#F4DF6C` primary typography and `#F5E9A9` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Alumni Sans` for display copy (`Shop All`) with `Albert Sans` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `var(--page-width)` container bounds (`gap: var(--space-8)`, padding `var(--space-16)`) with `cubic-bezier(.34,1.56,.64,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `lofliballs-com` in your global stylesheet:

:root {
  /* LoFli Balls—Innovative Training Tools for Youth Athletes – Lofli (lofliballs-com) — Ground-Truth Extracted CSS Variables */
  --color-yellow-5: #FDFBEE; /* Brand / Palette Token (lofliballs-com) */
  --color-yellow-50: #F8F4D9; /* Brand / Palette Token (lofliballs-com) */
  --color-yellow-100: #F6EEC2; /* Brand / Palette Token (lofliballs-com) */
  --color-yellow-200: #F5E9A9; /* Brand / Palette Token (lofliballs-com) */
  --color-yellow-300: #F4E48D; /* Brand / Palette Token (lofliballs-com) */
  --color-yellow-400: #F4DF6C; /* Brand / Palette Token (lofliballs-com) */
  --color-yellow-500: #F4DA40; /* Brand / Palette Token (lofliballs-com) */
  --color-yellow-600: #C9940D; /* Brand / Palette Token (lofliballs-com) */
  --color-yellow-700: #8E5A0B; /* Brand / Palette Token (lofliballs-com) */
  --color-yellow-800: #5D3309; /* Brand / Palette Token (lofliballs-com) */
  --color-yellow-900: #361C08; /* Brand / Palette Token (lofliballs-com) */
  --color-cyan-5: #F1FDFF; /* Brand / Palette Token (lofliballs-com) */
  --color-cyan-50: #D4EDF5; /* Brand / Palette Token (lofliballs-com) */
  --color-cyan-100: #B8E2EF; /* Brand / Palette Token (lofliballs-com) */
  --color-cyan-200: #9BD8EA; /* Brand / Palette Token (lofliballs-com) */
  --color-cyan-300: #7BCEE7; /* Brand / Palette Token (lofliballs-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#FDFBEE` — grounded in `var(--color-yellow-5)` in `:root`
- **Primary Typography Ink**: `#F8F4D9` — grounded in `var(--color-yellow-50)` in `:root`
- **Elevated Surface / Card Substrate**: `#F6EEC2` — grounded in `var(--color-yellow-100)` in `:root`
- **Interactive Accent / Highlight**: `#F5E9A9` — grounded in `var(--color-yellow-200)` in `:root`
- **Secondary / Muted Copy**: `#F4E48D` — grounded in `var(--color-yellow-300)` in `:root`
- **Structural Hairline Border**: `#F4DF6C` — grounded in `var(--color-yellow-400)` in `:root`
- **Variable Token (`--color-yellow-500`)**: `#F4DA40` — grounded in `var(--color-yellow-500)` in `:root`
- **Variable Token (`--color-yellow-600`)**: `#C9940D` — grounded in `var(--color-yellow-600)` in `:root`
- **Variable Token (`--color-yellow-700`)**: `#8E5A0B` — grounded in `var(--color-yellow-700)` in `:root`
- **Variable Token (`--color-yellow-800`)**: `#5D3309` — grounded in `var(--color-yellow-800)` in `:root`
- **Variable Token (`--color-yellow-900`)**: `#361C08` — grounded in `var(--color-yellow-900)` in `:root`
- **Variable Token (`--color-cyan-5`)**: `#F1FDFF` — grounded in `var(--color-cyan-5)` in `:root`
- **Variable Token (`--color-cyan-50`)**: `#D4EDF5` — grounded in `var(--color-cyan-50)` in `:root`
- **Variable Token (`--color-cyan-100`)**: `#B8E2EF` — grounded in `var(--color-cyan-100)` in `:root`
- **Variable Token (`--color-cyan-200`)**: `#9BD8EA` — grounded in `var(--color-cyan-200)` in `:root`
- **Variable Token (`--color-cyan-300`)**: `#7BCEE7` — grounded in `var(--color-cyan-300)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×7969px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `var(--page-width)` extracted from `lofliballs-com` stylesheet
- **Padding & Gutters**: `var(--space-16)` lateral canvas padding with `var(--space-8)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--page-width)`, `gap: var(--space-8)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--space-16)` horizontal padding
- **Media Queries**: `@media screen and (forced-colors:active)`, `@media screen and (width<=750px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:749px)`
- **Corner Radii**: `4px`, `var(--radius)`, `var(--radius-full)`, `var(--radius-xs)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Alumni Sans`
- **Body Font Stack**: `Albert Sans`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `clamp(var(--font-size-96)`, `clamp(var(--font-size-40)`, `clamp(var(--font-size-32)`, `var(--font-size-32)`)
- **H2 Section Rule**: rule `h2` (`font-size: calc(var(--kl-reviews-reviews...`, `line-height: 122%`, `font-weight: calc(var(--kl...`)
- **Body Copy Rule**: CSS variables `--gw-ball-body: var(--bg-brand)`, `--font-body: Assistant, sans-serif`; rule `p` (`font-size: medium`, `line-height: normal`, `letter-spacing: normal`, `font-weight: normal`)
- **Metadata & Index Rule**: rule `small` (`font-size: calc(var(--kl-reviews-reviews...`, `font-weight: var(--kl-revi...`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `lofliballs-com` (`LoFli Balls—Innovative Training Tools for Youth Athletes – Lofli`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.gw-header> — `lofliballs-com`)**:
   - DOM & Selectors: Landmark `<header class="gw-header gw-header--dark">` hosting `LoFli Balls—Innovative Training Tool` navigation (`Shop · Shop All · LoFli Baseball · LoFli Softball · About`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shop-id="77292208214"`, `data-venmo-supported="false"`, `data-environment="production"`), and stylesheet rule `.shopify-payment-button__button--... { visibility:hidden }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.gw-header> — `lofliballs-com`)` (`lofliballs-com`) adapts across `@media screen and (forced-colors:active)`, `@media screen and (width<=750px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:749px)` with `cubic-bezier(.34,1.56,.64,1)`, `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.55,0,.68,.3)` transitions and links `Shop · Shop All · LoFli Baseball · LoFli Softball · About`.
2. **Hero Stage & Focal Lead (<section.shopify-section> — `Shop All`)**:
   - DOM & Selectors: Landmark `<section class="shopify-section">` presenting display lead `Shop All` and copy excerpt *"Shop Shop Shop All LoFli Baseball LoFli Baseball LoFli Softball L"* over `#FDFBEE` canvas and `#F4DF6C` ink.
   - Responsive Contract: Hero stage (`1440×7969px` desktop / `390×2400px` mobile) sets `#FDFBEE` background with `#F4DF6C` headline `Shop All`.
3. **Primary Showcase & Content Grid (<section.gw-hero> — `LoFli Baseball`)**:
   - DOM & Selectors: Landmark `<section class="gw-hero color-scheme-1">` rendering section `LoFli Baseball` with copy *"Shop LoFli Baseball LoFli Baseball LoFli Softball LoFli Softball "*, asset references (`destination`, `1129077949490951`, `fbevents.js`, `lofli-favicon.png`), and grid rule `opify-payment-button__button--unb... { background-color:1990c6;padding:1em 2em }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.gw-hero> — `LoFli Baseball`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--page-width)`, `gap: var(--space-8)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--space-16)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.shopify-section> — `LoFli Softball`)**:
   - DOM & Selectors: Landmark `<section class="shopify-section">` framing `LoFli Softball` and `Swing hard Fly low` (*"Hits like a real ball, but travels about half as far."*) with `#F6EEC2` surface cards, `#F5E9A9` accents, and `ptions.shopify-payment-button__sk... { width:50%;margin-left:25%;margin-right:25%;border-radius:4px!important;h... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.shopify-section> — `LoFli Softball`)` uses `4px`, `var(--radius)`, `var(--radius-full)`, `var(--radius-xs)` radii, `#F5E9A9` highlights, and assets (destination, 1129077949490951, fbevents.js).
5. **Colophon & Global Directory Footer (<footer.gw-footer> — `http://lofliballs.com`)**:
   - DOM & Selectors: Landmark `<footer class="gw-footer gw-footer--black">` anchoring `LoFli Balls—Innovative Training ` footer links (`Shop · Shop All · LoFli Baseball · LoFli Softball · About`), copy *"We built the LoFli ball to fly like a real baseball when thr"*, and `#F4DF6C` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.gw-footer> — `http://lofliballs.com`)` aligns to `var(--page-width)` extracted from `lofliballs-com` stylesheet with `var(--space-16)` lateral canvas padding with `var(--space-8)` grid gap and attributes (data-source-attribution="shopify.exit_intersti...", data-shop-id="77292208214", data-venmo-supported="false").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Shop Shop Shop All LoFli Baseball LoFli Baseball LoFli Softball LoFli Softball"*
- Copy Excerpt 2: *"Shop LoFli Baseball LoFli Baseball LoFli Softball LoFli Softball Shop All"*
- Copy Excerpt 3: *"Hits like a real ball, but travels about half as far."*
- Copy Excerpt 4: *"We built the LoFli ball to fly like a real baseball when thrown and to reward soli..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.34,1.56,.64,1)`, `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.55,0,.68,.3)`
- **Extracted Stylesheet Rules (`lofliballs-com`)**:
- `.shopify-payment-button__button--... { visibility:hidden }`
- `opify-payment-button__button--unb... { background-color:1990c6;padding:1em 2em }`
- `ptions.shopify-payment-button__sk... { width:50%;margin-left:25%;margin-right:25%;border-radius:4px!important;h... }`
- `shopify-payment-button__button--b... { z-index:1;flex-direction:column;display:flex;position:relative }`
- `on__button--branded .shopify-clea... { flex-direction:column!important;flex:1!important;display:flex!important }`
- **Per-Selector Transition Rules**:
- **Selector `.shopify-payment-button__button`**: `transition: background .2s ease-in-out` extracted from `lofliballs-com` stylesheet.
- **Selector `.gw-model__poster`**: `transition: opacity .3s` extracted from `lofliballs-com` stylesheet.
- **Selector `media(prefers-reduced-motion:reduce)`**: `transition: none` extracted from `lofliballs-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.34,1.56,.64,1)`)**: Governs interactive state transitions across `<header.gw-header>` and `<section.gw-hero>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `lofliballs-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
