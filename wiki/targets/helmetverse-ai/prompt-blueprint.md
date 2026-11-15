---
title: "UI Prompt Blueprint: helmetverse-ai"
date: 2026-11-15
target: "[[overview|helmetverse-ai]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#5db389` / `#fd853a`)"
---

# UI Design System & Master Generation Blueprint: helmetverse-ai

> **Helmetverse · Design yours** (https://helmetverse.ai/) — Type a prompt. The team rides what you imagine.

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/helmetverse-ai/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Helmetverse · Design yours** (`https://helmetverse.ai/`). Type a prompt. The team rides what you imagine.
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#5db389` / `#fd853a`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#5db389` (`var(--g42-hero-tint)` in `:root`) paired with `#142a1c` primary typography and `#fd853a` accents.
  - **Extracted Typographic Hierarchy**: Pairs `G42 Sans` for display copy (`HELMETVERSE`) with `Space Grotesk` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `375px` container bounds (`gap: var(--spacing-lg)`, padding `var(--spacing-lg)`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/helmetverse-ai/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `375px` extracted from `helmetverse-ai` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--spacing-lg)` lateral canvas padding with `var(--spacing-lg)` grid gap.
- **Border Radius Scale**: `var(--radius-lg)`, `var(--radius-full)`, `.25rem`, `var(--radius-2xl)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 375px`, `gap: var(--spacing-lg)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--spacing-lg)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:375px)`, `@media (min-width:425px)`, `@media (min-width:640px)`, `@media (min-width:768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#5db389` | `var(--g42-hero-tint)` in `:root` |
| **Primary Typography Ink** | `#142a1c` | `var(--g42-hero-tint-dark)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff6ed` | `var(--color-orange-50)` in `:root` |
| **Interactive Accent / Highlight** | `#fd853a` | `var(--color-orange-400)` in `:root` |
| **Secondary / Muted Copy** | `#fb6514` | `var(--color-orange-500)` in `:root` |
| **Structural Hairline Border** | `#3080ff` | `var(--color-blue-500)` in `:root` |
| **Variable Token (`--color-gray-50`)** | `#f9fafb` | `var(--color-gray-50)` in `:root` |
| **Variable Token (`--color-gray-100`)** | `#f2f4f7` | `var(--color-gray-100)` in `:root` |
| **Variable Token (`--color-gray-200`)** | `#e4e7ec` | `var(--color-gray-200)` in `:root` |
| **Variable Token (`--color-gray-300`)** | `#d0d5dd` | `var(--color-gray-300)` in `:root` |
| **Variable Token (`--color-gray-400`)** | `#98a2b3` | `var(--color-gray-400)` in `:root` |
| **Variable Token (`--color-gray-500`)** | `#667085` | `var(--color-gray-500)` in `:root` |
| **Variable Token (`--color-gray-600`)** | `#475467` | `var(--color-gray-600)` in `:root` |
| **Variable Token (`--color-gray-700`)** | `#344054` | `var(--color-gray-700)` in `:root` |
| **Variable Token (`--color-gray-800`)** | `#1d2939` | `var(--color-gray-800)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--g42-hero-tint` | `#5db389` | Canvas / Surface Token |
| `--g42-hero-tint-dark` | `#142a1c` | Canvas / Surface Token |
| `--font-sans` | `"G42 Sans", "Space Grotesk", sans-serif` | Typography / Scale Token |
| `--color-orange-50` | `#fff6ed` | Brand / Palette Token |
| `--color-orange-400` | `#fd853a` | Brand / Palette Token |
| `--color-orange-500` | `#fb6514` | Brand / Palette Token |
| `--color-blue-500` | `#3080ff` | Brand / Palette Token |
| `--color-gray-50` | `#f9fafb` | Brand / Palette Token |
| `--color-gray-100` | `#f2f4f7` | Brand / Palette Token |
| `--color-gray-200` | `#e4e7ec` | Brand / Palette Token |
| `--color-gray-300` | `#d0d5dd` | Brand / Palette Token |
| `--color-gray-400` | `#98a2b3` | Brand / Palette Token |
| `--color-gray-500` | `#667085` | Brand / Palette Token |
| `--color-gray-600` | `#475467` | Brand / Palette Token |
| `--color-gray-700` | `#344054` | Brand / Palette Token |
| `--color-gray-800` | `#1d2939` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `G42 Sans`.
- **Primary Body Stack**: `Space Grotesk`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-display: 60px`, `--text-h1: 48px`.
- **Section Heading (`H2`)**: CSS variables `--text-h2: 36px`; rule `h2` (`font-size: 15px`, `line-height: 1.3`, `letter-spacing: .02em`, `font-weight: 900`).
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`, `--text-body-lg: 18px`.
- **Metadata & Navigation Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.2,.8,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `helmetverse-ai` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `helmetverse-ai` stylesheet.
- **Selector `color\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `helmetverse-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<nav.jsx-25f90e9ce2076406>` and `<main.relative>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Helmetverse · Design yours                 │
│ ====================================================================== │
│ [ <nav.jsx-25f90e9ce207640 | Home · Gallery · AI Studio · Leaderboa ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.relative>                                      |   │
│ | H1: HELMETVERSE                                                  |   │
│ | Substrate: #5db389    | Ink: #142a1c    | Accent: #fd853a        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.relative>           ) max-w: 375px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | DESIGN WITHOUT LIMITS        |  | A GLOBAL COMPETITION FOR THE | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<nav.jsx-25f90e9ce] -> [<main.relative>] -> [<main.relative>] |     │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.text-text-prim) | https://helmetverse.ai/            │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.jsx-25f90e9ce2076406> — `helmetverse-ai`)**:
   - Landmark `<nav class="jsx-25f90e9ce2076406 overflow-hidden">` hosting `Helmetverse · Design yours` navigation (`Home · Gallery · AI Studio · Leaderboard · About`), DOM attributes (`data-paper-shader`, `data-precedence="next"`, `data-precedence="next"`, `data-styled-jsx`), and stylesheet rule `host { --color-blue-500:lab(54.1736% 13.3369 -74.6839) }`.
2. **Hero Stage & Focal Lead (<main.relative> — `HELMETVERSE`)**:
   - Landmark `<main class="relative bg-bg-dark">` presenting display lead `HELMETVERSE` and copy excerpt *"H E L M E T V E R S E"* over `#5db389` canvas and `#142a1c` ink.
3. **Primary Showcase & Content Grid (<main.relative> — `DESIGN WITHOUT LIMITS`)**:
   - Landmark `<main class="relative bg-bg-dark">` rendering section `DESIGN WITHOUT LIMITS` with copy *"Win a trip to Abu Dhabi"*, asset references (`6577f91f-ad74-4868-93e8-13027534a...`, `79d7fc46-0103-4a7f-b9f7-d1012c6fa...`, `98da8316-c3f4-4946-adb6-727aa17a0...`, `b241f184-7659-4fb4-bdb4-cdf53d1fc...`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<main.relative> — `A GLOBAL COMPETITION FOR THE MOST `)**:
   - Landmark `<main class="relative bg-bg-dark">` framing `A GLOBAL COMPETITION FOR THE MOST CREATIVE MINDS` and `FEATURED HELMET DESIGNS` (*"THE DESIGNS ARE IN. NOW YOU DECIDE WHO WINS."*) with `#fff6ed` surface cards, `#fd853a` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.text-text-primary-dark> — `https://helmetverse.ai/`)**:
   - Landmark `<footer class="text-text-primary-dark">` anchoring `Helmetverse · Design yours` footer links (`Home · Gallery · AI Studio · Leaderboard · About`), copy *"Submissions and voting are officially closed. Explore this y"*, and `#3080ff` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: helmetverse-ai (Helmetverse · Design yours)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `helmetverse-ai` (**Helmetverse · Design yours** — `https://helmetverse.ai/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#5db389` / `#fd853a`).
- **Identity & Domain Context**: Type a prompt. The team rides what you imagine.
- **Primary Substrate**: `#5db389` (`var(--g42-hero-tint)` in `:root`), **Primary Ink**: `#142a1c`, **Accent / Highlight**: `#fd853a`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#5db389` (`var(--g42-hero-tint)` in `:root`) paired with `#142a1c` primary typography and `#fd853a` accents.
  - **Extracted Typographic Hierarchy**: Pairs `G42 Sans` for display copy (`HELMETVERSE`) with `Space Grotesk` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `375px` container bounds (`gap: var(--spacing-lg)`, padding `var(--spacing-lg)`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `helmetverse-ai` in your global stylesheet:

:root {
  /* Helmetverse · Design yours (helmetverse-ai) — Ground-Truth Extracted CSS Variables */
  --g42-hero-tint: #5db389; /* Canvas / Surface Token (helmetverse-ai) */
  --g42-hero-tint-dark: #142a1c; /* Canvas / Surface Token (helmetverse-ai) */
  --font-sans: "G42 Sans", "Space Grotesk", sans-serif; /* Typography / Scale Token (helmetverse-ai) */
  --color-orange-50: #fff6ed; /* Brand / Palette Token (helmetverse-ai) */
  --color-orange-400: #fd853a; /* Brand / Palette Token (helmetverse-ai) */
  --color-orange-500: #fb6514; /* Brand / Palette Token (helmetverse-ai) */
  --color-blue-500: #3080ff; /* Brand / Palette Token (helmetverse-ai) */
  --color-gray-50: #f9fafb; /* Brand / Palette Token (helmetverse-ai) */
  --color-gray-100: #f2f4f7; /* Brand / Palette Token (helmetverse-ai) */
  --color-gray-200: #e4e7ec; /* Brand / Palette Token (helmetverse-ai) */
  --color-gray-300: #d0d5dd; /* Brand / Palette Token (helmetverse-ai) */
  --color-gray-400: #98a2b3; /* Brand / Palette Token (helmetverse-ai) */
  --color-gray-500: #667085; /* Brand / Palette Token (helmetverse-ai) */
  --color-gray-600: #475467; /* Brand / Palette Token (helmetverse-ai) */
  --color-gray-700: #344054; /* Brand / Palette Token (helmetverse-ai) */
  --color-gray-800: #1d2939; /* Brand / Palette Token (helmetverse-ai) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#5db389` — grounded in `var(--g42-hero-tint)` in `:root`
- **Primary Typography Ink**: `#142a1c` — grounded in `var(--g42-hero-tint-dark)` in `:root`
- **Elevated Surface / Card Substrate**: `#fff6ed` — grounded in `var(--color-orange-50)` in `:root`
- **Interactive Accent / Highlight**: `#fd853a` — grounded in `var(--color-orange-400)` in `:root`
- **Secondary / Muted Copy**: `#fb6514` — grounded in `var(--color-orange-500)` in `:root`
- **Structural Hairline Border**: `#3080ff` — grounded in `var(--color-blue-500)` in `:root`
- **Variable Token (`--color-gray-50`)**: `#f9fafb` — grounded in `var(--color-gray-50)` in `:root`
- **Variable Token (`--color-gray-100`)**: `#f2f4f7` — grounded in `var(--color-gray-100)` in `:root`
- **Variable Token (`--color-gray-200`)**: `#e4e7ec` — grounded in `var(--color-gray-200)` in `:root`
- **Variable Token (`--color-gray-300`)**: `#d0d5dd` — grounded in `var(--color-gray-300)` in `:root`
- **Variable Token (`--color-gray-400`)**: `#98a2b3` — grounded in `var(--color-gray-400)` in `:root`
- **Variable Token (`--color-gray-500`)**: `#667085` — grounded in `var(--color-gray-500)` in `:root`
- **Variable Token (`--color-gray-600`)**: `#475467` — grounded in `var(--color-gray-600)` in `:root`
- **Variable Token (`--color-gray-700`)**: `#344054` — grounded in `var(--color-gray-700)` in `:root`
- **Variable Token (`--color-gray-800`)**: `#1d2939` — grounded in `var(--color-gray-800)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `375px` extracted from `helmetverse-ai` stylesheet
- **Padding & Gutters**: `var(--spacing-lg)` lateral canvas padding with `var(--spacing-lg)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 375px`, `gap: var(--spacing-lg)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--spacing-lg)` horizontal padding
- **Media Queries**: `@media (min-width:375px)`, `@media (min-width:425px)`, `@media (min-width:640px)`, `@media (min-width:768px)`
- **Corner Radii**: `var(--radius-lg)`, `var(--radius-full)`, `.25rem`, `var(--radius-2xl)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `G42 Sans`
- **Body Font Stack**: `Space Grotesk`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: CSS variables `--text-display: 60px`, `--text-h1: 48px`
- **H2 Section Rule**: CSS variables `--text-h2: 36px`; rule `h2` (`font-size: 15px`, `line-height: 1.3`, `letter-spacing: .02em`, `font-weight: 900`)
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`, `--text-body-lg: 18px`
- **Metadata & Index Rule**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `helmetverse-ai` (`Helmetverse · Design yours`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.jsx-25f90e9ce2076406> — `helmetverse-ai`)**:
   - DOM & Selectors: Landmark `<nav class="jsx-25f90e9ce2076406 overflow-hidden">` hosting `Helmetverse · Design yours` navigation (`Home · Gallery · AI Studio · Leaderboard · About`), DOM attributes (`data-paper-shader`, `data-precedence="next"`, `data-precedence="next"`, `data-styled-jsx`), and stylesheet rule `host { --color-blue-500:lab(54.1736% 13.3369 -74.6839) }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.jsx-25f90e9ce2076406> — `helmetverse-ai`)` (`helmetverse-ai`) adapts across `@media (min-width:375px)`, `@media (min-width:425px)`, `@media (min-width:640px)`, `@media (min-width:768px)` with `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.2,.8,.2,1)` transitions and links `Home · Gallery · AI Studio · Leaderboard · About`.
2. **Hero Stage & Focal Lead (<main.relative> — `HELMETVERSE`)**:
   - DOM & Selectors: Landmark `<main class="relative bg-bg-dark">` presenting display lead `HELMETVERSE` and copy excerpt *"H E L M E T V E R S E"* over `#5db389` canvas and `#142a1c` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#5db389` background with `#142a1c` headline `HELMETVERSE`.
