---
title: "UI Prompt Blueprint: www-barebonescollective-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "www-barebonescollective-com"
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
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#333333` ink, `#ffcc00` accent)"
---

# UI Design System & Master Generation Blueprint: www-barebonescollective-com

> **Bare Bones Collective** (https://www.barebonescollective.com/) — We are a creative agency that believes great brands are built through audacious work

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Bare Bones Collective** (`https://www.barebonescollective.com/`). We are a creative agency that believes great brands are built through audacious work
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#333333` ink, `#ffcc00` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#333333` primary typography and `#ffcc00` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Oswald` for display copy (`BARE`) with `PT Serif`.
  - **Calibrated Spatial Grid & Motion**: Combines `100rem` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.165,.84,.44,1)` easing and Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=9737px` / doc `11710px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `100rem` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `9px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `24px 24px 18px 18px`, `3px`, `100%`, `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 100rem`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#333333` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffff00` | `mark { background: #ffff00 }` |
| **Interactive Accent / Highlight** | `#ffcc00` | `crubber-button.ytp-swatch-backg... { background-color: #ffcc00 }` |
| **Secondary / Muted Copy** | `#ffd527` | live computed `h2` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e2e2e2` | `blockquote { border-left: #e2e2e2 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--td176b92ada598f8f` | `initial` | Design System Custom Token |
| `--td851cd75a8793667` | `initial` | Design System Custom Token |
| `--tc58f4bf5a9869b3e` | `initial` | Design System Custom Token |
| `--t3a480c2f814ef19c` | `initial` | Design System Custom Token |
| `--t77e217518bcd986b` | `initial` | Design System Custom Token |
| `--tc5e0863356bf5767` | `initial` | Design System Custom Token |
| `--t7a2234c5eadde886` | `initial` | Design System Custom Token |
| `--td340014d093b0821` | `initial` | Design System Custom Token |
| `--tf8c80baf678711b8` | `initial` | Design System Custom Token |
| `--t2986df03ecf88759` | `initial` | Design System Custom Token |
| `--te0c856964146535b` | `initial` | Design System Custom Token |
| `--tf630d2cff7da8057` | `initial` | Design System Custom Token |
| `--tf69032263d26c015` | `initial` | Design System Custom Token |
| `--ta5930fb3c4c7209c` | `initial` | Design System Custom Token |
| `--t1f1729a8e756e8bf` | `initial` | Design System Custom Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Oswald`.
- **Primary Body Stack**: `PT Serif`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 100px`, `line-height: 105px`, `font-weight: 700`); rule `h1` (`font-size: 2em`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 72px`, `line-height: 75.6px`, `font-weight: 600`); rule `h2` (`font-size: 32px`, `line-height: 36px`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 17.6px`, `font-weight: 400`); rule `body` (`font-size: 14px`, `line-height: 20px`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 17.6px`, `font-weight: 400`); rule `small` (`font-size: 80%`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.165,.84,.44,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,1,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `www-barebonescollective-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `www-barebonescollective-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-barebonescollective-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.165,.84,.44,1)`)**: Governs interactive state transitions across `<header.w-mod-js>` and `<section.logo_element>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `11710px`, deepest scrollY reached `9737px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: Native browser scroll / standard CSS transitions.
- **Hover Physics (`primary_cta` · `Menu`)**: Computed transition `0s` / `ease` (no static color/transform shift captured at rest).
- **Route Transition Architecture**: First internal navigation (`/work`) measured as `direct` in `2235ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Bare Bones Collective                      │
│ ====================================================================== │
│ [ <header.w-mod-js> (1440px)          | Menu · Work · Services · 360 ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.menu_element> (w=1440px)                      | │
│ | H1: BARE                                                           | │
│ | Substrate: #ffffff | Ink: #333333 | Accent: #ffcc00                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.logo_element>) max-w: 100rem               | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Bare Bones Collective Primar |  | www-barebonescollective-com  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.section-hero>) — www-barebonescollecti     | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.wf-oswald-n2) | https://www.barebonescollective.com  │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.w-mod-js>       ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.menu_element>) — 390px Vertical Lead          | │
│ | H1: BARE                                                           | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.logo_element>) — 1-Col Stack              | │
│ | [ Item 1: Bare Bones Collective Primary Showcase                 ] | │
│ | [ Item 2: www-barebonescollective-com Interactive Matrix         ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.section-hero>) — 1-Col (www-barebonescolle) | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.wf-oswald-n2) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.w-mod-js> — `www-barebonescollective-com`)**:
   - Landmark `<header class="w-mod-js">` (`1440px`) hosting `Bare Bones Collective` navigation (`Menu · Work · Services · 360° Campaigns · films`), DOM attributes (`data-wf-domain="www.barebonescollecti..."`, `data-wf-page="68358a988d15891f5e5e5ab6"`, `data-wf-site="68358a988d15891f5e5e5aad"`, `data-w-id="21dd915e-a730-31e5-d8..."`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.menu_element> — `BARE`)**:
   - Landmark `<section class="menu_element">` presenting display lead `BARE` and copy excerpt *"We are a creative agency that believes great brands are built thr"* over `#ffffff` canvas and `#333333` ink.
