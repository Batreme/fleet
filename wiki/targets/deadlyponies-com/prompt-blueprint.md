---
title: "UI Prompt Blueprint: deadlyponies-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "deadlyponies-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#f0efeb` canvas, `#000000` ink, `#084ccc` accent)"
---

# UI Design System & Master Generation Blueprint: deadlyponies-com

> **Deadly Ponies - Luxury Leather Bags & Accessories** (https://deadlyponies.com) — Discover Deadly Ponies, a New Zealand-based label, crafting luxury bags & accessories. Coveted luxury leather handbags and accessories.

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Deadly Ponies - Luxury Leather Bags & Accessories** (`https://deadlyponies.com`). Discover Deadly Ponies, a New Zealand-based label, crafting luxury bags & accessories. Coveted luxury leather handbags and accessories.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#f0efeb` canvas, `#000000` ink, `#084ccc` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f0efeb` (live computed `section` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#084ccc` accents.
  - **Grounded Typographic Hierarchy**: Pairs `DLYP` for display copy (`Transparency`) with `DLYP` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 2rem`, padding `1rem`) with `cubic-bezier(0.5,0,0.5,1)` easing and GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1440px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `1rem` lateral canvas padding with `2rem` grid gap.
- **Border Radius Scale**: `50%`, `0px`, `8px`, `5px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 2rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:992px)`, `@media (max-width:575.98px)`, `@media (max-width:767.98px)`, `@media (max-width:991.98px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f0efeb` | live computed `section` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f9f9f7` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#084ccc` | `.video-section__btn:active { background-color: #084ccc }` |
| **Secondary / Muted Copy** | `#8f8f8f` | `var(--apd-muted)` in `:root` |
| **Structural Hairline Border** | `#dadada` | `var(--apd-line)` in `:root` |
| **Variable Token (`--kl-reviews-color-light-gray`)** | `#e9e9eb` | `var(--kl-reviews-color-light-gray)` in `:root` |
| **Variable Token (`--swym-remind-cta-bg-color`)** | `#00a65a` | `var(--swym-remind-cta-bg-color)` in `:root` |
| **Variable Token (`--swym-subscribe-success-bg-color`)** | `#aee9d1` | `var(--swym-subscribe-success-bg-color)` in `:root` |
| **Variable Token (`--swym-subscribe-success-text-color`)** | `#202223` | `var(--swym-subscribe-success-text-color)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--height-full` | `100vh` | Layout / Spatial Grid Token |
| `--height-fill` | `calc(100vh - var(--nav-height))` | Layout / Spatial Grid Token |
| `--font-deadly` | `"Deadly", sans-serif` | Typography / Scale Token |
| `--nav-main-height` | `46px` | Layout / Spatial Grid Token |
| `--nav-height` | `var(--nav-main-height)` | Layout / Spatial Grid Token |
| `--text-color` | `#000000` | Typography Ink Token |
| `--section-height` | `90vh` | Layout / Spatial Grid Token |
| `--kl-reviews-color-light-gray` | `#e9e9eb` | Canvas / Surface Token |
| `--swym-remind-cta-bg-color` | `#00a65a` | Canvas / Surface Token |
| `--swym-remind-cta-text-color` | `white` | Typography Ink Token |
| `--swym-remind-cta-bg-color-v2` | `#000000` | Canvas / Surface Token |
| `--swym-remind-cta-text-color-v2` | `white` | Typography Ink Token |
| `--swym-subscribe-success-bg-color` | `#AEE9D1` | Canvas / Surface Token |
| `--swym-subscribe-success-text-color` | `#202223` | Typography Ink Token |
| `--swym-recently-viewed-pointer-pos` | `92%` | Dimension / Scale Token |
| `--base-height` | `calc(100vh - 310px)` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `DLYP`.
- **Primary Body Stack**: `DLYP`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 26px`, `line-height: 32px`, `letter-spacing: -.78px`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 16px`, `line-height: 38px`, `font-weight: 400`, `letter-spacing: -0.64px`); rule `h2` (`font-size: 22px`, `line-height: 30px`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 18.4px`, `font-weight: 400`); rule `p` (`font-size: 14px`, `line-height: 20px`, `letter-spacing: -.02em`, `font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 18.4px`, `font-weight: 400`); rule `small` (`font-size: calc(var(--kl-reviews-reviews...`, `font-weight: var(--kl-revi...`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.5,0,0.5,1)`, `cubic-bezier(0.4,0,0.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.swiper-wrapper`**: `transition: var(--swiper-wrapper-transition-timing-function,initial)` extracted from `deadlyponies-com` stylesheet.
- **Selector `.swiper-pagination`**: `transition: .3s opacity` extracted from `deadlyponies-com` stylesheet.
- **Selector `n-bullets-dynamic .swiper-paginat...`**: `transition: .2s transform,.2s top` extracted from `deadlyponies-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.5,0,0.5,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.content-section>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Deadly Ponies - Luxury Leather Bags & Acce │
│ ====================================================================== │
│ [ <header.header> (1440x83px)         | Bags · New Arrivals · View A ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.shopify-section> (w=1440px)                   | │
│ | H1: Transparency                                                   | │
│ | Substrate: #f0efeb | Ink: #000000 | Accent: #084ccc                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.content-section>) max-w: 1440px            | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Find your local              |  | Express Shipping             | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.section--hero_v2>) — Find in store         | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>     ) | https://deadlyponies.com             │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 2rem)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.header>         ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.shopify-section) — 390px Vertical Lead        | │
│ | H1: Transparency                                                   | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.content-secti) — 1-Col Stack              | │
│ | [ Item 1: Find your local                                        ] | │
│ | [ Item 2: Express Shipping                                       ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.section--hero_v) — 1-Col (Find in store)    | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>     ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.header> — `deadlyponies-com`)**:
   - Landmark `<header class="header header--dark">` (`1440x83px`) hosting `Deadly Ponies - Luxury Leather Bags ` navigation (`Bags · New Arrivals · View All · Tote Bags · Shoulder Bags`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shop-id="71218823442"`, `data-venmo-supported="false"`, `data-environment="production"`), and stylesheet rule `root { --swiper-theme-color:007aff }`.
2. **Hero Stage & Focal Lead (<section.shopify-section> — `Transparency`)**:
   - Landmark `<section class="shopify-section content-section">` presenting display lead `Transparency` and copy excerpt *"Deadly Ponies’ tiered loyalty programme with bespoke gifting and "* over `#f0efeb` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.content-section> — `Find your local`)**:
   - Landmark `<section class="shopify-section content-section">` rendering section `Find your local` with copy *"A commitment to responsible materials, thoughtful craft, and piec"*, asset references (`93837`, `loader.js`, `01H2CKQHWBM22V9RBNTG4KH275`, `swym-ext-shopify.js`), and grid rule `swiper-container { margin-left:auto;margin-right:auto;position:relative;overflow:hidden;lis... }`.
4. **Interactive Detail & Feature Matrix (<section.section--hero_v2> — `Express Shipping`)**:
   - Landmark `<section class="shopify-section content-section">` framing `Express Shipping` and `Find in store` (*"Our stores provide a serene space to live and breathe the magic t"*) with `#f9f9f7` surface cards, `#084ccc` accents, and `.swiper-vertical>.swiper-wrapper { flex-direction:column }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://deadlyponies.com`)**:
   - Landmark `<footer class="footer">` anchoring `Deadly Ponies - Luxury Leather B` footer links (`Bags · New Arrivals · View All · Tote Bags · Shoulder Bags`), copy *"Discover our Journal - a space for collections, creativity, "*, and `#dadada` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: deadlyponies-com (Deadly Ponies - Luxury Leather Bags & Accessories)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `deadlyponies-com` (**Deadly Ponies - Luxury Leather Bags & Accessories** — `https://deadlyponies.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#f0efeb` canvas, `#000000` ink, `#084ccc` accent).
- **Identity & Domain Context**: Discover Deadly Ponies, a New Zealand-based label, crafting luxury bags & accessories. Coveted luxury leather handbags and accessories.
- **Primary Substrate**: `#f0efeb` (live computed `section` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#084ccc`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f0efeb` (live computed `section` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#084ccc` accents.
  - **Grounded Typographic Hierarchy**: Pairs `DLYP` for display copy (`Transparency`) with `DLYP` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 2rem`, padding `1rem`) with `cubic-bezier(0.5,0,0.5,1)` easing and GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `deadlyponies-com` in your global stylesheet:

:root {
  /* Deadly Ponies - Luxury Leather Bags & Accessories (deadlyponies-com) — Live-Grounded CSS Variables */
  --height-full: 100vh; /* Layout / Spatial Grid Token (deadlyponies-com) */
  --height-fill: calc(100vh - var(--nav-height)); /* Layout / Spatial Grid Token (deadlyponies-com) */
  --font-deadly: "Deadly", sans-serif; /* Typography / Scale Token (deadlyponies-com) */
  --nav-main-height: 46px; /* Layout / Spatial Grid Token (deadlyponies-com) */
  --nav-height: var(--nav-main-height); /* Layout / Spatial Grid Token (deadlyponies-com) */
  --text-color: #000000; /* Typography Ink Token (deadlyponies-com) */
  --section-height: 90vh; /* Layout / Spatial Grid Token (deadlyponies-com) */
  --kl-reviews-color-light-gray: #e9e9eb; /* Canvas / Surface Token (deadlyponies-com) */
  --swym-remind-cta-bg-color: #00a65a; /* Canvas / Surface Token (deadlyponies-com) */
  --swym-remind-cta-text-color: white; /* Typography Ink Token (deadlyponies-com) */
  --swym-remind-cta-bg-color-v2: #000000; /* Canvas / Surface Token (deadlyponies-com) */
  --swym-remind-cta-text-color-v2: white; /* Typography Ink Token (deadlyponies-com) */
  --swym-subscribe-success-bg-color: #AEE9D1; /* Canvas / Surface Token (deadlyponies-com) */
  --swym-subscribe-success-text-color: #202223; /* Typography Ink Token (deadlyponies-com) */
  --swym-recently-viewed-pointer-pos: 92%; /* Dimension / Scale Token (deadlyponies-com) */
  --base-height: calc(100vh - 310px); /* Layout / Spatial Grid Token (deadlyponies-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f0efeb` — grounded in live computed `section` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#f9f9f7` — grounded in live computed `footer` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#084ccc` — grounded in `.video-section__btn:active { background-color: #084ccc }`
- **Secondary / Muted Copy**: `#8f8f8f` — grounded in `var(--apd-muted)` in `:root`
- **Structural Hairline Border**: `#dadada` — grounded in `var(--apd-line)` in `:root`
- **Variable Token (`--kl-reviews-color-light-gray`)**: `#e9e9eb` — grounded in `var(--kl-reviews-color-light-gray)` in `:root`
- **Variable Token (`--swym-remind-cta-bg-color`)**: `#00a65a` — grounded in `var(--swym-remind-cta-bg-color)` in `:root`
- **Variable Token (`--swym-subscribe-success-bg-color`)**: `#aee9d1` — grounded in `var(--swym-subscribe-success-bg-color)` in `:root`
- **Variable Token (`--swym-subscribe-success-text-color`)**: `#202223` — grounded in `var(--swym-subscribe-success-text-color)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1440px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `1rem` lateral canvas padding with `2rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 2rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding
- **Media Queries**: `@media (min-width:992px)`, `@media (max-width:575.98px)`, `@media (max-width:767.98px)`, `@media (max-width:991.98px)`
- **Corner Radii**: `50%`, `0px`, `8px`, `5px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `DLYP`
- **Body Font Stack**: `DLYP`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`font-size: 26px`, `line-height: 32px`, `letter-spacing: -.78px`)
- **H2 Section Rule**: live computed `h2` (`font-size: 16px`, `line-height: 38px`, `font-weight: 400`, `letter-spacing: -0.64px`); rule `h2` (`font-size: 22px`, `line-height: 30px`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 18.4px`, `font-weight: 400`); rule `p` (`font-size: 14px`, `line-height: 20px`, `letter-spacing: -.02em`, `font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 18.4px`, `font-weight: 400`); rule `small` (`font-size: calc(var(--kl-reviews-reviews...`, `font-weight: var(--kl-revi...`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `deadlyponies-com` (`Deadly Ponies - Luxury Leather Bags & Accessories`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header> — `deadlyponies-com`)**:
   - DOM & Selectors: Landmark `<header class="header header--dark">` (`1440x83px`) hosting `Deadly Ponies - Luxury Leather Bags ` navigation (`Bags · New Arrivals · View All · Tote Bags · Shoulder Bags`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shop-id="71218823442"`, `data-venmo-supported="false"`, `data-environment="production"`), and stylesheet rule `root { --swiper-theme-color:007aff }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header> — `deadlyponies-com`)` (`deadlyponies-com`) adapts across `@media (min-width:992px)`, `@media (max-width:575.98px)`, `@media (max-width:767.98px)`, `@media (max-width:991.98px)` with `cubic-bezier(0.5,0,0.5,1)`, `cubic-bezier(0.4,0,0.2,1)` transitions and links `Bags · New Arrivals · View All · Tote Bags · Shoulder Bags`.
2. **Hero Stage & Focal Lead (<section.shopify-section> — `Transparency`)**:
   - DOM & Selectors: Landmark `<section class="shopify-section content-section">` presenting display lead `Transparency` and copy excerpt *"Deadly Ponies’ tiered loyalty programme with bespoke gifting and "* over `#f0efeb` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#f0efeb` background with `#000000` headline `Transparency`.
3. **Primary Showcase & Content Grid (<section.content-section> — `Find your local`)**:
   - DOM & Selectors: Landmark `<section class="shopify-section content-section">` rendering section `Find your local` with copy *"A commitment to responsible materials, thoughtful craft, and piec"*, asset references (`93837`, `loader.js`, `01H2CKQHWBM22V9RBNTG4KH275`, `swym-ext-shopify.js`), and grid rule `swiper-container { margin-left:auto;margin-right:auto;position:relative;overflow:hidden;lis... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.content-section> — `Find your local`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 2rem`) on desktop and Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.section--hero_v2> — `Express Shipping`)**:
   - DOM & Selectors: Landmark `<section class="shopify-section content-section">` framing `Express Shipping` and `Find in store` (*"Our stores provide a serene space to live and breathe the magic t"*) with `#f9f9f7` surface cards, `#084ccc` accents, and `.swiper-vertical>.swiper-wrapper { flex-direction:column }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.section--hero_v2> — `Express Shipping`)` uses `50%`, `0px`, `8px`, `5px` radii, `#084ccc` highlights, and assets (93837, loader.js, 01H2CKQHWBM22V9RBNTG4KH275).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://deadlyponies.com`)**:
   - DOM & Selectors: Landmark `<footer class="footer">` anchoring `Deadly Ponies - Luxury Leather B` footer links (`Bags · New Arrivals · View All · Tote Bags · Shoulder Bags`), copy *"Discover our Journal - a space for collections, creativity, "*, and `#dadada` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://deadlyponies.com`)` aligns to `1440px` (non-`@media` desktop container stylesheet rule) with `1rem` lateral canvas padding with `2rem` grid gap and attributes (data-source-attribution="shopify.exit_intersti...", data-shop-id="71218823442", data-venmo-supported="false").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Deadly Ponies’ tiered loyalty programme with bespoke gifting and early access."*