3. **Primary Showcase & Content Grid (<main.relative> — `DESIGN WITHOUT LIMITS`)**:
   - DOM & Selectors: Landmark `<main class="relative bg-bg-dark">` rendering section `DESIGN WITHOUT LIMITS` with copy *"Win a trip to Abu Dhabi"*, asset references (`6577f91f-ad74-4868-93e8-13027534a...`, `79d7fc46-0103-4a7f-b9f7-d1012c6fa...`, `98da8316-c3f4-4946-adb6-727aa17a0...`, `b241f184-7659-4fb4-bdb4-cdf53d1fc...`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.relative> — `DESIGN WITHOUT LIMITS`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 375px`, `gap: var(--spacing-lg)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--spacing-lg)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.relative> — `A GLOBAL COMPETITION FOR THE MOST `)**:
   - DOM & Selectors: Landmark `<main class="relative bg-bg-dark">` framing `A GLOBAL COMPETITION FOR THE MOST CREATIVE MINDS` and `FEATURED HELMET DESIGNS` (*"THE DESIGNS ARE IN. NOW YOU DECIDE WHO WINS."*) with `#fff6ed` surface cards, `#fd853a` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.relative> — `A GLOBAL COMPETITION FOR THE MOST `)` uses `var(--radius-lg)`, `var(--radius-full)`, `.25rem`, `var(--radius-2xl)` radii, `#fd853a` highlights, and assets (6577f91f-ad74-4868-93e8-13027534a..., 79d7fc46-0103-4a7f-b9f7-d1012c6fa..., 98da8316-c3f4-4946-adb6-727aa17a0...).
