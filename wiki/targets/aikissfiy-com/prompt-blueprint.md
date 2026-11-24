---
title: "UI Prompt Blueprint: aikissfiy-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "aikissfiy-com"
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
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#020617` ink, `#4f46e5` accent)"
---

# UI Design System & Master Generation Blueprint: aikissfiy-com

> **Free AI Kissing Video Generator: Create AI Kiss Videos Online - AIKissfiy** (https://aikissfiy.com) — Description: AIKissfiy creates realistic AI kissing videos from your photos. Choose different kiss styles, keep faces recognizable, and e...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Free AI Kissing Video Generator: Create AI Kiss Videos Online - AIKissfiy** (`https://aikissfiy.com`). Description: AIKissfiy creates realistic AI kissing videos from your photos. Choose different kiss styles, keep faces recognizable, and e...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#020617` ink, `#4f46e5` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `section` `background-color` (`computed_styles.json`)) paired with `#020617` primary typography and `#4f46e5` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Plus Jakarta Sans` for display copy (`Free AI Kissing Video Generator`) with `Inter` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1196px` container bounds (`gap: 4px`, padding `13px`) with `cubic-bezier(.4,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=7843px` / doc `8743px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1196px` (measured `<main>` bounding box width within `1440px` desktop viewport).
- **Canvas Lateral Padding & Spacing**: `13px` lateral canvas padding with `4px` grid gap.
- **Border Radius Scale**: `10px`, `30px`, `.75rem`, `.5rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: 2-column persistent left sidebar (`232px`, <nav.app-navigation__nav>) + `1196px` main content stage at `1440px` (`max-width: 1196px`, `gap: 4px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with collapsed `<nav.app-navigation__nav>` drawer navigation and `13px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media (min-width:1280px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `section` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#020617` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f7f8fb` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#4f46e5` | `.dark .btn-ambient { background: #4f46e5 }` |
| **Secondary / Muted Copy** | `#909399` | `var(--ak-text-color-secondary)` in `:root` |
| **Structural Hairline Border** | `#d1d5db` | `var(--border-color)` in `:root` |
| **Variable Token (`--aikiss-text`)** | `#0f172a` | `var(--aikiss-text)` in `:root` |
| **Variable Token (`--aikiss-muted`)** | `#475569` | `var(--aikiss-muted)` in `:root` |
| **Variable Token (`--aikiss-soft-muted`)** | `#64748b` | `var(--aikiss-soft-muted)` in `:root` |
| **Variable Token (`--gradient-primary`)** | `#6c63ff` | `var(--gradient-primary)` in `:root` |
| **Variable Token (`--gradient-primary`)** | `#8b81ff` | `var(--gradient-primary)` in `:root` |
| **Variable Token (`--gradient-primary`)** | `#b941ff` | `var(--gradient-primary)` in `:root` |
| **Variable Token (`--gradient-primary`)** | `#ec4899` | `var(--gradient-primary)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `Inter,system-ui,sans-serif` | Typography / Scale Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--aikiss-section-bg` | `transparent` | Canvas / Surface Token |
| `--aikiss-surface-solid` | `#fff` | Canvas / Surface Token |
| `--aikiss-surface-muted` | `rgba(248,250,252,.82)` | Canvas / Surface Token |
| `--aikiss-border` | `rgba(99,102,241,.2)` | Elevation / Border Token |
| `--aikiss-border-strong` | `rgba(99,102,241,.34)` | Elevation / Border Token |
| `--aikiss-text` | `#0f172a` | Typography Ink Token |
| `--aikiss-muted` | `#475569` | Color / Atmospheric Token |
| `--aikiss-soft-muted` | `#64748b` | Color / Atmospheric Token |
| `--aikiss-glow-primary` | `rgba(108,99,255,.2)` | Brand / Palette Token |
| `--aikiss-glow-secondary` | `rgba(236,72,153,.14)` | Brand / Palette Token |
| `--gradient-primary` | `linear-gradient(135deg,#6c63ff,#8b81ff 30%,#b941ff 66%,#ec4899)` | Brand / Palette Token |
| `--aikiss-inner-highlight` | `hsla(0,0%,100%,.78)` | Canvas / Surface Token |
| `--aikiss-shadow` | `0 24px 60px rgba(15,23,42,.1)` | Elevation / Border Token |
| `--aikiss-tool-shell` | `hsla(0,0%,100%,.58)` | Color / Atmospheric Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Plus Jakarta Sans`.
- **Primary Body Stack**: `Inter`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 50px`, `line-height: 54px`, `font-weight: 800`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: 1.11111`, `--text-5xl: 3rem`; rule `h1` (`font-size: 2em`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 60px`, `line-height: 60px`, `font-weight: 900`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: 1.33333`, `--text-3xl: 1.875rem`; rule `h2` (`line-height: 1.33`, `font-weight: 600`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: 1.5`, `--ak-font-size-base: 14px`; rule `p` (`font-size: 1rem`, `line-height: 1.5rem`, `font-weight: 700`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: 1.33333`, `--text-sm: .875rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(0,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.btn:before`**: `transition: .5s` extracted from `aikissfiy-com` stylesheet.
- **Selector `.glass-btn`**: `transition: .3s` extracted from `aikissfiy-com` stylesheet.
- **Selector `.glass-btn__icon`**: `transition: .3s` extracted from `aikissfiy-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.navigate-new>` and `<article.gap-3>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `8743px`, deepest scrollY reached `7843px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: Native browser scroll / standard CSS transitions.
- **Nav / Drawer Probe**: Tested trigger `Collapse navigation` (diff `3.154`, below state-capture threshold).
- **Hover Physics (`primary_cta` · `START CREATING NOW`)**: Computed transition `0s` / `ease` (no static color/transform shift captured at rest).
- **Interactive Control Probe (`carousel_next` · `Next photo packs`)**: Triggered visual diff `33.972` (attr ` -> `, captured in `assets/state-interactive.webp`).
- **Route Transition Architecture**: First internal navigation (`/pricing`) measured as `direct` in `3620ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Sidebar (232px) + Main (1196px)            │
│ ====================================================================== │
│ +--[ SIDEBAR (232px) ]--+--[ MAIN CONTENT STAGE (1196px) ]-----------+ │
│ | <nav.app-navigation__ | [ <header.navigate- | Home · Nano Banana ] | │
│ | - Home                | ------------------------------------------ | │
│ | - Nano Banana Pro     | HERO STAGE: <section.home-section>         | │
│ | - AI Effects          | H1: Free AI Kissing Video Generator        | │
│ | - Explore             | Bg:#ffffff Ink:#020617 Acc:#4f46e5         | │
│ | x=11 h=608px rail     | ------------------------------------------ | │
│ |                       | SHOWCASE: <article.gap-3> max:1196px       | │
│ |                       | [Generate AI Kiss V] [What Else Can You ]  | │
│ |                       | DETAIL: <article.px-3>                     | │
│ +-----------------------+--------------------------------------------+ │
│ [ FOOTER (<footer.border-slate) | https://aikissfiy.com                │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Collapsed Sidebar + 1-Col Stack       │
│ ====================================================================== │
│ [ DRAWER (<nav.app-navigation__n) | <header.navigate-new>              │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.home-section>) — 390px Full-Width             | │
│ | H1: Free AI Kissing Video Generator                                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<article.gap-3>) — 1-Col (gap: 4px)                | │
│ | [ Card 1: Generate AI Kiss Videos in Any Style                   ] | │
│ | [ Card 2: What Else Can You Create with AIKissfiy?               ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<article.px-3>) — 1-Col (Generate Romantic )         | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.border-slate-2) | Stacked 390px Colophon             │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Persistent Left Sidebar Navigation (<nav.app-navigation__nav> — `232×608px` at `x=11`)**:
   - Fixed/sticky left rail `<nav class="app-navigation__nav desktop-only">` (`232px` wide) paired with top bar `<header class="navigate-new top-0">` hosting `Free AI Kissing Video Generato` navigation (`Home · Nano Banana Pro · AI Effects`), DOM attributes (`data-hid="page-structured-data"`, `data-gtag`, `data-v-3c617593`, `data-v-122af031`), and rule `before { border-color:var(--color-gray-200);border-style:solid;border-width:0;box... }`.
2. **Hero Stage & Focal Lead (<section.home-section> — `Free AI Kissing Video Generator`)**:
   - Landmark `<section class="home-section aikiss-ambient-section">` inside `1196px` main stage presenting display lead `Free AI Kissing Video Generator` and copy excerpt *"Upload two photos, choose a kiss style, and create a realistic AI"* over `#ffffff` canvas and `#020617` ink.
3. **Primary Showcase & Content Grid (<article.gap-3> — `Generate AI Kiss Videos in Any Sty`)**:
   - Landmark `<article class="gap-3 px-3">` rendering section `Generate AI Kiss Videos in Any Style` with copy *"AI Kissing Video Generator"*, asset references (`cdn.aikissfiy.com`, `entry.BRsH49Xa.css`, `OverlayScrollbar.CrLIJdLh.css`, `LanguageSwitch.BsPr10ru.css`), and grid rule `body { line-height:inherit;margin:0 }`.
4. **Interactive Detail & Feature Matrix (<article.px-3> — `What Else Can You Create with AIKi`)**:
   - Landmark `<article class="gap-3 px-3">` framing `What Else Can You Create with AIKissfiy?` and `Generate Romantic Videos & Love Stories` (*"Start Creating Now"*) with `#f7f8fb` surface cards, `#4f46e5` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.border-slate-200> — `https://aikissfiy.com`)**:
   - Landmark `<footer class="border-slate-200 pt-8">` anchoring `Free AI Kissing Video Generator:` footer links (`Home · Nano Banana Pro · AI Effects`), copy *"Your Photos Stay Private"*, and `#d1d5db` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `Free AI Kissing Video Generator` · sticky/fixed elements: `2`
- **Step 02** (`y=850px`, `11%`): Active landmark `What Else Can You Create with AIKissfiy?` · sticky/fixed elements: `2`
- **Step 03** (`y=2550px`, `33%`): Active landmark `Create More Photos with Your AI Character` · sticky/fixed elements: `2`
- **Step 04** (`y=3400px`, `43%`): Active landmark `Explore More Romantic AI Tools` · sticky/fixed elements: `2`
- **Step 05** (`y=5100px`, `65%`): Active landmark `What Users Say About AIKissfiy?` · sticky/fixed elements: `2`
- **Step 06** (`y=5950px`, `76%`): Active landmark `Frequently Asked Questions About the AI Kissing G...` · sticky/fixed elements: `2`
- **Step 07** (`y=7650px`, `98%`): Active landmark `Footer` · sticky/fixed elements: `2`
- **Step 08** (`y=7843px`, `100%`): Active landmark `Footer` · sticky/fixed elements: `2`

### Multi-Page Internal Route Map
- **Listing Route (`/pricing`)**: `https://aikissfiy.com/pricing` — H1: `Plans & Pricing`, scrollHeight `3528px`, transition `direct` (`3620ms`)
- **Detail Route (`/characters/create`)**: `https://aikissfiy.com/characters/create` — H1: `Create your AI Character`, scrollHeight `952px`, transition `direct` (`679ms`)
- **Other Route (`/ai-kissing-generator`)**: `https://aikissfiy.com/ai-kissing-generator` — H1: `Create an AI Kissing Video from Two Photos`, scrollHeight `9954px`, transition `direct` (`3218ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: aikissfiy-com (Free AI Kissing Video Generator: Create AI Kiss Videos Online - AIKissfiy)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `aikissfiy-com` (**Free AI Kissing Video Generator: Create AI Kiss Videos Online - AIKissfiy** — `https://aikissfiy.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#020617` ink, `#4f46e5` accent).
- **Identity & Domain Context**: Description: AIKissfiy creates realistic AI kissing videos from your photos. Choose different kiss styles, keep faces recognizable, and e...
- **Primary Substrate**: `#ffffff` (live computed `section` `background-color` (`computed_styles.json`)), **Primary Ink**: `#020617`, **Accent / Highlight**: `#4f46e5`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `section` `background-color` (`computed_styles.json`)) paired with `#020617` primary typography and `#4f46e5` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Plus Jakarta Sans` for display copy (`Free AI Kissing Video Generator`) with `Inter` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1196px` container bounds (`gap: 4px`, padding `13px`) with `cubic-bezier(.4,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `aikissfiy-com` in your global stylesheet:

:root {
  /* Free AI Kissing Video Generator: Create AI Kiss Videos Online - AIKissfiy (aikissfiy-com) — Live-Grounded CSS Variables */
  --font-sans: Inter,system-ui,sans-serif; /* Typography / Scale Token (aikissfiy-com) */
  --default-font-family: var(--font-sans); /* Typography / Scale Token (aikissfiy-com) */
  --aikiss-section-bg: transparent; /* Canvas / Surface Token (aikissfiy-com) */
  --aikiss-surface-solid: #fff; /* Canvas / Surface Token (aikissfiy-com) */
  --aikiss-surface-muted: rgba(248,250,252,.82); /* Canvas / Surface Token (aikissfiy-com) */
  --aikiss-border: rgba(99,102,241,.2); /* Elevation / Border Token (aikissfiy-com) */
  --aikiss-border-strong: rgba(99,102,241,.34); /* Elevation / Border Token (aikissfiy-com) */
  --aikiss-text: #0f172a; /* Typography Ink Token (aikissfiy-com) */
  --aikiss-muted: #475569; /* Color / Atmospheric Token (aikissfiy-com) */
  --aikiss-soft-muted: #64748b; /* Color / Atmospheric Token (aikissfiy-com) */
  --aikiss-glow-primary: rgba(108,99,255,.2); /* Brand / Palette Token (aikissfiy-com) */
  --aikiss-glow-secondary: rgba(236,72,153,.14); /* Brand / Palette Token (aikissfiy-com) */
  --gradient-primary: linear-gradient(135deg,#6c63ff,#8b81ff 30%,#b941ff 66%,#ec4899); /* Brand / Palette Token (aikissfiy-com) */
  --aikiss-inner-highlight: hsla(0,0%,100%,.78); /* Canvas / Surface Token (aikissfiy-com) */
  --aikiss-shadow: 0 24px 60px rgba(15,23,42,.1); /* Elevation / Border Token (aikissfiy-com) */
  --aikiss-tool-shell: hsla(0,0%,100%,.58); /* Color / Atmospheric Token (aikissfiy-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `section` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#020617` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#f7f8fb` — grounded in live computed `footer` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#4f46e5` — grounded in `.dark .btn-ambient { background: #4f46e5 }`
- **Secondary / Muted Copy**: `#909399` — grounded in `var(--ak-text-color-secondary)` in `:root`
- **Structural Hairline Border**: `#d1d5db` — grounded in `var(--border-color)` in `:root`
- **Variable Token (`--aikiss-text`)**: `#0f172a` — grounded in `var(--aikiss-text)` in `:root`
- **Variable Token (`--aikiss-muted`)**: `#475569` — grounded in `var(--aikiss-muted)` in `:root`
- **Variable Token (`--aikiss-soft-muted`)**: `#64748b` — grounded in `var(--aikiss-soft-muted)` in `:root`
- **Variable Token (`--gradient-primary`)**: `#6c63ff` — grounded in `var(--gradient-primary)` in `:root`
- **Variable Token (`--gradient-primary`)**: `#8b81ff` — grounded in `var(--gradient-primary)` in `:root`
- **Variable Token (`--gradient-primary`)**: `#b941ff` — grounded in `var(--gradient-primary)` in `:root`
- **Variable Token (`--gradient-primary`)**: `#ec4899` — grounded in `var(--gradient-primary)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1196px` (measured `<main>` bounding box width within `1440px` desktop viewport)
- **Padding & Gutters**: `13px` lateral canvas padding with `4px` grid gap
- **Desktop Grid**: 2-column persistent left sidebar (`232px`, <nav.app-navigation__nav>) + `1196px` main content stage at `1440px` (`max-width: 1196px`, `gap: 4px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with collapsed `<nav.app-navigation__nav>` drawer navigation and `13px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media (min-width:1280px)`
- **Corner Radii**: `10px`, `30px`, `.75rem`, `.5rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Plus Jakarta Sans`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: live computed `h1` (`font-size: 50px`, `line-height: 54px`, `font-weight: 800`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: 1.11111`, `--text-5xl: 3rem`; rule `h1` (`font-size: 2em`)
- **H2 Section Rule**: live computed `h2` (`font-size: 60px`, `line-height: 60px`, `font-weight: 900`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: 1.33333`, `--text-3xl: 1.875rem`; rule `h2` (`line-height: 1.33`, `font-weight: 600`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: 1.5`, `--ak-font-size-base: 14px`; rule `p` (`font-size: 1rem`, `line-height: 1.5rem`, `font-weight: 700`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: 1.33333`, `--text-sm: .875rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `aikissfiy-com` (`Free AI Kissing Video Generator: Create AI Kiss Videos Online - AIKissfiy`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Persistent Left Sidebar Navigation (<nav.app-navigation__nav> — `232×608px` at `x=11`)**:
   - DOM & Selectors: Fixed/sticky left rail `<nav class="app-navigation__nav desktop-only">` (`232px` wide) paired with top bar `<header class="navigate-new top-0">` hosting `Free AI Kissing Video Generato` navigation (`Home · Nano Banana Pro · AI Effects`), DOM attributes (`data-hid="page-structured-data"`, `data-gtag`, `data-v-3c617593`, `data-v-122af031`), and rule `before { border-color:var(--color-gray-200);border-style:solid;border-width:0;box... }`.
   - Responsive Contract: Header `Persistent Left Sidebar Navigation (<nav.app-navigation__nav> — `232×608px` at `x=11`)` (`aikissfiy-com`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media (min-width:1280px)` with `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(0,0,.2,1)` transitions and links `Home · Nano Banana Pro · AI Effects`.
2. **Hero Stage & Focal Lead (<section.home-section> — `Free AI Kissing Video Generator`)**:
   - DOM & Selectors: Landmark `<section class="home-section aikiss-ambient-section">` inside `1196px` main stage presenting display lead `Free AI Kissing Video Generator` and copy excerpt *"Upload two photos, choose a kiss style, and create a realistic AI"* over `#ffffff` canvas and `#020617` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#ffffff` background with `#020617` headline `Free AI Kissing Video Generator`.
3. **Primary Showcase & Content Grid (<article.gap-3> — `Generate AI Kiss Videos in Any Sty`)**:
   - DOM & Selectors: Landmark `<article class="gap-3 px-3">` rendering section `Generate AI Kiss Videos in Any Style` with copy *"AI Kissing Video Generator"*, asset references (`cdn.aikissfiy.com`, `entry.BRsH49Xa.css`, `OverlayScrollbar.CrLIJdLh.css`, `LanguageSwitch.BsPr10ru.css`), and grid rule `body { line-height:inherit;margin:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<article.gap-3> — `Generate AI Kiss Videos in Any Sty`)` applies 2-column persistent left sidebar (`232px`, <nav.app-navigation__nav>) + `1196px` main content stage at `1440px` (`max-width: 1196px`, `gap: 4px`) on desktop and Single-column vertical stack at `390px` viewport width with collapsed `<nav.app-navigation__nav>` drawer navigation and `13px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.px-3> — `What Else Can You Create with AIKi`)**:
   - DOM & Selectors: Landmark `<article class="gap-3 px-3">` framing `What Else Can You Create with AIKissfiy?` and `Generate Romantic Videos & Love Stories` (*"Start Creating Now"*) with `#f7f8fb` surface cards, `#4f46e5` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.px-3> — `What Else Can You Create with AIKi`)` uses `10px`, `30px`, `.75rem`, `.5rem` radii, `#4f46e5` highlights, and assets (cdn.aikissfiy.com, entry.BRsH49Xa.css, OverlayScrollbar.CrLIJdLh.css).
5. **Colophon & Global Directory Footer (<footer.border-slate-200> — `https://aikissfiy.com`)**:
   - DOM & Selectors: Landmark `<footer class="border-slate-200 pt-8">` anchoring `Free AI Kissing Video Generator:` footer links (`Home · Nano Banana Pro · AI Effects`), copy *"Your Photos Stay Private"*, and `#d1d5db` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.border-slate-200> — `https://aikissfiy.com`)` aligns to `1196px` (measured `<main>` bounding box width within `1440px` desktop viewport) with `13px` lateral canvas padding with `4px` grid gap and attributes (data-hid="page-structured-data", data-gtag, data-v-3c617593).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Upload two photos, choose a kiss style, and create a realistic AI kiss video with..."*
- Copy Excerpt 2: *"AI Kissing Video Generator"*
- Copy Excerpt 3: *"Start Creating Now"*
- Copy Excerpt 4: *"Your Photos Stay Private"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(0,0,.2,1)`
- **Extracted Stylesheet Rules (`aikissfiy-com`)**:
- `before { border-color:var(--color-gray-200);border-style:solid;border-width:0;box... }`
- `body { line-height:inherit;margin:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { font-size:75%;line-height:0;position:relative;vertical-align:baseline }`
- **Per-Selector Transition Rules**:
- **Selector `.btn:before`**: `transition: .5s` extracted from `aikissfiy-com` stylesheet.
- **Selector `.glass-btn`**: `transition: .3s` extracted from `aikissfiy-com` stylesheet.
- **Selector `.glass-btn__icon`**: `transition: .3s` extracted from `aikissfiy-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.navigate-new>` and `<article.gap-3>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `8743px` across 8 distinct viewport chapters.
- **Vertical Chapter Sequence**: Free AI Kissing Video Gener... (0%) -> What Else Can You Create wi... (11%) -> Create More Photos with You... (33%) -> Explore More Romantic AI Tools (43%) -> What Users Say About AIKiss... (65%) -> Frequently Asked Questions... (76%) -> Footer (98%) -> Footer (100%).
- **Multi-Page Routes**: Scaffold internal routes `/pricing` (listing, direct), `/characters/create` (detail, direct), `/ai-kissing-generator` (other, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `aikissfiy-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | Free AI Kissing Video Generator | `2` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `11%` | What Else Can You Create with AIKissfiy? | `2` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `2550px` | `33%` | Create More Photos with Your AI Character | `2` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `3400px` | `43%` | Explore More Romantic AI Tools | `2` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `5100px` | `65%` | What Users Say About AIKissfiy? | `2` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `5950px` | `76%` | Frequently Asked Questions About the AI Kissi... | `2` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `7650px` | `98%` | Footer | `2` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `7843px` | `100%` | Footer | `2` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | Free AI Kissing Video Generator | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `5259px` | `50%` | AI Hug Generator | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `10555px` | `100%` | Footer | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Interactive UI State Captures (`1440×900` WebP)
| State Type | Trigger / Observation | Visual Asset |
| :--- | :--- | :--- |
| `interactive_control` | Control `carousel_next` (`Next photo packs`, diff `33.972`) | [state-interactive.webp](assets/state-interactive.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `listing` | `https://aikissfiy.com/pricing` | Plans & Pricing | `3528px` | `direct` (`3620ms`) | [subpage-01-pricing.webp](assets/subpage-01-pricing.webp) |
| `2` | `detail` | `https://aikissfiy.com/characters/create` | Create your AI Character | `952px` | `direct` (`679ms`) | [subpage-02-characters-create.webp](assets/subpage-02-characters-create.webp) |
| `3` | `other` | `https://aikissfiy.com/ai-kissing-generator` | Create an AI Kissing Video from Two P... | `9954px` | `direct` (`3218ms`) | [subpage-03-ai-kissing-generator.webp](assets/subpage-03-ai-kissing-generator.webp) |

