---
title: "UI Prompt Blueprint: wiro-ae"
date: 2026-11-23
captured_at: 2026-11-23
target: "wiro-ae"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier2_webgl
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#efacd4`)"
---

# UI Design System & Master Generation Blueprint: wiro-ae

> **Wiro · Operating System for All Agencies** (https://wiro.ae/) — Run your whole agency in one place: projects, clients, invoices, social scheduling, ads, influencers and PR. The agency operating system...

![Desktop Viewport Capture (1440x900)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Wiro · Operating System for All Agencies** (`https://wiro.ae/`). Run your whole agency in one place: projects, clients, invoices, social scheduling, ads, influencers and PR. The agency operating system...
- **Capture Provenance**: Live browser capture (`tier2_webgl`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#efacd4`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#f6f0e4` primary typography and `#efacd4` accents.
  - **Grounded Typographic Hierarchy**: Pairs `__bricolage_29b70e` for display copy (`Organize Your Chaos`) with `__dmSans_224c19` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1536px` container bounds (`gap: 4px`, padding `48px`) with `cubic-bezier(.34,1.56,.64,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x844)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×900px` (`assets/desktop.png`, single-viewport 100vh live capture (900px)), Mobile `390×844px` (`assets/mobile.png`, single-viewport 100vh live capture (844px)).
- **Master Container Bounds**: `1536px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `48px` lateral canvas padding with `4px` grid gap.
- **Border Radius Scale**: `10px`, `var(--lp-radius-lg)`, `24%`, `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1536px`, `gap: 4px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `48px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (max-width:900px)`, `@media (max-width:1100px)`, `@media (min-width:761px) and (max-width:1100px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f6f0e4` | live computed `p` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#10100f` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#efacd4` | `var(--c-inverse-accent)` in `:root` |
| **Secondary / Muted Copy** | `#b8b5ac` | `var(--c-inverse-muted)` in `:root` |
| **Structural Hairline Border** | `#222220` | `var(--c-inverse-border)` in `:root` |
| **Variable Token (`--wiro-canvas`)** | `#f6efe3` | `var(--wiro-canvas)` in `:root` |
| **Variable Token (`--wiro-surface-2`)** | `#ece5da` | `var(--wiro-surface-2)` in `:root` |
| **Variable Token (`--wiro-yellow`)** | `#f6d94e` | `var(--wiro-yellow)` in `:root` |
| **Variable Token (`--wiro-sage`)** | `#9caf63` | `var(--wiro-sage)` in `:root` |
| **Variable Token (`--wiro-blue`)** | `#a9c5e9` | `var(--wiro-blue)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-heading` | `var(--font-bricolage),"Bricolage Grotesque",sans-serif` | Typography Ink Token |
| `--font-ui` | `var(--font-dmsans),"DM Sans",Arial,Helvetica,sans-serif` | Typography / Scale Token |
| `--solar-stroke-width` | `2.5` | Layout / Spatial Grid Token |
| `--wiro-ink` | `#10100f` | Typography Ink Token |
| `--wiro-muted` | `rgba(16,16,15,.52)` | Color / Atmospheric Token |
| `--wiro-canvas` | `#f6efe3` | Canvas / Surface Token |
| `--wiro-surface` | `#f6efe3` | Canvas / Surface Token |
| `--wiro-surface-2` | `#ece5da` | Canvas / Surface Token |
| `--wiro-border` | `rgba(16,16,15,.12)` | Elevation / Border Token |
| `--wiro-pink` | `#efacd4` | Typography Ink Token |
| `--wiro-yellow` | `#f6d94e` | Color / Atmospheric Token |
| `--wiro-sage` | `#9caf63` | Color / Atmospheric Token |
| `--wiro-blue` | `#a9c5e9` | Color / Atmospheric Token |
| `--wiro-radius-lg` | `18px` | Elevation / Border Token |
| `--wiro-radius-md` | `12px` | Elevation / Border Token |
| `--wiro-radius-sm` | `10px` | Elevation / Border Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `__bricolage_29b70e`.
- **Primary Body Stack**: `__dmSans_224c19`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 62px`, `line-height: 62px`, `font-weight: 700`); rule `h1` (`font-size: clamp(27px,4.4vw,62px)`, `line-height: 1`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 158.4px`, `line-height: 148.896px`, `font-weight: 700`); rule `h2` (`font-size: clamp(82px,11vw,220px)`, `line-height: .94`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: clamp(16px,1.2vw,19px)`, `line-height: 1.5`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.34,1.56,.64,1)`, `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.lp-morph-btn`**: `transition: transform .2s ease` extracted from `wiro-ae` stylesheet.
- **Selector `.lp-btn-square`**: `transition: opacity .2s ease,transform .22s ease,border-radius .22s ease` extracted from `wiro-ae` stylesheet.
- **Selector `.lp-morph-btn .lp-flower`**: `transition: opacity .18s ease,transform .26s cubic-bezier(.34,1.56,.64,1)` extracted from `wiro-ae` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.34,1.56,.64,1)`)**: Governs interactive state transitions across `<header.mkt-header>` and `<section.lp-hero>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Wiro · Operating System for All Agencies   │
│ ====================================================================== │
│ [ <header.mkt-header> (1440x68px)     | Platform · Influencer · Duba ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.wi> (w=1440px)                                | │
│ | H1: Organize Your Chaos                                            | │
│ | Substrate: #000000 | Ink: #f6f0e4 | Accent: #efacd4                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.lp-hero>) max-w: 1536px                    | │
│ | +------------------------------+  +------------------------------+ | │
│ | | One system for every page yo |  | Projects                     | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.lp-section>) — Clients                     | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.lp-footer>  ) | https://wiro.ae/                     │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 4px)        │
│ ====================================================================== │
│ [ HEADER BAR (<header.mkt-header>     ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.wi>) — 390px Vertical Lead                    | │
│ | H1: Organize Your Chaos                                            | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.lp-hero>) — 1-Col Stack                   | │
│ | [ Item 1: One system for every page your agency runs.            ] | │
│ | [ Item 2: Projects                                               ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.lp-section>) — 1-Col (Clients)              | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.lp-footer>  ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.mkt-header> — `wiro-ae`)**:
   - Landmark `<header class="mkt-header">` (`1440x68px`) hosting `Wiro · Operating System for All Agen` navigation (`Platform · Influencer · Dubai and the UAE · Articles · For creators`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `html { scroll-behavior:smooth }`.
2. **Hero Stage & Focal Lead (<section.wi> — `Organize Your Chaos`)**:
   - Landmark `<section class="wi">` presenting display lead `Organize Your Chaos` and copy excerpt *"The operating system for modern agencies."* over `#000000` canvas and `#f6f0e4` ink.
3. **Primary Showcase & Content Grid (<section.lp-hero> — `One system for every page your age`)**:
   - Landmark `<section class="lp-hero">` rendering section `One system for every page your agency runs.` with copy *"Fifteen modules, one shared record of the work. Nothing lives in "*, asset references (`intro-arrow.webp`, `intro-window-2.webp`, `logo-icon.svg`, `landscape-bg.webp`), and grid rule `.lp-page { position:relative;min-height:100vh;color:var(--lp-ink);font-family:var(-... }`.
4. **Interactive Detail & Feature Matrix (<section.lp-section> — `Projects`)**:
   - Landmark `<section class="lp-section lp-pages">` framing `Projects` and `Clients` (*"Progress 7 of 9 8 of 9"*) with `#10100f` surface cards, `#efacd4` accents, and `.lp-page strong { font-family:var(--lp-heading);font-weight:700;letter-spacing:0 }`.
5. **Colophon & Global Directory Footer (<footer.lp-footer> — `https://wiro.ae/`)**:
   - Landmark `<footer class="lp-footer lp-footer-scatter">` anchoring `Wiro · Operating System for All ` footer links (`Platform · Influencer · Dubai and the UAE · Articles · For creators`), copy *"Briefs, timelines, owners and approvals moving through one s"*, and `#222220` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: wiro-ae (Wiro · Operating System for All Agencies)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `wiro-ae` (**Wiro · Operating System for All Agencies** — `https://wiro.ae/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#efacd4`).
- **Identity & Domain Context**: Run your whole agency in one place: projects, clients, invoices, social scheduling, ads, influencers and PR. The agency operating system...
- **Primary Substrate**: `#000000` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#f6f0e4`, **Accent / Highlight**: `#efacd4`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#f6f0e4` primary typography and `#efacd4` accents.
  - **Grounded Typographic Hierarchy**: Pairs `__bricolage_29b70e` for display copy (`Organize Your Chaos`) with `__dmSans_224c19` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1536px` container bounds (`gap: 4px`, padding `48px`) with `cubic-bezier(.34,1.56,.64,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `wiro-ae` in your global stylesheet:

:root {
  /* Wiro · Operating System for All Agencies (wiro-ae) — Live-Grounded CSS Variables */
  --font-heading: var(--font-bricolage),"Bricolage Grotesque",sans-serif; /* Typography Ink Token (wiro-ae) */
  --font-ui: var(--font-dmsans),"DM Sans",Arial,Helvetica,sans-serif; /* Typography / Scale Token (wiro-ae) */
  --solar-stroke-width: 2.5; /* Layout / Spatial Grid Token (wiro-ae) */
  --wiro-ink: #10100f; /* Typography Ink Token (wiro-ae) */
  --wiro-muted: rgba(16,16,15,.52); /* Color / Atmospheric Token (wiro-ae) */
  --wiro-canvas: #f6efe3; /* Canvas / Surface Token (wiro-ae) */
  --wiro-surface: #f6efe3; /* Canvas / Surface Token (wiro-ae) */
  --wiro-surface-2: #ece5da; /* Canvas / Surface Token (wiro-ae) */
  --wiro-border: rgba(16,16,15,.12); /* Elevation / Border Token (wiro-ae) */
  --wiro-pink: #efacd4; /* Typography Ink Token (wiro-ae) */
  --wiro-yellow: #f6d94e; /* Color / Atmospheric Token (wiro-ae) */
  --wiro-sage: #9caf63; /* Color / Atmospheric Token (wiro-ae) */
  --wiro-blue: #a9c5e9; /* Color / Atmospheric Token (wiro-ae) */
  --wiro-radius-lg: 18px; /* Elevation / Border Token (wiro-ae) */
  --wiro-radius-md: 12px; /* Elevation / Border Token (wiro-ae) */
  --wiro-radius-sm: 10px; /* Elevation / Border Token (wiro-ae) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000000` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#f6f0e4` — grounded in live computed `p` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#10100f` — grounded in live computed `button` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#efacd4` — grounded in `var(--c-inverse-accent)` in `:root`
- **Secondary / Muted Copy**: `#b8b5ac` — grounded in `var(--c-inverse-muted)` in `:root`
- **Structural Hairline Border**: `#222220` — grounded in `var(--c-inverse-border)` in `:root`
- **Variable Token (`--wiro-canvas`)**: `#f6efe3` — grounded in `var(--wiro-canvas)` in `:root`
- **Variable Token (`--wiro-surface-2`)**: `#ece5da` — grounded in `var(--wiro-surface-2)` in `:root`
- **Variable Token (`--wiro-yellow`)**: `#f6d94e` — grounded in `var(--wiro-yellow)` in `:root`
- **Variable Token (`--wiro-sage`)**: `#9caf63` — grounded in `var(--wiro-sage)` in `:root`
- **Variable Token (`--wiro-blue`)**: `#a9c5e9` — grounded in `var(--wiro-blue)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×900px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×844px` (single-viewport 100vh live capture (844px), `390px` standard mobile width).
- **Container Max-Width**: `1536px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `48px` lateral canvas padding with `4px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1536px`, `gap: 4px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `48px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (max-width:900px)`, `@media (max-width:1100px)`, `@media (min-width:761px) and (max-width:1100px)`
- **Corner Radii**: `10px`, `var(--lp-radius-lg)`, `24%`, `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `__bricolage_29b70e`
- **Body Font Stack**: `__dmSans_224c19`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: live computed `h1` (`font-size: 62px`, `line-height: 62px`, `font-weight: 700`); rule `h1` (`font-size: clamp(27px,4.4vw,62px)`, `line-height: 1`)
- **H2 Section Rule**: live computed `h2` (`font-size: 158.4px`, `line-height: 148.896px`, `font-weight: 700`); rule `h2` (`font-size: clamp(82px,11vw,220px)`, `line-height: .94`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: clamp(16px,1.2vw,19px)`, `line-height: 1.5`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `wiro-ae` (`Wiro · Operating System for All Agencies`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.mkt-header> — `wiro-ae`)**:
   - DOM & Selectors: Landmark `<header class="mkt-header">` (`1440x68px`) hosting `Wiro · Operating System for All Agen` navigation (`Platform · Influencer · Dubai and the UAE · Articles · For creators`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `html { scroll-behavior:smooth }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.mkt-header> — `wiro-ae`)` (`wiro-ae`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (max-width:900px)`, `@media (max-width:1100px)`, `@media (min-width:761px) and (max-width:1100px)` with `cubic-bezier(.34,1.56,.64,1)`, `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Platform · Influencer · Dubai and the UAE · Articles · For creators`.
2. **Hero Stage & Focal Lead (<section.wi> — `Organize Your Chaos`)**:
   - DOM & Selectors: Landmark `<section class="wi">` presenting display lead `Organize Your Chaos` and copy excerpt *"The operating system for modern agencies."* over `#000000` canvas and `#f6f0e4` ink.
   - Responsive Contract: Hero stage (`1440×900px` desktop / `390×844px` mobile) sets `#000000` background with `#f6f0e4` headline `Organize Your Chaos`.
3. **Primary Showcase & Content Grid (<section.lp-hero> — `One system for every page your age`)**:
   - DOM & Selectors: Landmark `<section class="lp-hero">` rendering section `One system for every page your agency runs.` with copy *"Fifteen modules, one shared record of the work. Nothing lives in "*, asset references (`intro-arrow.webp`, `intro-window-2.webp`, `logo-icon.svg`, `landscape-bg.webp`), and grid rule `.lp-page { position:relative;min-height:100vh;color:var(--lp-ink);font-family:var(-... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.lp-hero> — `One system for every page your age`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1536px`, `gap: 4px`) on desktop and Single-column vertical stack at `390px` viewport width with `48px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.lp-section> — `Projects`)**:
   - DOM & Selectors: Landmark `<section class="lp-section lp-pages">` framing `Projects` and `Clients` (*"Progress 7 of 9 8 of 9"*) with `#10100f` surface cards, `#efacd4` accents, and `.lp-page strong { font-family:var(--lp-heading);font-weight:700;letter-spacing:0 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.lp-section> — `Projects`)` uses `10px`, `var(--lp-radius-lg)`, `24%`, `50%` radii, `#efacd4` highlights, and assets (intro-arrow.webp, intro-window-2.webp, logo-icon.svg).
5. **Colophon & Global Directory Footer (<footer.lp-footer> — `https://wiro.ae/`)**:
   - DOM & Selectors: Landmark `<footer class="lp-footer lp-footer-scatter">` anchoring `Wiro · Operating System for All ` footer links (`Platform · Influencer · Dubai and the UAE · Articles · For creators`), copy *"Briefs, timelines, owners and approvals moving through one s"*, and `#222220` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.lp-footer> — `https://wiro.ae/`)` aligns to `1536px` (non-`@media` desktop container stylesheet rule) with `48px` lateral canvas padding with `4px` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"The operating system for modern agencies."*
- Copy Excerpt 2: *"Fifteen modules, one shared record of the work. Nothing lives in its own silo."*
- Copy Excerpt 3: *"Progress 7 of 9 8 of 9"*
- Copy Excerpt 4: *"Briefs, timelines, owners and approvals moving through one shared board."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.34,1.56,.64,1)`, `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`wiro-ae`)**:
- `html { scroll-behavior:smooth }`
- `.lp-page { position:relative;min-height:100vh;color:var(--lp-ink);font-family:var(-... }`
- `.lp-page strong { font-family:var(--lp-heading);font-weight:700;letter-spacing:0 }`
- `.lp-stars { position:absolute;inset:0;z-index:1;overflow:hidden;pointer-events:none }`
- `.lp-stars-canvas { display:block;width:100%;height:100% }`
- **Per-Selector Transition Rules**:
- **Selector `.lp-morph-btn`**: `transition: transform .2s ease` extracted from `wiro-ae` stylesheet.
- **Selector `.lp-btn-square`**: `transition: opacity .2s ease,transform .22s ease,border-radius .22s ease` extracted from `wiro-ae` stylesheet.
- **Selector `.lp-morph-btn .lp-flower`**: `transition: opacity .18s ease,transform .26s cubic-bezier(.34,1.56,.64,1)` extracted from `wiro-ae` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.34,1.56,.64,1)`)**: Governs interactive state transitions across `<header.mkt-header>` and `<section.lp-hero>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `wiro-ae`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
