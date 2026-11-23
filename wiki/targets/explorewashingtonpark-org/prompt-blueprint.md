---
title: "UI Prompt Blueprint: explorewashingtonpark-org"
date: 2026-11-23
captured_at: 2026-11-23
target: "explorewashingtonpark-org"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#fdfbf8` canvas, `#313232` ink, `#ffff00` accent)"
---

# UI Design System & Master Generation Blueprint: explorewashingtonpark-org

> **Explore Washington Park** (https://explorewashingtonpark.org) — Washington Park in Portland, Oregon is home to the Oregon Zoo, Hoyt Arboretum, world-class gardens, museums, and miles of trails. Find ho...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Explore Washington Park** (`https://explorewashingtonpark.org`). Washington Park in Portland, Oregon is home to the Oregon Zoo, Hoyt Arboretum, world-class gardens, museums, and miles of trails. Find ho...
- **Final Redirected URL**: [https://www.explorewashingtonpark.org/](https://www.explorewashingtonpark.org/)
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#fdfbf8` canvas, `#313232` ink, `#ffff00` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#fdfbf8` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#313232` primary typography and `#ffff00` accents.
  - **Grounded Typographic Hierarchy**: Pairs `national-ygefsl` for display copy (`Portland’s Premier Park`) with `National` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1000px` container bounds (`gap: var(--stack-gap)`, padding `6px`) with `cubic-bezier(.175,.885,.32,1.275)` easing and Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1000px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `6px` lateral canvas padding with `var(--stack-gap)` grid gap.
- **Border Radius Scale**: `1000px`, `var(--stack-radius)`, `50%`, `5px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1000px`, `gap: var(--stack-gap)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `6px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (min-width:768px)`, `@media screen and (max-width:767px)`, `@media (max-width:767px)`, `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fdfbf8` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#313232` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#9bbd3c` | live computed `a` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ffff00` | `.icon-button:hover { color: yellow }` (`#ffff00`) |
| **Secondary / Muted Copy** | `#6b7280` | `var(--weather-modal-text-muted)` in `:root` |
| **Structural Hairline Border** | `#f1ebe2` | `var(--wm-accordion-item-border-color)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--course-item-nav-text-color` | `hsla(var(--black-hsl),1)` | Typography Ink Token |
| `--tweak-blog-item-pagination-icon-color` | `hsla(var(--black-hsl),1)` | Brand / Palette Token |
| `--tweak-quote-block-source-color-on-background` | `hsla(var(--safeDarkAccent-hsl),1)` | Canvas / Surface Token |
| `--product-basic-item-add-ons-title-color` | `hsla(var(--black-hsl),1)` | Brand / Palette Token |
| `--product-block-text-color-on-background` | `hsla(var(--safeDarkAccent-hsl),1)` | Canvas / Surface Token |
| `--paragraphSmallColor` | `hsla(var(--black-hsl),1)` | Brand / Palette Token |
| `--sqsp-paragraph-3-color` | `hsla(var(--black-hsl),1)` | Brand / Palette Token |
| `--list-section-simple-button-background-color` | `hsla(var(--safeDarkAccent-hsl),1)` | Canvas / Surface Token |
| `--gradientHeaderBorderColor` | `hsla(var(--black-hsl),1)` | Brand / Palette Token |
| `--solidHeaderDropShadowColor` | `hsla(var(--black-hsl),1)` | Brand / Palette Token |
| `--tweak-summary-block-background-color` | `hsla(var(--white-hsl),1)` | Canvas / Surface Token |
| `--tweak-form-block-survey-title-color` | `hsla(var(--black-hsl),1)` | Brand / Palette Token |
| `--list-section-carousel-card-description-color` | `hsla(var(--white-hsl),1)` | Brand / Palette Token |
| `--scheduling-block-scheduler-background-color` | `hsla(var(--lightAccent-hsl),1)` | Canvas / Surface Token |
| `--image-block-card-inline-link-color` | `hsla(var(--black-hsl),1)` | Typography Ink Token |
| `--paragraphLargeColor` | `hsla(var(--black-hsl),1)` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `national-ygefsl`.
- **Primary Body Stack**: `National`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 79.208px`, `line-height: 64.9506px`, `font-weight: 700`); CSS variables `--child-display: initial`, `--heading-1-size: 3.76rem`, `--heading-1-size-value: 3.76`; rule `.title` (`font-size: 1rem`, `line-height: 1.4`, `font-weight: 500`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 79.208px`, `line-height: 64.9506px`, `font-weight: 700`); CSS variables `--heading-2-size: 2.71rem`, `--heading-2-size-value: 2.71`; rule `h2` (`font-size: 1.88em`).
- **Body Copy**: live computed `body` (`font-size: 17px`, `line-height: normal`, `font-weight: 400`); CSS variables `--body-font-font-family: "national-ygefsl"`, `--body-font-font-style: normal`, `--body-font-font-weight: 500`; rule `p` (`line-height: 1`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 18.0368px`, `line-height: 18.0368px`, `font-weight: 500`); CSS variables `--heading-font-letter-spacing: 0em`, `--body-font-letter-spacing: 0em`, `--meta-font-font-family: "national-ygefsl"`; rule `.caption` (`font-size: 12px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.175,.885,.32,1.275)`, `cubic-bezier(.445,.05,.55,.95)`, `cubic-bezier(.5,0,1,.5)`.

### Per-Element Transition & Choreography Rules
- **Selector `.HJfcnBEmS6s00rth`**: `transition: background-color .1s ease-out` extracted from `explorewashingtonpark-org` stylesheet.
- **Selector `block-animations] .sqs-block-butt...`**: `transition: none!important` extracted from `explorewashingtonpark-org` stylesheet.
- **Selector `.sqs-use--mask)`**: `transition: fill .17s ease-in-out` extracted from `explorewashingtonpark-org` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.175,.885,.32,1.275)`)**: Governs interactive state transitions across `<header.white>` and `<section.region>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Explore Washington Park                    │
│ ====================================================================== │
│ [ <header.white> (1440x198px)         | Plan Your Visit · Explore Th ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <article.page-regions> (w=1440px)                      | │
│ | H1: Portland’s Premier Park                                        | │
│ | Substrate: #fdfbf8 | Ink: #313232 | Accent: #ffff00                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.region>) max-w: 1000px                     | │
│ | +------------------------------+  +------------------------------+ | │
│ | | 7 Spots to See Fall Color fo |  | Reservoir & Reflecting Pools | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.page-section>) — TriMet Gets You Here      | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.sections>   ) | https://explorewashingtonpark.org    │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--st)   │
│ ====================================================================== │
│ [ HEADER BAR (<header.white>          ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<article.page-regions>) — 390px Vertical Lead          | │
│ | H1: Portland’s Premier Park                                        | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.region>) — 1-Col Stack                    | │
│ | [ Item 1: 7 Spots to See Fall Color for Free                     ] | │
│ | [ Item 2: Reservoir & Reflecting Pools Are Now Open              ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.page-section>) — 1-Col (TriMet Gets You He) | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.sections>   ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.white> — `explorewashingtonpark-org`)**:
   - Landmark `<header class="white header">` (`1440x198px`) hosting `Explore Washington Park` navigation (`Plan Your Visit · Explore The Park`), DOM attributes (`data-tippy-stylesheet`, `data-name="static-context"`, `data-tawk-font-preconnect`, `data-animation-state="booted"`), and stylesheet rule `.J5FOAYd29BA3bVlN { animation-name:spin;animation-duration:1s;animation-timing-function:line... }`.
2. **Hero Stage & Focal Lead (<article.page-regions> — `Portland’s Premier Park`)**:
   - Landmark `<article class="page-regions">` presenting display lead `Portland’s Premier Park` and copy excerpt *"Know Before You Go"* over `#fdfbf8` canvas and `#313232` ink.
