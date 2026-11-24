---
title: "UI Prompt Blueprint: www-serko-ai"
date: 2026-11-24
captured_at: 2026-11-24
target: "www-serko-ai"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: native
desktop_keyframes: 8
subpages_crawled: 2
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#e8f3fe` / `#0082f3`)"
---

# UI Design System & Master Generation Blueprint: www-serko-ai

> **Serko.ai · AI Travel Agent for Business Trips** (https://www.serko.ai) — Serko.ai is an AI travel agent for work. Book personalized flights and hotels, follow company policy, manage disruptions and cancel with...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Serko.ai · AI Travel Agent for Business Trips** (`https://www.serko.ai`). Serko.ai is an AI travel agent for work. Book personalized flights and hotels, follow company policy, manage disruptions and cancel with...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#e8f3fe` / `#0082f3`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#e8f3fe` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#0082f3` accents.
  - **Grounded Typographic Hierarchy**: Uses `Jokker` across display (`The last travel agent you’ll ever ne`) and body copy.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(0.525,0,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=11188px` / doc `12088px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `9px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `3px`, `100%`, `50%`, `var(--radius--medium)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#e8f3fe` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ebebeb` | `var(--osano-info-dialog-selected-background-color)` in `:root` |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#058a5e` | `var(--osano-gpc-foreground-color)` in `:root` |
| **Structural Hairline Border** | `#d8d8d8` | `var(--osano-info-dialog-border-color)` in `:root` |
| **Variable Token (`--osano-info-dialog-border-subtle-color`)** | `#e9e9e9` | `var(--osano-info-dialog-border-subtle-color)` in `:root` |
| **Variable Token (`--osano-info-dialog-inset-color`)** | `#f4f4f4` | `var(--osano-info-dialog-inset-color)` in `:root` |
| **Variable Token (`--osano-info-dialog-gpc-tint-color`)** | `#e7f9f0` | `var(--osano-info-dialog-gpc-tint-color)` in `:root` |
| **Variable Token (`--osano-button-foreground-color`)** | `#ffffff` | `var(--osano-button-foreground-color)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--osano-clear-dialog-background` | `rgba(0,0,0,0)` | Canvas / Surface Token |
| `--osano-info-dialog-border-color` | `#d8d8d8` | Brand / Palette Token |
| `--osano-info-dialog-border-subtle-color` | `#e9e9e9` | Brand / Palette Token |
| `--osano-info-dialog-inset-color` | `#f4f4f4` | Brand / Palette Token |
| `--osano-info-dialog-selected-background-color` | `#ebebeb` | Canvas / Surface Token |
| `--osano-info-dialog-gpc-tint-color` | `#e7f9f0` | Canvas / Surface Token |
| `--osano-theme` | `modern` | Brand / Palette Token |
| `--osano-button-border-color` | `var(--osano-button-foreground-color)` | Brand / Palette Token |
| `--osano-dialog-type` | `box` | Typography / Scale Token |
| `--osano-display-position` | `"bottom-left"` | Design System Custom Token |
| `--osano-info-dialog-position` | `right` | Design System Custom Token |
| `--osano-widget-position` | `right` | Design System Custom Token |
| `--osano-opt-out-widget-position` | `right` | Design System Custom Token |
| `--osano-button-background-color` | `#000000` | Canvas / Surface Token |
| `--osano-button-foreground-color` | `#FFFFFF` | Typography Ink Token |
| `--osano-dialog-background-color` | `#ffffff` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Jokker`.
- **Primary Body Stack**: `Jokker`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 70.1985px`, `line-height: 70.1985px`, `font-weight: 500`, `letter-spacing: -2.10595px`); CSS variables `--osano-display-position: "bottom-left"`, `--library_typography---font-size--h1: 5.25rem`, `--library_typography---font-size--display: 6rem`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 62.3271px`, `line-height: 62.3271px`, `font-weight: 500`, `letter-spacing: -1.86981px`); CSS variables `--library_typography---font-size--h2: 4rem`.
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 500`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 500`); CSS variables `--library_heading-style---letter-spacing: var(--library_typography---letter-spacing--0em)`, `--library_text-style---letter-spacing: var(--library_typography---letter-spacing--0em)`, `--library_spacing---section-space--small: 5rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.525,0,0,1)`, `cubic-bezier(.22,1.15,.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `www-serko-ai` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `www-serko-ai` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-serko-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.525,0,0,1)`)**: Governs interactive state transitions across `<header.nav1_header>` and `<section.col3_wrap>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `12088px`, deepest scrollY reached `11188px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `Lenis`, `GSAP/ScrollTrigger`, `WebGL/Canvas`.
- **Hover Physics (`primary_cta` · `Join waitlist`)**: Computed transition `0s` / `ease` (no static color/transform shift captured at rest).
- **Interactive Control Probe (`accordion` · `Who is Serko.ai for?`)**: Triggered visual diff `6.559` (attr `false -> true`, captured in `assets/state-interactive.webp`).
- **Route Transition Architecture**: First internal navigation (`/about`) measured as `direct` in `4215ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Serko.ai · AI Travel Agent for Business Tr │
│ ====================================================================== │
│ [ <header.nav1_header> (1440x75px)    | Home · Platform · For compan ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero1_wrap> (w=1440px)                        | │
│ | H1: The last travel agent you’ll ever need.                        | │
│ | Substrate: #e8f3fe | Ink: #000000 | Accent: #0082f3                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.col3_wrap>) max-w: 1440px                  | │
│ | +------------------------------+  +------------------------------+ | │
│ | | AI travel agent for business |  | How Serko.ai works           | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.feature1_wrap>) — Business travel, book    | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.osano-cm-win) | https://www.serko.ai                 │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.nav1_header>    ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.hero1_wrap>) — 390px Vertical Lead            | │
│ | H1: The last travel agent you’ll ever need.                        | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.col3_wrap>) — 1-Col Stack                 | │
│ | [ Item 1: AI travel agent for business                           ] | │
│ | [ Item 2: How Serko.ai works                                     ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.feature1_wrap>) — 1-Col (Business travel, b)  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.osano-cm-win) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.nav1_header> — `www-serko-ai`)**:
   - Landmark `<header class="nav1_header">` (`1440x75px`) hosting `Serko.ai · AI Travel Agent for Busin` navigation (`Home · Platform · For companies · About · Sign up free`), DOM attributes (`data-wf-domain="www.serko.ai"`, `data-wf-page="6aa12b65e6dd0b96a2a83430"`, `data-wf-site="6aa12b65e6dd0b96a2a8345b"`, `data-wf-intellimize-customer-id="117114932"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.hero1_wrap> — `The last travel agent you’ll ever `)**:
   - Landmark `<section class="hero1_wrap u-gradient-bg-1">` presenting display lead `The last travel agent you’ll ever need.` and copy excerpt *"Serko learns how you like to travel, finds the best flights and h"* over `#e8f3fe` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.col3_wrap> — `AI travel agent for business`)**:
   - Landmark `<section class="col3_wrap">` rendering section `AI travel agent for business` with copy *"Venue, location, address..."*, asset references (`cdn.prod.website-files.com`, `serko-ai.webflow.shared.96cab25cb...`, `serko-ai.webflow.6aa12b65e6dd0b96...`, `clientParamBuilder.bundle.js`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.feature1_wrap> — `How Serko.ai works`)**:
   - Landmark `<section class="feature1_wrap u-background-3">` framing `How Serko.ai works` and `Business travel, booked in one chat.` (*"Trip details and preferences"*) with `#ebebeb` surface cards, `#0082f3` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.osano-cm-window> — `https://www.serko.ai`)**:
   - Landmark `<footer class="osano-cm-window">` anchoring `Serko.ai · AI Travel Agent for B` footer links (`Home · Platform · For companies · About · Sign up free`), copy *"Whether you’ve got a big client meeting in New York this Fri"*, and `#d8d8d8` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `The last travel agent you’ll ever need.` · sticky/fixed elements: `2`
