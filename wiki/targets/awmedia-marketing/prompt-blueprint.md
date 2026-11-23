---
title: "UI Prompt Blueprint: awmedia-marketing"
date: 2026-11-23
captured_at: 2026-11-23
target: "awmedia-marketing"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#f5f5f7` ink, `#ffffff` accent)"
---

# UI Design System & Master Generation Blueprint: awmedia-marketing

> **AW Media & Marketing · UK Web Design Studio** (https://awmedia.marketing/) — Award-winning web design for ambitious UK businesses. Sheffield-based, UK-wide. Bespoke when the project demands it, AI-accelerated when...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **AW Media & Marketing · UK Web Design Studio** (`https://awmedia.marketing/`). Award-winning web design for ambitious UK businesses. Sheffield-based, UK-wide. Bespoke when the project demands it, AI-accelerated when...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#f5f5f7` ink, `#ffffff` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `html` `background-color` (`computed_styles.json`)) paired with `#f5f5f7` primary typography and `#ffffff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Rethink Sans` for display copy (`Designed properly. Built faster.`) with `Rethink Sans` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1408px` container bounds (`gap: 2px`, padding `14px`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1408px` (measured widest bounded `<section>` landmark width on `1440px` desktop).
- **Canvas Lateral Padding & Spacing**: `14px` lateral canvas padding with `2px` grid gap.
- **Border Radius Scale**: `999px`, `.25rem`, `var(--radius-2xl)`, `var(--radius-xl)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1408px`, `gap: 2px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `14px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f5f5f7` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#111111` | `var(--card-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#ffffff` | `.btn-solid { background: #ffffff }` |
| **Secondary / Muted Copy** | `#888888` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#1a1a1a` | `var(--card-border)` in `:root` |
| **Variable Token (`--foreground`)** | `#ededed` | `var(--foreground)` in `:root` |
| **Variable Token (`--pink-dark`)** | `#d4d4d9` | `var(--pink-dark)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background` | `#000` | Canvas / Surface Token |
| `--foreground` | `#ededed` | Typography Ink Token |
| `--pink` | `#fff` | Typography Ink Token |
| `--pink-dark` | `#d4d4d9` | Canvas / Surface Token |
| `--card-bg` | `#111` | Canvas / Surface Token |
| `--card-border` | `#1a1a1a` | Elevation / Border Token |
| `--muted` | `#888` | Color / Atmospheric Token |
| `--bg` | `#000` | Canvas / Surface Token |
| `--ink` | `#f5f5f7` | Typography Ink Token |
| `--ink-2` | `#f5f5f7a8` | Typography Ink Token |
| `--ink-3` | `#f5f5f76b` | Typography Ink Token |
| `--line` | `#ffffff17` | Color / Atmospheric Token |
| `--maxw` | `1280px` | Dimension / Scale Token |
| `--gutter` | `clamp(20px,4.6vw,64px)` | Layout / Spatial Grid Token |
| `--ease` | `cubic-bezier(.16,1,.3,1)` | Motion / Easing Token |
| `--r-xl` | `32px` | Dimension / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Rethink Sans`.
- **Primary Body Stack**: `Rethink Sans`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 152.64px`, `line-height: 137.376px`, `font-weight: 700`, `letter-spacing: -8.3952px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 89.28px`, `line-height: 87.4944px`, `font-weight: 600`, `letter-spacing: -4.0176px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: clamp(38px,4.6vw,72px)`).
- **Body Copy**: live computed `body` (`font-size: 17px`, `line-height: 25.5px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: 16.5px`, `line-height: 1.62`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 17px`, `line-height: 25.5px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`.

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

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — AW Media & Marketing · UK Web Design Studi │
│ ====================================================================== │
│ [ <header.nav> (1440x60px)            | How We Work · Industries · A ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero> (w=1440px)                              | │
│ | H1: Designed properly. Built faster.                               | │
│ | Substrate: #000000 | Ink: #f5f5f7 | Accent: #ffffff                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.built>) max-w: 1408px                      | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Built like this.             |  | Award-⁠winning design, AI-⁠a | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.trusted>) — From idea to live. Si          | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>     ) | https://awmedia.marketing/           │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 2px)        │
│ ====================================================================== │
│ [ HEADER BAR (<header.nav>            ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.hero>) — 390px Vertical Lead                  | │
│ | H1: Designed properly. Built faster.                               | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.built>) — 1-Col Stack                     | │
│ | [ Item 1: Built like this.                                       ] | │
│ | [ Item 2: Award-⁠winning design, AI-⁠accelerated where it c...   ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.trusted>) — 1-Col (From idea to live.)      | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>     ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.nav> — `awmedia-marketing`)**:
   - Landmark `<header class="nav">` (`1440x60px`) hosting `AW Media & Marketing · UK Web Design` navigation (`How We Work · Industries · About · Blog`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-liquid="cursor"`, `data-liquid="pill"`), and stylesheet rule `sans_a7e6451-module__qxRvCW__clas... { font-family:Rethink Sans,Rethink Sans Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Designed properly. Built faster.`)**:
   - Landmark `<section class="hero">` presenting display lead `Designed properly. Built faster.` and copy excerpt *"An award-⁠winning UK studio shipping bespoke websites at AI-⁠acce"* over `#000000` canvas and `#f5f5f7` ink.
