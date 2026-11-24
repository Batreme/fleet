---
title: "UI Prompt Blueprint: dairyfoodbg-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "dairyfoodbg-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: native
desktop_keyframes: 8
subpages_crawled: 3
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#0000ff`)"
---

# UI Design System & Master Generation Blueprint: dairyfoodbg-com

> **Dairy Food Bulgaria — Private-Label UHT Dairy Manufacturer** (https://dairyfoodbg.com/) — Private-label manufacturer of UHT milk, creams and protein drinks. Four aseptic filling lines, 28 export markets, co-development from rec...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x1744)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Dairy Food Bulgaria — Private-Label UHT Dairy Manufacturer** (`https://dairyfoodbg.com/`). Private-label manufacturer of UHT milk, creams and protein drinks. Four aseptic filling lines, 28 export markets, co-development from rec...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#0000ff`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#0d2759` primary typography and `#0000ff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Verdana` for display copy (`Elevate your brand`) with `Albertsans` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 3.25px 16.25px`, padding `32px`) with `cubic-bezier(.625,.05,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=14400px` / doc `22545px`), Mobile `390×1744px` (`assets/mobile-journey.webp`, `2` keyframes).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `32px` lateral canvas padding with `3.25px 16.25px` grid gap.
- **Border Radius Scale**: `9999px`, `7px`, `3px`, `100%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 3.25px 16.25px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `32px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0d2759` | live computed `nav` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#d7ecf6` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0000ff` | `.eu-bar__link { color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#6b6b6b` | `var(--cc-color-muted)` in `:root` |
| **Structural Hairline Border** | `#e0e5f0` | `var(--_colors---semantic--border)` in `:root` (`21489524`) |
| **Variable Token (`--_colors---brand--green-hover`)** | `#2e7031` | `var(--_colors---brand--green-hover)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_type---family--body` | `Albertsans,Verdana,sans-serif` | Typography / Scale Token |
| `--_colors---semantic--content-primary` | `var(--_colors---neutral--700)` | Brand / Palette Token |
| `--_type---scale--base` | `1em` | Typography / Scale Token |
| `--_type---weight--regular` | `400` | Typography / Scale Token |
| `--_padding---section--lg` | `7.5em` | Layout / Spatial Grid Token |
| `--_padding---container--page` | `1.25em` | Layout / Spatial Grid Token |
| `--_padding---section--md` | `5em` | Layout / Spatial Grid Token |
| `--_colors---semantic--bg` | `var(--_colors---brand--cloud)` | Canvas / Surface Token |
| `--_component---sizing--container-small` | `64em` | Layout / Spatial Grid Token |
| `--_space---2xl` | `3em` | Layout / Spatial Grid Token |
| `--_space---sm` | `.5em` | Layout / Spatial Grid Token |
| `--_colors---brand--green-hover` | `#2e7031` | Brand / Palette Token |
| `--_type---scale--xs` | `.75em` | Typography / Scale Token |
| `--_type---weight--semibold` | `600` | Typography / Scale Token |
| `--_type---tracking--eyebrow` | `.2em` | Typography / Scale Token |
| `--_type---family--display` | `Bricolagegrotesquesemicondensed,Verdana,sans-serif` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Verdana`.
- **Primary Body Stack**: `Albertsans`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 64px`, `line-height: 64px`, `font-weight: 400`); CSS variables `--_type---family--display: Bricolagegrotesquesemicondensed,Verdana,sans-serif`, `--_type---leading--display: 1`, `--_type---scale--display: 6em`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 40px`, `line-height: 44px`, `font-weight: 400`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 19.2px`, `font-weight: 400`); CSS variables `--_type---family--body: Albertsans,Verdana,sans-serif`, `--_type---leading--body: 1.5`, `--_type---tracking--body: 0em`; rule `body` (`font-size: var(--size-font)`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 13px`, `line-height: 19.5px`, `font-weight: 400`); CSS variables `--_component---sizing--container-small: 64em`, `--_component---sizing--container-x-small: 48em`, `--cc-font-family-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.625,.05,0,1)`, `cubic-bezier(.34,1.3,.64,1)`, `cubic-bezier(.22,1,.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `dairyfoodbg-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `dairyfoodbg-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `dairyfoodbg-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.625,.05,0,1)`)**: Governs interactive state transitions across `<header.navbar>` and `<section.about>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `22545px`, deepest scrollY reached `14400px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `Lenis`, `GSAP/ScrollTrigger`, `WebGL/Canvas`.
- **Hover Physics (`primary_cta` · `Start Your Project`)**: `transform`: `none` -> `matrix(1.04198, 0, 0, 1...`; `backgroundColor`: `rgb(55, 134, 58)` -> `rgb(46, 112, 49)` (`transition-duration: 0.45s`, `timing: cubic-bezier(0.625, 0.05, 0, 1)`).
- **Route Transition Architecture**: First internal navigation (`/products`) measured as `direct` in `448ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Dairy Food Bulgaria — Private-Label UHT Da │
│ ====================================================================== │
│ [ <header.navbar> (1440x57px)         | Home · About · Products · Pa ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero> (w=1440px)                              | │
│ | H1: Elevate your brand                                             | │
│ | Substrate: #ffffff | Ink: #0d2759 | Accent: #0000ff                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.about>) max-w: 1440px                      | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Traditional craftsmanship wi |  | Customizable Products        | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.home-products>) — Flexible Packaging       | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>) | https://dairyfoodbg.com/             │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 3.25px 1)   │
│ ====================================================================== │
│ [ HEADER BAR (<header.navbar>         ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.hero>) — 390px Vertical Lead                  | │
│ | H1: Elevate your brand                                             | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.about>) — 1-Col Stack                     | │
│ | [ Item 1: Traditional craftsmanship with modern UHT technol...   ] | │
│ | [ Item 2: Customizable Products                                  ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.home-products>) — 1-Col (Flexible Packaging)  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.navbar> — `dairyfoodbg-com`)**:
   - Landmark `<header class="navbar">` (`1440x57px`) hosting `Dairy Food Bulgaria — Private-Label ` navigation (`Home · About · Products · Packaging · Catalog`), DOM attributes (`data-wf-domain="dairyfoodbg.com"`, `data-wf-page="6a450776d63ee937af4d29d7"`, `data-wf-site="6a450773d63ee937af4d28ea"`, `data-cc="analytics"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Elevate your brand`)**:
   - Landmark `<section class="hero">` presenting display lead `Elevate your brand` and copy excerpt *"From product development and packaging to large-scale manufacturi"* over `#ffffff` canvas and `#0d2759` ink.
