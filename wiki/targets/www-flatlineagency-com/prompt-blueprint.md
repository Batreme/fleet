---
title: "UI Prompt Blueprint: www-flatlineagency-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "www-flatlineagency-com"
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
archetype: "Light-Substrate Editorial & Modular Grid System (`#f3f0e9` canvas, `#000000` ink, `#0000ee` accent)"
---

# UI Design System & Master Generation Blueprint: www-flatlineagency-com

> **Shopify, Marketing & AI Agency Amsterdam · Flatline** (https://www.flatlineagency.com/) — Flatline is a Shopify Platinum Partner in Amsterdam. We build, migrate and grow Shopify Plus stores and run marketing and AI for premium...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Shopify, Marketing & AI Agency Amsterdam · Flatline** (`https://www.flatlineagency.com/`). Flatline is a Shopify Platinum Partner in Amsterdam. We build, migrate and grow Shopify Plus stores and run marketing and AI for premium...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#f3f0e9` canvas, `#000000` ink, `#0000ee` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f3f0e9` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#0000ee` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Canela Web Thin` for display copy (`THE LUXURY STANDARD IN DIGITAL`) with `Canela Web Thin Placeholder`.
  - **Calibrated Spatial Grid & Motion**: Combines `1200px` container bounds (`gap: 16px`, padding `32px`) with `cubic-bezier(.44,0,.56,1)` easing and Framer Motion Layout Physics.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=6142px` / doc `7042px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1200px` (measured widest bounded `<section>` landmark width on `1440px` desktop).
- **Canvas Lateral Padding & Spacing**: `32px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `20px`, `8px`, `15px`, `0px`.

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
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 80px`, `line-height: 72px`, `font-weight: 100`); rule `h2` (`font-size: 40px`, `line-height: 1em`, `letter-spacing: 0px`, `font-weight: 100`).
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
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `7042px`, deepest scrollY reached `6142px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `Framer Motion`.
- **Nav / Drawer Probe**: Tested trigger `What we do` (diff `2.076`, below state-capture threshold).
- **Hover Physics (`primary_cta` · `Insights`)**: `opacity`: `0.4` -> `1` (`transition-duration: 0s`, `timing: ease`).
- **Route Transition Architecture**: First internal navigation (`/cases`) measured as `SPA` in `1195ms`.

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
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `THE LUXURY STANDARD IN DIGITAL` · sticky/fixed elements: `4`
- **Step 02** (`y=850px`, `14%`): Active landmark `THE LUXURY STANDARD IN DIGITAL` · sticky/fixed elements: `6`
- **Step 03** (`y=1700px`, `28%`): Active landmark `Commerce` · sticky/fixed elements: `6`
- **Step 04** (`y=3400px`, `55%`): Active landmark `Section @ 55%` · sticky/fixed elements: `1`
- **Step 05** (`y=4250px`, `69%`): Active landmark `About us` · sticky/fixed elements: `1`
- **Step 06** (`y=5100px`, `83%`): Active landmark `Ecommerce platforms compared (2026): the best web...` · sticky/fixed elements: `1`
- **Step 07** (`y=5950px`, `97%`): Active landmark `Let’s work together` · sticky/fixed elements: `1`
- **Step 08** (`y=6142px`, `100%`): Active landmark `We’d love to hear about your project.` · sticky/fixed elements: `1`

### Multi-Page Internal Route Map
- **Listing Route (`/cases`)**: `https://www.flatlineagency.com/cases` — H1: `THE LUXURY STANDARD IN DIGITAL`, scrollHeight `7042px`, transition `SPA` (`1195ms`)
- **Detail Route (`/services/ecommerce`)**: `https://www.flatlineagency.com/services/ecommerce` — H1: `WE MIGRATE THE COMPLICATED ONES`, scrollHeight `8397px`, transition `direct` (`5024ms`)
- **About Route (`/about-us`)**: `https://www.flatlineagency.com/about-us` — H1: `ABOUT FLATLINE`, scrollHeight `9430px`, transition `direct` (`809ms`)

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
  - **Grounded Typographic Hierarchy**: Pairs `Canela Web Thin` for display copy (`THE LUXURY STANDARD IN DIGITAL`) with `Canela Web Thin Placeholder`.
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
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1200px` (measured widest bounded `<section>` landmark width on `1440px` desktop)
- **Padding & Gutters**: `32px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1200px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `32px` horizontal padding
- **Media Queries**: `@media (min-width: 1200px)`, `@media (min-width: 810px) and (max-width: 1199.98px)`, `@media (max-width: 809.98px)`, `@media (max-width:1199px) and (min-width:810px)`
- **Corner Radii**: `20px`, `8px`, `15px`, `0px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Canela Web Thin`
- **Body Font Stack**: `Canela Web Thin Placeholder`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 80px`, `line-height: 72px`, `font-weight: 100`); CSS variables `--text-truncation-display-inline-for-safari-16: inline`, `--text-truncation-display-none-for-safari-16: none`; rule `h1` (`font-size: 80px`, `line-height: 90%`, `letter-spacing: 0em`, `font-weight: 100`)
- **H2 Section Rule**: live computed `h2` (`font-size: 80px`, `line-height: 72px`, `font-weight: 100`); rule `h2` (`font-size: 40px`, `line-height: 1em`, `letter-spacing: 0px`, `font-weight: 100`)
- **Body Copy Rule**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 16px`, `line-height: 1.2em`, `letter-spacing: 0em`, `font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); CSS variables `--letter-spacing: var(--framer-letter-spacing)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-flatlineagency-com` (`Shopify, Marketing & AI Agency Amsterdam · Flatline`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.framer-ha9xM> — `www-flatlineagency-com`)**:
   - DOM & Selectors: Landmark `<header class="framer-ha9xM framer-1sgxrsx">` (`1440x100px`) hosting `Shopify, Marketing & AI Agency Amste` navigation (`What we do · Work · About · Insights · Events`), DOM attributes (`data-redirect-timezone="1"`, `data-framer-generated-canonical`, `data-framer-font-css`, `data-framer-generated-hreflang`), and stylesheet rule `.hidden-72rtr7 { display:none!important }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.framer-ha9xM> — `www-flatlineagency-com`)` (`www-flatlineagency-com`) adapts across `@media (min-width: 1200px)`, `@media (min-width: 810px) and (max-width: 1199.98px)`, `@media (max-width: 809.98px)`, `@media (max-width:1199px) and (min-width:810px)` with `cubic-bezier(.44,0,.56,1)` transitions and links `What we do · Work · About · Insights · Events`.
2. **Hero Stage & Focal Lead (<section.framer-yjze81> — `THE LUXURY STANDARD IN DIGITAL`)**:
   - DOM & Selectors: Landmark `<section class="framer-yjze81">` presenting display lead `THE LUXURY STANDARD IN DIGITAL` and copy excerpt *"We build and run the digital side of premium consumer brands."* over `#f3f0e9` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#f3f0e9` background with `#000000` headline `THE LUXURY STANDARD IN DIGITAL`.
