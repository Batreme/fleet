---
title: "UI Prompt Blueprint: www-mbidirectmail-com"
date: 2026-11-15
target: "[[overview|www-mbidirectmail-com]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#151515` / `#0A0A0C`)"
---

# UI Design System & Master Generation Blueprint: www-mbidirectmail-com

> **Direct Mail & Digital Marketing · Customer Acquisition · MBI** (https://www.mbidirectmail.com/) — MBI Direct Mail + Digital helps businesses find, reach, and win new customers: direct mail, print, digital, and seminar marketing from on...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/www-mbidirectmail-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Direct Mail & Digital Marketing · Customer Acquisition · MBI** (`https://www.mbidirectmail.com/`). MBI Direct Mail + Digital helps businesses find, reach, and win new customers: direct mail, print, digital, and seminar marketing from on...
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#151515` / `#0A0A0C`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#151515` (`var(--ink)` in `:root`) paired with `#F6F8FA` primary typography and `#0A0A0C` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter` for display copy (`A Marketing Partner.`) with `Inter Fallback Mac` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `60ch` container bounds (`gap: 14px`, padding `26px`) with `cubic-bezier(0.2,0.75,0.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-mbidirectmail-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `60ch` extracted from `www-mbidirectmail-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `26px` lateral canvas padding with `14px` grid gap.
- **Border Radius Scale**: `50%`, `1px`, `18px`, `46px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 60ch`, `gap: 14px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `26px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width: 560px)`, `@media (prefers-reduced-motion: reduce)`, `@media (max-width: 440px)`, `@media (max-height: 829px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#151515` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#d71920` | `var(--signal)` in `:root` |
| **Elevated Surface / Card Substrate** | `#06070A` | `var(--dark)` in `:root` |
| **Interactive Accent / Highlight** | `#0A0A0C` | `var(--dark2)` in `:root` |
| **Secondary / Muted Copy** | `#151719` | `var(--foot)` in `:root` |
| **Structural Hairline Border** | `#F6F8FA` | `var(--paper)` in `:root` |
| **Variable Token (`--white`)** | `#FFFFFF` | `var(--white)` in `:root` |
| **Variable Token (`--ink-d`)** | `#F0F0F2` | `var(--ink-d)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#151515` | Typography Ink Token |
| `--signal` | `#d71920` | Color / Atmospheric Token |
| `--rule` | `rgba(21, 21, 21, 0.3)` | Color / Atmospheric Token |
| `--rule-on` | `rgba(21, 21, 21, 0.46)` | Color / Atmospheric Token |
| `--wall` | `rgba(21, 21, 21, 0.13)` | Color / Atmospheric Token |
| `--rail` | `16px` | Dimension / Scale Token |
| `--ctrl` | `40px` | Dimension / Scale Token |
| `--gap` | `14px` | Layout / Spatial Grid Token |
| `--nf-size` | `56px` | Layout / Spatial Grid Token |
| `--nf-blade-l` | `200px` | Dimension / Scale Token |
| `--dark` | `#06070A` | Canvas / Surface Token |
| `--dark2` | `#0A0A0C` | Canvas / Surface Token |
| `--foot` | `#151719` | Color / Atmospheric Token |
| `--paper` | `#F6F8FA` | Canvas / Surface Token |
| `--white` | `#FFFFFF` | Canvas / Surface Token |
| `--ink-d` | `#F0F0F2` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Inter`.
- **Primary Body Stack**: `Inter Fallback Mac`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 22px`, `line-height: 1.25`, `letter-spacing: .05em`, `font-weight: 400`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(38px,11.6vw,48px)`, `line-height: 1.0`, `letter-spacing: -.035em`, `font-weight: 100`).
- **Body Copy**: CSS variables `--body-d: #C9CBD1`, `--body-l: rgba(0, 0, 0, 0.66)`; rule `p` (`font-size: 16px`, `line-height: 1.55`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `17px`, `15px`, `16px`, `18px`, `24px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.2,0.75,0.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.2,.9,.3,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.abt-cell::after`**: `transition: background-color 200ms ease, height 160ms ease` extracted from `www-mbidirectmail-com` stylesheet.
- **Selector `.abt-wall`**: `transition: background-color 200ms ease` extracted from `www-mbidirectmail-com` stylesheet.
- **Selector `.abt-field-name`**: `transition: opacity 200ms ease, transform 260ms cubic-bezier(0.2, 0.75, 0....` extracted from `www-mbidirectmail-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.2,0.75,0.2,1)`)**: Governs interactive state transitions across `<nav.hn-links>` and `<section.skip-link>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Direct Mail & Digital Marketing · Customer │
│ ====================================================================== │
│ [ <nav.hn-links>           | About · Capabilities · All capabilitie ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.solutions-section>                          |   │
│ | H1: A Marketing Partner.                                         |   │
│ | Substrate: #151515    | Ink: #F6F8FA    | Accent: #0A0A0C        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.skip-link>       ) max-w: 60ch           |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | We find the right audience.  |  | One partner. One team. Strat | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 14px  ) | │
│ | [<nav.hn-links>] -> [<section.solutions] -> [<section.skip-link] |   │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.print-signoff>) | https://www.mbidirectmail.com/     │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.hn-links> — `www-mbidirectmail-com`)**:
   - Landmark `<nav class="hn-links">` hosting `Direct Mail & Digital Marketing · Cu` navigation (`About · Capabilities · All capabilities → · Industries · Automotive 6`), DOM attributes (`data-tier="lite:cores2,mem4"`, `data-site-reveal`, `data-v-page-load-overlay="none"`, `data-v-hero-logo="wide"`), and stylesheet rule `.abt-band { margin-top: 28px; }`.
2. **Hero Stage & Focal Lead (<section.solutions-section> — `A Marketing Partner.`)**:
   - Landmark `<section class="solutions-section">` presenting display lead `A Marketing Partner.` and copy excerpt *"8 0 0 - 3 5 9 - 4 7 8 0"* over `#151515` canvas and `#F6F8FA` ink.
