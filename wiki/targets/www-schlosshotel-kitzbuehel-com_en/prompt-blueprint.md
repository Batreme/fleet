---
title: "UI Prompt Blueprint: www-schlosshotel-kitzbuehel-com_en"
date: 2026-11-15
target: "www-schlosshotel-kitzbuehel-com_en"
status: analyzed
capture: specimen
capture_desktop: dom
capture_mobile: specimen
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#300316` canvas, `#FFFFFF` ink, `#6e4e5b` accent)"
---

# UI Design System & Master Generation Blueprint: www-schlosshotel-kitzbuehel-com_en

> **Schlosshotel Kitzbühel – a premium experience** (https://www.schlosshotel-kitzbuehel.com/en) — A beacon of elegance, exclusivity, and warmth – Schlosshotel Kitzbühel is a truly unparalleled retreat.

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Schlosshotel Kitzbühel – a premium experience** (`https://www.schlosshotel-kitzbuehel.com/en`). A beacon of elegance, exclusivity, and warmth – Schlosshotel Kitzbühel is a truly unparalleled retreat.
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#300316` canvas, `#FFFFFF` ink, `#6e4e5b` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#300316` (`var(--dna-tldr-bg)` in `:root`) paired with `#FFFFFF` primary typography and `#6e4e5b` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Assistant` for display copy (`Schlosshotel Kitzbühel`) with `lg` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1024px` container bounds (`gap: .3rem`, padding `8px`) with `cubic-bezier(0,0,0.25,1)` easing and Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×19288px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1024px` extracted from `www-schlosshotel-kitzbuehel-com_en` stylesheet.
- **Canvas Lateral Padding & Spacing**: `8px` lateral canvas padding with `.3rem` grid gap.
- **Border Radius Scale**: `50%`, `2px`, `3px`, `8px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1024px`, `gap: .3rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `8px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width: 1024px)`, `@media (max-width: 767px)`, `@media (min-width: 1025px)`, `@media (max-width: 480px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#300316` | `var(--dna-tldr-bg)` in `:root` |
| **Primary Typography Ink** | `#FFFFFF` | `var(--dna-tldr-text)` in `:root` |
| **Elevated Surface / Card Substrate** | `#000000` | `var(--bl-trigger-text)` in `:root` |
| **Interactive Accent / Highlight** | `#6e4e5b` | `var(--bl-color-secondary)` in `:root` |
| **Secondary / Muted Copy** | `#42041e` | `.MOD-Banner .MOD-Banner__frame { background-color: #42041e }` |
| **Structural Hairline Border** | `#fff` | `-OffersTeaser__item__request__w... { color: #fff }` |

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
- **Primary Body Stack**: `lg`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`line-height: 1.2`, `font-weight: 500`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 1em !important`, `line-height: 1.2`, `font-weight: 500`).
- **Body Copy**: rule `p` (`font-size: 12px`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(1rem,11.5vw,22.9em)`, `6.8em`, `4em`, `3.5em`, `2em`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,0.25,1)`, `cubic-bezier(0.215,0.61,0.355,1)`, `cubic-bezier(0.17,0.88,0.32,1.28)`.

### Per-Element Transition & Choreography Rules
- **Selector `nd="1"] .MOD-HorizontalTextSlider...`**: `transition: opacity .25s ease` extracted from `www-schlosshotel-kitzbuehel-com_en` stylesheet.
- **Selector `.MOD-ImageCollage .MOD-ImageColla...`**: `transition: opacity .4s` extracted from `www-schlosshotel-kitzbuehel-com_en` stylesheet.
- **Selector `easer .MOD-OffersTeaser__item__me...`**: `transition: background-color .5s ease-out` extracted from `www-schlosshotel-kitzbuehel-com_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,0.25,1)`)**: Governs interactive state transitions across `<header.SECT-Header>` and `<section.MOD-OffersTeaser>`.
- **Runtime Interaction Engine**: Integrates Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Schlosshotel Kitzbühel – a premium experie │
│ ====================================================================== │
│ [ <header.SECT-Header>     | Book · Enquire · Spa · Rooms and Suite ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.MOD-RoomsTeaser>                            |   │
│ | H1: Schlosshotel Kitzbühel                                       |   │
│ | Substrate: #300316    | Ink: #FFFFFF    | Accent: #6e4e5b        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.MOD-OffersTeaser>) max-w: 1024px         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Welcome to the threshold of  |  | For people of refined taste. | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .3rem ) | │
│ | [<header.SECT-Heade] -> [<section.MOD-Rooms] -> [<section.MOD-Offer] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.SECT-Footer>  ) | https://www.schlosshotel-kitzbuehe │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.SECT-Header> — `www-schlosshotel-kitzbuehel-com_en`)**:
   - Landmark `<header class="SECT-Header DNA-section">` hosting `Schlosshotel Kitzbühel – a premium e` navigation (`Book · Enquire · Spa · Rooms and Suites · Meetings & Events`), DOM attributes (`data-asset-id="Scss/presets"`, `data-asset-id="Scss/vendors"`, `data-asset-id="Globals/Main"`, `data-asset-id="Sections/Header"`), and stylesheet rule `from { transform:translateX(0) }`.
2. **Hero Stage & Focal Lead (<section.MOD-RoomsTeaser> — `Schlosshotel Kitzbühel`)**:
   - Landmark `<section class="MOD-RoomsTeaser DNA-module">` presenting display lead `Schlosshotel Kitzbühel` and copy excerpt *"Kitzbühel For families For sports enthusiasts For culture lovers "* over `#300316` canvas and `#FFFFFF` ink.
