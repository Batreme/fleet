---
title: "UI Prompt Blueprint: becore-se"
date: 2026-11-15
target: "[[overview|becore-se]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#1990c6` canvas, `#fff` ink, `#121212` accent)"
---

# UI Design System & Master Generation Blueprint: becore-se

> **Becore** (https://becore.se/) — Experience the latest in activewear from our new Becore collection

![Desktop Viewport Capture (1440x6489)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Becore** (`https://becore.se/`). Experience the latest in activewear from our new Becore collection
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#1990c6` canvas, `#fff` ink, `#121212` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#1990c6` (`.shopify-payment-button__button... { background-color: #1990c6 }`) paired with `#fff` primary typography and `#121212` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Roboto` for display copy (`Cookie consent`) with `Cabin` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `var(--drawer-max-width)` container bounds (`gap: .75rem`, padding `.875rem`) with `cubic-bezier(.19,1,.22,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×6489px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `var(--drawer-max-width)` extracted from `becore-se` stylesheet.
- **Canvas Lateral Padding & Spacing**: `.875rem` lateral canvas padding with `.75rem` grid gap.
- **Border Radius Scale**: `4px`, `var(--button-border-radius)`, `100%`, `20px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--drawer-max-width)`, `gap: .75rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.875rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (forced-colors:active)`, `@media screen and (width<=750px)`, `@media screen and (min-width:700px)`, `@media screen and (pointer:fine)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#1990c6` | `.shopify-payment-button__button... { background-color: #1990c6 }` |
| **Primary Typography Ink** | `#0000` | `pify-payment-button__button.but... { color: #0000 }` |
| **Elevated Surface / Card Substrate** | `#fff` | `on.loading>.loading-overlay__sp... { stroke: #fff }` |
| **Interactive Accent / Highlight** | `#121212` | `.shopify-payment-button__button... { stroke: #121212 }` |
| **Secondary / Muted Copy** | `#1a1a1a` | `.toast__message { background: #1a1a1a }` |
| **Structural Hairline Border** | `#e51c00` | `.toast__message--error { background: #e51c00 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--border-color` | `var(--text-color) / .6` | Brand / Palette Token |
| `--accordion-block-padding` | `.875rem` | Layout / Spatial Grid Token |
| `--accordion-inline-padding` | `0` | Layout / Spatial Grid Token |
| `--button-padding-block` | `.75rem` | Layout / Spatial Grid Token |
| `--button-padding-inline` | `1.5rem` | Layout / Spatial Grid Token |
| `--button-background` | `var(--button-background-primary)` | Canvas / Surface Token |
| `--button-text-color` | `var(--button-text-primary)` | Typography Ink Token |
| `--button-border-color` | `0 0 0 / 0` | Brand / Palette Token |
| `--glowing-shape-width` | `min(40px, 60%)` | Layout / Spatial Grid Token |
| `--button-size` | `1.75rem` | Layout / Spatial Grid Token |
| `--content-box-spacing` | `max(1.5rem, var(--container-gutter))` | Layout / Spatial Grid Token |
| `--scroll-marker-group-gap` | `.3125rem .75rem` | Layout / Spatial Grid Token |
| `--scroll-marker-size` | `.375rem` | Layout / Spatial Grid Token |
| `--scroll-marker-width` | `.5rem` | Layout / Spatial Grid Token |
| `--scroll-marker-height` | `1px` | Layout / Spatial Grid Token |
| `--scroll-marker-group-justify-content` | `start` | Design System Custom Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Roboto`.
- **Primary Body Stack**: `Cabin`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `100%`, `.6875rem`, `.8125rem`, `.625rem`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 120%`, `font-weight: bold`).
- **Body Copy**: CSS variables `--drawer-body-padding-block: min(2rem, var(--container-gutter))`, `--drawer-body-padding-inline: min(2rem, var(--container-gutter))`, `--modal-body-padding-block: 1.25rem`; rule `p` (`line-height: 1.3`).
- **Metadata & Navigation Labels**: CSS variables `--subheading-letter-spacing: -0.01em`, `--heading-letter-spacing: 0.01em`, `--text-letter-spacing: -0.01em`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(.4,0,.22,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.shopify-payment-button__button`**: `transition: background .2s ease-in-out` extracted from `becore-se` stylesheet.
- **Selector `.accordion`**: `transition: color .2s` extracted from `becore-se` stylesheet.
- **Selector `.accordion__summary`**: `transition: color .2s` extracted from `becore-se` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.19,1,.22,1)`)**: Governs interactive state transitions across `<header.hydrated>` and `<section.shopify-section>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Becore                                     │
│ ====================================================================== │
│ [ <header.hydrated>        | MOVE · SHOP                            ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.shopify-pc__banner__dialog>                 |   │
│ | H1: Cookie consent                                               |   │
│ | Substrate: #1990c6    | Ink: #fff       | Accent: #121212        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.shopify-section> ) max-w: var(--drawer-m |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Becore                       |  | Cart                         | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .75rem) | │
│ | [<header.hydrated>] -> [<section.shopify-p] -> [<section.shopify-s]  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.shopify-pc__ba) | https://becore.se/                 │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.hydrated> — `becore-se`)**:
   - Landmark `<header class="hydrated">` hosting `Becore` navigation (`MOVE · SHOP`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-locksmith`, `data-styles`, `data-shop-id="85529952592"`), and stylesheet rule `.shopify-payment-button__button--... { visibility:hidden }`.
