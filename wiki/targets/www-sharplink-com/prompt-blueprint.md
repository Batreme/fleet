---
title: "UI Prompt Blueprint: www-sharplink-com"
date: 2026-11-15
target: "www-sharplink-com"
status: analyzed
capture: specimen
capture_desktop: specimen
capture_mobile: specimen
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#f3f3f3`)"
---

# UI Design System & Master Generation Blueprint: www-sharplink-com

> **Sharplink : Home** (https://www.sharplink.com/) — Sharplink is the institutional-grade Ethereum treasury platform giving investors a smarter, more productive access vehicle to ETH

![Desktop Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Sharplink : Home** (`https://www.sharplink.com/`). Sharplink is the institutional-grade Ethereum treasury platform giving investors a smarter, more productive access vehicle to ETH
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#f3f3f3`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--black)` in `:root`) paired with `#f7f7f5` primary typography and `#f3f3f3` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Archivo Narrow` for display copy (`Please enable JavaScript`) with `Archivo Narrow Fallback: Arial` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `var(--layout-width)` container bounds (`gap: 16px`, padding `var(--layout-margin)`) with `cubic-bezier(.25,.8,.25,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `var(--layout-width)` extracted from `www-sharplink-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--layout-margin)` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `4px`, `20px`, `0px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--layout-width)`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--layout-margin)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:800px)`, `@media (min-width:1920px)`, `@media (max-width:799px)`, `@media (min-width:800px)and (max-width:1199px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--black)` in `:root` |
| **Primary Typography Ink** | `#676767` | `var(--grey-primary)` in `:root` |
| **Elevated Surface / Card Substrate** | `#a9a9a9` | `var(--grey-secondary)` in `:root` |
| **Interactive Accent / Highlight** | `#f3f3f3` | `var(--off-white)` in `:root` |
| **Secondary / Muted Copy** | `#f7f7f5` | `var(--surface-background)` in `:root` |
| **Structural Hairline Border** | `#0e76ff` | `var(--brand-blue-primary)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--layout-columns-count` | `4` | Layout / Spatial Grid Token |
| `--layout-columns-gap` | `16px` | Layout / Spatial Grid Token |
| `--layout-rows-gap` | `8px` | Layout / Spatial Grid Token |
| `--layout-margin` | `16px` | Layout / Spatial Grid Token |
| `--layout-width` | `calc(100vw - var(--layout-margin)*2)` | Layout / Spatial Grid Token |
| `--pin-color` | `var(--brand-blue-primary)` | Brand / Palette Token |
| `--black` | `#000` | Canvas / Surface Token |
| `--black-0` | `transparent` | Canvas / Surface Token |
| `--black-5` | `rgb(0 0 0/5%)` | Canvas / Surface Token |
| `--black-10` | `rgba(0,0,0,.1)` | Canvas / Surface Token |
| `--black-15` | `rgba(0,0,0,.15)` | Canvas / Surface Token |
| `--black-20` | `rgba(0,0,0,.2)` | Canvas / Surface Token |
| `--black-25` | `rgba(0,0,0,.25)` | Canvas / Surface Token |
| `--black-30` | `rgba(0,0,0,.3)` | Canvas / Surface Token |
| `--black-35` | `rgba(0,0,0,.35)` | Canvas / Surface Token |
| `--black-40` | `rgba(0,0,0,.4)` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Archivo Narrow`.
- **Primary Body Stack**: `Archivo Narrow Fallback: Arial`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `,h1` (`font-size: 88px`, `line-height: .96`, `letter-spacing: -2.64px`).
- **Section Heading (`H2`)**: rule `,h2` (`font-weight: 400`).
- **Body Copy**: rule `p` (`font-size: 16px`, `line-height: 1.35`, `letter-spacing: 0`, `font-weight: 500`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `88px`, `68px`, `52px`, `44px`, `32px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.25,.8,.25,1)`, `cubic-bezier(.47,0,.745,.715)`, `cubic-bezier(.39,.575,.565,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `all-articles .article-card[data-v...`**: `transition: transform .3s ease,box-shadow .3s ease` extracted from `www-sharplink-com` stylesheet.
- **Selector `.all-articles .card-image[data-v-...`**: `transition: transform .8s cubic-bezier(.25,.8,.25,1)` extracted from `www-sharplink-com` stylesheet.
- **Selector `.ui-button>.content[data-v-a133cfe3]`**: `transition: transform .5s var(--ease-in-out-circ) 0s` extracted from `www-sharplink-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.25,.8,.25,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.home-productivity>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Sharplink : Home                           │
│ ====================================================================== │
│ [ <header.site-header>     | Home · About · Investors · Opportunity ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.home-hero>                                  |   │
│ | H1: Please enable JavaScript                                     |   │
│ | Substrate: #000       | Ink: #f7f7f5    | Accent: #f3f3f3        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.home-productivity) max-w: var(--layout-w |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | This website requires JavaSc |  | Ethereum with an Edge        | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px  ) | │
│ | [<header.site-heade] -> [<section.home-hero] -> [<section.home-prod] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>  ) | https://www.sharplink.com/         │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.site-header> — `www-sharplink-com`)**:
   - Landmark `<header class="site-header theme-dark">` hosting `Sharplink : Home` navigation (`Home · About · Investors · Opportunity · News`), DOM attributes (`data-v-00374420`, `data-v-e2147945`, `data-v-9d8fa70e`, `data-v-15fa0cd1`), and stylesheet rule `.body-large { font-size:19px;font-style:normal;line-height:1.35 }`.
2. **Hero Stage & Focal Lead (<section.home-hero> — `Please enable JavaScript`)**:
   - Landmark `<section class="home-hero mobile-only">` presenting display lead `Please enable JavaScript` and copy excerpt *"SharpLink is proudly listed on NASDAQ under the trading symbol SB"* over `#000` canvas and `#f7f7f5` ink.
3. **Primary Showcase & Content Grid (<section.home-productivity> — `This website requires JavaScript i`)**:
   - Landmark `<section class="home-productivity">` rendering section `This website requires JavaScript in order to work...` with copy *"Investors Investors"*, asset references (`entry.097ojG-J.css`, `Content.DYtseY0i.css`, `colors.DCDPWAmH.css`, `Wrapper.CA5eSekD.css`), and grid rule `.body-blog { font-size:16px;font-style:medium;line-height:1.56 }`.
4. **Interactive Detail & Feature Matrix (<section.home-hero> — `Ethereum with an Edge`)**:
   - Landmark `<section class="home-hero wrapped-hero">` framing `Ethereum with an Edge` and `Pioneering Productivity` (*"Opportunity Opportunity"*) with `#a9a9a9` surface cards, `#f3f3f3` accents, and `.mono { font-size:13px;font-weight:500 }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://www.sharplink.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Sharplink : Home` footer links (`Home · About · Investors · Opportunity · News`), copy *"ETH Dashboard ETH Dashboard"*, and `#0e76ff` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-sharplink-com (Sharplink : Home)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-sharplink-com` (**Sharplink : Home** — `https://www.sharplink.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#f3f3f3`).
- **Identity & Domain Context**: Sharplink is the institutional-grade Ethereum treasury platform giving investors a smarter, more productive access vehicle to ETH
- **Primary Substrate**: `#000` (`var(--black)` in `:root`), **Primary Ink**: `#f7f7f5`, **Accent / Highlight**: `#f3f3f3`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--black)` in `:root`) paired with `#f7f7f5` primary typography and `#f3f3f3` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Archivo Narrow` for display copy (`Please enable JavaScript`) with `Archivo Narrow Fallback: Arial` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `var(--layout-width)` container bounds (`gap: 16px`, padding `var(--layout-margin)`) with `cubic-bezier(.25,.8,.25,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-sharplink-com` in your global stylesheet:

:root {
  /* Sharplink : Home (www-sharplink-com) — Ground-Truth Extracted CSS Variables */
  --layout-columns-count: 4; /* Layout / Spatial Grid Token (www-sharplink-com) */
  --layout-columns-gap: 16px; /* Layout / Spatial Grid Token (www-sharplink-com) */
  --layout-rows-gap: 8px; /* Layout / Spatial Grid Token (www-sharplink-com) */
  --layout-margin: 16px; /* Layout / Spatial Grid Token (www-sharplink-com) */
  --layout-width: calc(100vw - var(--layout-margin)*2); /* Layout / Spatial Grid Token (www-sharplink-com) */
  --pin-color: var(--brand-blue-primary); /* Brand / Palette Token (www-sharplink-com) */
  --black: #000; /* Canvas / Surface Token (www-sharplink-com) */
  --black-0: transparent; /* Canvas / Surface Token (www-sharplink-com) */
  --black-5: rgb(0 0 0/5%); /* Canvas / Surface Token (www-sharplink-com) */
  --black-10: rgba(0,0,0,.1); /* Canvas / Surface Token (www-sharplink-com) */
  --black-15: rgba(0,0,0,.15); /* Canvas / Surface Token (www-sharplink-com) */
  --black-20: rgba(0,0,0,.2); /* Canvas / Surface Token (www-sharplink-com) */
  --black-25: rgba(0,0,0,.25); /* Canvas / Surface Token (www-sharplink-com) */
  --black-30: rgba(0,0,0,.3); /* Canvas / Surface Token (www-sharplink-com) */
  --black-35: rgba(0,0,0,.35); /* Canvas / Surface Token (www-sharplink-com) */
  --black-40: rgba(0,0,0,.4); /* Canvas / Surface Token (www-sharplink-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--black)` in `:root`
- **Primary Typography Ink**: `#676767` — grounded in `var(--grey-primary)` in `:root`
- **Elevated Surface / Card Substrate**: `#a9a9a9` — grounded in `var(--grey-secondary)` in `:root`
- **Interactive Accent / Highlight**: `#f3f3f3` — grounded in `var(--off-white)` in `:root`
- **Secondary / Muted Copy**: `#f7f7f5` — grounded in `var(--surface-background)` in `:root`
- **Structural Hairline Border**: `#0e76ff` — grounded in `var(--brand-blue-primary)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `var(--layout-width)` extracted from `www-sharplink-com` stylesheet
- **Padding & Gutters**: `var(--layout-margin)` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--layout-width)`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--layout-margin)` horizontal padding
- **Media Queries**: `@media (min-width:800px)`, `@media (min-width:1920px)`, `@media (max-width:799px)`, `@media (min-width:800px)and (max-width:1199px)`
- **Corner Radii**: `4px`, `20px`, `0px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Archivo Narrow`
- **Body Font Stack**: `Archivo Narrow Fallback: Arial`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `,h1` (`font-size: 88px`, `line-height: .96`, `letter-spacing: -2.64px`)
- **H2 Section Rule**: rule `,h2` (`font-weight: 400`)
- **Body Copy Rule**: rule `p` (`font-size: 16px`, `line-height: 1.35`, `letter-spacing: 0`, `font-weight: 500`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `88px`, `68px`, `52px`, `44px`, `32px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-sharplink-com` (`Sharplink : Home`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.site-header> — `www-sharplink-com`)**:
   - DOM & Selectors: Landmark `<header class="site-header theme-dark">` hosting `Sharplink : Home` navigation (`Home · About · Investors · Opportunity · News`), DOM attributes (`data-v-00374420`, `data-v-e2147945`, `data-v-9d8fa70e`, `data-v-15fa0cd1`), and stylesheet rule `.body-large { font-size:19px;font-style:normal;line-height:1.35 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.site-header> — `www-sharplink-com`)` (`www-sharplink-com`) adapts across `@media (min-width:800px)`, `@media (min-width:1920px)`, `@media (max-width:799px)`, `@media (min-width:800px)and (max-width:1199px)` with `cubic-bezier(.25,.8,.25,1)`, `cubic-bezier(.47,0,.745,.715)`, `cubic-bezier(.39,.575,.565,1)` transitions and links `Home · About · Investors · Opportunity · News`.
2. **Hero Stage & Focal Lead (<section.home-hero> — `Please enable JavaScript`)**:
   - DOM & Selectors: Landmark `<section class="home-hero mobile-only">` presenting display lead `Please enable JavaScript` and copy excerpt *"SharpLink is proudly listed on NASDAQ under the trading symbol SB"* over `#000` canvas and `#f7f7f5` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#000` background with `#f7f7f5` headline `Please enable JavaScript`.
3. **Primary Showcase & Content Grid (<section.home-productivity> — `This website requires JavaScript i`)**:
   - DOM & Selectors: Landmark `<section class="home-productivity">` rendering section `This website requires JavaScript in order to work...` with copy *"Investors Investors"*, asset references (`entry.097ojG-J.css`, `Content.DYtseY0i.css`, `colors.DCDPWAmH.css`, `Wrapper.CA5eSekD.css`), and grid rule `.body-blog { font-size:16px;font-style:medium;line-height:1.56 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.home-productivity> — `This website requires JavaScript i`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--layout-width)`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--layout-margin)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.home-hero> — `Ethereum with an Edge`)**:
   - DOM & Selectors: Landmark `<section class="home-hero wrapped-hero">` framing `Ethereum with an Edge` and `Pioneering Productivity` (*"Opportunity Opportunity"*) with `#a9a9a9` surface cards, `#f3f3f3` accents, and `.mono { font-size:13px;font-weight:500 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.home-hero> — `Ethereum with an Edge`)` uses `4px`, `20px`, `0px` radii, `#f3f3f3` highlights, and assets (entry.097ojG-J.css, Content.DYtseY0i.css, colors.DCDPWAmH.css).
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://www.sharplink.com/`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer">` anchoring `Sharplink : Home` footer links (`Home · About · Investors · Opportunity · News`), copy *"ETH Dashboard ETH Dashboard"*, and `#0e76ff` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-footer> — `https://www.sharplink.com/`)` aligns to `var(--layout-width)` extracted from `www-sharplink-com` stylesheet with `var(--layout-margin)` lateral canvas padding with `16px` grid gap and attributes (data-v-00374420, data-v-e2147945, data-v-9d8fa70e).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"SharpLink is proudly listed on NASDAQ under the trading symbol SBET"*
- Copy Excerpt 2: *"Investors Investors"*
- Copy Excerpt 3: *"Opportunity Opportunity"*
- Copy Excerpt 4: *"ETH Dashboard ETH Dashboard"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.25,.8,.25,1)`, `cubic-bezier(.47,0,.745,.715)`, `cubic-bezier(.39,.575,.565,1)`
- **Extracted Stylesheet Rules (`www-sharplink-com`)**:
- `.body-large { font-size:19px;font-style:normal;line-height:1.35 }`
- `.body-blog { font-size:16px;font-style:medium;line-height:1.56 }`
- `.mono { font-size:13px;font-weight:500 }`
- `.mono-small { font-size:12px;font-weight:400 }`
- `root { --layout-columns-count:12;--layout-columns-gap:28px;--layout-rows-gap:8p... }`
- **Per-Selector Transition Rules**:
- **Selector `all-articles .article-card[data-v...`**: `transition: transform .3s ease,box-shadow .3s ease` extracted from `www-sharplink-com` stylesheet.
- **Selector `.all-articles .card-image[data-v-...`**: `transition: transform .8s cubic-bezier(.25,.8,.25,1)` extracted from `www-sharplink-com` stylesheet.
- **Selector `.ui-button>.content[data-v-a133cfe3]`**: `transition: transform .5s var(--ease-in-out-circ) 0s` extracted from `www-sharplink-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.25,.8,.25,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.home-productivity>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-sharplink-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
