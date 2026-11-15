---
title: "UI Prompt Blueprint: www-lev-com"
date: 2026-11-15
target: "[[overview|www-lev-com]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#243c33` / `#fbfaf6`)"
---

# UI Design System & Master Generation Blueprint: www-lev-com

> **Lev · The AI platform for commercial real estate** (https://www.lev.com/) — Lev combines the industry's largest source of real-time commercial real estate data with purpose-built AI to transform the way sponsors a...

![Desktop Viewport Capture (1440x3365)](file:///root/projects/fleet/wiki/targets/www-lev-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Lev · The AI platform for commercial real estate** (`https://www.lev.com/`). Lev combines the industry's largest source of real-time commercial real estate data with purpose-built AI to transform the way sponsors a...
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#243c33` / `#fbfaf6`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#243c33` (`var(--illustration-foreground)` in `:root`) paired with `#fff` primary typography and `#fbfaf6` accents.
  - **Extracted Typographic Hierarchy**: Pairs `IBM Plex Sans` for display copy (`Do less work. Close more deals.`) with `IBM Plex Mono` and `IBM Plex Sans`.
  - **Calibrated Spatial Grid & Motion**: Combines `var(--container-lev-max)` container bounds (`gap: var(--spacing)`, padding `var(--container-lev-inline-padding)`) with `cubic-bezier(0,0,.2,1)` easing and Framer Motion Layout Physics, HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-lev-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×3365px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `var(--container-lev-max)` extracted from `www-lev-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--container-lev-inline-padding)` lateral canvas padding with `var(--spacing)` grid gap.
- **Border Radius Scale**: `.3125rem`, `.375rem`, `.25rem`, `12px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--container-lev-max)`, `gap: var(--spacing)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--container-lev-inline-padding)` horizontal padding.
- **Extracted CSS Media Queries**: `@media not all and (min-width:48rem)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#243c33` | `var(--illustration-foreground)` in `:root` |
| **Primary Typography Ink** | `#5c7563` | `var(--illustration-accent)` in `:root` |
| **Elevated Surface / Card Substrate** | `#d6e1d3` | `var(--illustration-fill)` in `:root` |
| **Interactive Accent / Highlight** | `#fbfaf6` | `var(--illustration-on-accent)` in `:root` |
| **Secondary / Muted Copy** | `#e7e5db` | `var(--illustration-surface)` in `:root` |
| **Structural Hairline Border** | `#fff` | `var(--m-surface)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--shimmer-angle` | `20deg` | Design System Custom Token |
| `--scroll-fade-t` | `0px` | Dimension / Scale Token |
| `--scroll-fade-b` | `0px` | Dimension / Scale Token |
| `--scroll-fade-s` | `0px` | Dimension / Scale Token |
| `--scroll-fade-e` | `0px` | Dimension / Scale Token |
| `--scroll-fade-mask` | `initial` | Design System Custom Token |
| `--shimmer-image` | `initial` | Design System Custom Token |
| `--shimmer-text-fill` | `initial` | Typography Ink Token |
| `--beam-angle` | `0deg` | Design System Custom Token |
| `--font-sans` | `"IBM Plex Sans", ui-sans-serif, system-ui, sans-serif` | Typography / Scale Token |
| `--font-serif` | `ui-serif, Georgia, Cambria, "Times New Roman", Times, serif` | Typography / Scale Token |
| `--font-mono` | `"IBM Plex Mono", ui-monospace, monospace` | Typography / Scale Token |
| `--color-red-300` | `oklch(var(--primitive-red-300))` | Brand / Palette Token |
| `--color-red-400` | `oklch(var(--primitive-red-400))` | Brand / Palette Token |
| `--color-red-500` | `oklch(var(--primitive-red-500))` | Brand / Palette Token |
| `--color-red-700` | `oklch(var(--primitive-red-700))` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `IBM Plex Sans`.
- **Primary Body Stack**: `IBM Plex Mono`.
- **Technical / Metadata Stack**: `IBM Plex Sans`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`; rule `h1` (`font-size: var(--text-size-base)`, `line-height: var(--tw-leading,var(...`).
- **Section Heading (`H2`)**: CSS variables `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl--line-height: calc(2.25 / 1.875)`; rule `h2` (`font-size: var(--text-size-base)`, `line-height: var(--tw-leading,var(...`).
- **Body Copy**: CSS variables `--text-base--line-height: calc(1.5 / 1)`, `--insights-body: 13px`, `--mini-demo-body-size: 13px`; rule `p` (`line-height: 1.55`).
- **Metadata & Navigation Labels**: CSS variables `--font-mono: "IBM Plex Mono", ui-monospace, monospace`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm--line-height: calc(1.25 / .875)`; rule `small` (`font-size: 11px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `www-lev-com` stylesheet.
- **Selector `body`**: `transition: background-color .3s,color .3s` extracted from `www-lev-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-lev-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.marketing-page-section>`.
- **Runtime Interaction Engine**: Integrates Framer Motion Layout Physics, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Lev · The AI platform for commercial real  │
│ ====================================================================== │
│ [ <header.site-header>     | Login · Talk to sales                  ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.dark>                                       |   │
│ | H1: Do less work. Close more deals.                              |   │
│ | Substrate: #243c33    | Ink: #fff       | Accent: #fbfaf6        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.marketing-page-se) max-w: var(--containe |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Workflows                    |  | Products                     | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.site-heade] -> [<section.dark>] -> [<section.marketing] |   │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>  ) | https://www.lev.com/               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.site-header> — `www-lev-com`)**:
   - Landmark `<header class="site-header fixed">` hosting `Lev · The AI platform for commercial` navigation (`Login · Talk to sales`), DOM attributes (`data-scroll-behavior="smooth"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `host { --shimmer-angle:20deg }`.
2. **Hero Stage & Focal Lead (<section.dark> — `Do less work. Close more deals.`)**:
   - Landmark `<section class="dark">` presenting display lead `Do less work. Close more deals.` and copy excerpt *"Lev brings cutting-edge superintelligence products and experience"* over `#243c33` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.marketing-page-section> — `Workflows`)**:
   - Landmark `<section class="marketing-page-section scroll-mt-16">` rendering section `Workflows` with copy *"Trusted by leading commercial real estate teams"*, asset references (`matthews.svg`, `time-equities.svg`, `mag-capital.svg`, `essex-capital-markets.svg`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.Footer-module__yg9ahW__column> — `Products`)**:
   - Landmark `<section class="Footer-module__yg9ahW__column">` framing `Products` and `Platform` (*"See their success stories"*) with `#d6e1d3` surface cards, `#fbfaf6` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://www.lev.com/`)**:
   - Landmark `<footer class="site-footer border-t">` anchoring `Lev · The AI platform for commer` footer links (`Login · Talk to sales`), copy *"Commercial real estate software"*, and `#fff` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-lev-com (Lev · The AI platform for commercial real estate)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-lev-com` (**Lev · The AI platform for commercial real estate** — `https://www.lev.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#243c33` / `#fbfaf6`).
- **Identity & Domain Context**: Lev combines the industry's largest source of real-time commercial real estate data with purpose-built AI to transform the way sponsors a...
- **Primary Substrate**: `#243c33` (`var(--illustration-foreground)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#fbfaf6`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#243c33` (`var(--illustration-foreground)` in `:root`) paired with `#fff` primary typography and `#fbfaf6` accents.
  - **Extracted Typographic Hierarchy**: Pairs `IBM Plex Sans` for display copy (`Do less work. Close more deals.`) with `IBM Plex Mono` and `IBM Plex Sans`.
  - **Calibrated Spatial Grid & Motion**: Combines `var(--container-lev-max)` container bounds (`gap: var(--spacing)`, padding `var(--container-lev-inline-padding)`) with `cubic-bezier(0,0,.2,1)` easing and Framer Motion Layout Physics, HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-lev-com` in your global stylesheet:

:root {
  /* Lev · The AI platform for commercial real estate (www-lev-com) — Ground-Truth Extracted CSS Variables */
  --shimmer-angle: 20deg; /* Design System Custom Token (www-lev-com) */
  --scroll-fade-t: 0px; /* Dimension / Scale Token (www-lev-com) */
  --scroll-fade-b: 0px; /* Dimension / Scale Token (www-lev-com) */
  --scroll-fade-s: 0px; /* Dimension / Scale Token (www-lev-com) */
  --scroll-fade-e: 0px; /* Dimension / Scale Token (www-lev-com) */
  --scroll-fade-mask: initial; /* Design System Custom Token (www-lev-com) */
  --shimmer-image: initial; /* Design System Custom Token (www-lev-com) */
  --shimmer-text-fill: initial; /* Typography Ink Token (www-lev-com) */
  --beam-angle: 0deg; /* Design System Custom Token (www-lev-com) */
  --font-sans: "IBM Plex Sans", ui-sans-serif, system-ui, sans-serif; /* Typography / Scale Token (www-lev-com) */
  --font-serif: ui-serif, Georgia, Cambria, "Times New Roman", Times, serif; /* Typography / Scale Token (www-lev-com) */
  --font-mono: "IBM Plex Mono", ui-monospace, monospace; /* Typography / Scale Token (www-lev-com) */
  --color-red-300: oklch(var(--primitive-red-300)); /* Brand / Palette Token (www-lev-com) */
  --color-red-400: oklch(var(--primitive-red-400)); /* Brand / Palette Token (www-lev-com) */
  --color-red-500: oklch(var(--primitive-red-500)); /* Brand / Palette Token (www-lev-com) */
  --color-red-700: oklch(var(--primitive-red-700)); /* Brand / Palette Token (www-lev-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#243c33` — grounded in `var(--illustration-foreground)` in `:root`
- **Primary Typography Ink**: `#5c7563` — grounded in `var(--illustration-accent)` in `:root`
- **Elevated Surface / Card Substrate**: `#d6e1d3` — grounded in `var(--illustration-fill)` in `:root`
- **Interactive Accent / Highlight**: `#fbfaf6` — grounded in `var(--illustration-on-accent)` in `:root`
- **Secondary / Muted Copy**: `#e7e5db` — grounded in `var(--illustration-surface)` in `:root`
- **Structural Hairline Border**: `#fff` — grounded in `var(--m-surface)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×3365px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `var(--container-lev-max)` extracted from `www-lev-com` stylesheet
- **Padding & Gutters**: `var(--container-lev-inline-padding)` lateral canvas padding with `var(--spacing)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--container-lev-max)`, `gap: var(--spacing)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--container-lev-inline-padding)` horizontal padding
- **Media Queries**: `@media not all and (min-width:48rem)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`
- **Corner Radii**: `.3125rem`, `.375rem`, `.25rem`, `12px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `IBM Plex Sans`
- **Body Font Stack**: `IBM Plex Mono`
- **Monospace / Technical Font Stack**: `IBM Plex Sans`
- **H1 Display Rule**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`; rule `h1` (`font-size: var(--text-size-base)`, `line-height: var(--tw-leading,var(...`)
- **H2 Section Rule**: CSS variables `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl--line-height: calc(2.25 / 1.875)`; rule `h2` (`font-size: var(--text-size-base)`, `line-height: var(--tw-leading,var(...`)
- **Body Copy Rule**: CSS variables `--text-base--line-height: calc(1.5 / 1)`, `--insights-body: 13px`, `--mini-demo-body-size: 13px`; rule `p` (`line-height: 1.55`)
- **Metadata & Index Rule**: CSS variables `--font-mono: "IBM Plex Mono", ui-monospace, monospace`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm--line-height: calc(1.25 / .875)`; rule `small` (`font-size: 11px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-lev-com` (`Lev · The AI platform for commercial real estate`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.site-header> — `www-lev-com`)**:
   - DOM & Selectors: Landmark `<header class="site-header fixed">` hosting `Lev · The AI platform for commercial` navigation (`Login · Talk to sales`), DOM attributes (`data-scroll-behavior="smooth"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `host { --shimmer-angle:20deg }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.site-header> — `www-lev-com`)` (`www-lev-com`) adapts across `@media not all and (min-width:48rem)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)` transitions and links `Login · Talk to sales`.
2. **Hero Stage & Focal Lead (<section.dark> — `Do less work. Close more deals.`)**:
   - DOM & Selectors: Landmark `<section class="dark">` presenting display lead `Do less work. Close more deals.` and copy excerpt *"Lev brings cutting-edge superintelligence products and experience"* over `#243c33` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×3365px` desktop / `390×2400px` mobile) sets `#243c33` background with `#fff` headline `Do less work. Close more deals.`.
3. **Primary Showcase & Content Grid (<section.marketing-page-section> — `Workflows`)**:
   - DOM & Selectors: Landmark `<section class="marketing-page-section scroll-mt-16">` rendering section `Workflows` with copy *"Trusted by leading commercial real estate teams"*, asset references (`matthews.svg`, `time-equities.svg`, `mag-capital.svg`, `essex-capital-markets.svg`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.marketing-page-section> — `Workflows`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--container-lev-max)`, `gap: var(--spacing)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--container-lev-inline-padding)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.Footer-module__yg9ahW__column> — `Products`)**:
   - DOM & Selectors: Landmark `<section class="Footer-module__yg9ahW__column">` framing `Products` and `Platform` (*"See their success stories"*) with `#d6e1d3` surface cards, `#fbfaf6` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.Footer-module__yg9ahW__column> — `Products`)` uses `.3125rem`, `.375rem`, `.25rem`, `12px` radii, `#fbfaf6` highlights, and assets (matthews.svg, time-equities.svg, mag-capital.svg).
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://www.lev.com/`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer border-t">` anchoring `Lev · The AI platform for commer` footer links (`Login · Talk to sales`), copy *"Commercial real estate software"*, and `#fff` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-footer> — `https://www.lev.com/`)` aligns to `var(--container-lev-max)` extracted from `www-lev-com` stylesheet with `var(--container-lev-inline-padding)` lateral canvas padding with `var(--spacing)` grid gap and attributes (data-scroll-behavior="smooth", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Lev brings cutting-edge superintelligence products and experiences to the best com..."*
- Copy Excerpt 2: *"Trusted by leading commercial real estate teams"*
- Copy Excerpt 3: *"See their success stories"*
- Copy Excerpt 4: *"Commercial real estate software"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`
- **Extracted Stylesheet Rules (`www-lev-com`)**:
- `host { --shimmer-angle:20deg }`
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `www-lev-com` stylesheet.
- **Selector `body`**: `transition: background-color .3s,color .3s` extracted from `www-lev-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-lev-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.marketing-page-section>`.
- **Runtime Interaction Engine**: Integrates Framer Motion Layout Physics, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-lev-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
