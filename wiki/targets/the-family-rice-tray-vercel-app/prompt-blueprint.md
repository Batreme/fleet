---
title: "UI Prompt Blueprint: the-family-rice-tray-vercel-app"
date: 2026-11-15
target: "[[overview|the-family-rice-tray-vercel-app]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#3f040c` canvas, `#e3a94a` ink, `#8b0c1c` accent)"
---

# UI Design System & Master Generation Blueprint: the-family-rice-tray-vercel-app

> **Mâm Cơm — the Vietnamese family rice tray** (https://the-family-rice-tray.vercel.app) — A love letter to mâm cơm, the round tray of shared dishes at the centre of every Vietnamese home — laid out on the face of a Đông Sơn bro...

![Desktop Viewport Capture (1440x10547)](file:///root/projects/fleet/wiki/targets/the-family-rice-tray-vercel-app/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Mâm Cơm — the Vietnamese family rice tray** (`https://the-family-rice-tray.vercel.app`). A love letter to mâm cơm, the round tray of shared dishes at the centre of every Vietnamese home — laid out on the face of a Đông Sơn bro...
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#3f040c` canvas, `#e3a94a` ink, `#8b0c1c` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#3f040c` (`var(--red-900)` in `:root`) paired with `#e3a94a` primary typography and `#8b0c1c` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Be Vietnam Pro` for display copy (`Mâm Cơm The family rice tray`) with `Big Shoulders Display` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `560px` container bounds (`gap: 0.9rem`, padding `0.85rem`) with `cubic-bezier(0.22,0.61,0.36,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/the-family-rice-tray-vercel-app/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×10547px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `560px` extracted from `the-family-rice-tray-vercel-app` stylesheet.
- **Canvas Lateral Padding & Spacing**: `0.85rem` lateral canvas padding with `0.9rem` grid gap.
- **Border Radius Scale**: `4px`, `2px`, `999px`, `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 560px`, `gap: 0.9rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `0.85rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width: 560px)`, `@media (prefers-reduced-motion: reduce)`, `@media (max-width: 720px)`, `@media (min-width: 561px) and (max-width: 959px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#3f040c` | `var(--red-900)` in `:root` |
| **Primary Typography Ink** | `#5e0712` | `var(--red-800)` in `:root` |
| **Elevated Surface / Card Substrate** | `#7a0a18` | `var(--red-700)` in `:root` |
| **Interactive Accent / Highlight** | `#8b0c1c` | `var(--red-600)` in `:root` |
| **Secondary / Muted Copy** | `#a8121f` | `var(--red-500)` in `:root` |
| **Structural Hairline Border** | `#e3a94a` | `var(--gold-400)` in `:root` |
| **Variable Token (`--gold-300`)** | `#f0be6b` | `var(--gold-300)` in `:root` |
| **Variable Token (`--gold-200`)** | `#f7d9a0` | `var(--gold-200)` in `:root` |
| **Variable Token (`--jade`)** | `#2e6b58` | `var(--jade)` in `:root` |
| **Variable Token (`--jade-light`)** | `#7fb8a2` | `var(--jade-light)` in `:root` |
| **Variable Token (`--cream`)** | `#f7efe0` | `var(--cream)` in `:root` |
| **Variable Token (`--cream-dim`)** | `#dccdb4` | `var(--cream-dim)` in `:root` |
| **Variable Token (`--ink`)** | `#1a0509` | `var(--ink)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--red-900` | `#3f040c` | Color / Atmospheric Token |
| `--red-800` | `#5e0712` | Color / Atmospheric Token |
| `--red-700` | `#7a0a18` | Color / Atmospheric Token |
| `--red-600` | `#8b0c1c` | Color / Atmospheric Token |
| `--red-500` | `#a8121f` | Color / Atmospheric Token |
| `--gold-400` | `#e3a94a` | Color / Atmospheric Token |
| `--gold-300` | `#f0be6b` | Color / Atmospheric Token |
| `--gold-200` | `#f7d9a0` | Color / Atmospheric Token |
| `--jade` | `#2e6b58` | Color / Atmospheric Token |
| `--jade-light` | `#7fb8a2` | Canvas / Surface Token |
| `--cream` | `#f7efe0` | Color / Atmospheric Token |
| `--cream-dim` | `#dccdb4` | Color / Atmospheric Token |
| `--cream-faint` | `rgba(247, 239, 224, 0.62)` | Color / Atmospheric Token |
| `--ink` | `#1a0509` | Typography Ink Token |
| `--font-display` | `"Big Shoulders Display", "Arial Narrow", system-ui, sans-serif` | Typography / Scale Token |
| `--font-body` | `"Be Vietnam Pro", system-ui, -apple-system, "Segoe UI", sans-serif` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Be Vietnam Pro`.
- **Primary Body Stack**: `Big Shoulders Display`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--font-display: "Big Shoulders Display", "Arial Narrow", system-ui, sans-serif`; rule `h1` (`font-size: var(--t-hero)`, `line-height: 0.82`, `letter-spacing: -0.015em`, `font-weight: 900`).
- **Section Heading (`H2`)**: CSS variables `--t-h2: clamp(2.4rem, 6vw, 4.6rem)`; rule `h2` (`font-size: var(--t-h2)`, `font-weight: 900`).
- **Body Copy**: CSS variables `--font-body: "Be Vietnam Pro", system-ui, -apple-system, "Segoe UI", sans-serif`, `--t-body: clamp(1rem, 0.55vw + 0.9rem, 1.16rem)`; rule `body` (`font-size: var(--t-body)`, `line-height: 1.72`, `font-weight: 300`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--t-body)`, `0.76rem`, `var(--t-lede)`, `0.62em`, `0.4em`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.22,0.61,0.36,1)`, `cubic-bezier(0.34,0.02,0.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.skip-link`**: `transition: translate 0.18s var(--ease)` extracted from `the-family-rice-tray-vercel-app` stylesheet.
- **Selector `.wl`**: `transition: color 0.18s var(--ease), border-color 0.18s var(--ease)` extracted from `the-family-rice-tray-vercel-app` stylesheet.
- **Selector `.btn`**: `transition: background-color 0.2s var(--ease), color 0.2s var(--ease), bor...` extracted from `the-family-rice-tray-vercel-app` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.22,0.61,0.36,1)`)**: Governs interactive state transitions across `<header.masthead>` and `<section.section>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Mâm Cơm — the Vietnamese family rice tray  │
│ ====================================================================== │
│ [ <header.masthead>        | The Tray · The Legend · The Recipe · N ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero>                                       |   │
│ | H1: Mâm Cơm The family rice tray                                 |   │
│ | Substrate: #3f040c    | Ink: #e3a94a    | Accent: #8b0c1c        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.section>         ) max-w: 560px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Three thousand years on a ci |  | Cơm Trắng                    | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 0.9rem) | │
│ | [<header.masthead>] -> [<section.hero>] -> [<section.section>] |     │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>       ) | https://the-family-rice-tray.verce │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.masthead> — `the-family-rice-tray-vercel-app`)**:
   - Landmark `<header class="masthead">` hosting `Mâm Cơm — the Vietnamese family rice` navigation (`The Tray · The Legend · The Recipe · Nếp Nhà`), DOM attributes (`data-audio-toggle`, `data-audio`, `data-jump="tab-com"`, `data-jump="tab-thitkho"`), and stylesheet rule `after { box-sizing: border-box; }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Mâm Cơm The family rice tray`)**:
   - Landmark `<section class="hero">` presenting display lead `Mâm Cơm The family rice tray` and copy excerpt *"A love letter to a regional dish Việt Nam · Đông Nam Á"* over `#3f040c` canvas and `#e3a94a` ink.
