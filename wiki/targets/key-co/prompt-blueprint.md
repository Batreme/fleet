---
title: "UI Prompt Blueprint: key-co"
date: 2026-11-15
target: "[[overview|key-co]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#808080` accent)"
---

# UI Design System & Master Generation Blueprint: key-co

> **KEY.co · Luxury Vacation Home Rentals + Concierge Services** (https://key.co/) — Find your perfect getaway with KEY.co. Explore curated vacation homes with in-home services like pre-arrival groceries and private chefs.

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/key-co/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **KEY.co · Luxury Vacation Home Rentals + Concierge Services** (`https://key.co/`). Find your perfect getaway with KEY.co. Explore curated vacation homes with in-home services like pre-arrival groceries and private chefs.
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#808080` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#808080` accents.
  - **Extracted Typographic Hierarchy**: Pairs `adobe-caslon-pro` for display copy (`Pack your bags, we’ll do the rest`) with `proxima-nova` and `GeistMono`.
  - **Calibrated Spatial Grid & Motion**: Combines `767px` container bounds (`gap: 6px`, padding `15px`) with `cubic-bezier(0,0,.2,1)` easing and GSAP Timeline & ScrollTrigger, Barba.js Page Transition Router.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/key-co/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `767px` extracted from `key-co` stylesheet.
- **Canvas Lateral Padding & Spacing**: `15px` lateral canvas padding with `6px` grid gap.
- **Border Radius Scale**: `var(--radius)`, `.3125rem`, `.375rem`, `.25rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 767px`, `gap: 6px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `15px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:64rem)`, `@media (max-width:767px)`, `@media (min-width:768px)`, `@media (min-width:40rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0000` | `textarea { background-color: #0000 }` |
| **Interactive Accent / Highlight** | `#808080` | `:before { border-color: gray }` (`#808080`) |
| **Secondary / Muted Copy** | `#ffffff` | `.left-b:before { background-color: white }` (`#ffffff`) |
| **Structural Hairline Border** | `#ce0070` | `.payload-richtext a { color: #ce0070 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-red-50` | `oklch(97.1% .013 17.38)` | Brand / Palette Token |
| `--color-red-100` | `oklch(93.6% .032 17.717)` | Brand / Palette Token |
| `--color-red-200` | `oklch(88.5% .062 18.334)` | Brand / Palette Token |
| `--color-red-400` | `oklch(70.4% .191 22.216)` | Brand / Palette Token |
| `--color-red-500` | `oklch(63.7% .237 25.331)` | Brand / Palette Token |
| `--color-red-600` | `oklch(57.7% .245 27.325)` | Brand / Palette Token |
| `--color-red-700` | `oklch(50.5% .213 27.518)` | Brand / Palette Token |
| `--color-red-800` | `oklch(44.4% .177 26.899)` | Brand / Palette Token |
| `--color-orange-100` | `oklch(95.4% .038 75.164)` | Brand / Palette Token |
| `--color-orange-600` | `oklch(64.6% .222 41.116)` | Brand / Palette Token |
| `--color-green-100` | `oklch(96.2% .044 156.743)` | Brand / Palette Token |
| `--color-green-600` | `oklch(62.7% .194 149.214)` | Brand / Palette Token |
| `--color-blue-50` | `oklch(97% .014 254.604)` | Brand / Palette Token |
| `--color-blue-100` | `oklch(93.2% .032 255.585)` | Brand / Palette Token |
| `--color-blue-500` | `oklch(62.3% .214 259.815)` | Brand / Palette Token |
| `--color-blue-600` | `oklch(54.6% .245 262.881)` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `adobe-caslon-pro`.
- **Primary Body Stack**: `proxima-nova`.
- **Technical / Metadata Stack**: `GeistMono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-5xl: 3rem`.
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`; rule `,h2` (`font-weight: var(--font-we...`).
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`; rule `p` (`font-size: var(--text-sm)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: .28px`, `font-weight: var(--font-we...`).
- **Metadata & Navigation Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`, `--text-sm: .875rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `key-co` stylesheet.
- **Selector `.navbar-hovered`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `key-co` stylesheet.
- **Selector `.navbar-hovered .navbar-logo img`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `key-co` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<nav.relative>` and `<article.wf-proximanova-n5-active>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — KEY.co · Luxury Vacation Home Rentals + Co │
│ ====================================================================== │
│ [ <nav.relative>           | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.navbar-section>                             |   │
│ | H1: Pack your bags, we’ll do the rest                            |   │
│ | Substrate: #000       | Ink: #fff       | Accent: #808080        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<article.wf-proximanova-n5) max-w: 767px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Homes that inspire           |  | Elegant Escape               | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 6px   ) | │
│ | [<nav.relative>] -> [<section.navbar-se] -> [<article.wf-proxim] |   │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.bg-brand-beige) | https://key.co/                    │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.relative> — `key-co`)**:
   - Landmark `<nav class="relative flex">` hosting `KEY.co · Luxury Vacation Home Rental` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-theme="light"`), and stylesheet rule `.icon--copy { height:1.5384615385rem;width:1.5384615385rem }`.
2. **Hero Stage & Focal Lead (<section.navbar-section> — `Pack your bags, we’ll do the rest`)**:
   - Landmark `<section class="navbar-section">` presenting display lead `Pack your bags, we’ll do the rest` and copy excerpt *"$500 off $10k+ stays w/ HOLIDAYSAREHERE - ends 12/31"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<article.wf-proximanova-n5-active> — `Homes that inspire`)**:
   - Landmark `<article class="wf-proximanova-n5-active">` rendering section `Homes that inspire` with copy *"Curated Vacation Homes + Luxury Services"*, asset references (`oaiq.min.js`, `283498678855975`, `fbevents.js`, `gtm.js`), and grid rule `.icon--copy .stroke { fill:none;stroke:currentColor;stroke-width:1px }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Elegant Escape`)**:
   - Landmark `<section class="relative video-fit">` framing `Elegant Escape` and `Galloping Goose Chalet` (*"Search destination"*) with `#0000` surface cards, `#808080` accents, and `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.bg-brand-beige> — `https://key.co/`)**:
   - Landmark `<footer class="bg-brand-beige">` anchoring `KEY.co · Luxury Vacation Home Re` footer links (`Overview · Index · Archive · About · Contact`), copy *"Explore our selection of premium homes—each chosen for style"*, and `#ce0070` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: key-co (KEY.co · Luxury Vacation Home Rentals + Concierge Services)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `key-co` (**KEY.co · Luxury Vacation Home Rentals + Concierge Services** — `https://key.co/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#808080` accent).
- **Identity & Domain Context**: Find your perfect getaway with KEY.co. Explore curated vacation homes with in-home services like pre-arrival groceries and private chefs.
- **Primary Substrate**: `#000` (`var(--color-black)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#808080`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#808080` accents.
  - **Extracted Typographic Hierarchy**: Pairs `adobe-caslon-pro` for display copy (`Pack your bags, we’ll do the rest`) with `proxima-nova` and `GeistMono`.
  - **Calibrated Spatial Grid & Motion**: Combines `767px` container bounds (`gap: 6px`, padding `15px`) with `cubic-bezier(0,0,.2,1)` easing and GSAP Timeline & ScrollTrigger, Barba.js Page Transition Router.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `key-co` in your global stylesheet:

:root {
  /* KEY.co · Luxury Vacation Home Rentals + Concierge Services (key-co) — Ground-Truth Extracted CSS Variables */
  --color-red-50: oklch(97.1% .013 17.38); /* Brand / Palette Token (key-co) */
  --color-red-100: oklch(93.6% .032 17.717); /* Brand / Palette Token (key-co) */
  --color-red-200: oklch(88.5% .062 18.334); /* Brand / Palette Token (key-co) */
  --color-red-400: oklch(70.4% .191 22.216); /* Brand / Palette Token (key-co) */
  --color-red-500: oklch(63.7% .237 25.331); /* Brand / Palette Token (key-co) */
  --color-red-600: oklch(57.7% .245 27.325); /* Brand / Palette Token (key-co) */
  --color-red-700: oklch(50.5% .213 27.518); /* Brand / Palette Token (key-co) */
  --color-red-800: oklch(44.4% .177 26.899); /* Brand / Palette Token (key-co) */
  --color-orange-100: oklch(95.4% .038 75.164); /* Brand / Palette Token (key-co) */
  --color-orange-600: oklch(64.6% .222 41.116); /* Brand / Palette Token (key-co) */
  --color-green-100: oklch(96.2% .044 156.743); /* Brand / Palette Token (key-co) */
  --color-green-600: oklch(62.7% .194 149.214); /* Brand / Palette Token (key-co) */
  --color-blue-50: oklch(97% .014 254.604); /* Brand / Palette Token (key-co) */
  --color-blue-100: oklch(93.2% .032 255.585); /* Brand / Palette Token (key-co) */
  --color-blue-500: oklch(62.3% .214 259.815); /* Brand / Palette Token (key-co) */
  --color-blue-600: oklch(54.6% .245 262.881); /* Brand / Palette Token (key-co) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--color-black)` in `:root`
- **Primary Typography Ink**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Elevated Surface / Card Substrate**: `#0000` — grounded in `textarea { background-color: #0000 }`
- **Interactive Accent / Highlight**: `#808080` — grounded in `:before { border-color: gray }` (`#808080`)
- **Secondary / Muted Copy**: `#ffffff` — grounded in `.left-b:before { background-color: white }` (`#ffffff`)
- **Structural Hairline Border**: `#ce0070` — grounded in `.payload-richtext a { color: #ce0070 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `767px` extracted from `key-co` stylesheet
- **Padding & Gutters**: `15px` lateral canvas padding with `6px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 767px`, `gap: 6px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `15px` horizontal padding
- **Media Queries**: `@media (min-width:64rem)`, `@media (max-width:767px)`, `@media (min-width:768px)`, `@media (min-width:40rem)`
- **Corner Radii**: `var(--radius)`, `.3125rem`, `.375rem`, `.25rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `adobe-caslon-pro`
- **Body Font Stack**: `proxima-nova`
- **Monospace / Technical Font Stack**: `GeistMono`
- **H1 Display Rule**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-5xl: 3rem`
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`; rule `,h2` (`font-weight: var(--font-we...`)
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`; rule `p` (`font-size: var(--text-sm)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: .28px`, `font-weight: var(--font-we...`)
- **Metadata & Index Rule**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`, `--text-sm: .875rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `key-co` (`KEY.co · Luxury Vacation Home Rentals + Concierge Services`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.relative> — `key-co`)**:
   - DOM & Selectors: Landmark `<nav class="relative flex">` hosting `KEY.co · Luxury Vacation Home Rental` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-theme="light"`), and stylesheet rule `.icon--copy { height:1.5384615385rem;width:1.5384615385rem }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.relative> — `key-co`)` (`key-co`) adapts across `@media (min-width:64rem)`, `@media (max-width:767px)`, `@media (min-width:768px)`, `@media (min-width:40rem)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.navbar-section> — `Pack your bags, we’ll do the rest`)**:
   - DOM & Selectors: Landmark `<section class="navbar-section">` presenting display lead `Pack your bags, we’ll do the rest` and copy excerpt *"$500 off $10k+ stays w/ HOLIDAYSAREHERE - ends 12/31"* over `#000` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#000` background with `#fff` headline `Pack your bags, we’ll do the rest`.
3. **Primary Showcase & Content Grid (<article.wf-proximanova-n5-active> — `Homes that inspire`)**:
   - DOM & Selectors: Landmark `<article class="wf-proximanova-n5-active">` rendering section `Homes that inspire` with copy *"Curated Vacation Homes + Luxury Services"*, asset references (`oaiq.min.js`, `283498678855975`, `fbevents.js`, `gtm.js`), and grid rule `.icon--copy .stroke { fill:none;stroke:currentColor;stroke-width:1px }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<article.wf-proximanova-n5-active> — `Homes that inspire`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 767px`, `gap: 6px`) on desktop and Single-column vertical stack at `390px` viewport width with `15px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Elegant Escape`)**:
   - DOM & Selectors: Landmark `<section class="relative video-fit">` framing `Elegant Escape` and `Galloping Goose Chalet` (*"Search destination"*) with `#0000` surface cards, `#808080` accents, and `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.relative> — `Elegant Escape`)` uses `var(--radius)`, `.3125rem`, `.375rem`, `.25rem` radii, `#808080` highlights, and assets (oaiq.min.js, 283498678855975, fbevents.js).
5. **Colophon & Global Directory Footer (<footer.bg-brand-beige> — `https://key.co/`)**:
   - DOM & Selectors: Landmark `<footer class="bg-brand-beige">` anchoring `KEY.co · Luxury Vacation Home Re` footer links (`Overview · Index · Archive · About · Contact`), copy *"Explore our selection of premium homes—each chosen for style"*, and `#ce0070` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.bg-brand-beige> — `https://key.co/`)` aligns to `767px` extracted from `key-co` stylesheet with `15px` lateral canvas padding with `6px` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"$500 off $10k+ stays w/ HOLIDAYSAREHERE - ends 12/31"*
- Copy Excerpt 2: *"Curated Vacation Homes + Luxury Services"*
- Copy Excerpt 3: *"Search destination"*
- Copy Excerpt 4: *"Explore our selection of premium homes—each chosen for style, comfort, and unforge..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`
- **Extracted Stylesheet Rules (`key-co`)**:
- `.icon--copy { height:1.5384615385rem;width:1.5384615385rem }`
- `.icon--copy .stroke { fill:none;stroke:currentColor;stroke-width:1px }`
- `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `key-co` stylesheet.
- **Selector `.navbar-hovered`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `key-co` stylesheet.
- **Selector `.navbar-hovered .navbar-logo img`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `key-co` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<nav.relative>` and `<article.wf-proximanova-n5-active>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `key-co`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
