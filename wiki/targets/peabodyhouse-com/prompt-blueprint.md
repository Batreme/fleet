---
title: "UI Prompt Blueprint: peabodyhouse-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "peabodyhouse-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: native
desktop_keyframes: 2
subpages_crawled: 0
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#faf6f3` / `#0000ff`)"
---

# UI Design System & Master Generation Blueprint: peabodyhouse-com

> **Peabody House • Digital Brand World Implementation Studio** (https://peabodyhouse.com) — Peabody House is a Milwaukee-based digital studio that turns brand aspirations into elevated, scalable design systems. Led by human expre...

![Desktop Journey Filmstrip (1280x1656)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Peabody House • Digital Brand World Implementation Studio** (`https://peabodyhouse.com`). Peabody House is a Milwaukee-based digital studio that turns brand aspirations into elevated, scalable design systems. Led by human expre...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#faf6f3` / `#0000ff`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#faf6f3` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#26211e` primary typography and `#0000ff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Peabody House` for display copy (`Peabody House is a digital brand wor`) with `PP Neue Montreal` and `SpotifyMixMono`.
  - **Calibrated Spatial Grid & Motion**: Combines `960px` container bounds (`gap: .5rem`, padding `.25rem`) with `cubic-bezier(.45,0,.55,1)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×1656px` (`assets/desktop-journey.webp`, `2` keyframes up to `y=0px` / doc `6542px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `960px` (measured widest bounded `<section>` landmark width on `1440px` desktop).
- **Canvas Lateral Padding & Spacing**: `.25rem` lateral canvas padding with `.5rem` grid gap.
- **Border Radius Scale**: `1px`, `50%`, `99px`, `12px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 960px`, `gap: .5rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.25rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width: 48rem)`, `@media (prefers-reduced-motion: reduce)`, `@media (min-width: 64rem)`, `@media (max-width: 63.99rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#faf6f3` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#26211e` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#c5f0c9` | `var(--encore-verified-badge-background)` in `:root` |
| **Interactive Accent / Highlight** | `#0000ff` | `.cta:hover .cta-line { color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#f3727f` | `var(--text-negative)` in `:root` |
| **Structural Hairline Border** | `#008080` | `.cta:before { border-top-color: #008080 }` |
| **Variable Token (`--color-accent`)** | `#dc942f` | `var(--color-accent)` in `:root` |
| **Variable Token (`--color-blue`)** | `#517bb3` | `var(--color-blue)` in `:root` |
| **Variable Token (`--color-teal`)** | `#71c7b7` | `var(--color-teal)` in `:root` |
| **Variable Token (`--color-red`)** | `#a24250` | `var(--color-red)` in `:root` |
| **Variable Token (`--color-green`)** | `#455330` | `var(--color-green)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-primary` | `#26211E` | Brand / Palette Token |
| `--color-secondary` | `#FAF6F3` | Brand / Palette Token |
| `--color-accent` | `#DC942F` | Brand / Palette Token |
| `--color-background` | `#FAF6F3` | Canvas / Surface Token |
| `--color-text` | `#26211E` | Typography Ink Token |
| `--color-white` | `#FAF6F3` | Canvas / Surface Token |
| `--color-black` | `#26211E` | Canvas / Surface Token |
| `--color-black-20` | `rgba(38, 33, 30, .2)` | Canvas / Surface Token |
| `--color-orange` | `#DC942F` | Brand / Palette Token |
| `--color-blue` | `#517BB3` | Brand / Palette Token |
| `--color-teal` | `#71C7B7` | Brand / Palette Token |
| `--color-red` | `#A24250` | Brand / Palette Token |
| `--color-green` | `#455330` | Brand / Palette Token |
| `--font-heading` | `"Peabody House", sans-serif` | Typography Ink Token |
| `--font-body` | `"PP Neue Montreal", sans-serif` | Typography / Scale Token |
| `--font-size-base` | `16px` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Peabody House`.
- **Primary Body Stack**: `PP Neue Montreal`.
- **Technical / Metadata Stack**: `SpotifyMixMono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 68px`, `line-height: 76.5px`, `font-weight: 400`); CSS variables `--text-link-standalone-display: block`, `--encore-overlay-trigger-display: block`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 60.48px`, `line-height: 63.504px`, `font-weight: 400`); rule `,.h2` (`font-size: clamp(2.0257rem,1.4626rem + 2...`, `line-height: 1.125`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-body: "PP Neue Montreal", sans-serif`, `--font-size-base: 16px`.
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--encore-text-size-smaller-3: 0.625rem`, `--encore-text-size-smaller-2: 0.75rem`, `--encore-text-size-smaller: 0.875rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.45,0,.55,1)`, `cubic-bezier(.65,.05,.36,1)`, `cubic-bezier(.22,1,.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.search-panel.svelte-1w6by2l`**: `transition: opacity .15s ease,transform .15s ease,visibility .15s ease` extracted from `peabodyhouse-com` stylesheet.
- **Selector `.search-panel.is-dragging.svelte-...`**: `transition: none` extracted from `peabodyhouse-com` stylesheet.
- **Selector `media (prefers-reduced-motion: re...`**: `transition: opacity .15s ease,visibility .15s ease` extracted from `peabodyhouse-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.45,0,.55,1)`)**: Governs interactive state transitions across `<header.svelte-126o6dr>` and `<section.subhero>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `6542px`, deepest scrollY reached `0px` across `2` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `Lenis`, `WebGL/Canvas`.
- **Nav / Drawer Probe (`Open player`)**: Triggered visual change (pixel diff `18.779`, captured in `assets/state-nav.webp`); revealed links: Peabody House Peabody..., Expertise Expertise, Works Works, Studio Studio, Contact Contact.
- **Interactive Control Probe (`accordion`)**: Tested `I'm an agency manager. I represen...` (diff `3.064`).

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Peabody House • Digital Brand World Implem │
│ ====================================================================== │
│ [ <header.svelte-126o6dr (1436x28px)  | Expertise Expertise · Works  ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero> (w=1440px)                              | │
│ | H1: Peabody House is a digital brand world implementa...           | │
│ | Substrate: #faf6f3 | Ink: #26211e | Accent: #0000ff                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.subhero>) max-w: 960px                     | │
│ | +------------------------------+  +------------------------------+ | │
│ | | The ordeal of being perceive |  | What does Peabody House do?  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.service-cards>) — Technical Implementat    | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.js-line-disp) | https://peabodyhouse.com             │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .5rem)      │
│ ====================================================================== │
│ [ HEADER BAR (<header.svelte-126o6dr> ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.hero>) — 390px Vertical Lead                  | │
│ | H1: Peabody House is a digital brand world implementa...           | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.subhero>) — 1-Col Stack                   | │
│ | [ Item 1: The ordeal of being perceived.                         ] | │
│ | [ Item 2: What does Peabody House do?                            ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.service-cards>) — 1-Col (Technical Implemen)  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.js-line-disp) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.svelte-126o6dr> — `peabodyhouse-com`)**:
   - Landmark `<header class="svelte-126o6dr">` (`1436x28px`) hosting `Peabody House • Digital Brand World ` navigation (`Expertise Expertise · Works Works · Studio Studio · Contact Contact · Expertise`), DOM attributes (`data-sveltekit-preload-data="hover"`, `data-text="Peabody House"`, `data-text="Expertise"`, `data-text="Works"`), and stylesheet rule `.search.svelte-1w6by2l { position:relative;display:inline-flex;align-items:center }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Peabody House is a digital brand w`)**:
   - Landmark `<section class="hero svelte-x35jl1">` presenting display lead `Peabody House is a digital brand world implementa...` and copy excerpt *"Peabody House is a digital brand world implementation studio."* over `#faf6f3` canvas and `#26211e` ink.
