---
title: "UI Prompt Blueprint: hole-money"
date: 2026-11-15
target: "hole-money"
status: analyzed
capture: specimen
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#e4e4e7` / `#afafb6`)"
---

# UI Design System & Master Generation Blueprint: hole-money

> **Money Hole** (https://hole.money) — Money Hole is a free personal finance manager for tracking income, expenses, accounts and budgets. Analytics, multi-currency support and...

![Desktop Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Money Hole** (`https://hole.money`). Money Hole is a free personal finance manager for tracking income, expenses, accounts and budgets. Analytics, multi-currency support and...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#e4e4e7` / `#afafb6`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#e4e4e7` (`var(--bg)` in `:root`) paired with `#18181b` primary typography and `#afafb6` accents.
  - **Extracted Typographic Hierarchy**: Pairs `IBM Plex Sans` for display copy (`Income sources`) with `IBM Plex Serif` and `IBM Plex Sans`.
  - **Calibrated Spatial Grid & Motion**: Combines `100vw` container bounds (`gap: 10px`, padding `7px`) with `cubic-bezier(.32,.72,0,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `100vw` extracted from `hole-money` stylesheet.
- **Canvas Lateral Padding & Spacing**: `7px` lateral canvas padding with `10px` grid gap.
- **Border Radius Scale**: `62px`, `1px`, `60px`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 100vw`, `gap: 10px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `7px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#e4e4e7` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#ffffff` | `var(--card)` in `:root` |
| **Elevated Surface / Card Substrate** | `#18181b` | `var(--primary)` in `:root` |
| **Interactive Accent / Highlight** | `#afafb6` | `var(--grab)` in `:root` |
| **Secondary / Muted Copy** | `#d7d7db` | `var(--divider)` in `:root` |
| **Structural Hairline Border** | `#797986` | `var(--ink2)` in `:root` |
| **Variable Token (`--module`)** | `#ffffff80` | `var(--module)` in `:root` |
| **Variable Token (`--glass`)** | `#ffffff73` | `var(--glass)` in `:root` |
| **Variable Token (`--bsm`)** | `#ffffff4d` | `var(--bsm)` in `:root` |
| **Variable Token (`--shadow-btn`)** | `#0000000a` | `var(--shadow-btn)` in `:root` |

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
- **Display Typography**: `IBM Plex Sans`.
- **Primary Body Stack**: `IBM Plex Serif`.
- **Technical / Metadata Stack**: `IBM Plex Sans`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `20px`, `24px`, `22px`, `9px`, `8px`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `20px`, `24px`, `22px`, `9px`, `8px`).
- **Body Copy**: rule `body` (`letter-spacing: -.1px`).
- **Metadata & Navigation Labels**: rule `small` (`font-weight: 500`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.32,.72,0,1)`, `cubic-bezier(.34,1.4,.64,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.splash`**: `transition: opacity .6s var(--ios)` extracted from `hole-money` stylesheet.
- **Selector `.splash .ico`**: `transition: opacity .7s var(--ios),transform .9s cubic-bezier(.34,1.4,.64,...` extracted from `hole-money` stylesheet.
- **Selector `.splash.out .ico`**: `transition: opacity .45s ease-in,transform .6s var(--ios),filter .45s` extracted from `hole-money` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.32,.72,0,1)`)**: Governs interactive state transitions across `<header.paused>` and `<section.sl>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Money Hole                                 │
│ ====================================================================== │
│ [ <header.paused>          | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.sl>                                         |   │
│ | H1: Income sources                                               |   │
│ | Substrate: #e4e4e7    | Ink: #18181b    | Accent: #afafb6        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.sl>              ) max-w: 100vw          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Accounts                     |  | Expenses                     | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 10px  ) | │
│ | [<header.paused>] -> [<section.sl>] -> [<section.sl>] |              │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.dframe>       ) | https://hole.money                 │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.paused> — `hole-money`)**:
   - Landmark `<header class="paused">` hosting `Money Hole` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-c="0"`, `data-m="0"`, `data-s="1"`, `data-v="incT"`), and stylesheet rule `.stage { position:relative;width:432px;height:871px }`.
2. **Hero Stage & Focal Lead (<section.sl> — `Income sources`)**:
   - Landmark `<section class="sl show">` presenting display lead `Income sources` and copy excerpt *"Spending by Category"* over `#e4e4e7` canvas and `#18181b` ink.
3. **Primary Showcase & Content Grid (<section.sl> — `Accounts`)**:
   - Landmark `<section class="sl">` rendering section `Accounts` with copy *"For example, Salary to Cash, ten thousand dollars"*, asset references (`fonts.googleapis.com`, `fonts.gstatic.com`, `css2`, `favicon.ico`), and grid rule `.device { position:absolute;left:0;top:0;width:432px;height:871px;transform-origin... }`.
4. **Interactive Detail & Feature Matrix (<section.sl> — `Expenses`)**:
   - Landmark `<section class="sl">` framing `Expenses` and `Expense category` (*"Manage Your Finance"*) with `#18181b` surface cards, `#afafb6` accents, and `.dcut { position:absolute;background:linear-gradient(817e73,c3beac);border-radiu... }`.
5. **Colophon & Global Directory Footer (<footer.dframe> — `https://hole.money`)**:
   - Landmark `<footer class="dframe">` anchoring `Money Hole` footer links (`Overview · Index · Archive · About · Contact`), copy *"– no intrusive ads or subscriptions"*, and `#797986` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: hole-money (Money Hole)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `hole-money` (**Money Hole** — `https://hole.money`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#e4e4e7` / `#afafb6`).
- **Identity & Domain Context**: Money Hole is a free personal finance manager for tracking income, expenses, accounts and budgets. Analytics, multi-currency support and...
- **Primary Substrate**: `#e4e4e7` (`var(--bg)` in `:root`), **Primary Ink**: `#18181b`, **Accent / Highlight**: `#afafb6`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#e4e4e7` (`var(--bg)` in `:root`) paired with `#18181b` primary typography and `#afafb6` accents.
  - **Extracted Typographic Hierarchy**: Pairs `IBM Plex Sans` for display copy (`Income sources`) with `IBM Plex Serif` and `IBM Plex Sans`.
  - **Calibrated Spatial Grid & Motion**: Combines `100vw` container bounds (`gap: 10px`, padding `7px`) with `cubic-bezier(.32,.72,0,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `hole-money` in your global stylesheet:

:root {
  /* Money Hole (hole-money) — Ground-Truth Extracted CSS Variables */
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
- **Primary Canvas Substrate**: `#e4e4e7` — grounded in `var(--bg)` in `:root`
- **Primary Typography Ink**: `#ffffff` — grounded in `var(--card)` in `:root`
- **Elevated Surface / Card Substrate**: `#18181b` — grounded in `var(--primary)` in `:root`
- **Interactive Accent / Highlight**: `#afafb6` — grounded in `var(--grab)` in `:root`
- **Secondary / Muted Copy**: `#d7d7db` — grounded in `var(--divider)` in `:root`
- **Structural Hairline Border**: `#797986` — grounded in `var(--ink2)` in `:root`
- **Variable Token (`--module`)**: `#ffffff80` — grounded in `var(--module)` in `:root`
- **Variable Token (`--glass`)**: `#ffffff73` — grounded in `var(--glass)` in `:root`
- **Variable Token (`--bsm`)**: `#ffffff4d` — grounded in `var(--bsm)` in `:root`
- **Variable Token (`--shadow-btn`)**: `#0000000a` — grounded in `var(--shadow-btn)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `100vw` extracted from `hole-money` stylesheet
- **Padding & Gutters**: `7px` lateral canvas padding with `10px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 100vw`, `gap: 10px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `7px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `62px`, `1px`, `60px`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `IBM Plex Sans`
- **Body Font Stack**: `IBM Plex Serif`
- **Monospace / Technical Font Stack**: `IBM Plex Sans`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `20px`, `24px`, `22px`, `9px`, `8px`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `20px`, `24px`, `22px`, `9px`, `8px`)
- **Body Copy Rule**: rule `body` (`letter-spacing: -.1px`)
- **Metadata & Index Rule**: rule `small` (`font-weight: 500`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `hole-money` (`Money Hole`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.paused> — `hole-money`)**:
   - DOM & Selectors: Landmark `<header class="paused">` hosting `Money Hole` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-c="0"`, `data-m="0"`, `data-s="1"`, `data-v="incT"`), and stylesheet rule `.stage { position:relative;width:432px;height:871px }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.paused> — `hole-money`)` (`hole-money`) adapts across `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(.32,.72,0,1)`, `cubic-bezier(.34,1.4,.64,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.sl> — `Income sources`)**:
   - DOM & Selectors: Landmark `<section class="sl show">` presenting display lead `Income sources` and copy excerpt *"Spending by Category"* over `#e4e4e7` canvas and `#18181b` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#e4e4e7` background with `#18181b` headline `Income sources`.
3. **Primary Showcase & Content Grid (<section.sl> — `Accounts`)**:
   - DOM & Selectors: Landmark `<section class="sl">` rendering section `Accounts` with copy *"For example, Salary to Cash, ten thousand dollars"*, asset references (`fonts.googleapis.com`, `fonts.gstatic.com`, `css2`, `favicon.ico`), and grid rule `.device { position:absolute;left:0;top:0;width:432px;height:871px;transform-origin... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.sl> — `Accounts`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 100vw`, `gap: 10px`) on desktop and Single-column vertical stack at `390px` viewport width with `7px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.sl> — `Expenses`)**:
   - DOM & Selectors: Landmark `<section class="sl">` framing `Expenses` and `Expense category` (*"Manage Your Finance"*) with `#18181b` surface cards, `#afafb6` accents, and `.dcut { position:absolute;background:linear-gradient(817e73,c3beac);border-radiu... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.sl> — `Expenses`)` uses `62px`, `1px`, `60px`, `2px` radii, `#afafb6` highlights, and assets (fonts.googleapis.com, fonts.gstatic.com, css2).
5. **Colophon & Global Directory Footer (<footer.dframe> — `https://hole.money`)**:
   - DOM & Selectors: Landmark `<footer class="dframe">` anchoring `Money Hole` footer links (`Overview · Index · Archive · About · Contact`), copy *"– no intrusive ads or subscriptions"*, and `#797986` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.dframe> — `https://hole.money`)` aligns to `100vw` extracted from `hole-money` stylesheet with `7px` lateral canvas padding with `10px` grid gap and attributes (data-c="0", data-m="0", data-s="1").

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
- **Extracted Easing Curve (`cubic-bezier(.32,.72,0,1)`)**: Governs interactive state transitions across `<header.paused>` and `<section.sl>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `hole-money`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
