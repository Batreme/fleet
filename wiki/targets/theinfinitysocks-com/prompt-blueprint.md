---
title: "UI Prompt Blueprint: theinfinitysocks-com"
date: 2026-11-15
target: "[[overview|theinfinitysocks-com]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#000000`)"
---

# UI Design System & Master Generation Blueprint: theinfinitysocks-com

> **Infinity Socks — Performance Basketball Socks** (https://theinfinitysocks.com/) — Infinity performance basketball socks. Court System™ — four technologies engineered for the hardwood. Tested by professional players. Pro...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Infinity Socks — Performance Basketball Socks** (`https://theinfinitysocks.com/`). Infinity performance basketball socks. Court System™ — four technologies engineered for the hardwood. Tested by professional players. Pro...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#000000`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ffffff` (`var(--cc-color-bg)` in `:root`) paired with `#000000` primary typography and `#000000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `FK Screamer` for display copy (`Cookies`) with `Geist` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `var(--cc-bar-max-width)` container bounds (`gap: var(--cc-space)`, padding `var(--cc-padding)`) with `cubic-bezier(.625,.05,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `var(--cc-bar-max-width)` extracted from `theinfinitysocks-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--cc-padding)` lateral canvas padding with `var(--cc-space)` grid gap.
- **Border Radius Scale**: `var(--cc-radius)`, `var(--cc-radius-btn)`, `var(--cc-radius-switch)`, `var(--btn-radius)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--cc-bar-max-width)`, `gap: var(--cc-space)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--cc-padding)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:40em)`, `@media (prefers-reduced-motion:reduce)`, `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | `var(--cc-color-bg)` in `:root` |
| **Primary Typography Ink** | `#171717` | `var(--cc-color-fg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#6b6b6b` | `var(--cc-color-muted)` in `:root` |
| **Interactive Accent / Highlight** | `#000000` | `var(--cc-color-accent-hover)` in `:root` |
| **Secondary / Muted Copy** | `#2f6acf` | `var(--cc-color-focus)` in `:root` |
| **Structural Hairline Border** | `#706A5E` | `var(--taupe)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cc-font-family` | `inherit` | Typography / Scale Token |
| `--cc-font-family-heading` | `var(--cc-font-family)` | Typography Ink Token |
| `--cc-font-family-mono` | `ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` | Typography / Scale Token |
| `--cc-font-size` | `1em` | Typography / Scale Token |
| `--cc-line-height` | `1.5` | Typography / Scale Token |
| `--cc-title-size` | `1.125em` | Layout / Spatial Grid Token |
| `--cc-title-weight` | `600` | Design System Custom Token |
| `--cc-title-transform` | `none` | Design System Custom Token |
| `--cc-title-spacing` | `0` | Layout / Spatial Grid Token |
| `--cc-text-size` | `.9375em` | Typography Ink Token |
| `--cc-small-size` | `.8125em` | Layout / Spatial Grid Token |
| `--cc-btn-size` | `.9375em` | Layout / Spatial Grid Token |
| `--cc-btn-weight` | `500` | Design System Custom Token |
| `--cc-btn-spacing` | `0` | Layout / Spatial Grid Token |
| `--cc-btn-transform` | `none` | Design System Custom Token |
| `--cc-color-bg` | `#ffffff` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `FK Screamer`.
- **Primary Body Stack**: `Geist`.
- **Technical / Metadata Stack**: `Geist Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25em`, `--display: var(--font-heading)`, `--h1-top: 18.2%`.
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5em`, `--text-3xl: 1.875em`.
- **Body Copy**: CSS variables `--font-body: "Geist", system-ui, sans-serif`, `--text-base: .875em`, `--body: var(--font-body)`.
- **Metadata & Navigation Labels**: CSS variables `--cc-font-family-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace`, `--cc-small-size: .8125em`, `--font-mono: "Geist Mono", ui-monospace, Menlo, monospace`; rule `small` (`font-size: calc(var(--size-font) * .6875)`, `letter-spacing: .26em`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.625,.05,0,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.32,.72,0,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.cc__backdrop`**: `transition: opacity var(--cc-duration) var(--cc-ease)` extracted from `theinfinitysocks-com` stylesheet.
- **Selector `.cc__dialog`**: `transition: opacity var(--cc-duration) var(--cc-ease),transform var(--cc-d...` extracted from `theinfinitysocks-com` stylesheet.
- **Selector `.cc__link`**: `transition: color var(--cc-duration-fast)` extracted from `theinfinitysocks-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.625,.05,0,1)`)**: Governs interactive state transitions across `<header.cc__dialog-head>` and `<section.cc__dialog>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Infinity Socks — Performance Basketball So │
│ ====================================================================== │
│ [ <header.cc__dialog-head> | Cookie Policy                          ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.cc__banner>                                 |   │
│ | H1: Cookies                                                      |   │
│ | Substrate: #ffffff    | Ink: #000000    | Accent: #000000        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.cc__dialog>      ) max-w: var(--cc-bar-m |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Cookie settings              |  | High-Performance Socks High- | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.cc__dialog] -> [<section.cc__banne] -> [<section.cc__dialo] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.cc__dialog-act) | https://theinfinitysocks.com/      │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.cc__dialog-head> — `theinfinitysocks-com`)**:
   - Landmark `<header class="cc__dialog-head">` hosting `Infinity Socks — Performance Basketb` navigation (`Cookie Policy`), DOM attributes (`data-skip`, `data-motion-toggle`, `data-motion-label`, `data-cc-host`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.cc__banner> — `Cookies`)**:
   - Landmark `<section class="cc__banner">` presenting display lead `Cookies` and copy excerpt *"Strictly necessary Needed for the site to work and to remember yo"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.cc__dialog> — `Cookie settings`)**:
   - Landmark `<section class="cc__dialog">` rendering section `Cookie settings` with copy *"Analytics Google Analytics and Microsoft Clarity, to see which pa"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `button { font:inherit;color:inherit;background:none;border:0;margin:0;cursor:poin... }`.
4. **Interactive Detail & Feature Matrix (<section.hero> — `High-Performance Socks High-Perfor`)**:
   - Landmark `<section class="hero hero--h1a">` framing `High-Performance Socks High-Performance Socks Hig...` and `Trusted every possession.` (*"Marketing Google Ads conversion measurement, to see whether our a"*) with `#6b6b6b` surface cards, `#000000` accents, and `.cc__placeholder :focus-visible { outline:2px solid var(--cc-color-focus);outline-offset:2px }`.
