---
title: "UI Prompt Blueprint: www-weisslameraner-com_en"
date: 2026-11-15
target: "[[overview|www-weisslameraner-com_en]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#fef2f2` canvas, `#bf000f` ink, `#fb2c36` accent)"
---

# UI Design System & Master Generation Blueprint: www-weisslameraner-com_en

> **Weiss & Lameraner Media Group – Lifestyle Media House Vienna** (https://www.weisslameraner.com/en) — Vienna media house: STYLE UP YOUR LIFE!, Y, OBEGG and ADIWEISS.TV. Advertising in print, online, social and TV, plus content and events f...

![Desktop Viewport Capture (1440x8878)](file:///root/projects/fleet/wiki/targets/www-weisslameraner-com_en/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Weiss & Lameraner Media Group – Lifestyle Media House Vienna** (`https://www.weisslameraner.com/en`). Vienna media house: STYLE UP YOUR LIFE!, Y, OBEGG and ADIWEISS.TV. Advertising in print, online, social and TV, plus content and events f...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#fef2f2` canvas, `#bf000f` ink, `#fb2c36` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fef2f2` (`var(--color-red-50)` in `:root`) paired with `#bf000f` primary typography and `#fb2c36` accents.
  - **Extracted Typographic Hierarchy**: Pairs `figtreeUpright` for display copy (`Lifestyle media for your brand.`) with `figtreeUpright Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--spacing)`, padding `1.5rem`) with `cubic-bezier(0,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`).

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-weisslameraner-com_en/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×8878px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40rem` extracted from `www-weisslameraner-com_en` stylesheet.
- **Canvas Lateral Padding & Spacing**: `1.5rem` lateral canvas padding with `var(--spacing)` grid gap.
- **Border Radius Scale**: `.3125rem`, `.375rem`, `.25rem`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1.5rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fef2f2` | `var(--color-red-50)` in `:root` |
| **Primary Typography Ink** | `#ffcaca` | `var(--color-red-200)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ffa3a3` | `var(--color-red-300)` in `:root` |
| **Interactive Accent / Highlight** | `#fb2c36` | `var(--color-red-500)` in `:root` |
| **Secondary / Muted Copy** | `#e40014` | `var(--color-red-600)` in `:root` |
| **Structural Hairline Border** | `#bf000f` | `var(--color-red-700)` in `:root` |
| **Variable Token (`--color-amber-400`)** | `#fcbb00` | `var(--color-amber-400)` in `:root` |
| **Variable Token (`--color-amber-500`)** | `#f99c00` | `var(--color-amber-500)` in `:root` |
| **Variable Token (`--color-amber-600`)** | `#dd7400` | `var(--color-amber-600)` in `:root` |
| **Variable Token (`--color-amber-700`)** | `#b75000` | `var(--color-amber-700)` in `:root` |
| **Variable Token (`--color-green-50`)** | `#f0fdf4` | `var(--color-green-50)` in `:root` |
| **Variable Token (`--color-green-200`)** | `#b9f8cf` | `var(--color-green-200)` in `:root` |
| **Variable Token (`--color-green-400`)** | `#05df72` | `var(--color-green-400)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--trigger-left` | `0` | Design System Custom Token |
| `--font-sans` | `var(--font-figtree)` | Typography / Scale Token |
| `--font-serif` | `ui-serif, Georgia, Cambria, "Times New Roman", Times, serif` | Typography / Scale Token |
| `--color-red-50` | `#fef2f2` | Brand / Palette Token |
| `--color-red-200` | `#ffcaca` | Brand / Palette Token |
| `--color-red-300` | `#ffa3a3` | Brand / Palette Token |
| `--color-red-500` | `#fb2c36` | Brand / Palette Token |
| `--color-red-600` | `#e40014` | Brand / Palette Token |
| `--color-red-700` | `#bf000f` | Brand / Palette Token |
| `--color-amber-400` | `#fcbb00` | Brand / Palette Token |
| `--color-amber-500` | `#f99c00` | Brand / Palette Token |
| `--color-amber-600` | `#dd7400` | Brand / Palette Token |
| `--color-amber-700` | `#b75000` | Brand / Palette Token |
| `--color-green-50` | `#f0fdf4` | Brand / Palette Token |
| `--color-green-200` | `#b9f8cf` | Brand / Palette Token |
| `--color-green-400` | `#05df72` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `figtreeUpright`.
- **Primary Body Stack**: `figtreeUpright Fallback`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`.
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: inherit!important`, `line-height: normal`, `letter-spacing: normal`, `font-weight: inherit`).
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`.
- **Metadata & Navigation Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`; rule `small` (`font-size: .36em`, `letter-spacing: .02em`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `www-weisslameraner-com_en` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-weisslameraner-com_en` stylesheet.
- **Selector `.transition-\[background-size\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-weisslameraner-com_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.fixed>` and `<section.bg-white>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`) with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Weiss & Lameraner Media Group – Lifestyle  │
│ ====================================================================== │
│ [ <header.fixed>           | About · Services · Media · Brand Event ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.relative>                                   |   │
│ | H1: Lifestyle media for your brand.                              |   │
│ | Substrate: #fef2f2    | Ink: #bf000f    | Accent: #fb2c36        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.bg-white>        ) max-w: 40rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Brands that work with us.    |  | Austria's media house for li | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.fixed>] -> [<section.relative>] -> [<section.bg-white>] |   │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.border-t>     ) | https://www.weisslameraner.com/en  │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.fixed> — `www-weisslameraner-com_en`)**:
   - Landmark `<header class="fixed top-0">` hosting `Weiss & Lameraner Media Group – Life` navigation (`About · Services · Media · Brand Events · WLX`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="cms-o9gdh8"`, `data-href="cms-o9gdh8"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Lifestyle media for your brand.`)**:
   - Landmark `<section class="relative bg-white">` presenting display lead `Lifestyle media for your brand.` and copy excerpt *"Media Data 2027 Media Data 2027"* over `#fef2f2` canvas and `#bf000f` ink.
3. **Primary Showcase & Content Grid (<section.bg-white> — `Brands that work with us.`)**:
   - Landmark `<section class="bg-white py-16">` rendering section `Brands that work with us.` with copy *"(opens in a new window)"*, asset references (`Figtree_VariableFont_wght-s.p.0r5...`, `3emm7imx_eab9.css`, `1lfjsiuslldzn.css`, `37mpl03i35te0.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Austria's media house for lifestyl`)**:
   - Landmark `<section class="relative overflow-hidden">` framing `Austria's media house for lifestyle.` and `Guide for brands What do you want to achieve? Dis...` (*"Austria's media house"*) with `#ffa3a3` surface cards, `#fb2c36` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.border-t> — `https://www.weisslameraner.com/en`)**:
   - Landmark `<footer class="border-t bg-stone-950">` anchoring `Weiss & Lameraner Media Group – ` footer links (`About · Services · Media · Brand Events · WLX`), copy *"Since 2009 we have been taking brands to where their audienc"*, and `#bf000f` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-weisslameraner-com_en (Weiss & Lameraner Media Group – Lifestyle Media House Vienna)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-weisslameraner-com_en` (**Weiss & Lameraner Media Group – Lifestyle Media House Vienna** — `https://www.weisslameraner.com/en`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#fef2f2` canvas, `#bf000f` ink, `#fb2c36` accent).
