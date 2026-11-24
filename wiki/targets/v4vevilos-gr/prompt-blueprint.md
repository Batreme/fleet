---
title: "UI Prompt Blueprint: v4vevilos-gr"
date: 2026-11-24
captured_at: 2026-11-24
target: "v4vevilos-gr"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: wheel
desktop_keyframes: 4
subpages_crawled: 0
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#050507` / `#ff6a00`)"
---

# UI Design System & Master Generation Blueprint: v4vevilos-gr

> **Βέβηλος • Once dead twice alive** (https://v4vevilos.gr) — Επίσημο hub του Βέβηλου • μουσική, live, δισκογραφία & σύνδεσμοι σε ένα σημείο.

![Desktop Journey Filmstrip (1280x3312)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Βέβηλος • Once dead twice alive** (`https://v4vevilos.gr`). Επίσημο hub του Βέβηλου • μουσική, live, δισκογραφία & σύνδεσμοι σε ένα σημείο.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#050507` / `#ff6a00`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#050507` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#ff6a00` accents.
  - **Grounded Typographic Hierarchy**: Uses `Advent Pro` across display (`Βέβηλος Βέβηλος`) and body copy, paired with `Fira Sans Extra Condensed` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `1192px` container bounds (`gap: 20px`, padding `24px`) with `cubic-bezier(.76,0,.24,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×3312px` (`assets/desktop-journey.webp`, `4` keyframes up to `y=2800px` / doc `4771px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1192px` (measured `<main>` bounding box width within `1440px` desktop viewport).
- **Canvas Lateral Padding & Spacing**: `24px` lateral canvas padding with `20px` grid gap.
- **Border Radius Scale**: `999px`, `12px`, `50%`, `18px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1192px`, `gap: 20px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `24px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (max-width:1100px)`, `@media (max-width:900px)`, `@media (max-width:640px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#050507` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#050506` | `var(--pl-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#ff6a00` | `var(--accent-fire)` in `:root` |
| **Secondary / Muted Copy** | `#f4efe6` | live computed `h2` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#1c1c1d` | `var(--border)` in `:root` (`rgba(255,255,255,.09)`) |
| **Variable Token (`--accent`)** | `#ff3e3e` | `var(--accent)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#050507` | Canvas / Surface Token |
| `--bg-soft` | `rgba(255,255,255,.02)` | Canvas / Surface Token |
| `--card-bg` | `rgba(255,255,255,.035)` | Canvas / Surface Token |
| `--card-bg-strong` | `rgba(255,255,255,.05)` | Canvas / Surface Token |
| `--border` | `rgba(255,255,255,.09)` | Elevation / Border Token |
| `--border-strong` | `rgba(255,62,62,.22)` | Elevation / Border Token |
| `--accent` | `#ff3e3e` | Brand / Palette Token |
| `--accent-fire` | `#ff6a00` | Brand / Palette Token |
| `--text` | `#ffffff` | Typography Ink Token |
| `--text-muted` | `rgba(255,255,255,.68)` | Typography Ink Token |
| `--text-soft` | `rgba(255,255,255,.45)` | Typography Ink Token |
| `--glass` | `blur(18px) saturate(155%)` | Dimension / Scale Token |
| `--radius-xl` | `32px` | Elevation / Border Token |
| `--radius-lg` | `22px` | Elevation / Border Token |
| `--radius-md` | `16px` | Elevation / Border Token |
| `--font-display` | `"Bebas Neue", "Fira Sans Extra Condensed", "Arial Narrow", sans-serif` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Advent Pro`.
- **Primary Body Stack**: `Advent Pro`.
- **Technical / Metadata Stack**: `Fira Sans Extra Condensed`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 168px`, `line-height: 154.56px`, `font-weight: 300`, `letter-spacing: 3.36px`); CSS variables `--font-display: "Bebas Neue", "Fira Sans Extra Condensed", "Arial Narrow", sans-serif`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 95.04px`, `line-height: 83.6352px`, `font-weight: 800`, `letter-spacing: -1.4256px`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`); CSS variables `--font-body: "Advent Pro", sans-serif`; rule `p` (`font-size: .98rem`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`); rule `small` (`font-size: .55em`, `font-weight: 500`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.76,0,.24,1)`, `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.45,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.pl-gate i`**: `transition: transform 1.1s cubic-bezier(.76,0,.24,1)` extracted from `v4vevilos-gr` stylesheet.
- **Selector `.pl-core`**: `transition: opacity .35s ease,transform .6s cubic-bezier(.76,0,.24,1),filt...` extracted from `v4vevilos-gr` stylesheet.
- **Selector `.pl-mark img`**: `transition: filter .5s ease,transform .5s cubic-bezier(.76,0,.24,1)` extracted from `v4vevilos-gr` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.76,0,.24,1)`)**: Governs interactive state transitions across `<header.topbar>` and `<section.gig-banner>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `wheel` (max document height `4771px`, deepest scrollY reached `2800px` across `4` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `WebGL/Canvas`.
- **Interactive Control Probe (`accordion`)**: Tested `Λεπτομέρειες` (diff `3.237`).

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Βέβηλος • Once dead twice alive            │
│ ====================================================================== │
│ [ <header.topbar> (1192x126px)        | EL · EN                      ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero> (w=1192px)                              | │
│ | H1: Βέβηλος Βέβηλος                                                | │
│ | Substrate: #050507 | Ink: #ffffff | Accent: #ff6a00                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.gig-banner>) max-w: 1192px                 | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Βέβηλος Β έ β η λ ο ς        |  | Νεκρή Ζώνη V                 | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.vv-consent>) — Η επόμενη σελίδα γράφ       | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.pl-open>    ) | https://v4vevilos.gr                 │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 20px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.topbar>         ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.hero>) — 390px Vertical Lead                  | │
│ | H1: Βέβηλος Βέβηλος                                                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.gig-banner>) — 1-Col Stack                | │
│ | [ Item 1: Βέβηλος Β έ β η λ ο ς                                  ] | │
│ | [ Item 2: Νεκρή Ζώνη V                                           ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.vv-consent>) — 1-Col (Η επόμενη σελίδα γ)   | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.pl-open>    ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.topbar> — `v4vevilos-gr`)**:
   - Landmark `<header class="topbar reveal">` (`1192x126px`) hosting `Βέβηλος • Once dead twice alive` navigation (`EL · EN`), DOM attributes (`data-state="off"`, `data-engine="assets/sound-engine.m..."`, `data-zap="Βέβηλος·Vevilos·V4"`, `data-split`), and stylesheet rule `html { scroll-behavior:smooth }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Βέβηλος Βέβηλος`)**:
   - Landmark `<section class="hero">` presenting display lead `Βέβηλος Βέβηλος` and copy excerpt *"Rap • Hip-hop • Αθήνα"* over `#050507` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.gig-banner> — `Βέβηλος Β έ β η λ ο ς`)**:
   - Landmark `<section class="gig-banner hero-gig">` rendering section `Βέβηλος Β έ β η λ ο ς` with copy *"Ιδρυτικό μέλος των Βαβυλώνα και Omerta. Rap και hip-hop με βάθος,"*, asset references (`favicon.ico`, `apple-touch-icon.png`, `advent-pro-100-700-greek.woff2`, `advent-pro-100-700-latin.woff2`), and grid rule `body { overflow-x:clip }`.