3. **Primary Showcase & Content Grid (<section.built> — `Built like this.`)**:
   - Landmark `<section class="built">` rendering section `Built like this.` with copy *"UK Web Design Studio · Since 2016"*, asset references (`0dc02305a3505331-s.p.045lmq4bb63o...`, `aw-logo.png`, `04rv9lq_~p.97.css`, `0yrizplp3s9dt.css`), and grid rule `k_sans_a7e6451-module__qxRvCW__va... { --font-rethink-sans:"Rethink Sans", "Rethink Sans Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.trusted> — `Award-⁠winning design, AI-⁠acceler`)**:
   - Landmark `<section class="trusted">` framing `Award-⁠winning design, AI-⁠accelerated where it c...` and `From idea to live. Sites that ship.` (*"Designed properly."*) with `#111111` surface cards, `#ffffff` accents, and `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://awmedia.marketing/`)**:
   - Landmark `<footer class="footer">` anchoring `AW Media & Marketing · UK Web De` footer links (`How We Work · Industries · About · Blog`), copy *"450+ websites shipped"*, and `#1a1a1a` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: awmedia-marketing (AW Media & Marketing · UK Web Design Studio)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `awmedia-marketing` (**AW Media & Marketing · UK Web Design Studio** — `https://awmedia.marketing/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#f5f5f7` ink, `#ffffff` accent).
- **Identity & Domain Context**: Award-winning web design for ambitious UK businesses. Sheffield-based, UK-wide. Bespoke when the project demands it, AI-accelerated when...
- **Primary Substrate**: `#000000` (live computed `html` `background-color` (`computed_styles.json`)), **Primary Ink**: `#f5f5f7`, **Accent / Highlight**: `#ffffff`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `html` `background-color` (`computed_styles.json`)) paired with `#f5f5f7` primary typography and `#ffffff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Rethink Sans` for display copy (`Designed properly. Built faster.`) with `Rethink Sans` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1408px` container bounds (`gap: 2px`, padding `14px`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `awmedia-marketing` in your global stylesheet:

:root {
  /* AW Media & Marketing · UK Web Design Studio (awmedia-marketing) — Live-Grounded CSS Variables */
  --background: #000; /* Canvas / Surface Token (awmedia-marketing) */
  --foreground: #ededed; /* Typography Ink Token (awmedia-marketing) */
  --pink: #fff; /* Typography Ink Token (awmedia-marketing) */
  --pink-dark: #d4d4d9; /* Canvas / Surface Token (awmedia-marketing) */
  --card-bg: #111; /* Canvas / Surface Token (awmedia-marketing) */
  --card-border: #1a1a1a; /* Elevation / Border Token (awmedia-marketing) */
  --muted: #888; /* Color / Atmospheric Token (awmedia-marketing) */
  --bg: #000; /* Canvas / Surface Token (awmedia-marketing) */
  --ink: #f5f5f7; /* Typography Ink Token (awmedia-marketing) */
  --ink-2: #f5f5f7a8; /* Typography Ink Token (awmedia-marketing) */
  --ink-3: #f5f5f76b; /* Typography Ink Token (awmedia-marketing) */
  --line: #ffffff17; /* Color / Atmospheric Token (awmedia-marketing) */
  --maxw: 1280px; /* Dimension / Scale Token (awmedia-marketing) */
  --gutter: clamp(20px,4.6vw,64px); /* Layout / Spatial Grid Token (awmedia-marketing) */
  --ease: cubic-bezier(.16,1,.3,1); /* Motion / Easing Token (awmedia-marketing) */
  --r-xl: 32px; /* Dimension / Scale Token (awmedia-marketing) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000000` — grounded in live computed `html` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#f5f5f7` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#111111` — grounded in `var(--card-bg)` in `:root`
