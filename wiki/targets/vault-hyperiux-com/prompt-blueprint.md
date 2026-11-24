---
title: "UI Prompt Blueprint: vault-hyperiux-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "vault-hyperiux-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: native
desktop_keyframes: 1
subpages_crawled: 0
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#111111` / `#ff5f00`)"
---

# UI Design System & Master Generation Blueprint: vault-hyperiux-com

> **Hyperiux Vault - React & Next.js Interaction Effects.** (https://vault.hyperiux.com) — Start with 70+ free source-first effects. Upgrade to Pro for 180+ effects.

![Desktop Journey Filmstrip (1280x828)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Hyperiux Vault - React & Next.js Interaction Effects.** (`https://vault.hyperiux.com`). Start with 70+ free source-first effects. Upgrade to Pro for 180+ effects.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#111111` / `#ff5f00`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#111111` (live computed `html` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#ff5f00` accents.
  - **Grounded Typographic Hierarchy**: Pairs `aeonikPro` for display copy (`The Interaction Layer Your Website I`) with `avenirNext` and `IBM Plex Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1310px` container bounds (`gap: 17.28px`, padding `64.8px`) with `cubic-bezier(.4,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×828px` (`assets/desktop-journey.webp`, `1` keyframes up to `y=0px` / doc `13140px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1310px` (measured widest bounded `<section>` landmark width on `1440px` desktop).
- **Canvas Lateral Padding & Spacing**: `64.8px` lateral canvas padding with `17.28px` grid gap.
- **Border Radius Scale**: `50%`, `9999px`, `.25rem`, `9px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1310px`, `gap: 17.28px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `64.8px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:640px)`, `@media (max-width:960px)`, `@media (max-width:720px)`, `@media (max-width:767px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#111111` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#161616` | `var(--dark-card)` in `:root` |
| **Interactive Accent / Highlight** | `#ff5f00` | live computed `button` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#ff5f00` | live computed `button` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#272727` | `var(--blog-border-color)` in `:root` |
| **Variable Token (`--secondary`)** | `#d9d9d9` | `var(--secondary)` in `:root` |
| **Variable Token (`--primary-hover`)** | `#ff9253` | `var(--primary-hover)` in `:root` |
| **Variable Token (`--border`)** | `#bcbcbc` | `var(--border)` in `:root` |
| **Variable Token (`--muted-on-dark`)** | `#d2d2d2` | `var(--muted-on-dark)` in `:root` |
| **Variable Token (`--light-grey`)** | `#939393` | `var(--light-grey)` in `:root` |
| **Variable Token (`--light`)** | `#f4f4f4` | `var(--light)` in `:root` |
| **Variable Token (`--ink`)** | `#1d1d1d` | `var(--ink)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--vault-ctl-h` | `max(44px,calc(var(--hx-vw,1vw) * 1.725 + 1rem))` | Dimension / Scale Token |
| `--cvw` | `min(1vw,15.36px)` | Layout / Spatial Grid Token |
| `--background` | `#111` | Canvas / Surface Token |
| `--white` | `#fff` | Canvas / Surface Token |
| `--foreground` | `var(--white)` | Typography Ink Token |
| `--secondary` | `#d9d9d9` | Brand / Palette Token |
| `--primary` | `#ff5f00` | Brand / Palette Token |
| `--primary-hover` | `#ff9253` | Brand / Palette Token |
| `--dark-card` | `#161616` | Canvas / Surface Token |
| `--border` | `#bcbcbc` | Elevation / Border Token |
| `--muted-on-dark` | `#d2d2d2` | Canvas / Surface Token |
| `--muted` | `var(--muted-on-dark)` | Design System Custom Token |
| `--grey` | `#272727` | Color / Atmospheric Token |
| `--light-grey` | `#939393` | Canvas / Surface Token |
| `--light` | `#f4f4f4` | Canvas / Surface Token |
| `--ink` | `#1d1d1d` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `aeonikPro`.
- **Primary Body Stack**: `avenirNext`.
- **Technical / Metadata Stack**: `IBM Plex Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 92.16px`, `line-height: 103.219px`, `font-weight: 400`, `letter-spacing: -3.2256px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`; rule `h1` (`font-size: 2.5rem`, `line-height: 1.2`, `letter-spacing: -.025em`, `font-weight: 700`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 66.24px`, `line-height: 76.176px`, `font-weight: 400`, `letter-spacing: -2.3184px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 1.75rem`, `line-height: 1.3`, `font-weight: 700`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`.
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`); CSS variables `--font-plex-mono: "IBM Plex Mono","IBM Plex Mono Fallback"`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `vault-hyperiux-com` stylesheet.
- **Selector `layer theme`**: `transition: .15s` extracted from `vault-hyperiux-com` stylesheet.
- **Selector `.codeblock) *)`**: `transition: opacity .15s` extracted from `vault-hyperiux-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<nav.z-900>` and `<section.section-x>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `13140px`, deepest scrollY reached `0px` across `1` desktop keyframes).
- **Detected Scroll / Motion Libraries**: Native browser scroll / standard CSS transitions.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Hyperiux Vault - React & Next.js Interacti │
│ ====================================================================== │
│ [ <nav.z-900> (427x164px)             | Docs D o c s Docs · Blog B l ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.relative> (w=1440px)                          | │
│ | H1: The Interaction Layer Your Website Is Missing.                 | │
│ | Substrate: #111111 | Ink: #ffffff | Accent: #ff5f00                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.section-x>) max-w: 1310px                  | │
│ | +------------------------------+  +------------------------------+ | │
│ | | The Interaction Layer Your W |  | Read Docs R e a d D o c s Re | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<article.flex>) — Browse All Effects B              | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.z-200>      ) | https://vault.hyperiux.com           │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 17.28px)    │
│ ====================================================================== │
│ [ HEADER BAR (<nav.z-900>             ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.relative>) — 390px Vertical Lead              | │
│ | H1: The Interaction Layer Your Website Is Missing.                 | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.section-x>) — 1-Col Stack                 | │
│ | [ Item 1: The Interaction Layer Your Website Is Missing .        ] | │
│ | [ Item 2: Read Docs R e a d D o c s Read Docs                    ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<article.flex>) — 1-Col (Browse All Effects)         | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.z-200>      ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.z-900> — `vault-hyperiux-com`)**:
   - Landmark `<nav class="z-900 top-0">` (`427x164px`) hosting `Hyperiux Vault - React & Next.js Int` navigation (`Docs D o c s Docs · Blog B l o g Blog`), DOM attributes (`data-sidebar="expanded"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.__className_644730 { font-family:aeonikPro,aeonikPro Fallback }`.
2. **Hero Stage & Focal Lead (<section.relative> — `The Interaction Layer Your Website`)**:
   - Landmark `<section class="relative z-10">` presenting display lead `The Interaction Layer Your Website Is Missing.` and copy excerpt *"Source-first scroll systems, cursor effects, text reveals, page t"* over `#111111` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.section-x> — `The Interaction Layer Your Website`)**:
   - Landmark `<section class="section-x text-ink">` rendering section `The Interaction Layer Your Website Is Missing .` with copy *"Read Docs R e a d D o c s Read Docs"*, asset references (`homepage-hero.webp`, `45c5b69ac3104145.css`, `b68a34d2a9030372.css`, `ee41bfcc83e4e14b.css`), and grid rule `.__variable_644730 { --font-aeonik:"aeonikPro","aeonikPro Fallback" }`.
