---
title: "UI Prompt Blueprint: hole-money"
date: 2026-11-24
captured_at: 2026-11-24
target: "hole-money"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: wheel
desktop_keyframes: 8
subpages_crawled: 0
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#c3c3c3` / `#18181b`)"
---

# UI Design System & Master Generation Blueprint: hole-money

> **Money Hole** (https://hole.money) — Money Hole is a free personal finance manager for tracking income, expenses, accounts and budgets. Analytics, multi-currency support and...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x872)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Money Hole** (`https://hole.money`). Money Hole is a free personal finance manager for tracking income, expenses, accounts and budgets. Analytics, multi-currency support and...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#c3c3c3` / `#18181b`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#c3c3c3` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#1c1c1c` primary typography and `#18181b` accents.
  - **Grounded Typographic Hierarchy**: Pairs `IBM Plex Serif` for display copy (`Manage Your Finance Manage Your Fina`) with `IBM Plex Sans`.
  - **Calibrated Spatial Grid & Motion**: Combines `1385px` container bounds (`gap: 10px`, padding `7px`) with `cubic-bezier(.32,.72,0,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=0px` / doc `900px`), Mobile `390×872px` (`assets/mobile-journey.webp`, `1` keyframes).
- **Master Container Bounds**: `1385px` (measured widest bounded `<section>` landmark width on `1440px` desktop).
- **Canvas Lateral Padding & Spacing**: `7px` lateral canvas padding with `10px` grid gap.
- **Border Radius Scale**: `62px`, `1px`, `60px`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1385px`, `gap: 10px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `7px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#c3c3c3` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1c1c1c` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e4e4e7` | `var(--bg)` in `:root` |
| **Interactive Accent / Highlight** | `#18181b` | `var(--primary)` in `:root` |
| **Secondary / Muted Copy** | `#797986` | `var(--ink2)` in `:root` |
| **Structural Hairline Border** | `#d7d7db` | `var(--divider)` in `:root` |
| **Variable Token (`--module`)** | `#ffffff` | `var(--module)` in `:root` |
| **Variable Token (`--grab`)** | `#afafb6` | `var(--grab)` in `:root` |
| **Variable Token (`--shadow-btn`)** | `#000000` | `var(--shadow-btn)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ios` | `cubic-bezier(.32,.72,0,1)` | Motion / Timing Token |
| `--bg` | `#e4e4e7` | Canvas / Surface Token |
| `--module` | `#ffffff80` | Color / Atmospheric Token |
| `--card` | `#ffffff` | Color / Atmospheric Token |
| `--glass` | `#ffffff73` | Color / Atmospheric Token |
| `--bsm` | `#ffffff4d` | Color / Atmospheric Token |
| `--primary` | `#18181b` | Brand / Palette Token |
| `--grab` | `#afafb6` | Color / Atmospheric Token |
| `--divider` | `#d7d7db` | Color / Atmospheric Token |
| `--gstroke` | `#ffffff73` | Elevation / Border Token |
| `--shadow-btn` | `#0000000a` | Elevation / Border Token |
| `--icon-shadow` | `#0000000a` | Elevation / Border Token |
| `--ink` | `#18181b` | Typography Ink Token |
| `--ink2` | `#797986` | Typography Ink Token |
| `--inv` | `#ffffff` | Color / Atmospheric Token |
| `--ph` | `#afafb6` | Color / Atmospheric Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `IBM Plex Serif`.
- **Primary Body Stack**: `IBM Plex Sans`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 120px`, `line-height: 130px`, `font-weight: 700`, `letter-spacing: -0.1px`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 60px`, `line-height: 70px`, `font-weight: 700`, `letter-spacing: -0.1px`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`, `letter-spacing: -0.1px`); rule `body` (`letter-spacing: -.1px`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`, `letter-spacing: -0.1px`); rule `small` (`font-weight: 500`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.32,.72,0,1)`, `cubic-bezier(.34,1.4,.64,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.splash`**: `transition: opacity .6s var(--ios)` extracted from `hole-money` stylesheet.
- **Selector `.splash .ico`**: `transition: opacity .7s var(--ios),transform .9s cubic-bezier(.34,1.4,.64,...` extracted from `hole-money` stylesheet.
- **Selector `.splash.out .ico`**: `transition: opacity .45s ease-in,transform .6s var(--ios),filter .45s` extracted from `hole-money` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.32,.72,0,1)`)**: Governs interactive state transitions across `<header.stage>` and `<section.sl:nth(2)>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `wheel` (max document height `900px`, deepest scrollY reached `0px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `WebGL/Canvas`.
- **Hover Physics (`primary_cta` · `Record Income`)**: Computed transition `0s` / `ease` (no static color/transform shift captured at rest).
- **Hover Physics (`first_card` · `Income $7,326 ▲ $545.85 · 4.25% E...`)**: Computed transition `0s` / `ease` (no static color/transform shift captured at rest).

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Money Hole                                 │
│ ====================================================================== │
│ [ <header.stage> (1400x20px)          | Overview · Index · Archive · ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.sl> (w=1440px)                                | │
│ | H1: Manage Your Finance Manage Your Finance                        | │
│ | Substrate: #c3c3c3 | Ink: #1c1c1c | Accent: #18181b                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.sl:nth(2)>) max-w: 1385px                  | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Spending by Category         |  | For example, Salary to Cash, | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.sl:nth(3)>) — Manage Your Finance          | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.dcut>       ) | https://hole.money                   │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 10px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.stage>          ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.sl>) — 390px Vertical Lead                    | │
│ | H1: Manage Your Finance Manage Your Finance                        | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.sl:nth(2)>) — 1-Col Stack                 | │
│ | [ Item 1: Spending by Category                                   ] | │
│ | [ Item 2: For example, Salary to Cash, ten thousand dollar       ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.sl:nth(3)>) — 1-Col (Manage Your Financ)    | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.dcut>       ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.stage> — `hole-money`)**:
   - Landmark `<header class="stage">` (`1400x20px`) hosting `Money Hole` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-c="0"`, `data-m="0"`, `data-s="1"`, `data-v="incT"`), and stylesheet rule `.stage { position:relative;width:432px;height:871px }`.
2. **Hero Stage & Focal Lead (<section.sl> — `Manage Your Finance Manage Your Fi`)**:
   - Landmark `<section class="sl">` presenting display lead `Manage Your Finance Manage Your Finance` and copy excerpt *"Spending by Category"* over `#c3c3c3` canvas and `#1c1c1c` ink.