3. **Primary Showcase & Content Grid (<section.region> — `7 Spots to See Fall Color for Free`)**:
   - Landmark `<section class="region">` rendering section `7 Spots to See Fall Color for Free` with copy *"Portland’s Premier Park Explore Attractions & Amenities"*, asset references (`twk-main.js`, `announcement-bar-ff2c04748aa19f8b...`, `popup-overlay-f39ec8cdc95ccd84-mi...`, `popup-overlay-eb69d574e194d111-mi...`), and grid rule `.n0vbvuFosektXczs { animation-name:fadeout;animation-iteration-count:1 }`.
4. **Interactive Detail & Feature Matrix (<section.page-section> — `Reservoir & Reflecting Pools Are N`)**:
   - Landmark `<section class="page-section user-items-list-section">` framing `Reservoir & Reflecting Pools Are Now Open` and `TriMet Gets You Here Faster` (*"7 Spots to See Fall Color for Free Read the Blog"*) with `#9bbd3c` surface cards, `#ffff00` accents, and `.hWuyu_pGCLQnxiCx { animation-name:fadein;animation-iteration-count:1 }`.
5. **Colophon & Global Directory Footer (<footer.sections> — `https://explorewashingtonpark.org`)**:
   - Landmark `<footer class="sections">` anchoring `Explore Washington Park` footer links (`Plan Your Visit · Explore The Park`), copy *"Reservoir & Reflecting Pools Are Now Open Explore the Reserv"*, and `#f1ebe2` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: explorewashingtonpark-org (Explore Washington Park)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `explorewashingtonpark-org` (**Explore Washington Park** — `https://explorewashingtonpark.org`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#fdfbf8` canvas, `#313232` ink, `#ffff00` accent).
- **Identity & Domain Context**: Washington Park in Portland, Oregon is home to the Oregon Zoo, Hoyt Arboretum, world-class gardens, museums, and miles of trails. Find ho...
- **Primary Substrate**: `#fdfbf8` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#313232`, **Accent / Highlight**: `#ffff00`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#fdfbf8` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#313232` primary typography and `#ffff00` accents.
  - **Grounded Typographic Hierarchy**: Pairs `national-ygefsl` for display copy (`Portland’s Premier Park`) with `National` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1000px` container bounds (`gap: var(--stack-gap)`, padding `6px`) with `cubic-bezier(.175,.885,.32,1.275)` easing and Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `explorewashingtonpark-org` in your global stylesheet:

:root {
  /* Explore Washington Park (explorewashingtonpark-org) — Live-Grounded CSS Variables */
  --course-item-nav-text-color: hsla(var(--black-hsl),1); /* Typography Ink Token (explorewashingtonpark-org) */
  --tweak-blog-item-pagination-icon-color: hsla(var(--black-hsl),1); /* Brand / Palette Token (explorewashingtonpark-org) */
  --tweak-quote-block-source-color-on-background: hsla(var(--safeDarkAccent-hsl),1); /* Canvas / Surface Token (explorewashingtonpark-org) */
  --product-basic-item-add-ons-title-color: hsla(var(--black-hsl),1); /* Brand / Palette Token (explorewashingtonpark-org) */
  --product-block-text-color-on-background: hsla(var(--safeDarkAccent-hsl),1); /* Canvas / Surface Token (explorewashingtonpark-org) */
  --paragraphSmallColor: hsla(var(--black-hsl),1); /* Brand / Palette Token (explorewashingtonpark-org) */
  --sqsp-paragraph-3-color: hsla(var(--black-hsl),1); /* Brand / Palette Token (explorewashingtonpark-org) */
  --list-section-simple-button-background-color: hsla(var(--safeDarkAccent-hsl),1); /* Canvas / Surface Token (explorewashingtonpark-org) */
  --gradientHeaderBorderColor: hsla(var(--black-hsl),1); /* Brand / Palette Token (explorewashingtonpark-org) */
  --solidHeaderDropShadowColor: hsla(var(--black-hsl),1); /* Brand / Palette Token (explorewashingtonpark-org) */
  --tweak-summary-block-background-color: hsla(var(--white-hsl),1); /* Canvas / Surface Token (explorewashingtonpark-org) */
  --tweak-form-block-survey-title-color: hsla(var(--black-hsl),1); /* Brand / Palette Token (explorewashingtonpark-org) */
  --list-section-carousel-card-description-color: hsla(var(--white-hsl),1); /* Brand / Palette Token (explorewashingtonpark-org) */
  --scheduling-block-scheduler-background-color: hsla(var(--lightAccent-hsl),1); /* Canvas / Surface Token (explorewashingtonpark-org) */
  --image-block-card-inline-link-color: hsla(var(--black-hsl),1); /* Typography Ink Token (explorewashingtonpark-org) */
  --paragraphLargeColor: hsla(var(--black-hsl),1); /* Brand / Palette Token (explorewashingtonpark-org) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fdfbf8` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#313232` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#9bbd3c` — grounded in live computed `a` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#ffff00` — grounded in `.icon-button:hover { color: yellow }` (`#ffff00`)
- **Secondary / Muted Copy**: `#6b7280` — grounded in `var(--weather-modal-text-muted)` in `:root`
- **Structural Hairline Border**: `#f1ebe2` — grounded in `var(--wm-accordion-item-border-color)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1000px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `6px` lateral canvas padding with `var(--stack-gap)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1000px`, `gap: var(--stack-gap)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `6px` horizontal padding
- **Media Queries**: `@media screen and (min-width:768px)`, `@media screen and (max-width:767px)`, `@media (max-width:767px)`, `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `1000px`, `var(--stack-radius)`, `50%`, `5px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `national-ygefsl`
- **Body Font Stack**: `National`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 79.208px`, `line-height: 64.9506px`, `font-weight: 700`); CSS variables `--child-display: initial`, `--heading-1-size: 3.76rem`, `--heading-1-size-value: 3.76`; rule `.title` (`font-size: 1rem`, `line-height: 1.4`, `font-weight: 500`)
- **H2 Section Rule**: live computed `h2` (`font-size: 79.208px`, `line-height: 64.9506px`, `font-weight: 700`); CSS variables `--heading-2-size: 2.71rem`, `--heading-2-size-value: 2.71`; rule `h2` (`font-size: 1.88em`)
- **Body Copy Rule**: live computed `body` (`font-size: 17px`, `line-height: normal`, `font-weight: 400`); CSS variables `--body-font-font-family: "national-ygefsl"`, `--body-font-font-style: normal`, `--body-font-font-weight: 500`; rule `p` (`line-height: 1`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 18.0368px`, `line-height: 18.0368px`, `font-weight: 500`); CSS variables `--heading-font-letter-spacing: 0em`, `--body-font-letter-spacing: 0em`, `--meta-font-font-family: "national-ygefsl"`; rule `.caption` (`font-size: 12px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `explorewashingtonpark-org` (`Explore Washington Park`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.white> — `explorewashingtonpark-org`)**:
   - DOM & Selectors: Landmark `<header class="white header">` (`1440x198px`) hosting `Explore Washington Park` navigation (`Plan Your Visit · Explore The Park`), DOM attributes (`data-tippy-stylesheet`, `data-name="static-context"`, `data-tawk-font-preconnect`, `data-animation-state="booted"`), and stylesheet rule `.J5FOAYd29BA3bVlN { animation-name:spin;animation-duration:1s;animation-timing-function:line... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.white> — `explorewashingtonpark-org`)` (`explorewashingtonpark-org`) adapts across `@media screen and (min-width:768px)`, `@media screen and (max-width:767px)`, `@media (max-width:767px)`, `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(.175,.885,.32,1.275)`, `cubic-bezier(.445,.05,.55,.95)`, `cubic-bezier(.5,0,1,.5)` transitions and links `Plan Your Visit · Explore The Park`.
2. **Hero Stage & Focal Lead (<article.page-regions> — `Portland’s Premier Park`)**:
   - DOM & Selectors: Landmark `<article class="page-regions">` presenting display lead `Portland’s Premier Park` and copy excerpt *"Know Before You Go"* over `#fdfbf8` canvas and `#313232` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#fdfbf8` background with `#313232` headline `Portland’s Premier Park`.
3. **Primary Showcase & Content Grid (<section.region> — `7 Spots to See Fall Color for Free`)**:
   - DOM & Selectors: Landmark `<section class="region">` rendering section `7 Spots to See Fall Color for Free` with copy *"Portland’s Premier Park Explore Attractions & Amenities"*, asset references (`twk-main.js`, `announcement-bar-ff2c04748aa19f8b...`, `popup-overlay-f39ec8cdc95ccd84-mi...`, `popup-overlay-eb69d574e194d111-mi...`), and grid rule `.n0vbvuFosektXczs { animation-name:fadeout;animation-iteration-count:1 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.region> — `7 Spots to See Fall Color for Free`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1000px`, `gap: var(--stack-gap)`) on desktop and Single-column vertical stack at `390px` viewport width with `6px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.page-section> — `Reservoir & Reflecting Pools Are N`)**:
   - DOM & Selectors: Landmark `<section class="page-section user-items-list-section">` framing `Reservoir & Reflecting Pools Are Now Open` and `TriMet Gets You Here Faster` (*"7 Spots to See Fall Color for Free Read the Blog"*) with `#9bbd3c` surface cards, `#ffff00` accents, and `.hWuyu_pGCLQnxiCx { animation-name:fadein;animation-iteration-count:1 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.page-section> — `Reservoir & Reflecting Pools Are N`)` uses `1000px`, `var(--stack-radius)`, `50%`, `5px` radii, `#ffff00` highlights, and assets (twk-main.js, announcement-bar-ff2c04748aa19f8b..., popup-overlay-f39ec8cdc95ccd84-mi...).
