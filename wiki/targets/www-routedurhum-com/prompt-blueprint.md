---
title: "UI Prompt Blueprint: www-routedurhum-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "www-routedurhum-com"
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
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#fcf150` accent)"
---

# UI Design System & Master Generation Blueprint: www-routedurhum-com

> **Route du Rhum 2026 – Destination Guadeloupe · Site Officiel** (https://www.routedurhum.com/) — Suivez la Route du Rhum, course légendaire entre Saint-Malo et la Guadeloupe. Skippers, actualités, villages de Saint-Malo à la Guadeloupe.

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Route du Rhum 2026 – Destination Guadeloupe · Site Officiel** (`https://www.routedurhum.com/`). Suivez la Route du Rhum, course légendaire entre Saint-Malo et la Guadeloupe. Skippers, actualités, villages de Saint-Malo à la Guadeloupe.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#fcf150` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `browser-default` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#fcf150` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Montserrat` for display copy (`Route du Rhum, Destination Guadeloup`) with `Varien`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 8px`, padding `12px`) with `cubic-bezier(.83,0,.17,1)` easing and Swiper Touch Carousel Engine, Lottie Vector Animation Player.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=10971px` / doc `11876px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `12px` lateral canvas padding with `8px` grid gap.
- **Border Radius Scale**: `6px`, `50%`, `var(--corvid-border-radius)`, `24px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 8px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `12px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:1025px)`, `@media (max-width:750px)`, `@media (max-width:760px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f2f6f9` | `var(--rn-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#fcf150` | `rdr-dernieres-infos .rdi-badge-... { background: #fcf150 }` |
| **Secondary / Muted Copy** | `#7b8aa0` | `var(--ink-3)` in `:root` |
| **Structural Hairline Border** | `#e1e6ee` | `var(--line)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--one-unit` | `1vw` | Dimension / Scale Token |
| `--section-max-width` | `9999px` | Layout / Spatial Grid Token |
| `--spx-stopper-max` | `9999px` | Dimension / Scale Token |
| `--spx-stopper-min` | `0px` | Dimension / Scale Token |
| `--browser-zoom` | `1` | Design System Custom Token |
| `--wst-button-color-fill-primary` | `rgb(var(--color_48))` | Brand / Palette Token |
| `--wst-button-color-border-primary` | `rgb(var(--color_49))` | Brand / Palette Token |
| `--wst-button-color-text-primary` | `rgb(var(--color_50))` | Typography Ink Token |
| `--wst-button-color-fill-primary-hover` | `rgb(var(--color_51))` | Brand / Palette Token |
| `--wst-button-color-border-primary-hover` | `rgb(var(--color_52))` | Brand / Palette Token |
| `--wst-button-color-text-primary-hover` | `rgb(var(--color_53))` | Typography Ink Token |
| `--wst-button-color-fill-primary-disabled` | `rgb(var(--color_54))` | Brand / Palette Token |
| `--wst-button-color-border-primary-disabled` | `rgb(var(--color_55))` | Brand / Palette Token |
| `--wst-button-color-text-primary-disabled` | `rgb(var(--color_56))` | Typography Ink Token |
| `--wst-button-color-fill-secondary` | `rgb(var(--color_57))` | Brand / Palette Token |
| `--wst-button-color-border-secondary` | `rgb(var(--color_58))` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Montserrat`.
- **Primary Body Stack**: `Varien`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 20px`, `line-height: normal`, `font-weight: 700`); CSS variables `--display: inline-block`, `--comp-display: unset`, `--container-display: grid`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 63.36px`, `line-height: 65.2608px`, `font-weight: 700`); CSS variables `--wst-font-style-h2: var(--font_2)`, `--item-depth2-direction: inherit`, `--item-depth2-align: inherit`; rule `h2` (`font-size: clamp(34px,min(4.6vw,7.4vh),7...`, `line-height: 1.1`).
- **Body Copy**: live computed `body` (`font-size: 10px`, `line-height: normal`, `font-weight: 400`); CSS variables `--wst-font-style-body-large: var(--font_7)`, `--wst-font-style-body-medium: var(--font_8)`, `--wst-font-style-body-small: var(--font_9)`; rule `p` (`font-size: 13px`, `line-height: 1.5`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 10px`, `line-height: normal`, `font-weight: 400`); CSS variables `--wst-font-style-body-small: var(--font_9)`, `--wst-font-style-body-x-small: var(--font_10)`; rule `small` (`letter-spacing: 0`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.83,0,.17,1)`, `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.64,0,.78,0)`.

### Per-Element Transition & Choreography Rules
- **Selector `id^=oldHoverBox-]`**: `transition: opacity .5s,visibility .5s` extracted from `www-routedurhum-com` stylesheet.
- **Selector `access-widget-ui::part(acsb-trigger)`**: `transition: width .2s cubic-bezier(.83,0,.17,1) !important` extracted from `www-routedurhum-com` stylesheet.
- **Selector `media (prefers-reduced-motion:red...`**: `transition: none !important` extracted from `www-routedurhum-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.83,0,.17,1)`)**: Governs interactive state transitions across `<header.gt>` and `<section.em>`.
- **Runtime Interaction Engine**: Integrates Swiper Touch Carousel Engine, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `11876px`, deepest scrollY reached `10971px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: Native browser scroll / standard CSS transitions.
- **Nav / Drawer Probe (`Plus de pages Actualités`)**: Triggered visual change (pixel diff `91.111`, captured in `assets/state-nav.webp`); revealed links: LA BOUTIQUE OFFICIELL..., JOUER (NOUVEL ONGLET).
- **Hover Physics (`primary_cta` · `Lire l’article`)**: Computed transition `0.15s, 0.15s, 0.15s` / `ease, ease, ease` (no static color/transform shift captured at rest).
- **Interactive Control Probe (`tab` · `1`)**: Triggered visual diff `26.374` (attr `false -> true`, captured in `assets/state-interactive.webp`).
- **Route Transition Architecture**: First internal navigation (`/nos-partenaires/r%C3%A9gion-guadeloupe`) measured as `direct` in `1842ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Route du Rhum 2026 – Destination Guadeloup │
│ ====================================================================== │
│ [ <header.gt> (1440px)                | Cartographie Carto · Classem ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.ke5pl1> (w=1440px)                            | │
│ | H1: Route du Rhum, Destination Guadeloupe                          | │
│ | Substrate: #ffffff | Ink: #000000 | Accent: #fcf150                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.em>) max-w: 1440px                         | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Saint-Malo est en fête !     |  | Jean Le Cam, le retour du Ro | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.hero>) — Se souvenir des belle             | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.comp-mmxzg4m) | https://www.routedurhum.com/         │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 8px)        │
│ ====================================================================== │
│ [ HEADER BAR (<header.gt>             ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.ke5pl1>) — 390px Vertical Lead                | │
│ | H1: Route du Rhum, Destination Guadeloupe                          | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.em>) — 1-Col Stack                        | │
│ | [ Item 1: Saint-Malo est en fête !                               ] | │
│ | [ Item 2: Jean Le Cam, le retour du Roi                          ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.hero>) — 1-Col (Se souvenir des be)         | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.comp-mmxzg4m) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.gt> — `www-routedurhum-com`)**:
   - Landmark `<header class="gt est-pause">` (`1440px`) hosting `Route du Rhum 2026 – Destination Gua` navigation (`Cartographie Carto · Classement`), DOM attributes (`data-rdr-entete="dessus"`, `data-url="https://static.parast..."`, `data-url="https://static.parast..."`, `data-url="https://static.parast..."`), and stylesheet rule `root:active-view-transition { view-transition-name:none }`.
2. **Hero Stage & Focal Lead (<section.ke5pl1> — `Route du Rhum, Destination Guadelo`)**:
   - Landmark `<section class="ke5pl1 comp-muf996vx">` presenting display lead `Route du Rhum, Destination Guadeloupe` and copy excerpt *"ARRIVÉES EN GUADELOUPE · COMMENT LES SUIVRE EN COURSE SUIVEZ LA F"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.em> — `Saint-Malo est en fête !`)**:
   - Landmark `<section class="em">` rendering section `Saint-Malo est en fête !` with copy *"Là où les rêves prennent le large"*, asset references (`7bb303_9e59bb8f77444a2fbb905831b5...`, `minified.js`, `focus-within-polyfill.js`, `cdn.jsdelivr.net`), and grid rule `root::view-transition { pointer-events:none }`.
4. **Interactive Detail & Feature Matrix (<section.hero> — `Jean Le Cam, le retour du Roi`)**:
   - Landmark `<section class="hero est-photo">` framing `Jean Le Cam, le retour du Roi` and `Se souvenir des belles choses` (*"Route du Rhum Destination Guadeloupe Départ le dimanche 1 er nove"*) with `#f2f6f9` surface cards, `#fcf150` accents, and `SITE_HEADER { view-transition-name:header-group }`.