3. **Primary Showcase & Content Grid (<section.subhero> — `The ordeal of being perceived.`)**:
   - Landmark `<section class="subhero svelte-x35jl1">` rendering section `The ordeal of being perceived.` with copy *"We future-proof brand aspirations into elevated, scalable design "*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `.search-panel.is-open.svelte-1w6by2l { opacity:1;visibility:visible;pointer-events:auto;transform:none }`.
4. **Interactive Detail & Feature Matrix (<section.service-cards> — `What does Peabody House do?`)**:
   - Landmark `<section class="service-cards svelte-1cpv9bu">` framing `What does Peabody House do?` and `Technical Implementation` (*"Your audience is more perceptible than you may think. How you aff"*) with `#c5f0c9` surface cards, `#0000ff` accents, and `arch-panel.is-positioned.svelte-1... { position:fixed;top:var(--panel-y);left:var(--panel-x);right:auto }`.
5. **Colophon & Global Directory Footer (<footer.js-line-displacement> — `https://peabodyhouse.com`)**:
   - Landmark `<footer class="js-line-displacement svelte-352yma">` anchoring `Peabody House • Digital Brand Wo` footer links (`Expertise Expertise · Works Works · Studio Studio · Contact Contact · Expertise`), copy *"People are more sensitive than ever to AI in 2026, and AI-pr"*, and `#008080` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `Peabod.?[;*=/<+ :·]-(/,)=<[?+[<(/ !,)·=!,*=:>+:>...` · sticky/fixed elements: `1`