- **Identity & Domain Context**: Vienna media house: STYLE UP YOUR LIFE!, Y, OBEGG and ADIWEISS.TV. Advertising in print, online, social and TV, plus content and events f...
- **Primary Substrate**: `#fef2f2` (`var(--color-red-50)` in `:root`), **Primary Ink**: `#bf000f`, **Accent / Highlight**: `#fb2c36`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fef2f2` (`var(--color-red-50)` in `:root`) paired with `#bf000f` primary typography and `#fb2c36` accents.
  - **Extracted Typographic Hierarchy**: Pairs `figtreeUpright` for display copy (`Lifestyle media for your brand.`) with `figtreeUpright Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--spacing)`, padding `1.5rem`) with `cubic-bezier(0,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`).

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-weisslameraner-com_en` in your global stylesheet:

:root {
  /* Weiss & Lameraner Media Group – Lifestyle Media House Vienna (www-weisslameraner-com_en) — Ground-Truth Extracted CSS Variables */
  --trigger-left: 0; /* Design System Custom Token (www-weisslameraner-com_en) */
  --font-sans: var(--font-figtree); /* Typography / Scale Token (www-weisslameraner-com_en) */
  --font-serif: ui-serif, Georgia, Cambria, "Times New Roman", Times, serif; /* Typography / Scale Token (www-weisslameraner-com_en) */
  --color-red-50: #fef2f2; /* Brand / Palette Token (www-weisslameraner-com_en) */
  --color-red-200: #ffcaca; /* Brand / Palette Token (www-weisslameraner-com_en) */
  --color-red-300: #ffa3a3; /* Brand / Palette Token (www-weisslameraner-com_en) */
  --color-red-500: #fb2c36; /* Brand / Palette Token (www-weisslameraner-com_en) */
  --color-red-600: #e40014; /* Brand / Palette Token (www-weisslameraner-com_en) */
  --color-red-700: #bf000f; /* Brand / Palette Token (www-weisslameraner-com_en) */
  --color-amber-400: #fcbb00; /* Brand / Palette Token (www-weisslameraner-com_en) */
  --color-amber-500: #f99c00; /* Brand / Palette Token (www-weisslameraner-com_en) */
  --color-amber-600: #dd7400; /* Brand / Palette Token (www-weisslameraner-com_en) */
  --color-amber-700: #b75000; /* Brand / Palette Token (www-weisslameraner-com_en) */
  --color-green-50: #f0fdf4; /* Brand / Palette Token (www-weisslameraner-com_en) */
  --color-green-200: #b9f8cf; /* Brand / Palette Token (www-weisslameraner-com_en) */
  --color-green-400: #05df72; /* Brand / Palette Token (www-weisslameraner-com_en) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fef2f2` — grounded in `var(--color-red-50)` in `:root`