- **Step 02** (`y=850px`, `8%`): Active landmark `How Serko.ai works` · sticky/fixed elements: `2`
- **Step 03** (`y=2550px`, `23%`): Active landmark `Cancel free up to 3 hours before.` · sticky/fixed elements: `2`
- **Step 04** (`y=5100px`, `46%`): Active landmark `from booking to back home.` · sticky/fixed elements: `2`
- **Step 05** (`y=6800px`, `61%`): Active landmark `from booking to back home.` · sticky/fixed elements: `2`
- **Step 06** (`y=9350px`, `84%`): Active landmark `Start booking` · sticky/fixed elements: `2`
- **Step 07** (`y=11050px`, `99%`): Active landmark `How much does Serko.ai cost?` · sticky/fixed elements: `2`
- **Step 08** (`y=11188px`, `100%`): Active landmark `How will I know if there's a problem with my trip?` · sticky/fixed elements: `2`

### Multi-Page Internal Route Map
- **About Route (`/about`)**: `https://www.serko.ai/about` — H1: `Serko, your AI travel agent`, scrollHeight `5689px`, transition `direct` (`4215ms`)
- **Other Route (`/for-companies`)**: `https://www.serko.ai/for-companies` — H1: `Business travel management`, scrollHeight `9197px`, transition `direct` (`7047ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-serko-ai (Serko.ai · AI Travel Agent for Business Trips)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-serko-ai` (**Serko.ai · AI Travel Agent for Business Trips** — `https://www.serko.ai`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#e8f3fe` / `#0082f3`).
- **Identity & Domain Context**: Serko.ai is an AI travel agent for work. Book personalized flights and hotels, follow company policy, manage disruptions and cancel with...
- **Primary Substrate**: `#e8f3fe` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#0082f3`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#e8f3fe` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#0082f3` accents.
  - **Grounded Typographic Hierarchy**: Uses `Jokker` across display (`The last travel agent you’ll ever ne`) and body copy.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(0.525,0,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-serko-ai` in your global stylesheet:

:root {
  /* Serko.ai · AI Travel Agent for Business Trips (www-serko-ai) — Live-Grounded CSS Variables */
  --osano-clear-dialog-background: rgba(0,0,0,0); /* Canvas / Surface Token (www-serko-ai) */
  --osano-info-dialog-border-color: #d8d8d8; /* Brand / Palette Token (www-serko-ai) */
  --osano-info-dialog-border-subtle-color: #e9e9e9; /* Brand / Palette Token (www-serko-ai) */
  --osano-info-dialog-inset-color: #f4f4f4; /* Brand / Palette Token (www-serko-ai) */
  --osano-info-dialog-selected-background-color: #ebebeb; /* Canvas / Surface Token (www-serko-ai) */
  --osano-info-dialog-gpc-tint-color: #e7f9f0; /* Canvas / Surface Token (www-serko-ai) */
  --osano-theme: modern; /* Brand / Palette Token (www-serko-ai) */
  --osano-button-border-color: var(--osano-button-foreground-color); /* Brand / Palette Token (www-serko-ai) */
  --osano-dialog-type: box; /* Typography / Scale Token (www-serko-ai) */
  --osano-display-position: "bottom-left"; /* Design System Custom Token (www-serko-ai) */
  --osano-info-dialog-position: right; /* Design System Custom Token (www-serko-ai) */
  --osano-widget-position: right; /* Design System Custom Token (www-serko-ai) */
  --osano-opt-out-widget-position: right; /* Design System Custom Token (www-serko-ai) */
  --osano-button-background-color: #000000; /* Canvas / Surface Token (www-serko-ai) */
  --osano-button-foreground-color: #FFFFFF; /* Typography Ink Token (www-serko-ai) */
  --osano-dialog-background-color: #ffffff; /* Canvas / Surface Token (www-serko-ai) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#e8f3fe` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#ebebeb` — grounded in `var(--osano-info-dialog-selected-background-color)` in `:root`
- **Interactive Accent / Highlight**: `#0082f3` — grounded in `.w-dropdown-link.w--current { color: #0082f3 }`
- **Secondary / Muted Copy**: `#058a5e` — grounded in `var(--osano-gpc-foreground-color)` in `:root`
- **Structural Hairline Border**: `#d8d8d8` — grounded in `var(--osano-info-dialog-border-color)` in `:root`
- **Variable Token (`--osano-info-dialog-border-subtle-color`)**: `#e9e9e9` — grounded in `var(--osano-info-dialog-border-subtle-color)` in `:root`
- **Variable Token (`--osano-info-dialog-inset-color`)**: `#f4f4f4` — grounded in `var(--osano-info-dialog-inset-color)` in `:root`
- **Variable Token (`--osano-info-dialog-gpc-tint-color`)**: `#e7f9f0` — grounded in `var(--osano-info-dialog-gpc-tint-color)` in `:root`
- **Variable Token (`--osano-button-foreground-color`)**: `#ffffff` — grounded in `var(--osano-button-foreground-color)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `9px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding
- **Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`
- **Corner Radii**: `3px`, `100%`, `50%`, `var(--radius--medium)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Jokker`
- **Body Font Stack**: `Jokker`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 70.1985px`, `line-height: 70.1985px`, `font-weight: 500`, `letter-spacing: -2.10595px`); CSS variables `--osano-display-position: "bottom-left"`, `--library_typography---font-size--h1: 5.25rem`, `--library_typography---font-size--display: 6rem`
- **H2 Section Rule**: live computed `h2` (`font-size: 62.3271px`, `line-height: 62.3271px`, `font-weight: 500`, `letter-spacing: -1.86981px`); CSS variables `--library_typography---font-size--h2: 4rem`
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 500`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 500`); CSS variables `--library_heading-style---letter-spacing: var(--library_typography---letter-spacing--0em)`, `--library_text-style---letter-spacing: var(--library_typography---letter-spacing--0em)`, `--library_spacing---section-space--small: 5rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-serko-ai` (`Serko.ai · AI Travel Agent for Business Trips`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.nav1_header> — `www-serko-ai`)**:
   - DOM & Selectors: Landmark `<header class="nav1_header">` (`1440x75px`) hosting `Serko.ai · AI Travel Agent for Busin` navigation (`Home · Platform · For companies · About · Sign up free`), DOM attributes (`data-wf-domain="www.serko.ai"`, `data-wf-page="6aa12b65e6dd0b96a2a83430"`, `data-wf-site="6aa12b65e6dd0b96a2a8345b"`, `data-wf-intellimize-customer-id="117114932"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.nav1_header> — `www-serko-ai`)` (`www-serko-ai`) adapts across `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)` with `cubic-bezier(0.525,0,0,1)`, `cubic-bezier(.22,1.15,.36,1)` transitions and links `Home · Platform · For companies · About · Sign up free`.
2. **Hero Stage & Focal Lead (<section.hero1_wrap> — `The last travel agent you’ll ever `)**:
   - DOM & Selectors: Landmark `<section class="hero1_wrap u-gradient-bg-1">` presenting display lead `The last travel agent you’ll ever need.` and copy excerpt *"Serko learns how you like to travel, finds the best flights and h"* over `#e8f3fe` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#e8f3fe` background with `#000000` headline `The last travel agent you’ll ever need.`.
3. **Primary Showcase & Content Grid (<section.col3_wrap> — `AI travel agent for business`)**:
   - DOM & Selectors: Landmark `<section class="col3_wrap">` rendering section `AI travel agent for business` with copy *"Venue, location, address..."*, asset references (`cdn.prod.website-files.com`, `serko-ai.webflow.shared.96cab25cb...`, `serko-ai.webflow.6aa12b65e6dd0b96...`, `clientParamBuilder.bundle.js`), and grid rule `summary { display:block }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.col3_wrap> — `AI travel agent for business`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `9px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.feature1_wrap> — `How Serko.ai works`)**:
   - DOM & Selectors: Landmark `<section class="feature1_wrap u-background-3">` framing `How Serko.ai works` and `Business travel, booked in one chat.` (*"Trip details and preferences"*) with `#ebebeb` surface cards, `#0082f3` accents, and `video { vertical-align:baseline;display:inline-block }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.feature1_wrap> — `How Serko.ai works`)` uses `3px`, `100%`, `50%`, `var(--radius--medium)` radii, `#0082f3` highlights, and assets (cdn.prod.website-files.com, serko-ai.webflow.shared.96cab25cb..., serko-ai.webflow.6aa12b65e6dd0b96...).
5. **Colophon & Global Directory Footer (<footer.osano-cm-window> — `https://www.serko.ai`)**:
   - DOM & Selectors: Landmark `<footer class="osano-cm-window">` anchoring `Serko.ai · AI Travel Agent for B` footer links (`Home · Platform · For companies · About · Sign up free`), copy *"Whether you’ve got a big client meeting in New York this Fri"*, and `#d8d8d8` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.osano-cm-window> — `https://www.serko.ai`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `9px` lateral canvas padding with `16px` grid gap and attributes (data-wf-domain="www.serko.ai", data-wf-page="6aa12b65e6dd0b96a2a83430", data-wf-site="6aa12b65e6dd0b96a2a8345b").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Serko learns how you like to travel, finds the best flights and hotels for you to..."*
- Copy Excerpt 2: *"Venue, location, address..."*
- Copy Excerpt 3: *"Trip details and preferences"*
- Copy Excerpt 4: *"Whether you’ve got a big client meeting in New York this Friday or a conference in..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.525,0,0,1)`, `cubic-bezier(.22,1.15,.36,1)`
- **Extracted Stylesheet Rules (`www-serko-ai`)**:
- `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`
- `summary { display:block }`
- `video { vertical-align:baseline;display:inline-block }`
- `template { display:none }`
- `strong { font-weight:700 }`
- **Per-Selector Transition Rules**:
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `www-serko-ai` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `www-serko-ai` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-serko-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.525,0,0,1)`)**: Governs interactive state transitions across `<header.nav1_header>` and `<section.col3_wrap>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `12088px` across 8 distinct viewport chapters using Lenis, GSAP/ScrollTrigger, WebGL/Canvas.
- **Vertical Chapter Sequence**: The last travel agent you’l... (0%) -> How Serko.ai works (8%) -> Cancel free up to 3 hours b... (23%) -> from booking to back home. (46%) -> from booking to back home. (61%) -> Start booking (84%) -> How much does Serko.ai cost? (99%) -> How will I know if there's... (100%).
- **Multi-Page Routes**: Scaffold internal routes `/about` (about, direct), `/for-companies` (other, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-serko-ai`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | The last travel agent you’ll ever need. | `2` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `8%` | How Serko.ai works | `2` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `2550px` | `23%` | Cancel free up to 3 hours before. | `2` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `5100px` | `46%` | from booking to back home. | `2` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `6800px` | `61%` | from booking to back home. | `2` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `9350px` | `84%` | Start booking | `2` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `11050px` | `99%` | How much does Serko.ai cost? | `2` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `11188px` | `100%` | How will I know if there's a problem with my... | `2` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | The last travel agent you’ll ever need. | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `6024px` | `50%` | Section @ 50% | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `12048px` | `100%` | Be there for the moments that matter. | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Interactive UI State Captures (`1440×900` WebP)
| State Type | Trigger / Observation | Visual Asset |
| :--- | :--- | :--- |
| `interactive_control` | Control `accordion` (`Who is Serko.ai for?`, diff `6.559`) | [state-interactive.webp](assets/state-interactive.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `about` | `https://www.serko.ai/about` | Serko, your AI travel agent | `5689px` | `direct` (`4215ms`) | [subpage-01-about.webp](assets/subpage-01-about.webp) |
| `3` | `other` | `https://www.serko.ai/for-companies` | Business travel management | `9197px` | `direct` (`7047ms`) | [subpage-03-for-companies.webp](assets/subpage-03-for-companies.webp) |