4. **Interactive Detail & Feature Matrix (<article.flex> — `Read Docs R e a d D o c s Read Doc`)**:
   - Landmark `<article class="flex flex-col">` framing `Read Docs R e a d D o c s Read Docs` and `Browse All Effects B r o w s e A l l E f f e c t` (*"Browse All Effects B r o w s e A l l E f f e c t s Browse All Eff"*) with `#161616` surface cards, `#ff5f00` accents, and `.__className_617731 { font-family:avenirNext,avenirNext Fallback }`.
5. **Colophon & Global Directory Footer (<footer.z-200> — `https://vault.hyperiux.com`)**:
   - Landmark `<footer class="z-200 overflow-x-clip">` anchoring `Hyperiux Vault - React & Next.js` footer links (`Docs D o c s Docs · Blog B l o g Blog`), copy *"Browse All Effects"*, and `#272727` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `The Interaction Layer Your Website Is Missing.` · sticky/fixed elements: `1`

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: vault-hyperiux-com (Hyperiux Vault - React & Next.js Interaction Effects.)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `vault-hyperiux-com` (**Hyperiux Vault - React & Next.js Interaction Effects.** — `https://vault.hyperiux.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#111111` / `#ff5f00`).
- **Identity & Domain Context**: Start with 70+ free source-first effects. Upgrade to Pro for 180+ effects.
- **Primary Substrate**: `#111111` (live computed `html` `background-color` (`computed_styles.json`)), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#ff5f00`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#111111` (live computed `html` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#ff5f00` accents.
  - **Grounded Typographic Hierarchy**: Pairs `aeonikPro` for display copy (`The Interaction Layer Your Website I`) with `avenirNext` and `IBM Plex Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1310px` container bounds (`gap: 17.28px`, padding `64.8px`) with `cubic-bezier(.4,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `vault-hyperiux-com` in your global stylesheet:

:root {
  /* Hyperiux Vault - React & Next.js Interaction Effects. (vault-hyperiux-com) — Live-Grounded CSS Variables */
  --vault-ctl-h: max(44px,calc(var(--hx-vw,1vw) * 1.725 + 1rem)); /* Dimension / Scale Token (vault-hyperiux-com) */
  --cvw: min(1vw,15.36px); /* Layout / Spatial Grid Token (vault-hyperiux-com) */
  --background: #111; /* Canvas / Surface Token (vault-hyperiux-com) */
  --white: #fff; /* Canvas / Surface Token (vault-hyperiux-com) */
  --foreground: var(--white); /* Typography Ink Token (vault-hyperiux-com) */
  --secondary: #d9d9d9; /* Brand / Palette Token (vault-hyperiux-com) */
  --primary: #ff5f00; /* Brand / Palette Token (vault-hyperiux-com) */
  --primary-hover: #ff9253; /* Brand / Palette Token (vault-hyperiux-com) */
  --dark-card: #161616; /* Canvas / Surface Token (vault-hyperiux-com) */
  --border: #bcbcbc; /* Elevation / Border Token (vault-hyperiux-com) */
  --muted-on-dark: #d2d2d2; /* Canvas / Surface Token (vault-hyperiux-com) */
  --muted: var(--muted-on-dark); /* Design System Custom Token (vault-hyperiux-com) */
  --grey: #272727; /* Color / Atmospheric Token (vault-hyperiux-com) */
  --light-grey: #939393; /* Canvas / Surface Token (vault-hyperiux-com) */
  --light: #f4f4f4; /* Canvas / Surface Token (vault-hyperiux-com) */
  --ink: #1d1d1d; /* Typography Ink Token (vault-hyperiux-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#111111` — grounded in live computed `html` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#ffffff` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#161616` — grounded in `var(--dark-card)` in `:root`