3. **Primary Showcase & Content Grid (<section.about> — `Traditional craftsmanship with mod`)**:
   - Landmark `<section class="about">` rendering section `Traditional craftsmanship with modern UHT technol...` with copy *"Leading producer of private-label UHT dairy in Bulgaria. Leading "*, asset references (`cdn.prod.website-files.com`, `dairy-food.shared.ce91a50f0.min.css`, `dairy-food.6a450776d63ee937af4d29...`, `6abf58390100a7826e7f0b59_favicon-...`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.home-products> — `Customizable Products`)**:
   - Landmark `<section class="home-products">` framing `Customizable Products` and `Flexible Packaging` (*"Leading producer of private-label UHT dairy in Bulgaria."*) with `#d7ecf6` surface cards, `#0000ff` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://dairyfoodbg.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Dairy Food Bulgaria — Private-La` footer links (`Home · About · Products · Packaging · Catalog`), copy *"Start Your Project"*, and `#e0e5f0` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `Elevate your brand` · sticky/fixed elements: `4`
- **Step 02** (`y=850px`, `4%`): Active landmark `Elevate your brand` · sticky/fixed elements: `3`
- **Step 03** (`y=4250px`, `20%`): Active landmark `This site uses cookies` · sticky/fixed elements: `3`
- **Step 04** (`y=5950px`, `27%`): Active landmark `Products we produce under your brand` · sticky/fixed elements: `3`
- **Step 05** (`y=10200px`, `47%`): Active landmark `This site uses cookies` · sticky/fixed elements: `3`
- **Step 06** (`y=11900px`, `55%`): Active landmark `This site uses cookies` · sticky/fixed elements: `3`
- **Step 07** (`y=13600px`, `63%`): Active landmark `This site uses cookies` · sticky/fixed elements: `3`
- **Step 08** (`y=14400px`, `67%`): Active landmark `End-to-End. Built to Scale.` · sticky/fixed elements: `4`