4. **Interactive Detail & Feature Matrix (<section.vv-consent> — `Νεκρή Ζώνη V`)**:
   - Landmark `<section class="vv-consent">` framing `Νεκρή Ζώνη V` and `Η επόμενη σελίδα γράφεται και από σένα.` (*"Δεν χρειάζεται πια να ψάξεις τη Νεκρή Ζώνη.. Αυτή τη φορά, θα σε "*) with `#050506` surface cards, `#ff6a00` accents, and `img { max-width:100%;display:block }`.
5. **Colophon & Global Directory Footer (<footer.pl-open> — `https://v4vevilos.gr`)**:
   - Landmark `<footer class="pl-open">` anchoring `Βέβηλος • Once dead twice alive` footer links (`EL · EN`), copy *"Δεν χρειάζεται πια να ψάξεις τη Νεκρή Ζώνη.."*, and `#1c1c1d` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `Βέβηλος Βέβηλος` · sticky/fixed elements: `4`
- **Step 02** (`y=1500px`, `39%`): Active landmark `Η επόμενη σελίδα γράφεται και από σένα.` · sticky/fixed elements: `4`
- **Step 03** (`y=2150px`, `56%`): Active landmark `Live Timeline` · sticky/fixed elements: `4`
- **Step 04** (`y=2800px`, `72%`): Active landmark `Συχνές ερωτήσεις` · sticky/fixed elements: `4`

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: v4vevilos-gr (Βέβηλος • Once dead twice alive)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `v4vevilos-gr` (**Βέβηλος • Once dead twice alive** — `https://v4vevilos.gr`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#050507` / `#ff6a00`).
- **Identity & Domain Context**: Επίσημο hub του Βέβηλου • μουσική, live, δισκογραφία & σύνδεσμοι σε ένα σημείο.
- **Primary Substrate**: `#050507` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#ff6a00`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#050507` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#ff6a00` accents.
  - **Grounded Typographic Hierarchy**: Uses `Advent Pro` across display (`Βέβηλος Βέβηλος`) and body copy, paired with `Fira Sans Extra Condensed` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `1192px` container bounds (`gap: 20px`, padding `24px`) with `cubic-bezier(.76,0,.24,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `v4vevilos-gr` in your global stylesheet:

:root {
  /* Βέβηλος • Once dead twice alive (v4vevilos-gr) — Live-Grounded CSS Variables */
  --bg: #050507; /* Canvas / Surface Token (v4vevilos-gr) */
  --bg-soft: rgba(255,255,255,.02); /* Canvas / Surface Token (v4vevilos-gr) */
  --card-bg: rgba(255,255,255,.035); /* Canvas / Surface Token (v4vevilos-gr) */
  --card-bg-strong: rgba(255,255,255,.05); /* Canvas / Surface Token (v4vevilos-gr) */
  --border: rgba(255,255,255,.09); /* Elevation / Border Token (v4vevilos-gr) */
  --border-strong: rgba(255,62,62,.22); /* Elevation / Border Token (v4vevilos-gr) */
  --accent: #ff3e3e; /* Brand / Palette Token (v4vevilos-gr) */
  --accent-fire: #ff6a00; /* Brand / Palette Token (v4vevilos-gr) */
  --text: #ffffff; /* Typography Ink Token (v4vevilos-gr) */
  --text-muted: rgba(255,255,255,.68); /* Typography Ink Token (v4vevilos-gr) */
  --text-soft: rgba(255,255,255,.45); /* Typography Ink Token (v4vevilos-gr) */
  --glass: blur(18px) saturate(155%); /* Dimension / Scale Token (v4vevilos-gr) */
  --radius-xl: 32px; /* Elevation / Border Token (v4vevilos-gr) */
  --radius-lg: 22px; /* Elevation / Border Token (v4vevilos-gr) */
  --radius-md: 16px; /* Elevation / Border Token (v4vevilos-gr) */
  --font-display: "Bebas Neue", "Fira Sans Extra Condensed", "Arial Narrow", sans-serif; /* Typography / Scale Token (v4vevilos-gr) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#050507` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#ffffff` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#050506` — grounded in `var(--pl-bg)` in `:root`
- **Interactive Accent / Highlight**: `#ff6a00` — grounded in `var(--accent-fire)` in `:root`
- **Secondary / Muted Copy**: `#f4efe6` — grounded in live computed `h2` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#1c1c1d` — grounded in `var(--border)` in `:root` (`rgba(255,255,255,.09)`)
- **Variable Token (`--accent`)**: `#ff3e3e` — grounded in `var(--accent)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×3312px` (multi-frame vertical journey filmstrip (3312px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1192px` (measured `<main>` bounding box width within `1440px` desktop viewport)
- **Padding & Gutters**: `24px` lateral canvas padding with `20px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1192px`, `gap: 20px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `24px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (max-width:1100px)`, `@media (max-width:900px)`, `@media (max-width:640px)`
- **Corner Radii**: `999px`, `12px`, `50%`, `18px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Advent Pro`
- **Body Font Stack**: `Advent Pro`
- **Monospace / Technical Font Stack**: `Fira Sans Extra Condensed`
- **H1 Display Rule**: live computed `h1` (`font-size: 168px`, `line-height: 154.56px`, `font-weight: 300`, `letter-spacing: 3.36px`); CSS variables `--font-display: "Bebas Neue", "Fira Sans Extra Condensed", "Arial Narrow", sans-serif`
- **H2 Section Rule**: live computed `h2` (`font-size: 95.04px`, `line-height: 83.6352px`, `font-weight: 800`, `letter-spacing: -1.4256px`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`); CSS variables `--font-body: "Advent Pro", sans-serif`; rule `p` (`font-size: .98rem`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`); rule `small` (`font-size: .55em`, `font-weight: 500`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `v4vevilos-gr` (`Βέβηλος • Once dead twice alive`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.topbar> — `v4vevilos-gr`)**:
   - DOM & Selectors: Landmark `<header class="topbar reveal">` (`1192x126px`) hosting `Βέβηλος • Once dead twice alive` navigation (`EL · EN`), DOM attributes (`data-state="off"`, `data-engine="assets/sound-engine.m..."`, `data-zap="Βέβηλος·Vevilos·V4"`, `data-split`), and stylesheet rule `html { scroll-behavior:smooth }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.topbar> — `v4vevilos-gr`)` (`v4vevilos-gr`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (max-width:1100px)`, `@media (max-width:900px)`, `@media (max-width:640px)` with `cubic-bezier(.76,0,.24,1)`, `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.45,0,.2,1)` transitions and links `EL · EN`.
2. **Hero Stage & Focal Lead (<section.hero> — `Βέβηλος Βέβηλος`)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `Βέβηλος Βέβηλος` and copy excerpt *"Rap • Hip-hop • Αθήνα"* over `#050507` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1280×3312px` desktop / `390×2616px` mobile) sets `#050507` background with `#ffffff` headline `Βέβηλος Βέβηλος`.
3. **Primary Showcase & Content Grid (<section.gig-banner> — `Βέβηλος Β έ β η λ ο ς`)**:
   - DOM & Selectors: Landmark `<section class="gig-banner hero-gig">` rendering section `Βέβηλος Β έ β η λ ο ς` with copy *"Ιδρυτικό μέλος των Βαβυλώνα και Omerta. Rap και hip-hop με βάθος,"*, asset references (`favicon.ico`, `apple-touch-icon.png`, `advent-pro-100-700-greek.woff2`, `advent-pro-100-700-latin.woff2`), and grid rule `body { overflow-x:clip }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.gig-banner> — `Βέβηλος Β έ β η λ ο ς`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1192px`, `gap: 20px`) on desktop and Single-column vertical stack at `390px` viewport width with `24px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.vv-consent> — `Νεκρή Ζώνη V`)**:
   - DOM & Selectors: Landmark `<section class="vv-consent">` framing `Νεκρή Ζώνη V` and `Η επόμενη σελίδα γράφεται και από σένα.` (*"Δεν χρειάζεται πια να ψάξεις τη Νεκρή Ζώνη.. Αυτή τη φορά, θα σε "*) with `#050506` surface cards, `#ff6a00` accents, and `img { max-width:100%;display:block }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.vv-consent> — `Νεκρή Ζώνη V`)` uses `999px`, `12px`, `50%`, `18px` radii, `#ff6a00` highlights, and assets (favicon.ico, apple-touch-icon.png, advent-pro-100-700-greek.woff2).
5. **Colophon & Global Directory Footer (<footer.pl-open> — `https://v4vevilos.gr`)**:
   - DOM & Selectors: Landmark `<footer class="pl-open">` anchoring `Βέβηλος • Once dead twice alive` footer links (`EL · EN`), copy *"Δεν χρειάζεται πια να ψάξεις τη Νεκρή Ζώνη.."*, and `#1c1c1d` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.pl-open> — `https://v4vevilos.gr`)` aligns to `1192px` (measured `<main>` bounding box width within `1440px` desktop viewport) with `24px` lateral canvas padding with `20px` grid gap and attributes (data-state="off", data-engine="assets/sound-engine.m...", data-zap="Βέβηλος·Vevilos·V4").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Rap • Hip-hop • Αθήνα"*
- Copy Excerpt 2: *"Ιδρυτικό μέλος των Βαβυλώνα και Omerta. Rap και hip-hop με βάθος, κοινωνική ματιά..."*
- Copy Excerpt 3: *"Δεν χρειάζεται πια να ψάξεις τη Νεκρή Ζώνη.. Αυτή τη φορά, θα σε βρει εκείνη."*
- Copy Excerpt 4: *"Δεν χρειάζεται πια να ψάξεις τη Νεκρή Ζώνη.."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.76,0,.24,1)`, `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.45,0,.2,1)`
- **Extracted Stylesheet Rules (`v4vevilos-gr`)**:
- `html { scroll-behavior:smooth }`
- `body { overflow-x:clip }`
- `img { max-width:100%;display:block }`
- `focus-visible { outline:2px solid var(--accent);outline-offset:3px }`
- `webkit-scrollbar-track { background:09090b }`
- **Per-Selector Transition Rules**:
- **Selector `.pl-gate i`**: `transition: transform 1.1s cubic-bezier(.76,0,.24,1)` extracted from `v4vevilos-gr` stylesheet.
- **Selector `.pl-core`**: `transition: opacity .35s ease,transform .6s cubic-bezier(.76,0,.24,1),filt...` extracted from `v4vevilos-gr` stylesheet.
- **Selector `.pl-mark img`**: `transition: filter .5s ease,transform .5s cubic-bezier(.76,0,.24,1)` extracted from `v4vevilos-gr` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.76,0,.24,1)`)**: Governs interactive state transitions across `<header.topbar>` and `<section.gig-banner>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `wheel` vertical progression up to `4771px` across 4 distinct viewport chapters using WebGL/Canvas.
- **Vertical Chapter Sequence**: Βέβηλος Βέβηλος (0%) -> Η επόμενη σελίδα γράφεται κ... (39%) -> Live Timeline (56%) -> Συχνές ερωτήσεις (72%).

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `v4vevilos-gr`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | Βέβηλος Βέβηλος | `4` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `1500px` | `39%` | Η επόμενη σελίδα γράφεται και από σένα. | `4` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `2150px` | `56%` | Live Timeline | `4` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `2800px` | `72%` | Συχνές ερωτήσεις | `4` | [desktop-step-04.webp](assets/desktop-step-04.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | Βέβηλος Βέβηλος | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `3214px` | `50%` | Βρες το στίχο | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `6428px` | `100%` | Footer | [mobile-step-03.webp](assets/mobile-step-03.webp) |

