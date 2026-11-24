---
title: "UI Prompt Blueprint: lifetimepastapass-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "lifetimepastapass-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: native
desktop_keyframes: 2
subpages_crawled: 3
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#0a0a0a` / `#ffff00`)"
---

# UI Design System & Master Generation Blueprint: lifetimepastapass-com

> **LIFETIME PASTA PASS · BRADEN'S INFINITE TOUR OF ITALY** (https://lifetimepastapass.com) — Braden is an Olive Garden Lifetime Pasta Pass holder. Now the internet votes on what he eats next. Live results, vote history, and the fu...

![Desktop Journey Filmstrip (1280x1656)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x872)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **LIFETIME PASTA PASS · BRADEN'S INFINITE TOUR OF ITALY** (`https://lifetimepastapass.com`). Braden is an Olive Garden Lifetime Pasta Pass holder. Now the internet votes on what he eats next. Live results, vote history, and the fu...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#0a0a0a` / `#ffff00`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#0a0a0a` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#f5f5f5` primary typography and `#ffff00` accents.
  - **Grounded Typographic Hierarchy**: Uses `VT323` across display (`Vote on what a LIFETIME PASTA PASS h`) and body copy.
  - **Calibrated Spatial Grid & Motion**: Combines `1200px` container bounds (`gap: 6.4px`, padding `20px`) with `cubic-bezier(.4,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×1656px` (`assets/desktop-journey.webp`, `2` keyframes up to `y=4416px` / doc `5316px`), Mobile `390×872px` (`assets/mobile-journey.webp`, `1` keyframes).
