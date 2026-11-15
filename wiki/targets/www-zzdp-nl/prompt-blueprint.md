---
title: "UI Prompt Blueprint: www-zzdp-nl"
date: 2026-11-15
target: "[[overview|www-zzdp-nl]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#8746e3` ink, `#c7c6be` accent)"
---

# UI Design System & Master Generation Blueprint: www-zzdp-nl

> **Al meer dan 70 jaar betekenisvolle architectuur · ZZDP** (https://www.zzdp.nl/) — Bij ZZDP combineren we vakmanschap en visie in betekenisvolle architectuur. Met meer dan 70 jaar ervaring realiseren we ontwerpen waarin...

![Desktop Viewport Capture (1440x18562)](file:///root/projects/fleet/wiki/targets/www-zzdp-nl/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Al meer dan 70 jaar betekenisvolle architectuur · ZZDP** (`https://www.zzdp.nl/`). Bij ZZDP combineren we vakmanschap en visie in betekenisvolle architectuur. Met meer dan 70 jaar ervaring realiseren we ontwerpen waarin...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#8746e3` ink, `#c7c6be` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--background-color)` in `:root`) paired with `#8746e3` primary typography and `#c7c6be` accents.
  - **Extracted Typographic Hierarchy**: Pairs `helveticaNowDisplay` for display copy (`ZZDP`) with `helveticaNowDisplay Fallback` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `0%` container bounds (`gap: 1px`, padding `.6vw`) with `cubic-bezier(.48,0,.03,1)` easing and Lenis Smooth Scroll (`data-lenis`), Lottie Vector Animation Player.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-zzdp-nl/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×18562px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `0%` extracted from `www-zzdp-nl` stylesheet.
- **Canvas Lateral Padding & Spacing**: `.6vw` lateral canvas padding with `1px` grid gap.
- **Border Radius Scale**: `10px`, `8px`, `50%`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 0%`, `gap: 1px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.6vw` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:47.99em)`, `@media (min-width:48em)`, `@media (min-width:0)`, `@media (min-width:23.4375em)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--background-color)` in `:root` |
| **Primary Typography Ink** | `#656657` | `var(--title-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#8746e3` | `var(--accent-color)` in `:root` |
| **Interactive Accent / Highlight** | `#c7c6be` | `var(--primary-ui-label-disabled-color)` in `:root` |
| **Secondary / Muted Copy** | `#b5b899` | `var(--primary-ui-background-hover-color)` in `:root` |
| **Structural Hairline Border** | `#ebeae1` | `var(--primary-ui-background-disabled-color)` in `:root` |
| **Variable Token (`--line-color`)** | `#1a163019` | `var(--line-color)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background-color` | `#fff` | Canvas / Surface Token |
| `--title-color` | `#656657` | Brand / Palette Token |
| `--subtitle-color` | `#656657` | Brand / Palette Token |
| `--body-color` | `#656657` | Typography Ink Token |
| `--line-color` | `#1a163019` | Brand / Palette Token |
| `--accent-color` | `#8746e3` | Brand / Palette Token |
| `--primary-ui-label-default-color` | `#fff` | Brand / Palette Token |
| `--primary-ui-label-hover-color` | `#fff` | Brand / Palette Token |
| `--primary-ui-label-disabled-color` | `#c7c6be` | Brand / Palette Token |
| `--primary-ui-background-default-color` | `#656657` | Canvas / Surface Token |
| `--primary-ui-background-hover-color` | `#b5b899` | Canvas / Surface Token |
| `--primary-ui-background-disabled-color` | `#ebeae1` | Canvas / Surface Token |
| `--primary-ui-stroke-default-color` | `#656657` | Brand / Palette Token |
| `--primary-ui-stroke-hover-color` | `#b5b899` | Brand / Palette Token |
| `--primary-ui-stroke-disabled-color` | `#ebeae1` | Brand / Palette Token |
| `--secondary-ui-label-default-color` | `#656657` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `helveticaNowDisplay`.
- **Primary Body Stack**: `helveticaNowDisplay Fallback`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--font-helvetica-now-display: "helveticaNowDisplay", "helveticaNowDisplay Fallback"`; rule `h1` (`font-size: 13.3333vw`, `line-height: 82%`, `letter-spacing: -.07em`, `font-weight: 400`).
- **Section Heading (`H2`)**: CSS variables `--subtitle-color: #656657`; rule `h2` (`font-size: 8vw`, `line-height: 105%`, `letter-spacing: .01em`, `font-weight: 400`).
- **Body Copy**: CSS variables `--body-color: #656657`; rule `p` (`font-size: 3.73333vw`, `line-height: 132%`, `letter-spacing: 0`, `font-weight: 400`).
- **Metadata & Navigation Labels**: CSS variables `--primary-ui-label-default-color: #fff`, `--primary-ui-label-hover-color: #fff`, `--primary-ui-label-disabled-color: #c7c6be`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.48,0,.03,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.6,.2,0,.8)`.

### Per-Element Transition & Choreography Rules
- **Selector `.c-scrollbar`**: `transition: transform .3s,opacity .3s` extracted from `www-zzdp-nl` stylesheet.
- **Selector `.u-underline-link:after`**: `transition: transform .3s cubic-bezier(.48,0,.03,1)` extracted from `www-zzdp-nl` stylesheet.
- **Selector `scss-module__shXJnq__u-underline-...`**: `transition: transform .3s cubic-bezier(.48,0,.03,1)` extracted from `www-zzdp-nl` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.48,0,.03,1)`)**: Governs interactive state transitions across `<nav.lenis>` and `<section.vjs-styles-dimensions>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Al meer dan 70 jaar betekenisvolle archite │
│ ====================================================================== │
│ [ <nav.lenis>              | Home · Projecten · Over ons · Nieuws e ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.theme--mossLight>                           |   │
│ | H1: ZZDP                                                         |   │
│ | Substrate: #fff       | Ink: #8746e3    | Accent: #c7c6be        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.vjs-styles-dimens) max-w: 0%             |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Bij ZZDP geloven wij dat arc |  | Ons Werk                     | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 1px   ) | │
│ | [<nav.lenis>] -> [<section.theme--mo] -> [<section.vjs-style] |      │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.theme--white> ) | https://www.zzdp.nl/               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.lenis> — `www-zzdp-nl`)**:
   - Landmark `<nav class="lenis">` hosting `Al meer dan 70 jaar betekenisvolle a` navigation (`Home · Projecten · Over ons · Nieuws en inzichten · Vacatures`), DOM attributes (`data-next-head`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`), and stylesheet rule `.u-underline-link:after { height:.266667vw }`.
