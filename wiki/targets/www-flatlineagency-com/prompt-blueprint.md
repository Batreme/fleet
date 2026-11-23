---
title: "UI Prompt Blueprint: www-flatlineagency-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-flatlineagency-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#f3f0e9` canvas, `#000000` ink, `#0000ee` accent)"
---

# UI Design System & Master Generation Blueprint: www-flatlineagency-com

> **Shopify, Marketing & AI Agency Amsterdam · Flatline** (https://www.flatlineagency.com/) — Flatline is a Shopify Platinum Partner in Amsterdam. We build, migrate and grow Shopify Plus stores and run marketing and AI for premium...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Shopify, Marketing & AI Agency Amsterdam · Flatline** (`https://www.flatlineagency.com/`). Flatline is a Shopify Platinum Partner in Amsterdam. We build, migrate and grow Shopify Plus stores and run marketing and AI for premium...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#f3f0e9` canvas, `#000000` ink, `#0000ee` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f3f0e9` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#0000ee` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Canela Web Thin` for display copy (`THE LUXURY STANDARD IN DIGITAL`) with `Canela Web Thin Placeholder` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1200px` container bounds (`gap: 16px`, padding `32px`) with `cubic-bezier(.44,0,.56,1)` easing and Framer Motion Layout Physics.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1200px` (measured widest bounded `<section>` landmark width on `1440px` desktop).
- **Canvas Lateral Padding & Spacing**: `32px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `20px`, `8px`, `15px`, `100px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1200px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `32px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width: 1200px)`, `@media (min-width: 810px) and (max-width: 1199.98px)`, `@media (max-width: 809.98px)`, `@media (max-width:1199px) and (min-width:810px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f3f0e9` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#050505` | `var(--selection-background-color)` in `:root` |
| **Interactive Accent / Highlight** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#dedbd6` | `var(--border-color)` in `:root` (`8883`) |
| **Variable Token (`--token-715d5f28-67a4-4211-a580-93fd5f080aaa`)** | `#fdfaf5` | `var(--token-715d5f28-67a4-4211-a580-93fd5f080aaa)` in `:root` |
| **Variable Token (`--token-a1931803-7cdb-4638-b54d-105fe7944f17`)** | `#ece9e0` | `var(--token-a1931803-7cdb-4638-b54d-105fe7944f17)` in `:root` |
| **Variable Token (`--token-9218c30c-f55e-4ab0-8878-b6991b7cf484`)** | `#0a2315` | `var(--token-9218c30c-f55e-4ab0-8878-b6991b7cf484)` in `:root` |
| **Variable Token (`--token-054adc8c-fb63-490f-a5ca-c48666fdfb8c`)** | `#060f23` | `var(--token-054adc8c-fb63-490f-a5ca-c48666fdfb8c)` in `:root` |
| **Variable Token (`--token-758cee22-2452-4bed-9dbf-0b445d8c6457`)** | `#afdbf6` | `var(--token-758cee22-2452-4bed-9dbf-0b445d8c6457)` in `:root` |
| **Variable Token (`--token-84e9d4de-a1f9-41a3-90c4-b17803185d3f`)** | `#4cc352` | `var(--token-84e9d4de-a1f9-41a3-90c4-b17803185d3f)` in `:root` |
| **Variable Token (`--token-523425b1-9af9-406c-86b2-b80d42d167c2`)** | `#ff2142` | `var(--token-523425b1-9af9-406c-86b2-b80d42d167c2)` in `:root` |
| **Variable Token (`--token-3f6d4d2a-4271-4963-bcc0-922062838b2e`)** | `#0003` | `var(--token-3f6d4d2a-4271-4963-bcc0-922062838b2e)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--token-ee10f296-15d9-41da-871d-89b364a646e0` | `#f3f0e9` | Color / Atmospheric Token |
| `--token-715d5f28-67a4-4211-a580-93fd5f080aaa` | `#fdfaf5` | Color / Atmospheric Token |
| `--token-a1931803-7cdb-4638-b54d-105fe7944f17` | `#ece9e0` | Color / Atmospheric Token |
| `--token-1efbab02-5753-4dc6-9b5a-17f4306b9402` | `#000` | Color / Atmospheric Token |
| `--token-417808d0-1dfe-483f-9164-e0725b1b82a7` | `#050505` | Color / Atmospheric Token |
| `--token-9218c30c-f55e-4ab0-8878-b6991b7cf484` | `#0a2315` | Color / Atmospheric Token |
| `--token-054adc8c-fb63-490f-a5ca-c48666fdfb8c` | `#060f23` | Color / Atmospheric Token |
| `--token-758cee22-2452-4bed-9dbf-0b445d8c6457` | `#afdbf6` | Color / Atmospheric Token |
| `--token-84e9d4de-a1f9-41a3-90c4-b17803185d3f` | `#4cc352` | Color / Atmospheric Token |
| `--token-523425b1-9af9-406c-86b2-b80d42d167c2` | `#ff2142` | Color / Atmospheric Token |
| `--token-3f6d4d2a-4271-4963-bcc0-922062838b2e` | `#0003` | Color / Atmospheric Token |
| `--text-decoration-skip-ink` | `var(--framer-text-decoration-skip-ink)` | Typography Ink Token |
| `--text-underline-offset` | `var(--framer-text-decoration-offset)` | Typography Ink Token |
| `--font-family` | `var(--framer-font-family)` | Typography / Scale Token |
| `--font-style` | `var(--framer-font-style)` | Typography / Scale Token |
| `--font-weight` | `var(--framer-font-weight)` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Canela Web Thin`.
- **Primary Body Stack**: `Canela Web Thin Placeholder`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 80px`, `line-height: 72px`, `font-weight: 100`); CSS variables `--text-truncation-display-inline-for-safari-16: inline`, `--text-truncation-display-none-for-safari-16: none`; rule `h1` (`font-size: 80px`, `line-height: 90%`, `letter-spacing: 0em`, `font-weight: 100`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 40px`, `line-height: 40px`, `font-weight: 100`); rule `h2` (`font-size: 40px`, `line-height: 1em`, `letter-spacing: 0px`, `font-weight: 100`).
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 16px`, `line-height: 1.2em`, `letter-spacing: 0em`, `font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); CSS variables `--letter-spacing: var(--framer-letter-spacing)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.44,0,.56,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.framer-form-input-wrapper:after`**: `transition: var(--framer-input-focused-transition)` extracted from `www-flatlineagency-com` stylesheet.
- **Selector `.framer-form-input-wrapper`**: `transition: var(--framer-input-focused-transition)` extracted from `www-flatlineagency-com` stylesheet.
- **Selector `.framer-form-text-input-clear`**: `transition: color .15s` extracted from `www-flatlineagency-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.44,0,.56,1)`)**: Governs interactive state transitions across `<header.framer-ha9xM>` and `<section.framer-yjze81:nth(2)>`.
- **Runtime Interaction Engine**: Integrates Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Shopify, Marketing & AI Agency Amsterdam · │
│ ====================================================================== │
│ [ <header.framer-ha9xM> (1440x100px)  | What we do · Work · About ·  ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.framer-yjze81> (w=1440px)                     | │
│ | H1: THE LUXURY STANDARD IN DIGITAL                                 | │
│ | Substrate: #f3f0e9 | Ink: #000000 | Accent: #0000ee                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.framer-yjze81:nth) max-w: 1200px           | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Elevating modern menswear th |  | Powering a smoother digital  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.framer-yjze81:nth) — Crafting a premium di | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.framer-uH155) | https://www.flatlineagency.com/      │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.framer-ha9xM>   ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.framer-yjze81>) — 390px Vertical Lead         | │
│ | H1: THE LUXURY STANDARD IN DIGITAL                                 | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.framer-yjze81) — 1-Col Stack              | │
│ | [ Item 1: Elevating modern menswear through a refined digit...   ] | │
│ | [ Item 2: Powering a smoother digital journey for cycling e...   ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.framer-yjze81:n) — 1-Col (Crafting a premium) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.framer-uH155) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.framer-ha9xM> — `www-flatlineagency-com`)**:
   - Landmark `<header class="framer-ha9xM framer-1sgxrsx">` (`1440x100px`) hosting `Shopify, Marketing & AI Agency Amste` navigation (`What we do · Work · About · Insights · Events`), DOM attributes (`data-redirect-timezone="1"`, `data-framer-generated-canonical`, `data-framer-font-css`, `data-framer-generated-hreflang`), and stylesheet rule `.hidden-72rtr7 { display:none!important }`.
2. **Hero Stage & Focal Lead (<section.framer-yjze81> — `THE LUXURY STANDARD IN DIGITAL`)**:
   - Landmark `<section class="framer-yjze81">` presenting display lead `THE LUXURY STANDARD IN DIGITAL` and copy excerpt *"We build and run the digital side of premium consumer brands."* over `#f3f0e9` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.framer-yjze81:nth(2)> — `Elevating modern menswear through `)**:
   - Landmark `<section class="framer-yjze81">` rendering section `Elevating modern menswear through a refined digit...` with copy *"350+ Shopify Plus migrations"*, asset references (`goPYDmczsQmWoGJRaZvSdomTZc.png`, `fonts.gstatic.com`, `script`, `gv5TmFnYtTK9GLZ9FjU09gs1guk.mp4`), and grid rule `.hidden-19c8o6d { display:none!important }`.