5. **Colophon & Global Directory Footer (<footer.text-text-primary-dark> — `https://helmetverse.ai/`)**:
   - DOM & Selectors: Landmark `<footer class="text-text-primary-dark">` anchoring `Helmetverse · Design yours` footer links (`Home · Gallery · AI Studio · Leaderboard · About`), copy *"Submissions and voting are officially closed. Explore this y"*, and `#3080ff` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.text-text-primary-dark> — `https://helmetverse.ai/`)` aligns to `375px` extracted from `helmetverse-ai` stylesheet with `var(--spacing-lg)` lateral canvas padding with `var(--spacing-lg)` grid gap and attributes (data-paper-shader, data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"H E L M E T V E R S E"*
- Copy Excerpt 2: *"Win a trip to Abu Dhabi"*
- Copy Excerpt 3: *"THE DESIGNS ARE IN. NOW YOU DECIDE WHO WINS."*
- Copy Excerpt 4: *"Submissions and voting are officially closed. Explore this year’s helmet designs."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.2,.8,.2,1)`
- **Extracted Stylesheet Rules (`helmetverse-ai`)**:
- `host { --color-blue-500:lab(54.1736% 13.3369 -74.6839) }`
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `helmetverse-ai` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `helmetverse-ai` stylesheet.
- **Selector `color\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `helmetverse-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<nav.jsx-25f90e9ce2076406>` and `<main.relative>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `helmetverse-ai`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
