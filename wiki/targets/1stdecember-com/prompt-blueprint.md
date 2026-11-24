---
title: "UI Prompt Blueprint: 1stdecember-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "1stdecember-com"
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
archetype: "Light-Substrate Editorial & Modular Grid System (`#efece7` canvas, `#20201e` ink, `#ffff00` accent)"
---

# UI Design System & Master Generation Blueprint: 1stdecember-com

> **First December Films · Ad Film Production House in India** (https://1stdecember.com) — Mumbai advertising film production house with 150+ international awards. TVCs, brand films and digital campaigns for brands across India...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **First December Films · Ad Film Production House in India** (`https://1stdecember.com`). Mumbai advertising film production house with 150+ international awards. TVCs, brand films and digital campaigns for brands across India...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#efece7` canvas, `#20201e` ink, `#ffff00` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#efece7` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#20201e` primary typography and `#ffff00` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Tartuffo Trial Regular` for display copy (`1st December Films`) with `Pp neue montreal Medium` and `DM Mono Medium`.
  - **Calibrated Spatial Grid & Motion**: Combines `1600px` container bounds (`gap: 96px`, padding `40px`) with `cubic-bezier(1,0,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=14400px` / doc `19767px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1600px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `40px` lateral canvas padding with `96px` grid gap.
- **Border Radius Scale**: `3px`, `100%`, `50%`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1600px`, `gap: 96px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `40px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#efece7` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#20201e` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e5e7eb` | `var(--cal-bg-emphasis)` in `:root` |
| **Interactive Accent / Highlight** | `#ffff00` | `.cta_blog_post { background-color: yellow }` (`#ffff00`) |
| **Secondary / Muted Copy** | `#6b7280` | `var(--cal-text-subtle)` in `:root` |
| **Structural Hairline Border** | `#9ca3b0` | `var(--cal-border-emphasis)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--brand--white-light` | `#efece7` | Canvas / Surface Token |
| `--font-family--body` | `"Pp neue montreal Medium",Arial,sans-serif` | Typography / Scale Token |
| `--_theme---text--primary` | `var(--brand--black-dark)` | Typography Ink Token |
| `--_typography---body--body-font-size` | `1rem` | Typography / Scale Token |
| `--_typography---body--body-line-height` | `var(--font-height--xlarge)` | Typography / Scale Token |
| `--_typography---body--body-font-weight` | `var(--font-weight--normal)` | Typography / Scale Token |
| `--_typography---body--body-letter-spacing` | `var(--letter-spacing--default)` | Typography / Scale Token |
| `--_layout---spacing--none` | `0rem` | Layout / Spatial Grid Token |
| `--font-family--heading` | `"Tartuffo Trial Regular",Arial,sans-serif` | Typography Ink Token |
| `--_typography---h1--h1-font-size` | `7.5rem` | Typography / Scale Token |
| `--_typography---h1--h1-line-height` | `var(--font-height--tiny)` | Typography / Scale Token |
| `--_typography---h1--h1-font-weight` | `var(--font-weight--normal)` | Typography / Scale Token |
| `--_typography---h1--h1-letter-spacing` | `var(--letter-spacing--tighter)` | Typography / Scale Token |
| `--_typography---h2--h2-font-size` | `5rem` | Typography / Scale Token |
| `--_typography---h2--h2-line-height` | `var(--font-height--tiny)` | Typography / Scale Token |
| `--_typography---h2--h2-font-weight` | `var(--font-weight--normal)` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Tartuffo Trial Regular`.
- **Primary Body Stack**: `Pp neue montreal Medium`.
- **Technical / Metadata Stack**: `DM Mono Medium`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 120px`, `line-height: 120px`, `font-weight: 400`, `letter-spacing: -2.4px`); CSS variables `--_typography---h1--h1-font-size: 7.5rem`, `--_typography---h1--h1-line-height: var(--font-height--tiny)`, `--_typography---h1--h1-font-weight: var(--font-weight--normal)`; rule `h1` (`font-size: var(--text-base)`, `line-height: var(--tw-leading,var(...`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 299.52px`, `line-height: 254.592px`, `font-weight: 400`, `letter-spacing: -5.9904px`); CSS variables `--_typography---h2--h2-font-size: 5rem`, `--_typography---h2--h2-line-height: var(--font-height--tiny)`, `--_typography---h2--h2-font-weight: var(--font-weight--normal)`; rule `h2` (`font-size: var(--text-sm)`, `line-height: var(--tw-leading,var(...`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-family--body: "Pp neue montreal Medium",Arial,sans-serif`, `--_typography---body--body-font-size: 1rem`, `--_typography---body--body-line-height: var(--font-height--xlarge)`; rule `p` (`font-size: var(--text-sm)`, `line-height: var(--tw-leading,var(...`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--_typography---body--body-letter-spacing: var(--letter-spacing--default)`, `--_typography---h1--h1-letter-spacing: var(--letter-spacing--tighter)`, `--_typography---h2--h2-letter-spacing: var(--letter-spacing--tighter)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(1,0,0,1)`, `cubic-bezier(.645,.045,.355,1)`, `cubic-bezier(.4,0,1,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `1stdecember-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `1stdecember-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `1stdecember-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(1,0,0,1)`)**: Governs interactive state transitions across `<header.underlay-nav__header>` and `<section.section_work>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `19767px`, deepest scrollY reached `14400px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `Lenis`, `GSAP/ScrollTrigger`.
- **Hover Physics (`primary_cta` · `Contact us`)**: Computed transition `0.15s` / `cubic-bezier(0.4, 0, 0.2, 1)` (no static color/transform shift captured at rest).
- **Route Transition Architecture**: First internal navigation (`/work`) measured as `direct` in `5465ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — First December Films · Ad Film Production  │
│ ====================================================================== │
│ [ <header.underlay-nav__ (1440x98px)  | Home · Work · Directors · Ab ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.section_about> (w=1440px)                     | │
│ | H1: 1st December Films                                             | │
│ | Substrate: #efece7 | Ink: #20201e | Accent: #ffff00                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.section_work>) max-w: 1600px               | │
│ | +------------------------------+  +------------------------------+ | │
│ | | India's most awarded ad film |  | The one film a brand builds  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.section_team-home) — what we are proud of  | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.demo-footer>) | https://1stdecember.com              │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 96px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.underlay-nav__he) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.section_about>) — 390px Vertical Lead         | │
│ | H1: 1st December Films                                             | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.section_work>) — 1-Col Stack              | │
│ | [ Item 1: India's most awarded ad film house                     ] | │
│ | [ Item 2: The one film a brand builds its year around            ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.section_team-ho) — 1-Col (what we are proud ) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.demo-footer>) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.underlay-nav__header> — `1stdecember-com`)**:
   - Landmark `<header class="underlay-nav__header">` (`1440x98px`) hosting `First December Films · Ad Film Produ` navigation (`Home · Work · Directors · About · AI Ad Films`), DOM attributes (`data-wf-domain="1stdecember.com"`, `data-wf-page="6a530ef9dd045382387c1080"`, `data-wf-site="6a530ef3dd045382387c1010"`, `data-key="CANq2ndVhhRcE6Gj1ydbwg"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.section_about> — `1st December Films`)**:
   - Landmark `<section class="section_about">` presenting display lead `1st December Films` and copy excerpt *"First December Films is a Mumbai based advertising film house, an"* over `#efece7` canvas and `#20201e` ink.
3. **Primary Showcase & Content Grid (<section.section_work> — `India's most awarded ad film house`)**:
   - Landmark `<section class="section_work">` rendering section `India's most awarded ad film house` with copy *"E x p l o r e A l l W o r k"*, asset references (`cdn.prod.website-files.com`, `first-december-films.webflow.shar...`, `6acdf9b670164716e898eb2d_fav%20we...`, `6acdf9b6d5ee9f500bdfb333_fav%20we...`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.section_team-home> — `The one film a brand builds its ye`)**:
   - Landmark `<section class="section_team-home">` framing `The one film a brand builds its year around` and `what we are proud of` (*"Cannes Gold and Glass Lion winning producer, counted among the wo"*) with `#e5e7eb` surface cards, `#ffff00` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.demo-footer> — `https://1stdecember.com`)**:
   - Landmark `<footer class="demo-footer">` anchoring `First December Films · Ad Film P` footer links (`Home · Work · Directors · About · AI Ad Films`), copy *"Cannes Lions winning director (2014, 2016, 2017) and the onl"*, and `#9ca3b0` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `1st December Films` · sticky/fixed elements: `3`
- **Step 02** (`y=850px`, `5%`): Active landmark `INDIA'S MOST AWARDED AD FILM HOUSE` · sticky/fixed elements: `4`
- **Step 03** (`y=3400px`, `18%`): Active landmark `#Work` · sticky/fixed elements: `4`
- **Step 04** (`y=5950px`, `32%`): Active landmark `#Work` · sticky/fixed elements: `4`
- **Step 05** (`y=8500px`, `45%`): Active landmark `INDIA'S MOST AWARDED DIRECTORS & PRODUCERS` · sticky/fixed elements: `4`
- **Step 06** (`y=11050px`, `59%`): Active landmark `IGP: Amazing Gifts, Samay Par · IMPACT Ads 2024 (...` · sticky/fixed elements: `4`
- **Step 07** (`y=13600px`, `72%`): Active landmark `Manu` · sticky/fixed elements: `4`
- **Step 08** (`y=14400px`, `76%`): Active landmark `Manu` · sticky/fixed elements: `4`

### Multi-Page Internal Route Map
- **Listing Route (`/work`)**: `https://1stdecember.com/work` — H1: `WHAT WE ARE PROUD OF`, scrollHeight `17624px`, transition `direct` (`5465ms`)
- **Detail Route (`/work/malaysia-airlines`)**: `https://1stdecember.com/work/malaysia-airlines` — H1: `MALAYSIA AIRLINES`, scrollHeight `8292px`, transition `direct` (`1712ms`)
- **About Route (`/contact`)**: `https://1stdecember.com/contact` — H1: `Contact us`, scrollHeight `2342px`, transition `direct` (`3065ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: 1stdecember-com (First December Films · Ad Film Production House in India)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `1stdecember-com` (**First December Films · Ad Film Production House in India** — `https://1stdecember.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#efece7` canvas, `#20201e` ink, `#ffff00` accent).
- **Identity & Domain Context**: Mumbai advertising film production house with 150+ international awards. TVCs, brand films and digital campaigns for brands across India...
- **Primary Substrate**: `#efece7` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#20201e`, **Accent / Highlight**: `#ffff00`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#efece7` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#20201e` primary typography and `#ffff00` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Tartuffo Trial Regular` for display copy (`1st December Films`) with `Pp neue montreal Medium` and `DM Mono Medium`.
  - **Calibrated Spatial Grid & Motion**: Combines `1600px` container bounds (`gap: 96px`, padding `40px`) with `cubic-bezier(1,0,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `1stdecember-com` in your global stylesheet:

:root {
  /* First December Films · Ad Film Production House in India (1stdecember-com) — Live-Grounded CSS Variables */
  --brand--white-light: #efece7; /* Canvas / Surface Token (1stdecember-com) */
  --font-family--body: "Pp neue montreal Medium",Arial,sans-serif; /* Typography / Scale Token (1stdecember-com) */
  --_theme---text--primary: var(--brand--black-dark); /* Typography Ink Token (1stdecember-com) */
  --_typography---body--body-font-size: 1rem; /* Typography / Scale Token (1stdecember-com) */
  --_typography---body--body-line-height: var(--font-height--xlarge); /* Typography / Scale Token (1stdecember-com) */
  --_typography---body--body-font-weight: var(--font-weight--normal); /* Typography / Scale Token (1stdecember-com) */
  --_typography---body--body-letter-spacing: var(--letter-spacing--default); /* Typography / Scale Token (1stdecember-com) */
  --_layout---spacing--none: 0rem; /* Layout / Spatial Grid Token (1stdecember-com) */
  --font-family--heading: "Tartuffo Trial Regular",Arial,sans-serif; /* Typography Ink Token (1stdecember-com) */
  --_typography---h1--h1-font-size: 7.5rem; /* Typography / Scale Token (1stdecember-com) */
  --_typography---h1--h1-line-height: var(--font-height--tiny); /* Typography / Scale Token (1stdecember-com) */
  --_typography---h1--h1-font-weight: var(--font-weight--normal); /* Typography / Scale Token (1stdecember-com) */
  --_typography---h1--h1-letter-spacing: var(--letter-spacing--tighter); /* Typography / Scale Token (1stdecember-com) */
  --_typography---h2--h2-font-size: 5rem; /* Typography / Scale Token (1stdecember-com) */
  --_typography---h2--h2-line-height: var(--font-height--tiny); /* Typography / Scale Token (1stdecember-com) */
  --_typography---h2--h2-font-weight: var(--font-weight--normal); /* Typography / Scale Token (1stdecember-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#efece7` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#20201e` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#e5e7eb` — grounded in `var(--cal-bg-emphasis)` in `:root`
- **Interactive Accent / Highlight**: `#ffff00` — grounded in `.cta_blog_post { background-color: yellow }` (`#ffff00`)
- **Secondary / Muted Copy**: `#6b7280` — grounded in `var(--cal-text-subtle)` in `:root`
- **Structural Hairline Border**: `#9ca3b0` — grounded in `var(--cal-border-emphasis)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1600px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `40px` lateral canvas padding with `96px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1600px`, `gap: 96px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `40px` horizontal padding
- **Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`
- **Corner Radii**: `3px`, `100%`, `50%`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Tartuffo Trial Regular`
- **Body Font Stack**: `Pp neue montreal Medium`
- **Monospace / Technical Font Stack**: `DM Mono Medium`
- **H1 Display Rule**: live computed `h1` (`font-size: 120px`, `line-height: 120px`, `font-weight: 400`, `letter-spacing: -2.4px`); CSS variables `--_typography---h1--h1-font-size: 7.5rem`, `--_typography---h1--h1-line-height: var(--font-height--tiny)`, `--_typography---h1--h1-font-weight: var(--font-weight--normal)`; rule `h1` (`font-size: var(--text-base)`, `line-height: var(--tw-leading,var(...`)
- **H2 Section Rule**: live computed `h2` (`font-size: 299.52px`, `line-height: 254.592px`, `font-weight: 400`, `letter-spacing: -5.9904px`); CSS variables `--_typography---h2--h2-font-size: 5rem`, `--_typography---h2--h2-line-height: var(--font-height--tiny)`, `--_typography---h2--h2-font-weight: var(--font-weight--normal)`; rule `h2` (`font-size: var(--text-sm)`, `line-height: var(--tw-leading,var(...`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-family--body: "Pp neue montreal Medium",Arial,sans-serif`, `--_typography---body--body-font-size: 1rem`, `--_typography---body--body-line-height: var(--font-height--xlarge)`; rule `p` (`font-size: var(--text-sm)`, `line-height: var(--tw-leading,var(...`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--_typography---body--body-letter-spacing: var(--letter-spacing--default)`, `--_typography---h1--h1-letter-spacing: var(--letter-spacing--tighter)`, `--_typography---h2--h2-letter-spacing: var(--letter-spacing--tighter)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `1stdecember-com` (`First December Films · Ad Film Production House in India`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.underlay-nav__header> — `1stdecember-com`)**:
   - DOM & Selectors: Landmark `<header class="underlay-nav__header">` (`1440x98px`) hosting `First December Films · Ad Film Produ` navigation (`Home · Work · Directors · About · AI Ad Films`), DOM attributes (`data-wf-domain="1stdecember.com"`, `data-wf-page="6a530ef9dd045382387c1080"`, `data-wf-site="6a530ef3dd045382387c1010"`, `data-key="CANq2ndVhhRcE6Gj1ydbwg"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.underlay-nav__header> — `1stdecember-com`)` (`1stdecember-com`) adapts across `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)` with `cubic-bezier(1,0,0,1)`, `cubic-bezier(.645,.045,.355,1)`, `cubic-bezier(.4,0,1,1)` transitions and links `Home · Work · Directors · About · AI Ad Films`.
2. **Hero Stage & Focal Lead (<section.section_about> — `1st December Films`)**:
   - DOM & Selectors: Landmark `<section class="section_about">` presenting display lead `1st December Films` and copy excerpt *"First December Films is a Mumbai based advertising film house, an"* over `#efece7` canvas and `#20201e` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#efece7` background with `#20201e` headline `1st December Films`.
3. **Primary Showcase & Content Grid (<section.section_work> — `India's most awarded ad film house`)**:
   - DOM & Selectors: Landmark `<section class="section_work">` rendering section `India's most awarded ad film house` with copy *"E x p l o r e A l l W o r k"*, asset references (`cdn.prod.website-files.com`, `first-december-films.webflow.shar...`, `6acdf9b670164716e898eb2d_fav%20we...`, `6acdf9b6d5ee9f500bdfb333_fav%20we...`), and grid rule `summary { display:block }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.section_work> — `India's most awarded ad film house`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1600px`, `gap: 96px`) on desktop and Single-column vertical stack at `390px` viewport width with `40px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.section_team-home> — `The one film a brand builds its ye`)**:
   - DOM & Selectors: Landmark `<section class="section_team-home">` framing `The one film a brand builds its year around` and `what we are proud of` (*"Cannes Gold and Glass Lion winning producer, counted among the wo"*) with `#e5e7eb` surface cards, `#ffff00` accents, and `video { vertical-align:baseline;display:inline-block }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.section_team-home> — `The one film a brand builds its ye`)` uses `3px`, `100%`, `50%`, `2px` radii, `#ffff00` highlights, and assets (cdn.prod.website-files.com, first-december-films.webflow.shar..., 6acdf9b670164716e898eb2d_fav%20we...).
5. **Colophon & Global Directory Footer (<footer.demo-footer> — `https://1stdecember.com`)**:
   - DOM & Selectors: Landmark `<footer class="demo-footer">` anchoring `First December Films · Ad Film P` footer links (`Home · Work · Directors · About · AI Ad Films`), copy *"Cannes Lions winning director (2014, 2016, 2017) and the onl"*, and `#9ca3b0` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.demo-footer> — `https://1stdecember.com`)` aligns to `1600px` (non-`@media` desktop container stylesheet rule) with `40px` lateral canvas padding with `96px` grid gap and attributes (data-wf-domain="1stdecember.com", data-wf-page="6a530ef9dd045382387c1080", data-wf-site="6a530ef3dd045382387c1010").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"First December Films is a Mumbai based advertising film house, and one of the most..."*
- Copy Excerpt 2: *"E x p l o r e A l l W o r k"*
- Copy Excerpt 3: *"Cannes Gold and Glass Lion winning producer, counted among the world’s top TV comm..."*
- Copy Excerpt 4: *"Cannes Lions winning director (2014, 2016, 2017) and the only Indian ever named in..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(1,0,0,1)`, `cubic-bezier(.645,.045,.355,1)`, `cubic-bezier(.4,0,1,1)`
- **Extracted Stylesheet Rules (`1stdecember-com`)**:
- `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`
- `summary { display:block }`
- `video { vertical-align:baseline;display:inline-block }`
- `template { display:none }`
- `strong { font-weight:700 }`
- **Per-Selector Transition Rules**:
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `1stdecember-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `1stdecember-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `1stdecember-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(1,0,0,1)`)**: Governs interactive state transitions across `<header.underlay-nav__header>` and `<section.section_work>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `19767px` across 8 distinct viewport chapters using Lenis, GSAP/ScrollTrigger.
- **Vertical Chapter Sequence**: 1st December Films (0%) -> INDIA'S MOST AWARDED AD FIL... (5%) -> #Work (18%) -> #Work (32%) -> INDIA'S MOST AWARDED DIRECT... (45%) -> IGP: Amazing Gifts, Samay P... (59%) -> Manu (72%) -> Manu (76%).
- **Multi-Page Routes**: Scaffold internal routes `/work` (listing, direct), `/work/malaysia-airlines` (detail, direct), `/contact` (about, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `1stdecember-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | 1st December Films | `3` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `5%` | INDIA'S MOST AWARDED AD FILM HOUSE | `4` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `3400px` | `18%` | #Work | `4` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `5950px` | `32%` | #Work | `4` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `8500px` | `45%` | INDIA'S MOST AWARDED DIRECTORS & PRODUCERS | `4` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `11050px` | `59%` | IGP: Amazing Gifts, Samay Par · IMPACT Ads 20... | `4` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `13600px` | `72%` | Manu | `4` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `14400px` | `76%` | Manu | `4` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | 1st December Films | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `7200px` | `50%` | Shivang Monga | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `14400px` | `100%` | Paste the script. See how we would make it. | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `listing` | `https://1stdecember.com/work` | WHAT WE ARE PROUD OF | `17624px` | `direct` (`5465ms`) | [subpage-01-work.webp](assets/subpage-01-work.webp) |
| `2` | `detail` | `https://1stdecember.com/work/malaysia-airlines` | MALAYSIA AIRLINES | `8292px` | `direct` (`1712ms`) | [subpage-02-work-malaysia-airlines.webp](assets/subpage-02-work-malaysia-airlines.webp) |
| `3` | `about` | `https://1stdecember.com/contact` | Contact us | `2342px` | `direct` (`3065ms`) | [subpage-03-contact.webp](assets/subpage-03-contact.webp) |

