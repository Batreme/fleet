---
title: "UI Prompt Blueprint: www-upscayl-app"
date: 2026-11-24
captured_at: 2026-11-24
target: "www-upscayl-app"
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
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#0c0a09` ink, `#2563eb` accent)"
---

# UI Design System & Master Generation Blueprint: www-upscayl-app

> **Upscale Image Online Free – Upscale to 8K with AI · Upscayl** (https://www.upscayl.app) — Enhance blurry, pixelated, or low-resolution photos online with AI-powered upscaling. Choose an enhancement mode, preview the result, and...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Upscale Image Online Free – Upscale to 8K with AI · Upscayl** (`https://www.upscayl.app`). Enhance blurry, pixelated, or low-resolution photos online with AI-powered upscaling. Choose an enhancement mode, preview the result, and...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#0c0a09` ink, `#2563eb` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#0c0a09` primary typography and `#2563eb` accents.
  - **Grounded Typographic Hierarchy**: Uses `Inter` across display (`Upscale Image Online Free with AI`) and body copy, paired with `SFMono-Regular` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `80rem` container bounds (`gap: 2px`, padding `6px`) with `cubic-bezier(0,0,.2,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=12587px` / doc `13487px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `80rem` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `6px` lateral canvas padding with `2px` grid gap.
- **Border Radius Scale**: `6px`, `27px`, `20px`, `.25rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 80rem`, `gap: 2px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `6px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:374px)`, `@media (min-width:375px)`, `@media (min-width:430px)`, `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0c0a09` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f3ede4` | `:hover { background: #f3ede4 }` |
| **Interactive Accent / Highlight** | `#2563eb` | `.accent-blue-600 { color: #2563eb }` |
| **Secondary / Muted Copy** | `#628481` | live computed `button` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#def1e9` | `65 { border-color: #def1e9 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background` | `0 0% 100%` | Canvas / Surface Token |
| `--foreground` | `20 14.3% 4.1%` | Typography Ink Token |
| `--card` | `0 0% 100%` | Dimension / Scale Token |
| `--card-foreground` | `20 14.3% 4.1%` | Typography Ink Token |
| `--popover` | `0 0% 100%` | Dimension / Scale Token |
| `--popover-foreground` | `20 14.3% 4.1%` | Typography Ink Token |
| `--primary` | `175 82% 42%` | Brand / Palette Token |
| `--primary-foreground` | `0 0% 100%` | Typography Ink Token |
| `--secondary` | `180 25% 95%` | Brand / Palette Token |
| `--secondary-foreground` | `175 25% 15%` | Typography Ink Token |
| `--muted` | `180 20% 95%` | Dimension / Scale Token |
| `--muted-foreground` | `175 15% 45%` | Typography Ink Token |
| `--accent` | `180 25% 95%` | Brand / Palette Token |
| `--accent-foreground` | `175 25% 15%` | Typography Ink Token |
| `--destructive` | `0 84.2% 60.2%` | Dimension / Scale Token |
| `--destructive-foreground` | `60 9.1% 97.8%` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Inter`.
- **Primary Body Stack**: `Inter`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 72px`, `line-height: 72px`, `font-weight: 700`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 60px`, `line-height: 60px`, `font-weight: 700`); rule `h2` (`font-size: 1.875rem`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: .875rem`, `line-height: 1.25rem`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.mobile-bottom-nav_tab__YGSP5`**: `transition: background-color .16s ease,color .16s ease,transform .16s ease` extracted from `www-upscayl-app` stylesheet.
- **Selector `media (prefers-reduced-motion:red...`**: `transition: none` extracted from `www-upscayl-app` stylesheet.
- **Selector `.transition`**: `transition: cubic-bezier(0,0,.2,1)` extracted from `www-upscayl-app` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.bg-background>` and `<section.bg-gradient-to-b>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.py-8>` and `<section.bg-gradient-to-b>` interactive targets.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `13487px`, deepest scrollY reached `12587px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: Native browser scroll / standard CSS transitions.
- **Nav / Drawer Probe**: Tested trigger `AI Tools` (diff `0.402`, below state-capture threshold).
- **Hover Physics (`primary_cta` · `Try Upscayl AI Image Upscaler for...`)**: `transform`: `matrix(1.00072, 0, 0, 1...` -> `matrix(1.00127, 0, 0, 1...`; `backgroundColor`: `rgb(19, 195, 180)` -> `rgba(19, 195, 180, 0.9)`; `opacity`: `0.996389` -> `0.993671`; `boxShadow`: `rgba(0, 0, 0, 0) 0px 0p...` -> `rgba(0, 0, 0, 0) 0px 0p...` (`transition-duration: 0.3s`, `timing: cubic-bezier(0.4, 0, 0.2, 1)`).
- **Interactive Control Probe (`tab`)**: Tested `Free Upscaler` (diff `2.124`).
- **Route Transition Architecture**: First internal navigation (`/pricing`) measured as `SPA` in `1347ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Upscale Image Online Free – Upscale to 8K  │
│ ====================================================================== │
│ [ <header.bg-background> (1440x65px)  | AI Photo Editor · Image Enha ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.py-8> (w=1440px)                              | │
│ | H1: Upscale Image Online Free with AI                              | │
│ | Substrate: #ffffff | Ink: #0c0a09 | Accent: #2563eb                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.bg-gradient-to-b>) max-w: 80rem            | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Upscayl AI Image Upscaler    |  | Explore other tools          | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.py-10>) — Upscayl AI Image Upsc            | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.antialiased>) | https://www.upscayl.app              │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 2px)        │
│ ====================================================================== │
│ [ HEADER BAR (<header.bg-background>  ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.py-8>) — 390px Vertical Lead                  | │
│ | H1: Upscale Image Online Free with AI                              | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.bg-gradient-t) — 1-Col Stack              | │
│ | [ Item 1: Upscayl AI Image Upscaler                              ] | │
│ | [ Item 2: Explore other tools                                    ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.py-10>) — 1-Col (Upscayl AI Image U)        | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.antialiased>) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.bg-background> — `www-upscayl-app`)**:
   - Landmark `<header class="bg-background relative">` (`1440x65px`) hosting `Upscale Image Online Free – Upscale ` navigation (`AI Photo Editor · Image Enhancer · AI Image Tools · Pricing · API`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.__className_d8ebd1 { font-family:Inter,Inter Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.py-8> — `Upscale Image Online Free with AI`)**:
   - Landmark `<section class="py-8 bg-gradient-to-br">` presenting display lead `Upscale Image Online Free with AI` and copy excerpt *"The ultimate Upscayl AI Image Upscaler for crystal-clear 4K image"* over `#ffffff` canvas and `#0c0a09` ink.
3. **Primary Showcase & Content Grid (<section.bg-gradient-to-b> — `Upscayl AI Image Upscaler`)**:
   - Landmark `<section class="bg-gradient-to-b via-white">` rendering section `Upscayl AI Image Upscaler` with copy *"Upscale Image Online Free with AI"*, asset references (`5544ee6471eef55b.css`, `a4aeb68a5f6d17c2.css`, `c50624e23d0abf09.css`, `520cfa8ebc6f0a4b.css`), and grid rule `.__variable_d8ebd1 { --font-sans:"Inter","Inter Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.py-10> — `Explore other tools`)**:
   - Landmark `<section class="py-10 relative">` framing `Explore other tools` and `Upscayl AI Image Upscaler Features` (*"Enhance blurry, pixelated, or low-resolution photos online with A"*) with `#f3ede4` surface cards, `#2563eb` accents, and `.mobile-bottom-nav_spacer__ghNfj { height:calc(100px + env(safe-area-inset-bottom, 0px)) }`.
5. **Colophon & Global Directory Footer (<footer.antialiased> — `https://www.upscayl.app`)**:
   - Landmark `<footer class="antialiased">` anchoring `Upscale Image Online Free – Upsc` footer links (`AI Photo Editor · Image Enhancer · AI Image Tools · Pricing · API`), copy *"Try Upscayl AI Image Upscaler for Free"*, and `#def1e9` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `Upscale Image Online Free with AI` · sticky/fixed elements: `0`
- **Step 02** (`y=850px`, `7%`): Active landmark `Upscayl AI Image Upscaler` · sticky/fixed elements: `0`
- **Step 03** (`y=1700px`, `14%`): Active landmark `Cookie settings` · sticky/fixed elements: `0`
- **Step 04** (`y=2550px`, `20%`): Active landmark `50% OFF` · sticky/fixed elements: `0`
- **Step 05** (`y=3400px`, `27%`): Active landmark `50% OFF` · sticky/fixed elements: `0`
- **Step 06** (`y=4250px`, `34%`): Active landmark `Upscayl AI Image Upscaler Features` · sticky/fixed elements: `0`
- **Step 07** (`y=5100px`, `41%`): Active landmark `50% OFF` · sticky/fixed elements: `0`
- **Step 08** (`y=12587px`, `100%`): Active landmark `API` · sticky/fixed elements: `0`

### Multi-Page Internal Route Map
- **Listing Route (`/pricing`)**: `https://www.upscayl.app/pricing` — H1: `Simple, Transparent Pricing - Upscayl AI Upscaler`, scrollHeight `4002px`, transition `SPA` (`1347ms`)
- **Detail Route (`/api/image-upscaler`)**: `https://www.upscayl.app/api/image-upscaler` — H1: `Upscale images by 2x or 4x with one API`, scrollHeight `6360px`, transition `direct` (`1062ms`)
- **About Route (`/about`)**: `https://www.upscayl.app/about` — H1: `Independent AI image enhancement, with clear mode...`, scrollHeight `4087px`, transition `direct` (`897ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-upscayl-app (Upscale Image Online Free – Upscale to 8K with AI · Upscayl)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-upscayl-app` (**Upscale Image Online Free – Upscale to 8K with AI · Upscayl** — `https://www.upscayl.app`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#0c0a09` ink, `#2563eb` accent).
- **Identity & Domain Context**: Enhance blurry, pixelated, or low-resolution photos online with AI-powered upscaling. Choose an enhancement mode, preview the result, and...
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#0c0a09`, **Accent / Highlight**: `#2563eb`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#0c0a09` primary typography and `#2563eb` accents.
  - **Grounded Typographic Hierarchy**: Uses `Inter` across display (`Upscale Image Online Free with AI`) and body copy, paired with `SFMono-Regular` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `80rem` container bounds (`gap: 2px`, padding `6px`) with `cubic-bezier(0,0,.2,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-upscayl-app` in your global stylesheet:

:root {
  /* Upscale Image Online Free – Upscale to 8K with AI · Upscayl (www-upscayl-app) — Live-Grounded CSS Variables */
  --background: 0 0% 100%; /* Canvas / Surface Token (www-upscayl-app) */
  --foreground: 20 14.3% 4.1%; /* Typography Ink Token (www-upscayl-app) */
  --card: 0 0% 100%; /* Dimension / Scale Token (www-upscayl-app) */
  --card-foreground: 20 14.3% 4.1%; /* Typography Ink Token (www-upscayl-app) */
  --popover: 0 0% 100%; /* Dimension / Scale Token (www-upscayl-app) */
  --popover-foreground: 20 14.3% 4.1%; /* Typography Ink Token (www-upscayl-app) */
  --primary: 175 82% 42%; /* Brand / Palette Token (www-upscayl-app) */
  --primary-foreground: 0 0% 100%; /* Typography Ink Token (www-upscayl-app) */
  --secondary: 180 25% 95%; /* Brand / Palette Token (www-upscayl-app) */
  --secondary-foreground: 175 25% 15%; /* Typography Ink Token (www-upscayl-app) */
  --muted: 180 20% 95%; /* Dimension / Scale Token (www-upscayl-app) */
  --muted-foreground: 175 15% 45%; /* Typography Ink Token (www-upscayl-app) */
  --accent: 180 25% 95%; /* Brand / Palette Token (www-upscayl-app) */
  --accent-foreground: 175 25% 15%; /* Typography Ink Token (www-upscayl-app) */
  --destructive: 0 84.2% 60.2%; /* Dimension / Scale Token (www-upscayl-app) */
  --destructive-foreground: 60 9.1% 97.8%; /* Typography Ink Token (www-upscayl-app) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#0c0a09` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#f3ede4` — grounded in `:hover { background: #f3ede4 }`
- **Interactive Accent / Highlight**: `#2563eb` — grounded in `.accent-blue-600 { color: #2563eb }`
- **Secondary / Muted Copy**: `#628481` — grounded in live computed `button` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#def1e9` — grounded in `65 { border-color: #def1e9 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `80rem` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `6px` lateral canvas padding with `2px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 80rem`, `gap: 2px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `6px` horizontal padding
- **Media Queries**: `@media (max-width:374px)`, `@media (min-width:375px)`, `@media (min-width:430px)`, `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `6px`, `27px`, `20px`, `.25rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: live computed `h1` (`font-size: 72px`, `line-height: 72px`, `font-weight: 700`)
- **H2 Section Rule**: live computed `h2` (`font-size: 60px`, `line-height: 60px`, `font-weight: 700`); rule `h2` (`font-size: 1.875rem`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: .875rem`, `line-height: 1.25rem`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-upscayl-app` (`Upscale Image Online Free – Upscale to 8K with AI · Upscayl`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.bg-background> — `www-upscayl-app`)**:
   - DOM & Selectors: Landmark `<header class="bg-background relative">` (`1440x65px`) hosting `Upscale Image Online Free – Upscale ` navigation (`AI Photo Editor · Image Enhancer · AI Image Tools · Pricing · API`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.__className_d8ebd1 { font-family:Inter,Inter Fallback;font-style:normal }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.bg-background> — `www-upscayl-app`)` (`www-upscayl-app`) adapts across `@media (max-width:374px)`, `@media (min-width:375px)`, `@media (min-width:430px)`, `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `AI Photo Editor · Image Enhancer · AI Image Tools · Pricing · API`.
2. **Hero Stage & Focal Lead (<section.py-8> — `Upscale Image Online Free with AI`)**:
   - DOM & Selectors: Landmark `<section class="py-8 bg-gradient-to-br">` presenting display lead `Upscale Image Online Free with AI` and copy excerpt *"The ultimate Upscayl AI Image Upscaler for crystal-clear 4K image"* over `#ffffff` canvas and `#0c0a09` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#ffffff` background with `#0c0a09` headline `Upscale Image Online Free with AI`.
3. **Primary Showcase & Content Grid (<section.bg-gradient-to-b> — `Upscayl AI Image Upscaler`)**:
   - DOM & Selectors: Landmark `<section class="bg-gradient-to-b via-white">` rendering section `Upscayl AI Image Upscaler` with copy *"Upscale Image Online Free with AI"*, asset references (`5544ee6471eef55b.css`, `a4aeb68a5f6d17c2.css`, `c50624e23d0abf09.css`, `520cfa8ebc6f0a4b.css`), and grid rule `.__variable_d8ebd1 { --font-sans:"Inter","Inter Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.bg-gradient-to-b> — `Upscayl AI Image Upscaler`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 80rem`, `gap: 2px`) on desktop and Single-column vertical stack at `390px` viewport width with `6px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.py-10> — `Explore other tools`)**:
   - DOM & Selectors: Landmark `<section class="py-10 relative">` framing `Explore other tools` and `Upscayl AI Image Upscaler Features` (*"Enhance blurry, pixelated, or low-resolution photos online with A"*) with `#f3ede4` surface cards, `#2563eb` accents, and `.mobile-bottom-nav_spacer__ghNfj { height:calc(100px + env(safe-area-inset-bottom, 0px)) }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.py-10> — `Explore other tools`)` uses `6px`, `27px`, `20px`, `.25rem` radii, `#2563eb` highlights, and assets (5544ee6471eef55b.css, a4aeb68a5f6d17c2.css, c50624e23d0abf09.css).
5. **Colophon & Global Directory Footer (<footer.antialiased> — `https://www.upscayl.app`)**:
   - DOM & Selectors: Landmark `<footer class="antialiased">` anchoring `Upscale Image Online Free – Upsc` footer links (`AI Photo Editor · Image Enhancer · AI Image Tools · Pricing · API`), copy *"Try Upscayl AI Image Upscaler for Free"*, and `#def1e9` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.antialiased> — `https://www.upscayl.app`)` aligns to `80rem` (non-`@media` desktop container stylesheet rule) with `6px` lateral canvas padding with `2px` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"The ultimate Upscayl AI Image Upscaler for crystal-clear 4K images."*
- Copy Excerpt 2: *"Upscale Image Online Free with AI"*
- Copy Excerpt 3: *"Enhance blurry, pixelated, or low-resolution photos online with AI-powered upscali..."*
- Copy Excerpt 4: *"Try Upscayl AI Image Upscaler for Free"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`www-upscayl-app`)**:
- `.__className_d8ebd1 { font-family:Inter,Inter Fallback;font-style:normal }`
- `.__variable_d8ebd1 { --font-sans:"Inter","Inter Fallback" }`
- `.mobile-bottom-nav_spacer__ghNfj { height:calc(100px + env(safe-area-inset-bottom, 0px)) }`
- `.mobile-bottom-nav_tabs__LMVYc { display:grid;grid-auto-flow:column;grid-auto-columns:minmax(0,1fr);gap:2... }`
- `.mobile-bottom-nav_icon__AtZ9O { width:21px;height:21px;flex:none }`
- **Per-Selector Transition Rules**:
- **Selector `.mobile-bottom-nav_tab__YGSP5`**: `transition: background-color .16s ease,color .16s ease,transform .16s ease` extracted from `www-upscayl-app` stylesheet.
- **Selector `media (prefers-reduced-motion:red...`**: `transition: none` extracted from `www-upscayl-app` stylesheet.
- **Selector `.transition`**: `transition: cubic-bezier(0,0,.2,1)` extracted from `www-upscayl-app` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.bg-background>` and `<section.bg-gradient-to-b>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.py-8>` and `<section.bg-gradient-to-b>` interactive targets.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `13487px` across 8 distinct viewport chapters.
- **Vertical Chapter Sequence**: Upscale Image Online Free w... (0%) -> Upscayl AI Image Upscaler (7%) -> Cookie settings (14%) -> 50% OFF (20%) -> 50% OFF (27%) -> Upscayl AI Image Upscaler F... (34%) -> 50% OFF (41%) -> API (100%).
- **Hover Micro-Interaction (`primary_cta`)**: Animate `transform, backgroundColor, opacity, boxShadow` with `0.3s cubic-bezier(0.4, 0, 0.2, 1)`.
- **Multi-Page Routes**: Scaffold internal routes `/pricing` (listing, SPA), `/api/image-upscaler` (detail, direct), `/about` (about, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-upscayl-app`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | Upscale Image Online Free with AI | `0` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `7%` | Upscayl AI Image Upscaler | `0` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `1700px` | `14%` | Cookie settings | `0` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `2550px` | `20%` | 50% OFF | `0` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `3400px` | `27%` | 50% OFF | `0` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `4250px` | `34%` | Upscayl AI Image Upscaler Features | `0` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `5100px` | `41%` | 50% OFF | `0` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `12587px` | `100%` | API | `0` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | Upscale Image Online Free with AI | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `7200px` | `50%` | Cookie settings | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `14400px` | `100%` | Wide Format Support | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `listing` | `https://www.upscayl.app/pricing` | Simple, Transparent Pricing - Upscayl... | `4002px` | `SPA` (`1347ms`) | [subpage-01-pricing.webp](assets/subpage-01-pricing.webp) |
| `2` | `detail` | `https://www.upscayl.app/api/image-upscaler` | Upscale images by 2x or 4x with one API | `6360px` | `direct` (`1062ms`) | [subpage-02-api-image-upscaler.webp](assets/subpage-02-api-image-upscaler.webp) |
| `3` | `about` | `https://www.upscayl.app/about` | Independent AI image enhancement, wit... | `4087px` | `direct` (`897ms`) | [subpage-03-about.webp](assets/subpage-03-about.webp) |

