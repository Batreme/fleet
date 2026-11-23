---
title: "UI Prompt Blueprint: spykercars-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "spykercars-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#0000ff` accent)"
---

# UI Design System & Master Generation Blueprint: spykercars-com

> **Hand-Built Super Sports Cars Since 1880 · Spyker Cars** (https://spykercars.com/) — Spyker builds highly exclusive, hand-built super sports cars in the Netherlands. Discover the C8 Preliator XXV Coupé and the marque's sto...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Hand-Built Super Sports Cars Since 1880 · Spyker Cars** (`https://spykercars.com/`). Spyker builds highly exclusive, hand-built super sports cars in the Netherlands. Discover the C8 Preliator XXV Coupé and the marque's sto...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#0000ff` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `browser-default` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#0000ff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `futura-pt-condensed` for display copy (`THE NEXT CHAPTER OF SPYKER`) with `swiss721` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `86rem` container bounds (`gap: 5px`, padding `16px`) with `cubic-bezier(.4,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `86rem` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `16px` lateral canvas padding with `5px` grid gap.
- **Border Radius Scale**: `.3125rem`, `.375rem`, `.25rem`, `var(--radius-2xl)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 86rem`, `gap: 5px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `16px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:64rem) and (orientation:landscape)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `p` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f24822` | `.animated-grid__col { background-color: #f24822 }` |
| **Interactive Accent / Highlight** | `#0000ff` | `.border-blue-600 { border-color: #0000ff }` |
| **Secondary / Muted Copy** | `#101010` | live computed `h2` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e5e5e5` | `10 { border-color: #e5e5e5 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background` | `oklch(100% 0 0)` | Canvas / Surface Token |
| `--foreground` | `oklch(14.5% 0 0)` | Typography Ink Token |
| `--card` | `oklch(96.5% .005 265)` | Color / Atmospheric Token |
| `--card-foreground` | `oklch(14.5% 0 0)` | Typography Ink Token |
| `--popover` | `oklch(100% 0 0)` | Color / Atmospheric Token |
| `--popover-foreground` | `oklch(14.5% 0 0)` | Typography Ink Token |
| `--primary` | `oklch(20.5% 0 0)` | Brand / Palette Token |
| `--primary-foreground` | `oklch(98.5% 0 0)` | Typography Ink Token |
| `--secondary` | `oklch(97% 0 0)` | Brand / Palette Token |
| `--secondary-foreground` | `oklch(20.5% 0 0)` | Typography Ink Token |
| `--muted` | `oklch(97% 0 0)` | Color / Atmospheric Token |
| `--muted-foreground` | `oklch(55.6% 0 0)` | Typography Ink Token |
| `--accent` | `oklch(97% 0 0)` | Brand / Palette Token |
| `--accent-foreground` | `oklch(20.5% 0 0)` | Typography Ink Token |
| `--destructive` | `oklch(57.7% .245 27.325)` | Color / Atmospheric Token |
| `--destructive-foreground` | `oklch(57.7% .245 27.325)` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `futura-pt-condensed`.
- **Primary Body Stack**: `swiss721`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 56px`, `line-height: 47.6px`, `font-weight: 500`, `letter-spacing: 2.24px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-5xl: 3rem`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 56px`, `line-height: 47.6px`, `font-weight: 500`, `letter-spacing: 2.24px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 38px`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`; rule `p` (`font-size: var(--text-sm)`, `line-height: var(--tw-leading,var(...`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-mono: ui-monospace,SFMono-Regular,monospace`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `spykercars-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `spykercars-com` stylesheet.
- **Selector `box-shadow\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `spykercars-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<nav.py-4>` and `<section.w-full>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Hand-Built Super Sports Cars Since 1880 ·  │
│ ====================================================================== │
│ [ <nav.py-4> (1425x88px)              | Home · Heritage · Boutique · ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <article.lenis-autoToggle> (w=1425px)                  | │
│ | H1: THE NEXT CHAPTER OF SPYKER                                     | │
│ | Substrate: #ffffff | Ink: #000000 | Accent: #0000ff                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.w-full>) max-w: 86rem                      | │
│ | +------------------------------+  +------------------------------+ | │
│ | | The next chapter of Spyker T |  | P u r e P a s s i o n        | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.fixed>) — N u l l a T e n a c i            | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.relative>   ) | https://spykercars.com/              │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 5px)        │
│ ====================================================================== │
│ [ HEADER BAR (<nav.py-4>              ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<article.lenis-autoToggl) — 390px Vertical Lead        | │
│ | H1: THE NEXT CHAPTER OF SPYKER                                     | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.w-full>) — 1-Col Stack                    | │
│ | [ Item 1: The next chapter of Spyker T h e n e x t c h a p...    ] | │
│ | [ Item 2: P u r e P a s s i o n                                  ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.fixed>) — 1-Col (N u l l a T e n a )        | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.relative>   ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.py-4> — `spykercars-com`)**:
   - Landmark `<nav class="py-4 container">` (`1425x88px`) hosting `Hand-Built Super Sports Cars Since 1` navigation (`Home · Heritage · Boutique · News · Contact`), DOM attributes (`data-theme="light"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.__className_e6d04a { font-family:swiss721,swiss721 Fallback }`.
2. **Hero Stage & Focal Lead (<article.lenis-autoToggle> — `THE NEXT CHAPTER OF SPYKER`)**:
   - Landmark `<article class="lenis-autoToggle">` presenting display lead `THE NEXT CHAPTER OF SPYKER` and copy excerpt *"We use cookies to run the site, and optionally for analytics and "* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.w-full> — `The next chapter of Spyker T h e n`)**:
   - Landmark `<section class="w-full relative">` rendering section `The next chapter of Spyker T h e n e x t c h a p...` with copy *"T h e b e g i n n i n g o f X X V"*, asset references (`f13a7bda184fa931.css`, `86c130d7567786c0.css`, `3c4afd8b2a3df79a.css`, `cdb4fb19178d4946.css`), and grid rule `.__variable_e6d04a { --font-swiss-721:"swiss721","swiss721 Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.fixed> — `P u r e P a s s i o n`)**:
   - Landmark `<section class="fixed">` framing `P u r e P a s s i o n` and `N u l l a T e n a c i I n v i a E s t V i a` (*"The next chapter of Spyker"*) with `#f24822` surface cards, `#0000ff` accents, and `.__className_83cf94 { font-family:"PT Serif","PT Serif Fallback";font-weight:400;font-style:no... }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://spykercars.com/`)**:
   - Landmark `<footer class="relative z-30">` anchoring `Hand-Built Super Sports Cars Sin` footer links (`Home · Heritage · Boutique · News · Contact`), copy *"T h e n e x t c h a p t e r o f S p y k e r"*, and `#e5e5e5` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: spykercars-com (Hand-Built Super Sports Cars Since 1880 · Spyker Cars)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `spykercars-com` (**Hand-Built Super Sports Cars Since 1880 · Spyker Cars** — `https://spykercars.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#0000ff` accent).
- **Identity & Domain Context**: Spyker builds highly exclusive, hand-built super sports cars in the Netherlands. Discover the C8 Preliator XXV Coupé and the marque's sto...
- **Primary Substrate**: `#ffffff` (live computed `browser-default` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#0000ff`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `browser-default` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#0000ff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `futura-pt-condensed` for display copy (`THE NEXT CHAPTER OF SPYKER`) with `swiss721` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `86rem` container bounds (`gap: 5px`, padding `16px`) with `cubic-bezier(.4,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `spykercars-com` in your global stylesheet:

:root {
  /* Hand-Built Super Sports Cars Since 1880 · Spyker Cars (spykercars-com) — Live-Grounded CSS Variables */
  --background: oklch(100% 0 0); /* Canvas / Surface Token (spykercars-com) */
  --foreground: oklch(14.5% 0 0); /* Typography Ink Token (spykercars-com) */
  --card: oklch(96.5% .005 265); /* Color / Atmospheric Token (spykercars-com) */
  --card-foreground: oklch(14.5% 0 0); /* Typography Ink Token (spykercars-com) */
  --popover: oklch(100% 0 0); /* Color / Atmospheric Token (spykercars-com) */
  --popover-foreground: oklch(14.5% 0 0); /* Typography Ink Token (spykercars-com) */
  --primary: oklch(20.5% 0 0); /* Brand / Palette Token (spykercars-com) */
  --primary-foreground: oklch(98.5% 0 0); /* Typography Ink Token (spykercars-com) */
  --secondary: oklch(97% 0 0); /* Brand / Palette Token (spykercars-com) */
  --secondary-foreground: oklch(20.5% 0 0); /* Typography Ink Token (spykercars-com) */
  --muted: oklch(97% 0 0); /* Color / Atmospheric Token (spykercars-com) */
  --muted-foreground: oklch(55.6% 0 0); /* Typography Ink Token (spykercars-com) */
  --accent: oklch(97% 0 0); /* Brand / Palette Token (spykercars-com) */
  --accent-foreground: oklch(20.5% 0 0); /* Typography Ink Token (spykercars-com) */
  --destructive: oklch(57.7% .245 27.325); /* Color / Atmospheric Token (spykercars-com) */
  --destructive-foreground: oklch(57.7% .245 27.325); /* Typography Ink Token (spykercars-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `browser-default` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in live computed `p` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#f24822` — grounded in `.animated-grid__col { background-color: #f24822 }`
- **Interactive Accent / Highlight**: `#0000ff` — grounded in `.border-blue-600 { border-color: #0000ff }`
- **Secondary / Muted Copy**: `#101010` — grounded in live computed `h2` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#e5e5e5` — grounded in `10 { border-color: #e5e5e5 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `86rem` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `16px` lateral canvas padding with `5px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 86rem`, `gap: 5px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `16px` horizontal padding
- **Media Queries**: `@media (min-width:64rem) and (orientation:landscape)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`
- **Corner Radii**: `.3125rem`, `.375rem`, `.25rem`, `var(--radius-2xl)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `futura-pt-condensed`
- **Body Font Stack**: `swiss721`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: live computed `h1` (`font-size: 56px`, `line-height: 47.6px`, `font-weight: 500`, `letter-spacing: 2.24px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-5xl: 3rem`
- **H2 Section Rule**: live computed `h2` (`font-size: 56px`, `line-height: 47.6px`, `font-weight: 500`, `letter-spacing: 2.24px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 38px`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`; rule `p` (`font-size: var(--text-sm)`, `line-height: var(--tw-leading,var(...`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-mono: ui-monospace,SFMono-Regular,monospace`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `spykercars-com` (`Hand-Built Super Sports Cars Since 1880 · Spyker Cars`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.py-4> — `spykercars-com`)**:
   - DOM & Selectors: Landmark `<nav class="py-4 container">` (`1425x88px`) hosting `Hand-Built Super Sports Cars Since 1` navigation (`Home · Heritage · Boutique · News · Contact`), DOM attributes (`data-theme="light"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.__className_e6d04a { font-family:swiss721,swiss721 Fallback }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.py-4> — `spykercars-com`)` (`spykercars-com`) adapts across `@media (min-width:64rem) and (orientation:landscape)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)` with `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Home · Heritage · Boutique · News · Contact`.
2. **Hero Stage & Focal Lead (<article.lenis-autoToggle> — `THE NEXT CHAPTER OF SPYKER`)**:
   - DOM & Selectors: Landmark `<article class="lenis-autoToggle">` presenting display lead `THE NEXT CHAPTER OF SPYKER` and copy excerpt *"We use cookies to run the site, and optionally for analytics and "* over `#ffffff` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#ffffff` background with `#000000` headline `THE NEXT CHAPTER OF SPYKER`.
3. **Primary Showcase & Content Grid (<section.w-full> — `The next chapter of Spyker T h e n`)**:
   - DOM & Selectors: Landmark `<section class="w-full relative">` rendering section `The next chapter of Spyker T h e n e x t c h a p...` with copy *"T h e b e g i n n i n g o f X X V"*, asset references (`f13a7bda184fa931.css`, `86c130d7567786c0.css`, `3c4afd8b2a3df79a.css`, `cdb4fb19178d4946.css`), and grid rule `.__variable_e6d04a { --font-swiss-721:"swiss721","swiss721 Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.w-full> — `The next chapter of Spyker T h e n`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 86rem`, `gap: 5px`) on desktop and Single-column vertical stack at `390px` viewport width with `16px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.fixed> — `P u r e P a s s i o n`)**:
   - DOM & Selectors: Landmark `<section class="fixed">` framing `P u r e P a s s i o n` and `N u l l a T e n a c i I n v i a E s t V i a` (*"The next chapter of Spyker"*) with `#f24822` surface cards, `#0000ff` accents, and `.__className_83cf94 { font-family:"PT Serif","PT Serif Fallback";font-weight:400;font-style:no... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.fixed> — `P u r e P a s s i o n`)` uses `.3125rem`, `.375rem`, `.25rem`, `var(--radius-2xl)` radii, `#0000ff` highlights, and assets (f13a7bda184fa931.css, 86c130d7567786c0.css, 3c4afd8b2a3df79a.css).
5. **Colophon & Global Directory Footer (<footer.relative> — `https://spykercars.com/`)**:
   - DOM & Selectors: Landmark `<footer class="relative z-30">` anchoring `Hand-Built Super Sports Cars Sin` footer links (`Home · Heritage · Boutique · News · Contact`), copy *"T h e n e x t c h a p t e r o f S p y k e r"*, and `#e5e5e5` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.relative> — `https://spykercars.com/`)` aligns to `86rem` (non-`@media` desktop container stylesheet rule) with `16px` lateral canvas padding with `5px` grid gap and attributes (data-theme="light", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"We use cookies to run the site, and optionally for analytics and marketing."*
- Copy Excerpt 2: *"T h e b e g i n n i n g o f X X V"*
- Copy Excerpt 3: *"The next chapter of Spyker"*
- Copy Excerpt 4: *"T h e n e x t c h a p t e r o f S p y k e r"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`spykercars-com`)**:
- `.__className_e6d04a { font-family:swiss721,swiss721 Fallback }`
- `.__variable_e6d04a { --font-swiss-721:"swiss721","swiss721 Fallback" }`
- `.__className_83cf94 { font-family:"PT Serif","PT Serif Fallback";font-weight:400;font-style:no... }`
- `.__variable_83cf94 { --font-pt-serif:"PT Serif","PT Serif Fallback" }`
- `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `spykercars-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `spykercars-com` stylesheet.
- **Selector `box-shadow\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `spykercars-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<nav.py-4>` and `<section.w-full>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `spykercars-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
