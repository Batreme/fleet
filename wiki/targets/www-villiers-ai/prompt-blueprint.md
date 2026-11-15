---
title: "UI Prompt Blueprint: www-villiers-ai"
date: 2026-11-15
target: "[[overview|www-villiers-ai]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#0f0f15` canvas, `#f8f9f9` ink, `#1a1a1f` accent)"
---

# UI Design System & Master Generation Blueprint: www-villiers-ai

> **Private Jet Charter and Empty Leg Flights · Villiers** (https://www.villiers.ai/) — Charter a private jet or find an empty leg flight. Villiers is an independent broker that compares vetted operators and quotes one clear...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Private Jet Charter and Empty Leg Flights · Villiers** (`https://www.villiers.ai/`). Charter a private jet or find an empty leg flight. Villiers is an independent broker that compares vetted operators and quotes one clear...
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#0f0f15` canvas, `#f8f9f9` ink, `#1a1a1f` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#0f0f15` (`var(--empty-bg)` in `:root`) paired with `#f8f9f9` primary typography and `#1a1a1f` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Benton Fallback` for display copy (`1. Your Route`) with `Haas Display Fallback` and `JetBrains Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1400px` container bounds (`gap: .125rem`, padding `2rem`) with `cubic-bezier(0,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1400px` extracted from `www-villiers-ai` stylesheet.
- **Canvas Lateral Padding & Spacing**: `2rem` lateral canvas padding with `.125rem` grid gap.
- **Border Radius Scale**: `.25rem`, `1rem`, `1.5rem`, `11px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1400px`, `gap: .125rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `2rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:1400px)`, `@media (min-width:390px)`, `@media (min-width:744px)`, `@media (min-width:1280px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0f0f15` | `var(--empty-bg)` in `:root` |
| **Primary Typography Ink** | `#f8f9f9` | `var(--empty-fg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#d9d9d9` | `var(--empty-sec)` in `:root` |
| **Interactive Accent / Highlight** | `#1a1a1f` | `var(--empty-search-bg)` in `:root` |
| **Secondary / Muted Copy** | `#b4b4b2` | `var(--empty-pill-unselected-text)` in `:root` |
| **Structural Hairline Border** | `#29292b` | `var(--empty-card-bg)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--mobile-bar-h` | `4rem` | Dimension / Scale Token |
| `--background` | `222 47% 11%` | Canvas / Surface Token |
| `--foreground` | `210 40% 98%` | Typography Ink Token |
| `--card` | `222 47% 11%` | Dimension / Scale Token |
| `--card-foreground` | `210 40% 98%` | Typography Ink Token |
| `--popover` | `222 47% 11%` | Dimension / Scale Token |
| `--popover-foreground` | `210 40% 98%` | Typography Ink Token |
| `--primary` | `210 40% 98%` | Brand / Palette Token |
| `--primary-foreground` | `222 47% 11%` | Typography Ink Token |
| `--secondary` | `217.2 32.6% 17.5%` | Brand / Palette Token |
| `--secondary-foreground` | `210 40% 98%` | Typography Ink Token |
| `--muted` | `217.2 32.6% 17.5%` | Dimension / Scale Token |
| `--muted-foreground` | `215 20.2% 82%` | Typography Ink Token |
| `--accent` | `217.2 32.6% 17.5%` | Brand / Palette Token |
| `--accent-foreground` | `210 40% 98%` | Typography Ink Token |
| `--destructive` | `0 62.8% 30.6%` | Dimension / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Benton Fallback`.
- **Primary Body Stack**: `Haas Display Fallback`.
- **Technical / Metadata Stack**: `JetBrains Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-h1: 4rem`, `--text-h1-clamp: clamp(64px,4rem,160px)`.
- **Section Heading (`H2`)**: CSS variables `--text-h2: 3.25rem`, `--text-h2-small: 2.333rem`, `--text-h2-clamp: clamp(52px,3.25rem,68px)`.
- **Body Copy**: CSS variables `--text-body: clamp(16px,1rem,9999px)`, `--text-body-sm: clamp(14px,0.875rem,9999px)`, `--text-body-xs: clamp(12px,0.75rem,9999px)`; rule `p` (`line-height: 1.625`).
- **Metadata & Navigation Labels**: CSS variables `--text-h2-small: 2.333rem`, `--text-h2-small-clamp: clamp(37px,2.333rem,44px)`, `--font-jetbrains-mono: "JetBrains Mono","JetBrains Mono Fallback",Menlo,ui-monospace,monospace`; rule `.meta` (`font-size: 13px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.transition`**: `transition: cubic-bezier(0,0,.2,1)` extracted from `www-villiers-ai` stylesheet.
- **Selector `sition-\[border-color\2c backgrou...`**: `transition: cubic-bezier(0,0,.2,1)` extracted from `www-villiers-ai` stylesheet.
- **Selector `.transition-\[color\2c transform\]`**: `transition: cubic-bezier(0,0,.2,1)` extracted from `www-villiers-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.fixed>` and `<section.py-section-lg>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Private Jet Charter and Empty Leg Flights  │
│ ====================================================================== │
│ [ <header.fixed>           | H H O O M M E E · B B L L O O G G · A  ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.relative>                                   |   │
│ | H1: 1. Your Route                                                |   │
│ | Substrate: #0f0f15    | Ink: #f8f9f9    | Accent: #1a1a1f        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.py-section-lg>   ) max-w: 1400px         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | New Trip                     |  | Summary                      | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .125re) | │
│ | [<header.fixed>] -> [<section.relative>] -> [<section.py-sectio] |   │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.flex>         ) | https://www.villiers.ai/           │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.fixed> — `www-villiers-ai`)**:
   - Landmark `<header class="fixed left-0">` hosting `Private Jet Charter and Empty Leg Fl` navigation (`H H O O M M E E · B B L L O O G G · A A B B O O U U T T`), DOM attributes (`data-header-ready="true"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.relative> — `1. Your Route`)**:
   - Landmark `<section class="relative min-h-screen">` presenting display lead `1. Your Route` and copy excerpt *"E E M M P P T T Y Y L L E E G G S S"* over `#0f0f15` canvas and `#f8f9f9` ink.
3. **Primary Showcase & Content Grid (<section.py-section-lg> — `New Trip`)**:
   - Landmark `<section class="py-section-lg bg-neutral-50">` rendering section `New Trip` with copy *"E E M M P P T T Y Y"*, asset references (`0484562807a97172-s.p.woff2`, `2cc74b96cdc9383d-s.p.woff2`, `36966cca54120369-s.p.woff2`, `427e4a37d3642943-s.p.woff2`), and grid rule `body { margin:0;line-height:inherit }`.
4. **Interactive Detail & Feature Matrix (<section.py-section-lg> — `Summary`)**:
   - Landmark `<section class="py-section-lg bg-neutral-50">` framing `Summary` and `Special Requirements` (*"v v i i l l l l i i e e r r s s O O S S"*) with `#d9d9d9` surface cards, `#1a1a1f` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.flex> — `https://www.villiers.ai/`)**:
   - Landmark `<footer class="flex flex-col">` anchoring `Private Jet Charter and Empty Le` footer links (`H H O O M M E E · B B L L O O G G · A A B B O O U U T T`), copy *"B B I I T T C C O O I I N N"*, and `#29292b` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-villiers-ai (Private Jet Charter and Empty Leg Flights · Villiers)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-villiers-ai` (**Private Jet Charter and Empty Leg Flights · Villiers** — `https://www.villiers.ai/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0f0f15` canvas, `#f8f9f9` ink, `#1a1a1f` accent).
- **Identity & Domain Context**: Charter a private jet or find an empty leg flight. Villiers is an independent broker that compares vetted operators and quotes one clear...
- **Primary Substrate**: `#0f0f15` (`var(--empty-bg)` in `:root`), **Primary Ink**: `#f8f9f9`, **Accent / Highlight**: `#1a1a1f`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#0f0f15` (`var(--empty-bg)` in `:root`) paired with `#f8f9f9` primary typography and `#1a1a1f` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Benton Fallback` for display copy (`1. Your Route`) with `Haas Display Fallback` and `JetBrains Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1400px` container bounds (`gap: .125rem`, padding `2rem`) with `cubic-bezier(0,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-villiers-ai` in your global stylesheet:

:root {
  /* Private Jet Charter and Empty Leg Flights · Villiers (www-villiers-ai) — Ground-Truth Extracted CSS Variables */
  --mobile-bar-h: 4rem; /* Dimension / Scale Token (www-villiers-ai) */
  --background: 222 47% 11%; /* Canvas / Surface Token (www-villiers-ai) */
  --foreground: 210 40% 98%; /* Typography Ink Token (www-villiers-ai) */
  --card: 222 47% 11%; /* Dimension / Scale Token (www-villiers-ai) */
  --card-foreground: 210 40% 98%; /* Typography Ink Token (www-villiers-ai) */
  --popover: 222 47% 11%; /* Dimension / Scale Token (www-villiers-ai) */
  --popover-foreground: 210 40% 98%; /* Typography Ink Token (www-villiers-ai) */
  --primary: 210 40% 98%; /* Brand / Palette Token (www-villiers-ai) */
  --primary-foreground: 222 47% 11%; /* Typography Ink Token (www-villiers-ai) */
  --secondary: 217.2 32.6% 17.5%; /* Brand / Palette Token (www-villiers-ai) */
  --secondary-foreground: 210 40% 98%; /* Typography Ink Token (www-villiers-ai) */
  --muted: 217.2 32.6% 17.5%; /* Dimension / Scale Token (www-villiers-ai) */
  --muted-foreground: 215 20.2% 82%; /* Typography Ink Token (www-villiers-ai) */
  --accent: 217.2 32.6% 17.5%; /* Brand / Palette Token (www-villiers-ai) */
  --accent-foreground: 210 40% 98%; /* Typography Ink Token (www-villiers-ai) */
  --destructive: 0 62.8% 30.6%; /* Dimension / Scale Token (www-villiers-ai) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#0f0f15` — grounded in `var(--empty-bg)` in `:root`
- **Primary Typography Ink**: `#f8f9f9` — grounded in `var(--empty-fg)` in `:root`
- **Elevated Surface / Card Substrate**: `#d9d9d9` — grounded in `var(--empty-sec)` in `:root`
- **Interactive Accent / Highlight**: `#1a1a1f` — grounded in `var(--empty-search-bg)` in `:root`
- **Secondary / Muted Copy**: `#b4b4b2` — grounded in `var(--empty-pill-unselected-text)` in `:root`
- **Structural Hairline Border**: `#29292b` — grounded in `var(--empty-card-bg)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1400px` extracted from `www-villiers-ai` stylesheet
- **Padding & Gutters**: `2rem` lateral canvas padding with `.125rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1400px`, `gap: .125rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `2rem` horizontal padding
- **Media Queries**: `@media (min-width:1400px)`, `@media (min-width:390px)`, `@media (min-width:744px)`, `@media (min-width:1280px)`
- **Corner Radii**: `.25rem`, `1rem`, `1.5rem`, `11px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Benton Fallback`
- **Body Font Stack**: `Haas Display Fallback`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **H1 Display Rule**: CSS variables `--text-h1: 4rem`, `--text-h1-clamp: clamp(64px,4rem,160px)`
- **H2 Section Rule**: CSS variables `--text-h2: 3.25rem`, `--text-h2-small: 2.333rem`, `--text-h2-clamp: clamp(52px,3.25rem,68px)`
- **Body Copy Rule**: CSS variables `--text-body: clamp(16px,1rem,9999px)`, `--text-body-sm: clamp(14px,0.875rem,9999px)`, `--text-body-xs: clamp(12px,0.75rem,9999px)`; rule `p` (`line-height: 1.625`)
- **Metadata & Index Rule**: CSS variables `--text-h2-small: 2.333rem`, `--text-h2-small-clamp: clamp(37px,2.333rem,44px)`, `--font-jetbrains-mono: "JetBrains Mono","JetBrains Mono Fallback",Menlo,ui-monospace,monospace`; rule `.meta` (`font-size: 13px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-villiers-ai` (`Private Jet Charter and Empty Leg Flights · Villiers`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.fixed> — `www-villiers-ai`)**:
   - DOM & Selectors: Landmark `<header class="fixed left-0">` hosting `Private Jet Charter and Empty Leg Fl` navigation (`H H O O M M E E · B B L L O O G G · A A B B O O U U T T`), DOM attributes (`data-header-ready="true"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid e5e7eb }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.fixed> — `www-villiers-ai`)` (`www-villiers-ai`) adapts across `@media (min-width:1400px)`, `@media (min-width:390px)`, `@media (min-width:744px)`, `@media (min-width:1280px)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `H H O O M M E E · B B L L O O G G · A A B B O O U U T T`.
2. **Hero Stage & Focal Lead (<section.relative> — `1. Your Route`)**:
   - DOM & Selectors: Landmark `<section class="relative min-h-screen">` presenting display lead `1. Your Route` and copy excerpt *"E E M M P P T T Y Y L L E E G G S S"* over `#0f0f15` canvas and `#f8f9f9` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#0f0f15` background with `#f8f9f9` headline `1. Your Route`.
3. **Primary Showcase & Content Grid (<section.py-section-lg> — `New Trip`)**:
   - DOM & Selectors: Landmark `<section class="py-section-lg bg-neutral-50">` rendering section `New Trip` with copy *"E E M M P P T T Y Y"*, asset references (`0484562807a97172-s.p.woff2`, `2cc74b96cdc9383d-s.p.woff2`, `36966cca54120369-s.p.woff2`, `427e4a37d3642943-s.p.woff2`), and grid rule `body { margin:0;line-height:inherit }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.py-section-lg> — `New Trip`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1400px`, `gap: .125rem`) on desktop and Single-column vertical stack at `390px` viewport width with `2rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.py-section-lg> — `Summary`)**:
   - DOM & Selectors: Landmark `<section class="py-section-lg bg-neutral-50">` framing `Summary` and `Special Requirements` (*"v v i i l l l l i i e e r r s s O O S S"*) with `#d9d9d9` surface cards, `#1a1a1f` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.py-section-lg> — `Summary`)` uses `.25rem`, `1rem`, `1.5rem`, `11px` radii, `#1a1a1f` highlights, and assets (0484562807a97172-s.p.woff2, 2cc74b96cdc9383d-s.p.woff2, 36966cca54120369-s.p.woff2).
5. **Colophon & Global Directory Footer (<footer.flex> — `https://www.villiers.ai/`)**:
   - DOM & Selectors: Landmark `<footer class="flex flex-col">` anchoring `Private Jet Charter and Empty Le` footer links (`H H O O M M E E · B B L L O O G G · A A B B O O U U T T`), copy *"B B I I T T C C O O I I N N"*, and `#29292b` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.flex> — `https://www.villiers.ai/`)` aligns to `1400px` extracted from `www-villiers-ai` stylesheet with `2rem` lateral canvas padding with `.125rem` grid gap and attributes (data-header-ready="true", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"E E M M P P T T Y Y L L E E G G S S"*
- Copy Excerpt 2: *"E E M M P P T T Y Y"*
- Copy Excerpt 3: *"v v i i l l l l i i e e r r s s O O S S"*
- Copy Excerpt 4: *"B B I I T T C C O O I I N N"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`www-villiers-ai`)**:
- `before { box-sizing:border-box;border:0 solid e5e7eb }`
- `body { margin:0;line-height:inherit }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { font-size:75%;line-height:0;position:relative;vertical-align:baseline }`
- **Per-Selector Transition Rules**:
- **Selector `.transition`**: `transition: cubic-bezier(0,0,.2,1)` extracted from `www-villiers-ai` stylesheet.
- **Selector `sition-\[border-color\2c backgrou...`**: `transition: cubic-bezier(0,0,.2,1)` extracted from `www-villiers-ai` stylesheet.
- **Selector `.transition-\[color\2c transform\]`**: `transition: cubic-bezier(0,0,.2,1)` extracted from `www-villiers-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.fixed>` and `<section.py-section-lg>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-villiers-ai`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