3. **Primary Showcase & Content Grid (<section.MOD-OffersTeaser> — `Welcome to the threshold of the ex`)**:
   - Landmark `<section class="MOD-OffersTeaser DNA-module">` rendering section `Welcome to the threshold of the extraordinary` with copy *"For sports enthusiasts"*, asset references (`favicon-96x96.png`, `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `.MOD-Banner .MOD-Banner__outer { display:flex }`.
4. **Interactive Detail & Feature Matrix (<section.MOD-Text> — `For people of refined taste. For y`)**:
   - Landmark `<section class="MOD-Text DNA-module">` framing `For people of refined taste. For you.` and `Schlosshotel offers Not for all. But definitely f...` (*"For culture lovers"*) with `#000000` surface cards, `#6e4e5b` accents, and `.MOD-Banner .MOD-Banner__frame { padding:6.5em 0;flex:1;position:relative;background-color:42041e;overflo... }`.
5. **Colophon & Global Directory Footer (<footer.SECT-Footer> — `https://www.schlosshotel-kitzbuehel.com/en`)**:
   - Landmark `<footer class="SECT-Footer DNA-section">` anchoring `Schlosshotel Kitzbühel – a premi` footer links (`Book · Enquire · Spa · Rooms and Suites · Meetings & Events`), copy *"Rooms and Suites Packages Inclusive services"*, and `#fff` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-schlosshotel-kitzbuehel-com_en (Schlosshotel Kitzbühel – a premium experience)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-schlosshotel-kitzbuehel-com_en` (**Schlosshotel Kitzbühel – a premium experience** — `https://www.schlosshotel-kitzbuehel.com/en`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#300316` canvas, `#FFFFFF` ink, `#6e4e5b` accent).
- **Identity & Domain Context**: A beacon of elegance, exclusivity, and warmth – Schlosshotel Kitzbühel is a truly unparalleled retreat.
- **Primary Substrate**: `#300316` (`var(--dna-tldr-bg)` in `:root`), **Primary Ink**: `#FFFFFF`, **Accent / Highlight**: `#6e4e5b`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#300316` (`var(--dna-tldr-bg)` in `:root`) paired with `#FFFFFF` primary typography and `#6e4e5b` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Assistant` for display copy (`Schlosshotel Kitzbühel`) with `lg` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1024px` container bounds (`gap: .3rem`, padding `8px`) with `cubic-bezier(0,0,0.25,1)` easing and Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-schlosshotel-kitzbuehel-com_en` in your global stylesheet:

:root {
  /* Schlosshotel Kitzbühel – a premium experience (www-schlosshotel-kitzbuehel-com_en) — Ground-Truth Extracted CSS Variables */
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
- **Primary Canvas Substrate**: `#300316` — grounded in `var(--dna-tldr-bg)` in `:root`
- **Primary Typography Ink**: `#FFFFFF` — grounded in `var(--dna-tldr-text)` in `:root`
- **Elevated Surface / Card Substrate**: `#000000` — grounded in `var(--bl-trigger-text)` in `:root`
- **Interactive Accent / Highlight**: `#6e4e5b` — grounded in `var(--bl-color-secondary)` in `:root`
- **Secondary / Muted Copy**: `#42041e` — grounded in `.MOD-Banner .MOD-Banner__frame { background-color: #42041e }`
- **Structural Hairline Border**: `#fff` — grounded in `-OffersTeaser__item__request__w... { color: #fff }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×19288px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1024px` extracted from `www-schlosshotel-kitzbuehel-com_en` stylesheet
- **Padding & Gutters**: `8px` lateral canvas padding with `.3rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1024px`, `gap: .3rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `8px` horizontal padding
- **Media Queries**: `@media (max-width: 1024px)`, `@media (max-width: 767px)`, `@media (min-width: 1025px)`, `@media (max-width: 480px)`
- **Corner Radii**: `50%`, `2px`, `3px`, `8px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Assistant`
- **Body Font Stack**: `lg`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: rule `h1` (`line-height: 1.2`, `font-weight: 500`)
- **H2 Section Rule**: rule `h2` (`font-size: 1em !important`, `line-height: 1.2`, `font-weight: 500`)
- **Body Copy Rule**: rule `p` (`font-size: 12px`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(1rem,11.5vw,22.9em)`, `6.8em`, `4em`, `3.5em`, `2em`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-schlosshotel-kitzbuehel-com_en` (`Schlosshotel Kitzbühel – a premium experience`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.SECT-Header> — `www-schlosshotel-kitzbuehel-com_en`)**:
   - DOM & Selectors: Landmark `<header class="SECT-Header DNA-section">` hosting `Schlosshotel Kitzbühel – a premium e` navigation (`Book · Enquire · Spa · Rooms and Suites · Meetings & Events`), DOM attributes (`data-asset-id="Scss/presets"`, `data-asset-id="Scss/vendors"`, `data-asset-id="Globals/Main"`, `data-asset-id="Sections/Header"`), and stylesheet rule `from { transform:translateX(0) }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.SECT-Header> — `www-schlosshotel-kitzbuehel-com_en`)` (`www-schlosshotel-kitzbuehel-com_en`) adapts across `@media (max-width: 1024px)`, `@media (max-width: 767px)`, `@media (min-width: 1025px)`, `@media (max-width: 480px)` with `cubic-bezier(0,0,0.25,1)`, `cubic-bezier(0.215,0.61,0.355,1)`, `cubic-bezier(0.17,0.88,0.32,1.28)` transitions and links `Book · Enquire · Spa · Rooms and Suites · Meetings & Events`.
2. **Hero Stage & Focal Lead (<section.MOD-RoomsTeaser> — `Schlosshotel Kitzbühel`)**:
   - DOM & Selectors: Landmark `<section class="MOD-RoomsTeaser DNA-module">` presenting display lead `Schlosshotel Kitzbühel` and copy excerpt *"Kitzbühel For families For sports enthusiasts For culture lovers "* over `#300316` canvas and `#FFFFFF` ink.
   - Responsive Contract: Hero stage (`1440×19288px` desktop / `390×2400px` mobile) sets `#300316` background with `#FFFFFF` headline `Schlosshotel Kitzbühel`.
3. **Primary Showcase & Content Grid (<section.MOD-OffersTeaser> — `Welcome to the threshold of the ex`)**:
   - DOM & Selectors: Landmark `<section class="MOD-OffersTeaser DNA-module">` rendering section `Welcome to the threshold of the extraordinary` with copy *"For sports enthusiasts"*, asset references (`favicon-96x96.png`, `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `.MOD-Banner .MOD-Banner__outer { display:flex }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.MOD-OffersTeaser> — `Welcome to the threshold of the ex`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1024px`, `gap: .3rem`) on desktop and Single-column vertical stack at `390px` viewport width with `8px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.MOD-Text> — `For people of refined taste. For y`)**:
   - DOM & Selectors: Landmark `<section class="MOD-Text DNA-module">` framing `For people of refined taste. For you.` and `Schlosshotel offers Not for all. But definitely f...` (*"For culture lovers"*) with `#000000` surface cards, `#6e4e5b` accents, and `.MOD-Banner .MOD-Banner__frame { padding:6.5em 0;flex:1;position:relative;background-color:42041e;overflo... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.MOD-Text> — `For people of refined taste. For y`)` uses `50%`, `2px`, `3px`, `8px` radii, `#6e4e5b` highlights, and assets (favicon-96x96.png, favicon.svg, favicon.ico).
5. **Colophon & Global Directory Footer (<footer.SECT-Footer> — `https://www.schlosshotel-kitzbuehel.com/en`)**:
   - DOM & Selectors: Landmark `<footer class="SECT-Footer DNA-section">` anchoring `Schlosshotel Kitzbühel – a premi` footer links (`Book · Enquire · Spa · Rooms and Suites · Meetings & Events`), copy *"Rooms and Suites Packages Inclusive services"*, and `#fff` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.SECT-Footer> — `https://www.schlosshotel-kitzbuehel.com/en`)` aligns to `1024px` extracted from `www-schlosshotel-kitzbuehel-com_en` stylesheet with `8px` lateral canvas padding with `.3rem` grid gap and attributes (data-asset-id="Scss/presets", data-asset-id="Scss/vendors", data-asset-id="Globals/Main").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Kitzbühel For families For sports enthusiasts For culture lovers Concierge tips"*
- Copy Excerpt 2: *"For sports enthusiasts"*
- Copy Excerpt 3: *"For culture lovers"*
- Copy Excerpt 4: *"Rooms and Suites Packages Inclusive services"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,0.25,1)`, `cubic-bezier(0.215,0.61,0.355,1)`, `cubic-bezier(0.17,0.88,0.32,1.28)`
- **Extracted Stylesheet Rules (`www-schlosshotel-kitzbuehel-com_en`)**:
- `from { transform:translateX(0) }`
- `.MOD-Banner .MOD-Banner__outer { display:flex }`
- `.MOD-Banner .MOD-Banner__frame { padding:6.5em 0;flex:1;position:relative;background-color:42041e;overflo... }`
- `.MOD-Banner .MOD-Banner__image { width:33.5em }`
- `img { height:100%;object-fit:cover }`
- **Per-Selector Transition Rules**:
- **Selector `nd="1"] .MOD-HorizontalTextSlider...`**: `transition: opacity .25s ease` extracted from `www-schlosshotel-kitzbuehel-com_en` stylesheet.
- **Selector `.MOD-ImageCollage .MOD-ImageColla...`**: `transition: opacity .4s` extracted from `www-schlosshotel-kitzbuehel-com_en` stylesheet.
- **Selector `easer .MOD-OffersTeaser__item__me...`**: `transition: background-color .5s ease-out` extracted from `www-schlosshotel-kitzbuehel-com_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,0.25,1)`)**: Governs interactive state transitions across `<header.SECT-Header>` and `<section.MOD-OffersTeaser>`.
- **Runtime Interaction Engine**: Integrates Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-schlosshotel-kitzbuehel-com_en`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