- **Interactive Accent / Highlight**: `#ffffff` — grounded in `.btn-solid { background: #ffffff }`
- **Secondary / Muted Copy**: `#888888` — grounded in `var(--muted)` in `:root`
- **Structural Hairline Border**: `#1a1a1a` — grounded in `var(--card-border)` in `:root`
- **Variable Token (`--foreground`)**: `#ededed` — grounded in `var(--foreground)` in `:root`
- **Variable Token (`--pink-dark`)**: `#d4d4d9` — grounded in `var(--pink-dark)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1408px` (measured widest bounded `<section>` landmark width on `1440px` desktop)
- **Padding & Gutters**: `14px` lateral canvas padding with `2px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1408px`, `gap: 2px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `14px` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `999px`, `.25rem`, `var(--radius-2xl)`, `var(--radius-xl)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Rethink Sans`
- **Body Font Stack**: `Rethink Sans`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: live computed `h1` (`font-size: 152.64px`, `line-height: 137.376px`, `font-weight: 700`, `letter-spacing: -8.3952px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **H2 Section Rule**: live computed `h2` (`font-size: 89.28px`, `line-height: 87.4944px`, `font-weight: 600`, `letter-spacing: -4.0176px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: clamp(38px,4.6vw,72px)`)
- **Body Copy Rule**: live computed `body` (`font-size: 17px`, `line-height: 25.5px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: 16.5px`, `line-height: 1.62`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 17px`, `line-height: 25.5px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `awmedia-marketing` (`AW Media & Marketing · UK Web Design Studio`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.nav> — `awmedia-marketing`)**:
   - DOM & Selectors: Landmark `<header class="nav">` (`1440x60px`) hosting `AW Media & Marketing · UK Web Design` navigation (`How We Work · Industries · About · Blog`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-liquid="cursor"`, `data-liquid="pill"`), and stylesheet rule `sans_a7e6451-module__qxRvCW__clas... { font-family:Rethink Sans,Rethink Sans Fallback;font-style:normal }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.nav> — `awmedia-marketing`)` (`awmedia-marketing`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)` with `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.22,1,.36,1)` transitions and links `How We Work · Industries · About · Blog`.
2. **Hero Stage & Focal Lead (<section.hero> — `Designed properly. Built faster.`)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `Designed properly. Built faster.` and copy excerpt *"An award-⁠winning UK studio shipping bespoke websites at AI-⁠acce"* over `#000000` canvas and `#f5f5f7` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#000000` background with `#f5f5f7` headline `Designed properly. Built faster.`.
3. **Primary Showcase & Content Grid (<section.built> — `Built like this.`)**:
   - DOM & Selectors: Landmark `<section class="built">` rendering section `Built like this.` with copy *"UK Web Design Studio · Since 2016"*, asset references (`0dc02305a3505331-s.p.045lmq4bb63o...`, `aw-logo.png`, `04rv9lq_~p.97.css`, `0yrizplp3s9dt.css`), and grid rule `k_sans_a7e6451-module__qxRvCW__va... { --font-rethink-sans:"Rethink Sans", "Rethink Sans Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.built> — `Built like this.`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1408px`, `gap: 2px`) on desktop and Single-column vertical stack at `390px` viewport width with `14px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.trusted> — `Award-⁠winning design, AI-⁠acceler`)**:
   - DOM & Selectors: Landmark `<section class="trusted">` framing `Award-⁠winning design, AI-⁠accelerated where it c...` and `From idea to live. Sites that ship.` (*"Designed properly."*) with `#111111` surface cards, `#ffffff` accents, and `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.trusted> — `Award-⁠winning design, AI-⁠acceler`)` uses `999px`, `.25rem`, `var(--radius-2xl)`, `var(--radius-xl)` radii, `#ffffff` highlights, and assets (0dc02305a3505331-s.p.045lmq4bb63o..., aw-logo.png, 04rv9lq_~p.97.css).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://awmedia.marketing/`)**:
   - DOM & Selectors: Landmark `<footer class="footer">` anchoring `AW Media & Marketing · UK Web De` footer links (`How We Work · Industries · About · Blog`), copy *"450+ websites shipped"*, and `#1a1a1a` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://awmedia.marketing/`)` aligns to `1408px` (measured widest bounded `<section>` landmark width on `1440px` desktop) with `14px` lateral canvas padding with `2px` grid gap and attributes (data-precedence="next", data-precedence="next", data-liquid="cursor").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"An award-⁠winning UK studio shipping bespoke websites at AI-⁠accelerated speed. Tw..."*
- Copy Excerpt 2: *"UK Web Design Studio · Since 2016"*
- Copy Excerpt 3: *"Designed properly."*
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
