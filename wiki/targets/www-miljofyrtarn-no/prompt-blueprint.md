---
title: "UI Prompt Blueprint: www-miljofyrtarn-no"
date: 2026-11-24
captured_at: 2026-11-24
target: "www-miljofyrtarn-no"
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
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#00aceb` accent)"
---

# UI Design System & Master Generation Blueprint: www-miljofyrtarn-no

> **Hjem · Miljøfyrtårn** (https://www.miljofyrtarn.no/) — Miljøfyrtårn er Norges ledende miljøsertifisering. Kom i gang med sertifisering og miljøledelse i LUMA – et verktøy som gjør arbeidet enk...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Hjem · Miljøfyrtårn** (`https://www.miljofyrtarn.no/`). Miljøfyrtårn er Norges ledende miljøsertifisering. Kom i gang med sertifisering og miljøledelse i LUMA – et verktøy som gjør arbeidet enk...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#00aceb` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#00aceb` accents.
  - **Grounded Typographic Hierarchy**: Uses `matterFont` across display (`Norges mest brukte miljøsertifiserin`) and body copy, paired with `SFMono-Regular` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `120rem` container bounds (`gap: var(--spacing)`, padding `var(--lines-gutter)`) with `cubic-bezier(0,0,.2,1)` easing and Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=14400px` / doc `17284px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `120rem` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `var(--lines-gutter)` lateral canvas padding with `var(--spacing)` grid gap.
- **Border Radius Scale**: `.25rem`, `1.2rem`, `1.05rem`, `20px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 120rem`, `gap: var(--spacing)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--lines-gutter)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:30rem)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e6e6e6` | `.bg-grey-20 { background-color: #e6e6e6 }` |
| **Interactive Accent / Highlight** | `#00aceb` | `stom-button.button-light .icon... { color: #00aceb }` |
| **Secondary / Muted Copy** | `#00aceb` | `stom-button.button-light .icon... { color: #00aceb }` |
| **Structural Hairline Border** | `#e5e5e5` | `10 { border-color: #e5e5e5 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--lines-gutter` | `clamp(.9rem, 1.11vw, 1.25rem)` | Layout / Spatial Grid Token |
| `--media-max-h` | `calc(100svh - 4.5rem - 3.25rem)` | Dimension / Scale Token |
| `--media-caption-h` | `4rem` | Dimension / Scale Token |
| `--media-min-w` | `24rem` | Dimension / Scale Token |
| `--font-matter` | `"matterFont", "matterFont Fallback"` | Typography / Scale Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-xl` | `36rem` | Layout / Spatial Grid Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--font-weight-semibold` | `600` | Typography / Scale Token |
| `--font-weight-bold` | `700` | Typography / Scale Token |
| `--leading-tight` | `1.25` | Typography / Scale Token |
| `--leading-normal` | `1.5` | Typography / Scale Token |
| `--radius-md` | `.375rem` | Elevation / Border Token |
| `--radius-lg` | `.5rem` | Elevation / Border Token |
| `--radius-xl` | `.75rem` | Elevation / Border Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `matterFont`.
- **Primary Body Stack**: `matterFont`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 87.984px`, `line-height: 87.984px`, `font-weight: 400`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 63.936px`, `line-height: 63.936px`, `font-weight: 400`); rule `h2` (`font-size: 1.75rem`, `line-height: 1`).
- **Body Copy**: live computed `body` (`font-size: 15.984px`, `line-height: 23.976px`, `font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 15.984px`, `line-height: 23.976px`, `font-weight: 400`); CSS variables `--media-caption-h: 4rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `www-miljofyrtarn-no` stylesheet.
- **Selector `.custom-underline:after`**: `transition: .3s` extracted from `www-miljofyrtarn-no` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-miljofyrtarn-no` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<nav.top-bar>` and `<section.image-fullscreen>`.
- **Runtime Interaction Engine**: Integrates Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `17284px`, deepest scrollY reached `14400px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `GSAP/ScrollTrigger`.
- **Hover Physics (`primary_cta` · `Se flere kundehistorier`)**: Computed transition `0s` / `ease` (no static color/transform shift captured at rest).
- **Route Transition Architecture**: First internal navigation (`/om-oss/bli-kjent-med-vare-ansatte`) measured as `direct` in `1769ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Hjem · Miljøfyrtårn                        │
│ ====================================================================== │
│ [ <nav.top-bar> (1440x96px)           | Interaktiv veiviser · Start  ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.stage> (w=1440px)                             | │
│ | H1: Norges mest brukte miljøsertifisering                          | │
│ | Substrate: #ffffff | Ink: #000000 | Accent: #00aceb                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.image-fullscreen>) max-w: 120rem           | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Fordi bærekraft er konkurran |  | Fornøyde kunder sier         | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.image-group>) — Hvorfor bli Miljøfyrt      | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.lines-scope>) | https://www.miljofyrtarn.no/         │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--sp)   │
│ ====================================================================== │
│ [ HEADER BAR (<nav.top-bar>           ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.stage>) — 390px Vertical Lead                 | │
│ | H1: Norges mest brukte miljøsertifisering                          | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.image-fullscr) — 1-Col Stack              | │
│ | [ Item 1: Fordi bærekraft er konkurransekraft                    ] | │
│ | [ Item 2: Fornøyde kunder sier                                   ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.image-group>) — 1-Col (Hvorfor bli Miljøf)  | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.lines-scope>) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.top-bar> — `www-miljofyrtarn-no`)**:
   - Landmark `<nav class="top-bar pointer-events-none">` (`1440x96px`) hosting `Hjem · Miljøfyrtårn` navigation (`Interaktiv veiviser · Start registrering · Finn konsulent · Kundehistorier · Om oss Om oss`), DOM attributes (`data-precedence="next"`, `data-href="/_next/static/chunks/..."`, `data-dgst`, `data-section="0"`), and stylesheet rule `._5KZDLG_className { font-family:matterFont,matterFont Fallback }`.
2. **Hero Stage & Focal Lead (<section.stage> — `Norges mest brukte miljøsertifiser`)**:
   - Landmark `<section class="stage relative">` presenting display lead `Norges mest brukte miljøsertifisering` and copy excerpt *"Bli Miljøfyrtårn? Prøv vår interaktive veiviser!"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.image-fullscreen> — `Fordi bærekraft er konkurransekraf`)**:
   - Landmark `<section class="image-fullscreen lines-scope">` rendering section `Fordi bærekraft er konkurransekraft` with copy *"Norges mest brukte miljøsertifisering"*, asset references (`MatterMedium-s.p.07t3y7_ykvrde.woff2`, `MatterRegular-s.p.3jjuiv35wp9rz.w...`, `MatterRegularItalic-s.p.03ktjrzd9...`, `MatterSemiBold-s.p.1twnp8ioanuv2....`), and grid rule `._5KZDLG_variable { --font-matter:"matterFont", "matterFont Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.image-group> — `Fornøyde kunder sier`)**:
   - Landmark `<section class="image-group lines-scope">` framing `Fornøyde kunder sier` and `Hvorfor bli Miljøfyrtårn` (*"Norges mest brukte"*) with `#e6e6e6` surface cards, `#00aceb` accents, and `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.lines-scope> — `https://www.miljofyrtarn.no/`)**:
   - Landmark `<footer class="lines-scope overflow-clip">` anchoring `Hjem · Miljøfyrtårn` footer links (`Interaktiv veiviser · Start registrering · Finn konsulent · Kundehistorier · Om oss Om oss`), copy *"miljøsertifisering"*, and `#e5e5e5` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `Norges mest brukte miljøsertifisering` · sticky/fixed elements: `2`
- **Step 02** (`y=850px`, `5%`): Active landmark `Fordi bærekraft er konkurransekraft` · sticky/fixed elements: `1`
- **Step 03** (`y=3400px`, `21%`): Active landmark `Fornøyde kunder sier` · sticky/fixed elements: `1`
- **Step 04** (`y=5950px`, `36%`): Active landmark `Hvorfor bli Miljøfyrtårn` · sticky/fixed elements: `1`
- **Step 05** (`y=8500px`, `52%`): Active landmark `Kundehistorier` · sticky/fixed elements: `1`
- **Step 06** (`y=11050px`, `67%`): Active landmark `Aktuelt` · sticky/fixed elements: `1`
- **Step 07** (`y=13600px`, `83%`): Active landmark `Kurs og webinarer` · sticky/fixed elements: `1`
- **Step 08** (`y=14400px`, `88%`): Active landmark `Kurs og webinarer` · sticky/fixed elements: `1`

### Multi-Page Internal Route Map
- **Detail Route (`/om-oss/bli-kjent-med-vare-ansatte`)**: `https://www.miljofyrtarn.no/om-oss/bli-kjent-med-vare-ansatte` — H1: `Bli kjent med våre ansatte`, scrollHeight `3355px`, transition `direct` (`1769ms`)
- **Detail Route (`/bli-miljofyrtarn/baerekraftsverktoyet-luma`)**: `https://www.miljofyrtarn.no/bli-miljofyrtarn/baerekraftsverktoyet-luma` — H1: `LUMA, Miljøfyrtårns bærekraftsverktøy`, scrollHeight `7777px`, transition `direct` (`813ms`)
- **Detail Route (`/bli-miljofyrtarn/miljofyrtarn-og-anbud`)**: `https://www.miljofyrtarn.no/bli-miljofyrtarn/miljofyrtarn-og-anbud` — H1: `Miljøfyrtårn og anbud`, scrollHeight `4416px`, transition `direct` (`2002ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-miljofyrtarn-no (Hjem · Miljøfyrtårn)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-miljofyrtarn-no` (**Hjem · Miljøfyrtårn** — `https://www.miljofyrtarn.no/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#00aceb` accent).
- **Identity & Domain Context**: Miljøfyrtårn er Norges ledende miljøsertifisering. Kom i gang med sertifisering og miljøledelse i LUMA – et verktøy som gjør arbeidet enk...
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#00aceb`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#00aceb` accents.
  - **Grounded Typographic Hierarchy**: Uses `matterFont` across display (`Norges mest brukte miljøsertifiserin`) and body copy, paired with `SFMono-Regular` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `120rem` container bounds (`gap: var(--spacing)`, padding `var(--lines-gutter)`) with `cubic-bezier(0,0,.2,1)` easing and Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-miljofyrtarn-no` in your global stylesheet:

:root {
  /* Hjem · Miljøfyrtårn (www-miljofyrtarn-no) — Live-Grounded CSS Variables */
  --lines-gutter: clamp(.9rem, 1.11vw, 1.25rem); /* Layout / Spatial Grid Token (www-miljofyrtarn-no) */
  --media-max-h: calc(100svh - 4.5rem - 3.25rem); /* Dimension / Scale Token (www-miljofyrtarn-no) */
  --media-caption-h: 4rem; /* Dimension / Scale Token (www-miljofyrtarn-no) */
  --media-min-w: 24rem; /* Dimension / Scale Token (www-miljofyrtarn-no) */
  --font-matter: "matterFont", "matterFont Fallback"; /* Typography / Scale Token (www-miljofyrtarn-no) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (www-miljofyrtarn-no) */
  --container-xl: 36rem; /* Layout / Spatial Grid Token (www-miljofyrtarn-no) */
  --font-weight-normal: 400; /* Typography / Scale Token (www-miljofyrtarn-no) */
  --font-weight-medium: 500; /* Typography / Scale Token (www-miljofyrtarn-no) */
  --font-weight-semibold: 600; /* Typography / Scale Token (www-miljofyrtarn-no) */
  --font-weight-bold: 700; /* Typography / Scale Token (www-miljofyrtarn-no) */
  --leading-tight: 1.25; /* Typography / Scale Token (www-miljofyrtarn-no) */
  --leading-normal: 1.5; /* Typography / Scale Token (www-miljofyrtarn-no) */
  --radius-md: .375rem; /* Elevation / Border Token (www-miljofyrtarn-no) */
  --radius-lg: .5rem; /* Elevation / Border Token (www-miljofyrtarn-no) */
  --radius-xl: .75rem; /* Elevation / Border Token (www-miljofyrtarn-no) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#e6e6e6` — grounded in `.bg-grey-20 { background-color: #e6e6e6 }`
- **Interactive Accent / Highlight**: `#00aceb` — grounded in `stom-button.button-light .icon... { color: #00aceb }`
- **Secondary / Muted Copy**: `#00aceb` — grounded in `stom-button.button-light .icon... { color: #00aceb }`
- **Structural Hairline Border**: `#e5e5e5` — grounded in `10 { border-color: #e5e5e5 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `120rem` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `var(--lines-gutter)` lateral canvas padding with `var(--spacing)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 120rem`, `gap: var(--spacing)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--lines-gutter)` horizontal padding
- **Media Queries**: `@media (min-width:30rem)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`
- **Corner Radii**: `.25rem`, `1.2rem`, `1.05rem`, `20px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `matterFont`
- **Body Font Stack**: `matterFont`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: live computed `h1` (`font-size: 87.984px`, `line-height: 87.984px`, `font-weight: 400`)
- **H2 Section Rule**: live computed `h2` (`font-size: 63.936px`, `line-height: 63.936px`, `font-weight: 400`); rule `h2` (`font-size: 1.75rem`, `line-height: 1`)
- **Body Copy Rule**: live computed `body` (`font-size: 15.984px`, `line-height: 23.976px`, `font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 15.984px`, `line-height: 23.976px`, `font-weight: 400`); CSS variables `--media-caption-h: 4rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-miljofyrtarn-no` (`Hjem · Miljøfyrtårn`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.top-bar> — `www-miljofyrtarn-no`)**:
   - DOM & Selectors: Landmark `<nav class="top-bar pointer-events-none">` (`1440x96px`) hosting `Hjem · Miljøfyrtårn` navigation (`Interaktiv veiviser · Start registrering · Finn konsulent · Kundehistorier · Om oss Om oss`), DOM attributes (`data-precedence="next"`, `data-href="/_next/static/chunks/..."`, `data-dgst`, `data-section="0"`), and stylesheet rule `._5KZDLG_className { font-family:matterFont,matterFont Fallback }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.top-bar> — `www-miljofyrtarn-no`)` (`www-miljofyrtarn-no`) adapts across `@media (min-width:30rem)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)` transitions and links `Interaktiv veiviser · Start registrering · Finn konsulent · Kundehistorier · Om oss Om oss`.
2. **Hero Stage & Focal Lead (<section.stage> — `Norges mest brukte miljøsertifiser`)**:
   - DOM & Selectors: Landmark `<section class="stage relative">` presenting display lead `Norges mest brukte miljøsertifisering` and copy excerpt *"Bli Miljøfyrtårn? Prøv vår interaktive veiviser!"* over `#ffffff` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#ffffff` background with `#000000` headline `Norges mest brukte miljøsertifisering`.
3. **Primary Showcase & Content Grid (<section.image-fullscreen> — `Fordi bærekraft er konkurransekraf`)**:
   - DOM & Selectors: Landmark `<section class="image-fullscreen lines-scope">` rendering section `Fordi bærekraft er konkurransekraft` with copy *"Norges mest brukte miljøsertifisering"*, asset references (`MatterMedium-s.p.07t3y7_ykvrde.woff2`, `MatterRegular-s.p.3jjuiv35wp9rz.w...`, `MatterRegularItalic-s.p.03ktjrzd9...`, `MatterSemiBold-s.p.1twnp8ioanuv2....`), and grid rule `._5KZDLG_variable { --font-matter:"matterFont", "matterFont Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.image-fullscreen> — `Fordi bærekraft er konkurransekraf`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 120rem`, `gap: var(--spacing)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--lines-gutter)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.image-group> — `Fornøyde kunder sier`)**:
   - DOM & Selectors: Landmark `<section class="image-group lines-scope">` framing `Fornøyde kunder sier` and `Hvorfor bli Miljøfyrtårn` (*"Norges mest brukte"*) with `#e6e6e6` surface cards, `#00aceb` accents, and `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.image-group> — `Fornøyde kunder sier`)` uses `.25rem`, `1.2rem`, `1.05rem`, `20px` radii, `#00aceb` highlights, and assets (MatterMedium-s.p.07t3y7_ykvrde.woff2, MatterRegular-s.p.3jjuiv35wp9rz.w..., MatterRegularItalic-s.p.03ktjrzd9...).
5. **Colophon & Global Directory Footer (<footer.lines-scope> — `https://www.miljofyrtarn.no/`)**:
   - DOM & Selectors: Landmark `<footer class="lines-scope overflow-clip">` anchoring `Hjem · Miljøfyrtårn` footer links (`Interaktiv veiviser · Start registrering · Finn konsulent · Kundehistorier · Om oss Om oss`), copy *"miljøsertifisering"*, and `#e5e5e5` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.lines-scope> — `https://www.miljofyrtarn.no/`)` aligns to `120rem` (non-`@media` desktop container stylesheet rule) with `var(--lines-gutter)` lateral canvas padding with `var(--spacing)` grid gap and attributes (data-precedence="next", data-href="/_next/static/chunks/...", data-dgst).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Bli Miljøfyrtårn? Prøv vår interaktive veiviser!"*
- Copy Excerpt 2: *"Norges mest brukte miljøsertifisering"*
- Copy Excerpt 3: *"Norges mest brukte"*
- Copy Excerpt 4: *"miljøsertifisering"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`
- **Extracted Stylesheet Rules (`www-miljofyrtarn-no`)**:
- `._5KZDLG_className { font-family:matterFont,matterFont Fallback }`
- `._5KZDLG_variable { --font-matter:"matterFont", "matterFont Fallback" }`
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `www-miljofyrtarn-no` stylesheet.
- **Selector `.custom-underline:after`**: `transition: .3s` extracted from `www-miljofyrtarn-no` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-miljofyrtarn-no` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<nav.top-bar>` and `<section.image-fullscreen>`.
- **Runtime Interaction Engine**: Integrates Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `17284px` across 8 distinct viewport chapters using GSAP/ScrollTrigger.
- **Vertical Chapter Sequence**: Norges mest brukte miljøser... (0%) -> Fordi bærekraft er konkurra... (5%) -> Fornøyde kunder sier (21%) -> Hvorfor bli Miljøfyrtårn (36%) -> Kundehistorier (52%) -> Aktuelt (67%) -> Kurs og webinarer (83%) -> Kurs og webinarer (88%).
- **Multi-Page Routes**: Scaffold internal routes `/om-oss/bli-kjent-med-vare-ansatte` (detail, direct), `/bli-miljofyrtarn/baerekraftsverktoyet-luma` (detail, direct), `/bli-miljofyrtarn/miljofyrtarn-og-anbud` (detail, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-miljofyrtarn-no`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | Norges mest brukte miljøsertifisering | `2` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `5%` | Fordi bærekraft er konkurransekraft | `1` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `3400px` | `21%` | Fornøyde kunder sier | `1` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `5950px` | `36%` | Hvorfor bli Miljøfyrtårn | `1` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `8500px` | `52%` | Kundehistorier | `1` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `11050px` | `67%` | Aktuelt | `1` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `13600px` | `83%` | Kurs og webinarer | `1` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `14400px` | `88%` | Kurs og webinarer | `1` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | Norges mest brukte miljøsertifisering | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `5027px` | `50%` | Slik får Mestergruppen miljøledelse til å... | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `10055px` | `100%` | Hjelp | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `detail` | `https://www.miljofyrtarn.no/om-oss/bli-kjent-med-vare-ansatte` | Bli kjent med våre ansatte | `3355px` | `direct` (`1769ms`) | [subpage-01-om-oss-bli-kjent-med-vare-ansatte.webp](assets/subpage-01-om-oss-bli-kjent-med-vare-ansatte.webp) |
| `2` | `detail` | `https://www.miljofyrtarn.no/bli-miljofyrtarn/baerekraftsverktoyet-luma` | LUMA, Miljøfyrtårns bærekraftsverktøy | `7777px` | `direct` (`813ms`) | [subpage-02-bli-miljofyrtarn-baerekraftsverktoye.webp](assets/subpage-02-bli-miljofyrtarn-baerekraftsverktoye.webp) |
| `3` | `detail` | `https://www.miljofyrtarn.no/bli-miljofyrtarn/miljofyrtarn-og-anbud` | Miljøfyrtårn og anbud | `4416px` | `direct` (`2002ms`) | [subpage-03-bli-miljofyrtarn-miljofyrtarn-og-anb.webp](assets/subpage-03-bli-miljofyrtarn-miljofyrtarn-og-anb.webp) |

