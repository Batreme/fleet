---
title: "UI Prompt Blueprint: www-allerstudio-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "www-allerstudio-com"
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
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#f9fafb` / `#0000ff`)"
---

# UI Design System & Master Generation Blueprint: www-allerstudio-com

> **ALLER Studio — Product design and development studio** (https://www.allerstudio.com/) — Product design and development studio for Web3, AI, fintech, and gaming.

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **ALLER Studio — Product design and development studio** (`https://www.allerstudio.com/`). Product design and development studio for Web3, AI, fintech, and gaming.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#f9fafb` / `#0000ff`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f9fafb` (live computed `html` `background-color` (`computed_styles.json`)) paired with `#121212` primary typography and `#0000ff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Rajdhani` for display copy (`Product design and development studi`) with `Inter`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: var(--btn-gap)`, padding `var(--btn-px)`) with `cubic-bezier(0,0,.2,1)` easing and Framer Motion Layout Physics, HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=11050px` / doc `13857px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1440px` (live computed `main` `max-width`).
- **Canvas Lateral Padding & Spacing**: `var(--btn-px)` lateral canvas padding with `var(--btn-gap)` grid gap.
- **Border Radius Scale**: `3.35544e+07px`, `999px`, `.25rem`, `var(--radius-2xl)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: var(--btn-gap)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--btn-px)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f9fafb` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#121212` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f6f7f8` | `var(--color-surface-bg-2)` in `:root` |
| **Interactive Accent / Highlight** | `#0000ff` | `:text-blue-600 a:hover { color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#787878` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#dadee2` | `var(--color-border)` in `:root` |
| **Variable Token (`--color-black`)** | `#000000` | `var(--color-black)` in `:root` |
| **Variable Token (`--color-white`)** | `#ffffff` | `var(--color-white)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--duration-quick` | `.15s` | Motion / Easing Token |
| `--duration-fast` | `.25s` | Motion / Easing Token |
| `--duration-medium` | `.35s` | Motion / Easing Token |
| `--duration-very-slow` | `.5s` | Motion / Easing Token |
| `--ease-smooth-out` | `cubic-bezier(.22, 1, .36, 1)` | Motion / Easing Token |
| `--ease-bounce` | `cubic-bezier(.34, 1.35, .64, 1)` | Motion / Easing Token |
| `--font-inter` | `"Inter", "Inter Fallback"` | Typography / Scale Token |
| `--font-rajdhani` | `"Rajdhani", "Rajdhani Fallback"` | Typography / Scale Token |
| `--font-sans` | `var(--font-inter), "Helvetica Neue", Arial, sans-serif` | Typography / Scale Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25 / .875)` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Rajdhani`.
- **Primary Body Stack**: `Inter`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 48px`, `line-height: 56px`, `font-weight: 600`); CSS variables `--text-5xl: 3rem`, `--text-5xl--line-height: 1`, `--font-display: var(--font-rajdhani), "Arial Narrow", sans-serif`; rule `h1` (`font-size: var(--text-base)`, `line-height: var(--tw-leading,var(...`).
- **Section Heading (`H2`)**: live computed `h2 (largest visible desktop heading)` (`font-size: 64px`, `line-height: 1.2`, `font-weight: 600`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: var(--text-sm)`, `line-height: var(--tw-leading,var(...`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: var(--text-sm)`, `line-height: var(--tw-leading,var(...`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `www-allerstudio-com` stylesheet.
- **Selector `layer components`**: `transition: padding .35s var(--ease-out-expo), gap .35s var(--ease-out-exp...` extracted from `www-allerstudio-com` stylesheet.
- **Selector `.btn-dark:before`**: `transition: opacity .35s` extracted from `www-allerstudio-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.header-in>` and `<section.relative>`.
- **Runtime Interaction Engine**: Integrates Framer Motion Layout Physics, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `13857px`, deepest scrollY reached `11050px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `WebGL/Canvas`.
- **Hover Physics (`primary_cta` · `Book a call with Bruno`)**: `boxShadow`: `none` -> `rgba(0, 0, 0, 0) 0px 0p...` (`transition-duration: 0.35s, 0.35s, 0.35s, 0.25s`, `timing: cubic-bezier(0.16, 1, 0.3, 1), cubic-bezier(0.16, 1, 0.3, 1), cubic-bezier(0.16, 1, 0.3, 1), ease`).
- **Interactive Control Probe (`accordion`)**: Tested `Are you more expensive than freel...` (diff `3.509`).
- **Route Transition Architecture**: First internal navigation (`/case-studies`) measured as `direct` in `1923ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — ALLER Studio — Product design and developm │
│ ====================================================================== │
│ [ <header.header-in> (954x64px)       | Services · Case Studies · St ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.pt-40> (w=1440px)                             | │
│ | H1: Product design and development studio for Web3, A...           | │
│ | Substrate: #f9fafb | Ink: #121212 | Accent: #0000ff                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.relative>) max-w: 1440px                   | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Technology can be complex. T |  | Complex flows                | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.pt-20>) — Low user trust                   | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.z-42>       ) | https://www.allerstudio.com/         │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--bt)   │
│ ====================================================================== │
│ [ HEADER BAR (<header.header-in>      ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.pt-40>) — 390px Vertical Lead                 | │
│ | H1: Product design and development studio for Web3, A...           | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.relative>) — 1-Col Stack                  | │
│ | [ Item 1: Technology can be complex. The experience should...    ] | │
│ | [ Item 2: Complex flows                                          ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.pt-20>) — 1-Col (Low user trust)            | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.z-42>       ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.header-in> — `www-allerstudio-com`)**:
   - Landmark `<header class="header-in top-4">` (`954x64px`) hosting `ALLER Studio — Product design and de` navigation (`Services · Case Studies · Studio · Insights · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`), and stylesheet rule `.jjo8ZG_className { font-family:Inter,Inter Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.pt-40> — `Product design and development stu`)**:
   - Landmark `<section class="pt-40 relative">` presenting display lead `Product design and development studio for Web3, A...` and copy excerpt *"Lima · 12:17 PM UTC-5"* over `#f9fafb` canvas and `#121212` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `Technology can be complex. The exp`)**:
   - Landmark `<section class="relative px-4">` rendering section `Technology can be complex. The experience should...` with copy *"Not made for the moment."*, asset references (`3206eb66b875a5b3-s.p.3gjg6tthudz5...`, `83afe278b6a6bb3c-s.p.45535valc9rz...`, `a079e02bba5bf7ab-s.p.2yv0x3fl1lx-...`, `a10c617c9026098c-s.p.1a-q6cj6za4e...`), and grid rule `.jjo8ZG_variable { --font-inter:"Inter", "Inter Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.pt-20> — `Complex flows`)**:
   - Landmark `<section class="pt-20 pb-4">` framing `Complex flows` and `Low user trust` (*"Built for what follows."*) with `#f6f7f8` surface cards, `#0000ff` accents, and `.U4jUma_className { font-family:Rajdhani,Rajdhani Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.z-42> — `https://www.allerstudio.com/`)**:
   - Landmark `<footer class="z-42 bg-dark-950">` anchoring `ALLER Studio — Product design an` footer links (`Services · Case Studies · Studio · Insights · Contact`), copy *"Product strategy · UX/UI · Branding · Development"*, and `#dadee2` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `Product design and development studio for Web3, A...` · sticky/fixed elements: `1`
- **Step 02** (`y=850px`, `7%`): Active landmark `Technology can be complex. The experience should...` · sticky/fixed elements: `1`
- **Step 03** (`y=2550px`, `20%`): Active landmark `Web3 Product Design` · sticky/fixed elements: `1`
- **Step 04** (`y=4250px`, `33%`): Active landmark `Turning complex agricultural data into an actiona...` · sticky/fixed elements: `1`
- **Step 05** (`y=6800px`, `52%`): Active landmark `More than a visual layer` · sticky/fixed elements: `1`
- **Step 06** (`y=8500px`, `66%`): Active landmark `Choose the right way to move your product forward...` · sticky/fixed elements: `1`
- **Step 07** (`y=10200px`, `79%`): Active landmark `Build and scale` · sticky/fixed elements: `1`
- **Step 08** (`y=11050px`, `85%`): Active landmark `Read the FAQs Read the FAQs Read the FAQs Read th...` · sticky/fixed elements: `1`

### Multi-Page Internal Route Map
- **Listing Route (`/case-studies`)**: `https://www.allerstudio.com/case-studies` — H1: `We design products that make complexity understan...`, scrollHeight `4063px`, transition `direct` (`1923ms`)
- **Detail Route (`/services/product-design`)**: `https://www.allerstudio.com/services/product-design` — H1: `Product Design for digital products people actual...`, scrollHeight `9907px`, transition `direct` (`2095ms`)
- **About Route (`/studio`)**: `https://www.allerstudio.com/studio` — H1: `An independent studio for teams building somethin...`, scrollHeight `5898px`, transition `direct` (`1283ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-allerstudio-com (ALLER Studio — Product design and development studio)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-allerstudio-com` (**ALLER Studio — Product design and development studio** — `https://www.allerstudio.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f9fafb` / `#0000ff`).
- **Identity & Domain Context**: Product design and development studio for Web3, AI, fintech, and gaming.
- **Primary Substrate**: `#f9fafb` (live computed `html` `background-color` (`computed_styles.json`)), **Primary Ink**: `#121212`, **Accent / Highlight**: `#0000ff`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f9fafb` (live computed `html` `background-color` (`computed_styles.json`)) paired with `#121212` primary typography and `#0000ff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Rajdhani` for display copy (`Product design and development studi`) with `Inter`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: var(--btn-gap)`, padding `var(--btn-px)`) with `cubic-bezier(0,0,.2,1)` easing and Framer Motion Layout Physics, HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-allerstudio-com` in your global stylesheet:

:root {
  /* ALLER Studio — Product design and development studio (www-allerstudio-com) — Live-Grounded CSS Variables */
  --duration-quick: .15s; /* Motion / Easing Token (www-allerstudio-com) */
  --duration-fast: .25s; /* Motion / Easing Token (www-allerstudio-com) */
  --duration-medium: .35s; /* Motion / Easing Token (www-allerstudio-com) */
  --duration-very-slow: .5s; /* Motion / Easing Token (www-allerstudio-com) */
  --ease-smooth-out: cubic-bezier(.22, 1, .36, 1); /* Motion / Easing Token (www-allerstudio-com) */
  --ease-bounce: cubic-bezier(.34, 1.35, .64, 1); /* Motion / Easing Token (www-allerstudio-com) */
  --font-inter: "Inter", "Inter Fallback"; /* Typography / Scale Token (www-allerstudio-com) */
  --font-rajdhani: "Rajdhani", "Rajdhani Fallback"; /* Typography / Scale Token (www-allerstudio-com) */
  --font-sans: var(--font-inter), "Helvetica Neue", Arial, sans-serif; /* Typography / Scale Token (www-allerstudio-com) */
  --color-black: #000; /* Canvas / Surface Token (www-allerstudio-com) */
  --color-white: #fff; /* Canvas / Surface Token (www-allerstudio-com) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (www-allerstudio-com) */
  --text-xs: .75rem; /* Typography Ink Token (www-allerstudio-com) */
  --text-xs--line-height: calc(1 / .75); /* Typography Ink Token (www-allerstudio-com) */
  --text-sm: .875rem; /* Typography Ink Token (www-allerstudio-com) */
  --text-sm--line-height: calc(1.25 / .875); /* Typography Ink Token (www-allerstudio-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f9fafb` — grounded in live computed `html` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#121212` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#f6f7f8` — grounded in `var(--color-surface-bg-2)` in `:root`
- **Interactive Accent / Highlight**: `#0000ff` — grounded in `:text-blue-600 a:hover { color: blue }` (`#0000ff`)
- **Secondary / Muted Copy**: `#787878` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#dadee2` — grounded in `var(--color-border)` in `:root`
- **Variable Token (`--color-black`)**: `#000000` — grounded in `var(--color-black)` in `:root`
- **Variable Token (`--color-white`)**: `#ffffff` — grounded in `var(--color-white)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (live computed `main` `max-width`)
- **Padding & Gutters**: `var(--btn-px)` lateral canvas padding with `var(--btn-gap)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: var(--btn-gap)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--btn-px)` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `3.35544e+07px`, `999px`, `.25rem`, `var(--radius-2xl)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Rajdhani`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 48px`, `line-height: 56px`, `font-weight: 600`); CSS variables `--text-5xl: 3rem`, `--text-5xl--line-height: 1`, `--font-display: var(--font-rajdhani), "Arial Narrow", sans-serif`; rule `h1` (`font-size: var(--text-base)`, `line-height: var(--tw-leading,var(...`)
- **H2 Section Rule**: live computed `h2 (largest visible desktop heading)` (`font-size: 64px`, `line-height: 1.2`, `font-weight: 600`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: var(--text-sm)`, `line-height: var(--tw-leading,var(...`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: var(--text-sm)`, `line-height: var(--tw-leading,var(...`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-allerstudio-com` (`ALLER Studio — Product design and development studio`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header-in> — `www-allerstudio-com`)**:
   - DOM & Selectors: Landmark `<header class="header-in top-4">` (`954x64px`) hosting `ALLER Studio — Product design and de` navigation (`Services · Case Studies · Studio · Insights · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`), and stylesheet rule `.jjo8ZG_className { font-family:Inter,Inter Fallback;font-style:normal }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header-in> — `www-allerstudio-com`)` (`www-allerstudio-com`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)` transitions and links `Services · Case Studies · Studio · Insights · Contact`.
2. **Hero Stage & Focal Lead (<section.pt-40> — `Product design and development stu`)**:
   - DOM & Selectors: Landmark `<section class="pt-40 relative">` presenting display lead `Product design and development studio for Web3, A...` and copy excerpt *"Lima · 12:17 PM UTC-5"* over `#f9fafb` canvas and `#121212` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#f9fafb` background with `#121212` headline `Product design and development studio for Web3, A...`.
3. **Primary Showcase & Content Grid (<section.relative> — `Technology can be complex. The exp`)**:
   - DOM & Selectors: Landmark `<section class="relative px-4">` rendering section `Technology can be complex. The experience should...` with copy *"Not made for the moment."*, asset references (`3206eb66b875a5b3-s.p.3gjg6tthudz5...`, `83afe278b6a6bb3c-s.p.45535valc9rz...`, `a079e02bba5bf7ab-s.p.2yv0x3fl1lx-...`, `a10c617c9026098c-s.p.1a-q6cj6za4e...`), and grid rule `.jjo8ZG_variable { --font-inter:"Inter", "Inter Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.relative> — `Technology can be complex. The exp`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: var(--btn-gap)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--btn-px)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.pt-20> — `Complex flows`)**:
   - DOM & Selectors: Landmark `<section class="pt-20 pb-4">` framing `Complex flows` and `Low user trust` (*"Built for what follows."*) with `#f6f7f8` surface cards, `#0000ff` accents, and `.U4jUma_className { font-family:Rajdhani,Rajdhani Fallback;font-style:normal }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.pt-20> — `Complex flows`)` uses `3.35544e+07px`, `999px`, `.25rem`, `var(--radius-2xl)` radii, `#0000ff` highlights, and assets (3206eb66b875a5b3-s.p.3gjg6tthudz5..., 83afe278b6a6bb3c-s.p.45535valc9rz..., a079e02bba5bf7ab-s.p.2yv0x3fl1lx-...).
5. **Colophon & Global Directory Footer (<footer.z-42> — `https://www.allerstudio.com/`)**:
   - DOM & Selectors: Landmark `<footer class="z-42 bg-dark-950">` anchoring `ALLER Studio — Product design an` footer links (`Services · Case Studies · Studio · Insights · Contact`), copy *"Product strategy · UX/UI · Branding · Development"*, and `#dadee2` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.z-42> — `https://www.allerstudio.com/`)` aligns to `1440px` (live computed `main` `max-width`) with `var(--btn-px)` lateral canvas padding with `var(--btn-gap)` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Lima · 12:17 PM UTC-5"*
- Copy Excerpt 2: *"Not made for the moment."*
- Copy Excerpt 3: *"Built for what follows."*
- Copy Excerpt 4: *"Product strategy · UX/UI · Branding · Development"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`
- **Extracted Stylesheet Rules (`www-allerstudio-com`)**:
- `.jjo8ZG_className { font-family:Inter,Inter Fallback;font-style:normal }`
- `.jjo8ZG_variable { --font-inter:"Inter", "Inter Fallback" }`
- `.U4jUma_className { font-family:Rajdhani,Rajdhani Fallback;font-style:normal }`
- `.U4jUma_variable { --font-rajdhani:"Rajdhani", "Rajdhani Fallback" }`
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `www-allerstudio-com` stylesheet.
- **Selector `layer components`**: `transition: padding .35s var(--ease-out-expo), gap .35s var(--ease-out-exp...` extracted from `www-allerstudio-com` stylesheet.
- **Selector `.btn-dark:before`**: `transition: opacity .35s` extracted from `www-allerstudio-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.header-in>` and `<section.relative>`.
- **Runtime Interaction Engine**: Integrates Framer Motion Layout Physics, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `13857px` across 8 distinct viewport chapters using WebGL/Canvas.
- **Vertical Chapter Sequence**: Product design and developm... (0%) -> Technology can be complex.... (7%) -> Web3 Product Design (20%) -> Turning complex agricultura... (33%) -> More than a visual layer (52%) -> Choose the right way to mov... (66%) -> Build and scale (79%) -> Read the FAQs Read the FAQs... (85%).
- **Hover Micro-Interaction (`primary_cta`)**: Animate `boxShadow` with `0.35s, 0.35s, 0.35s, 0.25s cubic-bezier(0.16, 1, 0.3, 1), cubic-bezier(0.16, 1, 0.3, 1), cubic-bezier(0.16, 1, 0.3, 1), ease`.
- **Multi-Page Routes**: Scaffold internal routes `/case-studies` (listing, direct), `/services/product-design` (detail, direct), `/studio` (about, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-allerstudio-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | Product design and development studio for Web... | `1` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `7%` | Technology can be complex. The experience sho... | `1` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `2550px` | `20%` | Web3 Product Design | `1` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `4250px` | `33%` | Turning complex agricultural data into an act... | `1` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `6800px` | `52%` | More than a visual layer | `1` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `8500px` | `66%` | Choose the right way to move your product for... | `1` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `10200px` | `79%` | Build and scale | `1` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `11050px` | `85%` | Read the FAQs Read the FAQs Read the FAQs Rea... | `1` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | Hero | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `7200px` | `50%` | More than a visual layer | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `14400px` | `100%` | Footer | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `listing` | `https://www.allerstudio.com/case-studies` | We design products that make complexi... | `4063px` | `direct` (`1923ms`) | [subpage-01-case-studies.webp](assets/subpage-01-case-studies.webp) |
| `2` | `detail` | `https://www.allerstudio.com/services/product-design` | Product Design for digital products p... | `9907px` | `direct` (`2095ms`) | [subpage-02-services-product-design.webp](assets/subpage-02-services-product-design.webp) |
| `3` | `about` | `https://www.allerstudio.com/studio` | An independent studio for teams build... | `5898px` | `direct` (`1283ms`) | [subpage-03-studio.webp](assets/subpage-03-studio.webp) |