### Multi-Page Internal Route Map
- **Listing Route (`/products`)**: `https://dairyfoodbg.com/products` — H1: `What Can We Produce for Your Brand?`, scrollHeight `3383px`, transition `direct` (`448ms`)
- **About Route (`/contact`)**: `https://dairyfoodbg.com/contact` — H1: `Get in Touch`, scrollHeight `1636px`, transition `direct` (`452ms`)
- **Listing Route (`/catalog`)**: `https://dairyfoodbg.com/catalog` — H1: `Our production range`, scrollHeight `9696px`, transition `direct` (`620ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: dairyfoodbg-com (Dairy Food Bulgaria — Private-Label UHT Dairy Manufacturer)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `dairyfoodbg-com` (**Dairy Food Bulgaria — Private-Label UHT Dairy Manufacturer** — `https://dairyfoodbg.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#0000ff`).
- **Identity & Domain Context**: Private-label manufacturer of UHT milk, creams and protein drinks. Four aseptic filling lines, 28 export markets, co-development from rec...
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#0d2759`, **Accent / Highlight**: `#0000ff`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#0d2759` primary typography and `#0000ff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Verdana` for display copy (`Elevate your brand`) with `Albertsans` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 3.25px 16.25px`, padding `32px`) with `cubic-bezier(.625,.05,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `dairyfoodbg-com` in your global stylesheet:

:root {
  /* Dairy Food Bulgaria — Private-Label UHT Dairy Manufacturer (dairyfoodbg-com) — Live-Grounded CSS Variables */
  --_type---family--body: Albertsans,Verdana,sans-serif; /* Typography / Scale Token (dairyfoodbg-com) */
  --_colors---semantic--content-primary: var(--_colors---neutral--700); /* Brand / Palette Token (dairyfoodbg-com) */
  --_type---scale--base: 1em; /* Typography / Scale Token (dairyfoodbg-com) */
  --_type---weight--regular: 400; /* Typography / Scale Token (dairyfoodbg-com) */
  --_padding---section--lg: 7.5em; /* Layout / Spatial Grid Token (dairyfoodbg-com) */
  --_padding---container--page: 1.25em; /* Layout / Spatial Grid Token (dairyfoodbg-com) */
  --_padding---section--md: 5em; /* Layout / Spatial Grid Token (dairyfoodbg-com) */
  --_colors---semantic--bg: var(--_colors---brand--cloud); /* Canvas / Surface Token (dairyfoodbg-com) */
  --_component---sizing--container-small: 64em; /* Layout / Spatial Grid Token (dairyfoodbg-com) */
  --_space---2xl: 3em; /* Layout / Spatial Grid Token (dairyfoodbg-com) */
  --_space---sm: .5em; /* Layout / Spatial Grid Token (dairyfoodbg-com) */
  --_colors---brand--green-hover: #2e7031; /* Brand / Palette Token (dairyfoodbg-com) */
  --_type---scale--xs: .75em; /* Typography / Scale Token (dairyfoodbg-com) */
  --_type---weight--semibold: 600; /* Typography / Scale Token (dairyfoodbg-com) */
  --_type---tracking--eyebrow: .2em; /* Typography / Scale Token (dairyfoodbg-com) */
  --_type---family--display: Bricolagegrotesquesemicondensed,Verdana,sans-serif; /* Typography / Scale Token (dairyfoodbg-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#0d2759` — grounded in live computed `nav` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#d7ecf6` — grounded in live computed `footer` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#0000ff` — grounded in `.eu-bar__link { color: blue }` (`#0000ff`)
- **Secondary / Muted Copy**: `#6b6b6b` — grounded in `var(--cc-color-muted)` in `:root`
- **Structural Hairline Border**: `#e0e5f0` — grounded in `var(--_colors---semantic--border)` in `:root` (`21489524`)
- **Variable Token (`--_colors---brand--green-hover`)**: `#2e7031` — grounded in `var(--_colors---brand--green-hover)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×1744px` (full-page live capture (1744px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `32px` lateral canvas padding with `3.25px 16.25px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 3.25px 16.25px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `32px` horizontal padding
- **Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`
- **Corner Radii**: `9999px`, `7px`, `3px`, `100%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Verdana`
- **Body Font Stack**: `Albertsans`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: live computed `h1` (`font-size: 64px`, `line-height: 64px`, `font-weight: 400`); CSS variables `--_type---family--display: Bricolagegrotesquesemicondensed,Verdana,sans-serif`, `--_type---leading--display: 1`, `--_type---scale--display: 6em`
- **H2 Section Rule**: live computed `h2` (`font-size: 40px`, `line-height: 44px`, `font-weight: 400`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 19.2px`, `font-weight: 400`); CSS variables `--_type---family--body: Albertsans,Verdana,sans-serif`, `--_type---leading--body: 1.5`, `--_type---tracking--body: 0em`; rule `body` (`font-size: var(--size-font)`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 13px`, `line-height: 19.5px`, `font-weight: 400`); CSS variables `--_component---sizing--container-small: 64em`, `--_component---sizing--container-x-small: 48em`, `--cc-font-family-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `dairyfoodbg-com` (`Dairy Food Bulgaria — Private-Label UHT Dairy Manufacturer`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.navbar> — `dairyfoodbg-com`)**:
   - DOM & Selectors: Landmark `<header class="navbar">` (`1440x57px`) hosting `Dairy Food Bulgaria — Private-Label ` navigation (`Home · About · Products · Packaging · Catalog`), DOM attributes (`data-wf-domain="dairyfoodbg.com"`, `data-wf-page="6a450776d63ee937af4d29d7"`, `data-wf-site="6a450773d63ee937af4d28ea"`, `data-cc="analytics"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.navbar> — `dairyfoodbg-com`)` (`dairyfoodbg-com`) adapts across `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)` with `cubic-bezier(.625,.05,0,1)`, `cubic-bezier(.34,1.3,.64,1)`, `cubic-bezier(.22,1,.36,1)` transitions and links `Home · About · Products · Packaging · Catalog`.
2. **Hero Stage & Focal Lead (<section.hero> — `Elevate your brand`)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `Elevate your brand` and copy excerpt *"From product development and packaging to large-scale manufacturi"* over `#ffffff` canvas and `#0d2759` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×1744px` mobile) sets `#ffffff` background with `#0d2759` headline `Elevate your brand`.
3. **Primary Showcase & Content Grid (<section.about> — `Traditional craftsmanship with mod`)**:
   - DOM & Selectors: Landmark `<section class="about">` rendering section `Traditional craftsmanship with modern UHT technol...` with copy *"Leading producer of private-label UHT dairy in Bulgaria. Leading "*, asset references (`cdn.prod.website-files.com`, `dairy-food.shared.ce91a50f0.min.css`, `dairy-food.6a450776d63ee937af4d29...`, `6abf58390100a7826e7f0b59_favicon-...`), and grid rule `summary { display:block }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.about> — `Traditional craftsmanship with mod`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 3.25px 16.25px`) on desktop and Single-column vertical stack at `390px` viewport width with `32px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.home-products> — `Customizable Products`)**:
   - DOM & Selectors: Landmark `<section class="home-products">` framing `Customizable Products` and `Flexible Packaging` (*"Leading producer of private-label UHT dairy in Bulgaria."*) with `#d7ecf6` surface cards, `#0000ff` accents, and `video { vertical-align:baseline;display:inline-block }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.home-products> — `Customizable Products`)` uses `9999px`, `7px`, `3px`, `100%` radii, `#0000ff` highlights, and assets (cdn.prod.website-files.com, dairy-food.shared.ce91a50f0.min.css, dairy-food.6a450776d63ee937af4d29...).
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://dairyfoodbg.com/`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer">` anchoring `Dairy Food Bulgaria — Private-La` footer links (`Home · About · Products · Packaging · Catalog`), copy *"Start Your Project"*, and `#e0e5f0` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-footer> — `https://dairyfoodbg.com/`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `32px` lateral canvas padding with `3.25px 16.25px` grid gap and attributes (data-wf-domain="dairyfoodbg.com", data-wf-page="6a450776d63ee937af4d29d7", data-wf-site="6a450773d63ee937af4d28ea").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"From product development and packaging to large-scale manufacturing and export, we..."*
- Copy Excerpt 2: *"Leading producer of private-label UHT dairy in Bulgaria. Leading producer of priva..."*
- Copy Excerpt 3: *"Leading producer of private-label UHT dairy in Bulgaria."*
- Copy Excerpt 4: *"Start Your Project"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.625,.05,0,1)`, `cubic-bezier(.34,1.3,.64,1)`, `cubic-bezier(.22,1,.36,1)`
- **Extracted Stylesheet Rules (`dairyfoodbg-com`)**:
- `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`
- `summary { display:block }`
- `video { vertical-align:baseline;display:inline-block }`
- `template { display:none }`
- `strong { font-weight:700 }`
- **Per-Selector Transition Rules**:
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `dairyfoodbg-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `dairyfoodbg-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `dairyfoodbg-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.625,.05,0,1)`)**: Governs interactive state transitions across `<header.navbar>` and `<section.about>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `22545px` across 8 distinct viewport chapters using Lenis, GSAP/ScrollTrigger, WebGL/Canvas.
- **Vertical Chapter Sequence**: Elevate your brand (0%) -> Elevate your brand (4%) -> This site uses cookies (20%) -> Products we produce under y... (27%) -> This site uses cookies (47%) -> This site uses cookies (55%) -> This site uses cookies (63%) -> End-to-End. Built to Scale. (67%).
- **Hover Micro-Interaction (`primary_cta`)**: Animate `transform, backgroundColor` with `0.45s cubic-bezier(0.625, 0.05, 0, 1)`.
- **Multi-Page Routes**: Scaffold internal routes `/products` (listing, direct), `/contact` (about, direct), `/catalog` (listing, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `dairyfoodbg-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | Elevate your brand | `4` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `4%` | Elevate your brand | `3` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `4250px` | `20%` | This site uses cookies | `3` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `5950px` | `27%` | Products we produce under your brand | `3` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `10200px` | `47%` | This site uses cookies | `3` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `11900px` | `55%` | This site uses cookies | `3` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `13600px` | `63%` | This site uses cookies | `3` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `14400px` | `67%` | End-to-End. Built to Scale. | `4` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | Elevate your brand | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `10739px` | `100%` | Footer | [mobile-step-02.webp](assets/mobile-step-02.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `listing` | `https://dairyfoodbg.com/products` | What Can We Produce for Your Brand? | `3383px` | `direct` (`448ms`) | [subpage-01-products.webp](assets/subpage-01-products.webp) |
| `2` | `about` | `https://dairyfoodbg.com/contact` | Get in Touch | `1636px` | `direct` (`452ms`) | [subpage-02-contact.webp](assets/subpage-02-contact.webp) |
| `3` | `listing` | `https://dairyfoodbg.com/catalog` | Our production range | `9696px` | `direct` (`620ms`) | [subpage-03-catalog.webp](assets/subpage-03-catalog.webp) |