2. **Hero Stage & Focal Lead (<section.theme--mossLight> — `ZZDP`)**:
   - Landmark `<section class="theme--mossLight">` presenting display lead `ZZDP` and copy excerpt *"Deze website gebruikt essentiële cookies voor functionaliteit en "* over `#fff` canvas and `#8746e3` ink.
3. **Primary Showcase & Content Grid (<section.vjs-styles-dimensions> — `Bij ZZDP geloven wij dat architect`)**:
   - Landmark `<section class="vjs-styles-dimensions">` rendering section `Bij ZZDP geloven wij dat architectuur meer is dan...` with copy *"Accepteren Accepteren"*, asset references (`favicon.svg`, `HelveticaNowDisplay_Regular-s.p.1...`, `HelveticaNowDisplay_Md-s.p.16ns3u...`, `PPNeueMachina_PlainRegular-s.p.39...`), and grid rule `.default-in-animation { transform:translateY(26.6667vw) }`.
4. **Interactive Detail & Feature Matrix (<section.theme--white> — `Ons Werk`)**:
   - Landmark `<section class="theme--white">` framing `Ons Werk` and `Nieuws` (*"Instellingen Instellingen"*) with `#8746e3` surface cards, `#c7c6be` accents, and `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;line-height:1.15 }`.
5. **Colophon & Global Directory Footer (<footer.theme--white> — `https://www.zzdp.nl/`)**:
   - Landmark `<footer class="theme--white">` anchoring `Al meer dan 70 jaar betekenisvol` footer links (`Home · Projecten · Over ons · Nieuws en inzichten · Vacatures`), copy *"Nieuws en inzichten"*, and `#ebeae1` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-zzdp-nl (Al meer dan 70 jaar betekenisvolle architectuur · ZZDP)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-zzdp-nl` (**Al meer dan 70 jaar betekenisvolle architectuur · ZZDP** — `https://www.zzdp.nl/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#8746e3` ink, `#c7c6be` accent).
