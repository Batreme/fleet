---
title: "UI Prompt Blueprint: www-mdscollective-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-mdscollective-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#101010` ink, `#ffa500` accent)"
---

# UI Design System & Master Generation Blueprint: www-mdscollective-com

> **MDS Collective · China Marketing Agency for Hotels & Tourism** (https://www.mdscollective.com) — Award-winning China marketing agency for luxury hotels and tourism brands. RedNote, WeChat, Douyin, KOLs and AI search. Formerly Metric D...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **MDS Collective · China Marketing Agency for Hotels & Tourism** (`https://www.mdscollective.com`). Award-winning China marketing agency for luxury hotels and tourism brands. RedNote, WeChat, Douyin, KOLs and AI search. Formerly Metric D...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#101010` ink, `#ffa500` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#101010` primary typography and `#ffa500` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Instrument Serif` for display copy (`Luxury Marketing targeting Chinese &`) with `Helvetica Neue` and `SF Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1296px` container bounds (`gap: 56px`, padding `72px`) with `cubic-bezier(.77,0,.18,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1296px` (measured widest bounded `<section>` landmark width on `1440px` desktop).
- **Canvas Lateral Padding & Spacing**: `72px` lateral canvas padding with `56px` grid gap.
- **Border Radius Scale**: `999px`, `14px`, `10px`, `9px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1296px`, `gap: 56px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `72px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (width<=820px)`, `@media (width>=821px)`, `@media (width<=800px)`, `@media (hover:none),(prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#101010` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f3f3f1` | `var(--bg2)` in `:root` |
| **Interactive Accent / Highlight** | `#ffa500` | `.legal-doc a:hover { color: orange }` (`#ffa500`) |
| **Secondary / Muted Copy** | `#8e8e89` | `var(--ink3-lg)` in `:root` |
| **Structural Hairline Border** | `#a3a39e` | `var(--rule)` in `:root` |
| **Variable Token (`--ink2`)** | `#5f5f5b` | `var(--ink2)` in `:root` |
| **Variable Token (`--ink3`)** | `#767671` | `var(--ink3)` in `:root` |
| **Variable Token (`--line`)** | `#e3e3df` | `var(--line)` in `:root` |
| **Variable Token (`--gold`)** | `#1c486d` | `var(--gold)` in `:root` |
| **Variable Token (`--orange`)** | `#e6872d` | `var(--orange)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#fff` | Canvas / Surface Token |
| `--bg2` | `#f3f3f1` | Canvas / Surface Token |
| `--ink` | `#101010` | Typography Ink Token |
| `--ink2` | `#5f5f5b` | Typography Ink Token |
| `--ink3` | `#767671` | Typography Ink Token |
| `--ink3-lg` | `#8e8e89` | Typography Ink Token |
| `--rule` | `#a3a39e` | Color / Atmospheric Token |
| `--line` | `#e3e3df` | Color / Atmospheric Token |
| `--gold` | `#1c486d` | Color / Atmospheric Token |
| `--navy` | `#1c486d` | Layout / Spatial Grid Token |
| `--orange` | `#e6872d` | Color / Atmospheric Token |
| `--serif` | `"Instrument Serif","PS Times","Times New Roman",Georgia,serif` | Typography / Scale Token |
| `--sans` | `"Helvetica Neue",Helvetica,Arial,system-ui,sans-serif` | Typography / Scale Token |
| `--r-lg` | `24px` | Dimension / Scale Token |
| `--hl` | `#e6872d52` | Color / Atmospheric Token |
| `--www-mdscollectiv-bg` | `#ffffff` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Instrument Serif`.
- **Primary Body Stack**: `Helvetica Neue`.
- **Technical / Metadata Stack**: `SF Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 141.12px`, `line-height: 143.942px`, `font-weight: 400`, `letter-spacing: -3.528px`); rule `h1` (`font-size: clamp(54px,9.8vw,156px)`, `line-height: 1.02`, `letter-spacing: -.025em`, `font-weight: 400`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 80.64px`, `line-height: 82.2528px`, `font-weight: 400`, `letter-spacing: -2.016px`); rule `h2` (`font-size: clamp(38px,5.6vw,88px)`, `line-height: 1.02`, `letter-spacing: -.025em`, `font-weight: 400`).
- **Body Copy**: live computed `body` (`font-size: 15px`, `line-height: 22.5px`, `font-weight: 400`); rule `p` (`font-size: 15px`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 15px`, `line-height: 22.5px`, `font-weight: 400`); rule `small` (`font-size: .5em`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.77,0,.18,1)`, `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.2,.7,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `#loader`**: `transition: opacity .8s,visibility .8s` extracted from `www-mdscollective-com` stylesheet.
- **Selector `#loader .bar i`**: `transition: width .1s linear` extracted from `www-mdscollective-com` stylesheet.
- **Selector `nav`**: `transition: background .45s,color .45s,padding .45s,border-color .45s` extracted from `www-mdscollective-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.77,0,.18,1)`)**: Governs interactive state transitions across `<nav.lenis>` and `<section.hero>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — MDS Collective · China Marketing Agency fo │
│ ====================================================================== │
│ [ <nav.lenis> (1440x79px)             | About · Hotels & Hospitality ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.brand-hero> (w=1440px)                        | │
│ | H1: Luxury Marketing targeting Chinese & East Asian T...           | │
│ | Substrate: #ffffff | Ink: #101010 | Accent: #ffa500                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.hero>) max-w: 1296px                       | │
│ | +------------------------------+  +------------------------------+ | │
│ | | FIT travelers have evolved.  |  | We are your long-term East A | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.hero-media>) — Mandapa, a Ritz-Carlt       | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.wrap>       ) | https://www.mdscollective.com        │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 56px)       │
│ ====================================================================== │
│ [ HEADER BAR (<nav.lenis>             ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.brand-hero>) — 390px Vertical Lead            | │
│ | H1: Luxury Marketing targeting Chinese & East Asian T...           | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.hero>) — 1-Col Stack                      | │
│ | [ Item 1: FIT travelers have evolved. AI is now where their...   ] | │
│ | [ Item 2: We are your long-term East Asia marketing partner.     ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.hero-media>) — 1-Col (Mandapa, a Ritz-Ca)   | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.wrap>       ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.lenis> — `www-mdscollective-com`)**:
   - Landmark `<nav class="lenis">` (`1440x79px`) hosting `MDS Collective · China Marketing Age` navigation (`About · Hotels & Hospitality · Tourism Boards · Airlines & Cruises · Higher Education`), DOM attributes (`data-u="hello"`, `data-d="mdscollective.com"`, `data-src-sm="/video/hero-720.mp4"`, `data-src-lg="/video/hero-1080.mp4"`), and stylesheet rule `selection { color:fff;background:e6872d }`.
2. **Hero Stage & Focal Lead (<section.brand-hero> — `Luxury Marketing targeting Chinese`)**:
   - Landmark `<section class="brand-hero">` presenting display lead `Luxury Marketing targeting Chinese & East Asian T...` and copy excerpt *"ASIA'S TOP HOSPITALITY, TRAVEL AND TOURISM MARKETING COMPANY"* over `#ffffff` canvas and `#101010` ink.
3. **Primary Showcase & Content Grid (<section.hero> — `FIT travelers have evolved. AI is `)**:
   - Landmark `<section class="hero wrap">` rendering section `FIT travelers have evolved. AI is now where their...` with copy *"Asia's top hospitality, travel and tourism marketing company"*, asset references (`favicon.ico`, `favicon-32.png`, `apple-touch-icon.png`, `hero-1080.mp4`), and grid rule `body { background:var(--bg);color:var(--ink);font-family:var(--sans);margin:0 }`.
4. **Interactive Detail & Feature Matrix (<section.hero-media> — `We are your long-term East Asia ma`)**:
   - Landmark `<section class="hero-media wrap">` framing `We are your long-term East Asia marketing partner.` and `Mandapa, a Ritz-Carlton Reserve` (*"targeting Chinese &"*) with `#f3f3f1` surface cards, `#ffa500` accents, and `html.lenis { height:auto }`.
5. **Colophon & Global Directory Footer (<footer.wrap> — `https://www.mdscollective.com`)**:
   - Landmark `<footer class="wrap">` anchoring `MDS Collective · China Marketing` footer links (`About · Hotels & Hospitality · Tourism Boards · Airlines & Cruises · Higher Education`), copy *"East Asian Travelers"*, and `#a3a39e` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-mdscollective-com (MDS Collective · China Marketing Agency for Hotels & Tourism)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-mdscollective-com` (**MDS Collective · China Marketing Agency for Hotels & Tourism** — `https://www.mdscollective.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#101010` ink, `#ffa500` accent).
- **Identity & Domain Context**: Award-winning China marketing agency for luxury hotels and tourism brands. RedNote, WeChat, Douyin, KOLs and AI search. Formerly Metric D...
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#101010`, **Accent / Highlight**: `#ffa500`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#101010` primary typography and `#ffa500` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Instrument Serif` for display copy (`Luxury Marketing targeting Chinese &`) with `Helvetica Neue` and `SF Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1296px` container bounds (`gap: 56px`, padding `72px`) with `cubic-bezier(.77,0,.18,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-mdscollective-com` in your global stylesheet:

:root {
  /* MDS Collective · China Marketing Agency for Hotels & Tourism (www-mdscollective-com) — Live-Grounded CSS Variables */
  --bg: #fff; /* Canvas / Surface Token (www-mdscollective-com) */
  --bg2: #f3f3f1; /* Canvas / Surface Token (www-mdscollective-com) */
  --ink: #101010; /* Typography Ink Token (www-mdscollective-com) */
  --ink2: #5f5f5b; /* Typography Ink Token (www-mdscollective-com) */
  --ink3: #767671; /* Typography Ink Token (www-mdscollective-com) */
  --ink3-lg: #8e8e89; /* Typography Ink Token (www-mdscollective-com) */
  --rule: #a3a39e; /* Color / Atmospheric Token (www-mdscollective-com) */
  --line: #e3e3df; /* Color / Atmospheric Token (www-mdscollective-com) */
  --gold: #1c486d; /* Color / Atmospheric Token (www-mdscollective-com) */
  --navy: #1c486d; /* Layout / Spatial Grid Token (www-mdscollective-com) */
  --orange: #e6872d; /* Color / Atmospheric Token (www-mdscollective-com) */
  --serif: "Instrument Serif","PS Times","Times New Roman",Georgia,serif; /* Typography / Scale Token (www-mdscollective-com) */
  --sans: "Helvetica Neue",Helvetica,Arial,system-ui,sans-serif; /* Typography / Scale Token (www-mdscollective-com) */
  --r-lg: 24px; /* Dimension / Scale Token (www-mdscollective-com) */
  --hl: #e6872d52; /* Color / Atmospheric Token (www-mdscollective-com) */
  --www-mdscollectiv-bg: #ffffff; /* Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) (www-mdscollective-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#101010` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#f3f3f1` — grounded in `var(--bg2)` in `:root`
- **Interactive Accent / Highlight**: `#ffa500` — grounded in `.legal-doc a:hover { color: orange }` (`#ffa500`)
- **Secondary / Muted Copy**: `#8e8e89` — grounded in `var(--ink3-lg)` in `:root`
- **Structural Hairline Border**: `#a3a39e` — grounded in `var(--rule)` in `:root`
- **Variable Token (`--ink2`)**: `#5f5f5b` — grounded in `var(--ink2)` in `:root`
- **Variable Token (`--ink3`)**: `#767671` — grounded in `var(--ink3)` in `:root`
- **Variable Token (`--line`)**: `#e3e3df` — grounded in `var(--line)` in `:root`
- **Variable Token (`--gold`)**: `#1c486d` — grounded in `var(--gold)` in `:root`
- **Variable Token (`--orange`)**: `#e6872d` — grounded in `var(--orange)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1296px` (measured widest bounded `<section>` landmark width on `1440px` desktop)
- **Padding & Gutters**: `72px` lateral canvas padding with `56px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1296px`, `gap: 56px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `72px` horizontal padding
- **Media Queries**: `@media (width<=820px)`, `@media (width>=821px)`, `@media (width<=800px)`, `@media (hover:none),(prefers-reduced-motion:reduce)`
- **Corner Radii**: `999px`, `14px`, `10px`, `9px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Instrument Serif`
- **Body Font Stack**: `Helvetica Neue`
- **Monospace / Technical Font Stack**: `SF Mono`
- **H1 Display Rule**: live computed `h1` (`font-size: 141.12px`, `line-height: 143.942px`, `font-weight: 400`, `letter-spacing: -3.528px`); rule `h1` (`font-size: clamp(54px,9.8vw,156px)`, `line-height: 1.02`, `letter-spacing: -.025em`, `font-weight: 400`)
- **H2 Section Rule**: live computed `h2` (`font-size: 80.64px`, `line-height: 82.2528px`, `font-weight: 400`, `letter-spacing: -2.016px`); rule `h2` (`font-size: clamp(38px,5.6vw,88px)`, `line-height: 1.02`, `letter-spacing: -.025em`, `font-weight: 400`)
- **Body Copy Rule**: live computed `body` (`font-size: 15px`, `line-height: 22.5px`, `font-weight: 400`); rule `p` (`font-size: 15px`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 15px`, `line-height: 22.5px`, `font-weight: 400`); rule `small` (`font-size: .5em`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-mdscollective-com` (`MDS Collective · China Marketing Agency for Hotels & Tourism`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.lenis> — `www-mdscollective-com`)**:
   - DOM & Selectors: Landmark `<nav class="lenis">` (`1440x79px`) hosting `MDS Collective · China Marketing Age` navigation (`About · Hotels & Hospitality · Tourism Boards · Airlines & Cruises · Higher Education`), DOM attributes (`data-u="hello"`, `data-d="mdscollective.com"`, `data-src-sm="/video/hero-720.mp4"`, `data-src-lg="/video/hero-1080.mp4"`), and stylesheet rule `selection { color:fff;background:e6872d }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.lenis> — `www-mdscollective-com`)` (`www-mdscollective-com`) adapts across `@media (width<=820px)`, `@media (width>=821px)`, `@media (width<=800px)`, `@media (hover:none),(prefers-reduced-motion:reduce)` with `cubic-bezier(.77,0,.18,1)`, `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.2,.7,.2,1)` transitions and links `About · Hotels & Hospitality · Tourism Boards · Airlines & Cruises · Higher Education`.
2. **Hero Stage & Focal Lead (<section.brand-hero> — `Luxury Marketing targeting Chinese`)**:
   - DOM & Selectors: Landmark `<section class="brand-hero">` presenting display lead `Luxury Marketing targeting Chinese & East Asian T...` and copy excerpt *"ASIA'S TOP HOSPITALITY, TRAVEL AND TOURISM MARKETING COMPANY"* over `#ffffff` canvas and `#101010` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#ffffff` background with `#101010` headline `Luxury Marketing targeting Chinese & East Asian T...`.
