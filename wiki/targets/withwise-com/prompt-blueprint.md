---
title: "UI Prompt Blueprint: withwise-com"
date: 2026-11-15
target: "[[overview|withwise-com]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#1B1B1B` canvas, `#FFFDF1` ink, `#D3C0A0` accent)"
---

# UI Design System & Master Generation Blueprint: withwise-com

> **Compliance-First Onboarding Software · Wise** (https://withwise.com/) — Wise is built for self-employed workforces. We protect you from compliance risks, help you onboard users digitally, and pay them securely.

![Desktop Viewport Capture (1440x14756)](file:///root/projects/fleet/wiki/targets/withwise-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Compliance-First Onboarding Software · Wise** (`https://withwise.com/`). Wise is built for self-employed workforces. We protect you from compliance risks, help you onboard users digitally, and pay them securely.
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#1B1B1B` canvas, `#FFFDF1` ink, `#D3C0A0` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#1B1B1B` (`var(--gf-color-primary)` in `:root`) paired with `#FFFDF1` primary typography and `#D3C0A0` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Open Sans` for display copy (`Compliance-First Onboarding software`) with `Figtree` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `400px` container bounds (`gap: 8px`, padding `44px`) with `cubic-bezier(0.47,0,0.74,0.71)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/withwise-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×14756px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `400px` extracted from `withwise-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `44px` lateral canvas padding with `8px` grid gap.
- **Border Radius Scale**: `50%`, `3px`, `10px`, `8px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 400px`, `gap: 8px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `44px` horizontal padding.
- **Extracted CSS Media Queries**: `@media all and (max-height: 576px)`, `@media all and (max-width: 576px)`, `@media print,screen and (max-width: 64.06125em)`, `@media print,screen and (min-width: 64.0625em)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#1B1B1B` | `var(--gf-color-primary)` in `:root` |
| **Primary Typography Ink** | `#FFFDF1` | `var(--gf-ctrl-bg-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#cc4b37` | `var(--gf-ctrl-border-color-error)` in `:root` |
| **Interactive Accent / Highlight** | `#D3C0A0` | `var(--gf-ctrl-border-color)` in `:root` |
| **Secondary / Muted Copy** | `#D81E5B` | `var(--gf-ctrl-btn-bg-color-primary)` in `:root` |
| **Structural Hairline Border** | `#C51B53` | `var(--gf-ctrl-btn-bg-color-hover-primary)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--input-fz` | `1rem` | Dimension / Scale Token |
| `--input-lh` | `1.5` | Design System Custom Token |
| `--input-pt` | `0.6875rem` | Dimension / Scale Token |
| `--input-pb` | `0.6875rem` | Dimension / Scale Token |
| `--input-pl` | `1rem` | Dimension / Scale Token |
| `--input-pr` | `1rem` | Dimension / Scale Token |
| `--input-bd` | `1px` | Dimension / Scale Token |
| `--grid-col-gap` | `2.5rem` | Layout / Spatial Grid Token |
| `--section-width` | `77.5rem` | Layout / Spatial Grid Token |
| `--section-horizontal-padding` | `calc(var(--grid-col-gap, 2rem) * 0.5)` | Layout / Spatial Grid Token |
| `--gf-form-gap-x` | `2rem` | Layout / Spatial Grid Token |
| `--gf-form-gap-y` | `1.5rem` | Layout / Spatial Grid Token |
| `--gf-field-gap-x` | `var(--gf-form-gap-x)` | Layout / Spatial Grid Token |
| `--gf-field-gap-y` | `var(--gf-form-gap-y)` | Layout / Spatial Grid Token |
| `--gf-color-primary` | `#1B1B1B !important` | Brand / Palette Token |
| `--gf-field-list-btn-size` | `1.25rem` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Open Sans`.
- **Primary Body Stack**: `Figtree`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--gf-field-pwd-str-ind-display: inline-block`, `--gf-local-display: block`; rule `h1` (`font-size: 35px`, `font-weight: 700`).
- **Section Heading (`H2`)**: rule `,.h2` (`font-size: 1.8125rem`, `line-height: 1.4`).
- **Body Copy**: rule `p` (`font-size: 16px`, `line-height: 20px`).
- **Metadata & Navigation Labels**: CSS variables `--gf-ctrl-label-font-size-primary: inherit`, `--gf-ctrl-label-font-size-secondary: inherit`, `--gf-ctrl-label-font-size-tertiary: inherit`; rule `small` (`line-height: 0`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.47,0,0.74,0.71)`, `cubic-bezier(0.22,0.61,0.36,1)`, `cubic-bezier(0.5,0,0.14,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.slick-dots li button::before`**: `transition: all .3s ease` extracted from `withwise-com` stylesheet.
- **Selector `.fancybox-bg`**: `transition: inherit` extracted from `withwise-com` stylesheet.
- **Selector `.fancybox-is-open .fancybox-bg`**: `transition: cubic-bezier(0.47,0,0.74,0.71)` extracted from `withwise-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.47,0,0.74,0.71)`)**: Governs interactive state transitions across `<header.header>` and `<section.flx-section>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Compliance-First Onboarding Software · Wis │
│ ====================================================================== │
│ [ <header.header>          | Request a callback · Platform · See ar ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.flx-section>                                |   │
│ | H1: Compliance-First Onboarding software                         |   │
│ | Substrate: #1B1B1B    | Ink: #FFFDF1    | Accent: #D3C0A0        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.flx-section>     ) max-w: 400px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Stay compliant . Pay on time |  | Why It Matters               | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 8px   ) | │
│ | [<header.header>] -> [<section.flx-secti] -> [<section.flx-secti] |  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>       ) | https://withwise.com/              │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.header> — `withwise-com`)**:
   - Landmark `<header class="header">` hosting `Compliance-First Onboarding Software` navigation (`Request a callback · Platform · See article · Industries`), DOM attributes (`data-scroll-dir-x="0"`, `data-scroll-dir-y="0"`, `data-loader="hs-scriptloader"`, `data-hsjs-portal="145539501"`), and stylesheet rule `.slick-list { position:relative;display:block;overflow:hidden;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.flx-section> — `Compliance-First Onboarding softwa`)**:
   - Landmark `<section class="flx-section flx-masthead-1">` presenting display lead `Compliance-First Onboarding software` and copy excerpt *"We value your privacy"* over `#1B1B1B` canvas and `#FFFDF1` ink.
3. **Primary Showcase & Content Grid (<section.flx-section> — `Stay compliant . Pay on time . Gro`)**:
   - Landmark `<section class="flx-section bg-type-dark">` rendering section `Stay compliant . Pay on time . Grow without the r...` with copy *"We use cookies to enhance your browsing experience, serve persona"*, asset references (`web-interactives-embed.js`, `banner.js`, `145539501.js`, `collectedforms.js`), and grid rule `.slick-list:focus { outline:none }`.
4. **Interactive Detail & Feature Matrix (<section.flx-section> — `Why It Matters`)**:
   - Landmark `<section class="flx-section bg-type-dark">` framing `Why It Matters` and `Compliance is a behaviour, not a document.` (*"Customise Consent Preferences"*) with `#cc4b37` surface cards, `#D3C0A0` accents, and `.slick-list.dragging { cursor:pointer;cursor:hand }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://withwise.com/`)**:
   - Landmark `<footer class="footer">` anchoring `Compliance-First Onboarding Soft` footer links (`Request a callback · Platform · See article · Industries`), copy *"We use cookies to help you navigate efficiently and perform "*, and `#C51B53` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: withwise-com (Compliance-First Onboarding Software · Wise)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `withwise-com` (**Compliance-First Onboarding Software · Wise** — `https://withwise.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#1B1B1B` canvas, `#FFFDF1` ink, `#D3C0A0` accent).
- **Identity & Domain Context**: Wise is built for self-employed workforces. We protect you from compliance risks, help you onboard users digitally, and pay them securely.
- **Primary Substrate**: `#1B1B1B` (`var(--gf-color-primary)` in `:root`), **Primary Ink**: `#FFFDF1`, **Accent / Highlight**: `#D3C0A0`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#1B1B1B` (`var(--gf-color-primary)` in `:root`) paired with `#FFFDF1` primary typography and `#D3C0A0` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Open Sans` for display copy (`Compliance-First Onboarding software`) with `Figtree` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `400px` container bounds (`gap: 8px`, padding `44px`) with `cubic-bezier(0.47,0,0.74,0.71)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `withwise-com` in your global stylesheet:

:root {
  /* Compliance-First Onboarding Software · Wise (withwise-com) — Ground-Truth Extracted CSS Variables */
  --input-fz: 1rem; /* Dimension / Scale Token (withwise-com) */
  --input-lh: 1.5; /* Design System Custom Token (withwise-com) */
  --input-pt: 0.6875rem; /* Dimension / Scale Token (withwise-com) */
  --input-pb: 0.6875rem; /* Dimension / Scale Token (withwise-com) */
  --input-pl: 1rem; /* Dimension / Scale Token (withwise-com) */
  --input-pr: 1rem; /* Dimension / Scale Token (withwise-com) */
  --input-bd: 1px; /* Dimension / Scale Token (withwise-com) */
  --grid-col-gap: 2.5rem; /* Layout / Spatial Grid Token (withwise-com) */
  --section-width: 77.5rem; /* Layout / Spatial Grid Token (withwise-com) */
  --section-horizontal-padding: calc(var(--grid-col-gap, 2rem) * 0.5); /* Layout / Spatial Grid Token (withwise-com) */
  --gf-form-gap-x: 2rem; /* Layout / Spatial Grid Token (withwise-com) */
  --gf-form-gap-y: 1.5rem; /* Layout / Spatial Grid Token (withwise-com) */
  --gf-field-gap-x: var(--gf-form-gap-x); /* Layout / Spatial Grid Token (withwise-com) */
  --gf-field-gap-y: var(--gf-form-gap-y); /* Layout / Spatial Grid Token (withwise-com) */
  --gf-color-primary: #1B1B1B !important; /* Brand / Palette Token (withwise-com) */
  --gf-field-list-btn-size: 1.25rem; /* Layout / Spatial Grid Token (withwise-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#1B1B1B` — grounded in `var(--gf-color-primary)` in `:root`
- **Primary Typography Ink**: `#FFFDF1` — grounded in `var(--gf-ctrl-bg-color)` in `:root`
- **Elevated Surface / Card Substrate**: `#cc4b37` — grounded in `var(--gf-ctrl-border-color-error)` in `:root`
- **Interactive Accent / Highlight**: `#D3C0A0` — grounded in `var(--gf-ctrl-border-color)` in `:root`
- **Secondary / Muted Copy**: `#D81E5B` — grounded in `var(--gf-ctrl-btn-bg-color-primary)` in `:root`
- **Structural Hairline Border**: `#C51B53` — grounded in `var(--gf-ctrl-btn-bg-color-hover-primary)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×14756px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `400px` extracted from `withwise-com` stylesheet
- **Padding & Gutters**: `44px` lateral canvas padding with `8px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 400px`, `gap: 8px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `44px` horizontal padding
- **Media Queries**: `@media all and (max-height: 576px)`, `@media all and (max-width: 576px)`, `@media print,screen and (max-width: 64.06125em)`, `@media print,screen and (min-width: 64.0625em)`
- **Corner Radii**: `50%`, `3px`, `10px`, `8px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Open Sans`
- **Body Font Stack**: `Figtree`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--gf-field-pwd-str-ind-display: inline-block`, `--gf-local-display: block`; rule `h1` (`font-size: 35px`, `font-weight: 700`)
- **H2 Section Rule**: rule `,.h2` (`font-size: 1.8125rem`, `line-height: 1.4`)
- **Body Copy Rule**: rule `p` (`font-size: 16px`, `line-height: 20px`)
- **Metadata & Index Rule**: CSS variables `--gf-ctrl-label-font-size-primary: inherit`, `--gf-ctrl-label-font-size-secondary: inherit`, `--gf-ctrl-label-font-size-tertiary: inherit`; rule `small` (`line-height: 0`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `withwise-com` (`Compliance-First Onboarding Software · Wise`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header> — `withwise-com`)**:
   - DOM & Selectors: Landmark `<header class="header">` hosting `Compliance-First Onboarding Software` navigation (`Request a callback · Platform · See article · Industries`), DOM attributes (`data-scroll-dir-x="0"`, `data-scroll-dir-y="0"`, `data-loader="hs-scriptloader"`, `data-hsjs-portal="145539501"`), and stylesheet rule `.slick-list { position:relative;display:block;overflow:hidden;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header> — `withwise-com`)` (`withwise-com`) adapts across `@media all and (max-height: 576px)`, `@media all and (max-width: 576px)`, `@media print,screen and (max-width: 64.06125em)`, `@media print,screen and (min-width: 64.0625em)` with `cubic-bezier(0.47,0,0.74,0.71)`, `cubic-bezier(0.22,0.61,0.36,1)`, `cubic-bezier(0.5,0,0.14,1)` transitions and links `Request a callback · Platform · See article · Industries`.
2. **Hero Stage & Focal Lead (<section.flx-section> — `Compliance-First Onboarding softwa`)**:
   - DOM & Selectors: Landmark `<section class="flx-section flx-masthead-1">` presenting display lead `Compliance-First Onboarding software` and copy excerpt *"We value your privacy"* over `#1B1B1B` canvas and `#FFFDF1` ink.
   - Responsive Contract: Hero stage (`1440×14756px` desktop / `390×2400px` mobile) sets `#1B1B1B` background with `#FFFDF1` headline `Compliance-First Onboarding software`.
3. **Primary Showcase & Content Grid (<section.flx-section> — `Stay compliant . Pay on time . Gro`)**:
   - DOM & Selectors: Landmark `<section class="flx-section bg-type-dark">` rendering section `Stay compliant . Pay on time . Grow without the r...` with copy *"We use cookies to enhance your browsing experience, serve persona"*, asset references (`web-interactives-embed.js`, `banner.js`, `145539501.js`, `collectedforms.js`), and grid rule `.slick-list:focus { outline:none }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.flx-section> — `Stay compliant . Pay on time . Gro`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 400px`, `gap: 8px`) on desktop and Single-column vertical stack at `390px` viewport width with `44px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.flx-section> — `Why It Matters`)**:
   - DOM & Selectors: Landmark `<section class="flx-section bg-type-dark">` framing `Why It Matters` and `Compliance is a behaviour, not a document.` (*"Customise Consent Preferences"*) with `#cc4b37` surface cards, `#D3C0A0` accents, and `.slick-list.dragging { cursor:pointer;cursor:hand }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.flx-section> — `Why It Matters`)` uses `50%`, `3px`, `10px`, `8px` radii, `#D3C0A0` highlights, and assets (web-interactives-embed.js, banner.js, 145539501.js).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://withwise.com/`)**:
   - DOM & Selectors: Landmark `<footer class="footer">` anchoring `Compliance-First Onboarding Soft` footer links (`Request a callback · Platform · See article · Industries`), copy *"We use cookies to help you navigate efficiently and perform "*, and `#C51B53` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://withwise.com/`)` aligns to `400px` extracted from `withwise-com` stylesheet with `44px` lateral canvas padding with `8px` grid gap and attributes (data-scroll-dir-x="0", data-scroll-dir-y="0", data-loader="hs-scriptloader").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"We value your privacy"*
- Copy Excerpt 2: *"We use cookies to enhance your browsing experience, serve personalised ads or cont..."*
- Copy Excerpt 3: *"Customise Consent Preferences"*
- Copy Excerpt 4: *"We use cookies to help you navigate efficiently and perform certain functions. You..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.47,0,0.74,0.71)`, `cubic-bezier(0.22,0.61,0.36,1)`, `cubic-bezier(0.5,0,0.14,1)`
- **Extracted Stylesheet Rules (`withwise-com`)**:
- `.slick-list { position:relative;display:block;overflow:hidden;margin:0;padding:0 }`
- `.slick-list:focus { outline:none }`
- `.slick-list.dragging { cursor:pointer;cursor:hand }`
- `.slick-track { position:relative;top:0;left:0;display:block;margin-right:auto;margin-le... }`
- `.slick-track::after { content:"";display:table }`
- **Per-Selector Transition Rules**:
- **Selector `.slick-dots li button::before`**: `transition: all .3s ease` extracted from `withwise-com` stylesheet.
- **Selector `.fancybox-bg`**: `transition: inherit` extracted from `withwise-com` stylesheet.
- **Selector `.fancybox-is-open .fancybox-bg`**: `transition: cubic-bezier(0.47,0,0.74,0.71)` extracted from `withwise-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.47,0,0.74,0.71)`)**: Governs interactive state transitions across `<header.header>` and `<section.flx-section>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `withwise-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