- **Primary Typography Ink**: `#ffcaca` — grounded in `var(--color-red-200)` in `:root`
- **Elevated Surface / Card Substrate**: `#ffa3a3` — grounded in `var(--color-red-300)` in `:root`
- **Interactive Accent / Highlight**: `#fb2c36` — grounded in `var(--color-red-500)` in `:root`
- **Secondary / Muted Copy**: `#e40014` — grounded in `var(--color-red-600)` in `:root`
- **Structural Hairline Border**: `#bf000f` — grounded in `var(--color-red-700)` in `:root`
- **Variable Token (`--color-amber-400`)**: `#fcbb00` — grounded in `var(--color-amber-400)` in `:root`
- **Variable Token (`--color-amber-500`)**: `#f99c00` — grounded in `var(--color-amber-500)` in `:root`
- **Variable Token (`--color-amber-600`)**: `#dd7400` — grounded in `var(--color-amber-600)` in `:root`
- **Variable Token (`--color-amber-700`)**: `#b75000` — grounded in `var(--color-amber-700)` in `:root`
- **Variable Token (`--color-green-50`)**: `#f0fdf4` — grounded in `var(--color-green-50)` in `:root`
- **Variable Token (`--color-green-200`)**: `#b9f8cf` — grounded in `var(--color-green-200)` in `:root`
- **Variable Token (`--color-green-400`)**: `#05df72` — grounded in `var(--color-green-400)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×8878px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40rem` extracted from `www-weisslameraner-com_en` stylesheet
- **Padding & Gutters**: `1.5rem` lateral canvas padding with `var(--spacing)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1.5rem` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `.3125rem`, `.375rem`, `.25rem`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `figtreeUpright`
- **Body Font Stack**: `figtreeUpright Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: inherit!important`, `line-height: normal`, `letter-spacing: normal`, `font-weight: inherit`)
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Index Rule**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`; rule `small` (`font-size: .36em`, `letter-spacing: .02em`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-weisslameraner-com_en` (`Weiss & Lameraner Media Group – Lifestyle Media House Vienna`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.fixed> — `www-weisslameraner-com_en`)**:
   - DOM & Selectors: Landmark `<header class="fixed top-0">` hosting `Weiss & Lameraner Media Group – Life` navigation (`About · Services · Media · Brand Events · WLX`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="cms-o9gdh8"`, `data-href="cms-o9gdh8"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.fixed> — `www-weisslameraner-com_en`)` (`www-weisslameraner-com_en`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)` transitions and links `About · Services · Media · Brand Events · WLX`.
