---
title: "UI Prompt Blueprint: www-politico-eu_sponsored-content-saving-costs-and-improving-lives"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-politico-eu_sponsored-content-saving-costs-and-improving-lives"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#0d0f16` ink, `#ff0000` accent)"
---

# UI Design System & Master Generation Blueprint: www-politico-eu_sponsored-content-saving-costs-and-improving-lives

> **Saving costs and improving lives – POLITICO** (https://www.politico.eu/sponsored-content/saving-costs-and-improving-lives/) — Visit the post for more.

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Saving costs and improving lives – POLITICO** (`https://www.politico.eu/sponsored-content/saving-costs-and-improving-lives/`). Visit the post for more.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#0d0f16` ink, `#ff0000` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#0d0f16` primary typography and `#ff0000` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Sohne` for display copy (`Our readers read next`) with `Martina Plantijn` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: normal 16px`, padding `40px`) with `cubic-bezier(.215,.61,.355,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1440px` (live computed `main` `max-width`).
- **Canvas Lateral Padding & Spacing**: `40px` lateral canvas padding with `normal 16px` grid gap.
- **Border Radius Scale**: `36px`, `var(--wp--custom--radius--round-8)`, `50%`, `var(--wp--custom--radius--round-4)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: 2-column persistent left sidebar (`200px`, <nav.navigation-mini>) + `1440px` main content stage at `1440px` (`max-width: 1440px`, `gap: normal 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with collapsed `<nav.navigation-mini>` drawer navigation and `40px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:48em)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-width:80em)`, `@media (max-width:47.9375em)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0d0f16` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#dddddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Interactive Accent / Highlight** | `#ff0000` | `ant--primary .tags__tags .tags_... { background-color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#1ea0c3` | `.wp-social-link-bandcamp { color: #1ea0c3 }` |
| **Structural Hairline Border** | `#dadada` | `.sponsored-content-banner__bott... { border-top: #dadada }` |
| **Variable Token (`--wp-block-synced-color`)** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color`)** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-10`)** | `#006ba1` | `var(--wp-admin-theme-color-darker-10)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-20`)** | `#005a87` | `var(--wp-admin-theme-color-darker-20)` in `:root` |
| **Variable Token (`--wp--custom--color--blue--100`)** | `#cce5f4` | `var(--wp--custom--color--blue--100)` in `:root` |
| **Variable Token (`--wp--custom--color--blue--300`)** | `#66b0dd` | `var(--wp--custom--color--blue--300)` in `:root` |
| **Variable Token (`--wp--custom--color--blue--500`)** | `#007bc7` | `var(--wp--custom--color--blue--500)` in `:root` |
| **Variable Token (`--wp--custom--color--blue--600`)** | `#00629f` | `var(--wp--custom--color--blue--600)` in `:root` |

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
| `--wp--custom--color--blue--100` | `#CCE5F4` | Brand / Palette Token |
| `--wp--custom--color--blue--300` | `#66B0DD` | Brand / Palette Token |
| `--wp--custom--color--blue--500` | `#007BC7` | Brand / Palette Token |
| `--wp--custom--color--blue--600` | `#00629F` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Sohne`.
- **Primary Body Stack**: `Martina Plantijn`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: rule `h1` (`font-weight: var(--font-we...`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 20px`, `line-height: 30px`, `font-weight: 500`); rule `h2` (`font-weight: var(--font-we...`).
- **Body Copy**: live computed `body` (`font-size: 20px`, `line-height: 30px`, `font-weight: 400`); rule `p` (`font-size: var(--wp--custom--type-scale-...`, `line-height: var(--wp--custom--typ...`, `font-weight: var(--font-we...`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 20px`, `line-height: 30px`, `font-weight: 400`); CSS variables `--wp--custom--animation--duration--small: 100ms`, `--wp--custom--animation--duration--extra-small: 50ms`, `--wp--custom--stroke--small: 1px`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.215,.61,.355,1)`, `cubic-bezier(0.215,0.61,0.355,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `media (prefers-reduced-motion:red...`**: `transition: 1ms!important` extracted from `www-politico-eu_sponsored-content-saving-costs-and-improving-lives` stylesheet.
- **Selector `a:where(:not(.wp-element-button))`**: `transition: color var(--transition-style-link-out),background-color var(--...` extracted from `www-politico-eu_sponsored-content-saving-costs-and-improving-lives` stylesheet.
- **Selector `a:where(:not(.wp-element-button))...`**: `transition: color var(--transition-style-link-in),background-color var(--t...` extracted from `www-politico-eu_sponsored-content-saving-costs-and-improving-lives` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.215,.61,.355,1)`)**: Governs interactive state transitions across `<header.header>` and `<article.article--no-top-margin>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Sidebar (200px) + Main (1440px)            │
│ ====================================================================== │
│ +--[ SIDEBAR (200px) ]--+--[ MAIN CONTENT STAGE (1440px) ]-----------+ │
│ | <nav.navigation-mini> | [ <header.header> | Europe · UK · Fran ]   | │
│ | - Europe              | ------------------------------------------ | │
│ | - UK                  | HERO STAGE: <article.article>              | │
│ | - France              | H1: Our readers read next                  | │
│ | - Germany             | Bg:#ffffff Ink:#0d0f16 Acc:#ff0000         | │
│ | x=40 h=700px rail     | ------------------------------------------ | │
│ |                       | SHOWCASE: <article.article--no max:1440px  | │
│ |                       | [Lucy Powell promot] [Global climate tal]  | │
│ |                       | DETAIL: <article.article:nth(2)>           | │
│ +-----------------------+--------------------------------------------+ │
│ [ FOOTER (<footer.article__foo) | https://www.politico.eu/sponsored-c  │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Collapsed Sidebar + 1-Col Stack       │
│ ====================================================================== │
│ [ DRAWER (<nav.navigation-mini> ) | <header.header>                    │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<article.article>) — 390px Full-Width                  | │
│ | H1: Our readers read next                                          | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<article.article--no-t) — 1-Col (gap: normal 16p)  | │
│ | [ Card 1: Lucy Powell promotes UK education in China despit...   ] | │
│ | [ Card 2: Global climate talks have collapsed. Here’s what...    ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<article.article:nth(2)>) — 1-Col (Global left rallie) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.article__foote) | Stacked 390px Colophon             │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Persistent Left Sidebar Navigation (<nav.navigation-mini> — `200×700px` at `x=40`)**:
   - Fixed/sticky left rail `<nav class="navigation-mini header__edition-nav-alt">` (`200px` wide) paired with top bar `<header class="header">` hosting `Saving costs and improving liv` navigation (`Europe · UK · France · Germany · Spain`), DOM attributes (`data-previous-scroll-y="null"`, `data-wp-strategy="async"`, `data-id="adlibScripts"`, `data-marketo-munchkin="true"`), and rule `k-polylang-navigation-language-sw... { align-self:center }`.
2. **Hero Stage & Focal Lead (<article.article> — `Our readers read next`)**:
   - Landmark `<article class="article article--no-top-margin">` inside `1440px` main stage presenting display lead `Our readers read next` and copy excerpt *"The above column is sponsor-generated content. To learn more abou"* over `#ffffff` canvas and `#0d0f16` ink.
3. **Primary Showcase & Content Grid (<article.article--no-top-margin> — `Lucy Powell promotes UK education `)**:
   - Landmark `<article class="article article--no-top-margin">` rendering section `Lucy Powell promotes UK education in China despit...` with copy *"is sponsor-generated"*, asset references (`wrap.js`, `munchkin.js`, `insight.min.js`, `uwt.js`), and grid rule `itcher .wp-block-navigation-item_... { align-items:center;display:inline-flex;line-height:normal;width:auto }`.
4. **Interactive Detail & Feature Matrix (<article.article:nth(2)> — `Global climate talks have collapse`)**:
   - Landmark `<article class="article article--no-top-margin">` framing `Global climate talks have collapsed. Here’s what...` and `Global left rallies in Paris to make ‘not so radi...` (*"Our readers read next"*) with `#dddddd` surface cards, `#ff0000` accents, and `on-language-switcher .pll-switche... { align-items:center;display:flex }`.
5. **Colophon & Global Directory Footer (<footer.article__footer-inline> — `https://www.politico.eu/sponsored-content/saving-costs-and-improving-lives/`)**:
   - Landmark `<footer class="article__footer-inline">` anchoring `Saving costs and improving lives` footer links (`Europe · UK · France · Germany · Spain`), copy *"Policy areas Agriculture and Food Central Banker Competition"*, and `#dadada` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-politico-eu_sponsored-content-saving-costs-and-improving-lives (Saving costs and improving lives – POLITICO)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-politico-eu_sponsored-content-saving-costs-and-improving-lives` (**Saving costs and improving lives – POLITICO** — `https://www.politico.eu/sponsored-content/saving-costs-and-improving-lives/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#0d0f16` ink, `#ff0000` accent).
- **Identity & Domain Context**: Visit the post for more.
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#0d0f16`, **Accent / Highlight**: `#ff0000`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#0d0f16` primary typography and `#ff0000` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Sohne` for display copy (`Our readers read next`) with `Martina Plantijn` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: normal 16px`, padding `40px`) with `cubic-bezier(.215,.61,.355,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-politico-eu_sponsored-content-saving-costs-and-improving-lives` in your global stylesheet:

:root {
  /* Saving costs and improving lives – POLITICO (www-politico-eu_sponsored-content-saving-costs-and-improving-lives) — Live-Grounded CSS Variables */
  --wp-block-synced-color: #7a00df; /* Brand / Palette Token (www-politico-eu_sponsored-content-saving-costs-and-improving-lives) */
  --wp-block-synced-color--rgb: 122,0,223; /* Brand / Palette Token (www-politico-eu_sponsored-content-saving-costs-and-improving-lives) */
  --wp-bound-block-color: var(--wp-block-synced-color); /* Brand / Palette Token (www-politico-eu_sponsored-content-saving-costs-and-improving-lives) */
  --wp-editor-canvas-background: #ddd; /* Canvas / Surface Token (www-politico-eu_sponsored-content-saving-costs-and-improving-lives) */
  --wp-admin-theme-color: #007cba; /* Brand / Palette Token (www-politico-eu_sponsored-content-saving-costs-and-improving-lives) */
  --wp-admin-theme-color--rgb: 0,124,186; /* Brand / Palette Token (www-politico-eu_sponsored-content-saving-costs-and-improving-lives) */
  --wp-admin-theme-color-darker-10: #006ba1; /* Canvas / Surface Token (www-politico-eu_sponsored-content-saving-costs-and-improving-lives) */
  --wp-admin-theme-color-darker-10--rgb: 0,107,160.5; /* Canvas / Surface Token (www-politico-eu_sponsored-content-saving-costs-and-improving-lives) */
  --wp-admin-theme-color-darker-20: #005a87; /* Canvas / Surface Token (www-politico-eu_sponsored-content-saving-costs-and-improving-lives) */
  --wp-admin-theme-color-darker-20--rgb: 0,90,135; /* Canvas / Surface Token (www-politico-eu_sponsored-content-saving-costs-and-improving-lives) */
  --wp-admin-border-width-focus: 2px; /* Layout / Spatial Grid Token (www-politico-eu_sponsored-content-saving-costs-and-improving-lives) */
  --wp-admin--admin-bar--position-offset: var(--wp-admin--admin-bar--height,0px); /* Dimension / Scale Token (www-politico-eu_sponsored-content-saving-costs-and-improving-lives) */
  --wp--custom--color--blue--100: #CCE5F4; /* Brand / Palette Token (www-politico-eu_sponsored-content-saving-costs-and-improving-lives) */
  --wp--custom--color--blue--300: #66B0DD; /* Brand / Palette Token (www-politico-eu_sponsored-content-saving-costs-and-improving-lives) */
  --wp--custom--color--blue--500: #007BC7; /* Brand / Palette Token (www-politico-eu_sponsored-content-saving-costs-and-improving-lives) */
  --wp--custom--color--blue--600: #00629F; /* Brand / Palette Token (www-politico-eu_sponsored-content-saving-costs-and-improving-lives) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#0d0f16` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#dddddd` — grounded in `var(--wp-editor-canvas-background)` in `:root`
- **Interactive Accent / Highlight**: `#ff0000` — grounded in `ant--primary .tags__tags .tags_... { background-color: red }` (`#ff0000`)
- **Secondary / Muted Copy**: `#1ea0c3` — grounded in `.wp-social-link-bandcamp { color: #1ea0c3 }`
- **Structural Hairline Border**: `#dadada` — grounded in `.sponsored-content-banner__bott... { border-top: #dadada }`
- **Variable Token (`--wp-block-synced-color`)**: `#7a00df` — grounded in `var(--wp-block-synced-color)` in `:root`
- **Variable Token (`--wp-admin-theme-color`)**: `#007cba` — grounded in `var(--wp-admin-theme-color)` in `:root`
- **Variable Token (`--wp-admin-theme-color-darker-10`)**: `#006ba1` — grounded in `var(--wp-admin-theme-color-darker-10)` in `:root`
- **Variable Token (`--wp-admin-theme-color-darker-20`)**: `#005a87` — grounded in `var(--wp-admin-theme-color-darker-20)` in `:root`
- **Variable Token (`--wp--custom--color--blue--100`)**: `#cce5f4` — grounded in `var(--wp--custom--color--blue--100)` in `:root`
- **Variable Token (`--wp--custom--color--blue--300`)**: `#66b0dd` — grounded in `var(--wp--custom--color--blue--300)` in `:root`
- **Variable Token (`--wp--custom--color--blue--500`)**: `#007bc7` — grounded in `var(--wp--custom--color--blue--500)` in `:root`
- **Variable Token (`--wp--custom--color--blue--600`)**: `#00629f` — grounded in `var(--wp--custom--color--blue--600)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1440px` (live computed `main` `max-width`)
- **Padding & Gutters**: `40px` lateral canvas padding with `normal 16px` grid gap
- **Desktop Grid**: 2-column persistent left sidebar (`200px`, <nav.navigation-mini>) + `1440px` main content stage at `1440px` (`max-width: 1440px`, `gap: normal 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with collapsed `<nav.navigation-mini>` drawer navigation and `40px` horizontal padding
- **Media Queries**: `@media (min-width:48em)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-width:80em)`, `@media (max-width:47.9375em)`
- **Corner Radii**: `36px`, `var(--wp--custom--radius--round-8)`, `50%`, `var(--wp--custom--radius--round-4)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Sohne`
- **Body Font Stack**: `Martina Plantijn`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`font-weight: var(--font-we...`)
- **H2 Section Rule**: live computed `h2` (`font-size: 20px`, `line-height: 30px`, `font-weight: 500`); rule `h2` (`font-weight: var(--font-we...`)
- **Body Copy Rule**: live computed `body` (`font-size: 20px`, `line-height: 30px`, `font-weight: 400`); rule `p` (`font-size: var(--wp--custom--type-scale-...`, `line-height: var(--wp--custom--typ...`, `font-weight: var(--font-we...`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 20px`, `line-height: 30px`, `font-weight: 400`); CSS variables `--wp--custom--animation--duration--small: 100ms`, `--wp--custom--animation--duration--extra-small: 50ms`, `--wp--custom--stroke--small: 1px`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-politico-eu_sponsored-content-saving-costs-and-improving-lives` (`Saving costs and improving lives – POLITICO`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Persistent Left Sidebar Navigation (<nav.navigation-mini> — `200×700px` at `x=40`)**:
   - DOM & Selectors: Fixed/sticky left rail `<nav class="navigation-mini header__edition-nav-alt">` (`200px` wide) paired with top bar `<header class="header">` hosting `Saving costs and improving liv` navigation (`Europe · UK · France · Germany · Spain`), DOM attributes (`data-previous-scroll-y="null"`, `data-wp-strategy="async"`, `data-id="adlibScripts"`, `data-marketo-munchkin="true"`), and rule `k-polylang-navigation-language-sw... { align-self:center }`.
   - Responsive Contract: Header `Persistent Left Sidebar Navigation (<nav.navigation-mini> — `200×700px` at `x=40`)` (`www-politico-eu_sponsored-content-saving-costs-and-improving-lives`) adapts across `@media (min-width:48em)`, `@media (prefers-reduced-motion:reduce)`, `@media (min-width:80em)`, `@media (max-width:47.9375em)` with `cubic-bezier(.215,.61,.355,1)`, `cubic-bezier(0.215,0.61,0.355,1)` transitions and links `Europe · UK · France · Germany · Spain`.
2. **Hero Stage & Focal Lead (<article.article> — `Our readers read next`)**:
   - DOM & Selectors: Landmark `<article class="article article--no-top-margin">` inside `1440px` main stage presenting display lead `Our readers read next` and copy excerpt *"The above column is sponsor-generated content. To learn more abou"* over `#ffffff` canvas and `#0d0f16` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#ffffff` background with `#0d0f16` headline `Our readers read next`.
3. **Primary Showcase & Content Grid (<article.article--no-top-margin> — `Lucy Powell promotes UK education `)**:
   - DOM & Selectors: Landmark `<article class="article article--no-top-margin">` rendering section `Lucy Powell promotes UK education in China despit...` with copy *"is sponsor-generated"*, asset references (`wrap.js`, `munchkin.js`, `insight.min.js`, `uwt.js`), and grid rule `itcher .wp-block-navigation-item_... { align-items:center;display:inline-flex;line-height:normal;width:auto }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<article.article--no-top-margin> — `Lucy Powell promotes UK education `)` applies 2-column persistent left sidebar (`200px`, <nav.navigation-mini>) + `1440px` main content stage at `1440px` (`max-width: 1440px`, `gap: normal 16px`) on desktop and Single-column vertical stack at `390px` viewport width with collapsed `<nav.navigation-mini>` drawer navigation and `40px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.article:nth(2)> — `Global climate talks have collapse`)**:
   - DOM & Selectors: Landmark `<article class="article article--no-top-margin">` framing `Global climate talks have collapsed. Here’s what...` and `Global left rallies in Paris to make ‘not so radi...` (*"Our readers read next"*) with `#dddddd` surface cards, `#ff0000` accents, and `on-language-switcher .pll-switche... { align-items:center;display:flex }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.article:nth(2)> — `Global climate talks have collapse`)` uses `36px`, `var(--wp--custom--radius--round-8)`, `50%`, `var(--wp--custom--radius--round-4)` radii, `#ff0000` highlights, and assets (wrap.js, munchkin.js, insight.min.js).
5. **Colophon & Global Directory Footer (<footer.article__footer-inline> — `https://www.politico.eu/sponsored-content/saving-costs-and-improving-lives/`)**:
   - DOM & Selectors: Landmark `<footer class="article__footer-inline">` anchoring `Saving costs and improving lives` footer links (`Europe · UK · France · Germany · Spain`), copy *"Policy areas Agriculture and Food Central Banker Competition"*, and `#dadada` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.article__footer-inline> — `https://www.politico.eu/sponsored-content/saving-costs-and-improving-lives/`)` aligns to `1440px` (live computed `main` `max-width`) with `40px` lateral canvas padding with `normal 16px` grid gap and attributes (data-previous-scroll-y="null", data-wp-strategy="async", data-id="adlibScripts").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"The above column is sponsor-generated content. To learn more about our advertising..."*
- Copy Excerpt 2: *"is sponsor-generated"*
- Copy Excerpt 3: *"Our readers read next"*
- Copy Excerpt 4: *"Policy areas Agriculture and Food Central Banker Competition and Industrial Policy..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.215,.61,.355,1)`, `cubic-bezier(0.215,0.61,0.355,1)`
- **Extracted Stylesheet Rules (`www-politico-eu_sponsored-content-saving-costs-and-improving-lives`)**:
- `k-polylang-navigation-language-sw... { align-self:center }`
- `itcher .wp-block-navigation-item_... { align-items:center;display:inline-flex;line-height:normal;width:auto }`
- `on-language-switcher .pll-switche... { align-items:center;display:flex }`
- `.pll-switcher { box-sizing:border-box;display:block;width:100% }`
- `.pll-switcher ul { line-height:normal;list-style:none;margin:0;padding:0 }`
- **Per-Selector Transition Rules**:
- **Selector `media (prefers-reduced-motion:red...`**: `transition: 1ms!important` extracted from `www-politico-eu_sponsored-content-saving-costs-and-improving-lives` stylesheet.
- **Selector `a:where(:not(.wp-element-button))`**: `transition: color var(--transition-style-link-out),background-color var(--...` extracted from `www-politico-eu_sponsored-content-saving-costs-and-improving-lives` stylesheet.
- **Selector `a:where(:not(.wp-element-button))...`**: `transition: color var(--transition-style-link-in),background-color var(--t...` extracted from `www-politico-eu_sponsored-content-saving-costs-and-improving-lives` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.215,.61,.355,1)`)**: Governs interactive state transitions across `<header.header>` and `<article.article--no-top-margin>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-politico-eu_sponsored-content-saving-costs-and-improving-lives`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
