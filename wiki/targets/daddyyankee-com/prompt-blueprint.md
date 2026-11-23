---
title: "UI Prompt Blueprint: daddyyankee-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "daddyyankee-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#ece8dc` / `#ff0000`)"
---

# UI Design System & Master Generation Blueprint: daddyyankee-com

> **Daddy Yankee · Official Website** (https://daddyyankee.com/) — The official Daddy Yankee website. Discover La Postal, his upcoming album, listen to his new single, and get the latest from Daddy Yankee.

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Daddy Yankee · Official Website** (`https://daddyyankee.com/`). The official Daddy Yankee website. Discover La Postal, his upcoming album, listen to his new single, and get the latest from Daddy Yankee.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#ece8dc` / `#ff0000`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ece8dc` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#ff0000` accents.
  - **Grounded Typographic Hierarchy**: Pairs `ABC Diatype Compressed` for display copy (`LA POSTAL`) with `Inter Tight 500` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.9,0,.1,1)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `9px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `3px`, `100%`, `50%`, `4px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ece8dc` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffff00` | `mark { background: #ffff00 }` |
| **Interactive Accent / Highlight** | `#ff0000` | `.hero_cta.is-red { color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#efee32` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e2e2e2` | `blockquote { border-left: #e2e2e2 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_theme---background` | `var(--_swatch---swatch--cream)` | Canvas / Surface Token |
| `--_typography---body-family` | `"Inter Tight 500",Arial,sans-serif` | Typography / Scale Token |
| `--_theme---body` | `var(--_swatch---swatch--black)` | Brand / Palette Token |
| `--size-font` | `calc(var(--size-container)/(var(--size-container-ideal)/var(--size-unit)))` | Typography / Scale Token |
| `--_typography---body-line-height` | `1.2` | Typography / Scale Token |
| `--_typography---body-weight` | `500` | Design System Custom Token |
| `--_typography---body-letter-space` | `-.03em` | Layout / Spatial Grid Token |
| `--_typography---heading-family` | `"ABC Diatype Compressed",Impact,sans-serif` | Typography Ink Token |
| `--text-style--64` | `4em` | Typography Ink Token |
| `--_typography---heading-line-height` | `.8` | Typography Ink Token |
| `--_typography---heading-weight` | `900` | Typography Ink Token |
| `--_typography---heading-letter-space` | `-.02em` | Typography Ink Token |
| `--text-style--32` | `2em` | Typography Ink Token |
| `--site-margin` | `.75em` | Layout / Spatial Grid Token |
| `--_swatch---swatch--cream` | `#ece8dc` | Brand / Palette Token |
| `--nav--height` | `4.5em` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `ABC Diatype Compressed`.
- **Primary Body Stack**: `Inter Tight 500`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 420px`, `line-height: 336px`, `font-weight: 900`, `letter-spacing: -8.4px`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 420px`, `line-height: 336px`, `font-weight: 900`, `letter-spacing: -8.4px`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 19.2px`, `font-weight: 500`, `letter-spacing: -0.48px`); CSS variables `--_typography---body-family: "Inter Tight 500",Arial,sans-serif`, `--_theme---body: var(--_swatch---swatch--black)`, `--_typography---body-line-height: 1.2`.
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 19.2px`, `font-weight: 500`, `letter-spacing: -0.48px`); CSS variables `--text-style--body-small: max(1em,16px)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.9,0,.1,1)`, `cubic-bezier(.215,.61,.355,1)`, `cubic-bezier(.32,.72,0,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `daddyyankee-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `daddyyankee-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `daddyyankee-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.9,0,.1,1)`)**: Governs interactive state transitions across `<nav.bold-nav-full>` and `<section.portrait_wrap>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Daddy Yankee · Official Website            │
│ ====================================================================== │
│ [ <nav.bold-nav-full> (1440x900px)    | STORE · FOUNDATIONS · GLOBAL ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero_wrap> (w=1440px)                         | │
│ | H1: LA POSTAL                                                      | │
│ | Substrate: #ece8dc | Ink: #000000 | Accent: #ff0000                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.portrait_wrap>) max-w: 1440px              | │
│ | +------------------------------+  +------------------------------+ | │
│ | | October 30th, 2026           |  | We use cookies to enhance yo | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.tl_wrap>) — Customise Consent Pre          | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer_wrap>) | https://daddyyankee.com/             │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px)       │
│ ====================================================================== │
│ [ HEADER BAR (<nav.bold-nav-full>     ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.hero_wrap>) — 390px Vertical Lead             | │
│ | H1: LA POSTAL                                                      | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.portrait_wrap) — 1-Col Stack              | │
│ | [ Item 1: October 30th, 2026                                     ] | │
│ | [ Item 2: We use cookies to enhance your browsing experien       ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.tl_wrap>) — 1-Col (Customise Consent )      | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer_wrap>) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.bold-nav-full> — `daddyyankee-com`)**:
   - Landmark `<nav class="bold-nav-full">` (`1440x900px`) hosting `Daddy Yankee · Official Website` navigation (`STORE · FOUNDATIONS · GLOBALIZATION · CRYSTALLIZATION · Store`), DOM attributes (`data-wf-domain="daddyyankee.com"`, `data-wf-page="6ab927d471adf53e60a6e4f4"`, `data-wf-site="6ab927d171adf53e60a6e4a4"`, `data-cky-tag="notice"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.hero_wrap> — `LA POSTAL`)**:
   - Landmark `<section class="hero_wrap u-section">` presenting display lead `LA POSTAL` and copy excerpt *"October 30th, 2026"* over `#ece8dc` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.portrait_wrap> — `October 30th, 2026`)**:
   - Landmark `<section class="portrait_wrap u-section">` rendering section `October 30th, 2026` with copy *"We use cookies to enhance your browsing experience, serve persona"*, asset references (`cdn.prod.website-files.com`, `daddy-yankee.webflow.shared.3af00...`, `script.js`, `gtm.js`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.tl_wrap> — `We use cookies to enhance your bro`)**:
   - Landmark `<section class="tl_wrap u-section">` framing `We use cookies to enhance your browsing experien` and `Customise Consent Preferences` (*"Customise Consent Preferences"*) with `#ffff00` surface cards, `#ff0000` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer_wrap> — `https://daddyyankee.com/`)**:
   - Landmark `<footer class="footer_wrap u-section">` anchoring `Daddy Yankee · Official Website` footer links (`STORE · FOUNDATIONS · GLOBALIZATION · CRYSTALLIZATION · Store`), copy *"We use cookies to help you navigate efficiently and perform "*, and `#e2e2e2` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: daddyyankee-com (Daddy Yankee · Official Website)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `daddyyankee-com` (**Daddy Yankee · Official Website** — `https://daddyyankee.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ece8dc` / `#ff0000`).
