---
title: "UI Prompt Blueprint: exspeedia-com"
date: 2026-11-15
target: "exspeedia-com"
status: analyzed
capture: dom
capture_desktop: dom
capture_mobile: dom
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#fbf8e6` / `#fae26a`)"
---

# UI Design System & Master Generation Blueprint: exspeedia-com

> **Official IShowSpeed Travel Site Powered by Expedia** (https://exspeedia.com) — The official IShowSpeed travel website powered by Expedia. Book trips inspired by Speed’s real travels, enter sweepstakes, and earn rewards.

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Official IShowSpeed Travel Site Powered by Expedia** (`https://exspeedia.com`). The official IShowSpeed travel website powered by Expedia. Book trips inspired by Speed’s real travels, enter sweepstakes, and earn rewards.
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#fbf8e6` / `#fae26a`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fbf8e6` (`var(--color-yellow-50)` in `:root`) paired with `#ffd60a` primary typography and `#fae26a` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Centra No2` for display copy (`Go places like`) with `Segoe UI` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--spacing)`, padding `var(--spacing)`) with `cubic-bezier(.4,0,1,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40rem` extracted from `exspeedia-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--spacing)` lateral canvas padding with `var(--spacing)` grid gap.
- **Border Radius Scale**: `.25rem`, `var(--radius-2xl)`, `4px`, `2147483647px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--spacing)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (width>=40rem)`, `@media (width>=48rem)`, `@media (width>=64rem)`, `@media (width>=80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fbf8e6` | `var(--color-yellow-50)` in `:root` |
| **Primary Typography Ink** | `#f9f2cf` | `var(--color-yellow-100)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f8e99e` | `var(--color-yellow-200)` in `:root` |
| **Interactive Accent / Highlight** | `#fae26a` | `var(--color-yellow-300)` in `:root` |
| **Secondary / Muted Copy** | `#fddb32` | `var(--color-yellow-400)` in `:root` |
| **Structural Hairline Border** | `#ffd60a` | `var(--color-yellow-500)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-serif` | `ui-serif, Georgia, Cambria, "Times New Roman", Times, serif` | Typography / Scale Token |
| `--color-red-50` | `oklch(97.1% .013 17.38)` | Brand / Palette Token |
| `--color-red-100` | `oklch(93.6% .032 17.717)` | Brand / Palette Token |
| `--color-red-200` | `oklch(88.5% .062 18.334)` | Brand / Palette Token |
| `--color-red-300` | `oklch(80.8% .114 19.571)` | Brand / Palette Token |
| `--color-red-400` | `oklch(70.4% .191 22.216)` | Brand / Palette Token |
| `--color-red-500` | `oklch(63.7% .237 25.331)` | Brand / Palette Token |
| `--color-red-600` | `oklch(57.7% .245 27.325)` | Brand / Palette Token |
| `--color-red-700` | `oklch(50.5% .213 27.518)` | Brand / Palette Token |
| `--color-red-800` | `oklch(44.4% .177 26.899)` | Brand / Palette Token |
| `--color-red-900` | `oklch(39.6% .141 25.723)` | Brand / Palette Token |
| `--color-red-950` | `oklch(25.8% .092 26.042)` | Brand / Palette Token |
| `--color-orange-50` | `oklch(98% .016 73.684)` | Brand / Palette Token |
| `--color-orange-100` | `oklch(95.4% .038 75.164)` | Brand / Palette Token |
| `--color-orange-200` | `oklch(90.1% .076 70.697)` | Brand / Palette Token |
| `--color-orange-300` | `oklch(83.7% .128 66.29)` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Centra No2`.
- **Primary Body Stack**: `Segoe UI`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`; rule `h1` (`font-size: 1.5rem`, `line-height: 1.2`).
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 1.5rem`, `line-height: 1.25`).
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: .75em`).
- **Metadata & Navigation Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `exspeedia-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `exspeedia-com` stylesheet.
- **Selector `.transition-all`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `exspeedia-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.grid>` and `<section.ot-hide>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Official IShowSpeed Travel Site Powered by │
│ ====================================================================== │
│ [ <header.grid>            | More information                       ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.ot-sdk-row>                                 |   │
│ | H1: Go places like                                               |   │
│ | Substrate: #fbf8e6    | Ink: #ffd60a    | Accent: #fae26a        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.ot-hide>         ) max-w: 40rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Privacy Preference Center    |  | Manage Consent Preferences   | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.grid>] -> [<section.ot-sdk-ro] -> [<section.ot-hide>] |     │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.inset-0>      ) | https://exspeedia.com              │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.grid> — `exspeedia-com`)**:
   - Landmark `<header class="grid">` hosting `Official IShowSpeed Travel Site Powe` navigation (`More information`), DOM attributes (`data-navigate-track="reload"`, `data-document-language="true"`, `data-domain-script="019d9c05-c22b-757a-b8..."`, `data-v-app`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.ot-sdk-row> — `Go places like`)**:
   - Landmark `<section class="ot-sdk-row ot-cat-grp">` presenting display lead `Go places like` and copy excerpt *"Accept All Cookies"* over `#fbf8e6` canvas and `#ffd60a` ink.
3. **Primary Showcase & Content Grid (<section.ot-hide> — `Privacy Preference Center`)**:
   - Landmark `<section class="ot-hide ot-pc-scrollbar">` rendering section `Privacy Preference Center` with copy *"checkbox label label"*, asset references (`speed-cdn.expedia.com`, `d2848tzd1fqvrv.cloudfront.net`, `cdn.usefathom.com`, `favicon-96x96.png`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.fixed> — `Manage Consent Preferences`)**:
   - Landmark `<section class="fixed">` framing `Manage Consent Preferences` and `Cookie List` (*"Confirm My Choices"*) with `#f8e99e` surface cards, `#fae26a` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.inset-0> — `https://exspeedia.com`)**:
   - Landmark `<footer class="inset-0">` anchoring `Official IShowSpeed Travel Site ` footer links (`More information`), copy *"Manage Consent Preferences"*, and `#ffd60a` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: exspeedia-com (Official IShowSpeed Travel Site Powered by Expedia)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `exspeedia-com` (**Official IShowSpeed Travel Site Powered by Expedia** — `https://exspeedia.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fbf8e6` / `#fae26a`).
