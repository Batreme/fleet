---
title: "UI Prompt Blueprint: www-banham-co-uk"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-banham-co-uk"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#ff0000` accent)"
---

# UI Design System & Master Generation Blueprint: www-banham-co-uk

> **Banham · Experts in Security Services Since 1926** (https://www.banham.co.uk/) — Welcome to Banham, market-leaders in the security industry since 1926, and the perfect people to help secure your property

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Banham · Experts in Security Services Since 1926** (`https://www.banham.co.uk/`). Welcome to Banham, market-leaders in the security industry since 1926, and the perfect people to help secure your property
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#ff0000` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `browser-default` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#ff0000` accents.
  - **Grounded Typographic Hierarchy**: Pairs `IvarHeadline` for display copy (`Protect What You Cherish`) with `IvarText` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: .375rem`, padding `.5rem`) with `cubic-bezier(.4,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1440px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `.5rem` lateral canvas padding with `.375rem` grid gap.
- **Border Radius Scale**: `100%`, `.3125rem`, `.375rem`, `.25rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: .375rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:640px)`, `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media (min-width:1440px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#eeeeee` | live computed `p` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ff0000` | `.dfd-btn-error { background-color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#737678` | `var(--df-accent-secondary)` in `:root` |
| **Structural Hairline Border** | `#cbcccd` | `var(--df-neutral-outline)` in `:root` |
| **Variable Token (`--btn-stroke`)** | `#0000` | `var(--btn-stroke)` in `:root` |
| **Variable Token (`--btn-bg`)** | `#333e48` | `var(--btn-bg)` in `:root` |
| **Variable Token (`--btn-hover-bg`)** | `#2b3239` | `var(--btn-hover-bg)` in `:root` |
| **Variable Token (`--color-cornflower-100`)** | `#8392a7` | `var(--color-cornflower-100)` in `:root` |
| **Variable Token (`--color-amsb_graystarts`)** | `#cbd5e0` | `var(--color-amsb_graystarts)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--btn-stroke` | `#0000` | Elevation / Border Token |
| `--btn-bg` | `#333e48` | Canvas / Surface Token |
| `--btn-color` | `#fff` | Brand / Palette Token |
| `--btn-hover-bg` | `#2b3239` | Canvas / Surface Token |
| `--btn-active-bg` | `#2b3239` | Canvas / Surface Token |
| `--line-after` | `#000` | Color / Atmospheric Token |
| `--line-before` | `#0000` | Color / Atmospheric Token |
| `--width-am-latter` | `32px` | Layout / Spatial Grid Token |
| `--width-am-brand` | `120px` | Brand / Palette Token |
| `--width-am-popup-content` | `600px` | Layout / Spatial Grid Token |
| `--height-am-latter` | `32px` | Layout / Spatial Grid Token |
| `--height-am-popup-content` | `415px` | Layout / Spatial Grid Token |
| `--background-size-size20` | `20px` | Canvas / Surface Token |
| `--color-cornflower-100` | `#8392a7` | Brand / Palette Token |
| `--padding-full` | `100%` | Layout / Spatial Grid Token |
| `--color-amsb_graystarts` | `#cbd5e0` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `IvarHeadline`.
- **Primary Body Stack**: `IvarText`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 48px`, `line-height: 52.8px`, `font-weight: 400`, `letter-spacing: 1.2px`); CSS variables `--dfd-btn-display: inline-flex`, `--dfd-btn-group-display: flex`; rule `,h1` (`font-size: 2.25rem`, `line-height: 2.5rem`, `letter-spacing: .36px`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 24px`, `line-height: 30px`, `font-weight: 400`, `letter-spacing: 0.24px`); rule `,h2` (`font-size: 28px`, `line-height: 1.25`, `letter-spacing: .28px`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: .875rem`, `line-height: 1.25rem`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`); rule `.label` (`font-size: 1rem`, `line-height: 1.5rem`, `font-weight: 600`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.8,0,1,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.catalog-product-view .product-ta...`**: `transition: cubic-bezier(.4,0,.2,1)` extracted from `www-banham-co-uk` stylesheet.
- **Selector `.catalog-product-view .what-new a`**: `transition: .3s` extracted from `www-banham-co-uk` stylesheet.
- **Selector `builder-banner-wrapper .pagebuild...`**: `transition: .5s` extracted from `www-banham-co-uk` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.page-header>` and `<section.storyblok-home>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router, Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Banham · Experts in Security Services Sinc │
│ ====================================================================== │
│ [ <header.page-header> (1425x0px)     | Book a Survey · Locks · All  ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.message> (w=1425px)                           | │
│ | H1: Protect What You Cherish                                       | │
│ | Substrate: #ffffff | Ink: #000000 | Accent: #ff0000                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.storyblok-home>) max-w: 1440px             | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Handcrafted in Britain Since |  | Bespoke Doors                | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.fixed>) — Explore Banham                   | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer-conta) | https://www.banham.co.uk/            │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .375rem)    │
│ ====================================================================== │
│ [ HEADER BAR (<header.page-header>    ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.message>) — 390px Vertical Lead               | │
│ | H1: Protect What You Cherish                                       | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.storyblok-hom) — 1-Col Stack              | │
│ | [ Item 1: Handcrafted in Britain Since 1926                      ] | │
│ | [ Item 2: Bespoke Doors                                          ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.fixed>) — 1-Col (Explore Banham)            | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer-conta) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.page-header> — `www-banham-co-uk`)**:
   - Landmark `<header class="page-header">` (`1425x0px`) hosting `Banham · Experts in Security Service` navigation (`Book a Survey · Locks · All Locks · Door Locks · Emergency Locksmiths`), DOM attributes (`data-mm-order="40"`, `data-mm-order="50"`, `data-ueto="ueto_12e8e1f459"`, `data-hj-csq-tag`), and stylesheet rule `before { box-sizing:border-box;border:0 solid e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.message> — `Protect What You Cherish`)**:
   - Landmark `<section class="message global">` presenting display lead `Protect What You Cherish` and copy excerpt *"Prefer to call? Reach us on 020 7819 3730"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.storyblok-home> — `Handcrafted in Britain Since 1926`)**:
   - Landmark `<section class="storyblok-home">` rendering section `Handcrafted in Britain Since 1926` with copy *"To celebrate 100 years of Banham, we went behind closed doors to "*, asset references (`styles.min.css`, `chosen.min.css`, `trustpilot.min.css`, `Banham_Logo_FA-04.png`), and grid rule `body { margin:0;line-height:inherit }`.
4. **Interactive Detail & Feature Matrix (<section.fixed> — `Bespoke Doors`)**:
   - Landmark `<section class="fixed w-full">` framing `Bespoke Doors` and `Explore Banham` (*"Marrying innovation with time honoured techniques, every detail o"*) with `#eeeeee` surface cards, `#ff0000` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.footer-container> — `https://www.banham.co.uk/`)**:
   - Landmark `<footer class="footer-container">` anchoring `Banham · Experts in Security Ser` footer links (`Book a Survey · Locks · All Locks · Door Locks · Emergency Locksmiths`), copy *"Innovative, award-winning and precision engineered in Britai"*, and `#cbcccd` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-banham-co-uk (Banham · Experts in Security Services Since 1926)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-banham-co-uk` (**Banham · Experts in Security Services Since 1926** — `https://www.banham.co.uk/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#ff0000` accent).
- **Identity & Domain Context**: Welcome to Banham, market-leaders in the security industry since 1926, and the perfect people to help secure your property
- **Primary Substrate**: `#ffffff` (live computed `browser-default` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#ff0000`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `browser-default` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#ff0000` accents.
  - **Grounded Typographic Hierarchy**: Pairs `IvarHeadline` for display copy (`Protect What You Cherish`) with `IvarText` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: .375rem`, padding `.5rem`) with `cubic-bezier(.4,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-banham-co-uk` in your global stylesheet:

:root {
  /* Banham · Experts in Security Services Since 1926 (www-banham-co-uk) — Live-Grounded CSS Variables */
  --btn-stroke: #0000; /* Elevation / Border Token (www-banham-co-uk) */
  --btn-bg: #333e48; /* Canvas / Surface Token (www-banham-co-uk) */
  --btn-color: #fff; /* Brand / Palette Token (www-banham-co-uk) */
  --btn-hover-bg: #2b3239; /* Canvas / Surface Token (www-banham-co-uk) */
  --btn-active-bg: #2b3239; /* Canvas / Surface Token (www-banham-co-uk) */
  --line-after: #000; /* Color / Atmospheric Token (www-banham-co-uk) */
  --line-before: #0000; /* Color / Atmospheric Token (www-banham-co-uk) */
  --width-am-latter: 32px; /* Layout / Spatial Grid Token (www-banham-co-uk) */
  --width-am-brand: 120px; /* Brand / Palette Token (www-banham-co-uk) */
  --width-am-popup-content: 600px; /* Layout / Spatial Grid Token (www-banham-co-uk) */
  --height-am-latter: 32px; /* Layout / Spatial Grid Token (www-banham-co-uk) */
  --height-am-popup-content: 415px; /* Layout / Spatial Grid Token (www-banham-co-uk) */
  --background-size-size20: 20px; /* Canvas / Surface Token (www-banham-co-uk) */
  --color-cornflower-100: #8392a7; /* Brand / Palette Token (www-banham-co-uk) */
  --padding-full: 100%; /* Layout / Spatial Grid Token (www-banham-co-uk) */
  --color-amsb_graystarts: #cbd5e0; /* Brand / Palette Token (www-banham-co-uk) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `browser-default` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#eeeeee` — grounded in live computed `p` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#ff0000` — grounded in `.dfd-btn-error { background-color: red }` (`#ff0000`)
- **Secondary / Muted Copy**: `#737678` — grounded in `var(--df-accent-secondary)` in `:root`
- **Structural Hairline Border**: `#cbcccd` — grounded in `var(--df-neutral-outline)` in `:root`
- **Variable Token (`--btn-stroke`)**: `#0000` — grounded in `var(--btn-stroke)` in `:root`
- **Variable Token (`--btn-bg`)**: `#333e48` — grounded in `var(--btn-bg)` in `:root`
- **Variable Token (`--btn-hover-bg`)**: `#2b3239` — grounded in `var(--btn-hover-bg)` in `:root`
- **Variable Token (`--color-cornflower-100`)**: `#8392a7` — grounded in `var(--color-cornflower-100)` in `:root`
- **Variable Token (`--color-amsb_graystarts`)**: `#cbd5e0` — grounded in `var(--color-amsb_graystarts)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1440px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `.5rem` lateral canvas padding with `.375rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: .375rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding
- **Media Queries**: `@media (min-width:640px)`, `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media (min-width:1440px)`
- **Corner Radii**: `100%`, `.3125rem`, `.375rem`, `.25rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `IvarHeadline`
- **Body Font Stack**: `IvarText`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 48px`, `line-height: 52.8px`, `font-weight: 400`, `letter-spacing: 1.2px`); CSS variables `--dfd-btn-display: inline-flex`, `--dfd-btn-group-display: flex`; rule `,h1` (`font-size: 2.25rem`, `line-height: 2.5rem`, `letter-spacing: .36px`)
- **H2 Section Rule**: live computed `h2` (`font-size: 24px`, `line-height: 30px`, `font-weight: 400`, `letter-spacing: 0.24px`); rule `,h2` (`font-size: 28px`, `line-height: 1.25`, `letter-spacing: .28px`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: .875rem`, `line-height: 1.25rem`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`); rule `.label` (`font-size: 1rem`, `line-height: 1.5rem`, `font-weight: 600`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-banham-co-uk` (`Banham · Experts in Security Services Since 1926`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.page-header> — `www-banham-co-uk`)**:
   - DOM & Selectors: Landmark `<header class="page-header">` (`1425x0px`) hosting `Banham · Experts in Security Service` navigation (`Book a Survey · Locks · All Locks · Door Locks · Emergency Locksmiths`), DOM attributes (`data-mm-order="40"`, `data-mm-order="50"`, `data-ueto="ueto_12e8e1f459"`, `data-hj-csq-tag`), and stylesheet rule `before { box-sizing:border-box;border:0 solid e5e7eb }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.page-header> — `www-banham-co-uk`)` (`www-banham-co-uk`) adapts across `@media (min-width:640px)`, `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media (min-width:1440px)` with `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.8,0,1,1)` transitions and links `Book a Survey · Locks · All Locks · Door Locks · Emergency Locksmiths`.
2. **Hero Stage & Focal Lead (<section.message> — `Protect What You Cherish`)**:
   - DOM & Selectors: Landmark `<section class="message global">` presenting display lead `Protect What You Cherish` and copy excerpt *"Prefer to call? Reach us on 020 7819 3730"* over `#ffffff` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#ffffff` background with `#000000` headline `Protect What You Cherish`.
3. **Primary Showcase & Content Grid (<section.storyblok-home> — `Handcrafted in Britain Since 1926`)**:
   - DOM & Selectors: Landmark `<section class="storyblok-home">` rendering section `Handcrafted in Britain Since 1926` with copy *"To celebrate 100 years of Banham, we went behind closed doors to "*, asset references (`styles.min.css`, `chosen.min.css`, `trustpilot.min.css`, `Banham_Logo_FA-04.png`), and grid rule `body { margin:0;line-height:inherit }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.storyblok-home> — `Handcrafted in Britain Since 1926`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: .375rem`) on desktop and Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.fixed> — `Bespoke Doors`)**:
   - DOM & Selectors: Landmark `<section class="fixed w-full">` framing `Bespoke Doors` and `Explore Banham` (*"Marrying innovation with time honoured techniques, every detail o"*) with `#eeeeee` surface cards, `#ff0000` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.fixed> — `Bespoke Doors`)` uses `100%`, `.3125rem`, `.375rem`, `.25rem` radii, `#ff0000` highlights, and assets (styles.min.css, chosen.min.css, trustpilot.min.css).
