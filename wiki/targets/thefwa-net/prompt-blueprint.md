---
title: "UI Prompt Blueprint: thefwa-net"
date: 2026-11-15
target: "[[overview|thefwa-net]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#7E7E7E` ink, `#303030` accent)"
---

# UI Design System & Master Generation Blueprint: thefwa-net

> **FWA Wire — winners' newswire** (https://thefwa.net/) — News from FWA winners — hires, launches, talks and work in progress. One post per person per day, newest first. No algorithm, no ranking.

![Desktop Viewport Capture (1440x4035)](file:///root/projects/fleet/wiki/targets/thefwa-net/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **FWA Wire — winners' newswire** (`https://thefwa.net/`). News from FWA winners — hires, launches, talks and work in progress. One post per person per day, newest first. No algorithm, no ranking.
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#7E7E7E` ink, `#303030` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000000` (`var(--void)` in `:root`) paired with `#7E7E7E` primary typography and `#303030` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Silkscreen` for display copy (`FWA Certified`) with `B4B4B4` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 10px`, padding `8px`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/thefwa-net/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×4035px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `940px` extracted from `thefwa-net` stylesheet.
- **Canvas Lateral Padding & Spacing**: `8px` lateral canvas padding with `10px` grid gap.
- **Border Radius Scale**: `0px` (sharp unrounded corners).

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 10px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `8px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:760px)`, `@media (max-width:520px)`, `@media (max-width:519px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | `var(--void)` in `:root` |
| **Primary Typography Ink** | `#0C0C0C` | `var(--panel)` in `:root` |
| **Elevated Surface / Card Substrate** | `#151515` | `var(--inset)` in `:root` |
| **Interactive Accent / Highlight** | `#303030` | `var(--line)` in `:root` |
| **Secondary / Muted Copy** | `#4A4A4A` | `var(--line-hi)` in `:root` |
| **Structural Hairline Border** | `#7E7E7E` | `var(--dim)` in `:root` |
| **Variable Token (`--body`)** | `#B4B4B4` | `var(--body)` in `:root` |
| **Variable Token (`--bright`)** | `#E6E6E6` | `var(--bright)` in `:root` |
| **Variable Token (`--yellow`)** | `#FFCC00` | `var(--yellow)` in `:root` |
| **Variable Token (`--yellow-dk`)** | `#8A6E00` | `var(--yellow-dk)` in `:root` |
| **Variable Token (`--amber`)** | `#FF9900` | `var(--amber)` in `:root` |
| **Variable Token (`--green`)** | `#9ACD00` | `var(--green)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--void` | `#000000` | Color / Atmospheric Token |
| `--panel` | `#0C0C0C` | Color / Atmospheric Token |
| `--inset` | `#151515` | Color / Atmospheric Token |
| `--line` | `#303030` | Color / Atmospheric Token |
| `--line-hi` | `#4A4A4A` | Color / Atmospheric Token |
| `--dim` | `#7E7E7E` | Color / Atmospheric Token |
| `--body` | `#B4B4B4` | Color / Atmospheric Token |
| `--bright` | `#E6E6E6` | Color / Atmospheric Token |
| `--yellow` | `#FFCC00` | Color / Atmospheric Token |
| `--yellow-dk` | `#8A6E00` | Color / Atmospheric Token |
| `--amber` | `#FF9900` | Color / Atmospheric Token |
| `--green` | `#9ACD00` | Color / Atmospheric Token |
| `--logo-knockout` | `var(--inset)` | Design System Custom Token |
| `--thefwa-net-bg` | `#000000` | Canvas Substrate (from `var(--void)` in `:root`) |
| `--thefwa-net-ink` | `#7E7E7E` | Primary Typography Ink (stylesheet-derived) |
| `--thefwa-net-surface` | `#151515` | Surface Substrate (stylesheet-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Silkscreen`.
- **Primary Body Stack**: `B4B4B4`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `8px`, `11px`, `9px`, `14px`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 11px`, `letter-spacing: .22em`, `font-weight: 700`).
- **Body Copy**: CSS variables `--body: #B4B4B4`; rule `body` (`font-size: 12px`, `line-height: 1.5`).
- **Metadata & Navigation Labels**: rule `.meta` (`font-size: 8px`, `letter-spacing: .06em`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.dropzone`**: `transition: border-color .12s` extracted from `thefwa-net` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — FWA Wire — winners' newswire               │
│ ====================================================================== │
│ [ <nav.pager>              | older →                                ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.panel>                                      |   │
│ | H1: FWA Certified                                                |   │
│ | Substrate: #000000    | Ink: #7E7E7E    | Accent: #303030        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.panel>           ) max-w: 940px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Incredible Space             |  | Filter                       | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 10px  ) | │
│ | [<nav.pager>] -> [<section.panel>] -> [<section.panel>] |            │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.ticker>       ) | https://thefwa.net/                │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.pager> — `thefwa-net`)**:
   - Landmark `<nav class="pager">` hosting `FWA Wire — winners' newswire` navigation (`older →`), DOM attributes (`data-id="84"`, `data-view="image"`, `data-seen="p84:image"`, `data-src="/media/posts/mwcmqskj..."`), and stylesheet rule `html { -webkit-text-size-adjust:100% }`.
2. **Hero Stage & Focal Lead (<section.panel> — `FWA Certified`)**:
   - Landmark `<section class="panel">` presenting display lead `FWA Certified` and copy excerpt *"Posted by FWA winners >>> one post per person per day >>> newest "* over `#000000` canvas and `#7E7E7E` ink.
3. **Primary Showcase & Content Grid (<section.panel> — `Incredible Space`)**:
   - Landmark `<section class="panel filters">` rendering section `Incredible Space` with copy *"Winners post here. One item a day, newest first."*, asset references (`favicon.ico`, `icon.svg`, `apple-touch-icon.png`, `manifest.webmanifest`), and grid rule `.px { font-family:'Silkscreen',monospace;font-weight:400;letter-spacing:.02em }`.
4. **Interactive Detail & Feature Matrix (<section.panel> — `Filter`)**:
   - Landmark `<section class="panel wire">` framing `Filter` and `The Wire` (*"Incredible Space is an interactive collection of procedural archi"*) with `#151515` surface cards, `#303030` accents, and `.shell { max-width:940px;margin:0 auto;padding:8px }`.
5. **Colophon & Global Directory Footer (<footer.ticker> — `https://thefwa.net/`)**:
   - Landmark `<footer class="ticker">` anchoring `FWA Wire — winners' newswire` footer links (`older →`), copy *"Website · Certified 14 November 2026"*, and `#7E7E7E` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: thefwa-net (FWA Wire — winners' newswire)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `thefwa-net` (**FWA Wire — winners' newswire** — `https://thefwa.net/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#7E7E7E` ink, `#303030` accent).
- **Identity & Domain Context**: News from FWA winners — hires, launches, talks and work in progress. One post per person per day, newest first. No algorithm, no ranking.
- **Primary Substrate**: `#000000` (`var(--void)` in `:root`), **Primary Ink**: `#7E7E7E`, **Accent / Highlight**: `#303030`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000000` (`var(--void)` in `:root`) paired with `#7E7E7E` primary typography and `#303030` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Silkscreen` for display copy (`FWA Certified`) with `B4B4B4` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 10px`, padding `8px`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `thefwa-net` in your global stylesheet:

:root {
  /* FWA Wire — winners' newswire (thefwa-net) — Ground-Truth Extracted CSS Variables */
  --void: #000000; /* Color / Atmospheric Token (thefwa-net) */
  --panel: #0C0C0C; /* Color / Atmospheric Token (thefwa-net) */
  --inset: #151515; /* Color / Atmospheric Token (thefwa-net) */
  --line: #303030; /* Color / Atmospheric Token (thefwa-net) */
  --line-hi: #4A4A4A; /* Color / Atmospheric Token (thefwa-net) */
  --dim: #7E7E7E; /* Color / Atmospheric Token (thefwa-net) */
  --body: #B4B4B4; /* Color / Atmospheric Token (thefwa-net) */
  --bright: #E6E6E6; /* Color / Atmospheric Token (thefwa-net) */
  --yellow: #FFCC00; /* Color / Atmospheric Token (thefwa-net) */
  --yellow-dk: #8A6E00; /* Color / Atmospheric Token (thefwa-net) */
  --amber: #FF9900; /* Color / Atmospheric Token (thefwa-net) */
  --green: #9ACD00; /* Color / Atmospheric Token (thefwa-net) */
  --logo-knockout: var(--inset); /* Design System Custom Token (thefwa-net) */
  --thefwa-net-bg: #000000; /* Canvas Substrate (from `var(--void)` in `:root`) (thefwa-net) */
  --thefwa-net-ink: #7E7E7E; /* Primary Typography Ink (stylesheet-derived) (thefwa-net) */
  --thefwa-net-surface: #151515; /* Surface Substrate (stylesheet-derived) (thefwa-net) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000000` — grounded in `var(--void)` in `:root`
- **Primary Typography Ink**: `#0C0C0C` — grounded in `var(--panel)` in `:root`
- **Elevated Surface / Card Substrate**: `#151515` — grounded in `var(--inset)` in `:root`
- **Interactive Accent / Highlight**: `#303030` — grounded in `var(--line)` in `:root`
- **Secondary / Muted Copy**: `#4A4A4A` — grounded in `var(--line-hi)` in `:root`
- **Structural Hairline Border**: `#7E7E7E` — grounded in `var(--dim)` in `:root`
- **Variable Token (`--body`)**: `#B4B4B4` — grounded in `var(--body)` in `:root`
- **Variable Token (`--bright`)**: `#E6E6E6` — grounded in `var(--bright)` in `:root`
- **Variable Token (`--yellow`)**: `#FFCC00` — grounded in `var(--yellow)` in `:root`
- **Variable Token (`--yellow-dk`)**: `#8A6E00` — grounded in `var(--yellow-dk)` in `:root`
- **Variable Token (`--amber`)**: `#FF9900` — grounded in `var(--amber)` in `:root`
- **Variable Token (`--green`)**: `#9ACD00` — grounded in `var(--green)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×4035px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `940px` extracted from `thefwa-net` stylesheet
- **Padding & Gutters**: `8px` lateral canvas padding with `10px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 10px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `8px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:760px)`, `@media (max-width:520px)`, `@media (max-width:519px)`
- **Corner Radii**: `0px` (sharp unrounded corners)

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Silkscreen`
- **Body Font Stack**: `B4B4B4`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `8px`, `11px`, `9px`, `14px`)
- **H2 Section Rule**: rule `h2` (`font-size: 11px`, `letter-spacing: .22em`, `font-weight: 700`)
- **Body Copy Rule**: CSS variables `--body: #B4B4B4`; rule `body` (`font-size: 12px`, `line-height: 1.5`)
- **Metadata & Index Rule**: rule `.meta` (`font-size: 8px`, `letter-spacing: .06em`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `thefwa-net` (`FWA Wire — winners' newswire`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.pager> — `thefwa-net`)**:
   - DOM & Selectors: Landmark `<nav class="pager">` hosting `FWA Wire — winners' newswire` navigation (`older →`), DOM attributes (`data-id="84"`, `data-view="image"`, `data-seen="p84:image"`, `data-src="/media/posts/mwcmqskj..."`), and stylesheet rule `html { -webkit-text-size-adjust:100% }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.pager> — `thefwa-net`)` (`thefwa-net`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (min-width:760px)`, `@media (max-width:520px)`, `@media (max-width:519px)` with `cubic-bezier(0.25,0.1,0.25,1)` transitions and links `older →`.
2. **Hero Stage & Focal Lead (<section.panel> — `FWA Certified`)**:
   - DOM & Selectors: Landmark `<section class="panel">` presenting display lead `FWA Certified` and copy excerpt *"Posted by FWA winners >>> one post per person per day >>> newest "* over `#000000` canvas and `#7E7E7E` ink.
   - Responsive Contract: Hero stage (`1440×4035px` desktop / `390×2400px` mobile) sets `#000000` background with `#7E7E7E` headline `FWA Certified`.
3. **Primary Showcase & Content Grid (<section.panel> — `Incredible Space`)**:
   - DOM & Selectors: Landmark `<section class="panel filters">` rendering section `Incredible Space` with copy *"Winners post here. One item a day, newest first."*, asset references (`favicon.ico`, `icon.svg`, `apple-touch-icon.png`, `manifest.webmanifest`), and grid rule `.px { font-family:'Silkscreen',monospace;font-weight:400;letter-spacing:.02em }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.panel> — `Incredible Space`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 10px`) on desktop and Single-column vertical stack at `390px` viewport width with `8px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.panel> — `Filter`)**:
   - DOM & Selectors: Landmark `<section class="panel wire">` framing `Filter` and `The Wire` (*"Incredible Space is an interactive collection of procedural archi"*) with `#151515` surface cards, `#303030` accents, and `.shell { max-width:940px;margin:0 auto;padding:8px }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.panel> — `Filter`)` uses `0px` (sharp unrounded corners) radii, `#303030` highlights, and assets (favicon.ico, icon.svg, apple-touch-icon.png).
5. **Colophon & Global Directory Footer (<footer.ticker> — `https://thefwa.net/`)**:
   - DOM & Selectors: Landmark `<footer class="ticker">` anchoring `FWA Wire — winners' newswire` footer links (`older →`), copy *"Website · Certified 14 November 2026"*, and `#7E7E7E` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.ticker> — `https://thefwa.net/`)` aligns to `940px` extracted from `thefwa-net` stylesheet with `8px` lateral canvas padding with `10px` grid gap and attributes (data-id="84", data-view="image", data-seen="p84:image").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Posted by FWA winners >>> one post per person per day >>> newest first, always >>>..."*
- Copy Excerpt 2: *"Winners post here. One item a day, newest first."*
- Copy Excerpt 3: *"Incredible Space is an interactive collection of procedural architectural worlds...."*
- Copy Excerpt 4: *"Website · Certified 14 November 2026"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`
- **Extracted Stylesheet Rules (`thefwa-net`)**:
- `html { -webkit-text-size-adjust:100% }`
- `.px { font-family:'Silkscreen',monospace;font-weight:400;letter-spacing:.02em }`
- `.shell { max-width:940px;margin:0 auto;padding:8px }`
- `.strip.lead { display:flex;align-items:center;gap:10px;color:var(--dim) }`
- `.strip.lead svg { width:58px;height:auto;color:var(--yellow);flex:none }`
- **Per-Selector Transition Rules**:
- **Selector `.dropzone`**: `transition: border-color .12s` extracted from `thefwa-net` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `thefwa-net`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