- **Interactive Accent / Highlight**: `#ff5f00` — grounded in live computed `button` `color` (`computed_styles.json`)
- **Secondary / Muted Copy**: `#ff5f00` — grounded in live computed `button` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#272727` — grounded in `var(--blog-border-color)` in `:root`
- **Variable Token (`--secondary`)**: `#d9d9d9` — grounded in `var(--secondary)` in `:root`
- **Variable Token (`--primary-hover`)**: `#ff9253` — grounded in `var(--primary-hover)` in `:root`
- **Variable Token (`--border`)**: `#bcbcbc` — grounded in `var(--border)` in `:root`
- **Variable Token (`--muted-on-dark`)**: `#d2d2d2` — grounded in `var(--muted-on-dark)` in `:root`
- **Variable Token (`--light-grey`)**: `#939393` — grounded in `var(--light-grey)` in `:root`
- **Variable Token (`--light`)**: `#f4f4f4` — grounded in `var(--light)` in `:root`
- **Variable Token (`--ink`)**: `#1d1d1d` — grounded in `var(--ink)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×828px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1310px` (measured widest bounded `<section>` landmark width on `1440px` desktop)
- **Padding & Gutters**: `64.8px` lateral canvas padding with `17.28px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1310px`, `gap: 17.28px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `64.8px` horizontal padding
- **Media Queries**: `@media (min-width:640px)`, `@media (max-width:960px)`, `@media (max-width:720px)`, `@media (max-width:767px)`
- **Corner Radii**: `50%`, `9999px`, `.25rem`, `9px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `aeonikPro`
- **Body Font Stack**: `avenirNext`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **H1 Display Rule**: live computed `h1` (`font-size: 92.16px`, `line-height: 103.219px`, `font-weight: 400`, `letter-spacing: -3.2256px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`; rule `h1` (`font-size: 2.5rem`, `line-height: 1.2`, `letter-spacing: -.025em`, `font-weight: 700`)
- **H2 Section Rule**: live computed `h2` (`font-size: 66.24px`, `line-height: 76.176px`, `font-weight: 400`, `letter-spacing: -2.3184px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 1.75rem`, `line-height: 1.3`, `font-weight: 700`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`); CSS variables `--font-plex-mono: "IBM Plex Mono","IBM Plex Mono Fallback"`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `vault-hyperiux-com` (`Hyperiux Vault - React & Next.js Interaction Effects.`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.z-900> — `vault-hyperiux-com`)**:
   - DOM & Selectors: Landmark `<nav class="z-900 top-0">` (`427x164px`) hosting `Hyperiux Vault - React & Next.js Int` navigation (`Docs D o c s Docs · Blog B l o g Blog`), DOM attributes (`data-sidebar="expanded"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.__className_644730 { font-family:aeonikPro,aeonikPro Fallback }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.z-900> — `vault-hyperiux-com`)` (`vault-hyperiux-com`) adapts across `@media (min-width:640px)`, `@media (max-width:960px)`, `@media (max-width:720px)`, `@media (max-width:767px)` with `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Docs D o c s Docs · Blog B l o g Blog`.
2. **Hero Stage & Focal Lead (<section.relative> — `The Interaction Layer Your Website`)**:
   - DOM & Selectors: Landmark `<section class="relative z-10">` presenting display lead `The Interaction Layer Your Website Is Missing.` and copy excerpt *"Source-first scroll systems, cursor effects, text reveals, page t"* over `#111111` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1280×828px` desktop / `390×2616px` mobile) sets `#111111` background with `#ffffff` headline `The Interaction Layer Your Website Is Missing.`.
3. **Primary Showcase & Content Grid (<section.section-x> — `The Interaction Layer Your Website`)**:
   - DOM & Selectors: Landmark `<section class="section-x text-ink">` rendering section `The Interaction Layer Your Website Is Missing .` with copy *"Read Docs R e a d D o c s Read Docs"*, asset references (`homepage-hero.webp`, `45c5b69ac3104145.css`, `b68a34d2a9030372.css`, `ee41bfcc83e4e14b.css`), and grid rule `.__variable_644730 { --font-aeonik:"aeonikPro","aeonikPro Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.section-x> — `The Interaction Layer Your Website`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1310px`, `gap: 17.28px`) on desktop and Single-column vertical stack at `390px` viewport width with `64.8px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.flex> — `Read Docs R e a d D o c s Read Doc`)**:
   - DOM & Selectors: Landmark `<article class="flex flex-col">` framing `Read Docs R e a d D o c s Read Docs` and `Browse All Effects B r o w s e A l l E f f e c t` (*"Browse All Effects B r o w s e A l l E f f e c t s Browse All Eff"*) with `#161616` surface cards, `#ff5f00` accents, and `.__className_617731 { font-family:avenirNext,avenirNext Fallback }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.flex> — `Read Docs R e a d D o c s Read Doc`)` uses `50%`, `9999px`, `.25rem`, `9px` radii, `#ff5f00` highlights, and assets (homepage-hero.webp, 45c5b69ac3104145.css, b68a34d2a9030372.css).
