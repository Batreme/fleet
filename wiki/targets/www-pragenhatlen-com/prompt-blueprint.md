---
title: "UI Prompt Blueprint: www-pragenhatlen-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "www-pragenhatlen-com"
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
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#ecebea` / `#0000ff`)"
---

# UI Design System & Master Generation Blueprint: www-pragenhatlen-com

> **Prägen Hätlen · Swiss watchmaking for the crypto community.** (https://www.pragenhatlen.com/) — Trust, precision, resilience and uncompromising attention to detail.

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x872)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Prägen Hätlen · Swiss watchmaking for the crypto community.** (`https://www.pragenhatlen.com/`). Trust, precision, resilience and uncompromising attention to detail.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#ecebea` / `#0000ff`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ecebea` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#0c1114` primary typography and `#0000ff` accents.
  - **Grounded Typographic Hierarchy**: Uses `Manrope` across display (`THE SCARCEST ASSET, ON YOUR WRIST`) and body copy, paired with `RedHatMono` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 12px 168px`, padding `32px`) with `cubic-bezier(.215,.61,.355,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=14400px` / doc `16667px`), Mobile `390×872px` (`assets/mobile-journey.webp`, `1` keyframes).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `32px` lateral canvas padding with `12px 168px` grid gap.
- **Border Radius Scale**: `var(--border-radius)`, `100%`, `1rem`, `4px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 12px 168px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `32px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width: 768px) and (min-height: 500px) and (orientati...`, `@media (max-width: 768px)`, `@media (max-width: 768px) and (min-width: 768px) and (min-height...`, `@media (min-width: 768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ecebea` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0c1114` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `.BaseButton-module__white__qygOa { background-color: white }` (`#ffffff`) |
| **Interactive Accent / Highlight** | `#0000ff` | `.App-module__link__jsQ7Z:hover { color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#ffffff` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#ffffff` | `.StickyModal-module__header__LViCK { border-bottom: #ffffff }` |
| **Variable Token (`--color-black`)** | `#000000` | `var(--color-black)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--breakpoint-mobile` | `320px` | Dimension / Scale Token |
| `--breakpoint-mobile-horizontal` | `500px` | Dimension / Scale Token |
| `--breakpoint-tablet` | `768px` | Dimension / Scale Token |
| `--breakpoint-tablet-height` | `950px` | Layout / Spatial Grid Token |
| `--breakpoint-laptop` | `1024px` | Dimension / Scale Token |
| `--breakpoint-bigLaptop-min` | `1366px` | Dimension / Scale Token |
| `--breakpoint-bigLaptop` | `1440px` | Dimension / Scale Token |
| `--breakpoint-desktop` | `1680px` | Dimension / Scale Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--color-white--40` | `#ffffff66` | Canvas / Surface Token |
| `--color-white--16` | `#ffffff29` | Canvas / Surface Token |
| `--color-white--4` | `#ffffff0a` | Canvas / Surface Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-black--50` | `#00000080` | Canvas / Surface Token |
| `--color-black--30` | `#0000004d` | Canvas / Surface Token |
| `--color-black--24` | `#0000003d` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Manrope`.
- **Primary Body Stack**: `Manrope`.
- **Technical / Metadata Stack**: `RedHatMono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 48px`, `line-height: 48px`, `font-weight: 500`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 36px`, `line-height: 39.6px`, `font-weight: 500`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 18.4px`, `font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 18.4px`, `font-weight: 400`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.215,.61,.355,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.Header-module__top__mJsjm`**: `transition: .5s ease color` extracted from `www-pragenhatlen-com` stylesheet.
- **Selector `.Header-module__top_open__BgPji`**: `transition: unset` extracted from `www-pragenhatlen-com` stylesheet.
- **Selector `media (hover: hover)`**: `transition: .25s cubic-bezier(.215,.61,.355,1) opacity` extracted from `www-pragenhatlen-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.215,.61,.355,1)`)**: Governs interactive state transitions across `<header.Header-module__top__mJsjm>` and `<section.RotateScreen-module__root__m8vUV>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `16667px`, deepest scrollY reached `14400px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `Lenis`, `GSAP/ScrollTrigger`, `WebGL/Canvas`.
- **Interactive Control Probe (`accordion`)**: Tested `Is the watch Swiss Made? [ + ]` (diff `2.449`).

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Prägen Hätlen · Swiss watchmaking for the  │
│ ====================================================================== │
│ [ <header.Header-module_ (1440x76px)  | [02] A b o u t · [04] F A Q  ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.HeroVideo-module__root__FiO (w=1440px)        | │
│ | H1: THE SCARCEST ASSET, ON YOUR WRIST                              | │
│ | Substrate: #ecebea | Ink: #0c1114 | Accent: #0000ff                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.RotateScreen-modu) max-w: 1440px           | │
│ | +------------------------------+  +------------------------------+ | │
│ | | The scarcest asset, on your  |  | Precision in every layer     | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.RotateScreen-modu) — Plate Customization   | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.Footer-modul) | https://www.pragenhatlen.com/        │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 12px 168)   │
│ ====================================================================== │
│ [ HEADER BAR (<header.Header-module__t) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.HeroVideo-modul) — 390px Vertical Lead        | │
│ | H1: THE SCARCEST ASSET, ON YOUR WRIST                              | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.RotateScreen-) — 1-Col Stack              | │
│ | [ Item 1: The scarcest asset, on your wrist                      ] | │
│ | [ Item 2: Precision in every layer                               ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.RotateScreen-mo) — 1-Col (Plate Customizatio) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.Footer-modul) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.Header-module__top__mJsjm> — `www-pragenhatlen-com`)**:
   - Landmark `<header class="Header-module__top__mJsjm">` (`1440x76px`) hosting `Prägen Hätlen · Swiss watchmaking fo` navigation (`[02] A b o u t · [04] F A Q`), DOM attributes (`data-modal-id="cart"`, `data-lenis-prevent="true"`, `data-lenis-prevent="true"`, `data-lenis-prevent="true"`), and stylesheet rule `.App-module__root__JTuhI { background-color:var(--color-bg) }`.
