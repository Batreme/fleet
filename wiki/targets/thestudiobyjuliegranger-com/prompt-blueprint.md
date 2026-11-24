---
title: "UI Prompt Blueprint: thestudiobyjuliegranger-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "thestudiobyjuliegranger-com"
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
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#474040` ink, `#91befc` accent)"
---

# UI Design System & Master Generation Blueprint: thestudiobyjuliegranger-com

> **The Studio by Julie Granger** (https://thestudiobyjuliegranger.com/) — Une méthode unique alliant barre, yoga et renforcement, développée depuis plus de 12 ans et déjà adoptée par des milliers de femmes à tra...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **The Studio by Julie Granger** (`https://thestudiobyjuliegranger.com/`). Une méthode unique alliant barre, yoga et renforcement, développée depuis plus de 12 ans et déjà adoptée par des milliers de femmes à tra...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#474040` ink, `#91befc` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#474040` primary typography and `#91befc` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Newsreader Hero` for display copy (`Un corps sculpté avec élégance`) with `Open Sans` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 10px`, padding `10px`) with `cubic-bezier(.645,.045,.355,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=13358px` / doc `14258px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1440px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `10px` lateral canvas padding with `10px` grid gap.
- **Border Radius Scale**: `50%`, `20px`, `10px`, `14px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 10px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `10px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:768px)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-width:1024px)`, `@media (min-width:480px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#474040` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f6f6f0` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#91befc` | `.hero__retreat-badge { background-color: #91befc }` |
| **Secondary / Muted Copy** | `#665c5a` | `var(--consent-soft-ink)` in `:root` |
| **Structural Hairline Border** | `#e2e2e2` | `var(--wc-address-book--border--color)` in `:root` |
| **Variable Token (`--wp-block-synced-color`)** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Variable Token (`--wp-editor-canvas-background`)** | `#dddddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Variable Token (`--wp-admin-theme-color`)** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-10`)** | `#006ba1` | `var(--wp-admin-theme-color-darker-10)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-20`)** | `#005a87` | `var(--wp-admin-theme-color-darker-20)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
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
| `--site-fixed-header-offset` | `70px` | Layout / Spatial Grid Token |
| `--site-no-hero-top-gap` | `18px` | Layout / Spatial Grid Token |
| `--site-anchor-scroll-gap` | `16px` | Layout / Spatial Grid Token |
| `--gap` | `12px` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Newsreader Hero`.
- **Primary Body Stack**: `Open Sans`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 64px`, `line-height: 64px`, `font-weight: 400`); rule `h1` (`font-size: 26px`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 42px`, `line-height: 46.2px`, `font-weight: 400`); rule `h2` (`font-size: 26px`, `line-height: 1.1`, `font-weight: 400`).
- **Body Copy**: live computed `body` (`font-size: 14px`, `line-height: 19.6px`, `font-weight: 400`); rule `p` (`font-size: 14px`, `line-height: 1.4`, `font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 19.6px`, `font-weight: 400`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.645,.045,.355,1)`, `cubic-bezier(0.625,0.05,0,1)`, `cubic-bezier(.625,.05,0,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.for-you__slide-overlay`**: `transition: opacity .4s ease` extracted from `thestudiobyjuliegranger-com` stylesheet.
- **Selector `.for-you__slide-title`**: `transition: opacity .3s cubic-bezier(.645,.045,.355,1),transform .3s cubic...` extracted from `thestudiobyjuliegranger-com` stylesheet.
- **Selector `.for-you__slide-title-link`**: `transition: color .2s ease` extracted from `thestudiobyjuliegranger-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.645,.045,.355,1)`)**: Governs interactive state transitions across `<header.mega-nav-header>` and `<section.logos>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `14258px`, deepest scrollY reached `13358px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `GSAP/ScrollTrigger`.
- **Nav / Drawer Probe (`La méthode`)**: Triggered visual change (pixel diff `72.224`, captured in `assets/state-nav.webp`); revealed links: MÉTHODE ET RÉSULTATS, THE STUDIO PAR JULIE..., PRESSE ET TÉMOIGNAGES, La méthode En savoir..., A propos En savoir plus.
- **Hover Physics (`primary_cta` · `Commencer l’essai`)**: `backgroundColor`: `rgb(255, 253, 226)` -> `rgba(255, 253, 226, 0.8)`; `borderColor`: `rgb(255, 253, 226)` -> `rgba(255, 253, 226, 0.8)` (`transition-duration: 0.2s, 0.2s, 0.2s, 0.2s`, `timing: ease, ease, ease, ease`).
- **Route Transition Architecture**: First internal navigation (`/mon-compte/`) measured as `direct` in `2387ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — The Studio by Julie Granger                │
│ ====================================================================== │
│ [ <header.mega-nav-heade (1340x92px)  | Connexion · en · Connexion C ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero> (w=1440px)                              | │
│ | H1: Un corps sculpté avec élégance                                 | │
│ | Substrate: #ffffff | Ink: #474040 | Accent: #91befc                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.logos>) max-w: 1440px                      | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Une méthode complète pour sc |  | The Studio by Julie Granger  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.benefits>) — Si vous vous reconnai         | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>) | https://thestudiobyjuliegranger.com  │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 10px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.mega-nav-header>) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.hero>) — 390px Vertical Lead                  | │
│ | H1: Un corps sculpté avec élégance                                 | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.logos>) — 1-Col Stack                     | │
│ | [ Item 1: Une méthode complète pour sculpter le corps            ] | │
│ | [ Item 2: The Studio by Julie Granger                            ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.benefits>) — 1-Col (Si vous vous recon)     | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.mega-nav-header> — `thestudiobyjuliegranger-com`)**:
   - Landmark `<header class="mega-nav-header">` (`1340x92px`) hosting `The Studio by Julie Granger` navigation (`Connexion · en · Connexion Connexion · Méthode et Résultats · Corps qui a changé`), DOM attributes (`data-cookieconsent="ignore"`, `data-implementation="wp"`, `data-cbid="22577dd5-f8e6-45b3-bb..."`, `data-culture="FR"`), and stylesheet rule `.banp-request-push-permission-button { margin-right:10px }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Un corps sculpté avec élégance`)**:
   - Landmark `<section class="hero hero--home">` presenting display lead `Un corps sculpté avec élégance` and copy excerpt *"La méthode unique de The Studio mêle barre, yoga et renforcement "* over `#ffffff` canvas and `#474040` ink.