5. **Colophon & Global Directory Footer (<footer.cc__dialog-actions> — `https://theinfinitysocks.com/`)**:
   - Landmark `<footer class="cc__dialog-actions cc__actions">` anchoring `Infinity Socks — Performance Bas` footer links (`Cookie Policy`), copy *"High-Performance Socks High-Performance Socks High-Performan"*, and `#706A5E` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: theinfinitysocks-com (Infinity Socks — Performance Basketball Socks)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `theinfinitysocks-com` (**Infinity Socks — Performance Basketball Socks** — `https://theinfinitysocks.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#000000`).
- **Identity & Domain Context**: Infinity performance basketball socks. Court System™ — four technologies engineered for the hardwood. Tested by professional players. Pro...
- **Primary Substrate**: `#ffffff` (`var(--cc-color-bg)` in `:root`), **Primary Ink**: `#000000`, **Accent / Highlight**: `#000000`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ffffff` (`var(--cc-color-bg)` in `:root`) paired with `#000000` primary typography and `#000000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `FK Screamer` for display copy (`Cookies`) with `Geist` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `var(--cc-bar-max-width)` container bounds (`gap: var(--cc-space)`, padding `var(--cc-padding)`) with `cubic-bezier(.625,.05,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `theinfinitysocks-com` in your global stylesheet:

:root {
  /* Infinity Socks — Performance Basketball Socks (theinfinitysocks-com) — Ground-Truth Extracted CSS Variables */
  --cc-font-family: inherit; /* Typography / Scale Token (theinfinitysocks-com) */
  --cc-font-family-heading: var(--cc-font-family); /* Typography Ink Token (theinfinitysocks-com) */
  --cc-font-family-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; /* Typography / Scale Token (theinfinitysocks-com) */
  --cc-font-size: 1em; /* Typography / Scale Token (theinfinitysocks-com) */
  --cc-line-height: 1.5; /* Typography / Scale Token (theinfinitysocks-com) */
  --cc-title-size: 1.125em; /* Layout / Spatial Grid Token (theinfinitysocks-com) */
  --cc-title-weight: 600; /* Design System Custom Token (theinfinitysocks-com) */
  --cc-title-transform: none; /* Design System Custom Token (theinfinitysocks-com) */
  --cc-title-spacing: 0; /* Layout / Spatial Grid Token (theinfinitysocks-com) */
  --cc-text-size: .9375em; /* Typography Ink Token (theinfinitysocks-com) */
  --cc-small-size: .8125em; /* Layout / Spatial Grid Token (theinfinitysocks-com) */
  --cc-btn-size: .9375em; /* Layout / Spatial Grid Token (theinfinitysocks-com) */
  --cc-btn-weight: 500; /* Design System Custom Token (theinfinitysocks-com) */
  --cc-btn-spacing: 0; /* Layout / Spatial Grid Token (theinfinitysocks-com) */
  --cc-btn-transform: none; /* Design System Custom Token (theinfinitysocks-com) */
  --cc-color-bg: #ffffff; /* Canvas / Surface Token (theinfinitysocks-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in `var(--cc-color-bg)` in `:root`
- **Primary Typography Ink**: `#171717` — grounded in `var(--cc-color-fg)` in `:root`
- **Elevated Surface / Card Substrate**: `#6b6b6b` — grounded in `var(--cc-color-muted)` in `:root`
- **Interactive Accent / Highlight**: `#000000` — grounded in `var(--cc-color-accent-hover)` in `:root`
- **Secondary / Muted Copy**: `#2f6acf` — grounded in `var(--cc-color-focus)` in `:root`
- **Structural Hairline Border**: `#706A5E` — grounded in `var(--taupe)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `var(--cc-bar-max-width)` extracted from `theinfinitysocks-com` stylesheet
- **Padding & Gutters**: `var(--cc-padding)` lateral canvas padding with `var(--cc-space)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--cc-bar-max-width)`, `gap: var(--cc-space)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--cc-padding)` horizontal padding
- **Media Queries**: `@media (max-width:40em)`, `@media (prefers-reduced-motion:reduce)`, `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`
- **Corner Radii**: `var(--cc-radius)`, `var(--cc-radius-btn)`, `var(--cc-radius-switch)`, `var(--btn-radius)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `FK Screamer`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **H1 Display Rule**: CSS variables `--text-4xl: 2.25em`, `--display: var(--font-heading)`, `--h1-top: 18.2%`
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5em`, `--text-3xl: 1.875em`
- **Body Copy Rule**: CSS variables `--font-body: "Geist", system-ui, sans-serif`, `--text-base: .875em`, `--body: var(--font-body)`
- **Metadata & Index Rule**: CSS variables `--cc-font-family-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace`, `--cc-small-size: .8125em`, `--font-mono: "Geist Mono", ui-monospace, Menlo, monospace`; rule `small` (`font-size: calc(var(--size-font) * .6875)`, `letter-spacing: .26em`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `theinfinitysocks-com` (`Infinity Socks — Performance Basketball Socks`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.cc__dialog-head> — `theinfinitysocks-com`)**:
   - DOM & Selectors: Landmark `<header class="cc__dialog-head">` hosting `Infinity Socks — Performance Basketb` navigation (`Cookie Policy`), DOM attributes (`data-skip`, `data-motion-toggle`, `data-motion-label`, `data-cc-host`), and stylesheet rule `after { box-sizing:border-box }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.cc__dialog-head> — `theinfinitysocks-com`)` (`theinfinitysocks-com`) adapts across `@media (max-width:40em)`, `@media (prefers-reduced-motion:reduce)`, `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)` with `cubic-bezier(.625,.05,0,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.32,.72,0,1)` transitions and links `Cookie Policy`.
2. **Hero Stage & Focal Lead (<section.cc__banner> — `Cookies`)**:
   - DOM & Selectors: Landmark `<section class="cc__banner">` presenting display lead `Cookies` and copy excerpt *"Strictly necessary Needed for the site to work and to remember yo"* over `#ffffff` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#ffffff` background with `#000000` headline `Cookies`.