- **Step 02** (`y=0px`, `100%`): Active landmark `Viewport` · sticky/fixed elements: `0`

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: peabodyhouse-com (Peabody House • Digital Brand World Implementation Studio)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `peabodyhouse-com` (**Peabody House • Digital Brand World Implementation Studio** — `https://peabodyhouse.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#faf6f3` / `#0000ff`).
- **Identity & Domain Context**: Peabody House is a Milwaukee-based digital studio that turns brand aspirations into elevated, scalable design systems. Led by human expre...
- **Primary Substrate**: `#faf6f3` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#26211e`, **Accent / Highlight**: `#0000ff`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#faf6f3` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#26211e` primary typography and `#0000ff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Peabody House` for display copy (`Peabody House is a digital brand wor`) with `PP Neue Montreal` and `SpotifyMixMono`.
  - **Calibrated Spatial Grid & Motion**: Combines `960px` container bounds (`gap: .5rem`, padding `.25rem`) with `cubic-bezier(.45,0,.55,1)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `peabodyhouse-com` in your global stylesheet:

:root {
  /* Peabody House • Digital Brand World Implementation Studio (peabodyhouse-com) — Live-Grounded CSS Variables */
  --color-primary: #26211E; /* Brand / Palette Token (peabodyhouse-com) */
  --color-secondary: #FAF6F3; /* Brand / Palette Token (peabodyhouse-com) */
  --color-accent: #DC942F; /* Brand / Palette Token (peabodyhouse-com) */
  --color-background: #FAF6F3; /* Canvas / Surface Token (peabodyhouse-com) */
  --color-text: #26211E; /* Typography Ink Token (peabodyhouse-com) */
  --color-white: #FAF6F3; /* Canvas / Surface Token (peabodyhouse-com) */
  --color-black: #26211E; /* Canvas / Surface Token (peabodyhouse-com) */
  --color-black-20: rgba(38, 33, 30, .2); /* Canvas / Surface Token (peabodyhouse-com) */
  --color-orange: #DC942F; /* Brand / Palette Token (peabodyhouse-com) */
  --color-blue: #517BB3; /* Brand / Palette Token (peabodyhouse-com) */
  --color-teal: #71C7B7; /* Brand / Palette Token (peabodyhouse-com) */
  --color-red: #A24250; /* Brand / Palette Token (peabodyhouse-com) */
  --color-green: #455330; /* Brand / Palette Token (peabodyhouse-com) */
  --font-heading: "Peabody House", sans-serif; /* Typography Ink Token (peabodyhouse-com) */
  --font-body: "PP Neue Montreal", sans-serif; /* Typography / Scale Token (peabodyhouse-com) */
  --font-size-base: 16px; /* Typography / Scale Token (peabodyhouse-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#faf6f3` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#26211e` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#c5f0c9` — grounded in `var(--encore-verified-badge-background)` in `:root`
