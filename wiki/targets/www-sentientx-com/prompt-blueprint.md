---
title: "UI Prompt Blueprint: www-sentientx-com"
date: 2026-11-15
target: "www-sentientx-com"
status: analyzed
capture: specimen
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#757575` / `#dbfac4`)"
---

# UI Design System & Master Generation Blueprint: www-sentientx-com

> **SentientX · Enterprise AI & Digital Likeness Protection** (https://www.sentientx.com) — SentientX is an AI operating partner for consumer products and retail. Production-grade AI across supply chain, finance, and operations....

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **SentientX · Enterprise AI & Digital Likeness Protection** (`https://www.sentientx.com`). SentientX is an AI operating partner for consumer products and retail. Production-grade AI across supply chain, finance, and operations....
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#757575` / `#dbfac4`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#757575` (`var(--stroke)` in `:root`) paired with `#FFFFFF` primary typography and `#dbfac4` accents.
  - **Extracted Typographic Hierarchy**: Pairs `wf_2751996ff9224fc486a0c6fe1` for display copy (`The Autonomous Enterprise`) with `din-next-w01-light` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `9999px` container bounds (`gap: 10px`, padding `8px`) with `cubic-bezier(.83,0,.17,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×10088px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `9999px` extracted from `www-sentientx-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `8px` lateral canvas padding with `10px` grid gap.
- **Border Radius Scale**: `2px`, `3px`, `999px`, `var(--corvid-border-radius)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 9999px`, `gap: 10px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `8px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (max-width:768px)`, `@media (prefers-reduced-motion:no-preference)`, `@media screen and (min-width: 1px) and (max-width: 1000px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#757575` | `var(--stroke)` in `:root` |
| **Primary Typography Ink** | `#FFFFFF` | `var(--fill)` in `:root` |
| **Elevated Surface / Card Substrate** | `#5f6360` | `device-mobile-non-optimized.ful... { background-color: #5f6360 }` |
| **Interactive Accent / Highlight** | `#dbfac4` | `.sx-toggle-track:before { background: #dbfac4 }` |
| **Secondary / Muted Copy** | `#000` | `.StylableButton2545352419__link { color: #000 }` |
| **Structural Hairline Border** | `#080808` | `ol.font_100 { color: #080808 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--scrollbar-width` | `0px` | Layout / Spatial Grid Token |
| `--one-unit` | `1vw` | Dimension / Scale Token |
| `--section-max-width` | `9999px` | Layout / Spatial Grid Token |
| `--spx-stopper-max` | `9999px` | Dimension / Scale Token |
| `--spx-stopper-min` | `0px` | Dimension / Scale Token |
| `--browser-zoom` | `1` | Design System Custom Token |
| `--safari-sticky-fix` | `opacity` | Design System Custom Token |
| `--experimental-safari-sticky-fix` | `translateZ(0)` | Design System Custom Token |
| `--wst-button-color-fill-primary` | `rgb(var(--color_48))` | Brand / Palette Token |
| `--wst-button-color-border-primary` | `rgb(var(--color_49))` | Brand / Palette Token |
| `--wst-button-color-text-primary` | `rgb(var(--color_50))` | Typography Ink Token |
| `--wst-button-color-fill-primary-hover` | `rgb(var(--color_51))` | Brand / Palette Token |
| `--wst-button-color-border-primary-hover` | `rgb(var(--color_52))` | Brand / Palette Token |
| `--wst-button-color-text-primary-hover` | `rgb(var(--color_53))` | Typography Ink Token |
| `--wst-button-color-fill-primary-disabled` | `rgb(var(--color_54))` | Brand / Palette Token |
| `--wst-button-color-border-primary-disabled` | `rgb(var(--color_55))` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `wf_2751996ff9224fc486a0c6fe1`.
- **Primary Body Stack**: `din-next-w01-light`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--display: inline-block`, `--comp-display: unset`, `--container-display: grid`.
- **Section Heading (`H2`)**: CSS variables `--wst-color-subtitle: rgb(var(--color_46))`, `--wst-font-style-h2: var(--font_2)`, `--item-depth2-direction: inherit`; rule `h2` (`font-size: 16px`, `line-height: 1.05`, `font-weight: 400`).
- **Body Copy**: CSS variables `--wst-font-style-body-large: var(--font_7)`, `--wst-font-style-body-medium: var(--font_8)`, `--wst-font-style-body-small: var(--font_9)`; rule `p` (`font-size: 13px`, `line-height: 1.4`, `font-weight: 400`).
- **Metadata & Navigation Labels**: CSS variables `--wst-font-style-body-small: var(--font_9)`, `--wst-font-style-body-x-small: var(--font_10)`, `--label-align: center`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.83,0,.17,1)`, `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.64,0,.78,0)`.

### Per-Element Transition & Choreography Rules
- **Selector `id^=oldHoverBox-]`**: `transition: opacity .5s,visibility .5s` extracted from `www-sentientx-com` stylesheet.
- **Selector `.sx-cookie-btn`**: `transition: background .2s ease,opacity .2s ease` extracted from `www-sentientx-com` stylesheet.
- **Selector `.sx-toggle-track`**: `transition: .3s` extracted from `www-sentientx-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.83,0,.17,1)`)**: Governs interactive state transitions across `<header.comp-mqurid64>` and `<section.ke5pl1>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — SentientX · Enterprise AI & Digital Likene │
│ ====================================================================== │
│ [ <header.comp-mqurid64>   | Home                                   ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.ke5pl1>                                     |   │
│ | H1: The Autonomous Enterprise                                    |   │
│ | Substrate: #757575    | Ink: #FFFFFF    | Accent: #dbfac4        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.ke5pl1>          ) max-w: 9999px         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | One intelligence, three laye |  | A new institutional layer fo | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 10px  ) | │
│ | [<header.comp-mquri] -> [<section.ke5pl1>] -> [<section.ke5pl1>] |   │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.comp-kbgakxmn>) | https://www.sentientx.com          │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.comp-mqurid64> — `www-sentientx-com`)**:
   - Landmark `<header class="comp-mqurid64 S829f_">` hosting `SentientX · Enterprise AI & Digital ` navigation (`Home`), DOM attributes (`data-url="https://static.parast..."`, `data-url="https://static.parast..."`, `data-url="https://static.parast..."`, `data-url="https://static.parast..."`), and stylesheet rule `root:active-view-transition { view-transition-name:none }`.
2. **Hero Stage & Focal Lead (<section.ke5pl1> — `The Autonomous Enterprise`)**:
   - Landmark `<section class="ke5pl1 comp-mqurid64_r_comp-kbgajy18">` presenting display lead `The Autonomous Enterprise` and copy excerpt *"Necessary 14 Necessary cookies help make a website usable by enab"* over `#757575` canvas and `#FFFFFF` ink.
3. **Primary Showcase & Content Grid (<section.ke5pl1> — `One intelligence, three layers`)**:
   - Landmark `<section class="ke5pl1 comp-mr0mk2kw-container">` rendering section `One intelligence, three layers` with copy *"Cookiebot 1 Learn more about this provider CookieConsent Stores t"*, asset references (`0b6ff1_2de67bd90d924a449a9260fe7d...`, `cc.js`, `minified.js`, `focus-within-polyfill.js`), and grid rule `root::view-transition { pointer-events:none }`.
4. **Interactive Detail & Feature Matrix (<section.ke5pl1> — `A new institutional layer for huma`)**:
   - Landmark `<section class="ke5pl1 comp-mrnlzewt-container">` framing `A new institutional layer for human identity.` and `Monitor, protect, control and enforce.` (*"Learn more about this provider"*) with `#5f6360` surface cards, `#dbfac4` accents, and `SITE_HEADER { view-transition-name:header-group }`.
5. **Colophon & Global Directory Footer (<footer.comp-kbgakxmn> — `https://www.sentientx.com`)**:
   - Landmark `<footer class="comp-kbgakxmn S829f_">` anchoring `SentientX · Enterprise AI & Digi` footer links (`Home`), copy *"Stores the user's cookie consent state for the current domai"*, and `#080808` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-sentientx-com (SentientX · Enterprise AI & Digital Likeness Protection)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-sentientx-com` (**SentientX · Enterprise AI & Digital Likeness Protection** — `https://www.sentientx.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#757575` / `#dbfac4`).
- **Identity & Domain Context**: SentientX is an AI operating partner for consumer products and retail. Production-grade AI across supply chain, finance, and operations....
- **Primary Substrate**: `#757575` (`var(--stroke)` in `:root`), **Primary Ink**: `#FFFFFF`, **Accent / Highlight**: `#dbfac4`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#757575` (`var(--stroke)` in `:root`) paired with `#FFFFFF` primary typography and `#dbfac4` accents.
  - **Extracted Typographic Hierarchy**: Pairs `wf_2751996ff9224fc486a0c6fe1` for display copy (`The Autonomous Enterprise`) with `din-next-w01-light` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `9999px` container bounds (`gap: 10px`, padding `8px`) with `cubic-bezier(.83,0,.17,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-sentientx-com` in your global stylesheet:

:root {
  /* SentientX · Enterprise AI & Digital Likeness Protection (www-sentientx-com) — Ground-Truth Extracted CSS Variables */
  --scrollbar-width: 0px; /* Layout / Spatial Grid Token (www-sentientx-com) */
  --one-unit: 1vw; /* Dimension / Scale Token (www-sentientx-com) */
  --section-max-width: 9999px; /* Layout / Spatial Grid Token (www-sentientx-com) */
  --spx-stopper-max: 9999px; /* Dimension / Scale Token (www-sentientx-com) */
  --spx-stopper-min: 0px; /* Dimension / Scale Token (www-sentientx-com) */
  --browser-zoom: 1; /* Design System Custom Token (www-sentientx-com) */
  --safari-sticky-fix: opacity; /* Design System Custom Token (www-sentientx-com) */
  --experimental-safari-sticky-fix: translateZ(0); /* Design System Custom Token (www-sentientx-com) */
  --wst-button-color-fill-primary: rgb(var(--color_48)); /* Brand / Palette Token (www-sentientx-com) */
  --wst-button-color-border-primary: rgb(var(--color_49)); /* Brand / Palette Token (www-sentientx-com) */
  --wst-button-color-text-primary: rgb(var(--color_50)); /* Typography Ink Token (www-sentientx-com) */
  --wst-button-color-fill-primary-hover: rgb(var(--color_51)); /* Brand / Palette Token (www-sentientx-com) */
  --wst-button-color-border-primary-hover: rgb(var(--color_52)); /* Brand / Palette Token (www-sentientx-com) */
  --wst-button-color-text-primary-hover: rgb(var(--color_53)); /* Typography Ink Token (www-sentientx-com) */
  --wst-button-color-fill-primary-disabled: rgb(var(--color_54)); /* Brand / Palette Token (www-sentientx-com) */
  --wst-button-color-border-primary-disabled: rgb(var(--color_55)); /* Brand / Palette Token (www-sentientx-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#757575` — grounded in `var(--stroke)` in `:root`
- **Primary Typography Ink**: `#FFFFFF` — grounded in `var(--fill)` in `:root`
- **Elevated Surface / Card Substrate**: `#5f6360` — grounded in `device-mobile-non-optimized.ful... { background-color: #5f6360 }`
- **Interactive Accent / Highlight**: `#dbfac4` — grounded in `.sx-toggle-track:before { background: #dbfac4 }`
- **Secondary / Muted Copy**: `#000` — grounded in `.StylableButton2545352419__link { color: #000 }`
- **Structural Hairline Border**: `#080808` — grounded in `ol.font_100 { color: #080808 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×10088px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `9999px` extracted from `www-sentientx-com` stylesheet
- **Padding & Gutters**: `8px` lateral canvas padding with `10px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 9999px`, `gap: 10px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `8px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (max-width:768px)`, `@media (prefers-reduced-motion:no-preference)`, `@media screen and (min-width: 1px) and (max-width: 1000px)`
- **Corner Radii**: `2px`, `3px`, `999px`, `var(--corvid-border-radius)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `wf_2751996ff9224fc486a0c6fe1`
- **Body Font Stack**: `din-next-w01-light`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--display: inline-block`, `--comp-display: unset`, `--container-display: grid`
- **H2 Section Rule**: CSS variables `--wst-color-subtitle: rgb(var(--color_46))`, `--wst-font-style-h2: var(--font_2)`, `--item-depth2-direction: inherit`; rule `h2` (`font-size: 16px`, `line-height: 1.05`, `font-weight: 400`)
- **Body Copy Rule**: CSS variables `--wst-font-style-body-large: var(--font_7)`, `--wst-font-style-body-medium: var(--font_8)`, `--wst-font-style-body-small: var(--font_9)`; rule `p` (`font-size: 13px`, `line-height: 1.4`, `font-weight: 400`)
- **Metadata & Index Rule**: CSS variables `--wst-font-style-body-small: var(--font_9)`, `--wst-font-style-body-x-small: var(--font_10)`, `--label-align: center`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-sentientx-com` (`SentientX · Enterprise AI & Digital Likeness Protection`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.comp-mqurid64> — `www-sentientx-com`)**:
   - DOM & Selectors: Landmark `<header class="comp-mqurid64 S829f_">` hosting `SentientX · Enterprise AI & Digital ` navigation (`Home`), DOM attributes (`data-url="https://static.parast..."`, `data-url="https://static.parast..."`, `data-url="https://static.parast..."`, `data-url="https://static.parast..."`), and stylesheet rule `root:active-view-transition { view-transition-name:none }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.comp-mqurid64> — `www-sentientx-com`)` (`www-sentientx-com`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (max-width:768px)`, `@media (prefers-reduced-motion:no-preference)`, `@media screen and (min-width: 1px) and (max-width: 1000px)` with `cubic-bezier(.83,0,.17,1)`, `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.64,0,.78,0)` transitions and links `Home`.
2. **Hero Stage & Focal Lead (<section.ke5pl1> — `The Autonomous Enterprise`)**:
   - DOM & Selectors: Landmark `<section class="ke5pl1 comp-mqurid64_r_comp-kbgajy18">` presenting display lead `The Autonomous Enterprise` and copy excerpt *"Necessary 14 Necessary cookies help make a website usable by enab"* over `#757575` canvas and `#FFFFFF` ink.
   - Responsive Contract: Hero stage (`1440×10088px` desktop / `390×2400px` mobile) sets `#757575` background with `#FFFFFF` headline `The Autonomous Enterprise`.
3. **Primary Showcase & Content Grid (<section.ke5pl1> — `One intelligence, three layers`)**:
   - DOM & Selectors: Landmark `<section class="ke5pl1 comp-mr0mk2kw-container">` rendering section `One intelligence, three layers` with copy *"Cookiebot 1 Learn more about this provider CookieConsent Stores t"*, asset references (`0b6ff1_2de67bd90d924a449a9260fe7d...`, `cc.js`, `minified.js`, `focus-within-polyfill.js`), and grid rule `root::view-transition { pointer-events:none }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.ke5pl1> — `One intelligence, three layers`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 9999px`, `gap: 10px`) on desktop and Single-column vertical stack at `390px` viewport width with `8px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.ke5pl1> — `A new institutional layer for huma`)**:
   - DOM & Selectors: Landmark `<section class="ke5pl1 comp-mrnlzewt-container">` framing `A new institutional layer for human identity.` and `Monitor, protect, control and enforce.` (*"Learn more about this provider"*) with `#5f6360` surface cards, `#dbfac4` accents, and `SITE_HEADER { view-transition-name:header-group }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.ke5pl1> — `A new institutional layer for huma`)` uses `2px`, `3px`, `999px`, `var(--corvid-border-radius)` radii, `#dbfac4` highlights, and assets (0b6ff1_2de67bd90d924a449a9260fe7d..., cc.js, minified.js).
5. **Colophon & Global Directory Footer (<footer.comp-kbgakxmn> — `https://www.sentientx.com`)**:
   - DOM & Selectors: Landmark `<footer class="comp-kbgakxmn S829f_">` anchoring `SentientX · Enterprise AI & Digi` footer links (`Home`), copy *"Stores the user's cookie consent state for the current domai"*, and `#080808` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.comp-kbgakxmn> — `https://www.sentientx.com`)` aligns to `9999px` extracted from `www-sentientx-com` stylesheet with `8px` lateral canvas padding with `10px` grid gap and attributes (data-url="https://static.parast...", data-url="https://static.parast...", data-url="https://static.parast...").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Necessary 14 Necessary cookies help make a website usable by enabling basic functi..."*
- Copy Excerpt 2: *"Cookiebot 1 Learn more about this provider CookieConsent Stores the user's cookie..."*
- Copy Excerpt 3: *"Learn more about this provider"*
- Copy Excerpt 4: *"Stores the user's cookie consent state for the current domain"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.83,0,.17,1)`, `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.64,0,.78,0)`
- **Extracted Stylesheet Rules (`www-sentientx-com`)**:
- `root:active-view-transition { view-transition-name:none }`
- `root::view-transition { pointer-events:none }`
- `SITE_HEADER { view-transition-name:header-group }`
- `WIX_ADS { view-transition-name:wix-ads-group }`
- `SITE_FOOTER { view-transition-name:footer-group }`
- **Per-Selector Transition Rules**:
- **Selector `id^=oldHoverBox-]`**: `transition: opacity .5s,visibility .5s` extracted from `www-sentientx-com` stylesheet.
- **Selector `.sx-cookie-btn`**: `transition: background .2s ease,opacity .2s ease` extracted from `www-sentientx-com` stylesheet.
- **Selector `.sx-toggle-track`**: `transition: .3s` extracted from `www-sentientx-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.83,0,.17,1)`)**: Governs interactive state transitions across `<header.comp-mqurid64>` and `<section.ke5pl1>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-sentientx-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
