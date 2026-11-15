---
title: "UI Prompt Blueprint: awmedia-marketing"
date: 2026-11-15
target: "awmedia-marketing"
status: analyzed
capture: dom
capture_desktop: dom
capture_mobile: dom
archetype: "Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#000` ink, `#d4d4d9` accent)"
---

# UI Design System & Master Generation Blueprint: awmedia-marketing

> **AW Media & Marketing · UK Web Design Studio** (https://awmedia.marketing/) — Award-winning web design for ambitious UK businesses. Sheffield-based, UK-wide. Bespoke when the project demands it, AI-accelerated when...

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **AW Media & Marketing · UK Web Design Studio** (`https://awmedia.marketing/`). Award-winning web design for ambitious UK businesses. Sheffield-based, UK-wide. Bespoke when the project demands it, AI-accelerated when...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#000` ink, `#d4d4d9` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--color-white)` in `:root`) paired with `#000` primary typography and `#d4d4d9` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Rethink Sans` for display copy (`Designed properly. Built faster.`) with `Rethink Sans Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: 10px`, padding `1px`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×16653px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40rem` extracted from `awmedia-marketing` stylesheet.
- **Canvas Lateral Padding & Spacing**: `1px` lateral canvas padding with `10px` grid gap.
- **Border Radius Scale**: `.25rem`, `var(--radius-2xl)`, `var(--radius-xl)`, `3px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 10px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--color-white)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--background)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ededed` | `var(--foreground)` in `:root` |
| **Interactive Accent / Highlight** | `#d4d4d9` | `var(--pink-dark)` in `:root` |
| **Secondary / Muted Copy** | `#111` | `var(--card-bg)` in `:root` |
| **Structural Hairline Border** | `#1a1a1a` | `var(--card-border)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-rethink-sans` | `"Rethink Sans", "Rethink Sans Fallback"` | Typography Ink Token |
| `--aw-angle` | `0deg` | Design System Custom Token |
| `--aw-n` | `0` | Design System Custom Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-md` | `28rem` | Layout / Spatial Grid Token |
| `--container-2xl` | `42rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |
| `--container-6xl` | `72rem` | Layout / Spatial Grid Token |
| `--container-7xl` | `80rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25 / .875)` | Typography Ink Token |
| `--text-base` | `1rem` | Typography Ink Token |
| `--text-base--line-height` | `calc(1.5 / 1)` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Rethink Sans`.
- **Primary Body Stack**: `Rethink Sans Fallback`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`.
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: clamp(38px,4.6vw,72px)`).
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: 16.5px`, `line-height: 1.62`).
- **Metadata & Navigation Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.22,1,.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `awmedia-marketing` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `awmedia-marketing` stylesheet.
- **Selector `.transition-all`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `awmedia-marketing` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.nav>` and `<section.built>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — AW Media & Marketing · UK Web Design Studi │
│ ====================================================================== │
│ [ <header.nav>             | How We Work · Industries · About · Blo ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero>                                       |   │
│ | H1: Designed properly. Built faster.                             |   │
│ | Substrate: #fff       | Ink: #000       | Accent: #d4d4d9        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.built>           ) max-w: 40rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Built like this.             |  | Award-⁠winning design, AI-⁠a | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 10px  ) | │
│ | [<header.nav>] -> [<section.hero>] -> [<section.built>] |            │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>       ) | https://awmedia.marketing/         │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.nav> — `awmedia-marketing`)**:
   - Landmark `<header class="nav">` hosting `AW Media & Marketing · UK Web Design` navigation (`How We Work · Industries · About · Blog`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-liquid="cursor"`, `data-liquid="pill"`), and stylesheet rule `sans_a7e6451-module__qxRvCW__clas... { font-family:Rethink Sans,Rethink Sans Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Designed properly. Built faster.`)**:
   - Landmark `<section class="hero">` presenting display lead `Designed properly. Built faster.` and copy excerpt *"UK Web Design Studio · Since 2016"* over `#fff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.built> — `Built like this.`)**:
   - Landmark `<section class="built">` rendering section `Built like this.` with copy *"Designed properly."*, asset references (`0dc02305a3505331-s.p.045lmq4bb63o...`, `aw-logo.png`, `04rv9lq_~p.97.css`, `0yrizplp3s9dt.css`), and grid rule `k_sans_a7e6451-module__qxRvCW__va... { --font-rethink-sans:"Rethink Sans", "Rethink Sans Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.trusted> — `Award-⁠winning design, AI-⁠acceler`)**:
   - Landmark `<section class="trusted">` framing `Award-⁠winning design, AI-⁠accelerated where it c...` and `From idea to live. Sites that ship.` (*"An award-⁠winning UK studio shipping bespoke websites at AI-⁠acce"*) with `#ededed` surface cards, `#d4d4d9` accents, and `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://awmedia.marketing/`)**:
   - Landmark `<footer class="footer">` anchoring `AW Media & Marketing · UK Web De` footer links (`How We Work · Industries · About · Blog`), copy *"450+ websites shipped"*, and `#1a1a1a` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: awmedia-marketing (AW Media & Marketing · UK Web Design Studio)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `awmedia-marketing` (**AW Media & Marketing · UK Web Design Studio** — `https://awmedia.marketing/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#000` ink, `#d4d4d9` accent).
- **Identity & Domain Context**: Award-winning web design for ambitious UK businesses. Sheffield-based, UK-wide. Bespoke when the project demands it, AI-accelerated when...
- **Primary Substrate**: `#fff` (`var(--color-white)` in `:root`), **Primary Ink**: `#000`, **Accent / Highlight**: `#d4d4d9`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--color-white)` in `:root`) paired with `#000` primary typography and `#d4d4d9` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Rethink Sans` for display copy (`Designed properly. Built faster.`) with `Rethink Sans Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: 10px`, padding `1px`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `awmedia-marketing` in your global stylesheet:

:root {
  /* AW Media & Marketing · UK Web Design Studio (awmedia-marketing) — Ground-Truth Extracted CSS Variables */
  --font-rethink-sans: "Rethink Sans", "Rethink Sans Fallback"; /* Typography Ink Token (awmedia-marketing) */
  --aw-angle: 0deg; /* Design System Custom Token (awmedia-marketing) */
  --aw-n: 0; /* Design System Custom Token (awmedia-marketing) */
  --color-white: #fff; /* Canvas / Surface Token (awmedia-marketing) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (awmedia-marketing) */
  --container-md: 28rem; /* Layout / Spatial Grid Token (awmedia-marketing) */
  --container-2xl: 42rem; /* Layout / Spatial Grid Token (awmedia-marketing) */
  --container-3xl: 48rem; /* Layout / Spatial Grid Token (awmedia-marketing) */
  --container-6xl: 72rem; /* Layout / Spatial Grid Token (awmedia-marketing) */
  --container-7xl: 80rem; /* Layout / Spatial Grid Token (awmedia-marketing) */
  --text-xs: .75rem; /* Typography Ink Token (awmedia-marketing) */
  --text-xs--line-height: calc(1 / .75); /* Typography Ink Token (awmedia-marketing) */
  --text-sm: .875rem; /* Typography Ink Token (awmedia-marketing) */
  --text-sm--line-height: calc(1.25 / .875); /* Typography Ink Token (awmedia-marketing) */
  --text-base: 1rem; /* Typography Ink Token (awmedia-marketing) */
  --text-base--line-height: calc(1.5 / 1); /* Typography Ink Token (awmedia-marketing) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Primary Typography Ink**: `#000` — grounded in `var(--background)` in `:root`
- **Elevated Surface / Card Substrate**: `#ededed` — grounded in `var(--foreground)` in `:root`
- **Interactive Accent / Highlight**: `#d4d4d9` — grounded in `var(--pink-dark)` in `:root`
- **Secondary / Muted Copy**: `#111` — grounded in `var(--card-bg)` in `:root`
- **Structural Hairline Border**: `#1a1a1a` — grounded in `var(--card-border)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×16653px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40rem` extracted from `awmedia-marketing` stylesheet
- **Padding & Gutters**: `1px` lateral canvas padding with `10px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 10px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1px` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `.25rem`, `var(--radius-2xl)`, `var(--radius-xl)`, `3px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Rethink Sans`
- **Body Font Stack**: `Rethink Sans Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: clamp(38px,4.6vw,72px)`)
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: 16.5px`, `line-height: 1.62`)
- **Metadata & Index Rule**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `awmedia-marketing` (`AW Media & Marketing · UK Web Design Studio`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.nav> — `awmedia-marketing`)**:
   - DOM & Selectors: Landmark `<header class="nav">` hosting `AW Media & Marketing · UK Web Design` navigation (`How We Work · Industries · About · Blog`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-liquid="cursor"`, `data-liquid="pill"`), and stylesheet rule `sans_a7e6451-module__qxRvCW__clas... { font-family:Rethink Sans,Rethink Sans Fallback;font-style:normal }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.nav> — `awmedia-marketing`)` (`awmedia-marketing`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)` with `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.22,1,.36,1)` transitions and links `How We Work · Industries · About · Blog`.
2. **Hero Stage & Focal Lead (<section.hero> — `Designed properly. Built faster.`)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `Designed properly. Built faster.` and copy excerpt *"UK Web Design Studio · Since 2016"* over `#fff` canvas and `#000` ink.
   - Responsive Contract: Hero stage (`1440×16653px` desktop / `390×2400px` mobile) sets `#fff` background with `#000` headline `Designed properly. Built faster.`.
3. **Primary Showcase & Content Grid (<section.built> — `Built like this.`)**:
   - DOM & Selectors: Landmark `<section class="built">` rendering section `Built like this.` with copy *"Designed properly."*, asset references (`0dc02305a3505331-s.p.045lmq4bb63o...`, `aw-logo.png`, `04rv9lq_~p.97.css`, `0yrizplp3s9dt.css`), and grid rule `k_sans_a7e6451-module__qxRvCW__va... { --font-rethink-sans:"Rethink Sans", "Rethink Sans Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.built> — `Built like this.`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 10px`) on desktop and Single-column vertical stack at `390px` viewport width with `1px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.trusted> — `Award-⁠winning design, AI-⁠acceler`)**:
   - DOM & Selectors: Landmark `<section class="trusted">` framing `Award-⁠winning design, AI-⁠accelerated where it c...` and `From idea to live. Sites that ship.` (*"An award-⁠winning UK studio shipping bespoke websites at AI-⁠acce"*) with `#ededed` surface cards, `#d4d4d9` accents, and `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.trusted> — `Award-⁠winning design, AI-⁠acceler`)` uses `.25rem`, `var(--radius-2xl)`, `var(--radius-xl)`, `3px` radii, `#d4d4d9` highlights, and assets (0dc02305a3505331-s.p.045lmq4bb63o..., aw-logo.png, 04rv9lq_~p.97.css).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://awmedia.marketing/`)**:
   - DOM & Selectors: Landmark `<footer class="footer">` anchoring `AW Media & Marketing · UK Web De` footer links (`How We Work · Industries · About · Blog`), copy *"450+ websites shipped"*, and `#1a1a1a` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://awmedia.marketing/`)` aligns to `40rem` extracted from `awmedia-marketing` stylesheet with `1px` lateral canvas padding with `10px` grid gap and attributes (data-precedence="next", data-precedence="next", data-liquid="cursor").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"UK Web Design Studio · Since 2016"*
- Copy Excerpt 2: *"Designed properly."*
- Copy Excerpt 3: *"An award-⁠winning UK studio shipping bespoke websites at AI-⁠accelerated speed. Tw..."*
- Copy Excerpt 4: *"450+ websites shipped"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.22,1,.36,1)`
- **Extracted Stylesheet Rules (`awmedia-marketing`)**:
- `sans_a7e6451-module__qxRvCW__clas... { font-family:Rethink Sans,Rethink Sans Fallback;font-style:normal }`
- `k_sans_a7e6451-module__qxRvCW__va... { --font-rethink-sans:"Rethink Sans", "Rethink Sans Fallback" }`
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `awmedia-marketing` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `awmedia-marketing` stylesheet.
- **Selector `.transition-all`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `awmedia-marketing` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.nav>` and `<section.built>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `awmedia-marketing`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