5. **Colophon & Global Directory Footer (<footer.z-200> — `https://vault.hyperiux.com`)**:
   - DOM & Selectors: Landmark `<footer class="z-200 overflow-x-clip">` anchoring `Hyperiux Vault - React & Next.js` footer links (`Docs D o c s Docs · Blog B l o g Blog`), copy *"Browse All Effects"*, and `#272727` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.z-200> — `https://vault.hyperiux.com`)` aligns to `1310px` (measured widest bounded `<section>` landmark width on `1440px` desktop) with `64.8px` lateral canvas padding with `17.28px` grid gap and attributes (data-sidebar="expanded", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Source-first scroll systems, cursor effects, text reveals, page transitions, loade..."*
- Copy Excerpt 2: *"Read Docs R e a d D o c s Read Docs"*
- Copy Excerpt 3: *"Browse All Effects B r o w s e A l l E f f e c t s Browse All Effects"*
- Copy Excerpt 4: *"Browse All Effects"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`vault-hyperiux-com`)**:
- `.__className_644730 { font-family:aeonikPro,aeonikPro Fallback }`
- `.__variable_644730 { --font-aeonik:"aeonikPro","aeonikPro Fallback" }`
- `.__className_617731 { font-family:avenirNext,avenirNext Fallback }`
- `.__variable_617731 { --font-avenir:"avenirNext","avenirNext Fallback" }`
- `.__className_542b9b { font-family:IBM Plex Mono,IBM Plex Mono Fallback;font-style:normal }`
- **Per-Selector Transition Rules**:
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `vault-hyperiux-com` stylesheet.
- **Selector `layer theme`**: `transition: .15s` extracted from `vault-hyperiux-com` stylesheet.
- **Selector `.codeblock) *)`**: `transition: opacity .15s` extracted from `vault-hyperiux-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<nav.z-900>` and `<section.section-x>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `13140px` across 1 distinct viewport chapters.
- **Vertical Chapter Sequence**: The Interaction Layer Your... (0%).

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `vault-hyperiux-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | The Interaction Layer Your Website Is Missing. | `1` | [desktop-step-01.webp](assets/desktop-step-01.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | The Interaction Layer Your Website Is Mis... | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `6594px` | `50%` | Explore the Moments Your Website is Missing. | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `13189px` | `100%` | Footer | [mobile-step-03.webp](assets/mobile-step-03.webp) |