2. **Hero Stage & Focal Lead (<section.relative> — `Lifestyle media for your brand.`)**:
   - DOM & Selectors: Landmark `<section class="relative bg-white">` presenting display lead `Lifestyle media for your brand.` and copy excerpt *"Media Data 2027 Media Data 2027"* over `#fef2f2` canvas and `#bf000f` ink.
   - Responsive Contract: Hero stage (`1440×8878px` desktop / `390×2400px` mobile) sets `#fef2f2` background with `#bf000f` headline `Lifestyle media for your brand.`.
3. **Primary Showcase & Content Grid (<section.bg-white> — `Brands that work with us.`)**:
   - DOM & Selectors: Landmark `<section class="bg-white py-16">` rendering section `Brands that work with us.` with copy *"(opens in a new window)"*, asset references (`Figtree_VariableFont_wght-s.p.0r5...`, `3emm7imx_eab9.css`, `1lfjsiuslldzn.css`, `37mpl03i35te0.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.bg-white> — `Brands that work with us.`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing)`) on desktop and Single-column vertical stack at `390px` viewport width with `1.5rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Austria's media house for lifestyl`)**:
   - DOM & Selectors: Landmark `<section class="relative overflow-hidden">` framing `Austria's media house for lifestyle.` and `Guide for brands What do you want to achieve? Dis...` (*"Austria's media house"*) with `#ffa3a3` surface cards, `#fb2c36` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.relative> — `Austria's media house for lifestyl`)` uses `.3125rem`, `.375rem`, `.25rem`, `2px` radii, `#fb2c36` highlights, and assets (Figtree_VariableFont_wght-s.p.0r5..., 3emm7imx_eab9.css, 1lfjsiuslldzn.css).
5. **Colophon & Global Directory Footer (<footer.border-t> — `https://www.weisslameraner.com/en`)**:
   - DOM & Selectors: Landmark `<footer class="border-t bg-stone-950">` anchoring `Weiss & Lameraner Media Group – ` footer links (`About · Services · Media · Brand Events · WLX`), copy *"Since 2009 we have been taking brands to where their audienc"*, and `#bf000f` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.border-t> — `https://www.weisslameraner.com/en`)` aligns to `40rem` extracted from `www-weisslameraner-com_en` stylesheet with `1.5rem` lateral canvas padding with `var(--spacing)` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="cms-o9gdh8").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Media Data 2027 Media Data 2027"*
- Copy Excerpt 2: *"(opens in a new window)"*
- Copy Excerpt 3: *"Austria's media house"*
- Copy Excerpt 4: *"Since 2009 we have been taking brands to where their audience is: into our four me..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`
- **Extracted Stylesheet Rules (`www-weisslameraner-com_en`)**:
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { vertical-align:baseline;font-size:75%;line-height:0;position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `www-weisslameraner-com_en` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-weisslameraner-com_en` stylesheet.
- **Selector `.transition-\[background-size\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-weisslameraner-com_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.fixed>` and `<section.bg-white>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`) with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-weisslameraner-com_en`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