- **Identity & Domain Context**: Bij ZZDP combineren we vakmanschap en visie in betekenisvolle architectuur. Met meer dan 70 jaar ervaring realiseren we ontwerpen waarin...
- **Primary Substrate**: `#fff` (`var(--background-color)` in `:root`), **Primary Ink**: `#8746e3`, **Accent / Highlight**: `#c7c6be`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--background-color)` in `:root`) paired with `#8746e3` primary typography and `#c7c6be` accents.
  - **Extracted Typographic Hierarchy**: Pairs `helveticaNowDisplay` for display copy (`ZZDP`) with `helveticaNowDisplay Fallback` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `0%` container bounds (`gap: 1px`, padding `.6vw`) with `cubic-bezier(.48,0,.03,1)` easing and Lenis Smooth Scroll (`data-lenis`), Lottie Vector Animation Player.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-zzdp-nl` in your global stylesheet:

:root {
  /* Al meer dan 70 jaar betekenisvolle architectuur · ZZDP (www-zzdp-nl) — Ground-Truth Extracted CSS Variables */
  --background-color: #fff; /* Canvas / Surface Token (www-zzdp-nl) */
  --title-color: #656657; /* Brand / Palette Token (www-zzdp-nl) */
  --subtitle-color: #656657; /* Brand / Palette Token (www-zzdp-nl) */
  --body-color: #656657; /* Typography Ink Token (www-zzdp-nl) */
  --line-color: #1a163019; /* Brand / Palette Token (www-zzdp-nl) */
  --accent-color: #8746e3; /* Brand / Palette Token (www-zzdp-nl) */
  --primary-ui-label-default-color: #fff; /* Brand / Palette Token (www-zzdp-nl) */
  --primary-ui-label-hover-color: #fff; /* Brand / Palette Token (www-zzdp-nl) */
  --primary-ui-label-disabled-color: #c7c6be; /* Brand / Palette Token (www-zzdp-nl) */
  --primary-ui-background-default-color: #656657; /* Canvas / Surface Token (www-zzdp-nl) */
  --primary-ui-background-hover-color: #b5b899; /* Canvas / Surface Token (www-zzdp-nl) */
  --primary-ui-background-disabled-color: #ebeae1; /* Canvas / Surface Token (www-zzdp-nl) */
  --primary-ui-stroke-default-color: #656657; /* Brand / Palette Token (www-zzdp-nl) */
  --primary-ui-stroke-hover-color: #b5b899; /* Brand / Palette Token (www-zzdp-nl) */
  --primary-ui-stroke-disabled-color: #ebeae1; /* Brand / Palette Token (www-zzdp-nl) */
  --secondary-ui-label-default-color: #656657; /* Brand / Palette Token (www-zzdp-nl) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fff` — grounded in `var(--background-color)` in `:root`
- **Primary Typography Ink**: `#656657` — grounded in `var(--title-color)` in `:root`
- **Elevated Surface / Card Substrate**: `#8746e3` — grounded in `var(--accent-color)` in `:root`
- **Interactive Accent / Highlight**: `#c7c6be` — grounded in `var(--primary-ui-label-disabled-color)` in `:root`
- **Secondary / Muted Copy**: `#b5b899` — grounded in `var(--primary-ui-background-hover-color)` in `:root`
- **Structural Hairline Border**: `#ebeae1` — grounded in `var(--primary-ui-background-disabled-color)` in `:root`
- **Variable Token (`--line-color`)**: `#1a163019` — grounded in `var(--line-color)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×18562px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `0%` extracted from `www-zzdp-nl` stylesheet
- **Padding & Gutters**: `.6vw` lateral canvas padding with `1px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 0%`, `gap: 1px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.6vw` horizontal padding
- **Media Queries**: `@media (max-width:47.99em)`, `@media (min-width:48em)`, `@media (min-width:0)`, `@media (min-width:23.4375em)`
- **Corner Radii**: `10px`, `8px`, `50%`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `helveticaNowDisplay`
- **Body Font Stack**: `helveticaNowDisplay Fallback`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--font-helvetica-now-display: "helveticaNowDisplay", "helveticaNowDisplay Fallback"`; rule `h1` (`font-size: 13.3333vw`, `line-height: 82%`, `letter-spacing: -.07em`, `font-weight: 400`)
- **H2 Section Rule**: CSS variables `--subtitle-color: #656657`; rule `h2` (`font-size: 8vw`, `line-height: 105%`, `letter-spacing: .01em`, `font-weight: 400`)
- **Body Copy Rule**: CSS variables `--body-color: #656657`; rule `p` (`font-size: 3.73333vw`, `line-height: 132%`, `letter-spacing: 0`, `font-weight: 400`)
- **Metadata & Index Rule**: CSS variables `--primary-ui-label-default-color: #fff`, `--primary-ui-label-hover-color: #fff`, `--primary-ui-label-disabled-color: #c7c6be`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-zzdp-nl` (`Al meer dan 70 jaar betekenisvolle architectuur · ZZDP`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.lenis> — `www-zzdp-nl`)**:
   - DOM & Selectors: Landmark `<nav class="lenis">` hosting `Al meer dan 70 jaar betekenisvolle a` navigation (`Home · Projecten · Over ons · Nieuws en inzichten · Vacatures`), DOM attributes (`data-next-head`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`), and stylesheet rule `.u-underline-link:after { height:.266667vw }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.lenis> — `www-zzdp-nl`)` (`www-zzdp-nl`) adapts across `@media (max-width:47.99em)`, `@media (min-width:48em)`, `@media (min-width:0)`, `@media (min-width:23.4375em)` with `cubic-bezier(.48,0,.03,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.6,.2,0,.8)` transitions and links `Home · Projecten · Over ons · Nieuws en inzichten · Vacatures`.