2. **Hero Stage & Focal Lead (<section.HeroVideo-module__root__FiOC1> — `THE SCARCEST ASSET, ON YOUR WRIST`)**:
   - Landmark `<section class="HeroVideo-module__root__FiOC1">` presenting display lead `THE SCARCEST ASSET, ON YOUR WRIST` and copy excerpt *"Limited Edition. Swiss-made. Crypto Native"* over `#ecebea` canvas and `#0c1114` ink.
3. **Primary Showcase & Content Grid (<section.RotateScreen-module__root__m8vUV> — `The scarcest asset, on your wrist`)**:
   - Landmark `<section class="RotateScreen-module__root__m8vUV">` rendering section `The scarcest asset, on your wrist` with copy *"Prägen Hätlen introduces a new relationship between craftsmanship"*, asset references (`watch-background-drawing-D_cIL0zr...`, `cart-DdlU5Vpi.png`, `engrave_blue-Bx6rooYN.jpg`, `www.pragenhatlen.com`), and grid rule `.App-module__link__jsQ7Z { color:var(--color-black) }`.
4. **Interactive Detail & Feature Matrix (<section.RotateScreen-module__hidden__pMK7C> — `Precision in every layer`)**:
   - Landmark `<section class="RotateScreen-module__hidden__pMK7C">` framing `Precision in every layer` and `Plate Customization` (*"By scanning the watch crystal with a smartphone, collectors are c"*) with `#ffffff` surface cards, `#0000ff` accents, and `.App-module__link__jsQ7Z:hover { color:var(--color-blue-cher-ami) }`.
5. **Colophon & Global Directory Footer (<footer.Footer-module__root__oib9b> — `https://www.pragenhatlen.com/`)**:
   - Landmark `<footer class="Footer-module__root__oib9b">` anchoring `Prägen Hätlen · Swiss watchmakin` footer links (`[02] A b o u t · [04] F A Q`), copy *"Through this interaction, they can access the associated Pro"*, and `#ffffff` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `THE SCARCEST ASSET, ON YOUR WRIST` · sticky/fixed elements: `2`