5. **Colophon & Global Directory Footer (<footer.footer-container> — `https://www.banham.co.uk/`)**:
   - DOM & Selectors: Landmark `<footer class="footer-container">` anchoring `Banham · Experts in Security Ser` footer links (`Book a Survey · Locks · All Locks · Door Locks · Emergency Locksmiths`), copy *"Innovative, award-winning and precision engineered in Britai"*, and `#cbcccd` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer-container> — `https://www.banham.co.uk/`)` aligns to `1440px` (non-`@media` desktop container stylesheet rule) with `.5rem` lateral canvas padding with `.375rem` grid gap and attributes (data-mm-order="40", data-mm-order="50", data-ueto="ueto_12e8e1f459").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Prefer to call? Reach us on 020 7819 3730"*
- Copy Excerpt 2: *"To celebrate 100 years of Banham, we went behind closed doors to discover what you..."*
- Copy Excerpt 3: *"Marrying innovation with time honoured techniques, every detail of every Banham pr..."*
- Copy Excerpt 4: *"Innovative, award-winning and precision engineered in Britain: explore our range o..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.8,0,1,1)`
- **Extracted Stylesheet Rules (`www-banham-co-uk`)**:
- `before { box-sizing:border-box;border:0 solid e5e7eb }`
- `body { margin:0;line-height:inherit }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { font-size:75%;line-height:0;position:relative;vertical-align:initial }`
- **Per-Selector Transition Rules**:
- **Selector `.catalog-product-view .product-ta...`**: `transition: cubic-bezier(.4,0,.2,1)` extracted from `www-banham-co-uk` stylesheet.
- **Selector `.catalog-product-view .what-new a`**: `transition: .3s` extracted from `www-banham-co-uk` stylesheet.
- **Selector `builder-banner-wrapper .pagebuild...`**: `transition: .5s` extracted from `www-banham-co-uk` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.page-header>` and `<section.storyblok-home>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router, Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-banham-co-uk`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
