---
title: "UI Prompt Blueprint: www-leadoff-fr"
date: 2026-11-24
captured_at: 2026-11-24
target: "www-leadoff-fr"
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
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#0000ff` canvas, `#ffffff` ink, `#ffff00` accent)"
---

# UI Design System & Master Generation Blueprint: www-leadoff-fr

> **Agence digitale à Vannes : web, mobile & acquisition · LEADOFF** (https://www.leadoff.fr) — LEADOFF conçoit des applications web et mobiles, sites e-commerce et stratégies d’acquisition. Une équipe digitale experte basée à Vannes.

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Agence digitale à Vannes : web, mobile & acquisition · LEADOFF** (`https://www.leadoff.fr`). LEADOFF conçoit des applications web et mobiles, sites e-commerce et stratégies d’acquisition. Une équipe digitale experte basée à Vannes.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#0000ff` canvas, `#ffffff` ink, `#ffff00` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#0000ff` (live computed `section` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#ffff00` accents.
  - **Grounded Typographic Hierarchy**: Pairs `NewTitle-Variable` for display copy (`DES APPLICATIONS ET DES SITES QUI PE`) with `GeneralSans-Variable`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 24px`, padding `16px`) with `cubic-bezier(.16,1,.3,1)` easing and Lenis Smooth Scroll (`data-lenis`), Barba.js Page Transition Router.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=6800px` / doc `14435px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1440px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `16px` lateral canvas padding with `24px` grid gap.
- **Border Radius Scale**: `8px`, `50%`, `999px`, `9999px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 24px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `16px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:768px)`, `@media (min-width:992px)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-aspect-ratio:1/1) and (min-width:992px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0000ff` | live computed `section` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | `.loader.loader--black { background: #000000 }` |
| **Interactive Accent / Highlight** | `#ffff00` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#000000` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#000099` | `.bg-yellow .editorial-flow-cont... { border-color: #000099 }` |
| **Variable Token (`--wp-block-synced-color`)** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Variable Token (`--wp-editor-canvas-background`)** | `#dddddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Variable Token (`--wp-admin-theme-color`)** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-10`)** | `#006ba1` | `var(--wp-admin-theme-color-darker-10)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-20`)** | `#005a87` | `var(--wp-admin-theme-color-darker-20)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--focus-color` | `#00f` | Brand / Palette Token |
| `--focus-ring-color` | `var(--focus-color)` | Brand / Palette Token |
| `--wp-block-synced-color` | `#7a00df` | Brand / Palette Token |
| `--wp-block-synced-color--rgb` | `122,0,223` | Brand / Palette Token |
| `--wp-bound-block-color` | `var(--wp-block-synced-color)` | Brand / Palette Token |
| `--wp-editor-canvas-background` | `#ddd` | Canvas / Surface Token |
| `--wp-admin-theme-color` | `#007cba` | Brand / Palette Token |
| `--wp-admin-theme-color--rgb` | `0,124,186` | Brand / Palette Token |
| `--wp-admin-theme-color-darker-10` | `#006ba1` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-10--rgb` | `0,107,160.5` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-20` | `#005a87` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-20--rgb` | `0,90,135` | Canvas / Surface Token |
| `--wp-admin-border-width-focus` | `2px` | Layout / Spatial Grid Token |
| `--wp-admin--admin-bar--position-offset` | `var(--wp-admin--admin-bar--height,0px)` | Dimension / Scale Token |
| `--menu-focus-color` | `#ff0` | Brand / Palette Token |
| `--menu-focus-contrast` | `#000` | Color / Atmospheric Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `NewTitle-Variable`.
- **Primary Body Stack**: `GeneralSans-Variable`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 129.6px`, `line-height: 132.84px`, `font-weight: 650`, `letter-spacing: 1.296px`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 144px`, `line-height: 144px`, `font-weight: 650`, `letter-spacing: 1.44px`); rule `,h2` (`font-size: max(80px,min(10vw,100vw))`, `font-weight: 650`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `,p` (`font-size: max(18px,min(.9vw,100vw))`, `line-height: 1.5`, `letter-spacing: .03em`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.loader`**: `transition: opacity .45s ease,-webkit-transform .45s ease` extracted from `www-leadoff-fr` stylesheet.
- **Selector `.loader .loader-skip`**: `transition: color .2s ease,opacity .2s ease` extracted from `www-leadoff-fr` stylesheet.
- **Selector `.loader .loader-word-letter`**: `transition: opacity .24s ease,-webkit-transform .58s cubic-bezier(.16,1,.3,1)` extracted from `www-leadoff-fr` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.lenis>` and `<section.editorial-pitch>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `14435px`, deepest scrollY reached `6800px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `Lenis`, `GSAP/ScrollTrigger`.
- **Nav / Drawer Probe (`Menu`)**: Triggered visual change (pixel diff `148.681`, captured in `assets/state-nav.webp`); revealed links: PROJETS PROJETS, CONTACT CONTACT, Linkedin Linkedin, Instagram Instagram, Facebook Facebook.
- **Route Transition Architecture**: First internal navigation (`/contact/`) measured as `direct` in `2162ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Agence digitale à Vannes : web, mobile & a │
│ ====================================================================== │
│ [ <header.lenis> (1440x0px)           | Services Services · Projets  ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.observe-section> (w=1440px)                   | │
│ | H1: DES APPLICATIONS ET DES SITES QUI PERFORMENT                   | │
│ | Substrate: #0000ff | Ink: #ffffff | Accent: #ffff00                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.editorial-pitch>) max-w: 1440px            | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Des applications et des site |  | On conçoit des solutions pen | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.editorial-highlig) — Ce qu’on fait (et bie | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.observe-sect) | https://www.leadoff.fr               │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 24px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.lenis>          ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.observe-section) — 390px Vertical Lead        | │
│ | H1: DES APPLICATIONS ET DES SITES QUI PERFORMENT                   | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.editorial-pit) — 1-Col Stack              | │
│ | [ Item 1: Des applications et des sites qui performent           ] | │
│ | [ Item 2: On conçoit des solutions pensées pour durer            ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.editorial-highl) — 1-Col (Ce qu’on fait (et ) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.observe-sect) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.lenis> — `www-leadoff-fr`)**:
   - Landmark `<header class="lenis">` (`1440x0px`) hosting `Agence digitale à Vannes : web, mobi` navigation (`Services Services · Projets Projets · À propos À propos · L’équipe L’équipe · Manifeste Manifeste`), DOM attributes (`data-barba="wrapper"`, `data-skip-link-ready="true"`, `data-icon="false"`, `data-icon="false"`), and stylesheet rule `.loader.loader--hidden { opacity:0;-webkit-transform:scale(.98);transform:scale(.98) }`.
2. **Hero Stage & Focal Lead (<section.observe-section> — `DES APPLICATIONS ET DES SITES QUI `)**:
   - Landmark `<section class="observe-section bg-blue">` presenting display lead `DES APPLICATIONS ET DES SITES QUI PERFORMENT` and copy excerpt *"Rapide. Fluide. Bien pensé. Pas un projet bricolé qui commence à "* over `#0000ff` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.editorial-pitch> — `Des applications et des sites qui `)**:
   - Landmark `<section class="editorial-pitch observe-section">` rendering section `Des applications et des sites qui performent` with copy *"Des applications et"*, asset references (`bundle.68ec1454.css`, `jquery.min.js`, `jquery-migrate.min.js`, `cropped-FAVICON-1-32x32.jpg`), and grid rule `.loader .loader-word { display:-webkit-box;display:-ms-flexbox;display:flex;overflow:hidden }`.
4. **Interactive Detail & Feature Matrix (<section.editorial-highlight> — `On conçoit des solutions pensées p`)**:
   - Landmark `<section class="editorial-highlight observe-section">` framing `On conçoit des solutions pensées pour durer` and `Ce qu’on fait (et bien)` (*"des sites qui performent"*) with `#000000` surface cards, `#ffff00` accents, and `.loader .loader-skip:focus-visible { color:ff0;outline:none }`.
5. **Colophon & Global Directory Footer (<footer.observe-section> — `https://www.leadoff.fr`)**:
   - Landmark `<footer class="observe-section bg-blue">` anchoring `Agence digitale à Vannes : web, ` footer links (`Services Services · Projets Projets · À propos À propos · L’équipe L’équipe · Manifeste Manifeste`), copy *"Un site web, une boutique en ligne, une application… C’est u"*, and `#000099` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `DES APPLICATIONS ET DES SITES QUI PERFORMENT` · sticky/fixed elements: `1`
- **Step 02** (`y=850px`, `6%`): Active landmark `ON CONÇOIT DES SOLUTIONS PENSÉES POUR DURER` · sticky/fixed elements: `2`
- **Step 03** (`y=1700px`, `13%`): Active landmark `CE QU’ON FAIT (ET BIEN)` · sticky/fixed elements: `2`
- **Step 04** (`y=2550px`, `19%`): Active landmark `#editorial` · sticky/fixed elements: `3`
- **Step 05** (`y=4250px`, `31%`): Active landmark `#editorial` · sticky/fixed elements: `2`
- **Step 06** (`y=5100px`, `38%`): Active landmark `#editorial` · sticky/fixed elements: `2`
- **Step 07** (`y=5950px`, `44%`): Active landmark `POURQUOI LEADOFF ET PAS UN AUTRE` · sticky/fixed elements: `2`
- **Step 08** (`y=6800px`, `50%`): Active landmark `NOS RÉALISATIONS` · sticky/fixed elements: `2`

### Multi-Page Internal Route Map
- **About Route (`/contact/`)**: `https://www.leadoff.fr/contact/` — H1: `UN PROJET SÉRIEUX ? ON EN PARLE.`, scrollHeight `5069px`, transition `direct` (`2162ms`)
- **Other Route (`/applications-mobiles/`)**: `https://www.leadoff.fr/applications-mobiles/` — H1: `DES APPLICATIONS MOBILES QUI TIENNENT LA ROUTE`, scrollHeight `11244px`, transition `direct` (`1881ms`)
- **Other Route (`/applications-web/`)**: `https://www.leadoff.fr/applications-web/` — H1: `VOTRE APPLICATION WEB DOIT S’ADAPTER À VOTRE MÉTI...`, scrollHeight `12383px`, transition `direct` (`1570ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-leadoff-fr (Agence digitale à Vannes : web, mobile & acquisition · LEADOFF)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-leadoff-fr` (**Agence digitale à Vannes : web, mobile & acquisition · LEADOFF** — `https://www.leadoff.fr`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0000ff` canvas, `#ffffff` ink, `#ffff00` accent).
- **Identity & Domain Context**: LEADOFF conçoit des applications web et mobiles, sites e-commerce et stratégies d’acquisition. Une équipe digitale experte basée à Vannes.
- **Primary Substrate**: `#0000ff` (live computed `section` `background-color` (`computed_styles.json`)), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#ffff00`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#0000ff` (live computed `section` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#ffff00` accents.
  - **Grounded Typographic Hierarchy**: Pairs `NewTitle-Variable` for display copy (`DES APPLICATIONS ET DES SITES QUI PE`) with `GeneralSans-Variable`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 24px`, padding `16px`) with `cubic-bezier(.16,1,.3,1)` easing and Lenis Smooth Scroll (`data-lenis`), Barba.js Page Transition Router.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-leadoff-fr` in your global stylesheet:

:root {
  /* Agence digitale à Vannes : web, mobile & acquisition · LEADOFF (www-leadoff-fr) — Live-Grounded CSS Variables */
  --focus-color: #00f; /* Brand / Palette Token (www-leadoff-fr) */
  --focus-ring-color: var(--focus-color); /* Brand / Palette Token (www-leadoff-fr) */
  --wp-block-synced-color: #7a00df; /* Brand / Palette Token (www-leadoff-fr) */
  --wp-block-synced-color--rgb: 122,0,223; /* Brand / Palette Token (www-leadoff-fr) */
  --wp-bound-block-color: var(--wp-block-synced-color); /* Brand / Palette Token (www-leadoff-fr) */
  --wp-editor-canvas-background: #ddd; /* Canvas / Surface Token (www-leadoff-fr) */
  --wp-admin-theme-color: #007cba; /* Brand / Palette Token (www-leadoff-fr) */
  --wp-admin-theme-color--rgb: 0,124,186; /* Brand / Palette Token (www-leadoff-fr) */
  --wp-admin-theme-color-darker-10: #006ba1; /* Canvas / Surface Token (www-leadoff-fr) */
  --wp-admin-theme-color-darker-10--rgb: 0,107,160.5; /* Canvas / Surface Token (www-leadoff-fr) */
  --wp-admin-theme-color-darker-20: #005a87; /* Canvas / Surface Token (www-leadoff-fr) */
  --wp-admin-theme-color-darker-20--rgb: 0,90,135; /* Canvas / Surface Token (www-leadoff-fr) */
  --wp-admin-border-width-focus: 2px; /* Layout / Spatial Grid Token (www-leadoff-fr) */
  --wp-admin--admin-bar--position-offset: var(--wp-admin--admin-bar--height,0px); /* Dimension / Scale Token (www-leadoff-fr) */
  --menu-focus-color: #ff0; /* Brand / Palette Token (www-leadoff-fr) */
  --menu-focus-contrast: #000; /* Color / Atmospheric Token (www-leadoff-fr) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#0000ff` — grounded in live computed `section` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#ffffff` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#000000` — grounded in `.loader.loader--black { background: #000000 }`
- **Interactive Accent / Highlight**: `#ffff00` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Secondary / Muted Copy**: `#000000` — grounded in live computed `p` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#000099` — grounded in `.bg-yellow .editorial-flow-cont... { border-color: #000099 }`
- **Variable Token (`--wp-block-synced-color`)**: `#7a00df` — grounded in `var(--wp-block-synced-color)` in `:root`
- **Variable Token (`--wp-editor-canvas-background`)**: `#dddddd` — grounded in `var(--wp-editor-canvas-background)` in `:root`
- **Variable Token (`--wp-admin-theme-color`)**: `#007cba` — grounded in `var(--wp-admin-theme-color)` in `:root`
- **Variable Token (`--wp-admin-theme-color-darker-10`)**: `#006ba1` — grounded in `var(--wp-admin-theme-color-darker-10)` in `:root`
- **Variable Token (`--wp-admin-theme-color-darker-20`)**: `#005a87` — grounded in `var(--wp-admin-theme-color-darker-20)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `16px` lateral canvas padding with `24px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 24px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `16px` horizontal padding
- **Media Queries**: `@media (min-width:768px)`, `@media (min-width:992px)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-aspect-ratio:1/1) and (min-width:992px)`
- **Corner Radii**: `8px`, `50%`, `999px`, `9999px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `NewTitle-Variable`
- **Body Font Stack**: `GeneralSans-Variable`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 129.6px`, `line-height: 132.84px`, `font-weight: 650`, `letter-spacing: 1.296px`)
- **H2 Section Rule**: live computed `h2` (`font-size: 144px`, `line-height: 144px`, `font-weight: 650`, `letter-spacing: 1.44px`); rule `,h2` (`font-size: max(80px,min(10vw,100vw))`, `font-weight: 650`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `,p` (`font-size: max(18px,min(.9vw,100vw))`, `line-height: 1.5`, `letter-spacing: .03em`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-leadoff-fr` (`Agence digitale à Vannes : web, mobile & acquisition · LEADOFF`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.lenis> — `www-leadoff-fr`)**:
   - DOM & Selectors: Landmark `<header class="lenis">` (`1440x0px`) hosting `Agence digitale à Vannes : web, mobi` navigation (`Services Services · Projets Projets · À propos À propos · L’équipe L’équipe · Manifeste Manifeste`), DOM attributes (`data-barba="wrapper"`, `data-skip-link-ready="true"`, `data-icon="false"`, `data-icon="false"`), and stylesheet rule `.loader.loader--hidden { opacity:0;-webkit-transform:scale(.98);transform:scale(.98) }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.lenis> — `www-leadoff-fr`)` (`www-leadoff-fr`) adapts across `@media (min-width:768px)`, `@media (min-width:992px)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-aspect-ratio:1/1) and (min-width:992px)` with `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Services Services · Projets Projets · À propos À propos · L’équipe L’équipe · Manifeste Manifeste`.
2. **Hero Stage & Focal Lead (<section.observe-section> — `DES APPLICATIONS ET DES SITES QUI `)**:
   - DOM & Selectors: Landmark `<section class="observe-section bg-blue">` presenting display lead `DES APPLICATIONS ET DES SITES QUI PERFORMENT` and copy excerpt *"Rapide. Fluide. Bien pensé. Pas un projet bricolé qui commence à "* over `#0000ff` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#0000ff` background with `#ffffff` headline `DES APPLICATIONS ET DES SITES QUI PERFORMENT`.
3. **Primary Showcase & Content Grid (<section.editorial-pitch> — `Des applications et des sites qui `)**:
   - DOM & Selectors: Landmark `<section class="editorial-pitch observe-section">` rendering section `Des applications et des sites qui performent` with copy *"Des applications et"*, asset references (`bundle.68ec1454.css`, `jquery.min.js`, `jquery-migrate.min.js`, `cropped-FAVICON-1-32x32.jpg`), and grid rule `.loader .loader-word { display:-webkit-box;display:-ms-flexbox;display:flex;overflow:hidden }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.editorial-pitch> — `Des applications et des sites qui `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 24px`) on desktop and Single-column vertical stack at `390px` viewport width with `16px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.editorial-highlight> — `On conçoit des solutions pensées p`)**:
   - DOM & Selectors: Landmark `<section class="editorial-highlight observe-section">` framing `On conçoit des solutions pensées pour durer` and `Ce qu’on fait (et bien)` (*"des sites qui performent"*) with `#000000` surface cards, `#ffff00` accents, and `.loader .loader-skip:focus-visible { color:ff0;outline:none }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.editorial-highlight> — `On conçoit des solutions pensées p`)` uses `8px`, `50%`, `999px`, `9999px` radii, `#ffff00` highlights, and assets (bundle.68ec1454.css, jquery.min.js, jquery-migrate.min.js).
5. **Colophon & Global Directory Footer (<footer.observe-section> — `https://www.leadoff.fr`)**:
   - DOM & Selectors: Landmark `<footer class="observe-section bg-blue">` anchoring `Agence digitale à Vannes : web, ` footer links (`Services Services · Projets Projets · À propos À propos · L’équipe L’équipe · Manifeste Manifeste`), copy *"Un site web, une boutique en ligne, une application… C’est u"*, and `#000099` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.observe-section> — `https://www.leadoff.fr`)` aligns to `1440px` (non-`@media` desktop container stylesheet rule) with `16px` lateral canvas padding with `24px` grid gap and attributes (data-barba="wrapper", data-skip-link-ready="true", data-icon="false").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Rapide. Fluide. Bien pensé. Pas un projet bricolé qui commence à montrer ses limit..."*
- Copy Excerpt 2: *"Des applications et"*
- Copy Excerpt 3: *"des sites qui performent"*
- Copy Excerpt 4: *"Un site web, une boutique en ligne, une application… C’est un investissement. Pas..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`www-leadoff-fr`)**:
- `.loader.loader--hidden { opacity:0;-webkit-transform:scale(.98);transform:scale(.98) }`
- `.loader .loader-word { display:-webkit-box;display:-ms-flexbox;display:flex;overflow:hidden }`
- `.loader .loader-skip:focus-visible { color:ff0;outline:none }`
- `.loader .loader-word-space { width:.22em }`
- `.loader .loader-logo svg { display:block;height:auto;width:100% }`
- **Per-Selector Transition Rules**:
- **Selector `.loader`**: `transition: opacity .45s ease,-webkit-transform .45s ease` extracted from `www-leadoff-fr` stylesheet.
- **Selector `.loader .loader-skip`**: `transition: color .2s ease,opacity .2s ease` extracted from `www-leadoff-fr` stylesheet.
- **Selector `.loader .loader-word-letter`**: `transition: opacity .24s ease,-webkit-transform .58s cubic-bezier(.16,1,.3,1)` extracted from `www-leadoff-fr` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.lenis>` and `<section.editorial-pitch>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `14435px` across 8 distinct viewport chapters using Lenis, GSAP/ScrollTrigger.
- **Vertical Chapter Sequence**: DES APPLICATIONS ET DES SIT... (0%) -> ON CONÇOIT DES SOLUTIONS PE... (6%) -> CE QU’ON FAIT (ET BIEN) (13%) -> #editorial (19%) -> #editorial (31%) -> #editorial (38%) -> POURQUOI LEADOFF ET PAS UN... (44%) -> NOS RÉALISATIONS (50%).
- **Navigation Drawer / Menu State**: Replicate interactive menu toggle (`Menu`) with Escape-to-close keyboard handling.
- **Multi-Page Routes**: Scaffold internal routes `/contact/` (about, direct), `/applications-mobiles/` (other, direct), `/applications-web/` (other, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-leadoff-fr`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | DES APPLICATIONS ET DES SITES QUI PERFORMENT | `1` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `6%` | ON CONÇOIT DES SOLUTIONS PENSÉES POUR DURER | `2` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `1700px` | `13%` | CE QU’ON FAIT (ET BIEN) | `2` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `2550px` | `19%` | #editorial | `3` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `4250px` | `31%` | #editorial | `2` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `5100px` | `38%` | #editorial | `2` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `5950px` | `44%` | POURQUOI LEADOFF ET PAS UN AUTRE | `2` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `6800px` | `50%` | NOS RÉALISATIONS | `2` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | #editorial | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `7200px` | `50%` | UN CAMPUS MONDIAL À PORTÉE DE MAIN POUR 6... | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `14400px` | `100%` | UN NOUVEAU SITE N’EFFACE PAS SON PASSÉ. | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Interactive UI State Captures (`1440×900` WebP)
| State Type | Trigger / Observation | Visual Asset |
| :--- | :--- | :--- |
| `nav_menu` | Nav/Menu opened (`Menu`, diff `148.681`) | [state-nav.webp](assets/state-nav.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `about` | `https://www.leadoff.fr/contact/` | UN PROJET SÉRIEUX ? ON EN PARLE. | `5069px` | `direct` (`2162ms`) | [subpage-01-contact.webp](assets/subpage-01-contact.webp) |
| `2` | `other` | `https://www.leadoff.fr/applications-mobiles/` | DES APPLICATIONS MOBILES QUI TIENNENT... | `11244px` | `direct` (`1881ms`) | [subpage-02-applications-mobiles.webp](assets/subpage-02-applications-mobiles.webp) |
| `3` | `other` | `https://www.leadoff.fr/applications-web/` | VOTRE APPLICATION WEB DOIT S’ADAPTER... | `12383px` | `direct` (`1570ms`) | [subpage-03-applications-web.webp](assets/subpage-03-applications-web.webp) |