5. **Colophon & Global Directory Footer (<footer.comp-mmxzg4ms> — `https://www.routedurhum.com/`)**:
   - Landmark `<footer class="comp-mmxzg4ms S829f_">` anchoring `Route du Rhum 2026 – Destination` footer links (`Cartographie Carto · Classement`), copy *"Route du Rhum Destination Guadeloupe"*, and `#e1e6ee` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `JEAN LE CAM, LE RETOUR DU ROI` · sticky/fixed elements: `0`
- **Step 02** (`y=850px`, `8%`): Active landmark `LA COURSE EN DIRECT` · sticky/fixed elements: `0`
- **Step 03** (`y=2550px`, `23%`): Active landmark `🎥 LES NOUVELLES DU BORD EN VIDÉO` · sticky/fixed elements: `0`
- **Step 04** (`y=4250px`, `39%`): Active landmark `VIVEZ VOTRE RHUM` · sticky/fixed elements: `0`
- **Step 05** (`y=6800px`, `62%`): Active landmark `TYMAL EST SUR LE VILLAGE` · sticky/fixed elements: `0`
- **Step 06** (`y=8500px`, `77%`): Active landmark `#comp-mmxzg4ms_r_comp-mm3m1ky0` · sticky/fixed elements: `0`
- **Step 07** (`y=10200px`, `93%`): Active landmark `Footer` · sticky/fixed elements: `0`
- **Step 08** (`y=10971px`, `100%`): Active landmark `Footer` · sticky/fixed elements: `0`

