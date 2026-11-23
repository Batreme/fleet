---
title: "UI Prompt Blueprint: southandstonestudio-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "southandstonestudio-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#ff0000`)"
---

# UI Design System & Master Generation Blueprint: southandstonestudio-com

> **South & Stone Studio · Web Design & Brand Identity** (http://southandstonestudio.com) — Websites written and built by Kelli Covey, a novelist and designer. Custom sites and brand identities for small businesses, with prices p...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **South & Stone Studio · Web Design & Brand Identity** (`http://southandstonestudio.com`). Websites written and built by Kelli Covey, a novelist and designer. Custom sites and brand identities for small businesses, with prices p...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#ff0000`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#ff0000` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Archivo` for display copy (`Every website has a better version.`) with `Geist` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1180px` container bounds (`gap: 2px`, padding `14px`) with `cubic-bezier(.65,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1180px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `14px` lateral canvas padding with `2px` grid gap.
- **Border Radius Scale**: `3px`, `16px`, `8px`, `12px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1180px`, `gap: 2px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `14px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width: 768px)`, `@media only screen and (min-width:768px)`, `@media (min-width:768px)`, `@media (min-width:1200px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#673de6` | `.hostinger-reach-block-dialog__... { background: #673de6 }` |
| **Interactive Accent / Highlight** | `#ff0000` | `.sx-fst-ctas a:first-child { background: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#7a7a7a` | `var(--e-global-color-text)` in `:root` |
| **Structural Hairline Border** | `#252422` | `var(--sx-line-d)` in `:root` (`rgba(232,225,211,.16)`) |
| **Variable Token (`--edd-blocks-light-grey`)** | `#eeeeee` | `var(--edd-blocks-light-grey)` in `:root` |
| **Variable Token (`--sx-raise`)** | `#121212` | `var(--sx-raise)` in `:root` |
| **Variable Token (`--sx-bone`)** | `#e8e1d3` | `var(--sx-bone)` in `:root` |
| **Variable Token (`--sx-bone-2`)** | `#dcd3c1` | `var(--sx-bone-2)` in `:root` |
| **Variable Token (`--sx-red`)** | `#e1251b` | `var(--sx-red)` in `:root` |
| **Variable Token (`--sx-red-ink`)** | `#b3170f` | `var(--sx-red-ink)` in `:root` |
| **Variable Token (`--sx-red-lit`)** | `#ff5146` | `var(--sx-red-lit)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--edd-blocks-light-grey` | `#eee` | Canvas / Surface Token |
| `--wp--style--global--content-size` | `800px` | Layout / Spatial Grid Token |
| `--wp--style--global--wide-size` | `1200px` | Layout / Spatial Grid Token |
| `--wp--style--block-gap` | `24px` | Layout / Spatial Grid Token |
| `--direction-multiplier` | `1` | Design System Custom Token |
| `--page-title-display` | `block` | Design System Custom Token |
| `--sx-serif` | `"Instrument Serif",Georgia,"Times New Roman",serif` | Typography / Scale Token |
| `--sx-hand` | `"Caveat","Segoe Print","Bradley Hand",cursive` | Design System Custom Token |
| `--sx-black` | `#000` | Canvas / Surface Token |
| `--sx-raise` | `#121212` | Color / Atmospheric Token |
| `--sx-bone` | `#E8E1D3` | Color / Atmospheric Token |
| `--sx-bone-2` | `#DCD3C1` | Color / Atmospheric Token |
| `--sx-white` | `#fff` | Canvas / Surface Token |
| `--sx-red` | `#E1251B` | Color / Atmospheric Token |
| `--sx-red-ink` | `#B3170F` | Typography Ink Token |
| `--sx-red-lit` | `#FF5146` | Color / Atmospheric Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Archivo`.
- **Primary Body Stack**: `Geist`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 80.64px`, `line-height: 72.576px`, `font-weight: 780`, `letter-spacing: -2.8224px`); CSS variables `--page-title-display: block`, `--display: flex`; rule `h1` (`font-size: clamp(2.7rem,7.6vw,8.2rem)`, `line-height: .92`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 74.88px`, `line-height: 71.136px`, `font-weight: 780`, `letter-spacing: -2.6208px`); rule `h2` (`font-size: clamp(1.5rem,2.4vw,2rem)`, `line-height: 1.1`, `letter-spacing: -.02em`, `font-weight: 760`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: clamp(2rem,5.4vw,5.2rem)`, `line-height: .98`, `letter-spacing: -.035em`, `font-weight: 780`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `small` (`font-size: .85rem`, `font-weight: 650`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.65,0,.2,1)`, `cubic-bezier(.7,0,.2,1)`, `cubic-bezier(.3,.6,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `stinger-reach-select-form-modal__...`**: `transition: border-color .2s ease` extracted from `southandstonestudio-com` stylesheet.
- **Selector `a.edd-add-to-cart .edd-add-to-car...`**: `transition: opacity .1s!important` extracted from `southandstonestudio-com` stylesheet.
- **Selector `textarea`**: `transition: all .3s` extracted from `southandstonestudio-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.65,0,.2,1)`)**: Governs interactive state transitions across `<header.sx-head>` and `<section.sx-sec>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — South & Stone Studio · Web Design & Brand  │
│ ====================================================================== │
│ [ <header.sx-head> (1440x76px)        | Services · Portfolio · Indus ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.sx-hero> (w=1440px)                           | │
│ | H1: Every website has a better version.                            | │
│ | Substrate: #000000 | Ink: #ffffff | Accent: #ff0000                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.sx-sec>) max-w: 1180px                     | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Booking projects now Written |  | Try the live demo Holloway H | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.sx-fst-band>) — Websites for contract      | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.sx-foot>    ) | http://southandstonestudio.com       │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 2px)        │
│ ====================================================================== │
│ [ HEADER BAR (<header.sx-head>        ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.sx-hero>) — 390px Vertical Lead               | │
│ | H1: Every website has a better version.                            | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.sx-sec>) — 1-Col Stack                    | │
│ | [ Item 1: Booking projects now Written & built by Kelli Co       ] | │
│ | [ Item 2: Try the live demo Holloway Home Repair                 ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.sx-fst-band>) — 1-Col (Websites for contr)  | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.sx-foot>    ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.sx-head> — `southandstonestudio-com`)**:
   - Landmark `<header class="sx-head">` (`1440x76px`) hosting `South & Stone Studio · Web Design & ` navigation (`Services · Portfolio · Industries · Estimate Desk · Shop`), DOM attributes (`data-domain="southandstonestudio.com"`, `data-elementor-device-mode="desktop"`, `data-sx-industry`, `data-trade="contractors"`), and stylesheet rule `.hostinger-reach-block-connect__t... { color:1d1e20;font-weight:700;margin-bottom:4px }`.
2. **Hero Stage & Focal Lead (<section.sx-hero> — `Every website has a better version`)**:
   - Landmark `<section class="sx-hero">` presenting display lead `Every website has a better version.` and copy excerpt *"Booking projects now Written & built by Kelli Covey Fort Myers, F"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.sx-sec> — `Booking projects now Written & bui`)**:
   - Landmark `<section class="sx-sec sx-t-bone">` rendering section `Booking projects now Written & built by Kelli Co` with copy *"Try the live demo Holloway Home Repair"*, asset references (`cdn-reach.hostinger.com`, `js.stripe.com`, `embed`, `south-stone-favicon.png`), and grid rule `hostinger-reach-block-connect__su... { color:727586;margin-bottom:4px }`.
4. **Interactive Detail & Feature Matrix (<section.sx-fst-band> — `Try the live demo Holloway Home Re`)**:
   - Landmark `<section class="sx-fst-band">` framing `Try the live demo Holloway Home Repair` and `Websites for contractors from $1,250` (*"Websites for contractors from $1,250"*) with `#673de6` surface cards, `#ff0000` accents, and `.hostinger-reach-block-connect a { color:rgba(var(--bs-link-color-rgb), var(--bs-link-opacity, 1));text-dec... }`.
5. **Colophon & Global Directory Footer (<footer.sx-foot> — `http://southandstonestudio.com`)**:
   - Landmark `<footer class="sx-foot">` anchoring `South & Stone Studio · Web Desig` footer links (`Services · Portfolio · Industries · Estimate Desk · Shop`), copy *"Eight concept sites see Meridian Contracting"*, and `#252422` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: southandstonestudio-com (South & Stone Studio · Web Design & Brand Identity)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `southandstonestudio-com` (**South & Stone Studio · Web Design & Brand Identity** — `http://southandstonestudio.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#ff0000`).
- **Identity & Domain Context**: Websites written and built by Kelli Covey, a novelist and designer. Custom sites and brand identities for small businesses, with prices p...
- **Primary Substrate**: `#000000` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#ff0000`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#ff0000` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Archivo` for display copy (`Every website has a better version.`) with `Geist` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1180px` container bounds (`gap: 2px`, padding `14px`) with `cubic-bezier(.65,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `southandstonestudio-com` in your global stylesheet:

:root {
  /* South & Stone Studio · Web Design & Brand Identity (southandstonestudio-com) — Live-Grounded CSS Variables */
  --edd-blocks-light-grey: #eee; /* Canvas / Surface Token (southandstonestudio-com) */
  --wp--style--global--content-size: 800px; /* Layout / Spatial Grid Token (southandstonestudio-com) */
  --wp--style--global--wide-size: 1200px; /* Layout / Spatial Grid Token (southandstonestudio-com) */
  --wp--style--block-gap: 24px; /* Layout / Spatial Grid Token (southandstonestudio-com) */
  --direction-multiplier: 1; /* Design System Custom Token (southandstonestudio-com) */
  --page-title-display: block; /* Design System Custom Token (southandstonestudio-com) */
  --sx-serif: "Instrument Serif",Georgia,"Times New Roman",serif; /* Typography / Scale Token (southandstonestudio-com) */
  --sx-hand: "Caveat","Segoe Print","Bradley Hand",cursive; /* Design System Custom Token (southandstonestudio-com) */
  --sx-black: #000; /* Canvas / Surface Token (southandstonestudio-com) */
  --sx-raise: #121212; /* Color / Atmospheric Token (southandstonestudio-com) */
  --sx-bone: #E8E1D3; /* Color / Atmospheric Token (southandstonestudio-com) */
  --sx-bone-2: #DCD3C1; /* Color / Atmospheric Token (southandstonestudio-com) */
  --sx-white: #fff; /* Canvas / Surface Token (southandstonestudio-com) */
  --sx-red: #E1251B; /* Color / Atmospheric Token (southandstonestudio-com) */
  --sx-red-ink: #B3170F; /* Typography Ink Token (southandstonestudio-com) */
  --sx-red-lit: #FF5146; /* Color / Atmospheric Token (southandstonestudio-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000000` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#ffffff` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#673de6` — grounded in `.hostinger-reach-block-dialog__... { background: #673de6 }`
- **Interactive Accent / Highlight**: `#ff0000` — grounded in `.sx-fst-ctas a:first-child { background: red }` (`#ff0000`)
- **Secondary / Muted Copy**: `#7a7a7a` — grounded in `var(--e-global-color-text)` in `:root`
- **Structural Hairline Border**: `#252422` — grounded in `var(--sx-line-d)` in `:root` (`rgba(232,225,211,.16)`)
- **Variable Token (`--edd-blocks-light-grey`)**: `#eeeeee` — grounded in `var(--edd-blocks-light-grey)` in `:root`
- **Variable Token (`--sx-raise`)**: `#121212` — grounded in `var(--sx-raise)` in `:root`
- **Variable Token (`--sx-bone`)**: `#e8e1d3` — grounded in `var(--sx-bone)` in `:root`
- **Variable Token (`--sx-bone-2`)**: `#dcd3c1` — grounded in `var(--sx-bone-2)` in `:root`
- **Variable Token (`--sx-red`)**: `#e1251b` — grounded in `var(--sx-red)` in `:root`
- **Variable Token (`--sx-red-ink`)**: `#b3170f` — grounded in `var(--sx-red-ink)` in `:root`
- **Variable Token (`--sx-red-lit`)**: `#ff5146` — grounded in `var(--sx-red-lit)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1180px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `14px` lateral canvas padding with `2px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1180px`, `gap: 2px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `14px` horizontal padding
- **Media Queries**: `@media (max-width: 768px)`, `@media only screen and (min-width:768px)`, `@media (min-width:768px)`, `@media (min-width:1200px)`
- **Corner Radii**: `3px`, `16px`, `8px`, `12px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 80.64px`, `line-height: 72.576px`, `font-weight: 780`, `letter-spacing: -2.8224px`); CSS variables `--page-title-display: block`, `--display: flex`; rule `h1` (`font-size: clamp(2.7rem,7.6vw,8.2rem)`, `line-height: .92`)
- **H2 Section Rule**: live computed `h2` (`font-size: 74.88px`, `line-height: 71.136px`, `font-weight: 780`, `letter-spacing: -2.6208px`); rule `h2` (`font-size: clamp(1.5rem,2.4vw,2rem)`, `line-height: 1.1`, `letter-spacing: -.02em`, `font-weight: 760`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: clamp(2rem,5.4vw,5.2rem)`, `line-height: .98`, `letter-spacing: -.035em`, `font-weight: 780`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `small` (`font-size: .85rem`, `font-weight: 650`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `southandstonestudio-com` (`South & Stone Studio · Web Design & Brand Identity`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.sx-head> — `southandstonestudio-com`)**:
   - DOM & Selectors: Landmark `<header class="sx-head">` (`1440x76px`) hosting `South & Stone Studio · Web Design & ` navigation (`Services · Portfolio · Industries · Estimate Desk · Shop`), DOM attributes (`data-domain="southandstonestudio.com"`, `data-elementor-device-mode="desktop"`, `data-sx-industry`, `data-trade="contractors"`), and stylesheet rule `.hostinger-reach-block-connect__t... { color:1d1e20;font-weight:700;margin-bottom:4px }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.sx-head> — `southandstonestudio-com`)` (`southandstonestudio-com`) adapts across `@media (max-width: 768px)`, `@media only screen and (min-width:768px)`, `@media (min-width:768px)`, `@media (min-width:1200px)` with `cubic-bezier(.65,0,.2,1)`, `cubic-bezier(.7,0,.2,1)`, `cubic-bezier(.3,.6,.2,1)` transitions and links `Services · Portfolio · Industries · Estimate Desk · Shop`.
2. **Hero Stage & Focal Lead (<section.sx-hero> — `Every website has a better version`)**:
   - DOM & Selectors: Landmark `<section class="sx-hero">` presenting display lead `Every website has a better version.` and copy excerpt *"Booking projects now Written & built by Kelli Covey Fort Myers, F"* over `#000000` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#000000` background with `#ffffff` headline `Every website has a better version.`.
3. **Primary Showcase & Content Grid (<section.sx-sec> — `Booking projects now Written & bui`)**:
   - DOM & Selectors: Landmark `<section class="sx-sec sx-t-bone">` rendering section `Booking projects now Written & built by Kelli Co` with copy *"Try the live demo Holloway Home Repair"*, asset references (`cdn-reach.hostinger.com`, `js.stripe.com`, `embed`, `south-stone-favicon.png`), and grid rule `hostinger-reach-block-connect__su... { color:727586;margin-bottom:4px }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.sx-sec> — `Booking projects now Written & bui`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1180px`, `gap: 2px`) on desktop and Single-column vertical stack at `390px` viewport width with `14px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.sx-fst-band> — `Try the live demo Holloway Home Re`)**:
   - DOM & Selectors: Landmark `<section class="sx-fst-band">` framing `Try the live demo Holloway Home Repair` and `Websites for contractors from $1,250` (*"Websites for contractors from $1,250"*) with `#673de6` surface cards, `#ff0000` accents, and `.hostinger-reach-block-connect a { color:rgba(var(--bs-link-color-rgb), var(--bs-link-opacity, 1));text-dec... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.sx-fst-band> — `Try the live demo Holloway Home Re`)` uses `3px`, `16px`, `8px`, `12px` radii, `#ff0000` highlights, and assets (cdn-reach.hostinger.com, js.stripe.com, embed).