3. **Primary Showcase & Content Grid (<section.hero> — `FIT travelers have evolved. AI is `)**:
   - DOM & Selectors: Landmark `<section class="hero wrap">` rendering section `FIT travelers have evolved. AI is now where their...` with copy *"Asia's top hospitality, travel and tourism marketing company"*, asset references (`favicon.ico`, `favicon-32.png`, `apple-touch-icon.png`, `hero-1080.mp4`), and grid rule `body { background:var(--bg);color:var(--ink);font-family:var(--sans);margin:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.hero> — `FIT travelers have evolved. AI is `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1296px`, `gap: 56px`) on desktop and Single-column vertical stack at `390px` viewport width with `72px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.hero-media> — `We are your long-term East Asia ma`)**:
   - DOM & Selectors: Landmark `<section class="hero-media wrap">` framing `We are your long-term East Asia marketing partner.` and `Mandapa, a Ritz-Carlton Reserve` (*"targeting Chinese &"*) with `#f3f3f1` surface cards, `#ffa500` accents, and `html.lenis { height:auto }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.hero-media> — `We are your long-term East Asia ma`)` uses `999px`, `14px`, `10px`, `9px` radii, `#ffa500` highlights, and assets (favicon.ico, favicon-32.png, apple-touch-icon.png).