3. **Primary Showcase & Content Grid (<section.skip-link> — `We find the right audience. We are`)**:
   - Landmark `<section class="skip-link">` rendering section `We find the right audience. We are experts at kno...` with copy *"All capabilities →"*, asset references (`favicon.svg`, `favicon.ico`, `lenis.min.js`, `d3-array.min.js`), and grid rule `.abt-band-title { color: var(--ink); font-size: 15px; white-space: normal; }`.
4. **Interactive Detail & Feature Matrix (<section.plo-overlay> — `One partner. One team. Strategy to`)**:
   - Landmark `<section class="plo-overlay">` framing `One partner. One team. Strategy to delivery.` and `See what this looks like for your business.` (*"Printing Commercial and variable-data printing, in-house."*) with `#06070A` surface cards, `#0A0A0C` accents, and `.abt-band-rule { flex: 1 1 auto; }`.
5. **Colophon & Global Directory Footer (<footer.print-signoff> — `https://www.mbidirectmail.com/`)**:
   - Landmark `<footer class="print-signoff">` anchoring `Direct Mail & Digital Marketing ` footer links (`About · Capabilities · All capabilities → · Industries · Automotive 6`), copy *"Commercial and variable-data printing, in-house."*, and `#F6F8FA` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-mbidirectmail-com (Direct Mail & Digital Marketing · Customer Acquisition · MBI)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-mbidirectmail-com` (**Direct Mail & Digital Marketing · Customer Acquisition · MBI** — `https://www.mbidirectmail.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#151515` / `#0A0A0C`).
- **Identity & Domain Context**: MBI Direct Mail + Digital helps businesses find, reach, and win new customers: direct mail, print, digital, and seminar marketing from on...
- **Primary Substrate**: `#151515` (`var(--ink)` in `:root`), **Primary Ink**: `#F6F8FA`, **Accent / Highlight**: `#0A0A0C`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#151515` (`var(--ink)` in `:root`) paired with `#F6F8FA` primary typography and `#0A0A0C` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter` for display copy (`A Marketing Partner.`) with `Inter Fallback Mac` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `60ch` container bounds (`gap: 14px`, padding `26px`) with `cubic-bezier(0.2,0.75,0.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-mbidirectmail-com` in your global stylesheet:

:root {
  /* Direct Mail & Digital Marketing · Customer Acquisition · MBI (www-mbidirectmail-com) — Ground-Truth Extracted CSS Variables */
  --ink: #151515; /* Typography Ink Token (www-mbidirectmail-com) */
  --signal: #d71920; /* Color / Atmospheric Token (www-mbidirectmail-com) */
  --rule: rgba(21, 21, 21, 0.3); /* Color / Atmospheric Token (www-mbidirectmail-com) */
  --rule-on: rgba(21, 21, 21, 0.46); /* Color / Atmospheric Token (www-mbidirectmail-com) */
  --wall: rgba(21, 21, 21, 0.13); /* Color / Atmospheric Token (www-mbidirectmail-com) */
  --rail: 16px; /* Dimension / Scale Token (www-mbidirectmail-com) */
  --ctrl: 40px; /* Dimension / Scale Token (www-mbidirectmail-com) */
  --gap: 14px; /* Layout / Spatial Grid Token (www-mbidirectmail-com) */
  --nf-size: 56px; /* Layout / Spatial Grid Token (www-mbidirectmail-com) */
  --nf-blade-l: 200px; /* Dimension / Scale Token (www-mbidirectmail-com) */
  --dark: #06070A; /* Canvas / Surface Token (www-mbidirectmail-com) */
  --dark2: #0A0A0C; /* Canvas / Surface Token (www-mbidirectmail-com) */
  --foot: #151719; /* Color / Atmospheric Token (www-mbidirectmail-com) */
  --paper: #F6F8FA; /* Canvas / Surface Token (www-mbidirectmail-com) */
  --white: #FFFFFF; /* Canvas / Surface Token (www-mbidirectmail-com) */
  --ink-d: #F0F0F2; /* Typography Ink Token (www-mbidirectmail-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#151515` — grounded in `var(--ink)` in `:root`
- **Primary Typography Ink**: `#d71920` — grounded in `var(--signal)` in `:root`
- **Elevated Surface / Card Substrate**: `#06070A` — grounded in `var(--dark)` in `:root`
- **Interactive Accent / Highlight**: `#0A0A0C` — grounded in `var(--dark2)` in `:root`
- **Secondary / Muted Copy**: `#151719` — grounded in `var(--foot)` in `:root`
- **Structural Hairline Border**: `#F6F8FA` — grounded in `var(--paper)` in `:root`
- **Variable Token (`--white`)**: `#FFFFFF` — grounded in `var(--white)` in `:root`
- **Variable Token (`--ink-d`)**: `#F0F0F2` — grounded in `var(--ink-d)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `60ch` extracted from `www-mbidirectmail-com` stylesheet
- **Padding & Gutters**: `26px` lateral canvas padding with `14px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 60ch`, `gap: 14px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `26px` horizontal padding
- **Media Queries**: `@media (max-width: 560px)`, `@media (prefers-reduced-motion: reduce)`, `@media (max-width: 440px)`, `@media (max-height: 829px)`
- **Corner Radii**: `50%`, `1px`, `18px`, `46px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter Fallback Mac`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`font-size: 22px`, `line-height: 1.25`, `letter-spacing: .05em`, `font-weight: 400`)
- **H2 Section Rule**: rule `h2` (`font-size: clamp(38px,11.6vw,48px)`, `line-height: 1.0`, `letter-spacing: -.035em`, `font-weight: 100`)
- **Body Copy Rule**: CSS variables `--body-d: #151515`, `--body-l: rgba(0, 0, 0, 0.66)`; rule `p` (`font-size: 16px`, `line-height: 1.55`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `17px`, `15px`, `16px`, `18px`, `24px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-mbidirectmail-com` (`Direct Mail & Digital Marketing · Customer Acquisition · MBI`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.hn-links> — `www-mbidirectmail-com`)**:
   - DOM & Selectors: Landmark `<nav class="hn-links">` hosting `Direct Mail & Digital Marketing · Cu` navigation (`About · Capabilities · All capabilities → · Industries · Automotive 6`), DOM attributes (`data-tier="lite:cores2,mem4"`, `data-site-reveal`, `data-v-page-load-overlay="none"`, `data-v-hero-logo="wide"`), and stylesheet rule `.abt-band { margin-top: 28px; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.hn-links> — `www-mbidirectmail-com`)` (`www-mbidirectmail-com`) adapts across `@media (max-width: 560px)`, `@media (prefers-reduced-motion: reduce)`, `@media (max-width: 440px)`, `@media (max-height: 829px)` with `cubic-bezier(0.2,0.75,0.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.2,.9,.3,1)` transitions and links `About · Capabilities · All capabilities → · Industries · Automotive 6`.
2. **Hero Stage & Focal Lead (<section.solutions-section> — `A Marketing Partner.`)**:
   - DOM & Selectors: Landmark `<section class="solutions-section">` presenting display lead `A Marketing Partner.` and copy excerpt *"8 0 0 - 3 5 9 - 4 7 8 0"* over `#151515` canvas and `#F6F8FA` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#151515` background with `#F6F8FA` headline `A Marketing Partner.`.
3. **Primary Showcase & Content Grid (<section.skip-link> — `We find the right audience. We are`)**:
   - DOM & Selectors: Landmark `<section class="skip-link">` rendering section `We find the right audience. We are experts at kno...` with copy *"All capabilities →"*, asset references (`favicon.svg`, `favicon.ico`, `lenis.min.js`, `d3-array.min.js`), and grid rule `.abt-band-title { color: var(--ink); font-size: 15px; white-space: normal; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.skip-link> — `We find the right audience. We are`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 60ch`, `gap: 14px`) on desktop and Single-column vertical stack at `390px` viewport width with `26px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.plo-overlay> — `One partner. One team. Strategy to`)**:
   - DOM & Selectors: Landmark `<section class="plo-overlay">` framing `One partner. One team. Strategy to delivery.` and `See what this looks like for your business.` (*"Printing Commercial and variable-data printing, in-house."*) with `#06070A` surface cards, `#0A0A0C` accents, and `.abt-band-rule { flex: 1 1 auto; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.plo-overlay> — `One partner. One team. Strategy to`)` uses `50%`, `1px`, `18px`, `46px` radii, `#0A0A0C` highlights, and assets (favicon.svg, favicon.ico, lenis.min.js).
