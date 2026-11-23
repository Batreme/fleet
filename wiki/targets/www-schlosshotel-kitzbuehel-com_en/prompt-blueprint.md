---
title: "UI Prompt Blueprint: www-schlosshotel-kitzbuehel-com_en"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-schlosshotel-kitzbuehel-com_en"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#300316` canvas, `#ffffff` ink, `#42041e` accent)"
---

# UI Design System & Master Generation Blueprint: www-schlosshotel-kitzbuehel-com_en

> **Schlosshotel Kitzbühel – a premium experience** (https://www.schlosshotel-kitzbuehel.com/en) — A beacon of elegance, exclusivity, and warmth – Schlosshotel Kitzbühel is a truly unparalleled retreat.

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Schlosshotel Kitzbühel – a premium experience** (`https://www.schlosshotel-kitzbuehel.com/en`). A beacon of elegance, exclusivity, and warmth – Schlosshotel Kitzbühel is a truly unparalleled retreat.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#300316` canvas, `#ffffff` ink, `#42041e` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#300316` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#42041e` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Assistant` for display copy (`SCHLOSSHOTEL KITZBÜHEL`) with `Assistant` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1360px` container bounds (`gap: .3rem`, padding `8px`) with `cubic-bezier(0,0,0.25,1)` easing and Lenis Smooth Scroll (`data-lenis`), Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1360px` (measured widest bounded `<section>` landmark width on `1440px` desktop).
- **Canvas Lateral Padding & Spacing**: `8px` lateral canvas padding with `.3rem` grid gap.
- **Border Radius Scale**: `2px`, `50%`, `3px`, `8px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1360px`, `gap: .3rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `8px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width: 1366px)`, `@media (max-width: 1024px)`, `@media (max-width: 767px)`, `@media (max-width: 480px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#300316` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#42041e` | `.branDNAmic .DNA-button--cta-bo... { color: #42041e }` |
| **Secondary / Muted Copy** | `#999999` | live computed `button` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#999999` | `blockquote { border: #999999 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--dna-tldr-bg` | `#300316` | Canvas / Surface Token |
| `--dna-tldr-text` | `#FFFFFF` | Typography Ink Token |
| `--dna-tldr-fs-desktop` | `2.1em` | Dimension / Scale Token |
| `--dna-tldr-fs-mobile` | `1.6em` | Dimension / Scale Token |
| `--track-width` | `52px` | Layout / Spatial Grid Token |
| `--track-height` | `28px` | Layout / Spatial Grid Token |
| `--thumb-size` | `23px` | Layout / Spatial Grid Token |
| `--thumb-gap` | `3px` | Layout / Spatial Grid Token |
| `--track-radius` | `999px` | Elevation / Border Token |
| `--vh` | `9px` | Layout / Spatial Grid Token |
| `--bl-size` | `40px` | Layout / Spatial Grid Token |
| `--bl-desktop-top` | `auto` | Design System Custom Token |
| `--bl-desktop-bottom` | `1.5em` | Dimension / Scale Token |
| `--bl-desktop-left` | `1.5em` | Dimension / Scale Token |
| `--bl-desktop-right` | `auto` | Design System Custom Token |
| `--bl-desktop-box-left` | `1.5em` | Dimension / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Assistant`.
- **Primary Body Stack**: `Assistant`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 9.008px`, `line-height: 10.8096px`, `font-weight: 600`, `letter-spacing: 2.2px`); rule `h1` (`line-height: 1.2`, `font-weight: 500`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 18.9168px`, `line-height: 29.5102px`, `font-weight: 700`); rule `h2` (`font-size: 1em`, `line-height: 1.2`, `font-weight: 500`).
- **Body Copy**: live computed `body` (`font-size: 9.008px`, `line-height: 14.0525px`, `font-weight: 400`); rule `p` (`font-size: 12px`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 9.008px`, `line-height: 14.0525px`, `font-weight: 400`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,0.25,1)`, `cubic-bezier(0.215,0.61,0.355,1)`, `cubic-bezier(0.17,0.88,0.32,1.28)`.

### Per-Element Transition & Choreography Rules
- **Selector `.MOD-Quotes .MOD-Quotes__rte__con...`**: `transition: opacity .2s` extracted from `www-schlosshotel-kitzbuehel-com_en` stylesheet.
- **Selector `.MOD-Quotes .MOD-Quotes__author>a`**: `transition: opacity .2s` extracted from `www-schlosshotel-kitzbuehel-com_en` stylesheet.
- **Selector `data-background="1"] .MOD-Quotes_...`**: `transition: opacity .25s ease` extracted from `www-schlosshotel-kitzbuehel-com_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,0.25,1)`)**: Governs interactive state transitions across `<header.SECT-Header>` and `<section.MOD-OffersTeaser>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Schlosshotel Kitzbühel – a premium experie │
│ ====================================================================== │
│ [ <header.SECT-Header> (1440x0px)     | Book · Enquire · Spa · Rooms ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.MOD-RoomsTeaser> (w=1440px)                   | │
│ | H1: SCHLOSSHOTEL KITZBÜHEL                                         | │
│ | Substrate: #300316 | Ink: #ffffff | Accent: #42041e                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.MOD-OffersTeaser>) max-w: 1360px           | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Schlosshotel Kitzbühel       |  | Welcome to the threshold of  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.MOD-Text>) — For people of refined         | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.SECT-Footer>) | https://www.schlosshotel-kitzbuehel  │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .3rem)      │
│ ====================================================================== │
│ [ HEADER BAR (<header.SECT-Header>    ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.MOD-RoomsTeaser) — 390px Vertical Lead        | │
│ | H1: SCHLOSSHOTEL KITZBÜHEL                                         | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.MOD-OffersTea) — 1-Col Stack              | │
│ | [ Item 1: Schlosshotel Kitzbühel                                 ] | │
│ | [ Item 2: Welcome to the threshold of the extraordinary          ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.MOD-Text>) — 1-Col (For people of refi)     | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.SECT-Footer>) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.SECT-Header> — `www-schlosshotel-kitzbuehel-com_en`)**:
   - Landmark `<header class="SECT-Header DNA-section">` (`1440x0px`) hosting `Schlosshotel Kitzbühel – a premium e` navigation (`Book · Enquire · Spa · Rooms and Suites · Meetings & Events`), DOM attributes (`data-asset-id="Scss/presets"`, `data-asset-id="Scss/vendors"`, `data-asset-id="Globals/Main"`, `data-asset-id="Sections/Header"`), and stylesheet rule `from { transform:translateX(0) }`.
