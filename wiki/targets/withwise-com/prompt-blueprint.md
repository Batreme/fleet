---
title: "UI Prompt Blueprint: withwise-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "withwise-com"
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
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#4e1c4f` canvas, `#ffffff` ink, `#00c2ff` accent)"
---

# UI Design System & Master Generation Blueprint: withwise-com

> **Compliance-First Onboarding Software · Wise** (https://withwise.com/) — Wise is built for self-employed workforces. We protect you from compliance risks, help you onboard users digitally, and pay them securely.

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Compliance-First Onboarding Software · Wise** (`https://withwise.com/`). Wise is built for self-employed workforces. We protect you from compliance risks, help you onboard users digitally, and pay them securely.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#4e1c4f` canvas, `#ffffff` ink, `#00c2ff` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#4e1c4f` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#00c2ff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Merriweather` for display copy (`Stay compliant. Pay on time. Grow wi`) with `Figtree` and `Consolas`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 4px`, padding `0.5rem`) with `cubic-bezier(0.47,0,0.74,0.71)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=13856px` / doc `14756px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1440px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `0.5rem` lateral canvas padding with `4px` grid gap.
- **Border Radius Scale**: `8px`, `2px`, `0px`, `4px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 4px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `0.5rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width:767px)`, `@media only screen and (min-width: 1025px)`, `@media only screen and (max-width: 1024px)`, `@media (min-width:640px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#4e1c4f` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `p` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#381334` | live computed `header` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#00c2ff` | `var(--gf-field-pg-prog-bar-bg-gradient-blues)` in `:root` |
| **Secondary / Muted Copy** | `#f2f3f5` | `var(--gf-color-secondary-darker)` in `:root` |
| **Structural Hairline Border** | `#dddddd` | `var(--border-color)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--wp--style--global--content-size` | `1170px` | Layout / Spatial Grid Token |
| `--wp--style--global--wide-size` | `1170px` | Layout / Spatial Grid Token |
| `--wp--style--block-gap` | `24px` | Layout / Spatial Grid Token |
| `--fa-family-brands` | `"Font Awesome 7 Brands"` | Brand / Palette Token |
| `--fa-font-brands` | `normal 400 1em/1 var(--fa-family-brands)` | Brand / Palette Token |
| `--fa-family-classic` | `"Font Awesome 7 Free"` | Typography / Scale Token |
| `--fa-font-regular` | `normal 400 1em/1 var(--fa-family-classic)` | Typography / Scale Token |
| `--fa-style-family-classic` | `var(--fa-family-classic)` | Typography / Scale Token |
| `--fa-font-solid` | `normal 900 1em/1 var(--fa-family-classic)` | Typography / Scale Token |
| `--input-fz` | `1rem` | Dimension / Scale Token |
| `--input-lh` | `1.5` | Design System Custom Token |
| `--input-pt` | `0.6875rem` | Dimension / Scale Token |
| `--input-pb` | `0.6875rem` | Dimension / Scale Token |
| `--input-pl` | `1rem` | Dimension / Scale Token |
| `--input-pr` | `1rem` | Dimension / Scale Token |
| `--input-bd` | `1px` | Dimension / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Merriweather`.
- **Primary Body Stack**: `Figtree`.
- **Technical / Metadata Stack**: `Consolas`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 60px`, `line-height: 84px`, `font-weight: 900`, `letter-spacing: -2px`); CSS variables `--gf-field-pwd-str-ind-display: inline-block`, `--gf-local-display: block`; rule `,.h1` (`font-size: 2.25rem`, `line-height: 1.4`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 42px`, `line-height: 58.8px`, `font-weight: 900`, `letter-spacing: -1px`); rule `,.h2` (`font-size: 1.8125rem`, `line-height: 1.4`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 300`); rule `p` (`font-size: var(--gf-ctrl-date-picker-hel...`, `line-height: var(--gf-ctrl-date-pi...`, `letter-spacing: var(--gf-ctrl-date-pi...`, `font-weight: var(--gf-ctrl...`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 300`); CSS variables `--gf-label-space-primary: 8px`, `--gf-label-choice-field-space-primary: 12px`, `--gf-label-space-x-secondary: 12px`; rule `small` (`line-height: 0`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.47,0,0.74,0.71)`, `cubic-bezier(0.22,0.61,0.36,1)`, `cubic-bezier(0.5,0,0.14,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.dashicons-before:before`**: `transition: color .1s ease-in` extracted from `withwise-com` stylesheet.
- **Selector `rap-header-menu button.mega-toggl...`**: `transition: none` extracted from `withwise-com` stylesheet.
- **Selector `ga-menu-header-menu .mega-descrip...`**: `transition: none` extracted from `withwise-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.47,0,0.74,0.71)`)**: Governs interactive state transitions across `<header.header>` and `<section.bg-type-dark>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `14756px`, deepest scrollY reached `13856px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `GSAP/ScrollTrigger`.
- **Hover Physics (`primary_cta` · `Book a demo`)**: `color`: `rgb(255, 255, 255)` -> `rgb(255, 253, 241)`; `backgroundColor`: `rgb(216, 30, 91)` -> `rgb(197, 27, 83)` (`transition-duration: 0.2s`, `timing: ease-in-out`).
- **Route Transition Architecture**: First internal navigation (`/blog/`) measured as `direct` in `2522ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Compliance-First Onboarding Software · Wis │
│ ====================================================================== │
│ [ <header.header> (1440x92px)         | Request a callback · Platfor ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.flx-section> (w=1440px)                       | │
│ | H1: Stay compliant. Pay on time. Grow without the risk.            | │
│ | Substrate: #4e1c4f | Ink: #ffffff | Accent: #00c2ff                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.bg-type-dark>) max-w: 1440px               | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Compliance-First Onboarding  |  | Stay compliant . Pay on time | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.flx-ft-grid>) — Why It Matters             | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>     ) | https://withwise.com/                │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 4px)        │
│ ====================================================================== │
│ [ HEADER BAR (<header.header>         ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.flx-section>) — 390px Vertical Lead           | │
│ | H1: Stay compliant. Pay on time. Grow without the risk.            | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.bg-type-dark>) — 1-Col Stack              | │
│ | [ Item 1: Compliance-First Onboarding software                   ] | │
│ | [ Item 2: Stay compliant . Pay on time . Grow without the r...   ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.flx-ft-grid>) — 1-Col (Why It Matters)      | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>     ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.header> — `withwise-com`)**:
   - Landmark `<header class="header">` (`1440x92px`) hosting `Compliance-First Onboarding Software` navigation (`Request a callback · Platform · See article · Industries · Why Wise`), DOM attributes (`data-scroll-dir-x="0"`, `data-scroll-dir-y="0"`, `data-loader="hs-scriptloader"`, `data-hsjs-portal="145539501"`), and stylesheet rule `.tablepress>.row-hover>tr { content-visibility:auto }`.
2. **Hero Stage & Focal Lead (<section.flx-section> — `Stay compliant. Pay on time. Grow `)**:
   - Landmark `<section class="flx-section flx-masthead-1">` presenting display lead `Stay compliant. Pay on time. Grow without the risk.` and copy excerpt *"Now live: October 2026 Right to work rules"* over `#4e1c4f` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.bg-type-dark> — `Compliance-First Onboarding softwa`)**:
   - Landmark `<section class="flx-section bg-type-dark">` rendering section `Compliance-First Onboarding software` with copy *"Onboard your workforce in minutes, pay them accurately, and keep "*, asset references (`web-interactives-embed.js`, `banner.js`, `collectedforms.js`, `145539501.js`), and grid rule `.tablepress img { border:none;margin:0;max-width:none;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.flx-ft-grid> — `Stay compliant . Pay on time . Gro`)**:
   - Landmark `<section class="flx-section bg-type-dark">` framing `Stay compliant . Pay on time . Grow without the r...` and `Why It Matters` (*"We look after your workforce too."*) with `#381334` surface cards, `#00c2ff` accents, and `.tablepress-table-description { clear:both;display:block }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://withwise.com/`)**:
   - Landmark `<footer class="footer">` anchoring `Compliance-First Onboarding Soft` footer links (`Request a callback · Platform · See article · Industries · Why Wise`), copy *"Payments powered by"*, and `#dddddd` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `Stay compliant. Pay on time. Grow without the risk.` · sticky/fixed elements: `2`
