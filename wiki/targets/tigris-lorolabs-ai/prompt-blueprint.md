---
title: "UI Prompt Blueprint: tigris-lorolabs-ai"
date: 2026-11-24
captured_at: 2026-11-24
target: "tigris-lorolabs-ai"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: native
desktop_keyframes: 8
subpages_crawled: 0
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#20060e` / `#f2d38a`)"
---

# UI Design System & Master Generation Blueprint: tigris-lorolabs-ai

> **TIGRIS · Instinct, in Its Rarest Form** (https://tigris.lorolabs.ai/) — Maison Tigris. Sculptural high jewellery in gold, rubies and diamonds. Discover the collection and explore a private viewing.

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **TIGRIS · Instinct, in Its Rarest Form** (`https://tigris.lorolabs.ai/`). Maison Tigris. Sculptural high jewellery in gold, rubies and diamonds. Discover the collection and explore a private viewing.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#20060e` / `#f2d38a`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#20060e` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#f5e9d6` primary typography and `#f2d38a` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Bodoni Moda` for display copy (`TIGRIS`) with `Space Grotesk`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 41.6px`, padding `57.6px`) with `cubic-bezier(.65,0,.35,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=14400px` / doc `18719px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `57.6px` lateral canvas padding with `41.6px` grid gap.
- **Border Radius Scale**: `32px`, `2rem`, `16px`, `8px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 41.6px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `57.6px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:600px)`, `@media (max-width:767px)`, `@media (max-width:768px)`, `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#20060e` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f5e9d6` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#200610` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#f2d38a` | live computed `a` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#4a0e1a` | live computed `h2` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#201c17` | `.loro-study-consent button { border: #201c17 }` |
| **Variable Token (`--oxblood`)** | `#24060e` | `var(--oxblood)` in `:root` |
| **Variable Token (`--void`)** | `#120309` | `var(--void)` in `:root` |
| **Variable Token (`--gold`)** | `#c9a24a` | `var(--gold)` in `:root` |
| **Variable Token (`--ruby`)** | `#9b1b30` | `var(--ruby)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--burgundy` | `#4a0e1a` | Color / Atmospheric Token |
| `--oxblood` | `#24060e` | Color / Atmospheric Token |
| `--void` | `#120309` | Color / Atmospheric Token |
| `--gold` | `#c9a24a` | Color / Atmospheric Token |
| `--gold-hi` | `#f2d38a` | Color / Atmospheric Token |
| `--ruby` | `#9b1b30` | Color / Atmospheric Token |
| `--cream` | `#f5e9d6` | Color / Atmospheric Token |
| `--serif` | `"Bodoni Moda", "Didot", serif` | Typography / Scale Token |
| `--grot` | `"Space Grotesk", system-ui, sans-serif` | Dimension / Scale Token |
| `--tigris-lorolabs--bg` | `#20060e` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--tigris-lorolabs--ink` | `#f5e9d6` | Primary Typography Ink (computed-derived) |
| `--tigris-lorolabs--surface` | `#200610` | Surface Substrate (computed-derived) |
| `--tigris-lorolabs--accent` | `#f2d38a` | Interactive Accent (computed-derived) |
| `--tigris-lorolabs--muted` | `#4a0e1a` | Secondary Ink (computed-derived) |
| `--tigris-lorolabs--border` | `#201c17` | Structural Border (computed-derived) |
| `--tigris-lorolabs--container` | `1440px` | Container Bound (computed-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Bodoni Moda`.
- **Primary Body Stack**: `Space Grotesk`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 227.52px`, `line-height: 216.144px`, `font-weight: 600`, `letter-spacing: 7.9632px`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 273.6px`, `line-height: 246.24px`, `font-weight: 800`, `letter-spacing: 5.472px`); rule `h2` (`letter-spacing: 0`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 300`); rule `p` (`font-size: .75rem`, `letter-spacing: .22em`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 11.52px`, `line-height: normal`, `font-weight: 300`, `letter-spacing: 3.2256px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.65,0,.35,1)`, `cubic-bezier(.22,1,.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.nav__links a:after`**: `transition: transform .45s cubic-bezier(.65,0,.35,1)` extracted from `tigris-lorolabs-ai` stylesheet.
- **Selector `.variants__btn`**: `transition: background .4s ease,color .4s ease,border-color .4s ease` extracted from `tigris-lorolabs-ai` stylesheet.
- **Selector `.card`**: `transition: opacity .5s ease` extracted from `tigris-lorolabs-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.65,0,.35,1)`)**: Governs interactive state transitions across `<header.nav>` and `<section.manifesto>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `18719px`, deepest scrollY reached `14400px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `Lenis`, `GSAP/ScrollTrigger`, `WebGL/Canvas`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — TIGRIS · Instinct, in Its Rarest Form      │
│ ====================================================================== │
│ [ <header.nav> (1440x88px)            | Collection · Heritage · Acqu ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero> (w=1440px)                              | │
│ | H1: TIGRIS                                                         | │
│ | Substrate: #20060e | Ink: #f5e9d6 | Accent: #f2d38a                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.manifesto>) max-w: 1440px                  | │
│ | +------------------------------+  +------------------------------+ | │
│ | | A stripe, held in gold.      |  | Power, unbroken.             | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.stripes>) — From Gold to Enamel            | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>     ) | https://tigris.lorolabs.ai/          │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 41.6px)     │
│ ====================================================================== │
│ [ HEADER BAR (<header.nav>            ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.hero>) — 390px Vertical Lead                  | │
│ | H1: TIGRIS                                                         | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.manifesto>) — 1-Col Stack                 | │
│ | [ Item 1: A stripe, held in gold.                                ] | │
│ | [ Item 2: Power, unbroken.                                       ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.stripes>) — 1-Col (From Gold to Ename)      | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>     ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.nav> — `tigris-lorolabs-ai`)**:
   - Landmark `<header class="nav">` (`1440x88px`) hosting `TIGRIS · Instinct, in Its Rarest For` navigation (`Collection · Heritage · Acquire`), DOM attributes (`data-hover`, `data-variant="gold"`, `data-variant="enamel"`, `data-variant="pave"`), and stylesheet rule `.loro-study-panel h2 { margin:12px 24px 14px 0;font:400 18px/1.4 var(--grot,Arial,sans-serif);l... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `TIGRIS`)**:
   - Landmark `<section class="hero">` presenting display lead `TIGRIS` and copy excerpt *"Instinct, in its rarest form."* over `#20060e` canvas and `#f5e9d6` ink.