- **Identity & Domain Context**: The official IShowSpeed travel website powered by Expedia. Book trips inspired by Speed’s real travels, enter sweepstakes, and earn rewards.
- **Primary Substrate**: `#fbf8e6` (`var(--color-yellow-50)` in `:root`), **Primary Ink**: `#ffd60a`, **Accent / Highlight**: `#fae26a`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fbf8e6` (`var(--color-yellow-50)` in `:root`) paired with `#ffd60a` primary typography and `#fae26a` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Centra No2` for display copy (`Go places like`) with `Segoe UI` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--spacing)`, padding `var(--spacing)`) with `cubic-bezier(.4,0,1,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `exspeedia-com` in your global stylesheet:

:root {
  /* Official IShowSpeed Travel Site Powered by Expedia (exspeedia-com) — Ground-Truth Extracted CSS Variables */
  --font-serif: ui-serif, Georgia, Cambria, "Times New Roman", Times, serif; /* Typography / Scale Token (exspeedia-com) */
  --color-red-50: oklch(97.1% .013 17.38); /* Brand / Palette Token (exspeedia-com) */
  --color-red-100: oklch(93.6% .032 17.717); /* Brand / Palette Token (exspeedia-com) */
  --color-red-200: oklch(88.5% .062 18.334); /* Brand / Palette Token (exspeedia-com) */
  --color-red-300: oklch(80.8% .114 19.571); /* Brand / Palette Token (exspeedia-com) */
  --color-red-400: oklch(70.4% .191 22.216); /* Brand / Palette Token (exspeedia-com) */
  --color-red-500: oklch(63.7% .237 25.331); /* Brand / Palette Token (exspeedia-com) */
  --color-red-600: oklch(57.7% .245 27.325); /* Brand / Palette Token (exspeedia-com) */
  --color-red-700: oklch(50.5% .213 27.518); /* Brand / Palette Token (exspeedia-com) */
  --color-red-800: oklch(44.4% .177 26.899); /* Brand / Palette Token (exspeedia-com) */
  --color-red-900: oklch(39.6% .141 25.723); /* Brand / Palette Token (exspeedia-com) */
  --color-red-950: oklch(25.8% .092 26.042); /* Brand / Palette Token (exspeedia-com) */
  --color-orange-50: oklch(98% .016 73.684); /* Brand / Palette Token (exspeedia-com) */
  --color-orange-100: oklch(95.4% .038 75.164); /* Brand / Palette Token (exspeedia-com) */
  --color-orange-200: oklch(90.1% .076 70.697); /* Brand / Palette Token (exspeedia-com) */
  --color-orange-300: oklch(83.7% .128 66.29); /* Brand / Palette Token (exspeedia-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fbf8e6` — grounded in `var(--color-yellow-50)` in `:root`
- **Primary Typography Ink**: `#f9f2cf` — grounded in `var(--color-yellow-100)` in `:root`
- **Elevated Surface / Card Substrate**: `#f8e99e` — grounded in `var(--color-yellow-200)` in `:root`
- **Interactive Accent / Highlight**: `#fae26a` — grounded in `var(--color-yellow-300)` in `:root`
- **Secondary / Muted Copy**: `#fddb32` — grounded in `var(--color-yellow-400)` in `:root`
- **Structural Hairline Border**: `#ffd60a` — grounded in `var(--color-yellow-500)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40rem` extracted from `exspeedia-com` stylesheet
- **Padding & Gutters**: `var(--spacing)` lateral canvas padding with `var(--spacing)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--spacing)` horizontal padding
- **Media Queries**: `@media (width>=40rem)`, `@media (width>=48rem)`, `@media (width>=64rem)`, `@media (width>=80rem)`
- **Corner Radii**: `.25rem`, `var(--radius-2xl)`, `4px`, `2147483647px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Centra No2`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`; rule `h1` (`font-size: 1.5rem`, `line-height: 1.2`)
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 1.5rem`, `line-height: 1.25`)
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: .75em`)
- **Metadata & Index Rule**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `exspeedia-com` (`Official IShowSpeed Travel Site Powered by Expedia`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.grid> — `exspeedia-com`)**:
   - DOM & Selectors: Landmark `<header class="grid">` hosting `Official IShowSpeed Travel Site Powe` navigation (`More information`), DOM attributes (`data-navigate-track="reload"`, `data-document-language="true"`, `data-domain-script="019d9c05-c22b-757a-b8..."`, `data-v-app`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.grid> — `exspeedia-com`)` (`exspeedia-com`) adapts across `@media (width>=40rem)`, `@media (width>=48rem)`, `@media (width>=64rem)`, `@media (width>=80rem)` with `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `More information`.
2. **Hero Stage & Focal Lead (<section.ot-sdk-row> — `Go places like`)**:
   - DOM & Selectors: Landmark `<section class="ot-sdk-row ot-cat-grp">` presenting display lead `Go places like` and copy excerpt *"Accept All Cookies"* over `#fbf8e6` canvas and `#ffd60a` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#fbf8e6` background with `#ffd60a` headline `Go places like`.
3. **Primary Showcase & Content Grid (<section.ot-hide> — `Privacy Preference Center`)**:
   - DOM & Selectors: Landmark `<section class="ot-hide ot-pc-scrollbar">` rendering section `Privacy Preference Center` with copy *"checkbox label label"*, asset references (`speed-cdn.expedia.com`, `d2848tzd1fqvrv.cloudfront.net`, `cdn.usefathom.com`, `favicon-96x96.png`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.ot-hide> — `Privacy Preference Center`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--spacing)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.fixed> — `Manage Consent Preferences`)**:
   - DOM & Selectors: Landmark `<section class="fixed">` framing `Manage Consent Preferences` and `Cookie List` (*"Confirm My Choices"*) with `#f8e99e` surface cards, `#fae26a` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.fixed> — `Manage Consent Preferences`)` uses `.25rem`, `var(--radius-2xl)`, `4px`, `2147483647px` radii, `#fae26a` highlights, and assets (speed-cdn.expedia.com, d2848tzd1fqvrv.cloudfront.net, cdn.usefathom.com).
5. **Colophon & Global Directory Footer (<footer.inset-0> — `https://exspeedia.com`)**:
   - DOM & Selectors: Landmark `<footer class="inset-0">` anchoring `Official IShowSpeed Travel Site ` footer links (`More information`), copy *"Manage Consent Preferences"*, and `#ffd60a` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.inset-0> — `https://exspeedia.com`)` aligns to `40rem` extracted from `exspeedia-com` stylesheet with `var(--spacing)` lateral canvas padding with `var(--spacing)` grid gap and attributes (data-navigate-track="reload", data-document-language="true", data-domain-script="019d9c05-c22b-757a-b8...").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Accept All Cookies"*
- Copy Excerpt 2: *"checkbox label label"*
- Copy Excerpt 3: *"Confirm My Choices"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`exspeedia-com`)**:
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { vertical-align:baseline;font-size:75%;line-height:0;position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `exspeedia-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `exspeedia-com` stylesheet.
- **Selector `.transition-all`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `exspeedia-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.grid>` and `<section.ot-hide>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `exspeedia-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