3. **Primary Showcase & Content Grid (<section.framer-yjze81:nth(2)> — `Elevating modern menswear through `)**:
   - DOM & Selectors: Landmark `<section class="framer-yjze81">` rendering section `Elevating modern menswear through a refined digit...` with copy *"350+ Shopify Plus migrations"*, asset references (`goPYDmczsQmWoGJRaZvSdomTZc.png`, `fonts.gstatic.com`, `script`, `gv5TmFnYtTK9GLZ9FjU09gs1guk.mp4`), and grid rule `.hidden-19c8o6d { display:none!important }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.framer-yjze81:nth(2)> — `Elevating modern menswear through `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1200px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `32px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.framer-yjze81:nth(3)> — `Powering a smoother digital journe`)**:
   - DOM & Selectors: Landmark `<section class="framer-yjze81">` framing `Powering a smoother digital journey for cycling e...` and `Crafting a premium digital home for contemporary...` (*"2x Agency of the Year"*) with `#050505` surface cards, `#0000ee` accents, and `.hidden-1us1r0u { display:none!important }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.framer-yjze81:nth(3)> — `Powering a smoother digital journe`)` uses `20px`, `8px`, `15px`, `0px` radii, `#0000ee` highlights, and assets (goPYDmczsQmWoGJRaZvSdomTZc.png, fonts.gstatic.com, script).
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
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `7042px` across 8 distinct viewport chapters using Framer Motion.
- **Vertical Chapter Sequence**: THE LUXURY STANDARD IN DIGITAL (0%) -> THE LUXURY STANDARD IN DIGITAL (14%) -> Commerce (28%) -> Section @ 55% (55%) -> About us (69%) -> Ecommerce platforms compare... (83%) -> Let’s work together (97%) -> We’d love to hear about you... (100%).
- **Hover Micro-Interaction (`primary_cta`)**: Animate `opacity` with `0s ease`.
- **Multi-Page Routes**: Scaffold internal routes `/cases` (listing, SPA), `/services/ecommerce` (detail, direct), `/about-us` (about, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-flatlineagency-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | THE LUXURY STANDARD IN DIGITAL | `4` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `14%` | THE LUXURY STANDARD IN DIGITAL | `6` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `1700px` | `28%` | Commerce | `6` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `3400px` | `55%` | Section @ 55% | `1` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `4250px` | `69%` | About us | `1` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `5100px` | `83%` | Ecommerce platforms compared (2026): the best... | `1` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `5950px` | `97%` | Let’s work together | `1` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `6142px` | `100%` | We’d love to hear about your project. | `1` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | THE LUXURY STANDARD IN DIGITAL | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `3106px` | `50%` | Join our exclusive events | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `6213px` | `100%` | Footer | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `listing` | `https://www.flatlineagency.com/cases` | THE LUXURY STANDARD IN DIGITAL | `7042px` | `SPA` (`1195ms`) | [subpage-01-cases.webp](assets/subpage-01-cases.webp) |
| `2` | `detail` | `https://www.flatlineagency.com/services/ecommerce` | WE MIGRATE THE COMPLICATED ONES | `8397px` | `direct` (`5024ms`) | [subpage-02-services-ecommerce.webp](assets/subpage-02-services-ecommerce.webp) |
| `3` | `about` | `https://www.flatlineagency.com/about-us` | ABOUT FLATLINE | `9430px` | `direct` (`809ms`) | [subpage-03-about-us.webp](assets/subpage-03-about-us.webp) |

