---
title: "UI Prompt Blueprint: vadimcarazan-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "vadimcarazan-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: native
desktop_keyframes: 1
subpages_crawled: 0
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#0a0a0b` / `#f2f2f2`)"
---

# UI Design System & Master Generation Blueprint: vadimcarazan-com

> **Vadim Carazan, Creative Director** (https://vadimcarazan.com/) — Vadim Carazan, creative director and founder of WeGrow. Fourteen years of brand identities, websites and products for founders.

![Desktop Journey Filmstrip (1280x828)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x872)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Vadim Carazan, Creative Director** (`https://vadimcarazan.com/`). Vadim Carazan, creative director and founder of WeGrow. Fourteen years of brand identities, websites and products for founders.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#0a0a0b` / `#f2f2f2`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#0a0a0b` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#f2f2f2` primary typography and `#f2f2f2` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Editorial Old Italic` for display copy (`Vadim Carazan, Creative Director`) with `Inter Tight`.
  - **Calibrated Spatial Grid & Motion**: Combines `1382px` container bounds (`gap: 8px`, padding `16px`) with `cubic-bezier(.22,1,.36,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×828px` (`assets/desktop-journey.webp`, `1` keyframes up to `y=0px` / doc `900px`), Mobile `390×872px` (`assets/mobile-journey.webp`, `1` keyframes).
- **Master Container Bounds**: `1382px` (measured widest bounded `<section>` landmark width on `1440px` desktop).
- **Canvas Lateral Padding & Spacing**: `16px` lateral canvas padding with `8px` grid gap.
- **Border Radius Scale**: `18px`, `999px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1382px`, `gap: 8px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `16px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:600px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0a0a0b` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f2f2f2` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0a0a0b` | transparent/inherited card surface over live computed `body` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#f2f2f2` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#f2f2f2` | secondary opacity step of live computed `h1` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#272728` | `var(--line)` in `:root` (`rgba(255, 255, 255, 0.12)`) |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#0a0a0b` | Canvas / Surface Token |
| `--ink` | `#f2f2f2` | Typography Ink Token |
| `--mute` | `rgba(242, 242, 242, 0.55)` | Color / Atmospheric Token |
| `--line` | `rgba(255, 255, 255, 0.12)` | Color / Atmospheric Token |
| `--serif` | `"Editorial Old Italic", "Instrument Serif", "Times New Roman", serif` | Typography / Scale Token |
| `--sans` | `"Inter Tight", "Inter", -apple-system, "Helvetica Neue", Arial, sans-serif` | Typography / Scale Token |
| `--pad` | `clamp(16px, 2vw, 32px)` | Layout / Spatial Grid Token |
| `--box-open` | `clamp(460px, 42vw, 780px)` | Dimension / Scale Token |
| `--ease` | `cubic-bezier(0.22, 1, 0.36, 1)` | Motion / Easing Token |
| `--vadimcarazan-com-bg` | `#0a0a0b` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--vadimcarazan-com-ink` | `#f2f2f2` | Primary Typography Ink (computed-derived) |
| `--vadimcarazan-com-surface` | `#0a0a0b` | Surface Substrate (computed-derived) |
| `--vadimcarazan-com-accent` | `#f2f2f2` | Interactive Accent (computed-derived) |
| `--vadimcarazan-com-muted` | `#f2f2f2` | Secondary Ink (computed-derived) |
| `--vadimcarazan-com-border` | `#272728` | Structural Border (computed-derived) |
| `--vadimcarazan-com-container` | `1382px` | Container Bound (computed-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Editorial Old Italic`.
- **Primary Body Stack**: `Inter Tight`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 0px`, `line-height: 0px`, `font-weight: 400`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 33.12px`, `line-height: 35.7696px`, `font-weight: 400`, `letter-spacing: -0.4968px`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(0.22,1,0.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `#vc-consent`**: `transition: opacity .35s ease,transform .45s cubic-bezier(.22,1,.36,1)` extracted from `vadimcarazan-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<header.topbar>` and `<section.view>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `900px`, deepest scrollY reached `0px` across `1` desktop keyframes).
- **Detected Scroll / Motion Libraries**: Native browser scroll / standard CSS transitions.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Vadim Carazan, Creative Director           │
│ ====================================================================== │
│ [ <header.topbar> (1382x41px)         | Overview · Index · Archive · ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero> (w=1440px)                              | │
│ | H1: Vadim Carazan, Creative Director                               | │
│ | Substrate: #0a0a0b | Ink: #f2f2f2 | Accent: #f2f2f2                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.view>) max-w: 1382px                       | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Featured Work & Interactive  |  | Technical Architecture & Nar | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.v-selected>) — Global Directory & Co       | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.logo>       ) | https://vadimcarazan.com/            │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 8px)        │
│ ====================================================================== │
│ [ HEADER BAR (<header.topbar>         ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.hero>) — 390px Vertical Lead                  | │
│ | H1: Vadim Carazan, Creative Director                               | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.view>) — 1-Col Stack                      | │
│ | [ Item 1: Featured Work & Interactive Showcase                   ] | │
│ | [ Item 2: Technical Architecture & Narrative                     ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.v-selected>) — 1-Col (Global Directory &)   | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.logo>       ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.topbar> — `vadimcarazan-com`)**:
   - Landmark `<header class="topbar">` (`1382x41px`) hosting `Vadim Carazan, Creative Director` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-engine="three.js r169"`, `data-go="about"`, `data-go="about"`, `data-go="selected"`), and stylesheet rule `vc-consent.in { opacity:1;transform:none }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Vadim Carazan, Creative Director`)**:
   - Landmark `<section class="hero">` presenting display lead `Vadim Carazan, Creative Director` and copy excerpt *"Fourteen years of brand identities, websites and products for fou"* over `#0a0a0b` canvas and `#f2f2f2` ink.
3. **Primary Showcase & Content Grid (<section.view> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="view v-project">` rendering section `Featured Work & Interactive Showcase` with copy *"Creative Director, WeGrow"*, asset references (`clarity.js`, `ywzmdkawk4`, `track.js`, `favicon.ico`), and grid rule `vc-consent.out { opacity:0;transform:translateY(14px) }`.
4. **Interactive Detail & Feature Matrix (<section.v-selected> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="view v-selected">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Cluj-Napoca, Romania ( 19:06 )"*) with `#0a0a0b` surface cards, `#f2f2f2` accents, and `vc-consent p { margin:0 0 12px;color:rgba(242,242,242,.82) }`.
5. **Colophon & Global Directory Footer (<footer.logo> — `https://vadimcarazan.com/`)**:
   - Landmark `<footer class="logo">` anchoring `Vadim Carazan, Creative Director` footer links (`Overview · Index · Archive · About · Contact`), copy *"Selected , Work , About , Contact"*, and `#272728` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `#intro` · sticky/fixed elements: `3`

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: vadimcarazan-com (Vadim Carazan, Creative Director)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `vadimcarazan-com` (**Vadim Carazan, Creative Director** — `https://vadimcarazan.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0a0a0b` / `#f2f2f2`).
- **Identity & Domain Context**: Vadim Carazan, creative director and founder of WeGrow. Fourteen years of brand identities, websites and products for founders.
- **Primary Substrate**: `#0a0a0b` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#f2f2f2`, **Accent / Highlight**: `#f2f2f2`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#0a0a0b` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#f2f2f2` primary typography and `#f2f2f2` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Editorial Old Italic` for display copy (`Vadim Carazan, Creative Director`) with `Inter Tight`.
  - **Calibrated Spatial Grid & Motion**: Combines `1382px` container bounds (`gap: 8px`, padding `16px`) with `cubic-bezier(.22,1,.36,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `vadimcarazan-com` in your global stylesheet:

:root {
  /* Vadim Carazan, Creative Director (vadimcarazan-com) — Live-Grounded CSS Variables */
  --bg: #0a0a0b; /* Canvas / Surface Token (vadimcarazan-com) */
  --ink: #f2f2f2; /* Typography Ink Token (vadimcarazan-com) */
  --mute: rgba(242, 242, 242, 0.55); /* Color / Atmospheric Token (vadimcarazan-com) */
  --line: rgba(255, 255, 255, 0.12); /* Color / Atmospheric Token (vadimcarazan-com) */
  --serif: "Editorial Old Italic", "Instrument Serif", "Times New Roman", serif; /* Typography / Scale Token (vadimcarazan-com) */
  --sans: "Inter Tight", "Inter", -apple-system, "Helvetica Neue", Arial, sans-serif; /* Typography / Scale Token (vadimcarazan-com) */
  --pad: clamp(16px, 2vw, 32px); /* Layout / Spatial Grid Token (vadimcarazan-com) */
  --box-open: clamp(460px, 42vw, 780px); /* Dimension / Scale Token (vadimcarazan-com) */
  --ease: cubic-bezier(0.22, 1, 0.36, 1); /* Motion / Easing Token (vadimcarazan-com) */
  --vadimcarazan-com-bg: #0a0a0b; /* Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) (vadimcarazan-com) */
  --vadimcarazan-com-ink: #f2f2f2; /* Primary Typography Ink (computed-derived) (vadimcarazan-com) */
  --vadimcarazan-com-surface: #0a0a0b; /* Surface Substrate (computed-derived) (vadimcarazan-com) */
  --vadimcarazan-com-accent: #f2f2f2; /* Interactive Accent (computed-derived) (vadimcarazan-com) */
  --vadimcarazan-com-muted: #f2f2f2; /* Secondary Ink (computed-derived) (vadimcarazan-com) */
  --vadimcarazan-com-border: #272728; /* Structural Border (computed-derived) (vadimcarazan-com) */
  --vadimcarazan-com-container: 1382px; /* Container Bound (computed-derived) (vadimcarazan-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#0a0a0b` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#f2f2f2` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#0a0a0b` — grounded in transparent/inherited card surface over live computed `body` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#f2f2f2` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Secondary / Muted Copy**: `#f2f2f2` — grounded in secondary opacity step of live computed `h1` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#272728` — grounded in `var(--line)` in `:root` (`rgba(255, 255, 255, 0.12)`)

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×828px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×872px` (full-page live capture (872px), `390px` standard mobile width).
- **Container Max-Width**: `1382px` (measured widest bounded `<section>` landmark width on `1440px` desktop)
- **Padding & Gutters**: `16px` lateral canvas padding with `8px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1382px`, `gap: 8px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `16px` horizontal padding
- **Media Queries**: `@media (max-width:600px)`
- **Corner Radii**: `18px`, `999px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Editorial Old Italic`
- **Body Font Stack**: `Inter Tight`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 0px`, `line-height: 0px`, `font-weight: 400`)
- **H2 Section Rule**: live computed `h2` (`font-size: 33.12px`, `line-height: 35.7696px`, `font-weight: 400`, `letter-spacing: -0.4968px`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `vadimcarazan-com` (`Vadim Carazan, Creative Director`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.topbar> — `vadimcarazan-com`)**:
   - DOM & Selectors: Landmark `<header class="topbar">` (`1382x41px`) hosting `Vadim Carazan, Creative Director` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-engine="three.js r169"`, `data-go="about"`, `data-go="about"`, `data-go="selected"`), and stylesheet rule `vc-consent.in { opacity:1;transform:none }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.topbar> — `vadimcarazan-com`)` (`vadimcarazan-com`) adapts across `@media (max-width:600px)` with `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(0.22,1,0.36,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.hero> — `Vadim Carazan, Creative Director`)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `Vadim Carazan, Creative Director` and copy excerpt *"Fourteen years of brand identities, websites and products for fou"* over `#0a0a0b` canvas and `#f2f2f2` ink.
   - Responsive Contract: Hero stage (`1280×828px` desktop / `390×872px` mobile) sets `#0a0a0b` background with `#f2f2f2` headline `Vadim Carazan, Creative Director`.
3. **Primary Showcase & Content Grid (<section.view> — `Featured Work & Interactive Showca`)**:
   - DOM & Selectors: Landmark `<section class="view v-project">` rendering section `Featured Work & Interactive Showcase` with copy *"Creative Director, WeGrow"*, asset references (`clarity.js`, `ywzmdkawk4`, `track.js`, `favicon.ico`), and grid rule `vc-consent.out { opacity:0;transform:translateY(14px) }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.view> — `Featured Work & Interactive Showca`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1382px`, `gap: 8px`) on desktop and Single-column vertical stack at `390px` viewport width with `16px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.v-selected> — `Technical Architecture & Narrative`)**:
   - DOM & Selectors: Landmark `<section class="view v-selected">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Cluj-Napoca, Romania ( 19:06 )"*) with `#0a0a0b` surface cards, `#f2f2f2` accents, and `vc-consent p { margin:0 0 12px;color:rgba(242,242,242,.82) }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.v-selected> — `Technical Architecture & Narrative`)` uses `18px`, `999px` radii, `#f2f2f2` highlights, and assets (clarity.js, ywzmdkawk4, track.js).
5. **Colophon & Global Directory Footer (<footer.logo> — `https://vadimcarazan.com/`)**:
   - DOM & Selectors: Landmark `<footer class="logo">` anchoring `Vadim Carazan, Creative Director` footer links (`Overview · Index · Archive · About · Contact`), copy *"Selected , Work , About , Contact"*, and `#272728` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.logo> — `https://vadimcarazan.com/`)` aligns to `1382px` (measured widest bounded `<section>` landmark width on `1440px` desktop) with `16px` lateral canvas padding with `8px` grid gap and attributes (data-engine="three.js r169", data-go="about", data-go="about").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Fourteen years of brand identities, websites and products for founders, from first..."*
- Copy Excerpt 2: *"Creative Director, WeGrow"*
- Copy Excerpt 3: *"Cluj-Napoca, Romania ( 19:06 )"*
- Copy Excerpt 4: *"Selected , Work , About , Contact"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(0.22,1,0.36,1)`
- **Extracted Stylesheet Rules (`vadimcarazan-com`)**:
- `vc-consent.in { opacity:1;transform:none }`
- `vc-consent.out { opacity:0;transform:translateY(14px) }`
- `vc-consent p { margin:0 0 12px;color:rgba(242,242,242,.82) }`
- `vc-consent a { color:f2f2f2;text-underline-offset:3px }`
- `.vc-consent-btns { display:flex;gap:8px;justify-content:flex-end }`
- **Per-Selector Transition Rules**:
- **Selector `#vc-consent`**: `transition: opacity .35s ease,transform .45s cubic-bezier(.22,1,.36,1)` extracted from `vadimcarazan-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<header.topbar>` and `<section.view>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `900px` across 1 distinct viewport chapters.
- **Vertical Chapter Sequence**: #intro (0%).

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `vadimcarazan-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | #intro | `3` | [desktop-step-01.webp](assets/desktop-step-01.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | Viewport | [mobile-step-01.webp](assets/mobile-step-01.webp) |

