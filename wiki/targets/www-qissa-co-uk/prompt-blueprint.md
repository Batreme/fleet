---
title: "UI Prompt Blueprint: www-qissa-co-uk"
date: 2026-11-24
captured_at: 2026-11-24
target: "www-qissa-co-uk"
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
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#0a1230` / `#0c1533`)"
---

# UI Design System & Master Generation Blueprint: www-qissa-co-uk

> **Indian Restaurant in Sevenoaks, Kent · Qissa** (https://www.qissa.co.uk/) — Qissa — A Tale of Food. Modern Indian dining beneath the blossoms in the heart of Sevenoaks, Kent. Reserve a table or order takeaway. Rat...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Indian Restaurant in Sevenoaks, Kent · Qissa** (`https://www.qissa.co.uk/`). Qissa — A Tale of Food. Modern Indian dining beneath the blossoms in the heart of Sevenoaks, Kent. Reserve a table or order takeaway. Rat...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#0a1230` / `#0c1533`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#0a1230` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#f6f1e7` primary typography and `#0c1533` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Cormorant Garamond` for display copy (`Qissa`) with `Manrope`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 22px`, padding `72px`) with `cubic-bezier(.22,.61,.36,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=10842px` / doc `11788px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `72px` lateral canvas padding with `22px` grid gap.
- **Border Radius Scale**: `100%`, `100px`, `50%`, `var(--radius)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 22px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `72px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion: reduce)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:560px)`, `@media (max-width:820px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0a1230` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f6f1e7` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#23282d` | `.wpcf7-spinner { background-color: #23282d }` |
| **Interactive Accent / Highlight** | `#0c1533` | `.cta-band { background: #0c1533 }` |
| **Secondary / Muted Copy** | `#05091a` | `var(--ink)` in `:root` |
| **Structural Hairline Border** | `#1e2c57` | `var(--navy-line)` in `:root` |
| **Variable Token (`--navy-2`)** | `#0e1838` | `var(--navy-2)` in `:root` |
| **Variable Token (`--navy-3`)** | `#16224a` | `var(--navy-3)` in `:root` |
| **Variable Token (`--gold`)** | `#c9a24b` | `var(--gold)` in `:root` |
| **Variable Token (`--gold-hi`)** | `#efd79a` | `var(--gold-hi)` in `:root` |
| **Variable Token (`--gold-deep`)** | `#9a7a34` | `var(--gold-deep)` in `:root` |
| **Variable Token (`--amber`)** | `#e9a85c` | `var(--amber)` in `:root` |
| **Variable Token (`--blossom`)** | `#e7a6c4` | `var(--blossom)` in `:root` |
| **Variable Token (`--blossom-2`)** | `#f2c6d9` | `var(--blossom-2)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#05091A` | Typography Ink Token |
| `--navy` | `#0A1230` | Layout / Spatial Grid Token |
| `--navy-2` | `#0E1838` | Layout / Spatial Grid Token |
| `--navy-3` | `#16224A` | Layout / Spatial Grid Token |
| `--navy-line` | `#1E2C57` | Layout / Spatial Grid Token |
| `--gold` | `#C9A24B` | Color / Atmospheric Token |
| `--gold-hi` | `#EFD79A` | Color / Atmospheric Token |
| `--gold-deep` | `#9A7A34` | Color / Atmospheric Token |
| `--amber` | `#E9A85C` | Color / Atmospheric Token |
| `--blossom` | `#E7A6C4` | Color / Atmospheric Token |
| `--blossom-2` | `#F2C6D9` | Color / Atmospheric Token |
| `--cream` | `#F6F1E7` | Color / Atmospheric Token |
| `--cream-dim` | `rgba(246,241,231,.70)` | Color / Atmospheric Token |
| `--cream-faint` | `rgba(246,241,231,.42)` | Color / Atmospheric Token |
| `--line` | `rgba(201,162,75,.22)` | Color / Atmospheric Token |
| `--line-soft` | `rgba(246,241,231,.10)` | Color / Atmospheric Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Cormorant Garamond`.
- **Primary Body Stack**: `Manrope`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 121.6px`, `line-height: 119.168px`, `font-weight: 330`, `letter-spacing: -2.432px`); CSS variables `--f-display: 'Cormorant Garamond', 'Times New Roman', serif`; rule `.hero-title` (`font-size: clamp(2rem,9vw,7.6rem)`, `letter-spacing: -.02em`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 64px`, `line-height: 62.72px`, `font-weight: 330`, `letter-spacing: -1.28px`); rule `.h2` (`font-size: clamp(2rem,4.6vw,3.6rem)`, `letter-spacing: -.015em`, `font-weight: 340`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 350`); CSS variables `--f-body: 'Manrope', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`; rule `body` (`line-height: 1.6`, `font-weight: 350`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 350`); rule `small` (`font-size: .7rem`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.22,.61,.36,1)`, `cubic-bezier(.65,.05,.36,1)`, `cubic-bezier(0.22,1,0.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.btn`**: `transition: transform .5s var(--ease),box-shadow .5s var(--ease),backgroun...` extracted from `www-qissa-co-uk` stylesheet.
- **Selector `.btn svg`**: `transition: transform .5s var(--ease)` extracted from `www-qissa-co-uk` stylesheet.
- **Selector `.site-header`**: `transition: padding .5s var(--ease),background .5s var(--ease),backdrop-fi...` extracted from `www-qissa-co-uk` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,.61,.36,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.section>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `11788px`, deepest scrollY reached `10842px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `WebGL/Canvas`.
- **Nav / Drawer Probe (`MENU`)**: Triggered visual change (pixel diff `29.403`, captured in `assets/state-nav.webp`); revealed links: Qissa — A Tale of Food, ORDER, RESERVE, VIEW MENU, RESERVE A TABLE.
- **Hover Physics (`primary_cta` · `VIEW MENU`)**: `transform`: `none` -> `matrix(1, 0, 0, 1, 0, -...`; `color`: `rgb(246, 241, 231)` -> `rgb(240, 217, 160)`; `borderColor`: `rgba(201, 162, 75, 0.22)` -> `rgb(201, 162, 75)` (`transition-duration: 0.5s, 0.5s, 0.4s, 0.4s`, `timing: cubic-bezier(0.22, 0.61, 0.36, 1), cubic-bezier(0.22, 0.61, 0.36, 1), ease, ease`).
- **Route Transition Architecture**: First internal navigation (`/journal/`) measured as `direct` in `1690ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Indian Restaurant in Sevenoaks, Kent · Qis │
│ ====================================================================== │
│ [ <header.site-header> (1440x136px)   | 00 Home · 01 Our Story · 02  ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero> (w=1440px)                              | │
│ | H1: Qissa                                                          | │
│ | Substrate: #0a1230 | Ink: #f6f1e7 | Accent: #0c1533                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.section>) max-w: 1440px                    | │
│ | +------------------------------+  +------------------------------+ | │
│ | | A word that means a tale.    |  | Crafted icons & signature pl | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.masterpieces>) — Explore the menu, cou     | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>) | https://www.qissa.co.uk/             │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 22px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.site-header>    ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.hero>) — 390px Vertical Lead                  | │
│ | H1: Qissa                                                          | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.section>) — 1-Col Stack                   | │
│ | [ Item 1: A word that means a tale.                              ] | │
│ | [ Item 2: Crafted icons & signature plates.                      ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.masterpieces>) — 1-Col (Explore the menu, ) | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.site-header> — `www-qissa-co-uk`)**:
   - Landmark `<header class="site-header">` (`1440x136px`) hosting `Indian Restaurant in Sevenoaks, Kent` navigation (`00 Home · 01 Our Story · 02 The Menu · Food Menu · Drinks Menu`), DOM attributes (`data-u="contact"`, `data-d="qissa.co.uk"`, `data-tilt`, `data-count="4.8"`), and stylesheet rule `.wpcf7 .hidden-fields-container { display: none; }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Qissa`)**:
   - Landmark `<section class="hero">` presenting display lead `Qissa` and copy excerpt *"Celebrating the flavors of India with dishes inspired by differen"* over `#0a1230` canvas and `#f6f1e7` ink.
