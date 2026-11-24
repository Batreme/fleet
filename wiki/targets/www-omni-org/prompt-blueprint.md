---
title: "UI Prompt Blueprint: www-omni-org"
date: 2026-11-24
captured_at: 2026-11-24
target: "www-omni-org"
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
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#081c39` ink, `#ffa500` accent)"
---

# UI Design System & Master Generation Blueprint: www-omni-org

> **Omni Institute** (https://www.omni.org) — At Omni Institute, we believe in the power of data to drive real-life change. As a nonprofit research and evaluation partner, we help nat...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Omni Institute** (`https://www.omni.org`). At Omni Institute, we believe in the power of data to drive real-life change. As a nonprofit research and evaluation partner, we help nat...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#081c39` ink, `#ffa500` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#081c39` primary typography and `#ffa500` accents.
  - **Grounded Typographic Hierarchy**: Uses `neue-haas-grotesk-display` across display (`Nonprofit Social Science Consultancy`) and body copy, paired with `Sometype Mono` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `1920px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(0,.3,.15,1)` easing and GSAP Timeline & ScrollTrigger, Lottie Vector Animation Player.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=9544px` / doc `10945px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1920px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `9px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `3px`, `100%`, `50%`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1920px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#081c39` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f3f3f3` | `var(--sds-g-color-surface-2)` in `:root` |
| **Interactive Accent / Highlight** | `#ffa500` | `.button.is-secondary.is-icon.or... { color: orange }` (`#ffa500`) |
| **Secondary / Muted Copy** | `#fe7298` | `var(--sds-g-color-palette-pink-65)` in `:root` |
| **Structural Hairline Border** | `#dd7a01` | `var(--sds-g-color-border-warning-1)` in `:root` |
| **Variable Token (`--_primitives---colors--periwinkle-600`)** | `#5776b2` | `var(--_primitives---colors--periwinkle-600)` in `:root` |
| **Variable Token (`--_primitives---colors--steel-blue-200`)** | `#bfcbd3` | `var(--_primitives---colors--steel-blue-200)` in `:root` |
| **Variable Token (`--_primitives---colors--steel-blue-400`)** | `#677384` | `var(--_primitives---colors--steel-blue-400)` in `:root` |
| **Variable Token (`--_primitives---colors--periwinkle-200`)** | `#d4ddeb` | `var(--_primitives---colors--periwinkle-200)` in `:root` |
| **Variable Token (`--_primitives---colors--plum-600`)** | `#921c4c` | `var(--_primitives---colors--plum-600)` in `:root` |
| **Variable Token (`--_primitives---colors--orange-600`)** | `#cc4100` | `var(--_primitives---colors--orange-600)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-scheme-1--background` | `var(--_primitives---colors--white)` | Canvas / Surface Token |
| `--_typography---font-styles--body` | `neue-haas-grotesk-display,sans-serif` | Typography / Scale Token |
| `--color-scheme-1--headers` | `var(--_primitives---colors--navy)` | Brand / Palette Token |
| `--_typography---font-styles--heading` | `neue-haas-grotesk-display,sans-serif` | Typography Ink Token |
| `--_typography---font-styles--eyebrows` | `"Sometype Mono",sans-serif` | Typography / Scale Token |
| `--color-scheme-1--paragraphs` | `var(--_primitives---colors--steel-blue-400)` | Brand / Palette Token |
| `--_primitives---colors--periwinkle-600` | `#5776b2` | Typography Ink Token |
| `--_primitives---colors--steel-blue-200` | `#bfcbd3` | Brand / Palette Token |
| `--_primitives---colors--navy` | `#081c39` | Brand / Palette Token |
| `--_primitives---colors--white` | `#fff` | Canvas / Surface Token |
| `--_ui-styles---radius--large` | `100px` | Elevation / Border Token |
| `--_primitives---colors--steel-blue-400` | `#677384` | Brand / Palette Token |
| `--_primitives---opacity--transparent` | `transparent` | Design System Custom Token |
| `--_primitives---colors--periwinkle-200` | `#d4ddeb` | Typography Ink Token |
| `--_primitives---colors--plum-600` | `#921c4c` | Brand / Palette Token |
| `--_primitives---colors--orange-600` | `#cc4100` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `neue-haas-grotesk-display`.
- **Primary Body Stack**: `neue-haas-grotesk-display`.
- **Technical / Metadata Stack**: `Sometype Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 20px`, `line-height: 24px`, `font-weight: 700`); CSS variables `--sds-g-sizing-heading-1: 20ch`, `--slds-g-sizing-heading-1: 20ch`; rule `h1` (`line-height: 1`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 80px`, `line-height: 80px`, `font-weight: 700`); CSS variables `--sds-g-sizing-heading-2: 25ch`, `--slds-g-sizing-heading-2: 25ch`; rule `h2` (`font-size: 1.125rem`, `font-weight: 700`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--_typography---font-styles--body: neue-haas-grotesk-display,sans-serif`, `--sds-g-font-size-base: 1rem`, `--slds-g-font-size-base: 0.8125rem`; rule `p` (`line-height: 1.7`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--_ui-styles---radius--small: 8px`, `--sds-g-font-family-monospace: Consolas,Menlo,Monaco,Courier,monospace`, `--slds-g-font-family-monospace: Consolas,Menlo,Monaco,Courier,monospace`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,.3,.15,1)`, `cubic-bezier(.3,0,.15,1)`, `cubic-bezier(0,0,1,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `www-omni-org` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `www-omni-org` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-omni-org` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,.3,.15,1)`)**: Governs interactive state transitions across `<header.section_header23>` and `<section.background-color-ivory>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `10945px`, deepest scrollY reached `9544px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `GSAP/ScrollTrigger`.
- **Hover Physics (`primary_cta` · `Work With Us`)**: `transform`: `none` -> `matrix(1.05, 0, 0, 1.05...`; `color`: `rgb(8, 28, 57)` -> `rgb(255, 255, 255)`; `backgroundColor`: `rgba(0, 0, 0, 0)` -> `rgb(8, 28, 57)` (`transition-duration: 0s`, `timing: ease`).
- **Route Transition Architecture**: First internal navigation (`/project/nd-sor`) measured as `direct` in `1868ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Omni Institute                             │
│ ====================================================================== │
│ [ <header.section_header (1440x524px) | Community Health · Behaviora ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.section_layout488> (w=1440px)                 | │
│ | H1: Nonprofit Social Science Consultancy                           | │
│ | Substrate: #ffffff | Ink: #081c39 | Accent: #ffa500                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.background-color-) max-w: 1920px           | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Turning Data into Stories, S |  | We strengthen communities th | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.section_layout516) — Data-Driven Insights. | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer6_comp) | https://www.omni.org                 │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.section_header23) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.section_layout4) — 390px Vertical Lead        | │
│ | H1: Nonprofit Social Science Consultancy                           | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.background-co) — 1-Col Stack              | │
│ | [ Item 1: Turning Data into Stories, Stories into Change         ] | │
│ | [ Item 2: We strengthen communities through research, evalu...   ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.section_layout5) — 1-Col (Data-Driven Insigh) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer6_comp) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.section_header23> — `www-omni-org`)**:
   - Landmark `<header class="section_header23">` (`1440x524px`) hosting `Omni Institute` navigation (`Community Health · Behavioral Health · Children & Families · Economic Security · Justice`), DOM attributes (`data-wf-domain="www.omni.org"`, `data-wf-page="682b5468dca036bcf33813c0"`, `data-wf-site="682b5467dca036bcf33811dc"`, `data-animation="default"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.section_layout488> — `Nonprofit Social Science Consultan`)**:
   - Landmark `<section class="section_layout488">` presenting display lead `Nonprofit Social Science Consultancy` and copy excerpt *"At Omni Institute, we believe in the power of data to drive real-"* over `#ffffff` canvas and `#081c39` ink.
3. **Primary Showcase & Content Grid (<section.background-color-ivory> — `Turning Data into Stories, Stories`)**:
   - Landmark `<section class="background-color-ivory">` rendering section `Turning Data into Stories, Stories into Change` with copy *"Rigorous, Human-First Research"*, asset references (`cdn.prod.website-files.com`, `omni-institute.webflow.shared.add...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.section_layout516> — `We strengthen communities through `)**:
   - Landmark `<section class="section_layout516">` framing `We strengthen communities through research, evalu...` and `Data-Driven Insights. Meaningful Impact.` (*"Committed to Actionable Impact"*) with `#f3f3f3` surface cards, `#ffa500` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer6_component> — `https://www.omni.org`)**:
   - Landmark `<footer class="footer6_component">` anchoring `Omni Institute` footer links (`Community Health · Behavioral Health · Children & Families · Economic Security · Justice`), copy *"Organizational Development"*, and `#dd7a01` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `Nonprofit Social Science Consultancy` · sticky/fixed elements: `2`
- **Step 02** (`y=850px`, `9%`): Active landmark `We strengthen communities through research, evalu...` · sticky/fixed elements: `1`
- **Step 03** (`y=2550px`, `27%`): Active landmark `Rigorous Research to Expand your Impact.` · sticky/fixed elements: `1`
- **Step 04** (`y=4250px`, `42%`): Active landmark `Actionable Evaluation to Strengthen your Impact.` · sticky/fixed elements: `0`
- **Step 05** (`y=5950px`, `59%`): Active landmark `Driving Impact` · sticky/fixed elements: `0`
- **Step 06** (`y=7650px`, `76%`): Active landmark `Family Justice Journal: ROI of a Rural Family Res...` · sticky/fixed elements: `0`
- **Step 07** (`y=9350px`, `93%`): Active landmark `Let’s make an impact together.` · sticky/fixed elements: `0`
- **Step 08** (`y=9544px`, `95%`): Active landmark `Let’s make an impact together.` · sticky/fixed elements: `0`

### Multi-Page Internal Route Map
- **Detail Route (`/project/nd-sor`)**: `https://www.omni.org/project/nd-sor` — H1: `North Dakota State Opioid Response Evaluation`, scrollHeight `6276px`, transition `direct` (`1868ms`)
- **About Route (`/contact`)**: `https://www.omni.org/contact` — H1: `CONTACT`, scrollHeight `4001px`, transition `direct` (`1249ms`)
- **Detail Route (`/project/wyoming-family-resource-centers-collective-evaluation`)**: `https://www.omni.org/project/wyoming-family-resource-centers-collective-evaluation` — H1: `Wyoming Family Resource Centers Collective Evalua...`, scrollHeight `6005px`, transition `direct` (`2685ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-omni-org (Omni Institute)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-omni-org` (**Omni Institute** — `https://www.omni.org`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#081c39` ink, `#ffa500` accent).
- **Identity & Domain Context**: At Omni Institute, we believe in the power of data to drive real-life change. As a nonprofit research and evaluation partner, we help nat...
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#081c39`, **Accent / Highlight**: `#ffa500`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#081c39` primary typography and `#ffa500` accents.
  - **Grounded Typographic Hierarchy**: Uses `neue-haas-grotesk-display` across display (`Nonprofit Social Science Consultancy`) and body copy, paired with `Sometype Mono` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `1920px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(0,.3,.15,1)` easing and GSAP Timeline & ScrollTrigger, Lottie Vector Animation Player.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-omni-org` in your global stylesheet:

:root {
  /* Omni Institute (www-omni-org) — Live-Grounded CSS Variables */
  --color-scheme-1--background: var(--_primitives---colors--white); /* Canvas / Surface Token (www-omni-org) */
  --_typography---font-styles--body: neue-haas-grotesk-display,sans-serif; /* Typography / Scale Token (www-omni-org) */
  --color-scheme-1--headers: var(--_primitives---colors--navy); /* Brand / Palette Token (www-omni-org) */
  --_typography---font-styles--heading: neue-haas-grotesk-display,sans-serif; /* Typography Ink Token (www-omni-org) */
  --_typography---font-styles--eyebrows: "Sometype Mono",sans-serif; /* Typography / Scale Token (www-omni-org) */
  --color-scheme-1--paragraphs: var(--_primitives---colors--steel-blue-400); /* Brand / Palette Token (www-omni-org) */
  --_primitives---colors--periwinkle-600: #5776b2; /* Typography Ink Token (www-omni-org) */
  --_primitives---colors--steel-blue-200: #bfcbd3; /* Brand / Palette Token (www-omni-org) */
  --_primitives---colors--navy: #081c39; /* Brand / Palette Token (www-omni-org) */
  --_primitives---colors--white: #fff; /* Canvas / Surface Token (www-omni-org) */
  --_ui-styles---radius--large: 100px; /* Elevation / Border Token (www-omni-org) */
  --_primitives---colors--steel-blue-400: #677384; /* Brand / Palette Token (www-omni-org) */
  --_primitives---opacity--transparent: transparent; /* Design System Custom Token (www-omni-org) */
  --_primitives---colors--periwinkle-200: #d4ddeb; /* Typography Ink Token (www-omni-org) */
  --_primitives---colors--plum-600: #921c4c; /* Brand / Palette Token (www-omni-org) */
  --_primitives---colors--orange-600: #cc4100; /* Brand / Palette Token (www-omni-org) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#081c39` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#f3f3f3` — grounded in `var(--sds-g-color-surface-2)` in `:root`
- **Interactive Accent / Highlight**: `#ffa500` — grounded in `.button.is-secondary.is-icon.or... { color: orange }` (`#ffa500`)
- **Secondary / Muted Copy**: `#fe7298` — grounded in `var(--sds-g-color-palette-pink-65)` in `:root`
- **Structural Hairline Border**: `#dd7a01` — grounded in `var(--sds-g-color-border-warning-1)` in `:root`
- **Variable Token (`--_primitives---colors--periwinkle-600`)**: `#5776b2` — grounded in `var(--_primitives---colors--periwinkle-600)` in `:root`
- **Variable Token (`--_primitives---colors--steel-blue-200`)**: `#bfcbd3` — grounded in `var(--_primitives---colors--steel-blue-200)` in `:root`
- **Variable Token (`--_primitives---colors--steel-blue-400`)**: `#677384` — grounded in `var(--_primitives---colors--steel-blue-400)` in `:root`
- **Variable Token (`--_primitives---colors--periwinkle-200`)**: `#d4ddeb` — grounded in `var(--_primitives---colors--periwinkle-200)` in `:root`
- **Variable Token (`--_primitives---colors--plum-600`)**: `#921c4c` — grounded in `var(--_primitives---colors--plum-600)` in `:root`
- **Variable Token (`--_primitives---colors--orange-600`)**: `#cc4100` — grounded in `var(--_primitives---colors--orange-600)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1920px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `9px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1920px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding
- **Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`
- **Corner Radii**: `3px`, `100%`, `50%`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `neue-haas-grotesk-display`
- **Body Font Stack**: `neue-haas-grotesk-display`
- **Monospace / Technical Font Stack**: `Sometype Mono`
- **H1 Display Rule**: live computed `h1` (`font-size: 20px`, `line-height: 24px`, `font-weight: 700`); CSS variables `--sds-g-sizing-heading-1: 20ch`, `--slds-g-sizing-heading-1: 20ch`; rule `h1` (`line-height: 1`)
- **H2 Section Rule**: live computed `h2` (`font-size: 80px`, `line-height: 80px`, `font-weight: 700`); CSS variables `--sds-g-sizing-heading-2: 25ch`, `--slds-g-sizing-heading-2: 25ch`; rule `h2` (`font-size: 1.125rem`, `font-weight: 700`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--_typography---font-styles--body: neue-haas-grotesk-display,sans-serif`, `--sds-g-font-size-base: 1rem`, `--slds-g-font-size-base: 0.8125rem`; rule `p` (`line-height: 1.7`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--_ui-styles---radius--small: 8px`, `--sds-g-font-family-monospace: Consolas,Menlo,Monaco,Courier,monospace`, `--slds-g-font-family-monospace: Consolas,Menlo,Monaco,Courier,monospace`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-omni-org` (`Omni Institute`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.section_header23> — `www-omni-org`)**:
   - DOM & Selectors: Landmark `<header class="section_header23">` (`1440x524px`) hosting `Omni Institute` navigation (`Community Health · Behavioral Health · Children & Families · Economic Security · Justice`), DOM attributes (`data-wf-domain="www.omni.org"`, `data-wf-page="682b5468dca036bcf33813c0"`, `data-wf-site="682b5467dca036bcf33811dc"`, `data-animation="default"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.section_header23> — `www-omni-org`)` (`www-omni-org`) adapts across `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)` with `cubic-bezier(0,.3,.15,1)`, `cubic-bezier(.3,0,.15,1)`, `cubic-bezier(0,0,1,1)` transitions and links `Community Health · Behavioral Health · Children & Families · Economic Security · Justice`.
2. **Hero Stage & Focal Lead (<section.section_layout488> — `Nonprofit Social Science Consultan`)**:
   - DOM & Selectors: Landmark `<section class="section_layout488">` presenting display lead `Nonprofit Social Science Consultancy` and copy excerpt *"At Omni Institute, we believe in the power of data to drive real-"* over `#ffffff` canvas and `#081c39` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#ffffff` background with `#081c39` headline `Nonprofit Social Science Consultancy`.
3. **Primary Showcase & Content Grid (<section.background-color-ivory> — `Turning Data into Stories, Stories`)**:
   - DOM & Selectors: Landmark `<section class="background-color-ivory">` rendering section `Turning Data into Stories, Stories into Change` with copy *"Rigorous, Human-First Research"*, asset references (`cdn.prod.website-files.com`, `omni-institute.webflow.shared.add...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `summary { display:block }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.background-color-ivory> — `Turning Data into Stories, Stories`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1920px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `9px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.section_layout516> — `We strengthen communities through `)**:
   - DOM & Selectors: Landmark `<section class="section_layout516">` framing `We strengthen communities through research, evalu...` and `Data-Driven Insights. Meaningful Impact.` (*"Committed to Actionable Impact"*) with `#f3f3f3` surface cards, `#ffa500` accents, and `video { vertical-align:baseline;display:inline-block }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.section_layout516> — `We strengthen communities through `)` uses `3px`, `100%`, `50%`, `2px` radii, `#ffa500` highlights, and assets (cdn.prod.website-files.com, omni-institute.webflow.shared.add..., fonts.googleapis.com).
5. **Colophon & Global Directory Footer (<footer.footer6_component> — `https://www.omni.org`)**:
   - DOM & Selectors: Landmark `<footer class="footer6_component">` anchoring `Omni Institute` footer links (`Community Health · Behavioral Health · Children & Families · Economic Security · Justice`), copy *"Organizational Development"*, and `#dd7a01` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer6_component> — `https://www.omni.org`)` aligns to `1920px` (non-`@media` desktop container stylesheet rule) with `9px` lateral canvas padding with `16px` grid gap and attributes (data-wf-domain="www.omni.org", data-wf-page="682b5468dca036bcf33813c0", data-wf-site="682b5467dca036bcf33811dc").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"At Omni Institute, we believe in the power of data to drive real-life change. As a..."*
- Copy Excerpt 2: *"Rigorous, Human-First Research"*
- Copy Excerpt 3: *"Committed to Actionable Impact"*
- Copy Excerpt 4: *"Organizational Development"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,.3,.15,1)`, `cubic-bezier(.3,0,.15,1)`, `cubic-bezier(0,0,1,1)`
- **Extracted Stylesheet Rules (`www-omni-org`)**:
- `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`
- `summary { display:block }`
- `video { vertical-align:baseline;display:inline-block }`
- `template { display:none }`
- `strong { font-weight:700 }`
- **Per-Selector Transition Rules**:
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `www-omni-org` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `www-omni-org` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-omni-org` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,.3,.15,1)`)**: Governs interactive state transitions across `<header.section_header23>` and `<section.background-color-ivory>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `10945px` across 8 distinct viewport chapters using GSAP/ScrollTrigger.
- **Vertical Chapter Sequence**: Nonprofit Social Science Co... (0%) -> We strengthen communities t... (9%) -> Rigorous Research to Expand... (27%) -> Actionable Evaluation to St... (42%) -> Driving Impact (59%) -> Family Justice Journal: ROI... (76%) -> Let’s make an impact together. (93%) -> Let’s make an impact together. (95%).
- **Hover Micro-Interaction (`primary_cta`)**: Animate `transform, color, backgroundColor` with `0s ease`.
- **Multi-Page Routes**: Scaffold internal routes `/project/nd-sor` (detail, direct), `/contact` (about, direct), `/project/wyoming-family-resource-centers-collective-evaluation` (detail, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-omni-org`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | Nonprofit Social Science Consultancy | `2` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `9%` | We strengthen communities through research, e... | `1` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `2550px` | `27%` | Rigorous Research to Expand your Impact. | `1` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `4250px` | `42%` | Actionable Evaluation to Strengthen your Impact. | `0` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `5950px` | `59%` | Driving Impact | `0` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `7650px` | `76%` | Family Justice Journal: ROI of a Rural Family... | `0` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `9350px` | `93%` | Let’s make an impact together. | `0` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `9544px` | `95%` | Let’s make an impact together. | `0` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | Nonprofit Social Science Consultancy | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `7573px` | `50%` | Driving Impact | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `13488px` | `100%` | Let’s make an impact together. | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `detail` | `https://www.omni.org/project/nd-sor` | North Dakota State Opioid Response Ev... | `6276px` | `direct` (`1868ms`) | [subpage-01-project-nd-sor.webp](assets/subpage-01-project-nd-sor.webp) |
| `2` | `about` | `https://www.omni.org/contact` | CONTACT | `4001px` | `direct` (`1249ms`) | [subpage-02-contact.webp](assets/subpage-02-contact.webp) |
| `3` | `detail` | `https://www.omni.org/project/wyoming-family-resource-centers-collective-evaluation` | Wyoming Family Resource Centers Colle... | `6005px` | `direct` (`2685ms`) | [subpage-03-project-wyoming-family-resource-cent.webp](assets/subpage-03-project-wyoming-family-resource-cent.webp) |