5. **Colophon & Global Directory Footer (<footer.print-signoff> — `https://www.mbidirectmail.com/`)**:
   - DOM & Selectors: Landmark `<footer class="print-signoff">` anchoring `Direct Mail & Digital Marketing ` footer links (`About · Capabilities · All capabilities → · Industries · Automotive 6`), copy *"Commercial and variable-data printing, in-house."*, and `#F6F8FA` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.print-signoff> — `https://www.mbidirectmail.com/`)` aligns to `60ch` extracted from `www-mbidirectmail-com` stylesheet with `26px` lateral canvas padding with `14px` grid gap and attributes (data-tier="lite:cores2,mem4", data-site-reveal, data-v-page-load-overlay="none").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"8 0 0 - 3 5 9 - 4 7 8 0"*
- Copy Excerpt 2: *"All capabilities →"*
- Copy Excerpt 3: *"Printing Commercial and variable-data printing, in-house."*
- Copy Excerpt 4: *"Commercial and variable-data printing, in-house."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.2,0.75,0.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.2,.9,.3,1)`
- **Extracted Stylesheet Rules (`www-mbidirectmail-com`)**:
- `.abt-band { margin-top: 28px; }`
- `.abt-band-title { color: var(--ink); font-size: 15px; white-space: normal; }`
- `.abt-band-rule { flex: 1 1 auto; }`
- `.abt-row { display: grid; }`
- `.abt-row--who { grid-template-columns: repeat(2, minmax(0, 1fr)); column-gap: var(--gap)... }`
- **Per-Selector Transition Rules**:
- **Selector `.abt-cell::after`**: `transition: background-color 200ms ease, height 160ms ease` extracted from `www-mbidirectmail-com` stylesheet.
- **Selector `.abt-wall`**: `transition: background-color 200ms ease` extracted from `www-mbidirectmail-com` stylesheet.
- **Selector `.abt-field-name`**: `transition: opacity 200ms ease, transform 260ms cubic-bezier(0.2, 0.75, 0....` extracted from `www-mbidirectmail-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.2,0.75,0.2,1)`)**: Governs interactive state transitions across `<nav.hn-links>` and `<section.skip-link>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-mbidirectmail-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