3. **Primary Showcase & Content Grid (<section.section> — `A word that means a tale.`)**:
   - Landmark `<section class="section">` rendering section `A word that means a tale.` with copy *"Food is all about its story — the origin, the spices, the texture"*, asset references (`gtm.js`, `hero-poster.webp`, `favicon-96.png`, `favicon-32.png`), and grid rule `.wpcf7 form .wpcf7-response-output { margin: 2em 0.5em 1em; padding: 0.2em 1em; border: 2px solid 00a0d2; }`.
4. **Interactive Detail & Feature Matrix (<section.masterpieces> — `Crafted icons & signature plates.`)**:
   - Landmark `<section class="section masterpieces">` framing `Crafted icons & signature plates.` and `Explore the menu, course by course.` (*"‘Qissa’ tells the extraordinary stories behind the foods we eat: "*) with `#23282d` surface cards, `#0c1533` accents, and `form.submitting .wpcf7-response-o... { display: none; }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://www.qissa.co.uk/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Indian Restaurant in Sevenoaks, ` footer links (`00 Home · 01 Our Story · 02 The Menu · Food Menu · Drinks Menu`), copy *"Qissa is a place of gathering, of celebrations, of business,"*, and `#1e2c57` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `Qissa` · sticky/fixed elements: `1`
