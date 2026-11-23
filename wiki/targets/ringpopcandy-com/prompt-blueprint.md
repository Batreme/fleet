---
title: "UI Prompt Blueprint: ringpopcandy-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "ringpopcandy-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#fff7e9` canvas, `#141723` ink, `#ff8300` accent)"
---

# UI Design System & Master Generation Blueprint: ringpopcandy-com

> **Ring Pop® — Candy for Every Celebration** (https://ringpopcandy.com/) — Ring Pop turns any occasion into a celebration: birthdays, weddings, game days, wins. Shop the collections and find Ring Pop at a store n...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Ring Pop® — Candy for Every Celebration** (`https://ringpopcandy.com/`). Ring Pop turns any occasion into a celebration: birthdays, weddings, game days, wins. Shop the collections and find Ring Pop at a store n...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#fff7e9` canvas, `#141723` ink, `#ff8300` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#fff7e9` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#141723` primary typography and `#ff8300` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Ringold` for display copy (`RING POP`) with `Greed Standard` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: .75rem`, padding `.75rem`) with `cubic-bezier(.5,0,0,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1440px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `.75rem` lateral canvas padding with `.75rem` grid gap.
- **Border Radius Scale**: `var(--header-border-radius-desktop)`, `.8125rem`, `var(--header-border-radius-sticky-mobile)`, `var(--header-border-radius-sticky-desktop)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: .75rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.75rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media print,screen and (min-width:64em)`, `@media print,screen and (max-width:63.99875em)`, `@media print,screen and (max-width:63.99875em)and (min-width:64em)`, `@media screen and (pointer:fine)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fff7e9` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#141723` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#fffaf6` | `var(--header-bg-color-sticky)` in `:root` |
| **Interactive Accent / Highlight** | `#ff8300` | `var(--oke-filter-searchHighlightColor)` in `:root` |
| **Secondary / Muted Copy** | `#ff8300` | `var(--oke-text-secondaryColor)` in `:root` |
| **Structural Hairline Border** | `#fcfcfc` | `var(--section-primary-button-border)` in `:root` |
| **Variable Token (`--color-accent`)** | `#b98c40` | `var(--color-accent)` in `:root` |
| **Variable Token (`--color-accent-hover`)** | `#936f33` | `var(--color-accent-hover)` in `:root` |
| **Variable Token (`--color-accent-2`)** | `#ff91b7` | `var(--color-accent-2)` in `:root` |
| **Variable Token (`--color-accent-2-darker`)** | `#ff5e96` | `var(--color-accent-2-darker)` in `:root` |
| **Variable Token (`--color-accent-3`)** | `#ff2b0f` | `var(--color-accent-3)` in `:root` |
| **Variable Token (`--color-accent-3-darker`)** | `#db1a00` | `var(--color-accent-3-darker)` in `:root` |
| **Variable Token (`--color-accent-4`)** | `#3e52ce` | `var(--color-accent-4)` in `:root` |
| **Variable Token (`--color-accent-4-darker`)** | `#2c3ead` | `var(--color-accent-4-darker)` in `:root` |
| **Variable Token (`--color-white`)** | `#ffffff` | `var(--color-white)` in `:root` |
| **Variable Token (`--color-off-white`)** | `#f5f4f3` | `var(--color-off-white)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--brand-color` | `#141723` | Brand / Palette Token |
| `--color-accent` | `#B98C40` | Brand / Palette Token |
| `--color-accent-alpha` | `rgba(185, 140, 64, 0.08)` | Brand / Palette Token |
| `--color-accent-hover` | `#936f33` | Brand / Palette Token |
| `--color-accent-2` | `#FF91B7` | Brand / Palette Token |
| `--color-accent-2-darker` | `#ff5e96` | Canvas / Surface Token |
| `--color-accent-3` | `#ff2b0f` | Brand / Palette Token |
| `--color-accent-3-darker` | `#db1a00` | Canvas / Surface Token |
| `--color-accent-4` | `#3e52ce` | Brand / Palette Token |
| `--color-accent-4-darker` | `#2c3ead` | Canvas / Surface Token |
| `--color-body-text` | `#141723` | Typography Ink Token |
| `--color-body-text-alpha` | `rgba(20, 23, 35, 0.5)` | Typography Ink Token |
| `--color-white` | `#ffffff` | Canvas / Surface Token |
| `--color-off-white` | `#f5f4f3` | Canvas / Surface Token |
| `--color-black` | `#141723` | Canvas / Surface Token |
| `--grid-container-padding-mobile` | `25px` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Ringold`.
- **Primary Body Stack**: `Greed Standard`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 250px`, `line-height: 213px`, `font-weight: 400`, `letter-spacing: -5px`); CSS variables `--font-heading-h1: 'Ringold', Helvetica, Arial, sans-serif`, `--font-heading-h1-weight: 400`, `--h1-font-case: uppercase`; rule `,h1` (`font-size: var(--font-heading-h1-size-mo...`, `line-height: var(--font-heading-h1...`, `letter-spacing: var(--font-heading-h1...`, `font-weight: var(--font-he...`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 120px`, `line-height: 100px`, `font-weight: 400`, `letter-spacing: -2.4px`); CSS variables `--font-heading-h2: 'Ringold', Helvetica, Arial, sans-serif`, `--font-heading-h2-weight: 400`, `--h2-font-case: uppercase`; rule `,h2` (`font-size: var(--font-heading-h2-size-mo...`, `line-height: var(--font-heading-h2...`, `letter-spacing: var(--font-heading-h2...`, `font-weight: var(--font-he...`).
- **Body Copy**: live computed `body` (`font-size: 20px`, `line-height: 26px`, `font-weight: 400`); CSS variables `--font-body: 'Greed Standard', Helvetica, Arial, sans-serif`, `--font-body-size-xsmall: 14px`, `--font-body-size-small: 18px`; rule `p` (`font-size: inherit`, `line-height: inherit`, `letter-spacing: inherit`, `font-weight: inherit`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 19px`, `line-height: 30px`, `font-weight: 400`); CSS variables `--font-heading-small-title: 'Greed Standard', Helvetica, Arial, sans-serif`, `--font-heading-small-title-weight: 900`, `--small_title-font-case: uppercase`; rule `.label` (`font-size: 1.5rem`, `line-height: 1.083em`, `letter-spacing: -.0225rem`, `font-weight: 600`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.5,0,0,1)`, `cubic-bezier(.65,.49,.21,.98)`, `cubic-bezier(0,.96,.4,.93)`.

### Per-Element Transition & Choreography Rules
- **Selector `header.header .header__inner`**: `transition: .4s all cubic-bezier(.5,0,0,1)` extracted from `ringpopcandy-com` stylesheet.
- **Selector `header.header .header__right-cta-...`**: `transition: all .4s cubic-bezier(.5,0,0,1)` extracted from `ringpopcandy-com` stylesheet.
- **Selector `header.header .header__wrapper`**: `transition: .4s all cubic-bezier(.5,0,0,1)` extracted from `ringpopcandy-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.5,0,0,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.mfr-core__banner-with-box>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Ring Pop® — Candy for Every Celebration    │
│ ====================================================================== │
│ [ <header.header> (1440x142px)        | Products · Explore · About   ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.mfr-core__hero-section> (w=1440px)            | │
│ | H1: RING POP                                                       | │
│ | Substrate: #fff7e9 | Ink: #141723 | Accent: #ff8300                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.mfr-core__banner-) max-w: 1440px           | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Ring Pop                     |  | A little Bling to Celebrate  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.mfr-core__scrolli) — The Sweetest Way To S | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>     ) | https://ringpopcandy.com/            │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .75rem)     │
│ ====================================================================== │
│ [ HEADER BAR (<header.header>         ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.mfr-core__hero-) — 390px Vertical Lead        | │
│ | H1: RING POP                                                       | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.mfr-core__ban) — 1-Col Stack              | │
│ | [ Item 1: Ring Pop                                               ] | │
│ | [ Item 2: A little Bling to Celebrate Your Thing                 ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.mfr-core__scrol) — 1-Col (The Sweetest Way T) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>     ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.header> — `ringpopcandy-com`)**:
   - Landmark `<header class="header is-inview">` (`1440x142px`) hosting `Ring Pop® — Candy for Every Celebrat` navigation (`Products · Explore · About`), DOM attributes (`data-toggler=".is-fixed"`, `data-id="CGMRQMBC77UCKR5263C0"`, `data-ot-ignore`, `data-source-attribution="shopify.exit_intersti..."`), and stylesheet rule `header.header { position:fixed;top:0;left:0;width:100%;z-index:100 }`.
2. **Hero Stage & Focal Lead (<section.mfr-core__hero-section> — `RING POP`)**:
   - Landmark `<section class="mfr-core__hero-section rendered">` presenting display lead `RING POP` and copy excerpt *"Explore Collections"* over `#fff7e9` canvas and `#141723` ink.
3. **Primary Showcase & Content Grid (<section.mfr-core__banner-with-box> — `Ring Pop`)**:
   - Landmark `<section class="mfr-core__banner-with-box grid-gutter-mobile">` rendering section `Ring Pop` with copy *"Made for every moment"*, asset references (`identify_f7846436.js`, `main.MTUyMzg1YjAxOQ.js`, `main.140d4362.js`, `events.js`), and grid rule `o.has-sticky-logo .header-logo__d... { display:none }`.
4. **Interactive Detail & Feature Matrix (<section.mfr-core__scrolling-bar> — `A little Bling to Celebrate Your T`)**:
   - Landmark `<section class="mfr-core__scrolling-bar">` framing `A little Bling to Celebrate Your Thing` and `The Sweetest Way To Say Yes!` (*"Ring Pop x Mindy Weiss"*) with `#fffaf6` surface cards, `#ff8300` accents, and `go.has-sticky-logo .header-logo__... { display:block }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://ringpopcandy.com/`)**:
   - Landmark `<footer class="footer">` anchoring `Ring Pop® — Candy for Every Cele` footer links (`Products · Explore · About`), copy *"Perfect for engagements, bridal showers, bachelorettes & wed"*, and `#fcfcfc` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: ringpopcandy-com (Ring Pop® — Candy for Every Celebration)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `ringpopcandy-com` (**Ring Pop® — Candy for Every Celebration** — `https://ringpopcandy.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff7e9` canvas, `#141723` ink, `#ff8300` accent).
- **Identity & Domain Context**: Ring Pop turns any occasion into a celebration: birthdays, weddings, game days, wins. Shop the collections and find Ring Pop at a store n...
- **Primary Substrate**: `#fff7e9` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#141723`, **Accent / Highlight**: `#ff8300`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#fff7e9` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#141723` primary typography and `#ff8300` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Ringold` for display copy (`RING POP`) with `Greed Standard` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: .75rem`, padding `.75rem`) with `cubic-bezier(.5,0,0,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `ringpopcandy-com` in your global stylesheet:

:root {
  /* Ring Pop® — Candy for Every Celebration (ringpopcandy-com) — Live-Grounded CSS Variables */
  --brand-color: #141723; /* Brand / Palette Token (ringpopcandy-com) */
  --color-accent: #B98C40; /* Brand / Palette Token (ringpopcandy-com) */
  --color-accent-alpha: rgba(185, 140, 64, 0.08); /* Brand / Palette Token (ringpopcandy-com) */
  --color-accent-hover: #936f33; /* Brand / Palette Token (ringpopcandy-com) */
  --color-accent-2: #FF91B7; /* Brand / Palette Token (ringpopcandy-com) */
  --color-accent-2-darker: #ff5e96; /* Canvas / Surface Token (ringpopcandy-com) */
  --color-accent-3: #ff2b0f; /* Brand / Palette Token (ringpopcandy-com) */
  --color-accent-3-darker: #db1a00; /* Canvas / Surface Token (ringpopcandy-com) */
  --color-accent-4: #3e52ce; /* Brand / Palette Token (ringpopcandy-com) */
  --color-accent-4-darker: #2c3ead; /* Canvas / Surface Token (ringpopcandy-com) */
  --color-body-text: #141723; /* Typography Ink Token (ringpopcandy-com) */
  --color-body-text-alpha: rgba(20, 23, 35, 0.5); /* Typography Ink Token (ringpopcandy-com) */
  --color-white: #ffffff; /* Canvas / Surface Token (ringpopcandy-com) */
  --color-off-white: #f5f4f3; /* Canvas / Surface Token (ringpopcandy-com) */
  --color-black: #141723; /* Canvas / Surface Token (ringpopcandy-com) */
  --grid-container-padding-mobile: 25px; /* Layout / Spatial Grid Token (ringpopcandy-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fff7e9` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#141723` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#fffaf6` — grounded in `var(--header-bg-color-sticky)` in `:root`
- **Interactive Accent / Highlight**: `#ff8300` — grounded in `var(--oke-filter-searchHighlightColor)` in `:root`
- **Secondary / Muted Copy**: `#ff8300` — grounded in `var(--oke-text-secondaryColor)` in `:root`
- **Structural Hairline Border**: `#fcfcfc` — grounded in `var(--section-primary-button-border)` in `:root`
- **Variable Token (`--color-accent`)**: `#b98c40` — grounded in `var(--color-accent)` in `:root`
- **Variable Token (`--color-accent-hover`)**: `#936f33` — grounded in `var(--color-accent-hover)` in `:root`
- **Variable Token (`--color-accent-2`)**: `#ff91b7` — grounded in `var(--color-accent-2)` in `:root`
- **Variable Token (`--color-accent-2-darker`)**: `#ff5e96` — grounded in `var(--color-accent-2-darker)` in `:root`
- **Variable Token (`--color-accent-3`)**: `#ff2b0f` — grounded in `var(--color-accent-3)` in `:root`
- **Variable Token (`--color-accent-3-darker`)**: `#db1a00` — grounded in `var(--color-accent-3-darker)` in `:root`
- **Variable Token (`--color-accent-4`)**: `#3e52ce` — grounded in `var(--color-accent-4)` in `:root`
- **Variable Token (`--color-accent-4-darker`)**: `#2c3ead` — grounded in `var(--color-accent-4-darker)` in `:root`
- **Variable Token (`--color-white`)**: `#ffffff` — grounded in `var(--color-white)` in `:root`
- **Variable Token (`--color-off-white`)**: `#f5f4f3` — grounded in `var(--color-off-white)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1440px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `.75rem` lateral canvas padding with `.75rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: .75rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.75rem` horizontal padding
- **Media Queries**: `@media print,screen and (min-width:64em)`, `@media print,screen and (max-width:63.99875em)`, `@media print,screen and (max-width:63.99875em)and (min-width:64em)`, `@media screen and (pointer:fine)`
- **Corner Radii**: `var(--header-border-radius-desktop)`, `.8125rem`, `var(--header-border-radius-sticky-mobile)`, `var(--header-border-radius-sticky-desktop)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Ringold`
- **Body Font Stack**: `Greed Standard`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 250px`, `line-height: 213px`, `font-weight: 400`, `letter-spacing: -5px`); CSS variables `--font-heading-h1: 'Ringold', Helvetica, Arial, sans-serif`, `--font-heading-h1-weight: 400`, `--h1-font-case: uppercase`; rule `,h1` (`font-size: var(--font-heading-h1-size-mo...`, `line-height: var(--font-heading-h1...`, `letter-spacing: var(--font-heading-h1...`, `font-weight: var(--font-he...`)
- **H2 Section Rule**: live computed `h2` (`font-size: 120px`, `line-height: 100px`, `font-weight: 400`, `letter-spacing: -2.4px`); CSS variables `--font-heading-h2: 'Ringold', Helvetica, Arial, sans-serif`, `--font-heading-h2-weight: 400`, `--h2-font-case: uppercase`; rule `,h2` (`font-size: var(--font-heading-h2-size-mo...`, `line-height: var(--font-heading-h2...`, `letter-spacing: var(--font-heading-h2...`, `font-weight: var(--font-he...`)
- **Body Copy Rule**: live computed `body` (`font-size: 20px`, `line-height: 26px`, `font-weight: 400`); CSS variables `--font-body: 'Greed Standard', Helvetica, Arial, sans-serif`, `--font-body-size-xsmall: 14px`, `--font-body-size-small: 18px`; rule `p` (`font-size: inherit`, `line-height: inherit`, `letter-spacing: inherit`, `font-weight: inherit`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 19px`, `line-height: 30px`, `font-weight: 400`); CSS variables `--font-heading-small-title: 'Greed Standard', Helvetica, Arial, sans-serif`, `--font-heading-small-title-weight: 900`, `--small_title-font-case: uppercase`; rule `.label` (`font-size: 1.5rem`, `line-height: 1.083em`, `letter-spacing: -.0225rem`, `font-weight: 600`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `ringpopcandy-com` (`Ring Pop® — Candy for Every Celebration`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header> — `ringpopcandy-com`)**:
   - DOM & Selectors: Landmark `<header class="header is-inview">` (`1440x142px`) hosting `Ring Pop® — Candy for Every Celebrat` navigation (`Products · Explore · About`), DOM attributes (`data-toggler=".is-fixed"`, `data-id="CGMRQMBC77UCKR5263C0"`, `data-ot-ignore`, `data-source-attribution="shopify.exit_intersti..."`), and stylesheet rule `header.header { position:fixed;top:0;left:0;width:100%;z-index:100 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header> — `ringpopcandy-com`)` (`ringpopcandy-com`) adapts across `@media print,screen and (min-width:64em)`, `@media print,screen and (max-width:63.99875em)`, `@media print,screen and (max-width:63.99875em)and (min-width:64em)`, `@media screen and (pointer:fine)` with `cubic-bezier(.5,0,0,1)`, `cubic-bezier(.65,.49,.21,.98)`, `cubic-bezier(0,.96,.4,.93)` transitions and links `Products · Explore · About`.
2. **Hero Stage & Focal Lead (<section.mfr-core__hero-section> — `RING POP`)**:
   - DOM & Selectors: Landmark `<section class="mfr-core__hero-section rendered">` presenting display lead `RING POP` and copy excerpt *"Explore Collections"* over `#fff7e9` canvas and `#141723` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#fff7e9` background with `#141723` headline `RING POP`.
3. **Primary Showcase & Content Grid (<section.mfr-core__banner-with-box> — `Ring Pop`)**:
   - DOM & Selectors: Landmark `<section class="mfr-core__banner-with-box grid-gutter-mobile">` rendering section `Ring Pop` with copy *"Made for every moment"*, asset references (`identify_f7846436.js`, `main.MTUyMzg1YjAxOQ.js`, `main.140d4362.js`, `events.js`), and grid rule `o.has-sticky-logo .header-logo__d... { display:none }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.mfr-core__banner-with-box> — `Ring Pop`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: .75rem`) on desktop and Single-column vertical stack at `390px` viewport width with `.75rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.mfr-core__scrolling-bar> — `A little Bling to Celebrate Your T`)**:
   - DOM & Selectors: Landmark `<section class="mfr-core__scrolling-bar">` framing `A little Bling to Celebrate Your Thing` and `The Sweetest Way To Say Yes!` (*"Ring Pop x Mindy Weiss"*) with `#fffaf6` surface cards, `#ff8300` accents, and `go.has-sticky-logo .header-logo__... { display:block }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.mfr-core__scrolling-bar> — `A little Bling to Celebrate Your T`)` uses `var(--header-border-radius-desktop)`, `.8125rem`, `var(--header-border-radius-sticky-mobile)`, `var(--header-border-radius-sticky-desktop)` radii, `#ff8300` highlights, and assets (identify_f7846436.js, main.MTUyMzg1YjAxOQ.js, main.140d4362.js).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://ringpopcandy.com/`)**:
   - DOM & Selectors: Landmark `<footer class="footer">` anchoring `Ring Pop® — Candy for Every Cele` footer links (`Products · Explore · About`), copy *"Perfect for engagements, bridal showers, bachelorettes & wed"*, and `#fcfcfc` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://ringpopcandy.com/`)` aligns to `1440px` (non-`@media` desktop container stylesheet rule) with `.75rem` lateral canvas padding with `.75rem` grid gap and attributes (data-toggler=".is-fixed", data-id="CGMRQMBC77UCKR5263C0", data-ot-ignore).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Explore Collections"*
- Copy Excerpt 2: *"Made for every moment"*
- Copy Excerpt 3: *"Ring Pop x Mindy Weiss"*
- Copy Excerpt 4: *"Perfect for engagements, bridal showers, bachelorettes & weddings!"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.5,0,0,1)`, `cubic-bezier(.65,.49,.21,.98)`, `cubic-bezier(0,.96,.4,.93)`
- **Extracted Stylesheet Rules (`ringpopcandy-com`)**:
- `header.header { position:fixed;top:0;left:0;width:100%;z-index:100 }`
- `o.has-sticky-logo .header-logo__d... { display:none }`
- `go.has-sticky-logo .header-logo__... { display:block }`
- `as-mega-menu-logo .header-logo__d... { display:none }`
- `has-mega-menu-logo .header-logo__... { display:none }`
- **Per-Selector Transition Rules**:
- **Selector `header.header .header__inner`**: `transition: .4s all cubic-bezier(.5,0,0,1)` extracted from `ringpopcandy-com` stylesheet.
- **Selector `header.header .header__right-cta-...`**: `transition: all .4s cubic-bezier(.5,0,0,1)` extracted from `ringpopcandy-com` stylesheet.
- **Selector `header.header .header__wrapper`**: `transition: .4s all cubic-bezier(.5,0,0,1)` extracted from `ringpopcandy-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.5,0,0,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.mfr-core__banner-with-box>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `ringpopcandy-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
