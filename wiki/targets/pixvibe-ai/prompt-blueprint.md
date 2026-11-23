---
title: "UI Prompt Blueprint: pixvibe-ai"
date: 2026-11-23
captured_at: 2026-11-23
target: "pixvibe-ai"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier2_webgl
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#0000ff`)"
---

# UI Design System & Master Generation Blueprint: pixvibe-ai

> **PixVibe — Free Background Remover, Converter & Upscaler** (https://pixvibe.ai) — Remove backgrounds, convert, compress, resize, crop and upscale images — free, batch up to 20 at once, right in your browser.

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **PixVibe — Free Background Remover, Converter & Upscaler** (`https://pixvibe.ai`). Remove backgrounds, convert, compress, resize, crop and upscale images — free, batch up to 20 at once, right in your browser.
- **Capture Provenance**: Live browser capture (`tier2_webgl`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#0000ff`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#18172d` primary typography and `#0000ff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `fontJakarta` for display copy (`The private image toolkit for you an`) with `fontInter` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1418px` container bounds (`gap: 16px`, padding `20px`) with `cubic-bezier(0,0,.2,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x844)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×844px` (`assets/mobile.png`, single-viewport 100vh live capture (844px)).
- **Master Container Bounds**: `1418px` (measured widest bounded `<section>` landmark width on `1440px` desktop).
- **Canvas Lateral Padding & Spacing**: `20px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `.25rem`, `var(--radius-4xl)`, `var(--radius-lg)`, `var(--radius-md)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1418px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `20px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:700px)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#18172d` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#bdbdbd` | `var(--tool-background-gray)` in `:root` |
| **Interactive Accent / Highlight** | `#0000ff` | `.uikit-button-ai { background: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#4d94ff` | `var(--color-secondary)` in `:root` |
| **Structural Hairline Border** | `#e7e9f0` | `var(--module-line)` in `:root` |
| **Variable Token (`--color-primary`)** | `#9b6dff` | `var(--color-primary)` in `:root` |
| **Variable Token (`--pv-bone`)** | `#f0ebe1` | `var(--pv-bone)` in `:root` |
| **Variable Token (`--pv-sheet`)** | `#faf6f0` | `var(--pv-sheet)` in `:root` |
| **Variable Token (`--pv-ink`)** | `#1b1620` | `var(--pv-ink)` in `:root` |
| **Variable Token (`--pv-violet`)** | `#7c3aed` | `var(--pv-violet)` in `:root` |
| **Variable Token (`--pv-fuchsia`)** | `#d946ef` | `var(--pv-fuchsia)` in `:root` |
| **Variable Token (`--pv-coral`)** | `#fb7185` | `var(--pv-coral)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-primary` | `#9b6dff` | Brand / Palette Token |
| `--color-primary-dark` | `#9b6dff` | Canvas / Surface Token |
| `--color-secondary` | `#4d94ff` | Brand / Palette Token |
| `--gradient-primary` | `linear-gradient(135deg, #9b6dff, #4d94ff)` | Brand / Palette Token |
| `--pv-bone` | `#f0ebe1` | Color / Atmospheric Token |
| `--pv-sheet` | `#faf6f0` | Color / Atmospheric Token |
| `--pv-card` | `#fff` | Color / Atmospheric Token |
| `--pv-ink` | `#1b1620` | Typography Ink Token |
| `--pv-muted` | `#1b16209e` | Color / Atmospheric Token |
| `--pv-faint` | `#1b16206b` | Color / Atmospheric Token |
| `--pv-violet` | `#7c3aed` | Color / Atmospheric Token |
| `--pv-fuchsia` | `#d946ef` | Color / Atmospheric Token |
| `--pv-coral` | `#fb7185` | Color / Atmospheric Token |
| `--pv-line` | `#1b16201a` | Color / Atmospheric Token |
| `--pv-line-2` | `#1b16200f` | Color / Atmospheric Token |
| `--pv-grad` | `linear-gradient(100deg,#7c3aed 0%,#d946ef 48%,#fb7185 100%)` | Color / Atmospheric Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `fontJakarta`.
- **Primary Body Stack**: `fontInter`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 78px`, `line-height: 78px`, `font-weight: 700`, `letter-spacing: -4px`); CSS variables `--pv-font-display: "Clash Display",system-ui,sans-serif`, `--tool-hero-title-badge-font-size: 12px`, `--text-display: 68px`; rule `h1` (`font-size: clamp(28px,7vw,40px)`).
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 20px`, `line-height: 28px`, `font-weight: 600`, `letter-spacing: -0.8px`); rule `h2` (`font-size: clamp(21px,1.9vw,26px)`, `line-height: 1.25`, `letter-spacing: -.02em`, `font-weight: 600`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--pv-font-body: "Satoshi",system-ui,sans-serif`, `--body: var(--font-inter), Inter, ui-sans-serif, system-ui, sans-serif`, `--text-base: 1rem`; rule `p` (`font-size: clamp(15px,1.1vw,16.5px)`, `line-height: 1.8`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--tool-processing-label-size: 10px`, `--tool-hero-label-height: 36px`, `--tool-hero-label-font-size: 14px`; rule `small` (`font-size: 12px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `pixvibe-ai` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `pixvibe-ai` stylesheet.
- **Selector `.transition-all`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `pixvibe-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.pv-notification-header>` and `<section.home-section>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — PixVibe — Free Background Remover, Convert │
│ ====================================================================== │
│ [ <header.pv-notificatio (419x65px)   | Home · Pricing · Blog        ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.home-hero> (w=1440px)                         | │
│ | H1: The private image toolkit for you and your AI age...           | │
│ | Substrate: #ffffff | Ink: #18172d | Accent: #0000ff                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.home-section>) max-w: 1418px               | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Free image tools             |  | Background Remover           | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.home-tool-group>) — Image Converter        | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>) | https://pixvibe.ai                   │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.pv-notification-) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.home-hero>) — 390px Vertical Lead             | │
│ | H1: The private image toolkit for you and your AI age...           | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.home-section>) — 1-Col Stack              | │
│ | [ Item 1: Free image tools                                       ] | │
│ | [ Item 2: Background Remover                                     ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.home-tool-group) — 1-Col (Image Converter)  | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.pv-notification-header> — `pixvibe-ai`)**:
   - Landmark `<header class="pv-notification-header">` (`419x65px`) hosting `PixVibe — Free Background Remover, C` navigation (`Home · Pricing · Blog`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `root { --fv-section-x:16px;--fv-section-top:12px;--fv-section-y:20px }`.
2. **Hero Stage & Focal Lead (<section.home-hero> — `The private image toolkit for you `)**:
   - Landmark `<section class="home-hero">` presenting display lead `The private image toolkit for you and your AI age...` and copy excerpt *"Full guide for AI agents, with shortcut URLs and parameters for e"* over `#ffffff` canvas and `#18172d` ink.
3. **Primary Showcase & Content Grid (<section.home-section> — `Free image tools`)**:
   - Landmark `<section class="home-section home-toolkit">` rendering section `Free image tools` with copy *"11 free tools · free batch processing · runs in your browser · pl"*, asset references (`dm_mono_400_latin-s.p.38hmww4cj4v...`, `dm_mono_500_latin-s.p.2yee423r7ah...`, `inter_400_700_latin-s.p.2bn3s6zvc...`, `manrope_400_700_latin-s.p.1sj6eob...`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.home-tool-group> — `Background Remover`)**:
   - Landmark `<section class="home-tool-group">` framing `Background Remover` and `Image Converter` (*"11 free tools · free batch processing · runs in your browser"*) with `#bdbdbd` surface cards, `#0000ff` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://pixvibe.ai`)**:
   - Landmark `<footer class="site-footer feedback-footer">` anchoring `PixVibe — Free Background Remove` footer links (`Home · Pricing · Blog`), copy *"· plus 3 Pro tools"*, and `#e7e9f0` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: pixvibe-ai (PixVibe — Free Background Remover, Converter & Upscaler)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `pixvibe-ai` (**PixVibe — Free Background Remover, Converter & Upscaler** — `https://pixvibe.ai`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#0000ff`).
- **Identity & Domain Context**: Remove backgrounds, convert, compress, resize, crop and upscale images — free, batch up to 20 at once, right in your browser.
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#18172d`, **Accent / Highlight**: `#0000ff`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#18172d` primary typography and `#0000ff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `fontJakarta` for display copy (`The private image toolkit for you an`) with `fontInter` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1418px` container bounds (`gap: 16px`, padding `20px`) with `cubic-bezier(0,0,.2,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `pixvibe-ai` in your global stylesheet:

:root {
  /* PixVibe — Free Background Remover, Converter & Upscaler (pixvibe-ai) — Live-Grounded CSS Variables */
  --color-primary: #9b6dff; /* Brand / Palette Token (pixvibe-ai) */
  --color-primary-dark: #9b6dff; /* Canvas / Surface Token (pixvibe-ai) */
  --color-secondary: #4d94ff; /* Brand / Palette Token (pixvibe-ai) */
  --gradient-primary: linear-gradient(135deg, #9b6dff, #4d94ff); /* Brand / Palette Token (pixvibe-ai) */
  --pv-bone: #f0ebe1; /* Color / Atmospheric Token (pixvibe-ai) */
  --pv-sheet: #faf6f0; /* Color / Atmospheric Token (pixvibe-ai) */
  --pv-card: #fff; /* Color / Atmospheric Token (pixvibe-ai) */
  --pv-ink: #1b1620; /* Typography Ink Token (pixvibe-ai) */
  --pv-muted: #1b16209e; /* Color / Atmospheric Token (pixvibe-ai) */
  --pv-faint: #1b16206b; /* Color / Atmospheric Token (pixvibe-ai) */
  --pv-violet: #7c3aed; /* Color / Atmospheric Token (pixvibe-ai) */
  --pv-fuchsia: #d946ef; /* Color / Atmospheric Token (pixvibe-ai) */
  --pv-coral: #fb7185; /* Color / Atmospheric Token (pixvibe-ai) */
  --pv-line: #1b16201a; /* Color / Atmospheric Token (pixvibe-ai) */
  --pv-line-2: #1b16200f; /* Color / Atmospheric Token (pixvibe-ai) */
  --pv-grad: linear-gradient(100deg,#7c3aed 0%,#d946ef 48%,#fb7185 100%); /* Color / Atmospheric Token (pixvibe-ai) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#18172d` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#bdbdbd` — grounded in `var(--tool-background-gray)` in `:root`
- **Interactive Accent / Highlight**: `#0000ff` — grounded in `.uikit-button-ai { background: blue }` (`#0000ff`)
- **Secondary / Muted Copy**: `#4d94ff` — grounded in `var(--color-secondary)` in `:root`
- **Structural Hairline Border**: `#e7e9f0` — grounded in `var(--module-line)` in `:root`
- **Variable Token (`--color-primary`)**: `#9b6dff` — grounded in `var(--color-primary)` in `:root`
- **Variable Token (`--pv-bone`)**: `#f0ebe1` — grounded in `var(--pv-bone)` in `:root`
- **Variable Token (`--pv-sheet`)**: `#faf6f0` — grounded in `var(--pv-sheet)` in `:root`
- **Variable Token (`--pv-ink`)**: `#1b1620` — grounded in `var(--pv-ink)` in `:root`
- **Variable Token (`--pv-violet`)**: `#7c3aed` — grounded in `var(--pv-violet)` in `:root`
- **Variable Token (`--pv-fuchsia`)**: `#d946ef` — grounded in `var(--pv-fuchsia)` in `:root`
- **Variable Token (`--pv-coral`)**: `#fb7185` — grounded in `var(--pv-coral)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×844px` (single-viewport 100vh live capture (844px), `390px` standard mobile width).
- **Container Max-Width**: `1418px` (measured widest bounded `<section>` landmark width on `1440px` desktop)
- **Padding & Gutters**: `20px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1418px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `20px` horizontal padding
- **Media Queries**: `@media (max-width:700px)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`
- **Corner Radii**: `.25rem`, `var(--radius-4xl)`, `var(--radius-lg)`, `var(--radius-md)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `fontJakarta`
- **Body Font Stack**: `fontInter`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: live computed `h1` (`font-size: 78px`, `line-height: 78px`, `font-weight: 700`, `letter-spacing: -4px`); CSS variables `--pv-font-display: "Clash Display",system-ui,sans-serif`, `--tool-hero-title-badge-font-size: 12px`, `--text-display: 68px`; rule `h1` (`font-size: clamp(28px,7vw,40px)`)
- **H2 Section Rule**: live computed `h3 (primary section heading)` (`font-size: 20px`, `line-height: 28px`, `font-weight: 600`, `letter-spacing: -0.8px`); rule `h2` (`font-size: clamp(21px,1.9vw,26px)`, `line-height: 1.25`, `letter-spacing: -.02em`, `font-weight: 600`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--pv-font-body: "Satoshi",system-ui,sans-serif`, `--body: var(--font-inter), Inter, ui-sans-serif, system-ui, sans-serif`, `--text-base: 1rem`; rule `p` (`font-size: clamp(15px,1.1vw,16.5px)`, `line-height: 1.8`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--tool-processing-label-size: 10px`, `--tool-hero-label-height: 36px`, `--tool-hero-label-font-size: 14px`; rule `small` (`font-size: 12px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `pixvibe-ai` (`PixVibe — Free Background Remover, Converter & Upscaler`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.pv-notification-header> — `pixvibe-ai`)**:
   - DOM & Selectors: Landmark `<header class="pv-notification-header">` (`419x65px`) hosting `PixVibe — Free Background Remover, C` navigation (`Home · Pricing · Blog`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `root { --fv-section-x:16px;--fv-section-top:12px;--fv-section-y:20px }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.pv-notification-header> — `pixvibe-ai`)` (`pixvibe-ai`) adapts across `@media (max-width:700px)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Home · Pricing · Blog`.
2. **Hero Stage & Focal Lead (<section.home-hero> — `The private image toolkit for you `)**:
   - DOM & Selectors: Landmark `<section class="home-hero">` presenting display lead `The private image toolkit for you and your AI age...` and copy excerpt *"Full guide for AI agents, with shortcut URLs and parameters for e"* over `#ffffff` canvas and `#18172d` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×844px` mobile) sets `#ffffff` background with `#18172d` headline `The private image toolkit for you and your AI age...`.
3. **Primary Showcase & Content Grid (<section.home-section> — `Free image tools`)**:
   - DOM & Selectors: Landmark `<section class="home-section home-toolkit">` rendering section `Free image tools` with copy *"11 free tools · free batch processing · runs in your browser · pl"*, asset references (`dm_mono_400_latin-s.p.38hmww4cj4v...`, `dm_mono_500_latin-s.p.2yee423r7ah...`, `inter_400_700_latin-s.p.2bn3s6zvc...`, `manrope_400_700_latin-s.p.1sj6eob...`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.home-section> — `Free image tools`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1418px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `20px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.home-tool-group> — `Background Remover`)**:
   - DOM & Selectors: Landmark `<section class="home-tool-group">` framing `Background Remover` and `Image Converter` (*"11 free tools · free batch processing · runs in your browser"*) with `#bdbdbd` surface cards, `#0000ff` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.home-tool-group> — `Background Remover`)` uses `.25rem`, `var(--radius-4xl)`, `var(--radius-lg)`, `var(--radius-md)` radii, `#0000ff` highlights, and assets (dm_mono_400_latin-s.p.38hmww4cj4v..., dm_mono_500_latin-s.p.2yee423r7ah..., inter_400_700_latin-s.p.2bn3s6zvc...).
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://pixvibe.ai`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer feedback-footer">` anchoring `PixVibe — Free Background Remove` footer links (`Home · Pricing · Blog`), copy *"· plus 3 Pro tools"*, and `#e7e9f0` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-footer> — `https://pixvibe.ai`)` aligns to `1418px` (measured widest bounded `<section>` landmark width on `1440px` desktop) with `20px` lateral canvas padding with `16px` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Full guide for AI agents, with shortcut URLs and parameters for each task on this..."*
- Copy Excerpt 2: *"11 free tools · free batch processing · runs in your browser · plus 3 Pro tools"*
- Copy Excerpt 3: *"11 free tools · free batch processing · runs in your browser"*
- Copy Excerpt 4: *"· plus 3 Pro tools"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`pixvibe-ai`)**:
- `root { --fv-section-x:16px;--fv-section-top:12px;--fv-section-y:20px }`
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `pixvibe-ai` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `pixvibe-ai` stylesheet.
- **Selector `.transition-all`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `pixvibe-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.pv-notification-header>` and `<section.home-section>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `pixvibe-ai`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