3. **Primary Showcase & Content Grid (<section.section> — `Three thousand years on a circle`)**:
   - Landmark `<section class="section tray-section">` rendering section `Three thousand years on a circle` with copy *"Việt Nam · Đông Nam Á"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `html { -webkit-text-size-adjust: 100%; }`.
4. **Interactive Detail & Feature Matrix (<section.feast> — `Cơm Trắng`)**:
   - Landmark `<section class="feast">` framing `Cơm Trắng` and `Thịt Kho Trứng` (*"mâm cơm · /məm kəːm/ · “the tray of rice”"*) with `#7a0a18` surface cards, `#8b0c1c` accents, and `img { max-width: 100%; height: auto; display: block; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://the-family-rice-tray.vercel.app`)**:
   - Landmark `<footer class="footer">` anchoring `Mâm Cơm — the Vietnamese family ` footer links (`The Tray · The Legend · The Recipe · Nếp Nhà`), copy *"Vietnamese has no word for entrée . There is only cơm — rice"*, and `#e3a94a` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: the-family-rice-tray-vercel-app (Mâm Cơm — the Vietnamese family rice tray)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `the-family-rice-tray-vercel-app` (**Mâm Cơm — the Vietnamese family rice tray** — `https://the-family-rice-tray.vercel.app`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#3f040c` canvas, `#e3a94a` ink, `#8b0c1c` accent).
- **Identity & Domain Context**: A love letter to mâm cơm, the round tray of shared dishes at the centre of every Vietnamese home — laid out on the face of a Đông Sơn bro...
- **Primary Substrate**: `#3f040c` (`var(--red-900)` in `:root`), **Primary Ink**: `#e3a94a`, **Accent / Highlight**: `#8b0c1c`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#3f040c` (`var(--red-900)` in `:root`) paired with `#e3a94a` primary typography and `#8b0c1c` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Be Vietnam Pro` for display copy (`Mâm Cơm The family rice tray`) with `Big Shoulders Display` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `560px` container bounds (`gap: 0.9rem`, padding `0.85rem`) with `cubic-bezier(0.22,0.61,0.36,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `the-family-rice-tray-vercel-app` in your global stylesheet:

:root {
  /* Mâm Cơm — the Vietnamese family rice tray (the-family-rice-tray-vercel-app) — Ground-Truth Extracted CSS Variables */
  --red-900: #3f040c; /* Color / Atmospheric Token (the-family-rice-tray-vercel-app) */
  --red-800: #5e0712; /* Color / Atmospheric Token (the-family-rice-tray-vercel-app) */
  --red-700: #7a0a18; /* Color / Atmospheric Token (the-family-rice-tray-vercel-app) */
  --red-600: #8b0c1c; /* Color / Atmospheric Token (the-family-rice-tray-vercel-app) */
  --red-500: #a8121f; /* Color / Atmospheric Token (the-family-rice-tray-vercel-app) */
  --gold-400: #e3a94a; /* Color / Atmospheric Token (the-family-rice-tray-vercel-app) */
  --gold-300: #f0be6b; /* Color / Atmospheric Token (the-family-rice-tray-vercel-app) */
  --gold-200: #f7d9a0; /* Color / Atmospheric Token (the-family-rice-tray-vercel-app) */
  --jade: #2e6b58; /* Color / Atmospheric Token (the-family-rice-tray-vercel-app) */
  --jade-light: #7fb8a2; /* Canvas / Surface Token (the-family-rice-tray-vercel-app) */
  --cream: #f7efe0; /* Color / Atmospheric Token (the-family-rice-tray-vercel-app) */
  --cream-dim: #dccdb4; /* Color / Atmospheric Token (the-family-rice-tray-vercel-app) */
  --cream-faint: rgba(247, 239, 224, 0.62); /* Color / Atmospheric Token (the-family-rice-tray-vercel-app) */
  --ink: #1a0509; /* Typography Ink Token (the-family-rice-tray-vercel-app) */
  --font-display: "Big Shoulders Display", "Arial Narrow", system-ui, sans-serif; /* Typography / Scale Token (the-family-rice-tray-vercel-app) */
  --font-body: "Be Vietnam Pro", system-ui, -apple-system, "Segoe UI", sans-serif; /* Typography / Scale Token (the-family-rice-tray-vercel-app) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#3f040c` — grounded in `var(--red-900)` in `:root`
- **Primary Typography Ink**: `#5e0712` — grounded in `var(--red-800)` in `:root`
- **Elevated Surface / Card Substrate**: `#7a0a18` — grounded in `var(--red-700)` in `:root`
- **Interactive Accent / Highlight**: `#8b0c1c` — grounded in `var(--red-600)` in `:root`
- **Secondary / Muted Copy**: `#a8121f` — grounded in `var(--red-500)` in `:root`
- **Structural Hairline Border**: `#e3a94a` — grounded in `var(--gold-400)` in `:root`
- **Variable Token (`--gold-300`)**: `#f0be6b` — grounded in `var(--gold-300)` in `:root`
- **Variable Token (`--gold-200`)**: `#f7d9a0` — grounded in `var(--gold-200)` in `:root`
- **Variable Token (`--jade`)**: `#2e6b58` — grounded in `var(--jade)` in `:root`
- **Variable Token (`--jade-light`)**: `#7fb8a2` — grounded in `var(--jade-light)` in `:root`
- **Variable Token (`--cream`)**: `#f7efe0` — grounded in `var(--cream)` in `:root`
- **Variable Token (`--cream-dim`)**: `#dccdb4` — grounded in `var(--cream-dim)` in `:root`
- **Variable Token (`--ink`)**: `#1a0509` — grounded in `var(--ink)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×10547px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `560px` extracted from `the-family-rice-tray-vercel-app` stylesheet
- **Padding & Gutters**: `0.85rem` lateral canvas padding with `0.9rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 560px`, `gap: 0.9rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `0.85rem` horizontal padding
- **Media Queries**: `@media (max-width: 560px)`, `@media (prefers-reduced-motion: reduce)`, `@media (max-width: 720px)`, `@media (min-width: 561px) and (max-width: 959px)`
- **Corner Radii**: `4px`, `2px`, `999px`, `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Be Vietnam Pro`
- **Body Font Stack**: `Big Shoulders Display`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--font-display: "Big Shoulders Display", "Arial Narrow", system-ui, sans-serif`; rule `h1` (`font-size: var(--t-hero)`, `line-height: 0.82`, `letter-spacing: -0.015em`, `font-weight: 900`)
- **H2 Section Rule**: CSS variables `--t-h2: clamp(2.4rem, 6vw, 4.6rem)`; rule `h2` (`font-size: var(--t-h2)`, `font-weight: 900`)
- **Body Copy Rule**: CSS variables `--font-body: "Be Vietnam Pro", system-ui, -apple-system, "Segoe UI", sans-serif`, `--t-body: clamp(1rem, 0.55vw + 0.9rem, 1.16rem)`; rule `body` (`font-size: var(--t-body)`, `line-height: 1.72`, `font-weight: 300`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--t-body)`, `0.76rem`, `var(--t-lede)`, `0.62em`, `0.4em`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `the-family-rice-tray-vercel-app` (`Mâm Cơm — the Vietnamese family rice tray`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.masthead> — `the-family-rice-tray-vercel-app`)**:
   - DOM & Selectors: Landmark `<header class="masthead">` hosting `Mâm Cơm — the Vietnamese family rice` navigation (`The Tray · The Legend · The Recipe · Nếp Nhà`), DOM attributes (`data-audio-toggle`, `data-audio`, `data-jump="tab-com"`, `data-jump="tab-thitkho"`), and stylesheet rule `after { box-sizing: border-box; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.masthead> — `the-family-rice-tray-vercel-app`)` (`the-family-rice-tray-vercel-app`) adapts across `@media (max-width: 560px)`, `@media (prefers-reduced-motion: reduce)`, `@media (max-width: 720px)`, `@media (min-width: 561px) and (max-width: 959px)` with `cubic-bezier(0.22,0.61,0.36,1)`, `cubic-bezier(0.34,0.02,0.2,1)` transitions and links `The Tray · The Legend · The Recipe · Nếp Nhà`.
2. **Hero Stage & Focal Lead (<section.hero> — `Mâm Cơm The family rice tray`)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `Mâm Cơm The family rice tray` and copy excerpt *"A love letter to a regional dish Việt Nam · Đông Nam Á"* over `#3f040c` canvas and `#e3a94a` ink.
   - Responsive Contract: Hero stage (`1440×10547px` desktop / `390×2400px` mobile) sets `#3f040c` background with `#e3a94a` headline `Mâm Cơm The family rice tray`.
3. **Primary Showcase & Content Grid (<section.section> — `Three thousand years on a circle`)**:
   - DOM & Selectors: Landmark `<section class="section tray-section">` rendering section `Three thousand years on a circle` with copy *"Việt Nam · Đông Nam Á"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `html { -webkit-text-size-adjust: 100%; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.section> — `Three thousand years on a circle`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 560px`, `gap: 0.9rem`) on desktop and Single-column vertical stack at `390px` viewport width with `0.85rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.feast> — `Cơm Trắng`)**:
   - DOM & Selectors: Landmark `<section class="feast">` framing `Cơm Trắng` and `Thịt Kho Trứng` (*"mâm cơm · /məm kəːm/ · “the tray of rice”"*) with `#7a0a18` surface cards, `#8b0c1c` accents, and `img { max-width: 100%; height: auto; display: block; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.feast> — `Cơm Trắng`)` uses `4px`, `2px`, `999px`, `50%` radii, `#8b0c1c` highlights, and assets (favicon.ico, favicon.svg, apple-touch-icon.png).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://the-family-rice-tray.vercel.app`)**:
   - DOM & Selectors: Landmark `<footer class="footer">` anchoring `Mâm Cơm — the Vietnamese family ` footer links (`The Tray · The Legend · The Recipe · Nếp Nhà`), copy *"Vietnamese has no word for entrée . There is only cơm — rice"*, and `#e3a94a` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://the-family-rice-tray.vercel.app`)` aligns to `560px` extracted from `the-family-rice-tray-vercel-app` stylesheet with `0.85rem` lateral canvas padding with `0.9rem` grid gap and attributes (data-audio-toggle, data-audio, data-jump="tab-com").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"A love letter to a regional dish Việt Nam · Đông Nam Á"*
- Copy Excerpt 2: *"Việt Nam · Đông Nam Á"*
- Copy Excerpt 3: *"mâm cơm · /məm kəːm/ · “the tray of rice”"*
- Copy Excerpt 4: *"Vietnamese has no word for entrée . There is only cơm — rice — and everything laid..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.22,0.61,0.36,1)`, `cubic-bezier(0.34,0.02,0.2,1)`
- **Extracted Stylesheet Rules (`the-family-rice-tray-vercel-app`)**:
- `after { box-sizing: border-box; }`
- `html { -webkit-text-size-adjust: 100%; }`
- `img { max-width: 100%; height: auto; display: block; }`
- `h4 { margin: 0; line-height: 1.02; font-weight: 800; letter-spacing: -0.01em; }`
- `p:last-child { margin-bottom: 0; }`
- **Per-Selector Transition Rules**:
- **Selector `.skip-link`**: `transition: translate 0.18s var(--ease)` extracted from `the-family-rice-tray-vercel-app` stylesheet.
- **Selector `.wl`**: `transition: color 0.18s var(--ease), border-color 0.18s var(--ease)` extracted from `the-family-rice-tray-vercel-app` stylesheet.
- **Selector `.btn`**: `transition: background-color 0.2s var(--ease), color 0.2s var(--ease), bor...` extracted from `the-family-rice-tray-vercel-app` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.22,0.61,0.36,1)`)**: Governs interactive state transitions across `<header.masthead>` and `<section.section>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `the-family-rice-tray-vercel-app`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
