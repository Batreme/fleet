---
title: "UI Prompt Blueprint: www-zzdp-nl"
date: 2026-11-24
captured_at: 2026-11-24
target: "www-zzdp-nl"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: native
desktop_keyframes: 8
subpages_crawled: 3
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#12366b` ink, `#ff2800` accent)"
---

# UI Design System & Master Generation Blueprint: www-zzdp-nl

> **Al meer dan 70 jaar betekenisvolle architectuur · ZZDP** (https://www.zzdp.nl/) — Bij ZZDP combineren we vakmanschap en visie in betekenisvolle architectuur. Met meer dan 70 jaar ervaring realiseren we ontwerpen waarin...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Al meer dan 70 jaar betekenisvolle architectuur · ZZDP** (`https://www.zzdp.nl/`). Bij ZZDP combineren we vakmanschap en visie in betekenisvolle architectuur. Met meer dan 70 jaar ervaring realiseren we ontwerpen waarin...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#12366b` ink, `#ff2800` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `html` `background-color` (`computed_styles.json`)) paired with `#12366b` primary typography and `#ff2800` accents.
  - **Grounded Typographic Hierarchy**: Uses `HelveticaNowDisplay` across display (`ZZDP`) and body copy.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 2.13333vw`, padding `2.66667vw`) with `cubic-bezier(.48,0,.03,1)` easing and Lenis Smooth Scroll (`data-lenis`), Lottie Vector Animation Player.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=14400px` / doc `18562px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `2.66667vw` lateral canvas padding with `2.13333vw` grid gap.
- **Border Radius Scale**: `10px`, `8px`, `50%`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 2.13333vw`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `2.66667vw` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:47.99em)`, `@media (min-width:48em)`, `@media (min-width:0)`, `@media (min-width:23.4375em)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#12366b` | live computed `p` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ebeae1` | live computed `section` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ff2800` | live computed `a` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#c7c6be` | `var(--secondary-ui-label-disabled-color)` in `:root` |
| **Structural Hairline Border** | `#b5b899` | `var(--primary-ui-stroke-hover-color)` in `:root` |
| **Variable Token (`--title-color`)** | `#656657` | `var(--title-color)` in `:root` |
| **Variable Token (`--line-color`)** | `#1a1630` | `var(--line-color)` in `:root` |
| **Variable Token (`--accent-color`)** | `#8746e3` | `var(--accent-color)` in `:root` |

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
- **Display Typography**: `HelveticaNowDisplay`.
- **Primary Body Stack**: `HelveticaNowDisplay`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 32px`, `line-height: 48px`, `font-weight: 700`); CSS variables `--font-helvetica-now-display: "helveticaNowDisplay", "helveticaNowDisplay Fallback"`; rule `h1` (`font-size: 13.3333vw`, `line-height: 82%`, `letter-spacing: -.07em`, `font-weight: 400`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 120px`, `line-height: 98.4px`, `font-weight: 400`, `letter-spacing: -8.4px`); rule `h2` (`font-size: 8vw`, `line-height: 105%`, `letter-spacing: .01em`, `font-weight: 400`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: 3.73333vw`, `line-height: 132%`, `letter-spacing: 0`, `font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.48,0,.03,1)`, `cubic-bezier(.5,0,0,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.c-scrollbar`**: `transition: transform .3s,opacity .3s` extracted from `www-zzdp-nl` stylesheet.
- **Selector `.u-underline-link:after`**: `transition: transform .3s cubic-bezier(.48,0,.03,1)` extracted from `www-zzdp-nl` stylesheet.
- **Selector `scss-module__gW1A4G__u-underline-...`**: `transition: transform .3s cubic-bezier(.48,0,.03,1)` extracted from `www-zzdp-nl` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.48,0,.03,1)`)**: Governs interactive state transitions across `<nav.lenis>` and `<section.vjs-styles-dimensions>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `18562px`, deepest scrollY reached `14400px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `Lenis`, `GSAP/ScrollTrigger`.
- **Route Transition Architecture**: First internal navigation (`/project/scarlet`) measured as `direct` in `3025ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Al meer dan 70 jaar betekenisvolle archite │
│ ====================================================================== │
│ [ <nav.lenis> (227x18px)              | Home · Projecten · Over ons  ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.theme--mossLight> (w=1440px)                  | │
│ | H1: ZZDP                                                           | │
│ | Substrate: #ffffff | Ink: #12366b | Accent: #ff2800                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.vjs-styles-dimens) max-w: 1440px           | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Bij ZZDP geloven wij dat arc |  | Gedreven door nalatenschap   | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.theme--white>) — Partners in design        | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.theme--white) | https://www.zzdp.nl/                 │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 2.13333v)   │
│ ====================================================================== │
│ [ HEADER BAR (<nav.lenis>             ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.theme--mossLigh) — 390px Vertical Lead        | │
│ | H1: ZZDP                                                           | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.vjs-styles-di) — 1-Col Stack              | │
│ | [ Item 1: Bij ZZDP geloven wij dat architectuur meer is dan...   ] | │
│ | [ Item 2: Gedreven door nalatenschap                             ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.theme--white>) — 1-Col (Partners in design) | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.theme--white) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.lenis> — `www-zzdp-nl`)**:
   - Landmark `<nav class="lenis">` (`227x18px`) hosting `Al meer dan 70 jaar betekenisvolle a` navigation (`Home · Projecten · Over ons · Nieuws en inzichten · Vacatures`), DOM attributes (`data-next-head`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`), and stylesheet rule `.u-underline-link:after { height:.266667vw }`.