- **Step 02** (`y=850px`, `6%`): Active landmark `WHY IT MATTERS` · sticky/fixed elements: `1`
- **Step 03** (`y=3400px`, `25%`): Active landmark `ONE PLATFORM, END TO END` · sticky/fixed elements: `1`
- **Step 04** (`y=5950px`, `43%`): Active landmark `THE PROOF` · sticky/fixed elements: `1`
- **Step 05** (`y=8500px`, `61%`): Active landmark `We’re not just here for your business. We look af...` · sticky/fixed elements: `1`
- **Step 06** (`y=11050px`, `80%`): Active landmark `#flex-section-8` · sticky/fixed elements: `1`
- **Step 07** (`y=13600px`, `98%`): Active landmark `Footer` · sticky/fixed elements: `1`
- **Step 08** (`y=13856px`, `100%`): Active landmark `Footer` · sticky/fixed elements: `1`

### Multi-Page Internal Route Map
- **Listing Route (`/blog/`)**: `https://withwise.com/blog/` — H1: `Blogs.`, scrollHeight `4160px`, transition `direct` (`2522ms`)
- **Detail Route (`/talking/trust-id/`)**: `https://withwise.com/talking/trust-id/` — H1: `EP 26. Understand the latest Right to Work change...`, scrollHeight `2799px`, transition `direct` (`3573ms`)
- **About Route (`/contact/`)**: `https://withwise.com/contact/` — H1: `Let's talk.`, scrollHeight `2988px`, transition `direct` (`5902ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: withwise-com (Compliance-First Onboarding Software · Wise)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `withwise-com` (**Compliance-First Onboarding Software · Wise** — `https://withwise.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#4e1c4f` canvas, `#ffffff` ink, `#00c2ff` accent).
- **Identity & Domain Context**: Wise is built for self-employed workforces. We protect you from compliance risks, help you onboard users digitally, and pay them securely.
- **Primary Substrate**: `#4e1c4f` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#00c2ff`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#4e1c4f` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#00c2ff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Merriweather` for display copy (`Stay compliant. Pay on time. Grow wi`) with `Figtree` and `Consolas`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 4px`, padding `0.5rem`) with `cubic-bezier(0.47,0,0.74,0.71)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `withwise-com` in your global stylesheet:

:root {
  /* Compliance-First Onboarding Software · Wise (withwise-com) — Live-Grounded CSS Variables */
  --wp--style--global--content-size: 1170px; /* Layout / Spatial Grid Token (withwise-com) */
  --wp--style--global--wide-size: 1170px; /* Layout / Spatial Grid Token (withwise-com) */
  --wp--style--block-gap: 24px; /* Layout / Spatial Grid Token (withwise-com) */
  --fa-family-brands: "Font Awesome 7 Brands"; /* Brand / Palette Token (withwise-com) */
  --fa-font-brands: normal 400 1em/1 var(--fa-family-brands); /* Brand / Palette Token (withwise-com) */
  --fa-family-classic: "Font Awesome 7 Free"; /* Typography / Scale Token (withwise-com) */
  --fa-font-regular: normal 400 1em/1 var(--fa-family-classic); /* Typography / Scale Token (withwise-com) */
  --fa-style-family-classic: var(--fa-family-classic); /* Typography / Scale Token (withwise-com) */
  --fa-font-solid: normal 900 1em/1 var(--fa-family-classic); /* Typography / Scale Token (withwise-com) */
  --input-fz: 1rem; /* Dimension / Scale Token (withwise-com) */
  --input-lh: 1.5; /* Design System Custom Token (withwise-com) */
  --input-pt: 0.6875rem; /* Dimension / Scale Token (withwise-com) */
  --input-pb: 0.6875rem; /* Dimension / Scale Token (withwise-com) */
  --input-pl: 1rem; /* Dimension / Scale Token (withwise-com) */
  --input-pr: 1rem; /* Dimension / Scale Token (withwise-com) */
  --input-bd: 1px; /* Dimension / Scale Token (withwise-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#4e1c4f` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#ffffff` — grounded in live computed `p` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#381334` — grounded in live computed `header` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#00c2ff` — grounded in `var(--gf-field-pg-prog-bar-bg-gradient-blues)` in `:root`
- **Secondary / Muted Copy**: `#f2f3f5` — grounded in `var(--gf-color-secondary-darker)` in `:root`
- **Structural Hairline Border**: `#dddddd` — grounded in `var(--border-color)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `0.5rem` lateral canvas padding with `4px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 4px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `0.5rem` horizontal padding
- **Media Queries**: `@media screen and (max-width:767px)`, `@media only screen and (min-width: 1025px)`, `@media only screen and (max-width: 1024px)`, `@media (min-width:640px)`
- **Corner Radii**: `8px`, `2px`, `0px`, `4px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Merriweather`
- **Body Font Stack**: `Figtree`
- **Monospace / Technical Font Stack**: `Consolas`
- **H1 Display Rule**: live computed `h1` (`font-size: 60px`, `line-height: 84px`, `font-weight: 900`, `letter-spacing: -2px`); CSS variables `--gf-field-pwd-str-ind-display: inline-block`, `--gf-local-display: block`; rule `,.h1` (`font-size: 2.25rem`, `line-height: 1.4`)
- **H2 Section Rule**: live computed `h2` (`font-size: 42px`, `line-height: 58.8px`, `font-weight: 900`, `letter-spacing: -1px`); rule `,.h2` (`font-size: 1.8125rem`, `line-height: 1.4`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 300`); rule `p` (`font-size: var(--gf-ctrl-date-picker-hel...`, `line-height: var(--gf-ctrl-date-pi...`, `letter-spacing: var(--gf-ctrl-date-pi...`, `font-weight: var(--gf-ctrl...`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 300`); CSS variables `--gf-label-space-primary: 8px`, `--gf-label-choice-field-space-primary: 12px`, `--gf-label-space-x-secondary: 12px`; rule `small` (`line-height: 0`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `withwise-com` (`Compliance-First Onboarding Software · Wise`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header> — `withwise-com`)**:
   - DOM & Selectors: Landmark `<header class="header">` (`1440x92px`) hosting `Compliance-First Onboarding Software` navigation (`Request a callback · Platform · See article · Industries · Why Wise`), DOM attributes (`data-scroll-dir-x="0"`, `data-scroll-dir-y="0"`, `data-loader="hs-scriptloader"`, `data-hsjs-portal="145539501"`), and stylesheet rule `.tablepress>.row-hover>tr { content-visibility:auto }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header> — `withwise-com`)` (`withwise-com`) adapts across `@media screen and (max-width:767px)`, `@media only screen and (min-width: 1025px)`, `@media only screen and (max-width: 1024px)`, `@media (min-width:640px)` with `cubic-bezier(0.47,0,0.74,0.71)`, `cubic-bezier(0.22,0.61,0.36,1)`, `cubic-bezier(0.5,0,0.14,1)` transitions and links `Request a callback · Platform · See article · Industries · Why Wise`.
2. **Hero Stage & Focal Lead (<section.flx-section> — `Stay compliant. Pay on time. Grow `)**:
   - DOM & Selectors: Landmark `<section class="flx-section flx-masthead-1">` presenting display lead `Stay compliant. Pay on time. Grow without the risk.` and copy excerpt *"Now live: October 2026 Right to work rules"* over `#4e1c4f` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#4e1c4f` background with `#ffffff` headline `Stay compliant. Pay on time. Grow without the risk.`.
3. **Primary Showcase & Content Grid (<section.bg-type-dark> — `Compliance-First Onboarding softwa`)**:
   - DOM & Selectors: Landmark `<section class="flx-section bg-type-dark">` rendering section `Compliance-First Onboarding software` with copy *"Onboard your workforce in minutes, pay them accurately, and keep "*, asset references (`web-interactives-embed.js`, `banner.js`, `collectedforms.js`, `145539501.js`), and grid rule `.tablepress img { border:none;margin:0;max-width:none;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.bg-type-dark> — `Compliance-First Onboarding softwa`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 4px`) on desktop and Single-column vertical stack at `390px` viewport width with `0.5rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.flx-ft-grid> — `Stay compliant . Pay on time . Gro`)**:
   - DOM & Selectors: Landmark `<section class="flx-section bg-type-dark">` framing `Stay compliant . Pay on time . Grow without the r...` and `Why It Matters` (*"We look after your workforce too."*) with `#381334` surface cards, `#00c2ff` accents, and `.tablepress-table-description { clear:both;display:block }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.flx-ft-grid> — `Stay compliant . Pay on time . Gro`)` uses `8px`, `2px`, `0px`, `4px` radii, `#00c2ff` highlights, and assets (web-interactives-embed.js, banner.js, collectedforms.js).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://withwise.com/`)**:
   - DOM & Selectors: Landmark `<footer class="footer">` anchoring `Compliance-First Onboarding Soft` footer links (`Request a callback · Platform · See article · Industries · Why Wise`), copy *"Payments powered by"*, and `#dddddd` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://withwise.com/`)` aligns to `1440px` (non-`@media` desktop container stylesheet rule) with `0.5rem` lateral canvas padding with `4px` grid gap and attributes (data-scroll-dir-x="0", data-scroll-dir-y="0", data-loader="hs-scriptloader").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Now live: October 2026 Right to work rules"*
- Copy Excerpt 2: *"Onboard your workforce in minutes, pay them accurately, and keep on the right side..."*
- Copy Excerpt 3: *"We look after your workforce too."*
- Copy Excerpt 4: *"Payments powered by"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.47,0,0.74,0.71)`, `cubic-bezier(0.22,0.61,0.36,1)`, `cubic-bezier(0.5,0,0.14,1)`
- **Extracted Stylesheet Rules (`withwise-com`)**:
- `.tablepress>.row-hover>tr { content-visibility:auto }`
- `.tablepress img { border:none;margin:0;max-width:none;padding:0 }`
- `.tablepress-table-description { clear:both;display:block }`
- `.dt-scroll { width:100% }`
- `.dt-scroll .tablepress { width:100%!important }`
- **Per-Selector Transition Rules**:
- **Selector `.dashicons-before:before`**: `transition: color .1s ease-in` extracted from `withwise-com` stylesheet.
- **Selector `rap-header-menu button.mega-toggl...`**: `transition: none` extracted from `withwise-com` stylesheet.
- **Selector `ga-menu-header-menu .mega-descrip...`**: `transition: none` extracted from `withwise-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.47,0,0.74,0.71)`)**: Governs interactive state transitions across `<header.header>` and `<section.bg-type-dark>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `14756px` across 8 distinct viewport chapters using GSAP/ScrollTrigger.
- **Vertical Chapter Sequence**: Stay compliant. Pay on time... (0%) -> WHY IT MATTERS (6%) -> ONE PLATFORM, END TO END (25%) -> THE PROOF (43%) -> We’re not just here for you... (61%) -> #flex-section-8 (80%) -> Footer (98%) -> Footer (100%).
- **Hover Micro-Interaction (`primary_cta`)**: Animate `color, backgroundColor` with `0.2s ease-in-out`.
- **Multi-Page Routes**: Scaffold internal routes `/blog/` (listing, direct), `/talking/trust-id/` (detail, direct), `/contact/` (about, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `withwise-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | Stay compliant. Pay on time. Grow without the... | `2` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `6%` | WHY IT MATTERS | `1` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `3400px` | `25%` | ONE PLATFORM, END TO END | `1` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `5950px` | `43%` | THE PROOF | `1` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `8500px` | `61%` | We’re not just here for your business. We loo... | `1` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `11050px` | `80%` | #flex-section-8 | `1` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `13600px` | `98%` | Footer | `1` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `13856px` | `100%` | Footer | `1` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | Stay compliant. Pay on time. Grow without... | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `7200px` | `50%` | Andrew Main | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `14400px` | `100%` | See what Wise could take off your plate. | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `listing` | `https://withwise.com/blog/` | Blogs. | `4160px` | `direct` (`2522ms`) | [subpage-01-blog.webp](assets/subpage-01-blog.webp) |
| `2` | `detail` | `https://withwise.com/talking/trust-id/` | EP 26. Understand the latest Right to... | `2799px` | `direct` (`3573ms`) | [subpage-02-talking-trust-id.webp](assets/subpage-02-talking-trust-id.webp) |
| `3` | `about` | `https://withwise.com/contact/` | Let's talk. | `2988px` | `direct` (`5902ms`) | [subpage-03-contact.webp](assets/subpage-03-contact.webp) |