4. **Interactive Detail & Feature Matrix (<section.framer-yjze81:nth(3)> — `Powering a smoother digital journe`)**:
   - Landmark `<section class="framer-yjze81">` framing `Powering a smoother digital journey for cycling e...` and `Crafting a premium digital home for contemporary...` (*"2x Agency of the Year"*) with `#050505` surface cards, `#0000ee` accents, and `.hidden-1us1r0u { display:none!important }`.
5. **Colophon & Global Directory Footer (<footer.framer-uH155> — `https://www.flatlineagency.com/`)**:
   - Landmark `<footer class="framer-uH155 framer-gkoC1">` anchoring `Shopify, Marketing & AI Agency A` footer links (`What we do · Work · About · Insights · Events`), copy *"Omnichannel eCommerce, where every touchpoint is united"*, and `#dedbd6` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-flatlineagency-com (Shopify, Marketing & AI Agency Amsterdam · Flatline)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-flatlineagency-com` (**Shopify, Marketing & AI Agency Amsterdam · Flatline** — `https://www.flatlineagency.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#f3f0e9` canvas, `#000000` ink, `#0000ee` accent).
- **Identity & Domain Context**: Flatline is a Shopify Platinum Partner in Amsterdam. We build, migrate and grow Shopify Plus stores and run marketing and AI for premium...
- **Primary Substrate**: `#f3f0e9` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#0000ee`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f3f0e9` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#0000ee` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Canela Web Thin` for display copy (`THE LUXURY STANDARD IN DIGITAL`) with `Canela Web Thin Placeholder` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1200px` container bounds (`gap: 16px`, padding `32px`) with `cubic-bezier(.44,0,.56,1)` easing and Framer Motion Layout Physics.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-flatlineagency-com` in your global stylesheet:

:root {
  /* Shopify, Marketing & AI Agency Amsterdam · Flatline (www-flatlineagency-com) — Live-Grounded CSS Variables */
  --token-ee10f296-15d9-41da-871d-89b364a646e0: #f3f0e9; /* Color / Atmospheric Token (www-flatlineagency-com) */
  --token-715d5f28-67a4-4211-a580-93fd5f080aaa: #fdfaf5; /* Color / Atmospheric Token (www-flatlineagency-com) */
  --token-a1931803-7cdb-4638-b54d-105fe7944f17: #ece9e0; /* Color / Atmospheric Token (www-flatlineagency-com) */
  --token-1efbab02-5753-4dc6-9b5a-17f4306b9402: #000; /* Color / Atmospheric Token (www-flatlineagency-com) */
  --token-417808d0-1dfe-483f-9164-e0725b1b82a7: #050505; /* Color / Atmospheric Token (www-flatlineagency-com) */
  --token-9218c30c-f55e-4ab0-8878-b6991b7cf484: #0a2315; /* Color / Atmospheric Token (www-flatlineagency-com) */
  --token-054adc8c-fb63-490f-a5ca-c48666fdfb8c: #060f23; /* Color / Atmospheric Token (www-flatlineagency-com) */
  --token-758cee22-2452-4bed-9dbf-0b445d8c6457: #afdbf6; /* Color / Atmospheric Token (www-flatlineagency-com) */
  --token-84e9d4de-a1f9-41a3-90c4-b17803185d3f: #4cc352; /* Color / Atmospheric Token (www-flatlineagency-com) */
  --token-523425b1-9af9-406c-86b2-b80d42d167c2: #ff2142; /* Color / Atmospheric Token (www-flatlineagency-com) */
  --token-3f6d4d2a-4271-4963-bcc0-922062838b2e: #0003; /* Color / Atmospheric Token (www-flatlineagency-com) */
  --text-decoration-skip-ink: var(--framer-text-decoration-skip-ink); /* Typography Ink Token (www-flatlineagency-com) */
  --text-underline-offset: var(--framer-text-decoration-offset); /* Typography Ink Token (www-flatlineagency-com) */
  --font-family: var(--framer-font-family); /* Typography / Scale Token (www-flatlineagency-com) */
  --font-style: var(--framer-font-style); /* Typography / Scale Token (www-flatlineagency-com) */
  --font-weight: var(--framer-font-weight); /* Typography / Scale Token (www-flatlineagency-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f3f0e9` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#050505` — grounded in `var(--selection-background-color)` in `:root`
- **Interactive Accent / Highlight**: `#0000ee` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Secondary / Muted Copy**: `#0000ee` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#dedbd6` — grounded in `var(--border-color)` in `:root` (`8883`)
- **Variable Token (`--token-715d5f28-67a4-4211-a580-93fd5f080aaa`)**: `#fdfaf5` — grounded in `var(--token-715d5f28-67a4-4211-a580-93fd5f080aaa)` in `:root`
- **Variable Token (`--token-a1931803-7cdb-4638-b54d-105fe7944f17`)**: `#ece9e0` — grounded in `var(--token-a1931803-7cdb-4638-b54d-105fe7944f17)` in `:root`
- **Variable Token (`--token-9218c30c-f55e-4ab0-8878-b6991b7cf484`)**: `#0a2315` — grounded in `var(--token-9218c30c-f55e-4ab0-8878-b6991b7cf484)` in `:root`
- **Variable Token (`--token-054adc8c-fb63-490f-a5ca-c48666fdfb8c`)**: `#060f23` — grounded in `var(--token-054adc8c-fb63-490f-a5ca-c48666fdfb8c)` in `:root`
- **Variable Token (`--token-758cee22-2452-4bed-9dbf-0b445d8c6457`)**: `#afdbf6` — grounded in `var(--token-758cee22-2452-4bed-9dbf-0b445d8c6457)` in `:root`
- **Variable Token (`--token-84e9d4de-a1f9-41a3-90c4-b17803185d3f`)**: `#4cc352` — grounded in `var(--token-84e9d4de-a1f9-41a3-90c4-b17803185d3f)` in `:root`
- **Variable Token (`--token-523425b1-9af9-406c-86b2-b80d42d167c2`)**: `#ff2142` — grounded in `var(--token-523425b1-9af9-406c-86b2-b80d42d167c2)` in `:root`
- **Variable Token (`--token-3f6d4d2a-4271-4963-bcc0-922062838b2e`)**: `#0003` — grounded in `var(--token-3f6d4d2a-4271-4963-bcc0-922062838b2e)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1200px` (measured widest bounded `<section>` landmark width on `1440px` desktop)
- **Padding & Gutters**: `32px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1200px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `32px` horizontal padding
- **Media Queries**: `@media (min-width: 1200px)`, `@media (min-width: 810px) and (max-width: 1199.98px)`, `@media (max-width: 809.98px)`, `@media (max-width:1199px) and (min-width:810px)`
- **Corner Radii**: `20px`, `8px`, `15px`, `100px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Canela Web Thin`
- **Body Font Stack**: `Canela Web Thin Placeholder`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 80px`, `line-height: 72px`, `font-weight: 100`); CSS variables `--text-truncation-display-inline-for-safari-16: inline`, `--text-truncation-display-none-for-safari-16: none`; rule `h1` (`font-size: 80px`, `line-height: 90%`, `letter-spacing: 0em`, `font-weight: 100`)
- **H2 Section Rule**: live computed `h2` (`font-size: 40px`, `line-height: 40px`, `font-weight: 100`); rule `h2` (`font-size: 40px`, `line-height: 1em`, `letter-spacing: 0px`, `font-weight: 100`)
- **Body Copy Rule**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 16px`, `line-height: 1.2em`, `letter-spacing: 0em`, `font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); CSS variables `--letter-spacing: var(--framer-letter-spacing)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-flatlineagency-com` (`Shopify, Marketing & AI Agency Amsterdam · Flatline`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.framer-ha9xM> — `www-flatlineagency-com`)**:
   - DOM & Selectors: Landmark `<header class="framer-ha9xM framer-1sgxrsx">` (`1440x100px`) hosting `Shopify, Marketing & AI Agency Amste` navigation (`What we do · Work · About · Insights · Events`), DOM attributes (`data-redirect-timezone="1"`, `data-framer-generated-canonical`, `data-framer-font-css`, `data-framer-generated-hreflang`), and stylesheet rule `.hidden-72rtr7 { display:none!important }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.framer-ha9xM> — `www-flatlineagency-com`)` (`www-flatlineagency-com`) adapts across `@media (min-width: 1200px)`, `@media (min-width: 810px) and (max-width: 1199.98px)`, `@media (max-width: 809.98px)`, `@media (max-width:1199px) and (min-width:810px)` with `cubic-bezier(.44,0,.56,1)` transitions and links `What we do · Work · About · Insights · Events`.
2. **Hero Stage & Focal Lead (<section.framer-yjze81> — `THE LUXURY STANDARD IN DIGITAL`)**:
   - DOM & Selectors: Landmark `<section class="framer-yjze81">` presenting display lead `THE LUXURY STANDARD IN DIGITAL` and copy excerpt *"We build and run the digital side of premium consumer brands."* over `#f3f0e9` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#f3f0e9` background with `#000000` headline `THE LUXURY STANDARD IN DIGITAL`.
3. **Primary Showcase & Content Grid (<section.framer-yjze81:nth(2)> — `Elevating modern menswear through `)**:
   - DOM & Selectors: Landmark `<section class="framer-yjze81">` rendering section `Elevating modern menswear through a refined digit...` with copy *"350+ Shopify Plus migrations"*, asset references (`goPYDmczsQmWoGJRaZvSdomTZc.png`, `fonts.gstatic.com`, `script`, `gv5TmFnYtTK9GLZ9FjU09gs1guk.mp4`), and grid rule `.hidden-19c8o6d { display:none!important }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.framer-yjze81:nth(2)> — `Elevating modern menswear through `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1200px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `32px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.framer-yjze81:nth(3)> — `Powering a smoother digital journe`)**:
   - DOM & Selectors: Landmark `<section class="framer-yjze81">` framing `Powering a smoother digital journey for cycling e...` and `Crafting a premium digital home for contemporary...` (*"2x Agency of the Year"*) with `#050505` surface cards, `#0000ee` accents, and `.hidden-1us1r0u { display:none!important }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.framer-yjze81:nth(3)> — `Powering a smoother digital journe`)` uses `20px`, `8px`, `15px`, `100px` radii, `#0000ee` highlights, and assets (goPYDmczsQmWoGJRaZvSdomTZc.png, fonts.gstatic.com, script).
5. **Colophon & Global Directory Footer (<footer.framer-uH155> — `https://www.flatlineagency.com/`)**:
   - DOM & Selectors: Landmark `<footer class="framer-uH155 framer-gkoC1">` anchoring `Shopify, Marketing & AI Agency A` footer links (`What we do · Work · About · Insights · Events`), copy *"Omnichannel eCommerce, where every touchpoint is united"*, and `#dedbd6` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.framer-uH155> — `https://www.flatlineagency.com/`)` aligns to `1200px` (measured widest bounded `<section>` landmark width on `1440px` desktop) with `32px` lateral canvas padding with `16px` grid gap and attributes (data-redirect-timezone="1", data-framer-generated-canonical, data-framer-font-css).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"We build and run the digital side of premium consumer brands."*
- Copy Excerpt 2: *"350+ Shopify Plus migrations"*
- Copy Excerpt 3: *"2x Agency of the Year"*
- Copy Excerpt 4: *"Omnichannel eCommerce, where every touchpoint is united"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.44,0,.56,1)`
- **Extracted Stylesheet Rules (`www-flatlineagency-com`)**:
- `.hidden-72rtr7 { display:none!important }`
- `.hidden-19c8o6d { display:none!important }`
- `.hidden-1us1r0u { display:none!important }`
- `.hidden-ds8oqe { display:none!important }`
- `.hidden-11hm25s { display:none!important }`
- **Per-Selector Transition Rules**:
- **Selector `.framer-form-input-wrapper:after`**: `transition: var(--framer-input-focused-transition)` extracted from `www-flatlineagency-com` stylesheet.
- **Selector `.framer-form-input-wrapper`**: `transition: var(--framer-input-focused-transition)` extracted from `www-flatlineagency-com` stylesheet.
- **Selector `.framer-form-text-input-clear`**: `transition: color .15s` extracted from `www-flatlineagency-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.44,0,.56,1)`)**: Governs interactive state transitions across `<header.framer-ha9xM>` and `<section.framer-yjze81:nth(2)>`.
- **Runtime Interaction Engine**: Integrates Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-flatlineagency-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