- **Interactive Accent / Highlight**: `#0000ff` — grounded in `.cta:hover .cta-line { color: blue }` (`#0000ff`)
- **Secondary / Muted Copy**: `#f3727f` — grounded in `var(--text-negative)` in `:root`
- **Structural Hairline Border**: `#008080` — grounded in `.cta:before { border-top-color: #008080 }`
- **Variable Token (`--color-accent`)**: `#dc942f` — grounded in `var(--color-accent)` in `:root`
- **Variable Token (`--color-blue`)**: `#517bb3` — grounded in `var(--color-blue)` in `:root`
- **Variable Token (`--color-teal`)**: `#71c7b7` — grounded in `var(--color-teal)` in `:root`
- **Variable Token (`--color-red`)**: `#a24250` — grounded in `var(--color-red)` in `:root`
- **Variable Token (`--color-green`)**: `#455330` — grounded in `var(--color-green)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×1656px` (full-page live capture (1656px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `960px` (measured widest bounded `<section>` landmark width on `1440px` desktop)
- **Padding & Gutters**: `.25rem` lateral canvas padding with `.5rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 960px`, `gap: .5rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.25rem` horizontal padding
- **Media Queries**: `@media (min-width: 48rem)`, `@media (prefers-reduced-motion: reduce)`, `@media (min-width: 64rem)`, `@media (max-width: 63.99rem)`
- **Corner Radii**: `1px`, `50%`, `99px`, `12px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Peabody House`
- **Body Font Stack**: `PP Neue Montreal`
- **Monospace / Technical Font Stack**: `SpotifyMixMono`
- **H1 Display Rule**: live computed `h1` (`font-size: 68px`, `line-height: 76.5px`, `font-weight: 400`); CSS variables `--text-link-standalone-display: block`, `--encore-overlay-trigger-display: block`
- **H2 Section Rule**: live computed `h2` (`font-size: 60.48px`, `line-height: 63.504px`, `font-weight: 400`); rule `,.h2` (`font-size: clamp(2.0257rem,1.4626rem + 2...`, `line-height: 1.125`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-body: "PP Neue Montreal", sans-serif`, `--font-size-base: 16px`
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--encore-text-size-smaller-3: 0.625rem`, `--encore-text-size-smaller-2: 0.75rem`, `--encore-text-size-smaller: 0.875rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `peabodyhouse-com` (`Peabody House • Digital Brand World Implementation Studio`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.svelte-126o6dr> — `peabodyhouse-com`)**:
   - DOM & Selectors: Landmark `<header class="svelte-126o6dr">` (`1436x28px`) hosting `Peabody House • Digital Brand World ` navigation (`Expertise Expertise · Works Works · Studio Studio · Contact Contact · Expertise`), DOM attributes (`data-sveltekit-preload-data="hover"`, `data-text="Peabody House"`, `data-text="Expertise"`, `data-text="Works"`), and stylesheet rule `.search.svelte-1w6by2l { position:relative;display:inline-flex;align-items:center }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.svelte-126o6dr> — `peabodyhouse-com`)` (`peabodyhouse-com`) adapts across `@media (min-width: 48rem)`, `@media (prefers-reduced-motion: reduce)`, `@media (min-width: 64rem)`, `@media (max-width: 63.99rem)` with `cubic-bezier(.45,0,.55,1)`, `cubic-bezier(.65,.05,.36,1)`, `cubic-bezier(.22,1,.36,1)` transitions and links `Expertise Expertise · Works Works · Studio Studio · Contact Contact · Expertise`.
2. **Hero Stage & Focal Lead (<section.hero> — `Peabody House is a digital brand w`)**:
   - DOM & Selectors: Landmark `<section class="hero svelte-x35jl1">` presenting display lead `Peabody House is a digital brand world implementa...` and copy excerpt *"Peabody House is a digital brand world implementation studio."* over `#faf6f3` canvas and `#26211e` ink.
   - Responsive Contract: Hero stage (`1280×1656px` desktop / `390×2616px` mobile) sets `#faf6f3` background with `#26211e` headline `Peabody House is a digital brand world implementa...`.
3. **Primary Showcase & Content Grid (<section.subhero> — `The ordeal of being perceived.`)**:
   - DOM & Selectors: Landmark `<section class="subhero svelte-x35jl1">` rendering section `The ordeal of being perceived.` with copy *"We future-proof brand aspirations into elevated, scalable design "*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `.search-panel.is-open.svelte-1w6by2l { opacity:1;visibility:visible;pointer-events:auto;transform:none }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.subhero> — `The ordeal of being perceived.`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 960px`, `gap: .5rem`) on desktop and Single-column vertical stack at `390px` viewport width with `.25rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.service-cards> — `What does Peabody House do?`)**:
   - DOM & Selectors: Landmark `<section class="service-cards svelte-1cpv9bu">` framing `What does Peabody House do?` and `Technical Implementation` (*"Your audience is more perceptible than you may think. How you aff"*) with `#c5f0c9` surface cards, `#0000ff` accents, and `arch-panel.is-positioned.svelte-1... { position:fixed;top:var(--panel-y);left:var(--panel-x);right:auto }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.service-cards> — `What does Peabody House do?`)` uses `1px`, `50%`, `99px`, `12px` radii, `#0000ff` highlights, and assets (favicon.ico, favicon.svg, apple-touch-icon.png).
5. **Colophon & Global Directory Footer (<footer.js-line-displacement> — `https://peabodyhouse.com`)**:
   - DOM & Selectors: Landmark `<footer class="js-line-displacement svelte-352yma">` anchoring `Peabody House • Digital Brand Wo` footer links (`Expertise Expertise · Works Works · Studio Studio · Contact Contact · Expertise`), copy *"People are more sensitive than ever to AI in 2026, and AI-pr"*, and `#008080` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.js-line-displacement> — `https://peabodyhouse.com`)` aligns to `960px` (measured widest bounded `<section>` landmark width on `1440px` desktop) with `.25rem` lateral canvas padding with `.5rem` grid gap and attributes (data-sveltekit-preload-data="hover", data-text="Peabody House", data-text="Expertise").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Peabody House is a digital brand world implementation studio."*
- Copy Excerpt 2: *"We future-proof brand aspirations into elevated, scalable design systems. Led by h..."*
- Copy Excerpt 3: *"Your audience is more perceptible than you may think. How you affect is how you at..."*
- Copy Excerpt 4: *"People are more sensitive than ever to AI in 2026, and AI-prompted digital is no l..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.45,0,.55,1)`, `cubic-bezier(.65,.05,.36,1)`, `cubic-bezier(.22,1,.36,1)`
- **Extracted Stylesheet Rules (`peabodyhouse-com`)**:
- `.search.svelte-1w6by2l { position:relative;display:inline-flex;align-items:center }`
- `.search-panel.is-open.svelte-1w6by2l { opacity:1;visibility:visible;pointer-events:auto;transform:none }`
- `arch-panel.is-positioned.svelte-1... { position:fixed;top:var(--panel-y);left:var(--panel-x);right:auto }`
- `search-panel.is-dragging.svelte-1... { transition:none;-webkit-user-select:none;user-select:none;cursor:grabbing }`
- `.search-field__icon.svelte-1w6by2l { flex:0 0 auto;color:var(--color-black);opacity:.55 }`
- **Per-Selector Transition Rules**:
- **Selector `.search-panel.svelte-1w6by2l`**: `transition: opacity .15s ease,transform .15s ease,visibility .15s ease` extracted from `peabodyhouse-com` stylesheet.
- **Selector `.search-panel.is-dragging.svelte-...`**: `transition: none` extracted from `peabodyhouse-com` stylesheet.
- **Selector `media (prefers-reduced-motion: re...`**: `transition: opacity .15s ease,visibility .15s ease` extracted from `peabodyhouse-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.45,0,.55,1)`)**: Governs interactive state transitions across `<header.svelte-126o6dr>` and `<section.subhero>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `6542px` across 2 distinct viewport chapters using Lenis, WebGL/Canvas.
- **Vertical Chapter Sequence**: Peabod.?[;*=/<+ :·]-(/,)=<[... (0%) -> Viewport (100%).
- **Navigation Drawer / Menu State**: Replicate interactive menu toggle (`Open player`) with Escape-to-close keyboard handling.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `peabodyhouse-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | Peabod.?[;*=/<+ :·]-(/,)=<[?+[<(/ !,)·=!,*=:>... | `1` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `0px` | `100%` | Viewport | `0` | [desktop-step-02.webp](assets/desktop-step-02.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | PeabodyHouseisa digitalbr.·]>++*+ *([+(-[... | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `3083px` | `50%` | Dr. Kevin Zhao | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `6166px` | `100%` | I'm a freelancer. | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Interactive UI State Captures (`1440×900` WebP)
| State Type | Trigger / Observation | Visual Asset |
| :--- | :--- | :--- |
| `nav_menu` | Nav/Menu opened (`Open player`, diff `18.779`) | [state-nav.webp](assets/state-nav.webp) |

