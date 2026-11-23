---
title: "UI Prompt Blueprint: thefwa-net"
date: 2026-11-23
captured_at: 2026-11-23
target: "thefwa-net"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#ffcc00` ink, `#ff9900` accent)"
---

# UI Design System & Master Generation Blueprint: thefwa-net

> **FWA Wire — winners' newswire** (https://thefwa.net/) — News from FWA winners — hires, launches, talks and work in progress. One post per person per day, newest first. No algorithm, no ranking.

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **FWA Wire — winners' newswire** (`https://thefwa.net/`). News from FWA winners — hires, launches, talks and work in progress. One post per person per day, newest first. No algorithm, no ranking.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#ffcc00` ink, `#ff9900` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffcc00` primary typography and `#ff9900` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Silkscreen` for display copy (`FWA // CANON_STATUS: VERIFIED`) with `Verdana` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 10px`, padding `8px`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1440px` (full-bleed `100%` viewport stage).
- **Canvas Lateral Padding & Spacing**: `8px` lateral canvas padding with `10px` grid gap.
- **Border Radius Scale**: `0px` (sharp unrounded corners).

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 10px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `8px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:760px)`, `@media (max-width:520px)`, `@media (max-width:519px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffcc00` | live computed `h2` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0c0c0c` | `var(--panel)` in `:root` |
| **Interactive Accent / Highlight** | `#ff9900` | live computed `button` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#7e7e7e` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#303030` | `var(--line)` in `:root` |
| **Variable Token (`--inset`)** | `#151515` | `var(--inset)` in `:root` |
| **Variable Token (`--line-hi`)** | `#4a4a4a` | `var(--line-hi)` in `:root` |
| **Variable Token (`--body`)** | `#b4b4b4` | `var(--body)` in `:root` |
| **Variable Token (`--bright`)** | `#e6e6e6` | `var(--bright)` in `:root` |
| **Variable Token (`--yellow-dk`)** | `#8a6e00` | `var(--yellow-dk)` in `:root` |
| **Variable Token (`--green`)** | `#9acd00` | `var(--green)` in `:root` |

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
| `--thefwa-net-bg` | `#000000` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--thefwa-net-ink` | `#ffcc00` | Primary Typography Ink (computed-derived) |
| `--thefwa-net-surface` | `#0c0c0c` | Surface Substrate (computed-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Silkscreen`.
- **Primary Body Stack**: `Verdana`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: observed font-size ladder: `11px`, `14px`, `12px`, `11.5px`, `8px`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 11px`, `line-height: 16.5px`, `font-weight: 700`, `letter-spacing: 2.42px`); rule `h2` (`font-size: 11px`, `letter-spacing: .22em`, `font-weight: 700`).
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: 18px`, `font-weight: 400`); rule `body` (`font-size: 12px`, `line-height: 1.5`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: 18px`, `font-weight: 400`); rule `.meta` (`font-size: 8px`, `letter-spacing: .06em`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.dropzone`**: `transition: border-color .12s` extracted from `thefwa-net` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in captured CSS).
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — FWA Wire — winners' newswire               │
│ ====================================================================== │
│ [ <nav.pager> (598x45px)              | older →                      ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.panel> (w=1440px)                             | │
│ | H1: FWA // CANON_STATUS: VERIFIED                                  | │
│ | Substrate: #000000 | Ink: #ffcc00 | Accent: #ff9900                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.filters>) max-w: 1440px                    | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Michael Bay Studio           |  | Posted by FWA winners >>> on | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.wire>) — Winners post here. On             | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.ticker>     ) | https://thefwa.net/                  │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 10px)       │
│ ====================================================================== │
│ [ HEADER BAR (<nav.pager>             ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.panel>) — 390px Vertical Lead                 | │
│ | H1: FWA // CANON_STATUS: VERIFIED                                  | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.filters>) — 1-Col Stack                   | │
│ | [ Item 1: Michael Bay Studio                                     ] | │
│ | [ Item 2: Posted by FWA winners >>> one post per person pe       ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.wire>) — 1-Col (Winners post here.)         | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.ticker>     ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.pager> — `thefwa-net`)**:
   - Landmark `<nav class="pager">` (`598x45px`) hosting `FWA Wire — winners' newswire` navigation (`older →`), DOM attributes (`data-id="89"`, `data-view="video"`, `data-seen="p89:video"`, `data-src="https://www.youtube-n..."`), and stylesheet rule `html { -webkit-text-size-adjust:100% }`.
2. **Hero Stage & Focal Lead (<section.panel> — `FWA // CANON_STATUS: VERIFIED`)**:
   - Landmark `<section class="panel">` presenting display lead `FWA // CANON_STATUS: VERIFIED` and copy excerpt *"CREDITSOliver Gareis"* over `#000000` canvas and `#ffcc00` ink.
3. **Primary Showcase & Content Grid (<section.filters> — `Michael Bay Studio`)**:
   - Landmark `<section class="panel filters">` rendering section `Michael Bay Studio` with copy *"Posted by FWA winners >>> one post per person per day >>> newest "*, asset references (`favicon.ico`, `icon.svg`, `apple-touch-icon.png`, `manifest.webmanifest`), and grid rule `.px { font-family:'Silkscreen',monospace;font-weight:400;letter-spacing:.02em }`.
4. **Interactive Detail & Feature Matrix (<section.wire> — `Posted by FWA winners >>> one post`)**:
   - Landmark `<section class="panel wire">` framing `Posted by FWA winners >>> one post per person pe` and `Winners post here. One item a day, newest first.` (*"Winners post here. One item a day, newest first."*) with `#0c0c0c` surface cards, `#ff9900` accents, and `.shell { max-width:940px;margin:0 auto;padding:8px }`.
5. **Colophon & Global Directory Footer (<footer.ticker> — `https://thefwa.net/`)**:
   - Landmark `<footer class="ticker">` anchoring `FWA Wire — winners' newswire` footer links (`older →`), copy *"Credits Oliver Gareis"*, and `#303030` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: thefwa-net (FWA Wire — winners' newswire)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `thefwa-net` (**FWA Wire — winners' newswire** — `https://thefwa.net/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#ffcc00` ink, `#ff9900` accent).
- **Identity & Domain Context**: News from FWA winners — hires, launches, talks and work in progress. One post per person per day, newest first. No algorithm, no ranking.
- **Primary Substrate**: `#000000` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#ffcc00`, **Accent / Highlight**: `#ff9900`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffcc00` primary typography and `#ff9900` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Silkscreen` for display copy (`FWA // CANON_STATUS: VERIFIED`) with `Verdana` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 10px`, padding `8px`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `thefwa-net` in your global stylesheet:

:root {
  /* FWA Wire — winners' newswire (thefwa-net) — Live-Grounded CSS Variables */
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
  --thefwa-net-bg: #000000; /* Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) (thefwa-net) */
  --thefwa-net-ink: #ffcc00; /* Primary Typography Ink (computed-derived) (thefwa-net) */
  --thefwa-net-surface: #0c0c0c; /* Surface Substrate (computed-derived) (thefwa-net) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000000` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#ffcc00` — grounded in live computed `h2` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#0c0c0c` — grounded in `var(--panel)` in `:root`
- **Interactive Accent / Highlight**: `#ff9900` — grounded in live computed `button` `color` (`computed_styles.json`)
- **Secondary / Muted Copy**: `#7e7e7e` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#303030` — grounded in `var(--line)` in `:root`
- **Variable Token (`--inset`)**: `#151515` — grounded in `var(--inset)` in `:root`
- **Variable Token (`--line-hi`)**: `#4a4a4a` — grounded in `var(--line-hi)` in `:root`
- **Variable Token (`--body`)**: `#b4b4b4` — grounded in `var(--body)` in `:root`
- **Variable Token (`--bright`)**: `#e6e6e6` — grounded in `var(--bright)` in `:root`
- **Variable Token (`--yellow-dk`)**: `#8a6e00` — grounded in `var(--yellow-dk)` in `:root`
- **Variable Token (`--green`)**: `#9acd00` — grounded in `var(--green)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` viewport stage)
- **Padding & Gutters**: `8px` lateral canvas padding with `10px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 10px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `8px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:760px)`, `@media (max-width:520px)`, `@media (max-width:519px)`
- **Corner Radii**: `0px` (sharp unrounded corners)

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Silkscreen`
- **Body Font Stack**: `Verdana`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: observed font-size ladder: `11px`, `14px`, `12px`, `11.5px`, `8px`
- **H2 Section Rule**: live computed `h2` (`font-size: 11px`, `line-height: 16.5px`, `font-weight: 700`, `letter-spacing: 2.42px`); rule `h2` (`font-size: 11px`, `letter-spacing: .22em`, `font-weight: 700`)
- **Body Copy Rule**: live computed `body` (`font-size: 12px`, `line-height: 18px`, `font-weight: 400`); rule `body` (`font-size: 12px`, `line-height: 1.5`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 12px`, `line-height: 18px`, `font-weight: 400`); rule `.meta` (`font-size: 8px`, `letter-spacing: .06em`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `thefwa-net` (`FWA Wire — winners' newswire`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.pager> — `thefwa-net`)**:
   - DOM & Selectors: Landmark `<nav class="pager">` (`598x45px`) hosting `FWA Wire — winners' newswire` navigation (`older →`), DOM attributes (`data-id="89"`, `data-view="video"`, `data-seen="p89:video"`, `data-src="https://www.youtube-n..."`), and stylesheet rule `html { -webkit-text-size-adjust:100% }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.pager> — `thefwa-net`)` (`thefwa-net`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (min-width:760px)`, `@media (max-width:520px)`, `@media (max-width:519px)` with `cubic-bezier(0.25,0.1,0.25,1)` transitions and links `older →`.
2. **Hero Stage & Focal Lead (<section.panel> — `FWA // CANON_STATUS: VERIFIED`)**:
   - DOM & Selectors: Landmark `<section class="panel">` presenting display lead `FWA // CANON_STATUS: VERIFIED` and copy excerpt *"CREDITSOliver Gareis"* over `#000000` canvas and `#ffcc00` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#000000` background with `#ffcc00` headline `FWA // CANON_STATUS: VERIFIED`.
3. **Primary Showcase & Content Grid (<section.filters> — `Michael Bay Studio`)**:
   - DOM & Selectors: Landmark `<section class="panel filters">` rendering section `Michael Bay Studio` with copy *"Posted by FWA winners >>> one post per person per day >>> newest "*, asset references (`favicon.ico`, `icon.svg`, `apple-touch-icon.png`, `manifest.webmanifest`), and grid rule `.px { font-family:'Silkscreen',monospace;font-weight:400;letter-spacing:.02em }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.filters> — `Michael Bay Studio`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 10px`) on desktop and Single-column vertical stack at `390px` viewport width with `8px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.wire> — `Posted by FWA winners >>> one post`)**:
   - DOM & Selectors: Landmark `<section class="panel wire">` framing `Posted by FWA winners >>> one post per person pe` and `Winners post here. One item a day, newest first.` (*"Winners post here. One item a day, newest first."*) with `#0c0c0c` surface cards, `#ff9900` accents, and `.shell { max-width:940px;margin:0 auto;padding:8px }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.wire> — `Posted by FWA winners >>> one post`)` uses `0px` (sharp unrounded corners) radii, `#ff9900` highlights, and assets (favicon.ico, icon.svg, apple-touch-icon.png).
5. **Colophon & Global Directory Footer (<footer.ticker> — `https://thefwa.net/`)**:
   - DOM & Selectors: Landmark `<footer class="ticker">` anchoring `FWA Wire — winners' newswire` footer links (`older →`), copy *"Credits Oliver Gareis"*, and `#303030` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.ticker> — `https://thefwa.net/`)` aligns to `1440px` (full-bleed `100%` viewport stage) with `8px` lateral canvas padding with `10px` grid gap and attributes (data-id="89", data-view="video", data-seen="p89:video").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"CREDITSOliver Gareis"*
- Copy Excerpt 2: *"Posted by FWA winners >>> one post per person per day >>> newest first, always >>>..."*
- Copy Excerpt 3: *"Winners post here. One item a day, newest first."*
- Copy Excerpt 4: *"Credits Oliver Gareis"*

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
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in captured CSS).
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `thefwa-net`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