3. **Primary Showcase & Content Grid (<section.sl:nth(2)> — `Spending by Category`)**:
   - Landmark `<section class="sl">` rendering section `Spending by Category` with copy *"For example, Salary to Cash, ten thousand dollars"*, asset references (`fonts.googleapis.com`, `fonts.gstatic.com`, `css2`, `favicon.ico`), and grid rule `.device { position:absolute;left:0;top:0;width:432px;height:871px;transform-origin... }`.
4. **Interactive Detail & Feature Matrix (<section.sl:nth(3)> — `For example, Salary to Cash, ten t`)**:
   - Landmark `<section class="sl">` framing `For example, Salary to Cash, ten thousand dollar` and `Manage Your Finance` (*"Manage Your Finance"*) with `#e4e4e7` surface cards, `#18181b` accents, and `.dcut { position:absolute;background:linear-gradient(817e73,c3beac);border-radiu... }`.
5. **Colophon & Global Directory Footer (<footer.dcut> — `https://hole.money`)**:
   - Landmark `<footer class="dcut">` anchoring `Money Hole` footer links (`Overview · Index · Archive · About · Contact`), copy *"– no intrusive ads or subscriptions"*, and `#d7d7db` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `Hero` · sticky/fixed elements: `1`
- **Step 02** (`y=0px`, `8%`): Active landmark `Simple and native interface` · sticky/fixed elements: `1`
- **Step 03** (`y=0px`, `17%`): Active landmark `Simple and native interface` · sticky/fixed elements: `1`
- **Step 04** (`y=0px`, `25%`): Active landmark `Drag and record` · sticky/fixed elements: `1`
- **Step 05** (`y=0px`, `33%`): Active landmark `Drag and record` · sticky/fixed elements: `1`
- **Step 06** (`y=0px`, `42%`): Active landmark `Drag and record` · sticky/fixed elements: `1`
- **Step 07** (`y=0px`, `50%`): Active landmark `Dictate and record` · sticky/fixed elements: `1`
- **Step 08** (`y=0px`, `58%`): Active landmark `Dictate and record` · sticky/fixed elements: `1`

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: hole-money (Money Hole)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `hole-money` (**Money Hole** — `https://hole.money`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#c3c3c3` / `#18181b`).
- **Identity & Domain Context**: Money Hole is a free personal finance manager for tracking income, expenses, accounts and budgets. Analytics, multi-currency support and...
- **Primary Substrate**: `#c3c3c3` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#1c1c1c`, **Accent / Highlight**: `#18181b`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#c3c3c3` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#1c1c1c` primary typography and `#18181b` accents.
  - **Grounded Typographic Hierarchy**: Pairs `IBM Plex Serif` for display copy (`Manage Your Finance Manage Your Fina`) with `IBM Plex Sans`.
  - **Calibrated Spatial Grid & Motion**: Combines `1385px` container bounds (`gap: 10px`, padding `7px`) with `cubic-bezier(.32,.72,0,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `hole-money` in your global stylesheet:

:root {
  /* Money Hole (hole-money) — Live-Grounded CSS Variables */
  --ios: cubic-bezier(.32,.72,0,1); /* Motion / Timing Token (hole-money) */
  --bg: #e4e4e7; /* Canvas / Surface Token (hole-money) */
  --module: #ffffff80; /* Color / Atmospheric Token (hole-money) */
  --card: #ffffff; /* Color / Atmospheric Token (hole-money) */
  --glass: #ffffff73; /* Color / Atmospheric Token (hole-money) */
  --bsm: #ffffff4d; /* Color / Atmospheric Token (hole-money) */
  --primary: #18181b; /* Brand / Palette Token (hole-money) */
  --grab: #afafb6; /* Color / Atmospheric Token (hole-money) */
  --divider: #d7d7db; /* Color / Atmospheric Token (hole-money) */
  --gstroke: #ffffff73; /* Elevation / Border Token (hole-money) */
  --shadow-btn: #0000000a; /* Elevation / Border Token (hole-money) */
  --icon-shadow: #0000000a; /* Elevation / Border Token (hole-money) */
  --ink: #18181b; /* Typography Ink Token (hole-money) */
  --ink2: #797986; /* Typography Ink Token (hole-money) */
  --inv: #ffffff; /* Color / Atmospheric Token (hole-money) */
  --ph: #afafb6; /* Color / Atmospheric Token (hole-money) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#c3c3c3` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#1c1c1c` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#e4e4e7` — grounded in `var(--bg)` in `:root`
- **Interactive Accent / Highlight**: `#18181b` — grounded in `var(--primary)` in `:root`
- **Secondary / Muted Copy**: `#797986` — grounded in `var(--ink2)` in `:root`
- **Structural Hairline Border**: `#d7d7db` — grounded in `var(--divider)` in `:root`
- **Variable Token (`--module`)**: `#ffffff` — grounded in `var(--module)` in `:root`
- **Variable Token (`--grab`)**: `#afafb6` — grounded in `var(--grab)` in `:root`
- **Variable Token (`--shadow-btn`)**: `#000000` — grounded in `var(--shadow-btn)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×872px` (full-page live capture (872px), `390px` standard mobile width).
- **Container Max-Width**: `1385px` (measured widest bounded `<section>` landmark width on `1440px` desktop)
- **Padding & Gutters**: `7px` lateral canvas padding with `10px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1385px`, `gap: 10px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `7px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `62px`, `1px`, `60px`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `IBM Plex Serif`
- **Body Font Stack**: `IBM Plex Sans`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 120px`, `line-height: 130px`, `font-weight: 700`, `letter-spacing: -0.1px`)
- **H2 Section Rule**: live computed `h2` (`font-size: 60px`, `line-height: 70px`, `font-weight: 700`, `letter-spacing: -0.1px`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`, `letter-spacing: -0.1px`); rule `body` (`letter-spacing: -.1px`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`, `letter-spacing: -0.1px`); rule `small` (`font-weight: 500`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `hole-money` (`Money Hole`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.stage> — `hole-money`)**:
   - DOM & Selectors: Landmark `<header class="stage">` (`1400x20px`) hosting `Money Hole` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-c="0"`, `data-m="0"`, `data-s="1"`, `data-v="incT"`), and stylesheet rule `.stage { position:relative;width:432px;height:871px }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.stage> — `hole-money`)` (`hole-money`) adapts across `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(.32,.72,0,1)`, `cubic-bezier(.34,1.4,.64,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.sl> — `Manage Your Finance Manage Your Fi`)**:
   - DOM & Selectors: Landmark `<section class="sl">` presenting display lead `Manage Your Finance Manage Your Finance` and copy excerpt *"Spending by Category"* over `#c3c3c3` canvas and `#1c1c1c` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×872px` mobile) sets `#c3c3c3` background with `#1c1c1c` headline `Manage Your Finance Manage Your Finance`.