- **Step 02** (`y=850px`, `8%`): Active landmark `A word that means a tale.` · sticky/fixed elements: `1`
- **Step 03** (`y=2550px`, `24%`): Active landmark `Section @ 24%` · sticky/fixed elements: `1`
- **Step 04** (`y=4250px`, `39%`): Active landmark `A feast worth gathering for.` · sticky/fixed elements: `1`
- **Step 05** (`y=6800px`, `62%`): Active landmark `Beneath the blossoms.` · sticky/fixed elements: `1`
- **Step 06** (`y=8500px`, `78%`): Active landmark `Section @ 78%` · sticky/fixed elements: `1`
- **Step 07** (`y=10200px`, `94%`): Active landmark `Reserve a Table` · sticky/fixed elements: `1`
- **Step 08** (`y=10842px`, `100%`): Active landmark `EXPLORE` · sticky/fixed elements: `1`

### Multi-Page Internal Route Map
- **Listing Route (`/journal/`)**: `https://www.qissa.co.uk/journal/` — H1: `Journal`, scrollHeight `2634px`, transition `direct` (`1690ms`)
- **About Route (`/story/`)**: `https://www.qissa.co.uk/story/` — H1: `Our Story`, scrollHeight `4585px`, transition `direct` (`649ms`)
- **About Route (`/contact/`)**: `https://www.qissa.co.uk/contact/` — H1: `Visit Us`, scrollHeight `2952px`, transition `direct` (`1235ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-qissa-co-uk (Indian Restaurant in Sevenoaks, Kent · Qissa)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-qissa-co-uk` (**Indian Restaurant in Sevenoaks, Kent · Qissa** — `https://www.qissa.co.uk/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0a1230` / `#0c1533`).
- **Identity & Domain Context**: Qissa — A Tale of Food. Modern Indian dining beneath the blossoms in the heart of Sevenoaks, Kent. Reserve a table or order takeaway. Rat...
- **Primary Substrate**: `#0a1230` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#f6f1e7`, **Accent / Highlight**: `#0c1533`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#0a1230` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#f6f1e7` primary typography and `#0c1533` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Cormorant Garamond` for display copy (`Qissa`) with `Manrope`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 22px`, padding `72px`) with `cubic-bezier(.22,.61,.36,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-qissa-co-uk` in your global stylesheet:

:root {
  /* Indian Restaurant in Sevenoaks, Kent · Qissa (www-qissa-co-uk) — Live-Grounded CSS Variables */
  --ink: #05091A; /* Typography Ink Token (www-qissa-co-uk) */
  --navy: #0A1230; /* Layout / Spatial Grid Token (www-qissa-co-uk) */
  --navy-2: #0E1838; /* Layout / Spatial Grid Token (www-qissa-co-uk) */
  --navy-3: #16224A; /* Layout / Spatial Grid Token (www-qissa-co-uk) */
  --navy-line: #1E2C57; /* Layout / Spatial Grid Token (www-qissa-co-uk) */
  --gold: #C9A24B; /* Color / Atmospheric Token (www-qissa-co-uk) */
  --gold-hi: #EFD79A; /* Color / Atmospheric Token (www-qissa-co-uk) */
  --gold-deep: #9A7A34; /* Color / Atmospheric Token (www-qissa-co-uk) */
  --amber: #E9A85C; /* Color / Atmospheric Token (www-qissa-co-uk) */
  --blossom: #E7A6C4; /* Color / Atmospheric Token (www-qissa-co-uk) */
  --blossom-2: #F2C6D9; /* Color / Atmospheric Token (www-qissa-co-uk) */
  --cream: #F6F1E7; /* Color / Atmospheric Token (www-qissa-co-uk) */
  --cream-dim: rgba(246,241,231,.70); /* Color / Atmospheric Token (www-qissa-co-uk) */
  --cream-faint: rgba(246,241,231,.42); /* Color / Atmospheric Token (www-qissa-co-uk) */
  --line: rgba(201,162,75,.22); /* Color / Atmospheric Token (www-qissa-co-uk) */
  --line-soft: rgba(246,241,231,.10); /* Color / Atmospheric Token (www-qissa-co-uk) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#0a1230` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#f6f1e7` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#23282d` — grounded in `.wpcf7-spinner { background-color: #23282d }`
- **Interactive Accent / Highlight**: `#0c1533` — grounded in `.cta-band { background: #0c1533 }`
- **Secondary / Muted Copy**: `#05091a` — grounded in `var(--ink)` in `:root`
- **Structural Hairline Border**: `#1e2c57` — grounded in `var(--navy-line)` in `:root`
- **Variable Token (`--navy-2`)**: `#0e1838` — grounded in `var(--navy-2)` in `:root`
- **Variable Token (`--navy-3`)**: `#16224a` — grounded in `var(--navy-3)` in `:root`
- **Variable Token (`--gold`)**: `#c9a24b` — grounded in `var(--gold)` in `:root`
- **Variable Token (`--gold-hi`)**: `#efd79a` — grounded in `var(--gold-hi)` in `:root`
- **Variable Token (`--gold-deep`)**: `#9a7a34` — grounded in `var(--gold-deep)` in `:root`
- **Variable Token (`--amber`)**: `#e9a85c` — grounded in `var(--amber)` in `:root`
- **Variable Token (`--blossom`)**: `#e7a6c4` — grounded in `var(--blossom)` in `:root`
- **Variable Token (`--blossom-2`)**: `#f2c6d9` — grounded in `var(--blossom-2)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `72px` lateral canvas padding with `22px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 22px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `72px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion: reduce)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:560px)`, `@media (max-width:820px)`
- **Corner Radii**: `100%`, `100px`, `50%`, `var(--radius)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Cormorant Garamond`
- **Body Font Stack**: `Manrope`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 121.6px`, `line-height: 119.168px`, `font-weight: 330`, `letter-spacing: -2.432px`); CSS variables `--f-display: 'Cormorant Garamond', 'Times New Roman', serif`; rule `.hero-title` (`font-size: clamp(2rem,9vw,7.6rem)`, `letter-spacing: -.02em`)
- **H2 Section Rule**: live computed `h2` (`font-size: 64px`, `line-height: 62.72px`, `font-weight: 330`, `letter-spacing: -1.28px`); rule `.h2` (`font-size: clamp(2rem,4.6vw,3.6rem)`, `letter-spacing: -.015em`, `font-weight: 340`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 350`); CSS variables `--f-body: 'Manrope', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`; rule `body` (`line-height: 1.6`, `font-weight: 350`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 350`); rule `small` (`font-size: .7rem`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-qissa-co-uk` (`Indian Restaurant in Sevenoaks, Kent · Qissa`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.site-header> — `www-qissa-co-uk`)**:
   - DOM & Selectors: Landmark `<header class="site-header">` (`1440x136px`) hosting `Indian Restaurant in Sevenoaks, Kent` navigation (`00 Home · 01 Our Story · 02 The Menu · Food Menu · Drinks Menu`), DOM attributes (`data-u="contact"`, `data-d="qissa.co.uk"`, `data-tilt`, `data-count="4.8"`), and stylesheet rule `.wpcf7 .hidden-fields-container { display: none; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.site-header> — `www-qissa-co-uk`)` (`www-qissa-co-uk`) adapts across `@media (prefers-reduced-motion: reduce)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:560px)`, `@media (max-width:820px)` with `cubic-bezier(.22,.61,.36,1)`, `cubic-bezier(.65,.05,.36,1)`, `cubic-bezier(0.22,1,0.36,1)` transitions and links `00 Home · 01 Our Story · 02 The Menu · Food Menu · Drinks Menu`.
2. **Hero Stage & Focal Lead (<section.hero> — `Qissa`)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `Qissa` and copy excerpt *"Celebrating the flavors of India with dishes inspired by differen"* over `#0a1230` canvas and `#f6f1e7` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#0a1230` background with `#f6f1e7` headline `Qissa`.
3. **Primary Showcase & Content Grid (<section.section> — `A word that means a tale.`)**:
   - DOM & Selectors: Landmark `<section class="section">` rendering section `A word that means a tale.` with copy *"Food is all about its story — the origin, the spices, the texture"*, asset references (`gtm.js`, `hero-poster.webp`, `favicon-96.png`, `favicon-32.png`), and grid rule `.wpcf7 form .wpcf7-response-output { margin: 2em 0.5em 1em; padding: 0.2em 1em; border: 2px solid 00a0d2; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.section> — `A word that means a tale.`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 22px`) on desktop and Single-column vertical stack at `390px` viewport width with `72px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.masterpieces> — `Crafted icons & signature plates.`)**:
   - DOM & Selectors: Landmark `<section class="section masterpieces">` framing `Crafted icons & signature plates.` and `Explore the menu, course by course.` (*"‘Qissa’ tells the extraordinary stories behind the foods we eat: "*) with `#23282d` surface cards, `#0c1533` accents, and `form.submitting .wpcf7-response-o... { display: none; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.masterpieces> — `Crafted icons & signature plates.`)` uses `100%`, `100px`, `50%`, `var(--radius)` radii, `#0c1533` highlights, and assets (gtm.js, hero-poster.webp, favicon-96.png).
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://www.qissa.co.uk/`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer">` anchoring `Indian Restaurant in Sevenoaks, ` footer links (`00 Home · 01 Our Story · 02 The Menu · Food Menu · Drinks Menu`), copy *"Qissa is a place of gathering, of celebrations, of business,"*, and `#1e2c57` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-footer> — `https://www.qissa.co.uk/`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `72px` lateral canvas padding with `22px` grid gap and attributes (data-u="contact", data-d="qissa.co.uk", data-tilt).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Celebrating the flavors of India with dishes inspired by different regions and cre..."*
- Copy Excerpt 2: *"Food is all about its story — the origin, the spices, the texture and the taste of..."*
- Copy Excerpt 3: *"‘Qissa’ tells the extraordinary stories behind the foods we eat: the finest Indian..."*
- Copy Excerpt 4: *"Qissa is a place of gathering, of celebrations, of business, and of pleasure. Let..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.22,.61,.36,1)`, `cubic-bezier(.65,.05,.36,1)`, `cubic-bezier(0.22,1,0.36,1)`
- **Extracted Stylesheet Rules (`www-qissa-co-uk`)**:
- `.wpcf7 .hidden-fields-container { display: none; }`
- `.wpcf7 form .wpcf7-response-output { margin: 2em 0.5em 1em; padding: 0.2em 1em; border: 2px solid 00a0d2; }`
- `form.submitting .wpcf7-response-o... { display: none; }`
- `.wpcf7 form.sent .wpcf7-response-... { border-color: 46b450; }`
- `cf7 form.aborted .wpcf7-response-... { border-color: dc3232; }`
- **Per-Selector Transition Rules**:
- **Selector `.btn`**: `transition: transform .5s var(--ease),box-shadow .5s var(--ease),backgroun...` extracted from `www-qissa-co-uk` stylesheet.
- **Selector `.btn svg`**: `transition: transform .5s var(--ease)` extracted from `www-qissa-co-uk` stylesheet.
- **Selector `.site-header`**: `transition: padding .5s var(--ease),background .5s var(--ease),backdrop-fi...` extracted from `www-qissa-co-uk` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,.61,.36,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.section>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `11788px` across 8 distinct viewport chapters using WebGL/Canvas.
- **Vertical Chapter Sequence**: Qissa (0%) -> A word that means a tale. (8%) -> Section @ 24% (24%) -> A feast worth gathering for. (39%) -> Beneath the blossoms. (62%) -> Section @ 78% (78%) -> Reserve a Table (94%) -> EXPLORE (100%).
- **Navigation Drawer / Menu State**: Replicate interactive menu toggle (`MENU`) with Escape-to-close keyboard handling.
- **Hover Micro-Interaction (`primary_cta`)**: Animate `transform, color, borderColor` with `0.5s, 0.5s, 0.4s, 0.4s cubic-bezier(0.22, 0.61, 0.36, 1), cubic-bezier(0.22, 0.61, 0.36, 1), ease, ease`.
- **Multi-Page Routes**: Scaffold internal routes `/journal/` (listing, direct), `/story/` (about, direct), `/contact/` (about, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-qissa-co-uk`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | Qissa | `1` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `8%` | A word that means a tale. | `1` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `2550px` | `24%` | Section @ 24% | `1` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `4250px` | `39%` | A feast worth gathering for. | `1` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `6800px` | `62%` | Beneath the blossoms. | `1` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `8500px` | `78%` | Section @ 78% | `1` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `10200px` | `94%` | Reserve a Table | `1` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `10842px` | `100%` | EXPLORE | `1` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | Qissa | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `5938px` | `50%` | Truck Drivers Lamb Curry | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `11877px` | `100%` | HOURS | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Interactive UI State Captures (`1440×900` WebP)
| State Type | Trigger / Observation | Visual Asset |
| :--- | :--- | :--- |
| `nav_menu` | Nav/Menu opened (`MENU`, diff `29.403`) | [state-nav.webp](assets/state-nav.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `listing` | `https://www.qissa.co.uk/journal/` | Journal | `2634px` | `direct` (`1690ms`) | [subpage-01-journal.webp](assets/subpage-01-journal.webp) |
| `2` | `about` | `https://www.qissa.co.uk/story/` | Our Story | `4585px` | `direct` (`649ms`) | [subpage-02-story.webp](assets/subpage-02-story.webp) |
| `3` | `about` | `https://www.qissa.co.uk/contact/` | Visit Us | `2952px` | `direct` (`1235ms`) | [subpage-03-contact.webp](assets/subpage-03-contact.webp) |