### Multi-Page Internal Route Map
- **Detail Route (`/nos-partenaires/r%C3%A9gion-guadeloupe`)**: `https://www.routedurhum.com/nos-partenaires/r%C3%A9gion-guadeloupe` — H1: `RÉGION GUADELOUPE`, scrollHeight `5993px`, transition `direct` (`1842ms`)
- **About Route (`/contact`)**: `https://www.routedurhum.com/contact` — H1: `CONTACT`, scrollHeight `5090px`, transition `direct` (`591ms`)
- **Detail Route (`/nos-partenaires/ville-de-saint-malo`)**: `https://www.routedurhum.com/nos-partenaires/ville-de-saint-malo` — H1: `VILLE DE SAINT-MALO`, scrollHeight `5767px`, transition `direct` (`3185ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-routedurhum-com (Route du Rhum 2026 – Destination Guadeloupe · Site Officiel)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-routedurhum-com` (**Route du Rhum 2026 – Destination Guadeloupe · Site Officiel** — `https://www.routedurhum.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#fcf150` accent).
- **Identity & Domain Context**: Suivez la Route du Rhum, course légendaire entre Saint-Malo et la Guadeloupe. Skippers, actualités, villages de Saint-Malo à la Guadeloupe.
- **Primary Substrate**: `#ffffff` (live computed `browser-default` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#fcf150`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `browser-default` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#fcf150` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Montserrat` for display copy (`Route du Rhum, Destination Guadeloup`) with `Varien`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 8px`, padding `12px`) with `cubic-bezier(.83,0,.17,1)` easing and Swiper Touch Carousel Engine, Lottie Vector Animation Player.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-routedurhum-com` in your global stylesheet:

:root {
  /* Route du Rhum 2026 – Destination Guadeloupe · Site Officiel (www-routedurhum-com) — Live-Grounded CSS Variables */
  --one-unit: 1vw; /* Dimension / Scale Token (www-routedurhum-com) */
  --section-max-width: 9999px; /* Layout / Spatial Grid Token (www-routedurhum-com) */
  --spx-stopper-max: 9999px; /* Dimension / Scale Token (www-routedurhum-com) */
  --spx-stopper-min: 0px; /* Dimension / Scale Token (www-routedurhum-com) */
  --browser-zoom: 1; /* Design System Custom Token (www-routedurhum-com) */
  --wst-button-color-fill-primary: rgb(var(--color_48)); /* Brand / Palette Token (www-routedurhum-com) */
  --wst-button-color-border-primary: rgb(var(--color_49)); /* Brand / Palette Token (www-routedurhum-com) */
  --wst-button-color-text-primary: rgb(var(--color_50)); /* Typography Ink Token (www-routedurhum-com) */
  --wst-button-color-fill-primary-hover: rgb(var(--color_51)); /* Brand / Palette Token (www-routedurhum-com) */
  --wst-button-color-border-primary-hover: rgb(var(--color_52)); /* Brand / Palette Token (www-routedurhum-com) */
  --wst-button-color-text-primary-hover: rgb(var(--color_53)); /* Typography Ink Token (www-routedurhum-com) */
  --wst-button-color-fill-primary-disabled: rgb(var(--color_54)); /* Brand / Palette Token (www-routedurhum-com) */
  --wst-button-color-border-primary-disabled: rgb(var(--color_55)); /* Brand / Palette Token (www-routedurhum-com) */
  --wst-button-color-text-primary-disabled: rgb(var(--color_56)); /* Typography Ink Token (www-routedurhum-com) */
  --wst-button-color-fill-secondary: rgb(var(--color_57)); /* Brand / Palette Token (www-routedurhum-com) */
  --wst-button-color-border-secondary: rgb(var(--color_58)); /* Brand / Palette Token (www-routedurhum-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `browser-default` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#f2f6f9` — grounded in `var(--rn-bg)` in `:root`
- **Interactive Accent / Highlight**: `#fcf150` — grounded in `rdr-dernieres-infos .rdi-badge-... { background: #fcf150 }`
- **Secondary / Muted Copy**: `#7b8aa0` — grounded in `var(--ink-3)` in `:root`
- **Structural Hairline Border**: `#e1e6ee` — grounded in `var(--line)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `12px` lateral canvas padding with `8px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 8px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `12px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:1025px)`, `@media (max-width:750px)`, `@media (max-width:760px)`
- **Corner Radii**: `6px`, `50%`, `var(--corvid-border-radius)`, `24px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Montserrat`
- **Body Font Stack**: `Varien`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 20px`, `line-height: normal`, `font-weight: 700`); CSS variables `--display: inline-block`, `--comp-display: unset`, `--container-display: grid`
- **H2 Section Rule**: live computed `h2` (`font-size: 63.36px`, `line-height: 65.2608px`, `font-weight: 700`); CSS variables `--wst-font-style-h2: var(--font_2)`, `--item-depth2-direction: inherit`, `--item-depth2-align: inherit`; rule `h2` (`font-size: clamp(34px,min(4.6vw,7.4vh),7...`, `line-height: 1.1`)
- **Body Copy Rule**: live computed `body` (`font-size: 10px`, `line-height: normal`, `font-weight: 400`); CSS variables `--wst-font-style-body-large: var(--font_7)`, `--wst-font-style-body-medium: var(--font_8)`, `--wst-font-style-body-small: var(--font_9)`; rule `p` (`font-size: 13px`, `line-height: 1.5`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 10px`, `line-height: normal`, `font-weight: 400`); CSS variables `--wst-font-style-body-small: var(--font_9)`, `--wst-font-style-body-x-small: var(--font_10)`; rule `small` (`letter-spacing: 0`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-routedurhum-com` (`Route du Rhum 2026 – Destination Guadeloupe · Site Officiel`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.gt> — `www-routedurhum-com`)**:
   - DOM & Selectors: Landmark `<header class="gt est-pause">` (`1440px`) hosting `Route du Rhum 2026 – Destination Gua` navigation (`Cartographie Carto · Classement`), DOM attributes (`data-rdr-entete="dessus"`, `data-url="https://static.parast..."`, `data-url="https://static.parast..."`, `data-url="https://static.parast..."`), and stylesheet rule `root:active-view-transition { view-transition-name:none }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.gt> — `www-routedurhum-com`)` (`www-routedurhum-com`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (min-width:1025px)`, `@media (max-width:750px)`, `@media (max-width:760px)` with `cubic-bezier(.83,0,.17,1)`, `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.64,0,.78,0)` transitions and links `Cartographie Carto · Classement`.
2. **Hero Stage & Focal Lead (<section.ke5pl1> — `Route du Rhum, Destination Guadelo`)**:
   - DOM & Selectors: Landmark `<section class="ke5pl1 comp-muf996vx">` presenting display lead `Route du Rhum, Destination Guadeloupe` and copy excerpt *"ARRIVÉES EN GUADELOUPE · COMMENT LES SUIVRE EN COURSE SUIVEZ LA F"* over `#ffffff` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#ffffff` background with `#000000` headline `Route du Rhum, Destination Guadeloupe`.
3. **Primary Showcase & Content Grid (<section.em> — `Saint-Malo est en fête !`)**:
   - DOM & Selectors: Landmark `<section class="em">` rendering section `Saint-Malo est en fête !` with copy *"Là où les rêves prennent le large"*, asset references (`7bb303_9e59bb8f77444a2fbb905831b5...`, `minified.js`, `focus-within-polyfill.js`, `cdn.jsdelivr.net`), and grid rule `root::view-transition { pointer-events:none }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.em> — `Saint-Malo est en fête !`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 8px`) on desktop and Single-column vertical stack at `390px` viewport width with `12px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.hero> — `Jean Le Cam, le retour du Roi`)**:
   - DOM & Selectors: Landmark `<section class="hero est-photo">` framing `Jean Le Cam, le retour du Roi` and `Se souvenir des belles choses` (*"Route du Rhum Destination Guadeloupe Départ le dimanche 1 er nove"*) with `#f2f6f9` surface cards, `#fcf150` accents, and `SITE_HEADER { view-transition-name:header-group }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.hero> — `Jean Le Cam, le retour du Roi`)` uses `6px`, `50%`, `var(--corvid-border-radius)`, `24px` radii, `#fcf150` highlights, and assets (7bb303_9e59bb8f77444a2fbb905831b5..., minified.js, focus-within-polyfill.js).
5. **Colophon & Global Directory Footer (<footer.comp-mmxzg4ms> — `https://www.routedurhum.com/`)**:
   - DOM & Selectors: Landmark `<footer class="comp-mmxzg4ms S829f_">` anchoring `Route du Rhum 2026 – Destination` footer links (`Cartographie Carto · Classement`), copy *"Route du Rhum Destination Guadeloupe"*, and `#e1e6ee` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.comp-mmxzg4ms> — `https://www.routedurhum.com/`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `12px` lateral canvas padding with `8px` grid gap and attributes (data-rdr-entete="dessus", data-url="https://static.parast...", data-url="https://static.parast...").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"ARRIVÉES EN GUADELOUPE · COMMENT LES SUIVRE EN COURSE SUIVEZ LA FLOTTE SUR LA CART..."*
- Copy Excerpt 2: *"Là où les rêves prennent le large"*
- Copy Excerpt 3: *"Route du Rhum Destination Guadeloupe Départ le dimanche 1 er novembre 2026 à 13 h..."*
- Copy Excerpt 4: *"Route du Rhum Destination Guadeloupe"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.83,0,.17,1)`, `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.64,0,.78,0)`
- **Extracted Stylesheet Rules (`www-routedurhum-com`)**:
- `root:active-view-transition { view-transition-name:none }`
- `root::view-transition { pointer-events:none }`
- `SITE_HEADER { view-transition-name:header-group }`
- `WIX_ADS { view-transition-name:wix-ads-group }`
- `SITE_FOOTER { view-transition-name:footer-group }`
- **Per-Selector Transition Rules**:
- **Selector `id^=oldHoverBox-]`**: `transition: opacity .5s,visibility .5s` extracted from `www-routedurhum-com` stylesheet.
- **Selector `access-widget-ui::part(acsb-trigger)`**: `transition: width .2s cubic-bezier(.83,0,.17,1) !important` extracted from `www-routedurhum-com` stylesheet.
- **Selector `media (prefers-reduced-motion:red...`**: `transition: none !important` extracted from `www-routedurhum-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.83,0,.17,1)`)**: Governs interactive state transitions across `<header.gt>` and `<section.em>`.
- **Runtime Interaction Engine**: Integrates Swiper Touch Carousel Engine, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `11876px` across 8 distinct viewport chapters.
- **Vertical Chapter Sequence**: JEAN LE CAM, LE RETOUR DU ROI (0%) -> LA COURSE EN DIRECT (8%) -> 🎥 LES NOUVELLES DU BORD EN... (23%) -> VIVEZ VOTRE RHUM (39%) -> TYMAL EST SUR LE VILLAGE (62%) -> #comp-mmxzg4ms_r_comp-mm3m1ky0 (77%) -> Footer (93%) -> Footer (100%).
- **Navigation Drawer / Menu State**: Replicate interactive menu toggle (`Plus de pages Actualités`) with Escape-to-close keyboard handling.
- **Multi-Page Routes**: Scaffold internal routes `/nos-partenaires/r%C3%A9gion-guadeloupe` (detail, direct), `/contact` (about, direct), `/nos-partenaires/ville-de-saint-malo` (detail, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-routedurhum-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | JEAN LE CAM, LE RETOUR DU ROI | `0` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `8%` | LA COURSE EN DIRECT | `0` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `2550px` | `23%` | 🎥 LES NOUVELLES DU BORD EN VIDÉO | `0` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `4250px` | `39%` | VIVEZ VOTRE RHUM | `0` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `6800px` | `62%` | TYMAL EST SUR LE VILLAGE | `0` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `8500px` | `77%` | #comp-mmxzg4ms_r_comp-mm3m1ky0 | `0` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `10200px` | `93%` | Footer | `0` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `10971px` | `100%` | Footer | `0` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | CAP SUR LA GUADELOUPE | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `5643px` | `50%` | VOS QUESTIONS, NOS RÉPONSES | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `11286px` | `100%` | Footer | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Interactive UI State Captures (`1440×900` WebP)
| State Type | Trigger / Observation | Visual Asset |
| :--- | :--- | :--- |
| `nav_menu` | Nav/Menu opened (`Plus de pages Actualités`, diff `91.111`) | [state-nav.webp](assets/state-nav.webp) |
| `interactive_control` | Control `tab` (`1`, diff `26.374`) | [state-interactive.webp](assets/state-interactive.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `detail` | `https://www.routedurhum.com/nos-partenaires/r%C3%A9gion-guadeloupe` | RÉGION GUADELOUPE | `5993px` | `direct` (`1842ms`) | [subpage-01-nos-partenaires-r-c3-a9gion-guadelou.webp](assets/subpage-01-nos-partenaires-r-c3-a9gion-guadelou.webp) |
| `2` | `about` | `https://www.routedurhum.com/contact` | CONTACT | `5090px` | `direct` (`591ms`) | [subpage-02-contact.webp](assets/subpage-02-contact.webp) |
| `3` | `detail` | `https://www.routedurhum.com/nos-partenaires/ville-de-saint-malo` | VILLE DE SAINT-MALO | `5767px` | `direct` (`3185ms`) | [subpage-03-nos-partenaires-ville-de-saint-malo.webp](assets/subpage-03-nos-partenaires-ville-de-saint-malo.webp) |