5. **Colophon & Global Directory Footer (<footer.sections> — `https://explorewashingtonpark.org`)**:
   - DOM & Selectors: Landmark `<footer class="sections">` anchoring `Explore Washington Park` footer links (`Plan Your Visit · Explore The Park`), copy *"Reservoir & Reflecting Pools Are Now Open Explore the Reserv"*, and `#f1ebe2` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.sections> — `https://explorewashingtonpark.org`)` aligns to `1000px` (non-`@media` desktop container stylesheet rule) with `6px` lateral canvas padding with `var(--stack-gap)` grid gap and attributes (data-tippy-stylesheet, data-name="static-context", data-tawk-font-preconnect).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Know Before You Go"*
- Copy Excerpt 2: *"Portland’s Premier Park Explore Attractions & Amenities"*
- Copy Excerpt 3: *"7 Spots to See Fall Color for Free Read the Blog"*
- Copy Excerpt 4: *"Reservoir & Reflecting Pools Are Now Open Explore the Reservoir"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.175,.885,.32,1.275)`, `cubic-bezier(.445,.05,.55,.95)`, `cubic-bezier(.5,0,1,.5)`
- **Extracted Stylesheet Rules (`explorewashingtonpark-org`)**:
- `.J5FOAYd29BA3bVlN { animation-name:spin;animation-duration:1s;animation-timing-function:line... }`
- `.n0vbvuFosektXczs { animation-name:fadeout;animation-iteration-count:1 }`
- `.hWuyu_pGCLQnxiCx { animation-name:fadein;animation-iteration-count:1 }`
- `.ZW7PDoaiuIANOlaf { animation-name:riseandfadein;animation-iteration-count:1 }`
- `.HJfcnBEmS6s00rth.mVW8qfAVC5cSpu5x { background-color:0000 }`
- **Per-Selector Transition Rules**:
- **Selector `.HJfcnBEmS6s00rth`**: `transition: background-color .1s ease-out` extracted from `explorewashingtonpark-org` stylesheet.
- **Selector `block-animations] .sqs-block-butt...`**: `transition: none!important` extracted from `explorewashingtonpark-org` stylesheet.
- **Selector `.sqs-use--mask)`**: `transition: fill .17s ease-in-out` extracted from `explorewashingtonpark-org` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.175,.885,.32,1.275)`)**: Governs interactive state transitions across `<header.white>` and `<section.region>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `explorewashingtonpark-org`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