2. **Hero Stage & Focal Lead (<section.shopify-pc__banner__dialog> — `Cookie consent`)**:
   - Landmark `<section class="shopify-pc__banner__dialog">` presenting display lead `Cookie consent` and copy excerpt *"We and our partners, including Shopify, use cookies and other tec"* over `#1990c6` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.shopify-section> — `Becore`)**:
   - Landmark `<section class="shopify-section shopify-section-group-overlay-group">` rendering section `Becore` with copy *"Manage preferences"*, asset references (`mixpanel-2-latest.min.js`, `jquery-3.6.4.min-dad6fdf250e31dfa...`, `jquery-migrate-3.4.1.min-6a381abc...`, `jquery-ui-1.13.2.widget-32e3429b3...`), and grid rule `opify-payment-button__button--unb... { background-color:1990c6;padding:1em 2em }`.
4. **Interactive Detail & Feature Matrix (<section.shopify-section> — `Cart`)**:
   - Landmark `<section class="shopify-section shopify-section-group-overlay-group">` framing `Cart` and `Favourites ( 0 )` (*"BLACK FRIDAY · 10 CREDITS FOR 2 500 SEK · SHOP NOW"*) with `#fff` surface cards, `#121212` accents, and `ptions.shopify-payment-button__sk... { width:50%;margin-left:25%;margin-right:25%;border-radius:4px!important;h... }`.
5. **Colophon & Global Directory Footer (<footer.shopify-pc__banner__dialog> — `https://becore.se/`)**:
   - Landmark `<footer class="shopify-pc__banner__dialog">` anchoring `Becore` footer links (`MOVE · SHOP`), copy *"Studio Join Membership & credits Gift card FAQ Studio login "*, and `#e51c00` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: becore-se (Becore)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `becore-se` (**Becore** — `https://becore.se/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#1990c6` canvas, `#fff` ink, `#121212` accent).
