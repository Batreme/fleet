---
title: "UI Prompt Blueprint: www-rtmaudio-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-rtmaudio-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier2_webgl
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#0e0f10` / `#d6c5a3`)"
---

# UI Design System & Master Generation Blueprint: www-rtmaudio-com

> **RTM Audio · Audio plug-ins for mixing and mastering** (https://www.rtmaudio.com) — Mixing and mastering plug-ins, built by working engineers. Judge the change. Not the volume.

![Desktop Viewport Capture (1440x900)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **RTM Audio · Audio plug-ins for mixing and mastering** (`https://www.rtmaudio.com`). Mixing and mastering plug-ins, built by working engineers. Judge the change. Not the volume.
- **Capture Provenance**: Live browser capture (`tier2_webgl`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#0e0f10` / `#d6c5a3`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#0e0f10` (live computed `html` `background-color` (`computed_styles.json`)) paired with `#f0e9dc` primary typography and `#d6c5a3` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Söhne Breit` for display copy (`Judge the change. Not the volume.`) with `Söhne Breit` and `JetBrains Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1296px` container bounds (`gap: 32px`, padding `.45rem`) with `cubic-bezier(.16,1,.3,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x844)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×900px` (`assets/desktop.png`, single-viewport 100vh live capture (900px)), Mobile `390×844px` (`assets/mobile.png`, single-viewport 100vh live capture (844px)).
- **Master Container Bounds**: `1296px` (measured widest bounded `<section>` landmark width on `1440px` desktop).
- **Canvas Lateral Padding & Spacing**: `.45rem` lateral canvas padding with `32px` grid gap.
- **Border Radius Scale**: `4px`, `2px`, `var(--r)`, `999px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1296px`, `gap: 32px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.45rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:560px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:820px)`, `@media (max-width:420px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0e0f10` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f0e9dc` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#121315` | live computed `a` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#d6c5a3` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#b08b5c` | `var(--ink-dim)` in `:root` |
| **Structural Hairline Border** | `#252524` | `var(--line)` in `:root` (`rgba(240,233,220,.10)`) |
| **Variable Token (`--green`)** | `#57c279` | `var(--green)` in `:root` |
| **Variable Token (`--well`)** | `#07080a` | `var(--well)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--display-weight` | `500` | Design System Custom Token |
| `--void` | `#0e0f10` | Color / Atmospheric Token |
| `--ink` | `#f0e9dc` | Typography Ink Token |
| `--ink-2` | `#d6c5a3` | Typography Ink Token |
| `--ink-dim` | `#b08b5c` | Typography Ink Token |
| `--green` | `#57c279` | Color / Atmospheric Token |
| `--line` | `rgba(240,233,220,.10)` | Color / Atmospheric Token |
| `--line-2` | `rgba(240,233,220,.22)` | Color / Atmospheric Token |
| `--wash` | `rgba(240,233,220,.05)` | Color / Atmospheric Token |
| `--well` | `#07080a` | Color / Atmospheric Token |
| `--raise` | `#121315` | Color / Atmospheric Token |
| `--glass` | `rgba(14,15,16,.72)` | Color / Atmospheric Token |
| `--acc` | `#b08b5c` | Color / Atmospheric Token |
| `--edge` | `inset 0 1px 0 rgba(240,233,220,.07)` | Color / Atmospheric Token |
| `--e1` | `var(--edge),0 1px 0 rgba(0,0,0,.5),0 34px 68px -34px rgba(0,0,0,.7)` | Color / Atmospheric Token |
| `--vignette` | `inset 0 0 34px 6px rgba(0,0,0,.55),inset 0 0 96px 20px rgba(8,6,4,.34)` | Color / Atmospheric Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Söhne Breit`.
- **Primary Body Stack**: `Söhne Breit`.
- **Technical / Metadata Stack**: `JetBrains Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 76.2899px`, `line-height: 71.7125px`, `font-weight: 500`, `letter-spacing: -1.90725px`); CSS variables `--display-weight: 500`, `--t-display: clamp(3.0518rem,2.3212rem + 2.7188vw,4.7684rem)`, `--lh-display: .94`; rule `h1` (`letter-spacing: -.02em`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 48.8288px`, `line-height: 48.8288px`, `font-weight: 500`, `letter-spacing: -0.976576px`); rule `h2` (`font-size: clamp(2.8rem,8vw,8rem)`, `line-height: .84`, `letter-spacing: -.045em`, `font-weight: 500`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`, `letter-spacing: 0.288px`); CSS variables `--t-body: 1rem`, `--lh-body: 24px`, `--tr-body: 0`; rule `body` (`letter-spacing: .018em`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 12.8px`, `line-height: normal`, `font-weight: 400`, `letter-spacing: 1.792px`); CSS variables `--mono: "JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace`, `--t-label: .8rem`, `--m-label: .8rem`; rule `small` (`font-size: .65rem`, `letter-spacing: .13em`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.16,1,.3,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `media(prefers-reduced-motion:reduce)`**: `transition: none!important` extracted from `www-rtmaudio-com` stylesheet.
- **Selector `.material-light::before`**: `transition: opacity .5s var(--ease)` extracted from `www-rtmaudio-com` stylesheet.
- **Selector `.campaign-object`**: `transition: transform .22s var(--ease)` extracted from `www-rtmaudio-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.campaigns-head>` and `<section.campaigns>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — RTM Audio · Audio plug-ins for mixing and  │
│ ====================================================================== │
│ [ <header.campaigns-head (1296x194px) | Plugins Plugins · Store Stor ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.take> (w=1440px)                              | │
│ | H1: Judge the change. Not the volume.                              | │
│ | Substrate: #0e0f10 | Ink: #f0e9dc | Accent: #d6c5a3                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.campaigns>) max-w: 1296px                  | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Nine in the rack.            |  | Your whole rack, in one app. | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<article.campaign-panel>) — One-time licences. No   | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.cn-ground>  ) | https://www.rtmaudio.com             │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 32px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.campaigns-head> ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.take>) — 390px Vertical Lead                  | │
│ | H1: Judge the change. Not the volume.                              | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.campaigns>) — 1-Col Stack                 | │
│ | [ Item 1: Nine in the rack.                                      ] | │
│ | [ Item 2: Your whole rack, in one app.                           ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<article.campaign-panel>) — 1-Col (One-time licences.) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.cn-ground>  ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.campaigns-head> — `www-rtmaudio-com`)**:
   - Landmark `<header class="campaigns-head">` (`1296x194px`) hosting `RTM Audio · Audio plug-ins for mixin` navigation (`Plugins Plugins · Store Store · About About · Account Account`), DOM attributes (`data-consent="granted"`, `data-i18n-key="RTM Audio · Audio plu..."`, `data-i18n-content="Mixing and mastering..."`, `data-i18n-content="Mixing and mastering..."`), and stylesheet rule `root { --display-weight:500; }`.
2. **Hero Stage & Focal Lead (<section.take> — `Judge the change. Not the volume.`)**:
   - Landmark `<section class="take">` presenting display lead `Judge the change. Not the volume.` and copy excerpt *"Mixing and mastering plug-ins, built by working engineers."* over `#0e0f10` canvas and `#f0e9dc` ink.
3. **Primary Showcase & Content Grid (<section.campaigns> — `Nine in the rack.`)**:
   - Landmark `<section class="campaigns">` rendering section `Nine in the rack.` with copy *"EQ, vocals, dynamics and loudness."*, asset references (`clarity.js`, `soehne-breit-kraftig.woff2`, `fonts.css`, `site.css`), and grid rule `body { letter-spacing:.018em }`.
4. **Interactive Detail & Feature Matrix (<article.campaign-panel> — `Your whole rack, in one app.`)**:
   - Landmark `<article class="campaign-panel material-light">` framing `Your whole rack, in one app.` and `One-time licences. No subscription.` (*"Download, install and activate every plug-in you own. Free for Ma"*) with `#121315` surface cards, `#d6c5a3` accents, and `.hero h1 { letter-spacing:-.02em }`.
5. **Colophon & Global Directory Footer (<footer.cn-ground> — `https://www.rtmaudio.com`)**:
   - Landmark `<footer class="cn-ground">` anchoring `RTM Audio · Audio plug-ins for m` footer links (`Plugins Plugins · Store Store · About About · Account Account`), copy *"Try any plug-in in the store first."*, and `#252524` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-rtmaudio-com (RTM Audio · Audio plug-ins for mixing and mastering)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-rtmaudio-com` (**RTM Audio · Audio plug-ins for mixing and mastering** — `https://www.rtmaudio.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0e0f10` / `#d6c5a3`).
- **Identity & Domain Context**: Mixing and mastering plug-ins, built by working engineers. Judge the change. Not the volume.
- **Primary Substrate**: `#0e0f10` (live computed `html` `background-color` (`computed_styles.json`)), **Primary Ink**: `#f0e9dc`, **Accent / Highlight**: `#d6c5a3`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#0e0f10` (live computed `html` `background-color` (`computed_styles.json`)) paired with `#f0e9dc` primary typography and `#d6c5a3` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Söhne Breit` for display copy (`Judge the change. Not the volume.`) with `Söhne Breit` and `JetBrains Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1296px` container bounds (`gap: 32px`, padding `.45rem`) with `cubic-bezier(.16,1,.3,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-rtmaudio-com` in your global stylesheet:

:root {
  /* RTM Audio · Audio plug-ins for mixing and mastering (www-rtmaudio-com) — Live-Grounded CSS Variables */
  --display-weight: 500; /* Design System Custom Token (www-rtmaudio-com) */
  --void: #0e0f10; /* Color / Atmospheric Token (www-rtmaudio-com) */
  --ink: #f0e9dc; /* Typography Ink Token (www-rtmaudio-com) */
  --ink-2: #d6c5a3; /* Typography Ink Token (www-rtmaudio-com) */
  --ink-dim: #b08b5c; /* Typography Ink Token (www-rtmaudio-com) */
  --green: #57c279; /* Color / Atmospheric Token (www-rtmaudio-com) */
  --line: rgba(240,233,220,.10); /* Color / Atmospheric Token (www-rtmaudio-com) */
  --line-2: rgba(240,233,220,.22); /* Color / Atmospheric Token (www-rtmaudio-com) */
  --wash: rgba(240,233,220,.05); /* Color / Atmospheric Token (www-rtmaudio-com) */
  --well: #07080a; /* Color / Atmospheric Token (www-rtmaudio-com) */
  --raise: #121315; /* Color / Atmospheric Token (www-rtmaudio-com) */
  --glass: rgba(14,15,16,.72); /* Color / Atmospheric Token (www-rtmaudio-com) */
  --acc: #b08b5c; /* Color / Atmospheric Token (www-rtmaudio-com) */
  --edge: inset 0 1px 0 rgba(240,233,220,.07); /* Color / Atmospheric Token (www-rtmaudio-com) */
  --e1: var(--edge),0 1px 0 rgba(0,0,0,.5),0 34px 68px -34px rgba(0,0,0,.7); /* Color / Atmospheric Token (www-rtmaudio-com) */
  --vignette: inset 0 0 34px 6px rgba(0,0,0,.55),inset 0 0 96px 20px rgba(8,6,4,.34); /* Color / Atmospheric Token (www-rtmaudio-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#0e0f10` — grounded in live computed `html` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#f0e9dc` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#121315` — grounded in live computed `a` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#d6c5a3` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Secondary / Muted Copy**: `#b08b5c` — grounded in `var(--ink-dim)` in `:root`
- **Structural Hairline Border**: `#252524` — grounded in `var(--line)` in `:root` (`rgba(240,233,220,.10)`)
- **Variable Token (`--green`)**: `#57c279` — grounded in `var(--green)` in `:root`
- **Variable Token (`--well`)**: `#07080a` — grounded in `var(--well)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×900px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×844px` (single-viewport 100vh live capture (844px), `390px` standard mobile width).
- **Container Max-Width**: `1296px` (measured widest bounded `<section>` landmark width on `1440px` desktop)
- **Padding & Gutters**: `.45rem` lateral canvas padding with `32px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1296px`, `gap: 32px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.45rem` horizontal padding
- **Media Queries**: `@media (max-width:560px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:820px)`, `@media (max-width:420px)`
- **Corner Radii**: `4px`, `2px`, `var(--r)`, `999px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Söhne Breit`
- **Body Font Stack**: `Söhne Breit`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **H1 Display Rule**: live computed `h1` (`font-size: 76.2899px`, `line-height: 71.7125px`, `font-weight: 500`, `letter-spacing: -1.90725px`); CSS variables `--display-weight: 500`, `--t-display: clamp(3.0518rem,2.3212rem + 2.7188vw,4.7684rem)`, `--lh-display: .94`; rule `h1` (`letter-spacing: -.02em`)
- **H2 Section Rule**: live computed `h2` (`font-size: 48.8288px`, `line-height: 48.8288px`, `font-weight: 500`, `letter-spacing: -0.976576px`); rule `h2` (`font-size: clamp(2.8rem,8vw,8rem)`, `line-height: .84`, `letter-spacing: -.045em`, `font-weight: 500`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`, `letter-spacing: 0.288px`); CSS variables `--t-body: 1rem`, `--lh-body: 24px`, `--tr-body: 0`; rule `body` (`letter-spacing: .018em`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 12.8px`, `line-height: normal`, `font-weight: 400`, `letter-spacing: 1.792px`); CSS variables `--mono: "JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace`, `--t-label: .8rem`, `--m-label: .8rem`; rule `small` (`font-size: .65rem`, `letter-spacing: .13em`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-rtmaudio-com` (`RTM Audio · Audio plug-ins for mixing and mastering`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.campaigns-head> — `www-rtmaudio-com`)**:
   - DOM & Selectors: Landmark `<header class="campaigns-head">` (`1296x194px`) hosting `RTM Audio · Audio plug-ins for mixin` navigation (`Plugins Plugins · Store Store · About About · Account Account`), DOM attributes (`data-consent="granted"`, `data-i18n-key="RTM Audio · Audio plu..."`, `data-i18n-content="Mixing and mastering..."`, `data-i18n-content="Mixing and mastering..."`), and stylesheet rule `root { --display-weight:500; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.campaigns-head> — `www-rtmaudio-com`)` (`www-rtmaudio-com`) adapts across `@media (max-width:560px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:820px)`, `@media (max-width:420px)` with `cubic-bezier(.16,1,.3,1)` transitions and links `Plugins Plugins · Store Store · About About · Account Account`.
2. **Hero Stage & Focal Lead (<section.take> — `Judge the change. Not the volume.`)**:
   - DOM & Selectors: Landmark `<section class="take">` presenting display lead `Judge the change. Not the volume.` and copy excerpt *"Mixing and mastering plug-ins, built by working engineers."* over `#0e0f10` canvas and `#f0e9dc` ink.
   - Responsive Contract: Hero stage (`1440×900px` desktop / `390×844px` mobile) sets `#0e0f10` background with `#f0e9dc` headline `Judge the change. Not the volume.`.
3. **Primary Showcase & Content Grid (<section.campaigns> — `Nine in the rack.`)**:
   - DOM & Selectors: Landmark `<section class="campaigns">` rendering section `Nine in the rack.` with copy *"EQ, vocals, dynamics and loudness."*, asset references (`clarity.js`, `soehne-breit-kraftig.woff2`, `fonts.css`, `site.css`), and grid rule `body { letter-spacing:.018em }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.campaigns> — `Nine in the rack.`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1296px`, `gap: 32px`) on desktop and Single-column vertical stack at `390px` viewport width with `.45rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.campaign-panel> — `Your whole rack, in one app.`)**:
   - DOM & Selectors: Landmark `<article class="campaign-panel material-light">` framing `Your whole rack, in one app.` and `One-time licences. No subscription.` (*"Download, install and activate every plug-in you own. Free for Ma"*) with `#121315` surface cards, `#d6c5a3` accents, and `.hero h1 { letter-spacing:-.02em }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.campaign-panel> — `Your whole rack, in one app.`)` uses `4px`, `2px`, `var(--r)`, `999px` radii, `#d6c5a3` highlights, and assets (clarity.js, soehne-breit-kraftig.woff2, fonts.css).
5. **Colophon & Global Directory Footer (<footer.cn-ground> — `https://www.rtmaudio.com`)**:
   - DOM & Selectors: Landmark `<footer class="cn-ground">` anchoring `RTM Audio · Audio plug-ins for m` footer links (`Plugins Plugins · Store Store · About About · Account Account`), copy *"Try any plug-in in the store first."*, and `#252524` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.cn-ground> — `https://www.rtmaudio.com`)` aligns to `1296px` (measured widest bounded `<section>` landmark width on `1440px` desktop) with `.45rem` lateral canvas padding with `32px` grid gap and attributes (data-consent="granted", data-i18n-key="RTM Audio · Audio plu...", data-i18n-content="Mixing and mastering...").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Mixing and mastering plug-ins, built by working engineers."*
- Copy Excerpt 2: *"EQ, vocals, dynamics and loudness."*
- Copy Excerpt 3: *"Download, install and activate every plug-in you own. Free for Mac and Windows."*
- Copy Excerpt 4: *"Try any plug-in in the store first."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.16,1,.3,1)`
- **Extracted Stylesheet Rules (`www-rtmaudio-com`)**:
- `root { --display-weight:500; }`
- `body { letter-spacing:.018em }`
- `.hero h1 { letter-spacing:-.02em }`
- `.rtm-language { display:inline-flex;align-items:center;margin-inline-start:clamp(8px,1.2... }`
- `.rtm-language select:focus-visible { outline:2px solid currentColor;outline-offset:3px }`
- **Per-Selector Transition Rules**:
- **Selector `media(prefers-reduced-motion:reduce)`**: `transition: none!important` extracted from `www-rtmaudio-com` stylesheet.
- **Selector `.material-light::before`**: `transition: opacity .5s var(--ease)` extracted from `www-rtmaudio-com` stylesheet.
- **Selector `.campaign-object`**: `transition: transform .22s var(--ease)` extracted from `www-rtmaudio-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.campaigns-head>` and `<section.campaigns>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-rtmaudio-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