3. **Primary Showcase & Content Grid (<section.cc__dialog> — `Cookie settings`)**:
   - DOM & Selectors: Landmark `<section class="cc__dialog">` rendering section `Cookie settings` with copy *"Analytics Google Analytics and Microsoft Clarity, to see which pa"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `button { font:inherit;color:inherit;background:none;border:0;margin:0;cursor:poin... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.cc__dialog> — `Cookie settings`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--cc-bar-max-width)`, `gap: var(--cc-space)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--cc-padding)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.hero> — `High-Performance Socks High-Perfor`)**:
   - DOM & Selectors: Landmark `<section class="hero hero--h1a">` framing `High-Performance Socks High-Performance Socks Hig...` and `Trusted every possession.` (*"Marketing Google Ads conversion measurement, to see whether our a"*) with `#6b6b6b` surface cards, `#000000` accents, and `.cc__placeholder :focus-visible { outline:2px solid var(--cc-color-focus);outline-offset:2px }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.hero> — `High-Performance Socks High-Perfor`)` uses `var(--cc-radius)`, `var(--cc-radius-btn)`, `var(--cc-radius-switch)`, `var(--btn-radius)` radii, `#000000` highlights, and assets (favicon.ico, favicon.svg, apple-touch-icon.png).
5. **Colophon & Global Directory Footer (<footer.cc__dialog-actions> — `https://theinfinitysocks.com/`)**:
   - DOM & Selectors: Landmark `<footer class="cc__dialog-actions cc__actions">` anchoring `Infinity Socks — Performance Bas` footer links (`Cookie Policy`), copy *"High-Performance Socks High-Performance Socks High-Performan"*, and `#706A5E` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.cc__dialog-actions> — `https://theinfinitysocks.com/`)` aligns to `var(--cc-bar-max-width)` extracted from `theinfinitysocks-com` stylesheet with `var(--cc-padding)` lateral canvas padding with `var(--cc-space)` grid gap and attributes (data-skip, data-motion-toggle, data-motion-label).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Strictly necessary Needed for the site to work and to remember your cookie choice...."*
- Copy Excerpt 2: *"Analytics Google Analytics and Microsoft Clarity, to see which pages are visited a..."*
- Copy Excerpt 3: *"Marketing Google Ads conversion measurement, to see whether our ads lead to team r..."*
- Copy Excerpt 4: *"High-Performance Socks High-Performance Socks High-Performance Socks"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.625,.05,0,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.32,.72,0,1)`
- **Extracted Stylesheet Rules (`theinfinitysocks-com`)**:
- `after { box-sizing:border-box }`
- `button { font:inherit;color:inherit;background:none;border:0;margin:0;cursor:poin... }`
- `.cc__placeholder :focus-visible { outline:2px solid var(--cc-color-focus);outline-offset:2px }`
- `.cc__dialog:focus { outline:none }`
- `html.cc-scroll-lock { overflow:hidden!important }`
- **Per-Selector Transition Rules**:
- **Selector `.cc__backdrop`**: `transition: opacity var(--cc-duration) var(--cc-ease)` extracted from `theinfinitysocks-com` stylesheet.
- **Selector `.cc__dialog`**: `transition: opacity var(--cc-duration) var(--cc-ease),transform var(--cc-d...` extracted from `theinfinitysocks-com` stylesheet.
- **Selector `.cc__link`**: `transition: color var(--cc-duration-fast)` extracted from `theinfinitysocks-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.625,.05,0,1)`)**: Governs interactive state transitions across `<header.cc__dialog-head>` and `<section.cc__dialog>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `theinfinitysocks-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