- **Step 02** (`y=850px`, `5%`): Active landmark `Precision in every layer` · sticky/fixed elements: `2`
- **Step 03** (`y=3400px`, `22%`): Active landmark `Section @ 22%` · sticky/fixed elements: `2`
- **Step 04** (`y=5100px`, `32%`): Active landmark `By scanning the watch crystal with a smartphone,...` · sticky/fixed elements: `2`
- **Step 05** (`y=9350px`, `59%`): Active landmark `By scanning the watch crystal with a smartphone,...` · sticky/fixed elements: `2`
- **Step 06** (`y=11050px`, `70%`): Active landmark `By scanning the watch crystal with a smartphone,...` · sticky/fixed elements: `2`
- **Step 07** (`y=13600px`, `86%`): Active landmark `#place-your-interest` · sticky/fixed elements: `2`
- **Step 08** (`y=14400px`, `91%`): Active landmark `#place-your-interest` · sticky/fixed elements: `2`

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-pragenhatlen-com (Prägen Hätlen · Swiss watchmaking for the crypto community.)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-pragenhatlen-com` (**Prägen Hätlen · Swiss watchmaking for the crypto community.** — `https://www.pragenhatlen.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ecebea` / `#0000ff`).
- **Identity & Domain Context**: Trust, precision, resilience and uncompromising attention to detail.
- **Primary Substrate**: `#ecebea` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#0c1114`, **Accent / Highlight**: `#0000ff`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ecebea` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#0c1114` primary typography and `#0000ff` accents.
  - **Grounded Typographic Hierarchy**: Uses `Manrope` across display (`THE SCARCEST ASSET, ON YOUR WRIST`) and body copy, paired with `RedHatMono` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 12px 168px`, padding `32px`) with `cubic-bezier(.215,.61,.355,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-pragenhatlen-com` in your global stylesheet:

:root {
  /* Prägen Hätlen · Swiss watchmaking for the crypto community. (www-pragenhatlen-com) — Live-Grounded CSS Variables */
  --breakpoint-mobile: 320px; /* Dimension / Scale Token (www-pragenhatlen-com) */
  --breakpoint-mobile-horizontal: 500px; /* Dimension / Scale Token (www-pragenhatlen-com) */
  --breakpoint-tablet: 768px; /* Dimension / Scale Token (www-pragenhatlen-com) */
  --breakpoint-tablet-height: 950px; /* Layout / Spatial Grid Token (www-pragenhatlen-com) */
  --breakpoint-laptop: 1024px; /* Dimension / Scale Token (www-pragenhatlen-com) */
  --breakpoint-bigLaptop-min: 1366px; /* Dimension / Scale Token (www-pragenhatlen-com) */
  --breakpoint-bigLaptop: 1440px; /* Dimension / Scale Token (www-pragenhatlen-com) */
  --breakpoint-desktop: 1680px; /* Dimension / Scale Token (www-pragenhatlen-com) */
  --color-white: #fff; /* Canvas / Surface Token (www-pragenhatlen-com) */
  --color-white--40: #ffffff66; /* Canvas / Surface Token (www-pragenhatlen-com) */
  --color-white--16: #ffffff29; /* Canvas / Surface Token (www-pragenhatlen-com) */
  --color-white--4: #ffffff0a; /* Canvas / Surface Token (www-pragenhatlen-com) */
  --color-black: #000; /* Canvas / Surface Token (www-pragenhatlen-com) */
  --color-black--50: #00000080; /* Canvas / Surface Token (www-pragenhatlen-com) */
  --color-black--30: #0000004d; /* Canvas / Surface Token (www-pragenhatlen-com) */
  --color-black--24: #0000003d; /* Canvas / Surface Token (www-pragenhatlen-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ecebea` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#0c1114` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#ffffff` — grounded in `.BaseButton-module__white__qygOa { background-color: white }` (`#ffffff`)
- **Interactive Accent / Highlight**: `#0000ff` — grounded in `.App-module__link__jsQ7Z:hover { color: blue }` (`#0000ff`)
- **Secondary / Muted Copy**: `#ffffff` — grounded in live computed `p` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#ffffff` — grounded in `.StickyModal-module__header__LViCK { border-bottom: #ffffff }`
- **Variable Token (`--color-black`)**: `#000000` — grounded in `var(--color-black)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×872px` (full-page live capture (872px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `32px` lateral canvas padding with `12px 168px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 12px 168px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `32px` horizontal padding
- **Media Queries**: `@media (min-width: 768px) and (min-height: 500px) and (orientati...`, `@media (max-width: 768px)`, `@media (max-width: 768px) and (min-width: 768px) and (min-height...`, `@media (min-width: 768px)`
- **Corner Radii**: `var(--border-radius)`, `100%`, `1rem`, `4px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Manrope`
- **Body Font Stack**: `Manrope`
- **Monospace / Technical Font Stack**: `RedHatMono`
- **H1 Display Rule**: live computed `h1` (`font-size: 48px`, `line-height: 48px`, `font-weight: 500`)
- **H2 Section Rule**: live computed `h2` (`font-size: 36px`, `line-height: 39.6px`, `font-weight: 500`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 18.4px`, `font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 18.4px`, `font-weight: 400`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-pragenhatlen-com` (`Prägen Hätlen · Swiss watchmaking for the crypto community.`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.Header-module__top__mJsjm> — `www-pragenhatlen-com`)**:
   - DOM & Selectors: Landmark `<header class="Header-module__top__mJsjm">` (`1440x76px`) hosting `Prägen Hätlen · Swiss watchmaking fo` navigation (`[02] A b o u t · [04] F A Q`), DOM attributes (`data-modal-id="cart"`, `data-lenis-prevent="true"`, `data-lenis-prevent="true"`, `data-lenis-prevent="true"`), and stylesheet rule `.App-module__root__JTuhI { background-color:var(--color-bg) }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.Header-module__top__mJsjm> — `www-pragenhatlen-com`)` (`www-pragenhatlen-com`) adapts across `@media (min-width: 768px) and (min-height: 500px) and (orientati...`, `@media (max-width: 768px)`, `@media (max-width: 768px) and (min-width: 768px) and (min-height...`, `@media (min-width: 768px)` with `cubic-bezier(.215,.61,.355,1)` transitions and links `[02] A b o u t · [04] F A Q`.
2. **Hero Stage & Focal Lead (<section.HeroVideo-module__root__FiOC1> — `THE SCARCEST ASSET, ON YOUR WRIST`)**:
   - DOM & Selectors: Landmark `<section class="HeroVideo-module__root__FiOC1">` presenting display lead `THE SCARCEST ASSET, ON YOUR WRIST` and copy excerpt *"Limited Edition. Swiss-made. Crypto Native"* over `#ecebea` canvas and `#0c1114` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×872px` mobile) sets `#ecebea` background with `#0c1114` headline `THE SCARCEST ASSET, ON YOUR WRIST`.
3. **Primary Showcase & Content Grid (<section.RotateScreen-module__root__m8vUV> — `The scarcest asset, on your wrist`)**:
   - DOM & Selectors: Landmark `<section class="RotateScreen-module__root__m8vUV">` rendering section `The scarcest asset, on your wrist` with copy *"Prägen Hätlen introduces a new relationship between craftsmanship"*, asset references (`watch-background-drawing-D_cIL0zr...`, `cart-DdlU5Vpi.png`, `engrave_blue-Bx6rooYN.jpg`, `www.pragenhatlen.com`), and grid rule `.App-module__link__jsQ7Z { color:var(--color-black) }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.RotateScreen-module__root__m8vUV> — `The scarcest asset, on your wrist`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 12px 168px`) on desktop and Single-column vertical stack at `390px` viewport width with `32px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.RotateScreen-module__hidden__pMK7C> — `Precision in every layer`)**:
   - DOM & Selectors: Landmark `<section class="RotateScreen-module__hidden__pMK7C">` framing `Precision in every layer` and `Plate Customization` (*"By scanning the watch crystal with a smartphone, collectors are c"*) with `#ffffff` surface cards, `#0000ff` accents, and `.App-module__link__jsQ7Z:hover { color:var(--color-blue-cher-ami) }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.RotateScreen-module__hidden__pMK7C> — `Precision in every layer`)` uses `var(--border-radius)`, `100%`, `1rem`, `4px` radii, `#0000ff` highlights, and assets (watch-background-drawing-D_cIL0zr..., cart-DdlU5Vpi.png, engrave_blue-Bx6rooYN.jpg).
5. **Colophon & Global Directory Footer (<footer.Footer-module__root__oib9b> — `https://www.pragenhatlen.com/`)**:
   - DOM & Selectors: Landmark `<footer class="Footer-module__root__oib9b">` anchoring `Prägen Hätlen · Swiss watchmakin` footer links (`[02] A b o u t · [04] F A Q`), copy *"Through this interaction, they can access the associated Pro"*, and `#ffffff` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.Footer-module__root__oib9b> — `https://www.pragenhatlen.com/`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `32px` lateral canvas padding with `12px 168px` grid gap and attributes (data-modal-id="cart", data-lenis-prevent="true", data-lenis-prevent="true").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Limited Edition. Swiss-made. Crypto Native"*
- Copy Excerpt 2: *"Prägen Hätlen introduces a new relationship between craftsmanship, digital identit..."*
- Copy Excerpt 3: *"By scanning the watch crystal with a smartphone, collectors are connected to its d..."*
- Copy Excerpt 4: *"Through this interaction, they can access the associated Proof of Collection NFT,..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.215,.61,.355,1)`
- **Extracted Stylesheet Rules (`www-pragenhatlen-com`)**:
- `.App-module__root__JTuhI { background-color:var(--color-bg) }`
- `.App-module__link__jsQ7Z { color:var(--color-black) }`
- `.App-module__link__jsQ7Z:hover { color:var(--color-blue-cher-ami) }`
- `.Loader-module__background__Nbt4d { position:absolute;top:50%;left:50%;-webkit-transform:translate(-50%,-50%... }`
- `.Loader-module__background__Nbt4d... { width:auto;height:72vh }`
- **Per-Selector Transition Rules**:
- **Selector `.Header-module__top__mJsjm`**: `transition: .5s ease color` extracted from `www-pragenhatlen-com` stylesheet.
- **Selector `.Header-module__top_open__BgPji`**: `transition: unset` extracted from `www-pragenhatlen-com` stylesheet.
- **Selector `media (hover: hover)`**: `transition: .25s cubic-bezier(.215,.61,.355,1) opacity` extracted from `www-pragenhatlen-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.215,.61,.355,1)`)**: Governs interactive state transitions across `<header.Header-module__top__mJsjm>` and `<section.RotateScreen-module__root__m8vUV>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `16667px` across 8 distinct viewport chapters using Lenis, GSAP/ScrollTrigger, WebGL/Canvas.
- **Vertical Chapter Sequence**: THE SCARCEST ASSET, ON YOUR... (0%) -> Precision in every layer (5%) -> Section @ 22% (22%) -> By scanning the watch cryst... (32%) -> By scanning the watch cryst... (59%) -> By scanning the watch cryst... (70%) -> #place-your-interest (86%) -> #place-your-interest (91%).

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-pragenhatlen-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | THE SCARCEST ASSET, ON YOUR WRIST | `2` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `5%` | Precision in every layer | `2` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `3400px` | `22%` | Section @ 22% | `2` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `5100px` | `32%` | By scanning the watch crystal with a smartpho... | `2` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `9350px` | `59%` | By scanning the watch crystal with a smartpho... | `2` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `11050px` | `70%` | By scanning the watch crystal with a smartpho... | `2` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `13600px` | `86%` | #place-your-interest | `2` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `14400px` | `91%` | #place-your-interest | `2` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | Hero | [mobile-step-01.webp](assets/mobile-step-01.webp) |