3. **Primary Showcase & Content Grid (<section.logo_element> — `Bare Bones Collective Primary Show`)**:
   - Landmark `<section class="logo_element">` rendering section `Bare Bones Collective Primary Showcase` with copy *"BARE"*, asset references (`cdn.prod.website-files.com`, `bare-bones-collective.webflow.sha...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.section-hero> — `www-barebonescollective-com Intera`)**:
   - Landmark `<section class="section-hero">` framing `www-barebonescollective-com Interactive Matrix` and `www-barebonescollective-com Archive & Directory` (*"Bare Bones Collective Primary Showcase"*) with `#ffff00` surface cards, `#ffcc00` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.wf-oswald-n2-active> — `https://www.barebonescollective.com/`)**:
   - Landmark `<footer class="wf-oswald-n2-active">` anchoring `Bare Bones Collective` footer links (`Menu · Work · Services · 360° Campaigns · films`), copy *"www-barebonescollective-com Interactive Matrix"*, and `#e2e2e2` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `BARE` · sticky/fixed elements: `1`
- **Step 02** (`y=850px`, `9%`): Active landmark `CREATIVE AGENCY THAT BELIEVES GREAT BRANDS ARE BU...` · sticky/fixed elements: `1`
- **Step 03** (`y=2550px`, `25%`): Active landmark `WE BELIEVE IN BIG BRAND THINKING` · sticky/fixed elements: `1`
- **Step 04** (`y=4250px`, `39%`): Active landmark `WE SOLVE COMMUNICATION PROBLEMS` · sticky/fixed elements: `0`
- **Step 05** (`y=5950px`, `55%`): Active landmark `#work` · sticky/fixed elements: `0`
- **Step 06** (`y=7650px`, `71%`): Active landmark `AWARDS` · sticky/fixed elements: `0`
- **Step 07** (`y=9350px`, `86%`): Active landmark `LET'S COLLABORATE` · sticky/fixed elements: `0`
- **Step 08** (`y=9737px`, `90%`): Active landmark `LET'S COLLABORATE` · sticky/fixed elements: `0`

### Multi-Page Internal Route Map
- **Listing Route (`/work`)**: `https://www.barebonescollective.com/work?tab=degree` — H1: `Work`, scrollHeight `2582px`, transition `direct` (`2235ms`)
- **Detail Route (`/work/jaggu-dada-mode`)**: `https://www.barebonescollective.com/work/jaggu-dada-mode` — H1: `JAGGU DADA MODE`, scrollHeight `3690px`, transition `direct` (`1728ms`)
- **About Route (`/people`)**: `https://www.barebonescollective.com/people` — H1: `OUR FOUNDERS`, scrollHeight `2642px`, transition `direct` (`1089ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-barebonescollective-com (Bare Bones Collective)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-barebonescollective-com` (**Bare Bones Collective** — `https://www.barebonescollective.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#333333` ink, `#ffcc00` accent).
- **Identity & Domain Context**: We are a creative agency that believes great brands are built through audacious work
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#333333`, **Accent / Highlight**: `#ffcc00`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#333333` primary typography and `#ffcc00` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Oswald` for display copy (`BARE`) with `PT Serif`.
  - **Calibrated Spatial Grid & Motion**: Combines `100rem` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.165,.84,.44,1)` easing and Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-barebonescollective-com` in your global stylesheet:

:root {
  /* Bare Bones Collective (www-barebonescollective-com) — Live-Grounded CSS Variables */
  --w-backdrop-animation: initial; /* Motion / Easing Token (www-barebonescollective-com) */
  --td176b92ada598f8f: initial; /* Design System Custom Token (www-barebonescollective-com) */
  --td851cd75a8793667: initial; /* Design System Custom Token (www-barebonescollective-com) */
  --tc58f4bf5a9869b3e: initial; /* Design System Custom Token (www-barebonescollective-com) */
  --t3a480c2f814ef19c: initial; /* Design System Custom Token (www-barebonescollective-com) */
  --t77e217518bcd986b: initial; /* Design System Custom Token (www-barebonescollective-com) */
  --tc5e0863356bf5767: initial; /* Design System Custom Token (www-barebonescollective-com) */
  --t7a2234c5eadde886: initial; /* Design System Custom Token (www-barebonescollective-com) */
  --td340014d093b0821: initial; /* Design System Custom Token (www-barebonescollective-com) */
  --tf8c80baf678711b8: initial; /* Design System Custom Token (www-barebonescollective-com) */
  --t2986df03ecf88759: initial; /* Design System Custom Token (www-barebonescollective-com) */
  --te0c856964146535b: initial; /* Design System Custom Token (www-barebonescollective-com) */
  --tf630d2cff7da8057: initial; /* Design System Custom Token (www-barebonescollective-com) */
  --tf69032263d26c015: initial; /* Design System Custom Token (www-barebonescollective-com) */
  --ta5930fb3c4c7209c: initial; /* Design System Custom Token (www-barebonescollective-com) */
  --t1f1729a8e756e8bf: initial; /* Design System Custom Token (www-barebonescollective-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#333333` — grounded in live computed `body` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#ffff00` — grounded in `mark { background: #ffff00 }`
- **Interactive Accent / Highlight**: `#ffcc00` — grounded in `crubber-button.ytp-swatch-backg... { background-color: #ffcc00 }`
- **Secondary / Muted Copy**: `#ffd527` — grounded in live computed `h2` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#e2e2e2` — grounded in `blockquote { border-left: #e2e2e2 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `100rem` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `9px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 100rem`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding
- **Media Queries**: `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)`
- **Corner Radii**: `24px 24px 18px 18px`, `3px`, `100%`, `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Oswald`
- **Body Font Stack**: `PT Serif`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 100px`, `line-height: 105px`, `font-weight: 700`); rule `h1` (`font-size: 2em`)
- **H2 Section Rule**: live computed `h2` (`font-size: 72px`, `line-height: 75.6px`, `font-weight: 600`); rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 17.6px`, `font-weight: 400`); rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 17.6px`, `font-weight: 400`); rule `small` (`font-size: 80%`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-barebonescollective-com` (`Bare Bones Collective`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.w-mod-js> — `www-barebonescollective-com`)**:
   - DOM & Selectors: Landmark `<header class="w-mod-js">` (`1440px`) hosting `Bare Bones Collective` navigation (`Menu · Work · Services · 360° Campaigns · films`), DOM attributes (`data-wf-domain="www.barebonescollecti..."`, `data-wf-page="68358a988d15891f5e5e5ab6"`, `data-wf-site="68358a988d15891f5e5e5aad"`, `data-w-id="21dd915e-a730-31e5-d8..."`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.w-mod-js> — `www-barebonescollective-com`)` (`www-barebonescollective-com`) adapts across `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)` with `cubic-bezier(.165,.84,.44,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,1,1)` transitions and links `Menu · Work · Services · 360° Campaigns · films`.
2. **Hero Stage & Focal Lead (<section.menu_element> — `BARE`)**:
   - DOM & Selectors: Landmark `<section class="menu_element">` presenting display lead `BARE` and copy excerpt *"We are a creative agency that believes great brands are built thr"* over `#ffffff` canvas and `#333333` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#ffffff` background with `#333333` headline `BARE`.
3. **Primary Showcase & Content Grid (<section.logo_element> — `Bare Bones Collective Primary Show`)**:
   - DOM & Selectors: Landmark `<section class="logo_element">` rendering section `Bare Bones Collective Primary Showcase` with copy *"BARE"*, asset references (`cdn.prod.website-files.com`, `bare-bones-collective.webflow.sha...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `body { margin: 0; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.logo_element> — `Bare Bones Collective Primary Show`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 100rem`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `9px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.section-hero> — `www-barebonescollective-com Intera`)**:
   - DOM & Selectors: Landmark `<section class="section-hero">` framing `www-barebonescollective-com Interactive Matrix` and `www-barebonescollective-com Archive & Directory` (*"Bare Bones Collective Primary Showcase"*) with `#ffff00` surface cards, `#ffcc00` accents, and `summary { display: block; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.section-hero> — `www-barebonescollective-com Intera`)` uses `24px 24px 18px 18px`, `3px`, `100%`, `50%` radii, `#ffcc00` highlights, and assets (cdn.prod.website-files.com, bare-bones-collective.webflow.sha..., fonts.googleapis.com).
5. **Colophon & Global Directory Footer (<footer.wf-oswald-n2-active> — `https://www.barebonescollective.com/`)**:
   - DOM & Selectors: Landmark `<footer class="wf-oswald-n2-active">` anchoring `Bare Bones Collective` footer links (`Menu · Work · Services · 360° Campaigns · films`), copy *"www-barebonescollective-com Interactive Matrix"*, and `#e2e2e2` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.wf-oswald-n2-active> — `https://www.barebonescollective.com/`)` aligns to `100rem` (non-`@media` desktop container stylesheet rule) with `9px` lateral canvas padding with `16px` grid gap and attributes (data-wf-domain="www.barebonescollecti...", data-wf-page="68358a988d15891f5e5e5ab6", data-wf-site="68358a988d15891f5e5e5aad").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Lead Copy: *"We are a creative agency that believes great brands are built through audacious work"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.165,.84,.44,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,1,1)`
- **Extracted Stylesheet Rules (`www-barebonescollective-com`)**:
- `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`
- `body { margin: 0; }`
- `summary { display: block; }`
- `video { vertical-align: baseline; display: inline-block; }`
- `template { display: none; }`
- **Per-Selector Transition Rules**:
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `www-barebonescollective-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `www-barebonescollective-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-barebonescollective-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.165,.84,.44,1)`)**: Governs interactive state transitions across `<header.w-mod-js>` and `<section.logo_element>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `11710px` across 8 distinct viewport chapters.
- **Vertical Chapter Sequence**: BARE (0%) -> CREATIVE AGENCY THAT BELIEV... (9%) -> WE BELIEVE IN BIG BRAND THI... (25%) -> WE SOLVE COMMUNICATION PROB... (39%) -> #work (55%) -> AWARDS (71%) -> LET'S COLLABORATE (86%) -> LET'S COLLABORATE (90%).
- **Multi-Page Routes**: Scaffold internal routes `/work` (listing, direct), `/work/jaggu-dada-mode` (detail, direct), `/people` (about, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-barebonescollective-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | BARE | `1` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `9%` | CREATIVE AGENCY THAT BELIEVES GREAT BRANDS AR... | `1` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `2550px` | `25%` | WE BELIEVE IN BIG BRAND THINKING | `1` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `4250px` | `39%` | WE SOLVE COMMUNICATION PROBLEMS | `0` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `5950px` | `55%` | #work | `0` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `7650px` | `71%` | AWARDS | `0` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `9350px` | `86%` | LET'S COLLABORATE | `0` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `9737px` | `90%` | LET'S COLLABORATE | `0` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | BARE | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `4630px` | `50%` | #work | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `9180px` | `100%` | #contact | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `listing` | `https://www.barebonescollective.com/work?tab=degree` | Work | `2582px` | `direct` (`2235ms`) | [subpage-01-work.webp](assets/subpage-01-work.webp) |
| `2` | `detail` | `https://www.barebonescollective.com/work/jaggu-dada-mode` | JAGGU DADA MODE | `3690px` | `direct` (`1728ms`) | [subpage-02-work-jaggu-dada-mode.webp](assets/subpage-02-work-jaggu-dada-mode.webp) |
| `3` | `about` | `https://www.barebonescollective.com/people` | OUR FOUNDERS | `2642px` | `direct` (`1089ms`) | [subpage-03-people.webp](assets/subpage-03-people.webp) |