2. **Hero Stage & Focal Lead (<section.theme--mossLight> — `ZZDP`)**:
   - Landmark `<section class="theme--mossLight">` presenting display lead `ZZDP` and copy excerpt *"We staan op de schouders van onze voorgangers. Met meer dan 70 ja"* over `#ffffff` canvas and `#12366b` ink.
3. **Primary Showcase & Content Grid (<section.vjs-styles-dimensions> — `Bij ZZDP geloven wij dat architect`)**:
   - Landmark `<section class="vjs-styles-dimensions">` rendering section `Bij ZZDP geloven wij dat architectuur meer is dan...` with copy *"Video Player is loading."*, asset references (`favicon.svg`, `HelveticaNowDisplay_Regular-s.p.1...`, `HelveticaNowDisplay_Md-s.p.16ns3u...`, `PPNeueMachina_PlainRegular-s.p.39...`), and grid rule `.default-in-animation { transform:translateY(26.6667vw) }`.
4. **Interactive Detail & Feature Matrix (<section.theme--white> — `Gedreven door nalatenschap`)**:
   - Landmark `<section class="theme--white">` framing `Gedreven door nalatenschap` and `Partners in design` (*"Seek to live, currently behind live"*) with `#ebeae1` surface cards, `#ff2800` accents, and `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;line-height:1.15 }`.
5. **Colophon & Global Directory Footer (<footer.theme--white> — `https://www.zzdp.nl/`)**:
   - Landmark `<footer class="theme--white">` anchoring `Al meer dan 70 jaar betekenisvol` footer links (`Home · Projecten · Over ons · Nieuws en inzichten · Vacatures`), copy *"descriptions off , selected"*, and `#b5b899` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `Hero` · sticky/fixed elements: `2`
- **Step 02** (`y=850px`, `5%`): Active landmark `Bij ZZDP geloven wij dat architectuur meer is dan...` · sticky/fixed elements: `2`
- **Step 03** (`y=3400px`, `19%`): Active landmark `Section @ 19%` · sticky/fixed elements: `2`
- **Step 04** (`y=5950px`, `34%`): Active landmark `ONS VERHAAL` · sticky/fixed elements: `2`
- **Step 05** (`y=8500px`, `48%`): Active landmark `ONS VERHAAL` · sticky/fixed elements: `2`
- **Step 06** (`y=11050px`, `63%`): Active landmark `ONZE GESCHIEDENIS` · sticky/fixed elements: `2`
- **Step 07** (`y=13600px`, `77%`): Active landmark `ONZE GESCHIEDENIS` · sticky/fixed elements: `2`
- **Step 08** (`y=14400px`, `82%`): Active landmark `ONZE GESCHIEDENIS` · sticky/fixed elements: `2`

### Multi-Page Internal Route Map
- **Detail Route (`/project/scarlet`)**: `https://www.zzdp.nl/project/scarlet` — H1: `SCARLET`, scrollHeight `14325px`, transition `direct` (`3025ms`)
- **About Route (`/contact`)**: `https://www.zzdp.nl/contact` — H1: `Laten we samen iets waardevols bouwen`, scrollHeight `6419px`, transition `direct` (`1828ms`)
- **Detail Route (`/project/pc-hoofstraat-7`)**: `https://www.zzdp.nl/project/pc-hoofstraat-7` — H1: `PC-HOOFTSTRAAT 7`, scrollHeight `15468px`, transition `direct` (`1048ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-zzdp-nl (Al meer dan 70 jaar betekenisvolle architectuur · ZZDP)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-zzdp-nl` (**Al meer dan 70 jaar betekenisvolle architectuur · ZZDP** — `https://www.zzdp.nl/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#12366b` ink, `#ff2800` accent).
- **Identity & Domain Context**: Bij ZZDP combineren we vakmanschap en visie in betekenisvolle architectuur. Met meer dan 70 jaar ervaring realiseren we ontwerpen waarin...
- **Primary Substrate**: `#ffffff` (live computed `html` `background-color` (`computed_styles.json`)), **Primary Ink**: `#12366b`, **Accent / Highlight**: `#ff2800`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `html` `background-color` (`computed_styles.json`)) paired with `#12366b` primary typography and `#ff2800` accents.
  - **Grounded Typographic Hierarchy**: Uses `HelveticaNowDisplay` across display (`ZZDP`) and body copy.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 2.13333vw`, padding `2.66667vw`) with `cubic-bezier(.48,0,.03,1)` easing and Lenis Smooth Scroll (`data-lenis`), Lottie Vector Animation Player.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-zzdp-nl` in your global stylesheet:

:root {
  /* Al meer dan 70 jaar betekenisvolle architectuur · ZZDP (www-zzdp-nl) — Live-Grounded CSS Variables */
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
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `html` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#12366b` — grounded in live computed `p` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#ebeae1` — grounded in live computed `section` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#ff2800` — grounded in live computed `a` `background-color` (`computed_styles.json`)
- **Secondary / Muted Copy**: `#c7c6be` — grounded in `var(--secondary-ui-label-disabled-color)` in `:root`
- **Structural Hairline Border**: `#b5b899` — grounded in `var(--primary-ui-stroke-hover-color)` in `:root`
- **Variable Token (`--title-color`)**: `#656657` — grounded in `var(--title-color)` in `:root`
- **Variable Token (`--line-color`)**: `#1a1630` — grounded in `var(--line-color)` in `:root`
- **Variable Token (`--accent-color`)**: `#8746e3` — grounded in `var(--accent-color)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `2.66667vw` lateral canvas padding with `2.13333vw` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 2.13333vw`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `2.66667vw` horizontal padding
- **Media Queries**: `@media (max-width:47.99em)`, `@media (min-width:48em)`, `@media (min-width:0)`, `@media (min-width:23.4375em)`
- **Corner Radii**: `10px`, `8px`, `50%`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `HelveticaNowDisplay`
- **Body Font Stack**: `HelveticaNowDisplay`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 32px`, `line-height: 48px`, `font-weight: 700`); CSS variables `--font-helvetica-now-display: "helveticaNowDisplay", "helveticaNowDisplay Fallback"`; rule `h1` (`font-size: 13.3333vw`, `line-height: 82%`, `letter-spacing: -.07em`, `font-weight: 400`)
- **H2 Section Rule**: live computed `h2` (`font-size: 120px`, `line-height: 98.4px`, `font-weight: 400`, `letter-spacing: -8.4px`); rule `h2` (`font-size: 8vw`, `line-height: 105%`, `letter-spacing: .01em`, `font-weight: 400`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: 3.73333vw`, `line-height: 132%`, `letter-spacing: 0`, `font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-zzdp-nl` (`Al meer dan 70 jaar betekenisvolle architectuur · ZZDP`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.lenis> — `www-zzdp-nl`)**:
   - DOM & Selectors: Landmark `<nav class="lenis">` (`227x18px`) hosting `Al meer dan 70 jaar betekenisvolle a` navigation (`Home · Projecten · Over ons · Nieuws en inzichten · Vacatures`), DOM attributes (`data-next-head`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`), and stylesheet rule `.u-underline-link:after { height:.266667vw }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.lenis> — `www-zzdp-nl`)` (`www-zzdp-nl`) adapts across `@media (max-width:47.99em)`, `@media (min-width:48em)`, `@media (min-width:0)`, `@media (min-width:23.4375em)` with `cubic-bezier(.48,0,.03,1)`, `cubic-bezier(.5,0,0,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Home · Projecten · Over ons · Nieuws en inzichten · Vacatures`.
2. **Hero Stage & Focal Lead (<section.theme--mossLight> — `ZZDP`)**:
   - DOM & Selectors: Landmark `<section class="theme--mossLight">` presenting display lead `ZZDP` and copy excerpt *"We staan op de schouders van onze voorgangers. Met meer dan 70 ja"* over `#ffffff` canvas and `#12366b` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#ffffff` background with `#12366b` headline `ZZDP`.
3. **Primary Showcase & Content Grid (<section.vjs-styles-dimensions> — `Bij ZZDP geloven wij dat architect`)**:
   - DOM & Selectors: Landmark `<section class="vjs-styles-dimensions">` rendering section `Bij ZZDP geloven wij dat architectuur meer is dan...` with copy *"Video Player is loading."*, asset references (`favicon.svg`, `HelveticaNowDisplay_Regular-s.p.1...`, `HelveticaNowDisplay_Md-s.p.16ns3u...`, `PPNeueMachina_PlainRegular-s.p.39...`), and grid rule `.default-in-animation { transform:translateY(26.6667vw) }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.vjs-styles-dimensions> — `Bij ZZDP geloven wij dat architect`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 2.13333vw`) on desktop and Single-column vertical stack at `390px` viewport width with `2.66667vw` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.theme--white> — `Gedreven door nalatenschap`)**:
   - DOM & Selectors: Landmark `<section class="theme--white">` framing `Gedreven door nalatenschap` and `Partners in design` (*"Seek to live, currently behind live"*) with `#ebeae1` surface cards, `#ff2800` accents, and `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;line-height:1.15 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.theme--white> — `Gedreven door nalatenschap`)` uses `10px`, `8px`, `50%`, `2px` radii, `#ff2800` highlights, and assets (favicon.svg, HelveticaNowDisplay_Regular-s.p.1..., HelveticaNowDisplay_Md-s.p.16ns3u...).