- **Identity & Domain Context**: The official Daddy Yankee website. Discover La Postal, his upcoming album, listen to his new single, and get the latest from Daddy Yankee.
- **Primary Substrate**: `#ece8dc` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#ff0000`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ece8dc` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#ff0000` accents.
  - **Grounded Typographic Hierarchy**: Pairs `ABC Diatype Compressed` for display copy (`LA POSTAL`) with `Inter Tight 500` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.9,0,.1,1)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `daddyyankee-com` in your global stylesheet:

:root {
  /* Daddy Yankee · Official Website (daddyyankee-com) — Live-Grounded CSS Variables */
  --_theme---background: var(--_swatch---swatch--cream); /* Canvas / Surface Token (daddyyankee-com) */
  --_typography---body-family: "Inter Tight 500",Arial,sans-serif; /* Typography / Scale Token (daddyyankee-com) */
  --_theme---body: var(--_swatch---swatch--black); /* Brand / Palette Token (daddyyankee-com) */
  --size-font: calc(var(--size-container)/(var(--size-container-ideal)/var(--size-unit))); /* Typography / Scale Token (daddyyankee-com) */
  --_typography---body-line-height: 1.2; /* Typography / Scale Token (daddyyankee-com) */
  --_typography---body-weight: 500; /* Design System Custom Token (daddyyankee-com) */
  --_typography---body-letter-space: -.03em; /* Layout / Spatial Grid Token (daddyyankee-com) */
  --_typography---heading-family: "ABC Diatype Compressed",Impact,sans-serif; /* Typography Ink Token (daddyyankee-com) */
  --text-style--64: 4em; /* Typography Ink Token (daddyyankee-com) */
  --_typography---heading-line-height: .8; /* Typography Ink Token (daddyyankee-com) */
  --_typography---heading-weight: 900; /* Typography Ink Token (daddyyankee-com) */
  --_typography---heading-letter-space: -.02em; /* Typography Ink Token (daddyyankee-com) */
  --text-style--32: 2em; /* Typography Ink Token (daddyyankee-com) */
  --site-margin: .75em; /* Layout / Spatial Grid Token (daddyyankee-com) */
  --_swatch---swatch--cream: #ece8dc; /* Brand / Palette Token (daddyyankee-com) */
  --nav--height: 4.5em; /* Layout / Spatial Grid Token (daddyyankee-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ece8dc` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in live computed `body` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#ffff00` — grounded in `mark { background: #ffff00 }`
- **Interactive Accent / Highlight**: `#ff0000` — grounded in `.hero_cta.is-red { color: red }` (`#ff0000`)
- **Secondary / Muted Copy**: `#efee32` — grounded in live computed `p` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#e2e2e2` — grounded in `blockquote { border-left: #e2e2e2 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `9px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding
- **Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`
- **Corner Radii**: `3px`, `100%`, `50%`, `4px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `ABC Diatype Compressed`
- **Body Font Stack**: `Inter Tight 500`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 420px`, `line-height: 336px`, `font-weight: 900`, `letter-spacing: -8.4px`)
- **H2 Section Rule**: live computed `h2` (`font-size: 420px`, `line-height: 336px`, `font-weight: 900`, `letter-spacing: -8.4px`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 19.2px`, `font-weight: 500`, `letter-spacing: -0.48px`); CSS variables `--_typography---body-family: "Inter Tight 500",Arial,sans-serif`, `--_theme---body: var(--_swatch---swatch--black)`, `--_typography---body-line-height: 1.2`
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 19.2px`, `font-weight: 500`, `letter-spacing: -0.48px`); CSS variables `--text-style--body-small: max(1em,16px)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `daddyyankee-com` (`Daddy Yankee · Official Website`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.bold-nav-full> — `daddyyankee-com`)**:
   - DOM & Selectors: Landmark `<nav class="bold-nav-full">` (`1440x900px`) hosting `Daddy Yankee · Official Website` navigation (`STORE · FOUNDATIONS · GLOBALIZATION · CRYSTALLIZATION · Store`), DOM attributes (`data-wf-domain="daddyyankee.com"`, `data-wf-page="6ab927d471adf53e60a6e4f4"`, `data-wf-site="6ab927d171adf53e60a6e4a4"`, `data-cky-tag="notice"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.bold-nav-full> — `daddyyankee-com`)` (`daddyyankee-com`) adapts across `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)` with `cubic-bezier(.9,0,.1,1)`, `cubic-bezier(.215,.61,.355,1)`, `cubic-bezier(.32,.72,0,1)` transitions and links `STORE · FOUNDATIONS · GLOBALIZATION · CRYSTALLIZATION · Store`.
2. **Hero Stage & Focal Lead (<section.hero_wrap> — `LA POSTAL`)**:
   - DOM & Selectors: Landmark `<section class="hero_wrap u-section">` presenting display lead `LA POSTAL` and copy excerpt *"October 30th, 2026"* over `#ece8dc` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#ece8dc` background with `#000000` headline `LA POSTAL`.
3. **Primary Showcase & Content Grid (<section.portrait_wrap> — `October 30th, 2026`)**:
   - DOM & Selectors: Landmark `<section class="portrait_wrap u-section">` rendering section `October 30th, 2026` with copy *"We use cookies to enhance your browsing experience, serve persona"*, asset references (`cdn.prod.website-files.com`, `daddy-yankee.webflow.shared.3af00...`, `script.js`, `gtm.js`), and grid rule `summary { display:block }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.portrait_wrap> — `October 30th, 2026`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `9px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.tl_wrap> — `We use cookies to enhance your bro`)**:
   - DOM & Selectors: Landmark `<section class="tl_wrap u-section">` framing `We use cookies to enhance your browsing experien` and `Customise Consent Preferences` (*"Customise Consent Preferences"*) with `#ffff00` surface cards, `#ff0000` accents, and `video { vertical-align:baseline;display:inline-block }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.tl_wrap> — `We use cookies to enhance your bro`)` uses `3px`, `100%`, `50%`, `4px` radii, `#ff0000` highlights, and assets (cdn.prod.website-files.com, daddy-yankee.webflow.shared.3af00..., script.js).
5. **Colophon & Global Directory Footer (<footer.footer_wrap> — `https://daddyyankee.com/`)**:
   - DOM & Selectors: Landmark `<footer class="footer_wrap u-section">` anchoring `Daddy Yankee · Official Website` footer links (`STORE · FOUNDATIONS · GLOBALIZATION · CRYSTALLIZATION · Store`), copy *"We use cookies to help you navigate efficiently and perform "*, and `#e2e2e2` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer_wrap> — `https://daddyyankee.com/`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `9px` lateral canvas padding with `16px` grid gap and attributes (data-wf-domain="daddyyankee.com", data-wf-page="6ab927d471adf53e60a6e4f4", data-wf-site="6ab927d171adf53e60a6e4a4").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"October 30th, 2026"*
- Copy Excerpt 2: *"We use cookies to enhance your browsing experience, serve personalised ads or cont..."*
- Copy Excerpt 3: *"Customise Consent Preferences"*
- Copy Excerpt 4: *"We use cookies to help you navigate efficiently and perform certain functions. You..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.9,0,.1,1)`, `cubic-bezier(.215,.61,.355,1)`, `cubic-bezier(.32,.72,0,1)`
- **Extracted Stylesheet Rules (`daddyyankee-com`)**:
- `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`
- `summary { display:block }`
- `video { vertical-align:baseline;display:inline-block }`
- `template { display:none }`
- `strong { font-weight:700 }`
- **Per-Selector Transition Rules**:
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `daddyyankee-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `daddyyankee-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `daddyyankee-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.9,0,.1,1)`)**: Governs interactive state transitions across `<nav.bold-nav-full>` and `<section.portrait_wrap>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `daddyyankee-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