3. **Primary Showcase & Content Grid (<section.manifesto> — `A stripe, held in gold.`)**:
   - Landmark `<section class="manifesto">` rendering section `A stripe, held in gold.` with copy *"Scroll to discover"*, asset references (`manifest.webmanifest`, `icon-192.png`, `bodoni-moda-latin-normal.woff2`, `space-grotesk-latin-normal.woff2`), and grid rule `.loro-study-panel p { margin:0 0 14px }`.
4. **Interactive Detail & Feature Matrix (<section.stripes> — `Power, unbroken.`)**:
   - Landmark `<section class="stripes">` framing `Power, unbroken.` and `From Gold to Enamel` (*"A stripe, remembered in gold."*) with `#200610` surface cards, `#f2d38a` accents, and `.loro-study-panel a { color:inherit;text-decoration:underline;text-underline-offset:4px }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://tigris.lorolabs.ai/`)**:
   - Landmark `<footer class="footer">` anchoring `TIGRIS · Instinct, in Its Rarest` footer links (`Collection · Heritage · Acquire`), copy *"Our story begins at dusk. A tiger crosses the river; its str"*, and `#201c17` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `TIGRIS` · sticky/fixed elements: `4`
- **Step 02** (`y=850px`, `5%`): Active landmark `#manifesto` · sticky/fixed elements: `4`
- **Step 03** (`y=3400px`, `19%`): Active landmark `The Stripes` · sticky/fixed elements: `4`
- **Step 04** (`y=5950px`, `33%`): Active landmark `Stripe` · sticky/fixed elements: `3`
- **Step 05** (`y=8500px`, `48%`): Active landmark `From Gold to Enamel` · sticky/fixed elements: `4`
- **Step 06** (`y=11050px`, `62%`): Active landmark `Inside the ruby.` · sticky/fixed elements: `3`
- **Step 07** (`y=13600px`, `76%`): Active landmark `The Hunt` · sticky/fixed elements: `4`
- **Step 08** (`y=14400px`, `81%`): Active landmark `BORN DARK` · sticky/fixed elements: `4`

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: tigris-lorolabs-ai (TIGRIS · Instinct, in Its Rarest Form)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `tigris-lorolabs-ai` (**TIGRIS · Instinct, in Its Rarest Form** — `https://tigris.lorolabs.ai/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#20060e` / `#f2d38a`).
- **Identity & Domain Context**: Maison Tigris. Sculptural high jewellery in gold, rubies and diamonds. Discover the collection and explore a private viewing.
- **Primary Substrate**: `#20060e` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#f5e9d6`, **Accent / Highlight**: `#f2d38a`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#20060e` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#f5e9d6` primary typography and `#f2d38a` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Bodoni Moda` for display copy (`TIGRIS`) with `Space Grotesk`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 41.6px`, padding `57.6px`) with `cubic-bezier(.65,0,.35,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `tigris-lorolabs-ai` in your global stylesheet:

:root {
  /* TIGRIS · Instinct, in Its Rarest Form (tigris-lorolabs-ai) — Live-Grounded CSS Variables */
  --burgundy: #4a0e1a; /* Color / Atmospheric Token (tigris-lorolabs-ai) */
  --oxblood: #24060e; /* Color / Atmospheric Token (tigris-lorolabs-ai) */
  --void: #120309; /* Color / Atmospheric Token (tigris-lorolabs-ai) */
  --gold: #c9a24a; /* Color / Atmospheric Token (tigris-lorolabs-ai) */
  --gold-hi: #f2d38a; /* Color / Atmospheric Token (tigris-lorolabs-ai) */
  --ruby: #9b1b30; /* Color / Atmospheric Token (tigris-lorolabs-ai) */
  --cream: #f5e9d6; /* Color / Atmospheric Token (tigris-lorolabs-ai) */
  --serif: "Bodoni Moda", "Didot", serif; /* Typography / Scale Token (tigris-lorolabs-ai) */
  --grot: "Space Grotesk", system-ui, sans-serif; /* Dimension / Scale Token (tigris-lorolabs-ai) */
  --tigris-lorolabs--bg: #20060e; /* Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) (tigris-lorolabs-ai) */
  --tigris-lorolabs--ink: #f5e9d6; /* Primary Typography Ink (computed-derived) (tigris-lorolabs-ai) */
  --tigris-lorolabs--surface: #200610; /* Surface Substrate (computed-derived) (tigris-lorolabs-ai) */
  --tigris-lorolabs--accent: #f2d38a; /* Interactive Accent (computed-derived) (tigris-lorolabs-ai) */
  --tigris-lorolabs--muted: #4a0e1a; /* Secondary Ink (computed-derived) (tigris-lorolabs-ai) */
  --tigris-lorolabs--border: #201c17; /* Structural Border (computed-derived) (tigris-lorolabs-ai) */
  --tigris-lorolabs--container: 1440px; /* Container Bound (computed-derived) (tigris-lorolabs-ai) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#20060e` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#f5e9d6` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#200610` — grounded in live computed `button` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#f2d38a` — grounded in live computed `a` `background-color` (`computed_styles.json`)
- **Secondary / Muted Copy**: `#4a0e1a` — grounded in live computed `h2` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#201c17` — grounded in `.loro-study-consent button { border: #201c17 }`
- **Variable Token (`--oxblood`)**: `#24060e` — grounded in `var(--oxblood)` in `:root`
- **Variable Token (`--void`)**: `#120309` — grounded in `var(--void)` in `:root`
- **Variable Token (`--gold`)**: `#c9a24a` — grounded in `var(--gold)` in `:root`
- **Variable Token (`--ruby`)**: `#9b1b30` — grounded in `var(--ruby)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `57.6px` lateral canvas padding with `41.6px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 41.6px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `57.6px` horizontal padding
- **Media Queries**: `@media (max-width:600px)`, `@media (max-width:767px)`, `@media (max-width:768px)`, `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `32px`, `2rem`, `16px`, `8px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Bodoni Moda`
- **Body Font Stack**: `Space Grotesk`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 227.52px`, `line-height: 216.144px`, `font-weight: 600`, `letter-spacing: 7.9632px`)
- **H2 Section Rule**: live computed `h2` (`font-size: 273.6px`, `line-height: 246.24px`, `font-weight: 800`, `letter-spacing: 5.472px`); rule `h2` (`letter-spacing: 0`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 300`); rule `p` (`font-size: .75rem`, `letter-spacing: .22em`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 11.52px`, `line-height: normal`, `font-weight: 300`, `letter-spacing: 3.2256px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `tigris-lorolabs-ai` (`TIGRIS · Instinct, in Its Rarest Form`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.nav> — `tigris-lorolabs-ai`)**:
   - DOM & Selectors: Landmark `<header class="nav">` (`1440x88px`) hosting `TIGRIS · Instinct, in Its Rarest For` navigation (`Collection · Heritage · Acquire`), DOM attributes (`data-hover`, `data-variant="gold"`, `data-variant="enamel"`, `data-variant="pave"`), and stylesheet rule `.loro-study-panel h2 { margin:12px 24px 14px 0;font:400 18px/1.4 var(--grot,Arial,sans-serif);l... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.nav> — `tigris-lorolabs-ai`)` (`tigris-lorolabs-ai`) adapts across `@media (max-width:600px)`, `@media (max-width:767px)`, `@media (max-width:768px)`, `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(.65,0,.35,1)`, `cubic-bezier(.22,1,.36,1)` transitions and links `Collection · Heritage · Acquire`.
2. **Hero Stage & Focal Lead (<section.hero> — `TIGRIS`)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `TIGRIS` and copy excerpt *"Instinct, in its rarest form."* over `#20060e` canvas and `#f5e9d6` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#20060e` background with `#f5e9d6` headline `TIGRIS`.
3. **Primary Showcase & Content Grid (<section.manifesto> — `A stripe, held in gold.`)**:
   - DOM & Selectors: Landmark `<section class="manifesto">` rendering section `A stripe, held in gold.` with copy *"Scroll to discover"*, asset references (`manifest.webmanifest`, `icon-192.png`, `bodoni-moda-latin-normal.woff2`, `space-grotesk-latin-normal.woff2`), and grid rule `.loro-study-panel p { margin:0 0 14px }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.manifesto> — `A stripe, held in gold.`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 41.6px`) on desktop and Single-column vertical stack at `390px` viewport width with `57.6px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.stripes> — `Power, unbroken.`)**:
   - DOM & Selectors: Landmark `<section class="stripes">` framing `Power, unbroken.` and `From Gold to Enamel` (*"A stripe, remembered in gold."*) with `#200610` surface cards, `#f2d38a` accents, and `.loro-study-panel a { color:inherit;text-decoration:underline;text-underline-offset:4px }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.stripes> — `Power, unbroken.`)` uses `32px`, `2rem`, `16px`, `8px` radii, `#f2d38a` highlights, and assets (manifest.webmanifest, icon-192.png, bodoni-moda-latin-normal.woff2).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://tigris.lorolabs.ai/`)**:
   - DOM & Selectors: Landmark `<footer class="footer">` anchoring `TIGRIS · Instinct, in Its Rarest` footer links (`Collection · Heritage · Acquire`), copy *"Our story begins at dusk. A tiger crosses the river; its str"*, and `#201c17` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://tigris.lorolabs.ai/`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `57.6px` lateral canvas padding with `41.6px` grid gap and attributes (data-hover, data-variant="gold", data-variant="enamel").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Instinct, in its rarest form."*
- Copy Excerpt 2: *"Scroll to discover"*
- Copy Excerpt 3: *"A stripe, remembered in gold."*
- Copy Excerpt 4: *"Our story begins at dusk. A tiger crosses the river; its stripes break into light..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.65,0,.35,1)`, `cubic-bezier(.22,1,.36,1)`
- **Extracted Stylesheet Rules (`tigris-lorolabs-ai`)**:
- `.loro-study-panel h2 { margin:12px 24px 14px 0;font:400 18px/1.4 var(--grot,Arial,sans-serif);l... }`
- `.loro-study-panel p { margin:0 0 14px }`
- `.loro-study-panel a { color:inherit;text-decoration:underline;text-underline-offset:4px }`
- `.loro-study-credit { padding-right:34px;color:c9ae70;font-size:10px;letter-spacing:.08em;text... }`
- `.loro-study-demo { font-size:12px;color:c8baa5 }`
- **Per-Selector Transition Rules**:
- **Selector `.nav__links a:after`**: `transition: transform .45s cubic-bezier(.65,0,.35,1)` extracted from `tigris-lorolabs-ai` stylesheet.
- **Selector `.variants__btn`**: `transition: background .4s ease,color .4s ease,border-color .4s ease` extracted from `tigris-lorolabs-ai` stylesheet.
- **Selector `.card`**: `transition: opacity .5s ease` extracted from `tigris-lorolabs-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.65,0,.35,1)`)**: Governs interactive state transitions across `<header.nav>` and `<section.manifesto>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `18719px` across 8 distinct viewport chapters using Lenis, GSAP/ScrollTrigger, WebGL/Canvas.
- **Vertical Chapter Sequence**: TIGRIS (0%) -> #manifesto (5%) -> The Stripes (19%) -> Stripe (33%) -> From Gold to Enamel (48%) -> Inside the ruby. (62%) -> The Hunt (76%) -> BORN DARK (81%).

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `tigris-lorolabs-ai`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | TIGRIS | `4` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `5%` | #manifesto | `4` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `3400px` | `19%` | The Stripes | `4` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `5950px` | `33%` | Stripe | `3` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `8500px` | `48%` | From Gold to Enamel | `4` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `11050px` | `62%` | Inside the ruby. | `3` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `13600px` | `76%` | The Hunt | `4` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `14400px` | `81%` | BORN DARK | `4` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | TIGRIS | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `7200px` | `50%` | Power, unbroken. | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `14400px` | `100%` | Find Your Signature | [mobile-step-03.webp](assets/mobile-step-03.webp) |