- **Identity & Domain Context**: Experience the latest in activewear from our new Becore collection
- **Primary Substrate**: `#1990c6` (`.shopify-payment-button__button... { background-color: #1990c6 }`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#121212`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#1990c6` (`.shopify-payment-button__button... { background-color: #1990c6 }`) paired with `#fff` primary typography and `#121212` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Roboto` for display copy (`Cookie consent`) with `Cabin` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `var(--drawer-max-width)` container bounds (`gap: .75rem`, padding `.875rem`) with `cubic-bezier(.19,1,.22,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `becore-se` in your global stylesheet:

:root {
  /* Becore (becore-se) — Ground-Truth Extracted CSS Variables */
  --border-color: var(--text-color) / .6; /* Brand / Palette Token (becore-se) */
  --accordion-block-padding: .875rem; /* Layout / Spatial Grid Token (becore-se) */
  --accordion-inline-padding: 0; /* Layout / Spatial Grid Token (becore-se) */
  --button-padding-block: .75rem; /* Layout / Spatial Grid Token (becore-se) */
  --button-padding-inline: 1.5rem; /* Layout / Spatial Grid Token (becore-se) */
  --button-background: var(--button-background-primary); /* Canvas / Surface Token (becore-se) */
  --button-text-color: var(--button-text-primary); /* Typography Ink Token (becore-se) */
  --button-border-color: 0 0 0 / 0; /* Brand / Palette Token (becore-se) */
  --glowing-shape-width: min(40px, 60%); /* Layout / Spatial Grid Token (becore-se) */
  --button-size: 1.75rem; /* Layout / Spatial Grid Token (becore-se) */
  --content-box-spacing: max(1.5rem, var(--container-gutter)); /* Layout / Spatial Grid Token (becore-se) */
  --scroll-marker-group-gap: .3125rem .75rem; /* Layout / Spatial Grid Token (becore-se) */
  --scroll-marker-size: .375rem; /* Layout / Spatial Grid Token (becore-se) */
  --scroll-marker-width: .5rem; /* Layout / Spatial Grid Token (becore-se) */
  --scroll-marker-height: 1px; /* Layout / Spatial Grid Token (becore-se) */
  --scroll-marker-group-justify-content: start; /* Design System Custom Token (becore-se) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#1990c6` — grounded in `.shopify-payment-button__button... { background-color: #1990c6 }`
- **Primary Typography Ink**: `#0000` — grounded in `pify-payment-button__button.but... { color: #0000 }`
- **Elevated Surface / Card Substrate**: `#fff` — grounded in `on.loading>.loading-overlay__sp... { stroke: #fff }`
- **Interactive Accent / Highlight**: `#121212` — grounded in `.shopify-payment-button__button... { stroke: #121212 }`
- **Secondary / Muted Copy**: `#1a1a1a` — grounded in `.toast__message { background: #1a1a1a }`
- **Structural Hairline Border**: `#e51c00` — grounded in `.toast__message--error { background: #e51c00 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×6489px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `var(--drawer-max-width)` extracted from `becore-se` stylesheet
- **Padding & Gutters**: `.875rem` lateral canvas padding with `.75rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--drawer-max-width)`, `gap: .75rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.875rem` horizontal padding
- **Media Queries**: `@media screen and (forced-colors:active)`, `@media screen and (width<=750px)`, `@media screen and (min-width:700px)`, `@media screen and (pointer:fine)`
- **Corner Radii**: `4px`, `var(--button-border-radius)`, `100%`, `20px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Roboto`
- **Body Font Stack**: `Cabin`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `100%`, `.6875rem`, `.8125rem`, `.625rem`)
- **H2 Section Rule**: rule `h2` (`font-size: 120%`, `font-weight: bold`)
- **Body Copy Rule**: CSS variables `--drawer-body-padding-block: min(2rem, var(--container-gutter))`, `--drawer-body-padding-inline: min(2rem, var(--container-gutter))`, `--modal-body-padding-block: 1.25rem`; rule `p` (`line-height: 1.3`)
- **Metadata & Index Rule**: CSS variables `--subheading-letter-spacing: -0.01em`, `--heading-letter-spacing: 0.01em`, `--text-letter-spacing: -0.01em`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `becore-se` (`Becore`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.hydrated> — `becore-se`)**:
   - DOM & Selectors: Landmark `<header class="hydrated">` hosting `Becore` navigation (`MOVE · SHOP`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-locksmith`, `data-styles`, `data-shop-id="85529952592"`), and stylesheet rule `.shopify-payment-button__button--... { visibility:hidden }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.hydrated> — `becore-se`)` (`becore-se`) adapts across `@media screen and (forced-colors:active)`, `@media screen and (width<=750px)`, `@media screen and (min-width:700px)`, `@media screen and (pointer:fine)` with `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(.4,0,.22,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `MOVE · SHOP`.
2. **Hero Stage & Focal Lead (<section.shopify-pc__banner__dialog> — `Cookie consent`)**:
   - DOM & Selectors: Landmark `<section class="shopify-pc__banner__dialog">` presenting display lead `Cookie consent` and copy excerpt *"We and our partners, including Shopify, use cookies and other tec"* over `#1990c6` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×6489px` desktop / `390×2400px` mobile) sets `#1990c6` background with `#fff` headline `Cookie consent`.
3. **Primary Showcase & Content Grid (<section.shopify-section> — `Becore`)**:
   - DOM & Selectors: Landmark `<section class="shopify-section shopify-section-group-overlay-group">` rendering section `Becore` with copy *"Manage preferences"*, asset references (`mixpanel-2-latest.min.js`, `jquery-3.6.4.min-dad6fdf250e31dfa...`, `jquery-migrate-3.4.1.min-6a381abc...`, `jquery-ui-1.13.2.widget-32e3429b3...`), and grid rule `opify-payment-button__button--unb... { background-color:1990c6;padding:1em 2em }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.shopify-section> — `Becore`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--drawer-max-width)`, `gap: .75rem`) on desktop and Single-column vertical stack at `390px` viewport width with `.875rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.shopify-section> — `Cart`)**:
   - DOM & Selectors: Landmark `<section class="shopify-section shopify-section-group-overlay-group">` framing `Cart` and `Favourites ( 0 )` (*"BLACK FRIDAY · 10 CREDITS FOR 2 500 SEK · SHOP NOW"*) with `#fff` surface cards, `#121212` accents, and `ptions.shopify-payment-button__sk... { width:50%;margin-left:25%;margin-right:25%;border-radius:4px!important;h... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.shopify-section> — `Cart`)` uses `4px`, `var(--button-border-radius)`, `100%`, `20px` radii, `#121212` highlights, and assets (mixpanel-2-latest.min.js, jquery-3.6.4.min-dad6fdf250e31dfa..., jquery-migrate-3.4.1.min-6a381abc...).
5. **Colophon & Global Directory Footer (<footer.shopify-pc__banner__dialog> — `https://becore.se/`)**:
   - DOM & Selectors: Landmark `<footer class="shopify-pc__banner__dialog">` anchoring `Becore` footer links (`MOVE · SHOP`), copy *"Studio Join Membership & credits Gift card FAQ Studio login "*, and `#e51c00` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.shopify-pc__banner__dialog> — `https://becore.se/`)` aligns to `var(--drawer-max-width)` extracted from `becore-se` stylesheet with `.875rem` lateral canvas padding with `.75rem` grid gap and attributes (data-source-attribution="shopify.exit_intersti...", data-locksmith, data-styles).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"We and our partners, including Shopify, use cookies and other technologies to pers..."*
- Copy Excerpt 2: *"Manage preferences"*
- Copy Excerpt 3: *"BLACK FRIDAY · 10 CREDITS FOR 2 500 SEK · SHOP NOW"*
- Copy Excerpt 4: *"Studio Join Membership & credits Gift card FAQ Studio login Classes Signature Mat..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(.4,0,.22,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`becore-se`)**:
- `.shopify-payment-button__button--... { visibility:hidden }`
- `opify-payment-button__button--unb... { background-color:1990c6;padding:1em 2em }`
- `ptions.shopify-payment-button__sk... { width:50%;margin-left:25%;margin-right:25%;border-radius:4px!important;h... }`
- `shopify-payment-button__button--b... { z-index:1;flex-direction:column;display:flex;position:relative }`
- `on__button--branded .shopify-clea... { flex-direction:column!important;flex:1!important;display:flex!important }`
- **Per-Selector Transition Rules**:
- **Selector `.shopify-payment-button__button`**: `transition: background .2s ease-in-out` extracted from `becore-se` stylesheet.
- **Selector `.accordion`**: `transition: color .2s` extracted from `becore-se` stylesheet.
- **Selector `.accordion__summary`**: `transition: color .2s` extracted from `becore-se` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.19,1,.22,1)`)**: Governs interactive state transitions across `<header.hydrated>` and `<section.shopify-section>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `becore-se`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