5. **Colophon & Global Directory Footer (<footer.theme--white> — `https://www.zzdp.nl/`)**:
   - DOM & Selectors: Landmark `<footer class="theme--white">` anchoring `Al meer dan 70 jaar betekenisvol` footer links (`Home · Projecten · Over ons · Nieuws en inzichten · Vacatures`), copy *"descriptions off , selected"*, and `#b5b899` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.theme--white> — `https://www.zzdp.nl/`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `2.66667vw` lateral canvas padding with `2.13333vw` grid gap and attributes (data-next-head, data-next-font="size-adjust", data-next-font="size-adjust").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"We staan op de schouders van onze voorgangers. Met meer dan 70 jaar aan ervaring,..."*
- Copy Excerpt 2: *"Video Player is loading."*
- Copy Excerpt 3: *"Seek to live, currently behind live"*
- Copy Excerpt 4: *"descriptions off , selected"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.48,0,.03,1)`, `cubic-bezier(.5,0,0,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`www-zzdp-nl`)**:
- `.u-underline-link:after { height:.266667vw }`
- `.default-in-animation { transform:translateY(26.6667vw) }`
- `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;line-height:1.15 }`
- `section { display:block }`
- `main { display:block }`
- **Per-Selector Transition Rules**:
- **Selector `.c-scrollbar`**: `transition: transform .3s,opacity .3s` extracted from `www-zzdp-nl` stylesheet.
- **Selector `.u-underline-link:after`**: `transition: transform .3s cubic-bezier(.48,0,.03,1)` extracted from `www-zzdp-nl` stylesheet.
- **Selector `scss-module__gW1A4G__u-underline-...`**: `transition: transform .3s cubic-bezier(.48,0,.03,1)` extracted from `www-zzdp-nl` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.48,0,.03,1)`)**: Governs interactive state transitions across `<nav.lenis>` and `<section.vjs-styles-dimensions>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `18562px` across 8 distinct viewport chapters using Lenis, GSAP/ScrollTrigger.
- **Vertical Chapter Sequence**: Hero (0%) -> Bij ZZDP geloven wij dat ar... (5%) -> Section @ 19% (19%) -> ONS VERHAAL (34%) -> ONS VERHAAL (48%) -> ONZE GESCHIEDENIS (63%) -> ONZE GESCHIEDENIS (77%) -> ONZE GESCHIEDENIS (82%).
- **Multi-Page Routes**: Scaffold internal routes `/project/scarlet` (detail, direct), `/contact` (about, direct), `/project/pc-hoofstraat-7` (detail, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-zzdp-nl`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | Hero | `2` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `5%` | Bij ZZDP geloven wij dat architectuur meer is... | `2` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `3400px` | `19%` | Section @ 19% | `2` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `5950px` | `34%` | ONS VERHAAL | `2` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `8500px` | `48%` | ONS VERHAAL | `2` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `11050px` | `63%` | ONZE GESCHIEDENIS | `2` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `13600px` | `77%` | ONZE GESCHIEDENIS | `2` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `14400px` | `82%` | ONZE GESCHIEDENIS | `2` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | Bij ZZDP geloven wij dat architectuur mee... | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `7131px` | `50%` | GEDREVEN DOOR NALATENSCHAP | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `14263px` | `100%` | Footer | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `detail` | `https://www.zzdp.nl/project/scarlet` | SCARLET | `14325px` | `direct` (`3025ms`) | [subpage-01-project-scarlet.webp](assets/subpage-01-project-scarlet.webp) |
| `2` | `about` | `https://www.zzdp.nl/contact` | Laten we samen iets waardevols bouwen | `6419px` | `direct` (`1828ms`) | [subpage-02-contact.webp](assets/subpage-02-contact.webp) |
| `3` | `detail` | `https://www.zzdp.nl/project/pc-hoofstraat-7` | PC-HOOFTSTRAAT 7 | `15468px` | `direct` (`1048ms`) | [subpage-03-project-pc-hoofstraat-7.webp](assets/subpage-03-project-pc-hoofstraat-7.webp) |