3. **Primary Showcase & Content Grid (<section.logos> — `Une méthode complète pour sculpter`)**:
   - Landmark `<section class="logos">` rendering section `Une méthode complète pour sculpter le corps` with copy *"C o m m e n c e r l ’ e s s a i"*, asset references (`matomo.js`, `gtm.js`, `state.js`, `widgetIcon.min.js`), and grid rule `.banp-ajax-success { display:inline-block;font-size:1.2em;margin:0 10px;vertical-align:middle }`.
4. **Interactive Detail & Feature Matrix (<section.benefits> — `The Studio by Julie Granger`)**:
   - Landmark `<section class="benefits">` framing `The Studio by Julie Granger` and `Si vous vous reconnaissez, The Studio est fait po...` (*"Pour tous les niveaux"*) with `#f6f6f0` surface cards, `#91befc` accents, and `.banp-ajax-error { color:b81c23 }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://thestudiobyjuliegranger.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `The Studio by Julie Granger` footer links (`Connexion · en · Connexion Connexion · Méthode et Résultats · Corps qui a changé`), copy *"Des workouts adaptés à tous les niveaux"*, and `#e2e2e2` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `Un corps sculpté avec élégance` · sticky/fixed elements: `1`
- **Step 02** (`y=850px`, `6%`): Active landmark `Une méthode complète pour sculpter le corps` · sticky/fixed elements: `0`
- **Step 03** (`y=3400px`, `25%`): Active landmark `Exigeante avec votre corps` · sticky/fixed elements: `0`
- **Step 04** (`y=5950px`, `45%`): Active landmark `Section @ 45%` · sticky/fixed elements: `0`
- **Step 05** (`y=7650px`, `57%`): Active landmark `The Studio est bien plus qu’une plateforme de fit...` · sticky/fixed elements: `0`
- **Step 06** (`y=10200px`, `76%`): Active landmark `The Studio par Julie Granger` · sticky/fixed elements: `0`
- **Step 07** (`y=12750px`, `95%`): Active landmark `Footer` · sticky/fixed elements: `0`
- **Step 08** (`y=13358px`, `100%`): Active landmark `Footer` · sticky/fixed elements: `0`