- **Master Container Bounds**: `1200px` (live computed `main` `max-width`).
- **Canvas Lateral Padding & Spacing**: `20px` lateral canvas padding with `6.4px` grid gap.
- **Border Radius Scale**: `50%`, `2px`, `6px`, `4px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1200px`, `gap: 6.4px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `20px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width: 641px)`, `@media (max-width: 640px)`, `@media (max-width: 480px)`, `@media (min-width: 900px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0a0a0a` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f5f5f5` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#141414` | live computed `nav` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ffff00` | `.mp-btn:hover { background: yellow }` (`#ffff00`) |
| **Secondary / Muted Copy** | `#ff2079` | live computed `footer` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#747775` | `var(--chat-messenger-color--outline-active)` in `:root` |
| **Variable Token (`--neon-green`)** | `#39ff14` | `var(--neon-green)` in `:root` |
| **Variable Token (`--neon-yellow`)** | `#ffe900` | `var(--neon-yellow)` in `:root` |
| **Variable Token (`--neon-cyan`)** | `#00e5ff` | `var(--neon-cyan)` in `:root` |
| **Variable Token (`--trophy-bronze`)** | `#d98a3d` | `var(--trophy-bronze)` in `:root` |
| **Variable Token (`--trophy-silver`)** | `#d8d8e2` | `var(--trophy-silver)` in `:root` |
| **Variable Token (`--trophy-gold`)** | `#ffd700` | `var(--trophy-gold)` in `:root` |
| **Variable Token (`--bada-bing`)** | `#ff7a3d` | `var(--bada-bing)` in `:root` |
| **Variable Token (`--bada-boom`)** | `#ff2b1f` | `var(--bada-boom)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#0a0a0a` | Canvas / Surface Token |
| `--bg-panel` | `#141414` | Canvas / Surface Token |
| `--neon-green` | `#39ff14` | Color / Atmospheric Token |
| `--neon-pink` | `#ff2079` | Typography Ink Token |
| `--neon-yellow` | `#ffe900` | Color / Atmospheric Token |
| `--neon-cyan` | `#00e5ff` | Color / Atmospheric Token |
| `--white` | `#f5f5f5` | Canvas / Surface Token |
| `--pixel-font` | `'Press Start 2P', monospace` | Typography / Scale Token |
| `--body-font` | `'VT323', monospace` | Typography / Scale Token |
| `--trophy-bronze` | `#d98a3d` | Color / Atmospheric Token |
| `--trophy-silver` | `#d8d8e2` | Color / Atmospheric Token |
| `--trophy-gold` | `#ffd700` | Color / Atmospheric Token |
| `--bada-bing` | `#ff7a3d` | Color / Atmospheric Token |
| `--bada-boom` | `#ff2b1f` | Color / Atmospheric Token |
| `--hover-lift-amount` | `4px` | Dimension / Scale Token |
| `--hover-scale-amount` | `1.03` | Design System Custom Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `VT323`.
- **Primary Body Stack**: `VT323`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: CSS variables `--header-logo-display: none`, `--header-logo-inverse-display: block`; rule `h1` (`line-height: var(--line-height--di...`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 20.8px`, `line-height: normal`, `font-weight: 700`, `letter-spacing: 1px`); rule `h2` (`font-size: 1.1rem`).
- **Body Copy**: live computed `body` (`font-size: 19px`, `line-height: normal`, `font-weight: 400`); CSS variables `--body-font: 'VT323', monospace`, `--font-paragraph--line-height: 1`, `--body-text-font-weight: 400`; rule `body` (`font-size: 19px`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 19px`, `line-height: normal`, `font-weight: 400`); CSS variables `--checkbox-label-padding: 8px`, `--image-height-small: calc(var(--image-height-basis) * 2)`, `--pill-label-padding-inline: var(--padding-xs)`; rule `small` (`font-size: calc(var(--kl-reviews-reviews...`, `font-weight: var(--kl-revi...`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(0.5,0,0.5,1)`, `cubic-bezier(0.4,0,0.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.hamburger span`**: `transition: transform 0.15s steps(3)` extracted from `lifetimepastapass-com` stylesheet.
- **Selector `.site-nav`**: `transition: right 0.2s steps(6)` extracted from `lifetimepastapass-com` stylesheet.
- **Selector `.status-icon`**: `transition: filter 0.15s ease, opacity 0.15s ease` extracted from `lifetimepastapass-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.visits-section>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `5316px`, deepest scrollY reached `4416px` across `2` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `WebGL/Canvas`.
- **Nav / Drawer Probe (`Menu`)**: Triggered visual change (pixel diff `25.271`, captured in `assets/state-nav.webp`); revealed links: BRADEN'S INFINITE TOU..., Email Braden.
- **Hover Physics (`primary_cta` · `Vote`)**: `transform`: `none` -> `matrix(1, 0, 0, 1, 1, 1)`; `boxShadow`: `rgb(255, 32, 121) 3px 3...` -> `rgb(255, 32, 121) 2px 2...` (`transition-duration: 0s`, `timing: ease`).
- **Route Transition Architecture**: First internal navigation (`/out/newks-sauce`) measured as `direct` in `5632ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — LIFETIME PASTA PASS · BRADEN'S INFINITE TO │
│ ====================================================================== │
│ [ <header.site-header> (1440x66px)    | Home · Trophy Case · OG Merc ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.poll-section> (w=1200px)                      | │
│ | H1: Vote on what a LIFETIME PASTA PASS holder eats next            | │
│ | Substrate: #0a0a0a | Ink: #f5f5f5 | Accent: #ffff00                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.visits-section>) max-w: 1200px             | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Second Sauce                 |  | Embed This Poll              | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.visits-section:nt) — Things are heating up | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>) | https://lifetimepastapass.com        │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 6.4px)      │
│ ====================================================================== │
│ [ HEADER BAR (<header.site-header>    ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.poll-section>) — 390px Vertical Lead          | │
│ | H1: Vote on what a LIFETIME PASTA PASS holder eats next            | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.visits-sectio) — 1-Col Stack              | │
│ | [ Item 1: Second Sauce                                           ] | │
│ | [ Item 2: Embed This Poll                                        ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.visits-section:) — 1-Col (Things are heating) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.site-header> — `lifetimepastapass-com`)**:
   - Landmark `<header class="site-header">` (`1440x66px`) hosting `LIFETIME PASTA PASS · BRADEN'S INFIN` navigation (`Home · Trophy Case · OG Merch Gallery · Backstory · Get in Touch`), DOM attributes (`data-address="braden@lifetimepastap..."`, `data-track="mailapp"`, `data-category="Pasta"`, `data-category="Pasta"`), and stylesheet rule `h3 { font-family: var(--pixel-font); text-transform: uppercase; letter-spacin... }`.
2. **Hero Stage & Focal Lead (<section.poll-section> — `Vote on what a LIFETIME PASTA PASS`)**:
   - Landmark `<section class="poll-section">` presenting display lead `Vote on what a LIFETIME PASTA PASS holder eats next` and copy excerpt *"Use discount code PASTAPASS for 10% off Newks Hot Sauce!"* over `#0a0a0a` canvas and `#f5f5f5` ink.
3. **Primary Showcase & Content Grid (<section.visits-section> — `Second Sauce`)**:
   - Landmark `<section class="visits-section">` rendering section `Second Sauce` with copy *"LIFETIME PASTA PASS"*, asset references (`fonts.googleapis.com`, `css2`, `style.css`, `card.png (Lifetime Pasta Pass card)`), and grid rule `.site-header { position: sticky; top: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.visits-section:nth(2)> — `Embed This Poll`)**:
   - Landmark `<section class="visits-section">` framing `Embed This Poll` and `Things are heating up!` (*"33% (10) Continue your pasta adventure to unlock new roles, and u"*) with `#141414` surface cards, `#ffff00` accents, and `.site-nav.open { right: 0; }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://lifetimepastapass.com`)**:
   - Landmark `<footer class="site-footer">` anchoring `LIFETIME PASTA PASS · BRADEN'S I` footer links (`Home · Trophy Case · OG Merch Gallery · Backstory · Get in Touch`), copy *"Continue your pasta adventure to unlock new roles, and use t"*, and `#747775` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=117px`, `0%`): Active landmark `THINGS ARE HEATING UP!` · sticky/fixed elements: `0`
- **Step 02** (`y=4416px`, `100%`): Active landmark `THINGS ARE HEATING UP!` · sticky/fixed elements: `0`

### Multi-Page Internal Route Map
- **Detail Route (`/out/newks-sauce`)**: `https://lifetimepastapass.com/out/newks-sauce` — H1: `Sauces – Newks Sauces`, scrollHeight `5907px`, transition `direct` (`5632ms`)
- **Detail Route (`/out/newks-bing`)**: `https://lifetimepastapass.com/out/newks-bing` — H1: `Newks Bada-Bing Hot Sauce (Calabrian Chili Sauce)`, scrollHeight `6251px`, transition `direct` (`3828ms`)
- **Detail Route (`/out/newks-boom`)**: `https://lifetimepastapass.com/out/newks-boom` — H1: `BADA-BOOM`, scrollHeight `3150px`, transition `direct` (`7464ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: lifetimepastapass-com (LIFETIME PASTA PASS · BRADEN'S INFINITE TOUR OF ITALY)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `lifetimepastapass-com` (**LIFETIME PASTA PASS · BRADEN'S INFINITE TOUR OF ITALY** — `https://lifetimepastapass.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0a0a0a` / `#ffff00`).
- **Identity & Domain Context**: Braden is an Olive Garden Lifetime Pasta Pass holder. Now the internet votes on what he eats next. Live results, vote history, and the fu...
- **Primary Substrate**: `#0a0a0a` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#f5f5f5`, **Accent / Highlight**: `#ffff00`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#0a0a0a` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#f5f5f5` primary typography and `#ffff00` accents.
  - **Grounded Typographic Hierarchy**: Uses `VT323` across display (`Vote on what a LIFETIME PASTA PASS h`) and body copy.
  - **Calibrated Spatial Grid & Motion**: Combines `1200px` container bounds (`gap: 6.4px`, padding `20px`) with `cubic-bezier(.4,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `lifetimepastapass-com` in your global stylesheet:

:root {
  /* LIFETIME PASTA PASS · BRADEN'S INFINITE TOUR OF ITALY (lifetimepastapass-com) — Live-Grounded CSS Variables */
  --bg: #0a0a0a; /* Canvas / Surface Token (lifetimepastapass-com) */
  --bg-panel: #141414; /* Canvas / Surface Token (lifetimepastapass-com) */
  --neon-green: #39ff14; /* Color / Atmospheric Token (lifetimepastapass-com) */
  --neon-pink: #ff2079; /* Typography Ink Token (lifetimepastapass-com) */
  --neon-yellow: #ffe900; /* Color / Atmospheric Token (lifetimepastapass-com) */
  --neon-cyan: #00e5ff; /* Color / Atmospheric Token (lifetimepastapass-com) */
  --white: #f5f5f5; /* Canvas / Surface Token (lifetimepastapass-com) */
  --pixel-font: 'Press Start 2P', monospace; /* Typography / Scale Token (lifetimepastapass-com) */
  --body-font: 'VT323', monospace; /* Typography / Scale Token (lifetimepastapass-com) */
  --trophy-bronze: #d98a3d; /* Color / Atmospheric Token (lifetimepastapass-com) */
  --trophy-silver: #d8d8e2; /* Color / Atmospheric Token (lifetimepastapass-com) */
  --trophy-gold: #ffd700; /* Color / Atmospheric Token (lifetimepastapass-com) */
  --bada-bing: #ff7a3d; /* Color / Atmospheric Token (lifetimepastapass-com) */
  --bada-boom: #ff2b1f; /* Color / Atmospheric Token (lifetimepastapass-com) */
  --hover-lift-amount: 4px; /* Dimension / Scale Token (lifetimepastapass-com) */
  --hover-scale-amount: 1.03; /* Design System Custom Token (lifetimepastapass-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#0a0a0a` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#f5f5f5` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#141414` — grounded in live computed `nav` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#ffff00` — grounded in `.mp-btn:hover { background: yellow }` (`#ffff00`)
- **Secondary / Muted Copy**: `#ff2079` — grounded in live computed `footer` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#747775` — grounded in `var(--chat-messenger-color--outline-active)` in `:root`
- **Variable Token (`--neon-green`)**: `#39ff14` — grounded in `var(--neon-green)` in `:root`
- **Variable Token (`--neon-yellow`)**: `#ffe900` — grounded in `var(--neon-yellow)` in `:root`
- **Variable Token (`--neon-cyan`)**: `#00e5ff` — grounded in `var(--neon-cyan)` in `:root`
- **Variable Token (`--trophy-bronze`)**: `#d98a3d` — grounded in `var(--trophy-bronze)` in `:root`
- **Variable Token (`--trophy-silver`)**: `#d8d8e2` — grounded in `var(--trophy-silver)` in `:root`
- **Variable Token (`--trophy-gold`)**: `#ffd700` — grounded in `var(--trophy-gold)` in `:root`
- **Variable Token (`--bada-bing`)**: `#ff7a3d` — grounded in `var(--bada-bing)` in `:root`
- **Variable Token (`--bada-boom`)**: `#ff2b1f` — grounded in `var(--bada-boom)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×1656px` (full-page live capture (1656px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×872px` (full-page live capture (872px), `390px` standard mobile width).
- **Container Max-Width**: `1200px` (live computed `main` `max-width`)
- **Padding & Gutters**: `20px` lateral canvas padding with `6.4px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1200px`, `gap: 6.4px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `20px` horizontal padding
- **Media Queries**: `@media (min-width: 641px)`, `@media (max-width: 640px)`, `@media (max-width: 480px)`, `@media (min-width: 900px)`
- **Corner Radii**: `50%`, `2px`, `6px`, `4px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `VT323`
- **Body Font Stack**: `VT323`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--header-logo-display: none`, `--header-logo-inverse-display: block`; rule `h1` (`line-height: var(--line-height--di...`)
- **H2 Section Rule**: live computed `h2` (`font-size: 20.8px`, `line-height: normal`, `font-weight: 700`, `letter-spacing: 1px`); rule `h2` (`font-size: 1.1rem`)
- **Body Copy Rule**: live computed `body` (`font-size: 19px`, `line-height: normal`, `font-weight: 400`); CSS variables `--body-font: 'VT323', monospace`, `--font-paragraph--line-height: 1`, `--body-text-font-weight: 400`; rule `body` (`font-size: 19px`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 19px`, `line-height: normal`, `font-weight: 400`); CSS variables `--checkbox-label-padding: 8px`, `--image-height-small: calc(var(--image-height-basis) * 2)`, `--pill-label-padding-inline: var(--padding-xs)`; rule `small` (`font-size: calc(var(--kl-reviews-reviews...`, `font-weight: var(--kl-revi...`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `lifetimepastapass-com` (`LIFETIME PASTA PASS · BRADEN'S INFINITE TOUR OF ITALY`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.site-header> — `lifetimepastapass-com`)**:
   - DOM & Selectors: Landmark `<header class="site-header">` (`1440x66px`) hosting `LIFETIME PASTA PASS · BRADEN'S INFIN` navigation (`Home · Trophy Case · OG Merch Gallery · Backstory · Get in Touch`), DOM attributes (`data-address="braden@lifetimepastap..."`, `data-track="mailapp"`, `data-category="Pasta"`, `data-category="Pasta"`), and stylesheet rule `h3 { font-family: var(--pixel-font); text-transform: uppercase; letter-spacin... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.site-header> — `lifetimepastapass-com`)` (`lifetimepastapass-com`) adapts across `@media (min-width: 641px)`, `@media (max-width: 640px)`, `@media (max-width: 480px)`, `@media (min-width: 900px)` with `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(0.5,0,0.5,1)`, `cubic-bezier(0.4,0,0.2,1)` transitions and links `Home · Trophy Case · OG Merch Gallery · Backstory · Get in Touch`.
2. **Hero Stage & Focal Lead (<section.poll-section> — `Vote on what a LIFETIME PASTA PASS`)**:
   - DOM & Selectors: Landmark `<section class="poll-section">` presenting display lead `Vote on what a LIFETIME PASTA PASS holder eats next` and copy excerpt *"Use discount code PASTAPASS for 10% off Newks Hot Sauce!"* over `#0a0a0a` canvas and `#f5f5f5` ink.
   - Responsive Contract: Hero stage (`1280×1656px` desktop / `390×872px` mobile) sets `#0a0a0a` background with `#f5f5f5` headline `Vote on what a LIFETIME PASTA PASS holder eats next`.
3. **Primary Showcase & Content Grid (<section.visits-section> — `Second Sauce`)**:
   - DOM & Selectors: Landmark `<section class="visits-section">` rendering section `Second Sauce` with copy *"LIFETIME PASTA PASS"*, asset references (`fonts.googleapis.com`, `css2`, `style.css`, `card.png (Lifetime Pasta Pass card)`), and grid rule `.site-header { position: sticky; top: 0; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.visits-section> — `Second Sauce`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1200px`, `gap: 6.4px`) on desktop and Single-column vertical stack at `390px` viewport width with `20px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.visits-section:nth(2)> — `Embed This Poll`)**:
   - DOM & Selectors: Landmark `<section class="visits-section">` framing `Embed This Poll` and `Things are heating up!` (*"33% (10) Continue your pasta adventure to unlock new roles, and u"*) with `#141414` surface cards, `#ffff00` accents, and `.site-nav.open { right: 0; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.visits-section:nth(2)> — `Embed This Poll`)` uses `50%`, `2px`, `6px`, `4px` radii, `#ffff00` highlights, and assets (fonts.googleapis.com, css2, style.css).
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://lifetimepastapass.com`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer">` anchoring `LIFETIME PASTA PASS · BRADEN'S I` footer links (`Home · Trophy Case · OG Merch Gallery · Backstory · Get in Touch`), copy *"Continue your pasta adventure to unlock new roles, and use t"*, and `#747775` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-footer> — `https://lifetimepastapass.com`)` aligns to `1200px` (live computed `main` `max-width`) with `20px` lateral canvas padding with `6.4px` grid gap and attributes (data-address="braden@lifetimepastap...", data-track="mailapp", data-category="Pasta").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Use discount code PASTAPASS for 10% off Newks Hot Sauce!"*
- Copy Excerpt 2: *"LIFETIME PASTA PASS"*
- Copy Excerpt 3: *"33% (10) Continue your pasta adventure to unlock new roles, and use the perks that..."*
- Copy Excerpt 4: *"Continue your pasta adventure to unlock new roles, and use the perks that come wit..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(0.5,0,0.5,1)`, `cubic-bezier(0.4,0,0.2,1)`
- **Extracted Stylesheet Rules (`lifetimepastapass-com`)**:
- `h3 { font-family: var(--pixel-font); text-transform: uppercase; letter-spacin... }`
- `.site-header { position: sticky; top: 0; }`
- `.site-nav.open { right: 0; }`
- `.site-nav a.active { border-color: var(--neon-green); background: rgba(57, 255, 20, 0.1); col... }`
- `.nav-overlay { display: none; position: fixed; inset: 0; background: rgba(0, 0, 0, 0.7)... }`
- **Per-Selector Transition Rules**:
- **Selector `.hamburger span`**: `transition: transform 0.15s steps(3)` extracted from `lifetimepastapass-com` stylesheet.
- **Selector `.site-nav`**: `transition: right 0.2s steps(6)` extracted from `lifetimepastapass-com` stylesheet.
- **Selector `.status-icon`**: `transition: filter 0.15s ease, opacity 0.15s ease` extracted from `lifetimepastapass-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.visits-section>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `5316px` across 2 distinct viewport chapters using WebGL/Canvas.
- **Vertical Chapter Sequence**: THINGS ARE HEATING UP! (0%) -> THINGS ARE HEATING UP! (100%).
- **Navigation Drawer / Menu State**: Replicate interactive menu toggle (`Menu`) with Escape-to-close keyboard handling.
- **Hover Micro-Interaction (`primary_cta`)**: Animate `transform, boxShadow` with `0s ease`.
- **Multi-Page Routes**: Scaffold internal routes `/out/newks-sauce` (detail, direct), `/out/newks-bing` (detail, direct), `/out/newks-boom` (detail, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `lifetimepastapass-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `117px` | `0%` | THINGS ARE HEATING UP! | `0` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `4416px` | `100%` | THINGS ARE HEATING UP! | `0` | [desktop-step-02.webp](assets/desktop-step-02.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | VOTE ON WHAT A LIFETIME PASTA PASS HOLDER... | [mobile-step-01.webp](assets/mobile-step-01.webp) |

### Interactive UI State Captures (`1440×900` WebP)
| State Type | Trigger / Observation | Visual Asset |
| :--- | :--- | :--- |
| `nav_menu` | Nav/Menu opened (`Menu`, diff `25.271`) | [state-nav.webp](assets/state-nav.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `detail` | `https://lifetimepastapass.com/out/newks-sauce` | Sauces – Newks Sauces | `5907px` | `direct` (`5632ms`) | [subpage-01-out-newks-sauce.webp](assets/subpage-01-out-newks-sauce.webp) |
| `2` | `detail` | `https://lifetimepastapass.com/out/newks-bing` | Newks Bada-Bing Hot Sauce (Calabrian... | `6251px` | `direct` (`3828ms`) | [subpage-02-out-newks-bing.webp](assets/subpage-02-out-newks-bing.webp) |
| `3` | `detail` | `https://lifetimepastapass.com/out/newks-boom` | BADA-BOOM | `3150px` | `direct` (`7464ms`) | [subpage-03-out-newks-boom.webp](assets/subpage-03-out-newks-boom.webp) |

