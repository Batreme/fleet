---
title: "UI Prompt Blueprint: spykercars-com"
date: 2026-11-15
target: "[[overview|spykercars-com]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#0000` accent)"
---

# UI Design System & Master Generation Blueprint: spykercars-com

> **Hand-Built Super Sports Cars Since 1880 · Spyker Cars** (https://spykercars.com/) — Spyker builds highly exclusive, hand-built super sports cars in the Netherlands. Discover the C8 Preliator XXV Coupé and the marque's sto...

![Desktop Viewport Capture (1440x9519)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Hand-Built Super Sports Cars Since 1880 · Spyker Cars** (`https://spykercars.com/`). Spyker builds highly exclusive, hand-built super sports cars in the Netherlands. Discover the C8 Preliator XXV Coupé and the marque's sto...
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#0000` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#0000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `swiss721` for display copy (`The next chapter of Spyker T h e n e`) with `swiss721 Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1023px` container bounds (`gap: 5px`, padding `16px`) with `cubic-bezier(.4,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×9519px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1023px` extracted from `spykercars-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `16px` lateral canvas padding with `5px` grid gap.
- **Border Radius Scale**: `.3125rem`, `.375rem`, `.25rem`, `var(--radius-2xl)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1023px`, `gap: 5px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `16px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width:1023px)`, `@media (min-width:64rem) and (orientation:landscape)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f24822` | `.animated-grid__col { background-color: #f24822 }` |
| **Interactive Accent / Highlight** | `#0000` | `textarea { background-color: #0000 }` |
| **Secondary / Muted Copy** | `#1d1d1b` | `::selection { background-color: #1d1d1b }` |
| **Structural Hairline Border** | `#000000` | `.border-black { border-color: black }` (`#000000`) |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `var(--font-swiss-721),sans-serif` | Typography / Scale Token |
| `--font-mono` | `ui-monospace,SFMono-Regular,monospace` | Typography / Scale Token |
| `--color-red-300` | `oklch(80.8% .114 19.571)` | Brand / Palette Token |
| `--color-red-500` | `oklch(63.7% .237 25.331)` | Brand / Palette Token |
| `--color-red-600` | `oklch(57.7% .245 27.325)` | Brand / Palette Token |
| `--color-red-700` | `oklch(50.5% .213 27.518)` | Brand / Palette Token |
| `--color-cyan-300` | `oklch(86.5% .127 207.078)` | Brand / Palette Token |
| `--color-blue-600` | `oklch(54.6% .245 262.881)` | Brand / Palette Token |
| `--color-gray-400` | `oklch(70.7% .022 261.325)` | Brand / Palette Token |
| `--color-gray-500` | `oklch(55.1% .027 264.364)` | Brand / Palette Token |
| `--color-neutral-50` | `oklch(98.5% 0 none)` | Brand / Palette Token |
| `--color-neutral-100` | `oklch(97% 0 none)` | Brand / Palette Token |
| `--color-neutral-200` | `oklch(92.2% 0 none)` | Brand / Palette Token |
| `--color-neutral-300` | `oklch(87% 0 none)` | Brand / Palette Token |
| `--color-neutral-400` | `oklch(70.8% 0 none)` | Brand / Palette Token |
| `--color-neutral-500` | `oklch(55.6% 0 none)` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `swiss721`.
- **Primary Body Stack**: `swiss721 Fallback`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-5xl: 3rem`.
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 38px`).
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`; rule `p` (`font-size: var(--text-sm)`, `line-height: var(--tw-leading,var(...`).
- **Metadata & Navigation Labels**: CSS variables `--font-mono: ui-monospace,SFMono-Regular,monospace`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.navLink`**: `transition: transform .3s` extracted from `spykercars-com` stylesheet.
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `spykercars-com` stylesheet.
- **Selector `layer theme`**: `transition: .15s` extracted from `spykercars-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<nav.container>` and `<article.sr-only>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Hand-Built Super Sports Cars Since 1880 ·  │
│ ====================================================================== │
│ [ <nav.container>          | Home · Heritage · Boutique · News · Co ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.lenis-autoToggle>                           |   │
│ | H1: The next chapter of Spyker T h e n e x t c h a p...          |   │
│ | Substrate: #000       | Ink: #fff       | Accent: #0000          |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<article.sr-only>         ) max-w: 1023px         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | P u r e P a s s i o n        |  | N u l l a T e n a c i I n v  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 5px   ) | │
│ | [<nav.container>] -> [<section.lenis-aut] -> [<article.sr-only>] |   │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.relative>     ) | https://spykercars.com/            │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.container> — `spykercars-com`)**:
   - Landmark `<nav class="container grid">` hosting `Hand-Built Super Sports Cars Since 1` navigation (`Home · Heritage · Boutique · News · Contact`), DOM attributes (`data-theme="light"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `after { transform:translateY(-2px) }`.
2. **Hero Stage & Focal Lead (<section.lenis-autoToggle> — `The next chapter of Spyker T h e n`)**:
   - Landmark `<section class="lenis-autoToggle">` presenting display lead `The next chapter of Spyker T h e n e x t c h a p...` and copy excerpt *"Skip to main content"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<article.sr-only> — `P u r e P a s s i o n`)**:
   - Landmark `<article class="sr-only">` rendering section `P u r e P a s s i o n` with copy *"C8 Preliator XXV Coupé"*, asset references (`f13a7bda184fa931.css`, `86c130d7567786c0.css`, `3c4afd8b2a3df79a.css`, `cdb4fb19178d4946.css`), and grid rule `.icon--copy { height:1.5384615385rem;width:1.5384615385rem }`.
4. **Interactive Detail & Feature Matrix (<section.w-full> — `N u l l a T e n a c i I n v i a E `)**:
   - Landmark `<section class="w-full relative">` framing `N u l l a T e n a c i I n v i a E s t V i a` and `T h e S p y k e r h e r i t a g e` (*"info@spykercars.com"*) with `#f24822` surface cards, `#0000` accents, and `.icon--copy .stroke { fill:none;stroke:currentColor;stroke-width:1px }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://spykercars.com/`)**:
   - Landmark `<footer class="relative z-30">` anchoring `Hand-Built Super Sports Cars Sin` footer links (`Home · Heritage · Boutique · News · Contact`), copy *"For press contacts:"*, and `#000000` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: spykercars-com (Hand-Built Super Sports Cars Since 1880 · Spyker Cars)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `spykercars-com` (**Hand-Built Super Sports Cars Since 1880 · Spyker Cars** — `https://spykercars.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#0000` accent).
- **Identity & Domain Context**: Spyker builds highly exclusive, hand-built super sports cars in the Netherlands. Discover the C8 Preliator XXV Coupé and the marque's sto...
- **Primary Substrate**: `#000` (`var(--color-black)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#0000`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#0000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `swiss721` for display copy (`The next chapter of Spyker T h e n e`) with `swiss721 Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1023px` container bounds (`gap: 5px`, padding `16px`) with `cubic-bezier(.4,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `spykercars-com` in your global stylesheet:

:root {
  /* Hand-Built Super Sports Cars Since 1880 · Spyker Cars (spykercars-com) — Ground-Truth Extracted CSS Variables */
  --font-sans: var(--font-swiss-721),sans-serif; /* Typography / Scale Token (spykercars-com) */
  --font-mono: ui-monospace,SFMono-Regular,monospace; /* Typography / Scale Token (spykercars-com) */
  --color-red-300: oklch(80.8% .114 19.571); /* Brand / Palette Token (spykercars-com) */
  --color-red-500: oklch(63.7% .237 25.331); /* Brand / Palette Token (spykercars-com) */
  --color-red-600: oklch(57.7% .245 27.325); /* Brand / Palette Token (spykercars-com) */
  --color-red-700: oklch(50.5% .213 27.518); /* Brand / Palette Token (spykercars-com) */
  --color-cyan-300: oklch(86.5% .127 207.078); /* Brand / Palette Token (spykercars-com) */
  --color-blue-600: oklch(54.6% .245 262.881); /* Brand / Palette Token (spykercars-com) */
  --color-gray-400: oklch(70.7% .022 261.325); /* Brand / Palette Token (spykercars-com) */
  --color-gray-500: oklch(55.1% .027 264.364); /* Brand / Palette Token (spykercars-com) */
  --color-neutral-50: oklch(98.5% 0 none); /* Brand / Palette Token (spykercars-com) */
  --color-neutral-100: oklch(97% 0 none); /* Brand / Palette Token (spykercars-com) */
  --color-neutral-200: oklch(92.2% 0 none); /* Brand / Palette Token (spykercars-com) */
  --color-neutral-300: oklch(87% 0 none); /* Brand / Palette Token (spykercars-com) */
  --color-neutral-400: oklch(70.8% 0 none); /* Brand / Palette Token (spykercars-com) */
  --color-neutral-500: oklch(55.6% 0 none); /* Brand / Palette Token (spykercars-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--color-black)` in `:root`
- **Primary Typography Ink**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Elevated Surface / Card Substrate**: `#f24822` — grounded in `.animated-grid__col { background-color: #f24822 }`
- **Interactive Accent / Highlight**: `#0000` — grounded in `textarea { background-color: #0000 }`
- **Secondary / Muted Copy**: `#1d1d1b` — grounded in `::selection { background-color: #1d1d1b }`
- **Structural Hairline Border**: `#000000` — grounded in `.border-black { border-color: black }` (`#000000`)

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×9519px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1023px` extracted from `spykercars-com` stylesheet
- **Padding & Gutters**: `16px` lateral canvas padding with `5px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1023px`, `gap: 5px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `16px` horizontal padding
- **Media Queries**: `@media screen and (max-width:1023px)`, `@media (min-width:64rem) and (orientation:landscape)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`
- **Corner Radii**: `.3125rem`, `.375rem`, `.25rem`, `var(--radius-2xl)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `swiss721`
- **Body Font Stack**: `swiss721 Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-5xl: 3rem`
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 38px`)
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`; rule `p` (`font-size: var(--text-sm)`, `line-height: var(--tw-leading,var(...`)
- **Metadata & Index Rule**: CSS variables `--font-mono: ui-monospace,SFMono-Regular,monospace`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `spykercars-com` (`Hand-Built Super Sports Cars Since 1880 · Spyker Cars`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.container> — `spykercars-com`)**:
   - DOM & Selectors: Landmark `<nav class="container grid">` hosting `Hand-Built Super Sports Cars Since 1` navigation (`Home · Heritage · Boutique · News · Contact`), DOM attributes (`data-theme="light"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `after { transform:translateY(-2px) }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.container> — `spykercars-com`)` (`spykercars-com`) adapts across `@media screen and (max-width:1023px)`, `@media (min-width:64rem) and (orientation:landscape)`, `@media (min-width:40rem)`, `@media (min-width:48rem)` with `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Home · Heritage · Boutique · News · Contact`.
2. **Hero Stage & Focal Lead (<section.lenis-autoToggle> — `The next chapter of Spyker T h e n`)**:
   - DOM & Selectors: Landmark `<section class="lenis-autoToggle">` presenting display lead `The next chapter of Spyker T h e n e x t c h a p...` and copy excerpt *"Skip to main content"* over `#000` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×9519px` desktop / `390×2400px` mobile) sets `#000` background with `#fff` headline `The next chapter of Spyker T h e n e x t c h a p...`.
3. **Primary Showcase & Content Grid (<article.sr-only> — `P u r e P a s s i o n`)**:
   - DOM & Selectors: Landmark `<article class="sr-only">` rendering section `P u r e P a s s i o n` with copy *"C8 Preliator XXV Coupé"*, asset references (`f13a7bda184fa931.css`, `86c130d7567786c0.css`, `3c4afd8b2a3df79a.css`, `cdb4fb19178d4946.css`), and grid rule `.icon--copy { height:1.5384615385rem;width:1.5384615385rem }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<article.sr-only> — `P u r e P a s s i o n`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1023px`, `gap: 5px`) on desktop and Single-column vertical stack at `390px` viewport width with `16px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.w-full> — `N u l l a T e n a c i I n v i a E `)**:
   - DOM & Selectors: Landmark `<section class="w-full relative">` framing `N u l l a T e n a c i I n v i a E s t V i a` and `T h e S p y k e r h e r i t a g e` (*"info@spykercars.com"*) with `#f24822` surface cards, `#0000` accents, and `.icon--copy .stroke { fill:none;stroke:currentColor;stroke-width:1px }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.w-full> — `N u l l a T e n a c i I n v i a E `)` uses `.3125rem`, `.375rem`, `.25rem`, `var(--radius-2xl)` radii, `#0000` highlights, and assets (f13a7bda184fa931.css, 86c130d7567786c0.css, 3c4afd8b2a3df79a.css).
5. **Colophon & Global Directory Footer (<footer.relative> — `https://spykercars.com/`)**:
   - DOM & Selectors: Landmark `<footer class="relative z-30">` anchoring `Hand-Built Super Sports Cars Sin` footer links (`Home · Heritage · Boutique · News · Contact`), copy *"For press contacts:"*, and `#000000` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.relative> — `https://spykercars.com/`)` aligns to `1023px` extracted from `spykercars-com` stylesheet with `16px` lateral canvas padding with `5px` grid gap and attributes (data-theme="light", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Skip to main content"*
- Copy Excerpt 2: *"C8 Preliator XXV Coupé"*
- Copy Excerpt 3: *"info@spykercars.com"*
- Copy Excerpt 4: *"For press contacts:"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`spykercars-com`)**:
- `after { transform:translateY(-2px) }`
- `.icon--copy { height:1.5384615385rem;width:1.5384615385rem }`
- `.icon--copy .stroke { fill:none;stroke:currentColor;stroke-width:1px }`
- `html.lenis body { height:auto }`
- `.lenis-stopped { overflow:clip }`
- **Per-Selector Transition Rules**:
- **Selector `.navLink`**: `transition: transform .3s` extracted from `spykercars-com` stylesheet.
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `spykercars-com` stylesheet.
- **Selector `layer theme`**: `transition: .15s` extracted from `spykercars-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<nav.container>` and `<article.sr-only>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `spykercars-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