2. **Hero Stage & Focal Lead (<section.MOD-RoomsTeaser> — `SCHLOSSHOTEL KITZBÜHEL`)**:
   - Landmark `<section class="MOD-RoomsTeaser DNA-module">` presenting display lead `SCHLOSSHOTEL KITZBÜHEL` and copy excerpt *"Some places whisper rather than shout. Schlosshotel Kitzbühel is "* over `#300316` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.MOD-OffersTeaser> — `Schlosshotel Kitzbühel`)**:
   - Landmark `<section class="MOD-OffersTeaser DNA-module">` rendering section `Schlosshotel Kitzbühel` with copy *"Schlosshotel Kitzbühel"*, asset references (`favicon-96x96.png`, `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `page { margin:.5cm }`.
4. **Interactive Detail & Feature Matrix (<section.MOD-Text> — `Welcome to the threshold of the ex`)**:
   - Landmark `<section class="MOD-Text DNA-module">` framing `Welcome to the threshold of the extraordinary` and `For people of refined taste. For you.` (*"Welcome to the threshold of the extraordinary"*) with `#000000` surface cards, `#42041e` accents, and `body { font-family:Arial,sans-serif;font-size:12px }`.
5. **Colophon & Global Directory Footer (<footer.SECT-Footer> — `https://www.schlosshotel-kitzbuehel.com/en`)**:
   - Landmark `<footer class="SECT-Footer DNA-section">` anchoring `Schlosshotel Kitzbühel – a premi` footer links (`Book · Enquire · Spa · Rooms and Suites · Meetings & Events`), copy *"No flashy façade. No hollow shine. Instead: real stone benea"*, and `#999999` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-schlosshotel-kitzbuehel-com_en (Schlosshotel Kitzbühel – a premium experience)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-schlosshotel-kitzbuehel-com_en` (**Schlosshotel Kitzbühel – a premium experience** — `https://www.schlosshotel-kitzbuehel.com/en`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#300316` canvas, `#ffffff` ink, `#42041e` accent).
- **Identity & Domain Context**: A beacon of elegance, exclusivity, and warmth – Schlosshotel Kitzbühel is a truly unparalleled retreat.
- **Primary Substrate**: `#300316` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#42041e`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#300316` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#42041e` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Assistant` for display copy (`SCHLOSSHOTEL KITZBÜHEL`) with `Assistant` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1360px` container bounds (`gap: .3rem`, padding `8px`) with `cubic-bezier(0,0,0.25,1)` easing and Lenis Smooth Scroll (`data-lenis`), Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-schlosshotel-kitzbuehel-com_en` in your global stylesheet:

:root {
  /* Schlosshotel Kitzbühel – a premium experience (www-schlosshotel-kitzbuehel-com_en) — Live-Grounded CSS Variables */
  --dna-tldr-bg: #300316; /* Canvas / Surface Token (www-schlosshotel-kitzbuehel-com_en) */
  --dna-tldr-text: #FFFFFF; /* Typography Ink Token (www-schlosshotel-kitzbuehel-com_en) */
  --dna-tldr-fs-desktop: 2.1em; /* Dimension / Scale Token (www-schlosshotel-kitzbuehel-com_en) */
  --dna-tldr-fs-mobile: 1.6em; /* Dimension / Scale Token (www-schlosshotel-kitzbuehel-com_en) */
  --track-width: 52px; /* Layout / Spatial Grid Token (www-schlosshotel-kitzbuehel-com_en) */
  --track-height: 28px; /* Layout / Spatial Grid Token (www-schlosshotel-kitzbuehel-com_en) */
  --thumb-size: 23px; /* Layout / Spatial Grid Token (www-schlosshotel-kitzbuehel-com_en) */
  --thumb-gap: 3px; /* Layout / Spatial Grid Token (www-schlosshotel-kitzbuehel-com_en) */
  --track-radius: 999px; /* Elevation / Border Token (www-schlosshotel-kitzbuehel-com_en) */
  --vh: 9px; /* Layout / Spatial Grid Token (www-schlosshotel-kitzbuehel-com_en) */
  --bl-size: 40px; /* Layout / Spatial Grid Token (www-schlosshotel-kitzbuehel-com_en) */
  --bl-desktop-top: auto; /* Design System Custom Token (www-schlosshotel-kitzbuehel-com_en) */
  --bl-desktop-bottom: 1.5em; /* Dimension / Scale Token (www-schlosshotel-kitzbuehel-com_en) */
  --bl-desktop-left: 1.5em; /* Dimension / Scale Token (www-schlosshotel-kitzbuehel-com_en) */
  --bl-desktop-right: auto; /* Design System Custom Token (www-schlosshotel-kitzbuehel-com_en) */
  --bl-desktop-box-left: 1.5em; /* Dimension / Scale Token (www-schlosshotel-kitzbuehel-com_en) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#300316` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#ffffff` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#000000` — grounded in live computed `button` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#42041e` — grounded in `.branDNAmic .DNA-button--cta-bo... { color: #42041e }`
- **Secondary / Muted Copy**: `#999999` — grounded in live computed `button` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#999999` — grounded in `blockquote { border: #999999 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1360px` (measured widest bounded `<section>` landmark width on `1440px` desktop)
- **Padding & Gutters**: `8px` lateral canvas padding with `.3rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1360px`, `gap: .3rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `8px` horizontal padding
- **Media Queries**: `@media (max-width: 1366px)`, `@media (max-width: 1024px)`, `@media (max-width: 767px)`, `@media (max-width: 480px)`
- **Corner Radii**: `2px`, `50%`, `3px`, `8px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Assistant`
- **Body Font Stack**: `Assistant`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: live computed `h1` (`font-size: 9.008px`, `line-height: 10.8096px`, `font-weight: 600`, `letter-spacing: 2.2px`); rule `h1` (`line-height: 1.2`, `font-weight: 500`)
- **H2 Section Rule**: live computed `h2` (`font-size: 18.9168px`, `line-height: 29.5102px`, `font-weight: 700`); rule `h2` (`font-size: 1em`, `line-height: 1.2`, `font-weight: 500`)
- **Body Copy Rule**: live computed `body` (`font-size: 9.008px`, `line-height: 14.0525px`, `font-weight: 400`); rule `p` (`font-size: 12px`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 9.008px`, `line-height: 14.0525px`, `font-weight: 400`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-schlosshotel-kitzbuehel-com_en` (`Schlosshotel Kitzbühel – a premium experience`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.SECT-Header> — `www-schlosshotel-kitzbuehel-com_en`)**:
   - DOM & Selectors: Landmark `<header class="SECT-Header DNA-section">` (`1440x0px`) hosting `Schlosshotel Kitzbühel – a premium e` navigation (`Book · Enquire · Spa · Rooms and Suites · Meetings & Events`), DOM attributes (`data-asset-id="Scss/presets"`, `data-asset-id="Scss/vendors"`, `data-asset-id="Globals/Main"`, `data-asset-id="Sections/Header"`), and stylesheet rule `from { transform:translateX(0) }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.SECT-Header> — `www-schlosshotel-kitzbuehel-com_en`)` (`www-schlosshotel-kitzbuehel-com_en`) adapts across `@media (max-width: 1366px)`, `@media (max-width: 1024px)`, `@media (max-width: 767px)`, `@media (max-width: 480px)` with `cubic-bezier(0,0,0.25,1)`, `cubic-bezier(0.215,0.61,0.355,1)`, `cubic-bezier(0.17,0.88,0.32,1.28)` transitions and links `Book · Enquire · Spa · Rooms and Suites · Meetings & Events`.
2. **Hero Stage & Focal Lead (<section.MOD-RoomsTeaser> — `SCHLOSSHOTEL KITZBÜHEL`)**:
   - DOM & Selectors: Landmark `<section class="MOD-RoomsTeaser DNA-module">` presenting display lead `SCHLOSSHOTEL KITZBÜHEL` and copy excerpt *"Some places whisper rather than shout. Schlosshotel Kitzbühel is "* over `#300316` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#300316` background with `#ffffff` headline `SCHLOSSHOTEL KITZBÜHEL`.
3. **Primary Showcase & Content Grid (<section.MOD-OffersTeaser> — `Schlosshotel Kitzbühel`)**:
   - DOM & Selectors: Landmark `<section class="MOD-OffersTeaser DNA-module">` rendering section `Schlosshotel Kitzbühel` with copy *"Schlosshotel Kitzbühel"*, asset references (`favicon-96x96.png`, `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `page { margin:.5cm }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.MOD-OffersTeaser> — `Schlosshotel Kitzbühel`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1360px`, `gap: .3rem`) on desktop and Single-column vertical stack at `390px` viewport width with `8px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.MOD-Text> — `Welcome to the threshold of the ex`)**:
   - DOM & Selectors: Landmark `<section class="MOD-Text DNA-module">` framing `Welcome to the threshold of the extraordinary` and `For people of refined taste. For you.` (*"Welcome to the threshold of the extraordinary"*) with `#000000` surface cards, `#42041e` accents, and `body { font-family:Arial,sans-serif;font-size:12px }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.MOD-Text> — `Welcome to the threshold of the ex`)` uses `2px`, `50%`, `3px`, `8px` radii, `#42041e` highlights, and assets (favicon-96x96.png, favicon.svg, favicon.ico).
5. **Colophon & Global Directory Footer (<footer.SECT-Footer> — `https://www.schlosshotel-kitzbuehel.com/en`)**:
   - DOM & Selectors: Landmark `<footer class="SECT-Footer DNA-section">` anchoring `Schlosshotel Kitzbühel – a premi` footer links (`Book · Enquire · Spa · Rooms and Suites · Meetings & Events`), copy *"No flashy façade. No hollow shine. Instead: real stone benea"*, and `#999999` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.SECT-Footer> — `https://www.schlosshotel-kitzbuehel.com/en`)` aligns to `1360px` (measured widest bounded `<section>` landmark width on `1440px` desktop) with `8px` lateral canvas padding with `.3rem` grid gap and attributes (data-asset-id="Scss/presets", data-asset-id="Scss/vendors", data-asset-id="Globals/Main").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Some places whisper rather than shout. Schlosshotel Kitzbühel is one of them."*
- Copy Excerpt 2: *"Schlosshotel Kitzbühel"*
- Copy Excerpt 3: *"Welcome to the threshold of the extraordinary"*
- Copy Excerpt 4: *"No flashy façade. No hollow shine. Instead: real stone beneath your fingertips. Ha..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,0.25,1)`, `cubic-bezier(0.215,0.61,0.355,1)`, `cubic-bezier(0.17,0.88,0.32,1.28)`
- **Extracted Stylesheet Rules (`www-schlosshotel-kitzbuehel-com_en`)**:
- `from { transform:translateX(0) }`
- `page { margin:.5cm }`
- `body { font-family:Arial,sans-serif;font-size:12px }`
- `a:visited { text-decoration:none }`
- `after { display:none }`
- **Per-Selector Transition Rules**:
- **Selector `.MOD-Quotes .MOD-Quotes__rte__con...`**: `transition: opacity .2s` extracted from `www-schlosshotel-kitzbuehel-com_en` stylesheet.
- **Selector `.MOD-Quotes .MOD-Quotes__author>a`**: `transition: opacity .2s` extracted from `www-schlosshotel-kitzbuehel-com_en` stylesheet.
- **Selector `data-background="1"] .MOD-Quotes_...`**: `transition: opacity .25s ease` extracted from `www-schlosshotel-kitzbuehel-com_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,0.25,1)`)**: Governs interactive state transitions across `<header.SECT-Header>` and `<section.MOD-OffersTeaser>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-schlosshotel-kitzbuehel-com_en`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