3. **Primary Showcase & Content Grid (<section.sl:nth(2)> — `Spending by Category`)**:
   - DOM & Selectors: Landmark `<section class="sl">` rendering section `Spending by Category` with copy *"For example, Salary to Cash, ten thousand dollars"*, asset references (`fonts.googleapis.com`, `fonts.gstatic.com`, `css2`, `favicon.ico`), and grid rule `.device { position:absolute;left:0;top:0;width:432px;height:871px;transform-origin... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.sl:nth(2)> — `Spending by Category`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1385px`, `gap: 10px`) on desktop and Single-column vertical stack at `390px` viewport width with `7px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.sl:nth(3)> — `For example, Salary to Cash, ten t`)**:
   - DOM & Selectors: Landmark `<section class="sl">` framing `For example, Salary to Cash, ten thousand dollar` and `Manage Your Finance` (*"Manage Your Finance"*) with `#e4e4e7` surface cards, `#18181b` accents, and `.dcut { position:absolute;background:linear-gradient(817e73,c3beac);border-radiu... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.sl:nth(3)> — `For example, Salary to Cash, ten t`)` uses `62px`, `1px`, `60px`, `2px` radii, `#18181b` highlights, and assets (fonts.googleapis.com, fonts.gstatic.com, css2).
5. **Colophon & Global Directory Footer (<footer.dcut> — `https://hole.money`)**:
   - DOM & Selectors: Landmark `<footer class="dcut">` anchoring `Money Hole` footer links (`Overview · Index · Archive · About · Contact`), copy *"– no intrusive ads or subscriptions"*, and `#d7d7db` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.dcut> — `https://hole.money`)` aligns to `1385px` (measured widest bounded `<section>` landmark width on `1440px` desktop) with `7px` lateral canvas padding with `10px` grid gap and attributes (data-c="0", data-m="0", data-s="1").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Spending by Category"*
- Copy Excerpt 2: *"For example, Salary to Cash, ten thousand dollars"*
- Copy Excerpt 3: *"Manage Your Finance"*
- Copy Excerpt 4: *"– no intrusive ads or subscriptions"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.32,.72,0,1)`, `cubic-bezier(.34,1.4,.64,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`hole-money`)**:
- `.stage { position:relative;width:432px;height:871px }`
- `.device { position:absolute;left:0;top:0;width:432px;height:871px;transform-origin... }`
- `.dcut { position:absolute;background:linear-gradient(817e73,c3beac);border-radiu... }`
- `.dscreen { position:absolute;left:7px;top:4px;width:418px;height:863px;border-radiu... }`
- `.dbtn.r { border-radius:0 2px 2px 0;background:linear-gradient(270deg,8a867c,f0ece... }`
- **Per-Selector Transition Rules**:
- **Selector `.splash`**: `transition: opacity .6s var(--ios)` extracted from `hole-money` stylesheet.
- **Selector `.splash .ico`**: `transition: opacity .7s var(--ios),transform .9s cubic-bezier(.34,1.4,.64,...` extracted from `hole-money` stylesheet.
- **Selector `.splash.out .ico`**: `transition: opacity .45s ease-in,transform .6s var(--ios),filter .45s` extracted from `hole-money` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.32,.72,0,1)`)**: Governs interactive state transitions across `<header.stage>` and `<section.sl:nth(2)>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `wheel` vertical progression up to `900px` across 8 distinct viewport chapters using WebGL/Canvas.
- **Vertical Chapter Sequence**: Hero (0%) -> Simple and native interface (8%) -> Simple and native interface (17%) -> Drag and record (25%) -> Drag and record (33%) -> Drag and record (42%) -> Dictate and record (50%) -> Dictate and record (58%).

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `hole-money`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | Hero | `1` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `0px` | `8%` | Simple and native interface | `1` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `0px` | `17%` | Simple and native interface | `1` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `0px` | `25%` | Drag and record | `1` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `0px` | `33%` | Drag and record | `1` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `0px` | `42%` | Drag and record | `1` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `0px` | `50%` | Dictate and record | `1` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `0px` | `58%` | Dictate and record | `1` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | Manage Your Finance | [mobile-step-01.webp](assets/mobile-step-01.webp) |

