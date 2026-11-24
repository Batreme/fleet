---
title: "UI Prompt Blueprint: about-centra-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "about-centra-com"
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
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#ffffff` ink, `#ffff00` accent)"
---

# UI Design System & Master Generation Blueprint: about-centra-com

> **Centra? Centra! The definitive guide.** (https://about.centra.com) — The commerce platform for fashion brands.

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Centra? Centra! The definitive guide.** (`https://about.centra.com`). The commerce platform for fashion brands.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#ffffff` ink, `#ffff00` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#ffff00` accents.
  - **Grounded Typographic Hierarchy**: Pairs `neue-haas-grotesk-display` for display copy (`CENTRA? CENTRA!`) with `neue-haas-grotesk-text`.
  - **Calibrated Spatial Grid & Motion**: Combines `1920px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.4,0,.2,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=4929px` / doc `6253px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1920px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `9px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `99px`, `3px`, `100%`, `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1920px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#222222` | `.w-slider-nav-invert>div.w-active { background-color: #222222 }` |
| **Interactive Accent / Highlight** | `#ffff00` | `.hs-button.submit:hover { background-color: yellow }` (`#ffff00`) |
| **Secondary / Muted Copy** | `#a9a9a9` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#959494` | `var(--hsf-default-field-input__border-color)` in `:root` (`rgb(149, 148, 148)`) |
| **Variable Token (`--_colours---mono--200`)** | `#d9d9d9` | `var(--_colours---mono--200)` in `:root` |
| **Variable Token (`--_colours---yellow--main`)** | `#fecf48` | `var(--_colours---yellow--main)` in `:root` |
| **Variable Token (`--_colours---mono--800`)** | `#191919` | `var(--_colours---mono--800)` in `:root` |
| **Variable Token (`--_colours---red--main`)** | `#f85943` | `var(--_colours---red--main)` in `:root` |
| **Variable Token (`--_colours---mono--600`)** | `#333333` | `var(--_colours---mono--600)` in `:root` |
| **Variable Token (`--_colours---green--main`)** | `#1cad56` | `var(--_colours---green--main)` in `:root` |
| **Variable Token (`--_colours---blue--main`)** | `#1d80f6` | `var(--_colours---blue--main)` in `:root` |
| **Variable Token (`--_colours---mono--400`)** | `#787878` | `var(--_colours---mono--400)` in `:root` |
| **Variable Token (`--_colours---mono--700`)** | `#252525` | `var(--_colours---mono--700)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_colours---mono--0` | `white` | Typography / Scale Token |
| `--_colours---mono--900` | `black` | Typography / Scale Token |
| `--_colours---mono--300` | `darkgrey` | Typography / Scale Token |
| `--_colours---mono--200` | `#d9d9d9` | Typography / Scale Token |
| `--padding-inner-md` | `40px` | Layout / Spatial Grid Token |
| `--_colours---yellow--main` | `#fecf48` | Layout / Spatial Grid Token |
| `--padding-section-xl` | `90px` | Layout / Spatial Grid Token |
| `--padding-inner-sm` | `20px` | Layout / Spatial Grid Token |
| `--_colours---mono--800` | `#191919` | Typography / Scale Token |
| `--_colours---red--main` | `#f85943` | Layout / Spatial Grid Token |
| `--_colours---mono--600` | `#333` | Typography / Scale Token |
| `--_colours---green--main` | `#1cad56` | Layout / Spatial Grid Token |
| `--_colours---blue--main` | `#1d80f6` | Layout / Spatial Grid Token |
| `--padding-inner-lg` | `80px` | Layout / Spatial Grid Token |
| `--_colours---mono--400` | `#787878` | Typography / Scale Token |
| `--_colours---mono--700` | `#252525` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `neue-haas-grotesk-display`.
- **Primary Body Stack**: `neue-haas-grotesk-text`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 146.71px`, `line-height: 124.703px`, `font-weight: 900`, `letter-spacing: 0.12px`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 140px`, `line-height: 140px`, `font-weight: 700`).
- **Body Copy**: live computed `body` (`font-size: 14px`, `line-height: 20px`, `font-weight: 400`); rule `p` (`font-size: inherit`, `font-weight: inherit`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 26px`, `font-weight: 400`); CSS variables `--_colours---mono--0: white`, `--_colours---mono--900: black`, `--_colours---mono--300: darkgrey`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `about-centra-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `about-centra-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `about-centra-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<nav.navigation-glass-wrapper>` and `<section.section-parallax>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `6253px`, deepest scrollY reached `4929px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `GSAP/ScrollTrigger`.
- **Route Transition Architecture**: First internal navigation (`/centra-preview`) measured as `MPA` in `1832ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Centra? Centra! The definitive guide.      │
│ ====================================================================== │
│ [ <nav.navigation-glass- (675x60px)   | 13 ½ Centra Facts · Brands o ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.heading-animation> (w=1440px)                 | │
│ | H1: CENTRA? CENTRA!                                                | │
│ | Substrate: #000000 | Ink: #ffffff | Accent: #ffff00                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.section-parallax>) max-w: 1920px           | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Centra? Centra!              |  | about-centra-com Interactive | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.section-call-to-a) — about-centra-com Arch | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.wf-neuehaasg) | https://about.centra.com             │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px)       │
│ ====================================================================== │
│ [ HEADER BAR (<nav.navigation-glass-wr) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.heading-animati) — 390px Vertical Lead        | │
│ | H1: CENTRA? CENTRA!                                                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.section-paral) — 1-Col Stack              | │
│ | [ Item 1: Centra? Centra!                                        ] | │
│ | [ Item 2: about-centra-com Interactive Matrix                    ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.section-call-to) — 1-Col (about-centra-com A) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.wf-neuehaasg) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.navigation-glass-wrapper> — `about-centra-com`)**:
   - Landmark `<nav class="navigation-glass-wrapper mobile-navigation">` (`675x60px`) hosting `Centra? Centra! The definitive guide` navigation (`13 ½ Centra Facts · Brands on Centra`), DOM attributes (`data-wf-domain="about.centra.com"`, `data-wf-page="6a0af5d1e1f707540842bee4"`, `data-wf-site="6a0af5d1e1f707540842bf02"`, `data-global-dreamdata-analytics-key="dreamdata"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.heading-animation> — `CENTRA? CENTRA!`)**:
   - Landmark `<section class="heading-animation">` presenting display lead `CENTRA? CENTRA!` and copy excerpt *"Centra uses your contact information to send product and service "* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.section-parallax> — `Centra? Centra!`)**:
   - Landmark `<section class="section-parallax">` rendering section `Centra? Centra!` with copy *"CENTRA? CENTRA!"*, asset references (`cdn.prod.website-files.com`, `centra-centra.webflow.shared.3f63...`, `dreamdata.min.js`, `lftracker_v1_ywVkO4XVlwx8Z6Bj.js`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.section-call-to-action> — `about-centra-com Interactive Matri`)**:
   - Landmark `<section class="section-call-to-action">` framing `about-centra-com Interactive Matrix` and `about-centra-com Archive & Directory` (*"Centra? Centra!"*) with `#222222` surface cards, `#ffff00` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.wf-neuehaasgrotesktext-n4-active> — `https://about.centra.com`)**:
   - Landmark `<footer class="wf-neuehaasgrotesktext-n4-active">` anchoring `Centra? Centra! The definitive g` footer links (`13 ½ Centra Facts · Brands on Centra`), copy *"about-centra-com Interactive Matrix"*, and `#959494` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `CENTRA? CENTRA!` · sticky/fixed elements: `1`
- **Step 02** (`y=850px`, `17%`): Active landmark `Section @ 17%` · sticky/fixed elements: `1`
- **Step 03** (`y=1700px`, `34%`): Active landmark `Centra preview in 60 seconds` · sticky/fixed elements: `1`
- **Step 04** (`y=2550px`, `52%`): Active landmark `Centra preview in 60 seconds` · sticky/fixed elements: `1`
- **Step 05** (`y=3400px`, `69%`): Active landmark `#Section-CTA` · sticky/fixed elements: `1`
- **Step 06** (`y=4250px`, `86%`): Active landmark `#Section-CTA` · sticky/fixed elements: `1`
- **Step 07** (`y=4929px`, `100%`): Active landmark `#Facts` · sticky/fixed elements: `1`
- **Step 08** (`y=4929px`, `100%`): Active landmark `#Facts` · sticky/fixed elements: `1`

### Multi-Page Internal Route Map
- **Other Route (`/centra-preview`)**: `https://about.centra.com/centra-preview` — H1: `Centra? Centra! The commerce platform for fashion`, scrollHeight `1371px`, transition `MPA` (`1832ms`)
- **Other Route (`/facts-about-centra`)**: `https://about.centra.com/facts-about-centra` — H1: `Centra? Centra! The commerce platform for fashion`, scrollHeight `23686px`, transition `direct` (`1208ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: about-centra-com (Centra? Centra! The definitive guide.)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `about-centra-com` (**Centra? Centra! The definitive guide.** — `https://about.centra.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#ffffff` ink, `#ffff00` accent).
- **Identity & Domain Context**: The commerce platform for fashion brands.
- **Primary Substrate**: `#000000` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#ffff00`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#ffff00` accents.
  - **Grounded Typographic Hierarchy**: Pairs `neue-haas-grotesk-display` for display copy (`CENTRA? CENTRA!`) with `neue-haas-grotesk-text`.
  - **Calibrated Spatial Grid & Motion**: Combines `1920px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.4,0,.2,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `about-centra-com` in your global stylesheet:

:root {
  /* Centra? Centra! The definitive guide. (about-centra-com) — Live-Grounded CSS Variables */
  --_colours---mono--0: white; /* Typography / Scale Token (about-centra-com) */
  --_colours---mono--900: black; /* Typography / Scale Token (about-centra-com) */
  --_colours---mono--300: darkgrey; /* Typography / Scale Token (about-centra-com) */
  --_colours---mono--200: #d9d9d9; /* Typography / Scale Token (about-centra-com) */
  --padding-inner-md: 40px; /* Layout / Spatial Grid Token (about-centra-com) */
  --_colours---yellow--main: #fecf48; /* Layout / Spatial Grid Token (about-centra-com) */
  --padding-section-xl: 90px; /* Layout / Spatial Grid Token (about-centra-com) */
  --padding-inner-sm: 20px; /* Layout / Spatial Grid Token (about-centra-com) */
  --_colours---mono--800: #191919; /* Typography / Scale Token (about-centra-com) */
  --_colours---red--main: #f85943; /* Layout / Spatial Grid Token (about-centra-com) */
  --_colours---mono--600: #333; /* Typography / Scale Token (about-centra-com) */
  --_colours---green--main: #1cad56; /* Layout / Spatial Grid Token (about-centra-com) */
  --_colours---blue--main: #1d80f6; /* Layout / Spatial Grid Token (about-centra-com) */
  --padding-inner-lg: 80px; /* Layout / Spatial Grid Token (about-centra-com) */
  --_colours---mono--400: #787878; /* Typography / Scale Token (about-centra-com) */
  --_colours---mono--700: #252525; /* Typography / Scale Token (about-centra-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000000` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#ffffff` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#222222` — grounded in `.w-slider-nav-invert>div.w-active { background-color: #222222 }`
- **Interactive Accent / Highlight**: `#ffff00` — grounded in `.hs-button.submit:hover { background-color: yellow }` (`#ffff00`)
- **Secondary / Muted Copy**: `#a9a9a9` — grounded in live computed `p` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#959494` — grounded in `var(--hsf-default-field-input__border-color)` in `:root` (`rgb(149, 148, 148)`)
- **Variable Token (`--_colours---mono--200`)**: `#d9d9d9` — grounded in `var(--_colours---mono--200)` in `:root`
- **Variable Token (`--_colours---yellow--main`)**: `#fecf48` — grounded in `var(--_colours---yellow--main)` in `:root`
- **Variable Token (`--_colours---mono--800`)**: `#191919` — grounded in `var(--_colours---mono--800)` in `:root`
- **Variable Token (`--_colours---red--main`)**: `#f85943` — grounded in `var(--_colours---red--main)` in `:root`
- **Variable Token (`--_colours---mono--600`)**: `#333333` — grounded in `var(--_colours---mono--600)` in `:root`
- **Variable Token (`--_colours---green--main`)**: `#1cad56` — grounded in `var(--_colours---green--main)` in `:root`
- **Variable Token (`--_colours---blue--main`)**: `#1d80f6` — grounded in `var(--_colours---blue--main)` in `:root`
- **Variable Token (`--_colours---mono--400`)**: `#787878` — grounded in `var(--_colours---mono--400)` in `:root`
- **Variable Token (`--_colours---mono--700`)**: `#252525` — grounded in `var(--_colours---mono--700)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1920px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `9px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1920px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding
- **Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`
- **Corner Radii**: `99px`, `3px`, `100%`, `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `neue-haas-grotesk-display`
- **Body Font Stack**: `neue-haas-grotesk-text`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 146.71px`, `line-height: 124.703px`, `font-weight: 900`, `letter-spacing: 0.12px`)
- **H2 Section Rule**: live computed `h2` (`font-size: 140px`, `line-height: 140px`, `font-weight: 700`)
- **Body Copy Rule**: live computed `body` (`font-size: 14px`, `line-height: 20px`, `font-weight: 400`); rule `p` (`font-size: inherit`, `font-weight: inherit`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 26px`, `font-weight: 400`); CSS variables `--_colours---mono--0: white`, `--_colours---mono--900: black`, `--_colours---mono--300: darkgrey`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `about-centra-com` (`Centra? Centra! The definitive guide.`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.navigation-glass-wrapper> — `about-centra-com`)**:
   - DOM & Selectors: Landmark `<nav class="navigation-glass-wrapper mobile-navigation">` (`675x60px`) hosting `Centra? Centra! The definitive guide` navigation (`13 ½ Centra Facts · Brands on Centra`), DOM attributes (`data-wf-domain="about.centra.com"`, `data-wf-page="6a0af5d1e1f707540842bee4"`, `data-wf-site="6a0af5d1e1f707540842bf02"`, `data-global-dreamdata-analytics-key="dreamdata"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.navigation-glass-wrapper> — `about-centra-com`)` (`about-centra-com`) adapts across `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)` with `cubic-bezier(.4,0,.2,1)` transitions and links `13 ½ Centra Facts · Brands on Centra`.
2. **Hero Stage & Focal Lead (<section.heading-animation> — `CENTRA? CENTRA!`)**:
   - DOM & Selectors: Landmark `<section class="heading-animation">` presenting display lead `CENTRA? CENTRA!` and copy excerpt *"Centra uses your contact information to send product and service "* over `#000000` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#000000` background with `#ffffff` headline `CENTRA? CENTRA!`.
3. **Primary Showcase & Content Grid (<section.section-parallax> — `Centra? Centra!`)**:
   - DOM & Selectors: Landmark `<section class="section-parallax">` rendering section `Centra? Centra!` with copy *"CENTRA? CENTRA!"*, asset references (`cdn.prod.website-files.com`, `centra-centra.webflow.shared.3f63...`, `dreamdata.min.js`, `lftracker_v1_ywVkO4XVlwx8Z6Bj.js`), and grid rule `summary { display:block }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.section-parallax> — `Centra? Centra!`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1920px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `9px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.section-call-to-action> — `about-centra-com Interactive Matri`)**:
   - DOM & Selectors: Landmark `<section class="section-call-to-action">` framing `about-centra-com Interactive Matrix` and `about-centra-com Archive & Directory` (*"Centra? Centra!"*) with `#222222` surface cards, `#ffff00` accents, and `video { vertical-align:baseline;display:inline-block }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.section-call-to-action> — `about-centra-com Interactive Matri`)` uses `99px`, `3px`, `100%`, `50%` radii, `#ffff00` highlights, and assets (cdn.prod.website-files.com, centra-centra.webflow.shared.3f63..., dreamdata.min.js).
5. **Colophon & Global Directory Footer (<footer.wf-neuehaasgrotesktext-n4-active> — `https://about.centra.com`)**:
   - DOM & Selectors: Landmark `<footer class="wf-neuehaasgrotesktext-n4-active">` anchoring `Centra? Centra! The definitive g` footer links (`13 ½ Centra Facts · Brands on Centra`), copy *"about-centra-com Interactive Matrix"*, and `#959494` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.wf-neuehaasgrotesktext-n4-active> — `https://about.centra.com`)` aligns to `1920px` (non-`@media` desktop container stylesheet rule) with `9px` lateral canvas padding with `16px` grid gap and attributes (data-wf-domain="about.centra.com", data-wf-page="6a0af5d1e1f707540842bee4", data-wf-site="6a0af5d1e1f707540842bf02").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Centra uses your contact information to send product and service updates, which yo..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`about-centra-com`)**:
- `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`
- `summary { display:block }`
- `video { vertical-align:baseline;display:inline-block }`
- `template { display:none }`
- `strong { font-weight:700 }`
- **Per-Selector Transition Rules**:
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `about-centra-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `about-centra-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `about-centra-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<nav.navigation-glass-wrapper>` and `<section.section-parallax>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `6253px` across 8 distinct viewport chapters using GSAP/ScrollTrigger.
- **Vertical Chapter Sequence**: CENTRA? CENTRA! (0%) -> Section @ 17% (17%) -> Centra preview in 60 seconds (34%) -> Centra preview in 60 seconds (52%) -> #Section-CTA (69%) -> #Section-CTA (86%) -> #Facts (100%) -> #Facts (100%).
- **Multi-Page Routes**: Scaffold internal routes `/centra-preview` (other, MPA), `/facts-about-centra` (other, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `about-centra-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | CENTRA? CENTRA! | `1` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `17%` | Section @ 17% | `1` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `1700px` | `34%` | Centra preview in 60 seconds | `1` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `2550px` | `52%` | Centra preview in 60 seconds | `1` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `3400px` | `69%` | #Section-CTA | `1` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `4250px` | `86%` | #Section-CTA | `1` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `4929px` | `100%` | #Facts | `1` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `4929px` | `100%` | #Facts | `1` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | CENTRA? CENTRA! | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `1301px` | `50%` | #Section-CTA | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `2899px` | `100%` | #Facts | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `other` | `https://about.centra.com/centra-preview` | Centra? Centra! The commerce platform... | `1371px` | `MPA` (`1832ms`) | [subpage-01-centra-preview.webp](assets/subpage-01-centra-preview.webp) |
| `2` | `other` | `https://about.centra.com/facts-about-centra` | Centra? Centra! The commerce platform... | `23686px` | `direct` (`1208ms`) | [subpage-02-facts-about-centra.webp](assets/subpage-02-facts-about-centra.webp) |

