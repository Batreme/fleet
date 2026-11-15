---
title: "UI Prompt Blueprint: www-fieldrank-run"
date: 2026-11-15
target: "www-fieldrank-run"
status: analyzed
capture: dom
capture_desktop: dom
capture_mobile: dom
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#faf9f6` ink, `#faf9f6` accent)"
---

# UI Design System & Master Generation Blueprint: www-fieldrank-run

> **FieldRank: Trail and ultra rankings** (https://www.fieldrank.run) — A season ranking of trail and ultra runners, built from race results. Overall and by distance.

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **FieldRank: Trail and ultra rankings** (`https://www.fieldrank.run`). A season ranking of trail and ultra runners, built from race results. Overall and by distance.
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#faf9f6` ink, `#faf9f6` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#faf9f6` primary typography and `#faf9f6` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Geist` for display copy (`Trail and ultra rankings`) with `Geist Fallback` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `var(--container-6xl)` container bounds (`gap: var(--card-spacing)`, padding `var(--card-spacing)`) with `cubic-bezier(.4,0,.6,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×1266px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `var(--container-6xl)` extracted from `www-fieldrank-run` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--card-spacing)` lateral canvas padding with `var(--card-spacing)` grid gap.
- **Border Radius Scale**: `.25rem`, `1px`, `2px`, `3px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--container-6xl)`, `gap: var(--card-spacing)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--card-spacing)` horizontal padding.
- **Extracted CSS Media Queries**: `@media not all and (min-width:40rem)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#f1efea` | `var(--background)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1e1d1a` | `var(--foreground)` in `:root` |
| **Interactive Accent / Highlight** | `#faf9f6` | `var(--card)` in `:root` |
| **Secondary / Muted Copy** | `#e9e6df` | `var(--secondary)` in `:root` |
| **Structural Hairline Border** | `#66635d` | `var(--muted-foreground)` in `:root` |

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
| `--font-sans` | `var(--font-sans)` | Typography / Scale Token |
| `--font-mono` | `var(--font-mono)` | Typography / Scale Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-sm` | `24rem` | Layout / Spatial Grid Token |
| `--container-md` | `28rem` | Layout / Spatial Grid Token |
| `--container-6xl` | `72rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Geist`.
- **Primary Body Stack**: `Geist Fallback`.
- **Technical / Metadata Stack**: `Geist Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`.
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`.
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`.
- **Metadata & Navigation Labels**: CSS variables `--font-mono: var(--font-mono)`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `www-fieldrank-run` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-fieldrank-run` stylesheet.
- **Selector `.transition-all`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-fieldrank-run` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.6,1)`)**: Governs interactive state transitions across `<header.sticky>` and `<div.min-h-screen>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<div.light>` and `<div.min-h-screen>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — FieldRank: Trail and ultra rankings        │
│ ====================================================================== │
│ [ <header.sticky>          | Rankings · Races                       ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <div.light>                                          |   │
│ | H1: Trail and ultra rankings                                     |   │
│ | Substrate: #000       | Ink: #faf9f6    | Accent: #faf9f6        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<div.min-h-screen>        ) max-w: var(--containe |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Season in progress           |  | A season ranking of trail an | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.sticky>] -> [<div.light>] -> [<div.min-h-screen>] |         │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.text-foregroun) | https://www.fieldrank.run          │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.sticky> — `www-fieldrank-run`)**:
   - Landmark `<header class="sticky top-0">` hosting `FieldRank: Trail and ultra rankings` navigation (`Rankings · Races`), DOM attributes (`data-precedence="next"`, `data-site="KPVLKBUA"`, `data-auto="false"`, `data-slot="button"`), and stylesheet rule `host { --shimmer-angle:20deg }`.
2. **Hero Stage & Focal Lead (<div.light> — `Trail and ultra rankings`)**:
   - Landmark `<div class="light">` presenting display lead `Trail and ultra rankings` and copy excerpt *"Season in progress"* over `#000` canvas and `#faf9f6` ink.