5. **Colophon & Global Directory Footer (<footer.sx-foot> — `http://southandstonestudio.com`)**:
   - DOM & Selectors: Landmark `<footer class="sx-foot">` anchoring `South & Stone Studio · Web Desig` footer links (`Services · Portfolio · Industries · Estimate Desk · Shop`), copy *"Eight concept sites see Meridian Contracting"*, and `#252422` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.sx-foot> — `http://southandstonestudio.com`)` aligns to `1180px` (non-`@media` desktop container stylesheet rule) with `14px` lateral canvas padding with `2px` grid gap and attributes (data-domain="southandstonestudio.com", data-elementor-device-mode="desktop", data-sx-industry).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Booking projects now Written & built by Kelli Covey Fort Myers, FL"*
- Copy Excerpt 2: *"Try the live demo Holloway Home Repair"*
- Copy Excerpt 3: *"Websites for contractors from $1,250"*
- Copy Excerpt 4: *"Eight concept sites see Meridian Contracting"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.65,0,.2,1)`, `cubic-bezier(.7,0,.2,1)`, `cubic-bezier(.3,.6,.2,1)`
- **Extracted Stylesheet Rules (`southandstonestudio-com`)**:
- `.hostinger-reach-block-connect__t... { color:1d1e20;font-weight:700;margin-bottom:4px }`
- `hostinger-reach-block-connect__su... { color:727586;margin-bottom:4px }`
- `.hostinger-reach-block-connect a { color:rgba(var(--bs-link-color-rgb), var(--bs-link-opacity, 1));text-dec... }`
- `.hostinger-reach-block-dialog__ac... { display:flex;justify-content:flex-start;gap:10px }`
- `er-reach-block-dialog__button_ind... { height:16px;width:16px }`
- **Per-Selector Transition Rules**:
- **Selector `stinger-reach-select-form-modal__...`**: `transition: border-color .2s ease` extracted from `southandstonestudio-com` stylesheet.
- **Selector `a.edd-add-to-cart .edd-add-to-car...`**: `transition: opacity .1s!important` extracted from `southandstonestudio-com` stylesheet.
- **Selector `textarea`**: `transition: all .3s` extracted from `southandstonestudio-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.65,0,.2,1)`)**: Governs interactive state transitions across `<header.sx-head>` and `<section.sx-sec>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `southandstonestudio-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