5. **Colophon & Global Directory Footer (<footer.wrap> — `https://www.mdscollective.com`)**:
   - DOM & Selectors: Landmark `<footer class="wrap">` anchoring `MDS Collective · China Marketing` footer links (`About · Hotels & Hospitality · Tourism Boards · Airlines & Cruises · Higher Education`), copy *"East Asian Travelers"*, and `#a3a39e` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.wrap> — `https://www.mdscollective.com`)` aligns to `1296px` (measured widest bounded `<section>` landmark width on `1440px` desktop) with `72px` lateral canvas padding with `56px` grid gap and attributes (data-u="hello", data-d="mdscollective.com", data-src-sm="/video/hero-720.mp4").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"ASIA'S TOP HOSPITALITY, TRAVEL AND TOURISM MARKETING COMPANY"*
- Copy Excerpt 2: *"Asia's top hospitality, travel and tourism marketing company"*
- Copy Excerpt 3: *"targeting Chinese &"*
- Copy Excerpt 4: *"East Asian Travelers"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.77,0,.18,1)`, `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.2,.7,.2,1)`
- **Extracted Stylesheet Rules (`www-mdscollective-com`)**:
- `selection { color:fff;background:e6872d }`
- `body { background:var(--bg);color:var(--ink);font-family:var(--sans);margin:0 }`
- `html.lenis { height:auto }`
- `.lenis.lenis-smooth { scroll-behavior:auto }`
- `img { max-width:100%;height:auto;display:block }`
- **Per-Selector Transition Rules**:
- **Selector `#loader`**: `transition: opacity .8s,visibility .8s` extracted from `www-mdscollective-com` stylesheet.
- **Selector `#loader .bar i`**: `transition: width .1s linear` extracted from `www-mdscollective-com` stylesheet.
- **Selector `nav`**: `transition: background .45s,color .45s,padding .45s,border-color .45s` extracted from `www-mdscollective-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.77,0,.18,1)`)**: Governs interactive state transitions across `<nav.lenis>` and `<section.hero>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-mdscollective-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
