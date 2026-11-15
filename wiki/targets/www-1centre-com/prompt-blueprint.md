---
title: "UI Prompt Blueprint: www-1centre-com"
date: 2026-11-15
target: "[[overview|www-1centre-com]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#f99c00` / `#fff`)"
---

# UI Design System & Master Generation Blueprint: www-1centre-com

> **1Centre — Trade Credit Software for NZ & Australia** (https://www.1centre.com/) — Trade credit software for suppliers in New Zealand and Australia: digital account applications, ID checks, credit decisions, 24/7 monitor...

![Desktop Viewport Capture (1440x18756)](file:///root/projects/fleet/wiki/targets/www-1centre-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **1Centre — Trade Credit Software for NZ & Australia** (`https://www.1centre.com/`). Trade credit software for suppliers in New Zealand and Australia: digital account applications, ID checks, credit decisions, 24/7 monitor...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#f99c00` / `#fff`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f99c00` (`var(--color-amber-500)` in `:root`) paired with `#000` primary typography and `#fff` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter` for display copy (`Trade credit at scale, so you can fo`) with `Inter Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `639px` container bounds (`gap: var(--spacing)`, padding `1.25rem`) with `cubic-bezier(0,0,.2,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-1centre-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×18756px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `639px` extracted from `www-1centre-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `1.25rem` lateral canvas padding with `var(--spacing)` grid gap.
- **Border Radius Scale**: `4px`, `12px`, `2px`, `6px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 639px`, `gap: var(--spacing)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1.25rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (max-width:639px)`, `@media (min-width:1024px)`, `@media (min-width:40rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f99c00` | `var(--color-amber-500)` in `:root` |
| **Primary Typography Ink** | `#b75000` | `var(--color-amber-700)` in `:root` |
| **Elevated Surface / Card Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Interactive Accent / Highlight** | `#fff` | `var(--color-white)` in `:root` |
| **Secondary / Muted Copy** | `#fafbfa` | `var(--color-canvas)` in `:root` |
| **Structural Hairline Border** | `#101112` | `var(--color-ink)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--dot-r` | `0px` | Dimension / Scale Token |
| `--qc-r` | `60%` | Dimension / Scale Token |
| `--qc-r2` | `70%` | Dimension / Scale Token |
| `--font-sans` | `var(--font-inter), ui-sans-serif, system-ui, -apple-system, sans-serif` | Typography / Scale Token |
| `--font-serif` | `ui-serif, Georgia, Cambria, "Times New Roman", Times, serif` | Typography / Scale Token |
| `--color-amber-500` | `#f99c00` | Brand / Palette Token |
| `--color-amber-700` | `#b75000` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--text-4xl` | `2.25rem` | Typography Ink Token |
| `--text-4xl--line-height` | `calc(2.5 / 2.25)` | Typography Ink Token |
| `--text-5xl` | `3rem` | Typography Ink Token |
| `--text-5xl--line-height` | `1` | Typography Ink Token |
| `--font-weight-light` | `300` | Canvas / Surface Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Inter`.
- **Primary Body Stack**: `Inter Fallback`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`.
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `15.5px`, `13.5px`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `15.5px`, `13.5px`).
- **Metadata & Navigation Labels**: CSS variables `--default-mono-font-family: var(--font-mono)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `www-1centre-com` stylesheet.
- **Selector `.v10-art`**: `transition: opacity .4s` extracted from `www-1centre-com` stylesheet.
- **Selector `.v8-card .v8-ui`**: `transition: transform .9s var(--ease-out-expo)` extracted from `www-1centre-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.sticky>` and `<section.group>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — 1Centre — Trade Credit Software for NZ & A │
│ ====================================================================== │
│ [ <header.sticky>          | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.relative>                                   |   │
│ | H1: Trade credit at scale, so you can focus on sales.            |   │
│ | Substrate: #f99c00    | Ink: #000       | Accent: #fff           |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.group>           ) max-w: 639px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Build trade credit workflows |  | Open trade accounts from the | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.sticky>] -> [<section.relative>] -> [<section.group>] |     │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.relative>     ) | https://www.1centre.com/           │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.sticky> — `www-1centre-com`)**:
   - Landmark `<header class="sticky top-0">` hosting `1Centre — Trade Credit Software for ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-nimg="1"`, `data-dark="true"`), and stylesheet rule `host { --color-amber-500:lab(72.7183% 31.8672 97.9407);--color-amber-700:lab(47... }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Trade credit at scale, so you can `)**:
   - Landmark `<section class="relative overflow-hidden">` presenting display lead `Trade credit at scale, so you can focus on sales.` and copy excerpt *"Trade credit at scale,"* over `#f99c00` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.group> — `Build trade credit workflows on ev`)**:
   - Landmark `<section class="group border-y">` rendering section `Build trade credit workflows on everything your b...` with copy *"so you can focus on sales."*, asset references (`5e4d537aaa9e154b-s.p.0g9-.3zp53cu...`, `83afe278b6a6bb3c-s.p.0q-301v4kxxn...`, `logo-mark.svg`, `mitre10.svg`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.mx-auto> — `Open trade accounts from the count`)**:
   - Landmark `<section class="mx-auto scroll-mt-20">` framing `Open trade accounts from the counter, the web, yo...` and `Write your own credit rules — and let them decide...` (*"1Centre helps businesses across all industries trade with trust. "*) with `#000` surface cards, `#fff` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://www.1centre.com/`)**:
   - Landmark `<footer class="relative overflow-hidden">` anchoring `1Centre — Trade Credit Software ` footer links (`Overview · Index · Archive · About · Contact`), copy *"1Centre helps businesses across all industries"*, and `#101112` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-1centre-com (1Centre — Trade Credit Software for NZ & Australia)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-1centre-com` (**1Centre — Trade Credit Software for NZ & Australia** — `https://www.1centre.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f99c00` / `#fff`).
- **Identity & Domain Context**: Trade credit software for suppliers in New Zealand and Australia: digital account applications, ID checks, credit decisions, 24/7 monitor...
- **Primary Substrate**: `#f99c00` (`var(--color-amber-500)` in `:root`), **Primary Ink**: `#000`, **Accent / Highlight**: `#fff`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f99c00` (`var(--color-amber-500)` in `:root`) paired with `#000` primary typography and `#fff` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter` for display copy (`Trade credit at scale, so you can fo`) with `Inter Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `639px` container bounds (`gap: var(--spacing)`, padding `1.25rem`) with `cubic-bezier(0,0,.2,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-1centre-com` in your global stylesheet:

:root {
  /* 1Centre — Trade Credit Software for NZ & Australia (www-1centre-com) — Ground-Truth Extracted CSS Variables */
  --dot-r: 0px; /* Dimension / Scale Token (www-1centre-com) */
  --qc-r: 60%; /* Dimension / Scale Token (www-1centre-com) */
  --qc-r2: 70%; /* Dimension / Scale Token (www-1centre-com) */
  --font-sans: var(--font-inter), ui-sans-serif, system-ui, -apple-system, sans-serif; /* Typography / Scale Token (www-1centre-com) */
  --font-serif: ui-serif, Georgia, Cambria, "Times New Roman", Times, serif; /* Typography / Scale Token (www-1centre-com) */
  --color-amber-500: #f99c00; /* Brand / Palette Token (www-1centre-com) */
  --color-amber-700: #b75000; /* Brand / Palette Token (www-1centre-com) */
  --color-black: #000; /* Canvas / Surface Token (www-1centre-com) */
  --color-white: #fff; /* Canvas / Surface Token (www-1centre-com) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (www-1centre-com) */
  --text-4xl: 2.25rem; /* Typography Ink Token (www-1centre-com) */
  --text-4xl--line-height: calc(2.5 / 2.25); /* Typography Ink Token (www-1centre-com) */
  --text-5xl: 3rem; /* Typography Ink Token (www-1centre-com) */
  --text-5xl--line-height: 1; /* Typography Ink Token (www-1centre-com) */
  --font-weight-light: 300; /* Canvas / Surface Token (www-1centre-com) */
  --font-weight-normal: 400; /* Typography / Scale Token (www-1centre-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f99c00` — grounded in `var(--color-amber-500)` in `:root`
- **Primary Typography Ink**: `#b75000` — grounded in `var(--color-amber-700)` in `:root`
- **Elevated Surface / Card Substrate**: `#000` — grounded in `var(--color-black)` in `:root`
- **Interactive Accent / Highlight**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Secondary / Muted Copy**: `#fafbfa` — grounded in `var(--color-canvas)` in `:root`
- **Structural Hairline Border**: `#101112` — grounded in `var(--color-ink)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×18756px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `639px` extracted from `www-1centre-com` stylesheet
- **Padding & Gutters**: `1.25rem` lateral canvas padding with `var(--spacing)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 639px`, `gap: var(--spacing)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1.25rem` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (max-width:639px)`, `@media (min-width:1024px)`, `@media (min-width:40rem)`
- **Corner Radii**: `4px`, `12px`, `2px`, `6px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `15.5px`, `13.5px`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `15.5px`, `13.5px`)
- **Metadata & Index Rule**: CSS variables `--default-mono-font-family: var(--font-mono)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-1centre-com` (`1Centre — Trade Credit Software for NZ & Australia`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.sticky> — `www-1centre-com`)**:
   - DOM & Selectors: Landmark `<header class="sticky top-0">` hosting `1Centre — Trade Credit Software for ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-nimg="1"`, `data-dark="true"`), and stylesheet rule `host { --color-amber-500:lab(72.7183% 31.8672 97.9407);--color-amber-700:lab(47... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.sticky> — `www-1centre-com`)` (`www-1centre-com`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (max-width:639px)`, `@media (min-width:1024px)`, `@media (min-width:40rem)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.relative> — `Trade credit at scale, so you can `)**:
   - DOM & Selectors: Landmark `<section class="relative overflow-hidden">` presenting display lead `Trade credit at scale, so you can focus on sales.` and copy excerpt *"Trade credit at scale,"* over `#f99c00` canvas and `#000` ink.
   - Responsive Contract: Hero stage (`1440×18756px` desktop / `390×2400px` mobile) sets `#f99c00` background with `#000` headline `Trade credit at scale, so you can focus on sales.`.
3. **Primary Showcase & Content Grid (<section.group> — `Build trade credit workflows on ev`)**:
   - DOM & Selectors: Landmark `<section class="group border-y">` rendering section `Build trade credit workflows on everything your b...` with copy *"so you can focus on sales."*, asset references (`5e4d537aaa9e154b-s.p.0g9-.3zp53cu...`, `83afe278b6a6bb3c-s.p.0q-301v4kxxn...`, `logo-mark.svg`, `mitre10.svg`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.group> — `Build trade credit workflows on ev`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 639px`, `gap: var(--spacing)`) on desktop and Single-column vertical stack at `390px` viewport width with `1.25rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.mx-auto> — `Open trade accounts from the count`)**:
   - DOM & Selectors: Landmark `<section class="mx-auto scroll-mt-20">` framing `Open trade accounts from the counter, the web, yo...` and `Write your own credit rules — and let them decide...` (*"1Centre helps businesses across all industries trade with trust. "*) with `#000` surface cards, `#fff` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.mx-auto> — `Open trade accounts from the count`)` uses `4px`, `12px`, `2px`, `6px` radii, `#fff` highlights, and assets (5e4d537aaa9e154b-s.p.0g9-.3zp53cu..., 83afe278b6a6bb3c-s.p.0q-301v4kxxn..., logo-mark.svg).
5. **Colophon & Global Directory Footer (<footer.relative> — `https://www.1centre.com/`)**:
   - DOM & Selectors: Landmark `<footer class="relative overflow-hidden">` anchoring `1Centre — Trade Credit Software ` footer links (`Overview · Index · Archive · About · Contact`), copy *"1Centre helps businesses across all industries"*, and `#101112` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.relative> — `https://www.1centre.com/`)` aligns to `639px` extracted from `www-1centre-com` stylesheet with `1.25rem` lateral canvas padding with `var(--spacing)` grid gap and attributes (data-precedence="next", data-precedence="next", data-nimg="1").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Trade credit at scale,"*
- Copy Excerpt 2: *"so you can focus on sales."*
- Copy Excerpt 3: *"1Centre helps businesses across all industries trade with trust. Our secure Trans-..."*
- Copy Excerpt 4: *"1Centre helps businesses across all industries"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`www-1centre-com`)**:
- `host { --color-amber-500:lab(72.7183% 31.8672 97.9407);--color-amber-700:lab(47... }`
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `www-1centre-com` stylesheet.
- **Selector `.v10-art`**: `transition: opacity .4s` extracted from `www-1centre-com` stylesheet.
- **Selector `.v8-card .v8-ui`**: `transition: transform .9s var(--ease-out-expo)` extracted from `www-1centre-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.sticky>` and `<section.group>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-1centre-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