2. **Hero Stage & Focal Lead (<section.theme--mossLight> — `ZZDP`)**:
   - DOM & Selectors: Landmark `<section class="theme--mossLight">` presenting display lead `ZZDP` and copy excerpt *"Deze website gebruikt essentiële cookies voor functionaliteit en "* over `#fff` canvas and `#8746e3` ink.
   - Responsive Contract: Hero stage (`1440×18562px` desktop / `390×2400px` mobile) sets `#fff` background with `#8746e3` headline `ZZDP`.
3. **Primary Showcase & Content Grid (<section.vjs-styles-dimensions> — `Bij ZZDP geloven wij dat architect`)**:
   - DOM & Selectors: Landmark `<section class="vjs-styles-dimensions">` rendering section `Bij ZZDP geloven wij dat architectuur meer is dan...` with copy *"Accepteren Accepteren"*, asset references (`favicon.svg`, `HelveticaNowDisplay_Regular-s.p.1...`, `HelveticaNowDisplay_Md-s.p.16ns3u...`, `PPNeueMachina_PlainRegular-s.p.39...`), and grid rule `.default-in-animation { transform:translateY(26.6667vw) }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.vjs-styles-dimensions> — `Bij ZZDP geloven wij dat architect`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 0%`, `gap: 1px`) on desktop and Single-column vertical stack at `390px` viewport width with `.6vw` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.theme--white> — `Ons Werk`)**:
   - DOM & Selectors: Landmark `<section class="theme--white">` framing `Ons Werk` and `Nieuws` (*"Instellingen Instellingen"*) with `#8746e3` surface cards, `#c7c6be` accents, and `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;line-height:1.15 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.theme--white> — `Ons Werk`)` uses `10px`, `8px`, `50%`, `2px` radii, `#c7c6be` highlights, and assets (favicon.svg, HelveticaNowDisplay_Regular-s.p.1..., HelveticaNowDisplay_Md-s.p.16ns3u...).
5. **Colophon & Global Directory Footer (<footer.theme--white> — `https://www.zzdp.nl/`)**:
   - DOM & Selectors: Landmark `<footer class="theme--white">` anchoring `Al meer dan 70 jaar betekenisvol` footer links (`Home · Projecten · Over ons · Nieuws en inzichten · Vacatures`), copy *"Nieuws en inzichten"*, and `#ebeae1` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.theme--white> — `https://www.zzdp.nl/`)` aligns to `0%` extracted from `www-zzdp-nl` stylesheet with `.6vw` lateral canvas padding with `1px` grid gap and attributes (data-next-head, data-next-font="size-adjust", data-next-font="size-adjust").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Deze website gebruikt essentiële cookies voor functionaliteit en tracking cookies..."*
- Copy Excerpt 2: *"Accepteren Accepteren"*
- Copy Excerpt 3: *"Instellingen Instellingen"*
- Copy Excerpt 4: *"Nieuws en inzichten"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.48,0,.03,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.6,.2,0,.8)`
- **Extracted Stylesheet Rules (`www-zzdp-nl`)**:
- `.u-underline-link:after { height:.266667vw }`
- `.default-in-animation { transform:translateY(26.6667vw) }`
- `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;line-height:1.15 }`
- `section { display:block }`
- `main { display:block }`
- **Per-Selector Transition Rules**:
- **Selector `.c-scrollbar`**: `transition: transform .3s,opacity .3s` extracted from `www-zzdp-nl` stylesheet.
- **Selector `.u-underline-link:after`**: `transition: transform .3s cubic-bezier(.48,0,.03,1)` extracted from `www-zzdp-nl` stylesheet.
- **Selector `scss-module__shXJnq__u-underline-...`**: `transition: transform .3s cubic-bezier(.48,0,.03,1)` extracted from `www-zzdp-nl` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.48,0,.03,1)`)**: Governs interactive state transitions across `<nav.lenis>` and `<section.vjs-styles-dimensions>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-zzdp-nl`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
