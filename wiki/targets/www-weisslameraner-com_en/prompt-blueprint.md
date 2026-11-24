---
title: "UI Prompt Blueprint: www-weisslameraner-com_en"
date: 2026-11-24
captured_at: 2026-11-24
target: "www-weisslameraner-com_en"
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
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#171717` accent)"
---

# UI Design System & Master Generation Blueprint: www-weisslameraner-com_en

> **Weiss & Lameraner Media Group – Lifestyle Media House Vienna** (https://www.weisslameraner.com/en) — Vienna media house: STYLE UP YOUR LIFE!, Y, OBEGG and ADIWEISS.TV. Advertising in print, online, social and TV, plus content and events f...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Weiss & Lameraner Media Group – Lifestyle Media House Vienna** (`https://www.weisslameraner.com/en`). Vienna media house: STYLE UP YOUR LIFE!, Y, OBEGG and ADIWEISS.TV. Advertising in print, online, social and TV, plus content and events f...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#171717` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `section` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#171717` accents.
  - **Grounded Typographic Hierarchy**: Pairs `figtreeUpright` for display copy (`Lifestyle media for your brand.`) with `Segoe UI` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: 4px`, padding `1.5rem`) with `cubic-bezier(0,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`).

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=7978px` / doc `8878px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `96rem` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `1.5rem` lateral canvas padding with `4px` grid gap.
- **Border Radius Scale**: `.3125rem`, `.375rem`, `.25rem`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 4px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1.5rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `section` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#808080` | `.bg-gray-100 { background-color: gray }` (`#808080`) |
| **Interactive Accent / Highlight** | `#171717` | `var(--primary)` in `:root` |
| **Secondary / Muted Copy** | `#737373` | `var(--muted-foreground)` in `:root` |
| **Structural Hairline Border** | `#e5e5e5` | `var(--border)` in `:root` |
| **Variable Token (`--foreground`)** | `#0a0a0a` | `var(--foreground)` in `:root` |
| **Variable Token (`--primary-foreground`)** | `#fafafa` | `var(--primary-foreground)` in `:root` |
| **Variable Token (`--secondary`)** | `#f5f5f5` | `var(--secondary)` in `:root` |
| **Variable Token (`--destructive`)** | `#e40014` | `var(--destructive)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--radius` | `.625rem` | Elevation / Border Token |
| `--background` | `#fff` | Canvas / Surface Token |
| `--foreground` | `#0a0a0a` | Typography Ink Token |
| `--card` | `#fff` | Color / Atmospheric Token |
| `--card-foreground` | `#0a0a0a` | Typography Ink Token |
| `--popover` | `#fff` | Color / Atmospheric Token |
| `--popover-foreground` | `#0a0a0a` | Typography Ink Token |
| `--primary` | `#171717` | Brand / Palette Token |
| `--primary-foreground` | `#fafafa` | Typography Ink Token |
| `--secondary` | `#f5f5f5` | Brand / Palette Token |
| `--secondary-foreground` | `#171717` | Typography Ink Token |
| `--muted` | `#f5f5f5` | Color / Atmospheric Token |
| `--muted-foreground` | `#737373` | Typography Ink Token |
| `--accent` | `#f5f5f5` | Brand / Palette Token |
| `--accent-foreground` | `#171717` | Typography Ink Token |
| `--destructive` | `#e40014` | Color / Atmospheric Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `figtreeUpright`.
- **Primary Body Stack**: `Segoe UI`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 72px`, `line-height: 77.76px`, `font-weight: 300`, `letter-spacing: -1.8px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 60px`, `line-height: 69px`, `font-weight: 300`, `letter-spacing: -1.5px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: inherit`, `line-height: normal`, `letter-spacing: normal`, `font-weight: inherit`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`.
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`; rule `small` (`font-size: .36em`, `letter-spacing: .02em`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `www-weisslameraner-com_en` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-weisslameraner-com_en` stylesheet.
- **Selector `.transition-\[background-size\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-weisslameraner-com_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.top-0>` and `<section.bg-white>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`) with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `8878px`, deepest scrollY reached `7978px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `Lenis`.
- **Hover Physics (`primary_cta` · `About`)**: `color`: `lab(35.6337 -1.58697 -1...` -> `lab(9.03835 1.15298 1.9...` (`transition-duration: 0.15s`, `timing: cubic-bezier(0.4, 0, 0.2, 1)`).
- **Route Transition Architecture**: First internal navigation (`/en/project/events`) measured as `MPA` in `1434ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Weiss & Lameraner Media Group – Lifestyle  │
│ ====================================================================== │
│ [ <header.top-0> (1440x85px)          | About · Services · Media · B ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.relative> (w=1440px)                          | │
│ | H1: Lifestyle media for your brand.                                | │
│ | Substrate: #ffffff | Ink: #000000 | Accent: #171717                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.bg-white>) max-w: 96rem                    | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Brands that work with us.    |  | Austria's media house for li | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.bg-stone-950>) — Guide for brands What     | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.bg-stone-950) | https://www.weisslameraner.com/en    │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 4px)        │
│ ====================================================================== │
│ [ HEADER BAR (<header.top-0>          ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.relative>) — 390px Vertical Lead              | │
│ | H1: Lifestyle media for your brand.                                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.bg-white>) — 1-Col Stack                  | │
│ | [ Item 1: Brands that work with us.                              ] | │
│ | [ Item 2: Austria's media house for lifestyle.                   ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.bg-stone-950>) — 1-Col (Guide for brands W) | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.bg-stone-950) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.top-0> — `www-weisslameraner-com_en`)**:
   - Landmark `<header class="top-0 left-0">` (`1440x85px`) hosting `Weiss & Lameraner Media Group – Life` navigation (`About · Services · Media · Brand Events · WLX`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="cms-o9gdh8"`, `data-href="cms-o9gdh8"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Lifestyle media for your brand.`)**:
   - Landmark `<section class="relative bg-white">` presenting display lead `Lifestyle media for your brand.` and copy excerpt *"Since 2009 we have been taking brands to where their audience is:"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.bg-white> — `Brands that work with us.`)**:
   - Landmark `<section class="bg-white py-16">` rendering section `Brands that work with us.` with copy *"Media Data 2027 Media Data 2027"*, asset references (`Figtree_VariableFont_wght-s.p.0r5...`, `3emm7imx_eab9.css`, `1lfjsiuslldzn.css`, `37mpl03i35te0.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.bg-stone-950> — `Austria's media house for lifestyl`)**:
   - Landmark `<section class="bg-stone-950 relative">` framing `Austria's media house for lifestyle.` and `Guide for brands What do you want to achieve? Dis...` (*"(opens in a new window)"*) with `#808080` surface cards, `#171717` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.bg-stone-950> — `https://www.weisslameraner.com/en`)**:
   - Landmark `<footer class="bg-stone-950 font-sans">` anchoring `Weiss & Lameraner Media Group – ` footer links (`About · Services · Media · Brand Events · WLX`), copy *"Austria's media house"*, and `#e5e5e5` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `Hero` · sticky/fixed elements: `2`
- **Step 02** (`y=850px`, `11%`): Active landmark `Lifestyle media for your brand.` · sticky/fixed elements: `2`
- **Step 03** (`y=2550px`, `32%`): Active landmark `Austria's media house for lifestyle.` · sticky/fixed elements: `1`
- **Step 04** (`y=3400px`, `43%`): Active landmark `MEDIA & REACH` · sticky/fixed elements: `1`
- **Step 05** (`y=5100px`, `64%`): Active landmark `Our media. Your stage. 89,950 Copies per issue: d...` · sticky/fixed elements: `2`
- **Step 06** (`y=5950px`, `75%`): Active landmark `WLX. Made to measure for your brand.` · sticky/fixed elements: `2`
- **Step 07** (`y=7650px`, `96%`): Active landmark `Want your brand to be seen? Let’s talk in person.` · sticky/fixed elements: `1`
- **Step 08** (`y=7978px`, `100%`): Active landmark `BRANDS` · sticky/fixed elements: `1`

### Multi-Page Internal Route Map
- **Detail Route (`/en/project/events`)**: `https://www.weisslameraner.com/en/project/events` — H1: `We stage your brand event.`, scrollHeight `12271px`, transition `MPA` (`1434ms`)
- **Detail Route (`/en/wlx`)**: `https://www.weisslameraner.com/en/wlx` — H1: `WLX. Made to measure for your brand.`, scrollHeight `12464px`, transition `direct` (`977ms`)
- **Detail Route (`/en/media-data`)**: `https://www.weisslameraner.com/en/media-data` — H1: `Media Data 2027`, scrollHeight `11427px`, transition `direct` (`637ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-weisslameraner-com_en (Weiss & Lameraner Media Group – Lifestyle Media House Vienna)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-weisslameraner-com_en` (**Weiss & Lameraner Media Group – Lifestyle Media House Vienna** — `https://www.weisslameraner.com/en`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#171717` accent).
- **Identity & Domain Context**: Vienna media house: STYLE UP YOUR LIFE!, Y, OBEGG and ADIWEISS.TV. Advertising in print, online, social and TV, plus content and events f...
- **Primary Substrate**: `#ffffff` (live computed `section` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#171717`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `section` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#171717` accents.
  - **Grounded Typographic Hierarchy**: Pairs `figtreeUpright` for display copy (`Lifestyle media for your brand.`) with `Segoe UI` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: 4px`, padding `1.5rem`) with `cubic-bezier(0,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`).

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-weisslameraner-com_en` in your global stylesheet:

:root {
  /* Weiss & Lameraner Media Group – Lifestyle Media House Vienna (www-weisslameraner-com_en) — Live-Grounded CSS Variables */
  --radius: .625rem; /* Elevation / Border Token (www-weisslameraner-com_en) */
  --background: #fff; /* Canvas / Surface Token (www-weisslameraner-com_en) */
  --foreground: #0a0a0a; /* Typography Ink Token (www-weisslameraner-com_en) */
  --card: #fff; /* Color / Atmospheric Token (www-weisslameraner-com_en) */
  --card-foreground: #0a0a0a; /* Typography Ink Token (www-weisslameraner-com_en) */
  --popover: #fff; /* Color / Atmospheric Token (www-weisslameraner-com_en) */
  --popover-foreground: #0a0a0a; /* Typography Ink Token (www-weisslameraner-com_en) */
  --primary: #171717; /* Brand / Palette Token (www-weisslameraner-com_en) */
  --primary-foreground: #fafafa; /* Typography Ink Token (www-weisslameraner-com_en) */
  --secondary: #f5f5f5; /* Brand / Palette Token (www-weisslameraner-com_en) */
  --secondary-foreground: #171717; /* Typography Ink Token (www-weisslameraner-com_en) */
  --muted: #f5f5f5; /* Color / Atmospheric Token (www-weisslameraner-com_en) */
  --muted-foreground: #737373; /* Typography Ink Token (www-weisslameraner-com_en) */
  --accent: #f5f5f5; /* Brand / Palette Token (www-weisslameraner-com_en) */
  --accent-foreground: #171717; /* Typography Ink Token (www-weisslameraner-com_en) */
  --destructive: #e40014; /* Color / Atmospheric Token (www-weisslameraner-com_en) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `section` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#808080` — grounded in `.bg-gray-100 { background-color: gray }` (`#808080`)
- **Interactive Accent / Highlight**: `#171717` — grounded in `var(--primary)` in `:root`
- **Secondary / Muted Copy**: `#737373` — grounded in `var(--muted-foreground)` in `:root`
- **Structural Hairline Border**: `#e5e5e5` — grounded in `var(--border)` in `:root`
- **Variable Token (`--foreground`)**: `#0a0a0a` — grounded in `var(--foreground)` in `:root`
- **Variable Token (`--primary-foreground`)**: `#fafafa` — grounded in `var(--primary-foreground)` in `:root`
- **Variable Token (`--secondary`)**: `#f5f5f5` — grounded in `var(--secondary)` in `:root`
- **Variable Token (`--destructive`)**: `#e40014` — grounded in `var(--destructive)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `96rem` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `1.5rem` lateral canvas padding with `4px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 4px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1.5rem` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `.3125rem`, `.375rem`, `.25rem`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `figtreeUpright`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: live computed `h1` (`font-size: 72px`, `line-height: 77.76px`, `font-weight: 300`, `letter-spacing: -1.8px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **H2 Section Rule**: live computed `h2` (`font-size: 60px`, `line-height: 69px`, `font-weight: 300`, `letter-spacing: -1.5px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: inherit`, `line-height: normal`, `letter-spacing: normal`, `font-weight: inherit`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`; rule `small` (`font-size: .36em`, `letter-spacing: .02em`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-weisslameraner-com_en` (`Weiss & Lameraner Media Group – Lifestyle Media House Vienna`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.top-0> — `www-weisslameraner-com_en`)**:
   - DOM & Selectors: Landmark `<header class="top-0 left-0">` (`1440x85px`) hosting `Weiss & Lameraner Media Group – Life` navigation (`About · Services · Media · Brand Events · WLX`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="cms-o9gdh8"`, `data-href="cms-o9gdh8"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.top-0> — `www-weisslameraner-com_en`)` (`www-weisslameraner-com_en`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)` transitions and links `About · Services · Media · Brand Events · WLX`.
2. **Hero Stage & Focal Lead (<section.relative> — `Lifestyle media for your brand.`)**:
   - DOM & Selectors: Landmark `<section class="relative bg-white">` presenting display lead `Lifestyle media for your brand.` and copy excerpt *"Since 2009 we have been taking brands to where their audience is:"* over `#ffffff` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#ffffff` background with `#000000` headline `Lifestyle media for your brand.`.
3. **Primary Showcase & Content Grid (<section.bg-white> — `Brands that work with us.`)**:
   - DOM & Selectors: Landmark `<section class="bg-white py-16">` rendering section `Brands that work with us.` with copy *"Media Data 2027 Media Data 2027"*, asset references (`Figtree_VariableFont_wght-s.p.0r5...`, `3emm7imx_eab9.css`, `1lfjsiuslldzn.css`, `37mpl03i35te0.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.bg-white> — `Brands that work with us.`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 4px`) on desktop and Single-column vertical stack at `390px` viewport width with `1.5rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.bg-stone-950> — `Austria's media house for lifestyl`)**:
   - DOM & Selectors: Landmark `<section class="bg-stone-950 relative">` framing `Austria's media house for lifestyle.` and `Guide for brands What do you want to achieve? Dis...` (*"(opens in a new window)"*) with `#808080` surface cards, `#171717` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.bg-stone-950> — `Austria's media house for lifestyl`)` uses `.3125rem`, `.375rem`, `.25rem`, `2px` radii, `#171717` highlights, and assets (Figtree_VariableFont_wght-s.p.0r5..., 3emm7imx_eab9.css, 1lfjsiuslldzn.css).
5. **Colophon & Global Directory Footer (<footer.bg-stone-950> — `https://www.weisslameraner.com/en`)**:
   - DOM & Selectors: Landmark `<footer class="bg-stone-950 font-sans">` anchoring `Weiss & Lameraner Media Group – ` footer links (`About · Services · Media · Brand Events · WLX`), copy *"Austria's media house"*, and `#e5e5e5` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.bg-stone-950> — `https://www.weisslameraner.com/en`)` aligns to `96rem` (non-`@media` desktop container stylesheet rule) with `1.5rem` lateral canvas padding with `4px` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="cms-o9gdh8").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Since 2009 we have been taking brands to where their audience is: into our four me..."*
- Copy Excerpt 2: *"Media Data 2027 Media Data 2027"*
- Copy Excerpt 3: *"(opens in a new window)"*
- Copy Excerpt 4: *"Austria's media house"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`
- **Extracted Stylesheet Rules (`www-weisslameraner-com_en`)**:
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { vertical-align:baseline;font-size:75%;line-height:0;position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `www-weisslameraner-com_en` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-weisslameraner-com_en` stylesheet.
- **Selector `.transition-\[background-size\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-weisslameraner-com_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.top-0>` and `<section.bg-white>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`) with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `8878px` across 8 distinct viewport chapters using Lenis.
- **Vertical Chapter Sequence**: Hero (0%) -> Lifestyle media for your br... (11%) -> Austria's media house for l... (32%) -> MEDIA & REACH (43%) -> Our media. Your stage. 89,9... (64%) -> WLX. Made to measure for yo... (75%) -> Want your brand to be seen?... (96%) -> BRANDS (100%).
- **Hover Micro-Interaction (`primary_cta`)**: Animate `color` with `0.15s cubic-bezier(0.4, 0, 0.2, 1)`.
- **Multi-Page Routes**: Scaffold internal routes `/en/project/events` (detail, MPA), `/en/wlx` (detail, direct), `/en/media-data` (detail, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-weisslameraner-com_en`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | Hero | `2` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `11%` | Lifestyle media for your brand. | `2` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `2550px` | `32%` | Austria's media house for lifestyle. | `1` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `3400px` | `43%` | MEDIA & REACH | `1` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `5100px` | `64%` | Our media. Your stage. 89,950 Copies per issu... | `2` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `5950px` | `75%` | WLX. Made to measure for your brand. | `2` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `7650px` | `96%` | Want your brand to be seen? Let’s talk in per... | `1` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `7978px` | `100%` | BRANDS | `1` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | Hero | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `4537px` | `50%` | Our media. Your stage. 89,950 Copies per... | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `9075px` | `100%` | LOCATIONS | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `detail` | `https://www.weisslameraner.com/en/project/events` | We stage your brand event. | `12271px` | `MPA` (`1434ms`) | [subpage-01-en-project-events.webp](assets/subpage-01-en-project-events.webp) |
| `2` | `detail` | `https://www.weisslameraner.com/en/wlx` | WLX. Made to measure for your brand. | `12464px` | `direct` (`977ms`) | [subpage-02-en-wlx.webp](assets/subpage-02-en-wlx.webp) |
| `3` | `detail` | `https://www.weisslameraner.com/en/media-data` | Media Data 2027 | `11427px` | `direct` (`637ms`) | [subpage-03-en-media-data.webp](assets/subpage-03-en-media-data.webp) |