3. **Primary Showcase & Content Grid (<div.min-h-screen> — `Season in progress`)**:
   - Landmark `<div class="min-h-screen">` rendering section `Season in progress` with copy *"A season ranking of trail and ultra runners, built from race resu"*, asset references (`2oz0lep7db5t2.css`, `0jvhpaew_uadu.js`, `script.js`, `19mx3mg6lkumu.js`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<div.bg-background> — `A season ranking of trail and ultr`)**:
   - Landmark `<div class="bg-background">` framing `A season ranking of trail and ultra runners, bui` and `Mallorca - CDA 2026` (*"Mallorca - CDA 2026"*) with `#1e1d1a` surface cards, `#faf9f6` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.text-foreground> — `https://www.fieldrank.run`)**:
   - Landmark `<footer class="text-foreground">` anchoring `FieldRank: Trail and ultra ranki` footer links (`Rankings · Races`), copy *"2026-11-01 · Valldemossa, Spain · Marathon · 564 results"*, and `#66635d` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-fieldrank-run (FieldRank: Trail and ultra rankings)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-fieldrank-run` (**FieldRank: Trail and ultra rankings** — `https://www.fieldrank.run`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#faf9f6` ink, `#faf9f6` accent).
- **Identity & Domain Context**: A season ranking of trail and ultra runners, built from race results. Overall and by distance.
- **Primary Substrate**: `#000` (`var(--color-black)` in `:root`), **Primary Ink**: `#faf9f6`, **Accent / Highlight**: `#faf9f6`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#faf9f6` primary typography and `#faf9f6` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Geist` for display copy (`Trail and ultra rankings`) with `Geist Fallback` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `var(--container-6xl)` container bounds (`gap: var(--card-spacing)`, padding `var(--card-spacing)`) with `cubic-bezier(.4,0,.6,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-fieldrank-run` in your global stylesheet:

:root {
  /* FieldRank: Trail and ultra rankings (www-fieldrank-run) — Ground-Truth Extracted CSS Variables */
  --shimmer-angle: 20deg; /* Design System Custom Token (www-fieldrank-run) */
  --scroll-fade-t: 0px; /* Dimension / Scale Token (www-fieldrank-run) */
  --scroll-fade-b: 0px; /* Dimension / Scale Token (www-fieldrank-run) */
  --scroll-fade-s: 0px; /* Dimension / Scale Token (www-fieldrank-run) */
  --scroll-fade-e: 0px; /* Dimension / Scale Token (www-fieldrank-run) */
  --scroll-fade-mask: initial; /* Design System Custom Token (www-fieldrank-run) */
  --shimmer-image: initial; /* Design System Custom Token (www-fieldrank-run) */
  --shimmer-text-fill: initial; /* Typography Ink Token (www-fieldrank-run) */
  --font-sans: var(--font-sans); /* Typography / Scale Token (www-fieldrank-run) */
  --font-mono: var(--font-mono); /* Typography / Scale Token (www-fieldrank-run) */
  --color-black: #000; /* Canvas / Surface Token (www-fieldrank-run) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (www-fieldrank-run) */
  --container-sm: 24rem; /* Layout / Spatial Grid Token (www-fieldrank-run) */
  --container-md: 28rem; /* Layout / Spatial Grid Token (www-fieldrank-run) */
  --container-6xl: 72rem; /* Layout / Spatial Grid Token (www-fieldrank-run) */
  --text-xs: .75rem; /* Typography Ink Token (www-fieldrank-run) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--color-black)` in `:root`
- **Primary Typography Ink**: `#f1efea` — grounded in `var(--background)` in `:root`
- **Elevated Surface / Card Substrate**: `#1e1d1a` — grounded in `var(--foreground)` in `:root`
- **Interactive Accent / Highlight**: `#faf9f6` — grounded in `var(--card)` in `:root`
- **Secondary / Muted Copy**: `#e9e6df` — grounded in `var(--secondary)` in `:root`
- **Structural Hairline Border**: `#66635d` — grounded in `var(--muted-foreground)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×1266px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `var(--container-6xl)` extracted from `www-fieldrank-run` stylesheet
- **Padding & Gutters**: `var(--card-spacing)` lateral canvas padding with `var(--card-spacing)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--container-6xl)`, `gap: var(--card-spacing)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--card-spacing)` horizontal padding
- **Media Queries**: `@media not all and (min-width:40rem)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`
- **Corner Radii**: `.25rem`, `1px`, `2px`, `3px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `Geist Fallback`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **H1 Display Rule**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Index Rule**: CSS variables `--font-mono: var(--font-mono)`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-fieldrank-run` (`FieldRank: Trail and ultra rankings`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.sticky> — `www-fieldrank-run`)**:
   - DOM & Selectors: Landmark `<header class="sticky top-0">` hosting `FieldRank: Trail and ultra rankings` navigation (`Rankings · Races`), DOM attributes (`data-precedence="next"`, `data-site="KPVLKBUA"`, `data-auto="false"`, `data-slot="button"`), and stylesheet rule `host { --shimmer-angle:20deg }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.sticky> — `www-fieldrank-run`)` (`www-fieldrank-run`) adapts across `@media not all and (min-width:40rem)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)` with `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Rankings · Races`.
2. **Hero Stage & Focal Lead (<div.light> — `Trail and ultra rankings`)**:
   - DOM & Selectors: Landmark `<div class="light">` presenting display lead `Trail and ultra rankings` and copy excerpt *"Season in progress"* over `#000` canvas and `#faf9f6` ink.
   - Responsive Contract: Hero stage (`1440×1266px` desktop / `390×2400px` mobile) sets `#000` background with `#faf9f6` headline `Trail and ultra rankings`.
3. **Primary Showcase & Content Grid (<div.min-h-screen> — `Season in progress`)**:
   - DOM & Selectors: Landmark `<div class="min-h-screen">` rendering section `Season in progress` with copy *"A season ranking of trail and ultra runners, built from race resu"*, asset references (`2oz0lep7db5t2.css`, `0jvhpaew_uadu.js`, `script.js`, `19mx3mg6lkumu.js`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<div.min-h-screen> — `Season in progress`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--container-6xl)`, `gap: var(--card-spacing)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--card-spacing)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<div.bg-background> — `A season ranking of trail and ultr`)**:
   - DOM & Selectors: Landmark `<div class="bg-background">` framing `A season ranking of trail and ultra runners, bui` and `Mallorca - CDA 2026` (*"Mallorca - CDA 2026"*) with `#1e1d1a` surface cards, `#faf9f6` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<div.bg-background> — `A season ranking of trail and ultr`)` uses `.25rem`, `1px`, `2px`, `3px` radii, `#faf9f6` highlights, and assets (2oz0lep7db5t2.css, 0jvhpaew_uadu.js, script.js).
5. **Colophon & Global Directory Footer (<footer.text-foreground> — `https://www.fieldrank.run`)**:
   - DOM & Selectors: Landmark `<footer class="text-foreground">` anchoring `FieldRank: Trail and ultra ranki` footer links (`Rankings · Races`), copy *"2026-11-01 · Valldemossa, Spain · Marathon · 564 results"*, and `#66635d` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.text-foreground> — `https://www.fieldrank.run`)` aligns to `var(--container-6xl)` extracted from `www-fieldrank-run` stylesheet with `var(--card-spacing)` lateral canvas padding with `var(--card-spacing)` grid gap and attributes (data-precedence="next", data-site="KPVLKBUA", data-auto="false").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Season in progress"*
- Copy Excerpt 2: *"A season ranking of trail and ultra runners, built from race results. Overall and..."*
- Copy Excerpt 3: *"Mallorca - CDA 2026"*
- Copy Excerpt 4: *"2026-11-01 · Valldemossa, Spain · Marathon · 564 results"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`www-fieldrank-run`)**:
- `host { --shimmer-angle:20deg }`
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `www-fieldrank-run` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-fieldrank-run` stylesheet.
- **Selector `.transition-all`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-fieldrank-run` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.6,1)`)**: Governs interactive state transitions across `<header.sticky>` and `<div.min-h-screen>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<div.light>` and `<div.min-h-screen>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-fieldrank-run`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