### Multi-Page Internal Route Map
- **Other Route (`/mon-compte/`)**: `https://thestudiobyjuliegranger.com/mon-compte/?auth=login` — H1: `Mon compte`, scrollHeight `2358px`, transition `direct` (`2387ms`)
- **Other Route (`/en/`)**: `https://thestudiobyjuliegranger.com/en/` — H1: `A sculpted body with elegance`, scrollHeight `14193px`, transition `direct` (`1691ms`)
- **Other Route (`/abonnements-programmes/`)**: `https://thestudiobyjuliegranger.com/abonnements-programmes/` — H1: `Optez pour la méthode de pratique qui vous convient`, scrollHeight `10204px`, transition `direct` (`1442ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: thestudiobyjuliegranger-com (The Studio by Julie Granger)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `thestudiobyjuliegranger-com` (**The Studio by Julie Granger** — `https://thestudiobyjuliegranger.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#474040` ink, `#91befc` accent).
- **Identity & Domain Context**: Une méthode unique alliant barre, yoga et renforcement, développée depuis plus de 12 ans et déjà adoptée par des milliers de femmes à tra...
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#474040`, **Accent / Highlight**: `#91befc`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#474040` primary typography and `#91befc` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Newsreader Hero` for display copy (`Un corps sculpté avec élégance`) with `Open Sans` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 10px`, padding `10px`) with `cubic-bezier(.645,.045,.355,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `thestudiobyjuliegranger-com` in your global stylesheet:

:root {
  /* The Studio by Julie Granger (thestudiobyjuliegranger-com) — Live-Grounded CSS Variables */
  --wp-block-synced-color: #7a00df; /* Brand / Palette Token (thestudiobyjuliegranger-com) */
  --wp-block-synced-color--rgb: 122,0,223; /* Brand / Palette Token (thestudiobyjuliegranger-com) */
  --wp-bound-block-color: var(--wp-block-synced-color); /* Brand / Palette Token (thestudiobyjuliegranger-com) */
  --wp-editor-canvas-background: #ddd; /* Canvas / Surface Token (thestudiobyjuliegranger-com) */
  --wp-admin-theme-color: #007cba; /* Brand / Palette Token (thestudiobyjuliegranger-com) */
  --wp-admin-theme-color--rgb: 0,124,186; /* Brand / Palette Token (thestudiobyjuliegranger-com) */
  --wp-admin-theme-color-darker-10: #006ba1; /* Canvas / Surface Token (thestudiobyjuliegranger-com) */
  --wp-admin-theme-color-darker-10--rgb: 0,107,160.5; /* Canvas / Surface Token (thestudiobyjuliegranger-com) */
  --wp-admin-theme-color-darker-20: #005a87; /* Canvas / Surface Token (thestudiobyjuliegranger-com) */
  --wp-admin-theme-color-darker-20--rgb: 0,90,135; /* Canvas / Surface Token (thestudiobyjuliegranger-com) */
  --wp-admin-border-width-focus: 2px; /* Layout / Spatial Grid Token (thestudiobyjuliegranger-com) */
  --wp-admin--admin-bar--position-offset: var(--wp-admin--admin-bar--height,0px); /* Dimension / Scale Token (thestudiobyjuliegranger-com) */
  --site-fixed-header-offset: 70px; /* Layout / Spatial Grid Token (thestudiobyjuliegranger-com) */
  --site-no-hero-top-gap: 18px; /* Layout / Spatial Grid Token (thestudiobyjuliegranger-com) */
  --site-anchor-scroll-gap: 16px; /* Layout / Spatial Grid Token (thestudiobyjuliegranger-com) */
  --gap: 12px; /* Layout / Spatial Grid Token (thestudiobyjuliegranger-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#474040` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#f6f6f0` — grounded in live computed `footer` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#91befc` — grounded in `.hero__retreat-badge { background-color: #91befc }`
- **Secondary / Muted Copy**: `#665c5a` — grounded in `var(--consent-soft-ink)` in `:root`
- **Structural Hairline Border**: `#e2e2e2` — grounded in `var(--wc-address-book--border--color)` in `:root`
- **Variable Token (`--wp-block-synced-color`)**: `#7a00df` — grounded in `var(--wp-block-synced-color)` in `:root`
- **Variable Token (`--wp-editor-canvas-background`)**: `#dddddd` — grounded in `var(--wp-editor-canvas-background)` in `:root`
- **Variable Token (`--wp-admin-theme-color`)**: `#007cba` — grounded in `var(--wp-admin-theme-color)` in `:root`
- **Variable Token (`--wp-admin-theme-color-darker-10`)**: `#006ba1` — grounded in `var(--wp-admin-theme-color-darker-10)` in `:root`
- **Variable Token (`--wp-admin-theme-color-darker-20`)**: `#005a87` — grounded in `var(--wp-admin-theme-color-darker-20)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `10px` lateral canvas padding with `10px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 10px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `10px` horizontal padding
- **Media Queries**: `@media (min-width:768px)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-width:1024px)`, `@media (min-width:480px)`
- **Corner Radii**: `50%`, `20px`, `10px`, `14px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Newsreader Hero`
- **Body Font Stack**: `Open Sans`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: live computed `h1` (`font-size: 64px`, `line-height: 64px`, `font-weight: 400`); rule `h1` (`font-size: 26px`)
- **H2 Section Rule**: live computed `h2` (`font-size: 42px`, `line-height: 46.2px`, `font-weight: 400`); rule `h2` (`font-size: 26px`, `line-height: 1.1`, `font-weight: 400`)
- **Body Copy Rule**: live computed `body` (`font-size: 14px`, `line-height: 19.6px`, `font-weight: 400`); rule `p` (`font-size: 14px`, `line-height: 1.4`, `font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 14px`, `line-height: 19.6px`, `font-weight: 400`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `thestudiobyjuliegranger-com` (`The Studio by Julie Granger`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.mega-nav-header> — `thestudiobyjuliegranger-com`)**:
   - DOM & Selectors: Landmark `<header class="mega-nav-header">` (`1340x92px`) hosting `The Studio by Julie Granger` navigation (`Connexion · en · Connexion Connexion · Méthode et Résultats · Corps qui a changé`), DOM attributes (`data-cookieconsent="ignore"`, `data-implementation="wp"`, `data-cbid="22577dd5-f8e6-45b3-bb..."`, `data-culture="FR"`), and stylesheet rule `.banp-request-push-permission-button { margin-right:10px }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.mega-nav-header> — `thestudiobyjuliegranger-com`)` (`thestudiobyjuliegranger-com`) adapts across `@media (min-width:768px)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-width:1024px)`, `@media (min-width:480px)` with `cubic-bezier(.645,.045,.355,1)`, `cubic-bezier(0.625,0.05,0,1)`, `cubic-bezier(.625,.05,0,1)` transitions and links `Connexion · en · Connexion Connexion · Méthode et Résultats · Corps qui a changé`.
2. **Hero Stage & Focal Lead (<section.hero> — `Un corps sculpté avec élégance`)**:
   - DOM & Selectors: Landmark `<section class="hero hero--home">` presenting display lead `Un corps sculpté avec élégance` and copy excerpt *"La méthode unique de The Studio mêle barre, yoga et renforcement "* over `#ffffff` canvas and `#474040` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#ffffff` background with `#474040` headline `Un corps sculpté avec élégance`.
3. **Primary Showcase & Content Grid (<section.logos> — `Une méthode complète pour sculpter`)**:
   - DOM & Selectors: Landmark `<section class="logos">` rendering section `Une méthode complète pour sculpter le corps` with copy *"C o m m e n c e r l ’ e s s a i"*, asset references (`matomo.js`, `gtm.js`, `state.js`, `widgetIcon.min.js`), and grid rule `.banp-ajax-success { display:inline-block;font-size:1.2em;margin:0 10px;vertical-align:middle }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.logos> — `Une méthode complète pour sculpter`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 10px`) on desktop and Single-column vertical stack at `390px` viewport width with `10px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.benefits> — `The Studio by Julie Granger`)**:
   - DOM & Selectors: Landmark `<section class="benefits">` framing `The Studio by Julie Granger` and `Si vous vous reconnaissez, The Studio est fait po...` (*"Pour tous les niveaux"*) with `#f6f6f0` surface cards, `#91befc` accents, and `.banp-ajax-error { color:b81c23 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.benefits> — `The Studio by Julie Granger`)` uses `50%`, `20px`, `10px`, `14px` radii, `#91befc` highlights, and assets (matomo.js, gtm.js, state.js).
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://thestudiobyjuliegranger.com/`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer">` anchoring `The Studio by Julie Granger` footer links (`Connexion · en · Connexion Connexion · Méthode et Résultats · Corps qui a changé`), copy *"Des workouts adaptés à tous les niveaux"*, and `#e2e2e2` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-footer> — `https://thestudiobyjuliegranger.com/`)` aligns to `1440px` (non-`@media` desktop container stylesheet rule) with `10px` lateral canvas padding with `10px` grid gap and attributes (data-cookieconsent="ignore", data-implementation="wp", data-cbid="22577dd5-f8e6-45b3-bb...").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"La méthode unique de The Studio mêle barre, yoga et renforcement pour transformer..."*
- Copy Excerpt 2: *"C o m m e n c e r l ’ e s s a i"*
- Copy Excerpt 3: *"Pour tous les niveaux"*
- Copy Excerpt 4: *"Des workouts adaptés à tous les niveaux"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.645,.045,.355,1)`, `cubic-bezier(0.625,0.05,0,1)`, `cubic-bezier(.625,.05,0,1)`
- **Extracted Stylesheet Rules (`thestudiobyjuliegranger-com`)**:
- `.banp-request-push-permission-button { margin-right:10px }`
- `.banp-ajax-success { display:inline-block;font-size:1.2em;margin:0 10px;vertical-align:middle }`
- `.banp-ajax-error { color:b81c23 }`
- `.banp-ajax-success:before { content:"\0049";font-family:booking_activities_icons }`
- `.banp-ajax-error:before { content:"\004a";font-family:booking_activities_icons }`
- **Per-Selector Transition Rules**:
- **Selector `.for-you__slide-overlay`**: `transition: opacity .4s ease` extracted from `thestudiobyjuliegranger-com` stylesheet.
- **Selector `.for-you__slide-title`**: `transition: opacity .3s cubic-bezier(.645,.045,.355,1),transform .3s cubic...` extracted from `thestudiobyjuliegranger-com` stylesheet.
- **Selector `.for-you__slide-title-link`**: `transition: color .2s ease` extracted from `thestudiobyjuliegranger-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.645,.045,.355,1)`)**: Governs interactive state transitions across `<header.mega-nav-header>` and `<section.logos>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `14258px` across 8 distinct viewport chapters using GSAP/ScrollTrigger.
- **Vertical Chapter Sequence**: Un corps sculpté avec élégance (0%) -> Une méthode complète pour s... (6%) -> Exigeante avec votre corps (25%) -> Section @ 45% (45%) -> The Studio est bien plus qu... (57%) -> The Studio par Julie Granger (76%) -> Footer (95%) -> Footer (100%).
- **Navigation Drawer / Menu State**: Replicate interactive menu toggle (`La méthode`) with Escape-to-close keyboard handling.
- **Hover Micro-Interaction (`primary_cta`)**: Animate `backgroundColor, borderColor` with `0.2s, 0.2s, 0.2s, 0.2s ease, ease, ease, ease`.
- **Multi-Page Routes**: Scaffold internal routes `/mon-compte/` (other, direct), `/en/` (other, direct), `/abonnements-programmes/` (other, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `thestudiobyjuliegranger-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | Un corps sculpté avec élégance | `1` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `6%` | Une méthode complète pour sculpter le corps | `0` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `3400px` | `25%` | Exigeante avec votre corps | `0` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `5950px` | `45%` | Section @ 45% | `0` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `7650px` | `57%` | The Studio est bien plus qu’une plateforme de... | `0` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `10200px` | `76%` | The Studio par Julie Granger | `0` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `12750px` | `95%` | Footer | `0` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `13358px` | `100%` | Footer | `0` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | Un corps sculpté avec élégance | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `6492px` | `50%` | Section @ 50% | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `12985px` | `100%` | Footer | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Interactive UI State Captures (`1440×900` WebP)
| State Type | Trigger / Observation | Visual Asset |
| :--- | :--- | :--- |
| `nav_menu` | Nav/Menu opened (`La méthode`, diff `72.224`) | [state-nav.webp](assets/state-nav.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `other` | `https://thestudiobyjuliegranger.com/mon-compte/?auth=login` | Mon compte | `2358px` | `direct` (`2387ms`) | [subpage-01-mon-compte.webp](assets/subpage-01-mon-compte.webp) |
| `2` | `other` | `https://thestudiobyjuliegranger.com/en/` | A sculpted body with elegance | `14193px` | `direct` (`1691ms`) | [subpage-02-en.webp](assets/subpage-02-en.webp) |
| `3` | `other` | `https://thestudiobyjuliegranger.com/abonnements-programmes/` | Optez pour la méthode de pratique qui... | `10204px` | `direct` (`1442ms`) | [subpage-03-abonnements-programmes.webp](assets/subpage-03-abonnements-programmes.webp) |