- Copy Excerpt 2: *"A commitment to responsible materials, thoughtful craft, and pieces made to endure."*
- Copy Excerpt 3: *"Our stores provide a serene space to live and breathe the magic that is Deadly Pon..."*
- Copy Excerpt 4: *"Discover our Journal - a space for collections, creativity, and inspiration."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.5,0,0.5,1)`, `cubic-bezier(0.4,0,0.2,1)`
- **Extracted Stylesheet Rules (`deadlyponies-com`)**:
- `root { --swiper-theme-color:007aff }`
- `swiper-container { margin-left:auto;margin-right:auto;position:relative;overflow:hidden;lis... }`
- `.swiper-vertical>.swiper-wrapper { flex-direction:column }`
- `.swiper-wrapper { transform:translate3d(0px,0,0) }`
- `.swiper-horizontal { touch-action:pan-y }`
- **Per-Selector Transition Rules**:
- **Selector `.swiper-wrapper`**: `transition: var(--swiper-wrapper-transition-timing-function,initial)` extracted from `deadlyponies-com` stylesheet.
- **Selector `.swiper-pagination`**: `transition: .3s opacity` extracted from `deadlyponies-com` stylesheet.
- **Selector `n-bullets-dynamic .swiper-paginat...`**: `transition: .2s transform,.2s top` extracted from `deadlyponies-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.5,0,0.5,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.content-section>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `deadlyponies-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
