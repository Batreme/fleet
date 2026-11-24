---
title: "UI Prompt Blueprint: reelmotion-fit"
date: 2026-11-24
captured_at: 2026-11-24
target: "reelmotion-fit"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: native
desktop_keyframes: 6
subpages_crawled: 1
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#f5f7fb` canvas, `#0e1116` ink, `#0d95e8` accent)"
---

# UI Design System & Master Generation Blueprint: reelmotion-fit

> **Reel Motion: Turn Workout Videos Into Exercise Routines** (https://reelmotion.fit/) — Paste a link from YouTube, Instagram, or TikTok and Reel Motion creates an illustrated, step-by-step workout you can follow on iPhone and...

![Desktop Journey Filmstrip (1280x4968)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Reel Motion: Turn Workout Videos Into Exercise Routines** (`https://reelmotion.fit/`). Paste a link from YouTube, Instagram, or TikTok and Reel Motion creates an illustrated, step-by-step workout you can follow on iPhone and...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#f5f7fb` canvas, `#0e1116` ink, `#0d95e8` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f5f7fb` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#0e1116` primary typography and `#0d95e8` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Inter Tight` for display copy (`Any workout video becomes a routine `) with `Inter`.
  - **Calibrated Spatial Grid & Motion**: Combines `1304px` container bounds (`gap: var(--row-gap)`, padding `.5rem`) with `cubic-bezier(.47,0,.74,.71)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×4968px` (`assets/desktop-journey.webp`, `6` keyframes up to `y=4038px` / doc `4938px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1304px` (measured widest bounded `<section>` landmark width on `1440px` desktop).
- **Canvas Lateral Padding & Spacing**: `.5rem` lateral canvas padding with `var(--row-gap)` grid gap.
- **Border Radius Scale**: `999px`, `3px`, `var(--border-radius)`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1304px`, `gap: var(--row-gap)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:767px)`, `@media (max-width:1024px)`, `@media (min-width:-1)`, `@media (max-width:-1)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f5f7fb` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0e1116` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0d95e8` | `.fancybox-share__button--tw:hover { background: #0d95e8 }` |
| **Secondary / Muted Copy** | `#8a93a3` | `var(--Muted)` in `:root` |
| **Structural Hairline Border** | `#cccccc` | `pre { border: #cccccc }` |
| **Variable Token (`--e-gv-d8119ec`)** | `#934cff` | `var(--e-gv-d8119ec)` in `:root` |
| **Variable Token (`--e-gv-22831a4`)** | `#7a32f0` | `var(--e-gv-22831a4)` in `:root` |
| **Variable Token (`--e-gv-c75aa4e`)** | `#2f7cf8` | `var(--e-gv-c75aa4e)` in `:root` |
| **Variable Token (`--e-gv-ac48b9b`)** | `#78aafa` | `var(--e-gv-ac48b9b)` in `:root` |
| **Variable Token (`--e-gv-399bfaa`)** | `#975af4` | `var(--e-gv-399bfaa)` in `:root` |
| **Variable Token (`--e-gv-cd3db67`)** | `#f5f4fb` | `var(--e-gv-cd3db67)` in `:root` |
| **Variable Token (`--e-gv-0105447`)** | `#161a20` | `var(--e-gv-0105447)` in `:root` |
| **Variable Token (`--e-gv-80cc8b6`)** | `#6b6f7b` | `var(--e-gv-80cc8b6)` in `:root` |
| **Variable Token (`--e-gv-d4944d5`)** | `#e6e4f0` | `var(--e-gv-d4944d5)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--wp--style--global--content-size` | `800px` | Layout / Spatial Grid Token |
| `--wp--style--global--wide-size` | `1200px` | Layout / Spatial Grid Token |
| `--wp--style--block-gap` | `24px` | Layout / Spatial Grid Token |
| `--direction-multiplier` | `1` | Design System Custom Token |
| `--page-title-display` | `block` | Design System Custom Token |
| `--e-gv-d8119ec` | `#934cff` | Color / Atmospheric Token |
| `--e-gv-22831a4` | `#7a32f0` | Color / Atmospheric Token |
| `--e-gv-c75aa4e` | `#2f7cf8` | Color / Atmospheric Token |
| `--e-gv-ac48b9b` | `#78aafa` | Color / Atmospheric Token |
| `--e-gv-399bfaa` | `#975af4` | Color / Atmospheric Token |
| `--e-gv-1036c6e` | `#ffffff` | Color / Atmospheric Token |
| `--e-gv-cd3db67` | `#f5f4fb` | Color / Atmospheric Token |
| `--e-gv-0105447` | `#161a20` | Color / Atmospheric Token |
| `--e-gv-9d9c176` | `#161a20` | Color / Atmospheric Token |
| `--e-gv-80cc8b6` | `#6b6f7b` | Color / Atmospheric Token |
| `--e-gv-d4944d5` | `#e6e4f0` | Color / Atmospheric Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Inter Tight`.
- **Primary Body Stack**: `Inter`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 66px`, `line-height: 68.64px`, `font-weight: 700`, `letter-spacing: -1.65px`); CSS variables `--page-title-display: block`, `--Display: Inter Tight`, `--TextDisplay: clamp(32px, 5.4vw, 66px)`; rule `h1` (`font-size: 35px`, `font-weight: 700`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 48px`, `line-height: 50.88px`, `font-weight: 700`, `letter-spacing: -1.2px`); CSS variables `--TextH2: clamp(30px, 3.9vw, 48px)`; rule `h2` (`font-size: var( --e-global-typography-se...`, `line-height: var( --e-global-typog...`, `letter-spacing: var( --e-global-typog...`, `font-weight: var( --e-glob...`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24.8px`, `font-weight: 400`); CSS variables `--Body: Inter`, `--TextBody: 16px`; rule `p` (`font-size: 16px`, `line-height: 20px`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24.8px`, `font-weight: 400`); CSS variables `--TextSmall: 15px`, `--e-global-typography-primary-letter-spacing: -0.025em`, `--e-global-typography-secondary-letter-spacing: -0.025em`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.47,0,.74,.71)`, `cubic-bezier(.22,.61,.36,1)`, `cubic-bezier(.5,0,.14,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `textarea`**: `transition: all .3s` extracted from `reelmotion-fit` stylesheet.
- **Selector `button`**: `transition: all .3s` extracted from `reelmotion-fit` stylesheet.
- **Selector `entor .elementor-background-video...`**: `transition: opacity 1s` extracted from `reelmotion-fit` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.47,0,.74,.71)`)**: Governs interactive state transitions across `<nav.elementor>` and `<section.elementor-element-rmhowsec>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `4938px`, deepest scrollY reached `4038px` across `6` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `GSAP/ScrollTrigger`.
- **Hover Physics (`primary_cta` · `Download App`)**: `backgroundColor`: `rgb(14, 17, 22)` -> `rgb(26, 31, 40)`; `boxShadow`: `none` -> `rgba(120, 127, 246, 0.6...` (`transition-duration: 0.2s, 0.2s`, `timing: ease, ease`).
- **Route Transition Architecture**: First internal navigation (`/support/`) measured as `MPA` in `4382ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Reel Motion: Turn Workout Videos Into Exer │
│ ====================================================================== │
│ [ <nav.elementor> (1440x0px)          | Reel Motion · Home · Feature ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.elementor-element> (w=1440px)                 | │
│ | H1: Any workout video becomes a routine you can                    | │
│ | Substrate: #f5f7fb | Ink: #0e1116 | Accent: #0d95e8                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.elementor-element) max-w: 1304px           | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Read once, run hands-free    |  | Illustrated exercises        | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.elementor-element) — Hands-free control    | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.elementor>  ) | https://reelmotion.fit/              │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--ro)   │
│ ====================================================================== │
│ [ HEADER BAR (<nav.elementor>         ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.elementor-eleme) — 390px Vertical Lead        | │
│ | H1: Any workout video becomes a routine you can                    | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.elementor-ele) — 1-Col Stack              | │
│ | [ Item 1: Read once, run hands-free                              ] | │
│ | [ Item 2: Illustrated exercises                                  ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.elementor-eleme) — 1-Col (Hands-free control) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.elementor>  ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.elementor> — `reelmotion-fit`)**:
   - Landmark `<nav class="elementor elementor-15">` (`1440x0px`) hosting `Reel Motion: Turn Workout Videos Int` navigation (`Reel Motion · Home · Features · How it works · Pricing`), DOM attributes (`data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-elementor-device-mode="desktop"`), and stylesheet rule `html { line-height:1.15;-webkit-text-size-adjust:100% }`.
2. **Hero Stage & Focal Lead (<section.elementor-element> — `Any workout video becomes a routin`)**:
   - Landmark `<section class="elementor-element elementor-element-rmfeatsec">` presenting display lead `Any workout video becomes a routine you can` and copy excerpt *"Paste a link from YouTube, Instagram, or TikTok. Get illustrated "* over `#f5f7fb` canvas and `#0e1116` ink.
3. **Primary Showcase & Content Grid (<section.elementor-element-rmhowsec> — `Read once, run hands-free`)**:
   - Landmark `<section class="elementor-element elementor-element-rmhowsec">` rendering section `Read once, run hands-free` with copy *"Reel Motion reads the video for you, then hands back a workout yo"*, asset references (`fonts.googleapis.com`, `embed`, `reset.css`, `theme.css`), and grid rule `before { box-sizing:border-box }`.
4. **Interactive Detail & Feature Matrix (<section.elementor-element-rmpricesec> — `Illustrated exercises`)**:
   - Landmark `<section class="elementor-element elementor-element-rmpricesec">` framing `Illustrated exercises` and `Hands-free control` (*"Start and finish positions, drawn for every move."*) with `#ffffff` surface cards, `#0d95e8` accents, and `pre { font-family:monospace;font-size:1em;white-space:pre-wrap }`.
5. **Colophon & Global Directory Footer (<footer.elementor> — `https://reelmotion.fit/`)**:
   - Landmark `<footer class="elementor elementor-68">` anchoring `Reel Motion: Turn Workout Videos` footer links (`Reel Motion · Home · Features · How it works · Pricing`), copy *"Say start, next, or done. Your phone stays on the floor."*, and `#cccccc` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `Any workout video becomes a routine you can` · sticky/fixed elements: `1`
- **Step 02** (`y=850px`, `21%`): Active landmark `Read once, run hands-free` · sticky/fixed elements: `1`
- **Step 03** (`y=1700px`, `42%`): Active landmark `How it works` · sticky/fixed elements: `1`
- **Step 04** (`y=2550px`, `63%`): Active landmark `Every plan unlocks the whole app` · sticky/fixed elements: `1`
- **Step 05** (`y=3400px`, `84%`): Active landmark `Your next workout is one link away.` · sticky/fixed elements: `1`
- **Step 06** (`y=4038px`, `100%`): Active landmark `Footer` · sticky/fixed elements: `1`

### Multi-Page Internal Route Map
- **Other Route (`/support/`)**: `https://reelmotion.fit/support/` — H1: `Need a hand?`, scrollHeight `2646px`, transition `MPA` (`4382ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: reelmotion-fit (Reel Motion: Turn Workout Videos Into Exercise Routines)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `reelmotion-fit` (**Reel Motion: Turn Workout Videos Into Exercise Routines** — `https://reelmotion.fit/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#f5f7fb` canvas, `#0e1116` ink, `#0d95e8` accent).
- **Identity & Domain Context**: Paste a link from YouTube, Instagram, or TikTok and Reel Motion creates an illustrated, step-by-step workout you can follow on iPhone and...
- **Primary Substrate**: `#f5f7fb` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#0e1116`, **Accent / Highlight**: `#0d95e8`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f5f7fb` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#0e1116` primary typography and `#0d95e8` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Inter Tight` for display copy (`Any workout video becomes a routine `) with `Inter`.
  - **Calibrated Spatial Grid & Motion**: Combines `1304px` container bounds (`gap: var(--row-gap)`, padding `.5rem`) with `cubic-bezier(.47,0,.74,.71)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `reelmotion-fit` in your global stylesheet:

:root {
  /* Reel Motion: Turn Workout Videos Into Exercise Routines (reelmotion-fit) — Live-Grounded CSS Variables */
  --wp--style--global--content-size: 800px; /* Layout / Spatial Grid Token (reelmotion-fit) */
  --wp--style--global--wide-size: 1200px; /* Layout / Spatial Grid Token (reelmotion-fit) */
  --wp--style--block-gap: 24px; /* Layout / Spatial Grid Token (reelmotion-fit) */
  --direction-multiplier: 1; /* Design System Custom Token (reelmotion-fit) */
  --page-title-display: block; /* Design System Custom Token (reelmotion-fit) */
  --e-gv-d8119ec: #934cff; /* Color / Atmospheric Token (reelmotion-fit) */
  --e-gv-22831a4: #7a32f0; /* Color / Atmospheric Token (reelmotion-fit) */
  --e-gv-c75aa4e: #2f7cf8; /* Color / Atmospheric Token (reelmotion-fit) */
  --e-gv-ac48b9b: #78aafa; /* Color / Atmospheric Token (reelmotion-fit) */
  --e-gv-399bfaa: #975af4; /* Color / Atmospheric Token (reelmotion-fit) */
  --e-gv-1036c6e: #ffffff; /* Color / Atmospheric Token (reelmotion-fit) */
  --e-gv-cd3db67: #f5f4fb; /* Color / Atmospheric Token (reelmotion-fit) */
  --e-gv-0105447: #161a20; /* Color / Atmospheric Token (reelmotion-fit) */
  --e-gv-9d9c176: #161a20; /* Color / Atmospheric Token (reelmotion-fit) */
  --e-gv-80cc8b6: #6b6f7b; /* Color / Atmospheric Token (reelmotion-fit) */
  --e-gv-d4944d5: #e6e4f0; /* Color / Atmospheric Token (reelmotion-fit) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f5f7fb` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#0e1116` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#ffffff` — grounded in live computed `button` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#0d95e8` — grounded in `.fancybox-share__button--tw:hover { background: #0d95e8 }`
- **Secondary / Muted Copy**: `#8a93a3` — grounded in `var(--Muted)` in `:root`
- **Structural Hairline Border**: `#cccccc` — grounded in `pre { border: #cccccc }`
- **Variable Token (`--e-gv-d8119ec`)**: `#934cff` — grounded in `var(--e-gv-d8119ec)` in `:root`
- **Variable Token (`--e-gv-22831a4`)**: `#7a32f0` — grounded in `var(--e-gv-22831a4)` in `:root`
- **Variable Token (`--e-gv-c75aa4e`)**: `#2f7cf8` — grounded in `var(--e-gv-c75aa4e)` in `:root`
- **Variable Token (`--e-gv-ac48b9b`)**: `#78aafa` — grounded in `var(--e-gv-ac48b9b)` in `:root`
- **Variable Token (`--e-gv-399bfaa`)**: `#975af4` — grounded in `var(--e-gv-399bfaa)` in `:root`
- **Variable Token (`--e-gv-cd3db67`)**: `#f5f4fb` — grounded in `var(--e-gv-cd3db67)` in `:root`
- **Variable Token (`--e-gv-0105447`)**: `#161a20` — grounded in `var(--e-gv-0105447)` in `:root`
- **Variable Token (`--e-gv-80cc8b6`)**: `#6b6f7b` — grounded in `var(--e-gv-80cc8b6)` in `:root`
- **Variable Token (`--e-gv-d4944d5`)**: `#e6e4f0` — grounded in `var(--e-gv-d4944d5)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×4968px` (multi-frame vertical journey filmstrip (4968px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1304px` (measured widest bounded `<section>` landmark width on `1440px` desktop)
- **Padding & Gutters**: `.5rem` lateral canvas padding with `var(--row-gap)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1304px`, `gap: var(--row-gap)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding
- **Media Queries**: `@media (max-width:767px)`, `@media (max-width:1024px)`, `@media (min-width:-1)`, `@media (max-width:-1)`
- **Corner Radii**: `999px`, `3px`, `var(--border-radius)`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Inter Tight`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 66px`, `line-height: 68.64px`, `font-weight: 700`, `letter-spacing: -1.65px`); CSS variables `--page-title-display: block`, `--Display: Inter Tight`, `--TextDisplay: clamp(32px, 5.4vw, 66px)`; rule `h1` (`font-size: 35px`, `font-weight: 700`)
- **H2 Section Rule**: live computed `h2` (`font-size: 48px`, `line-height: 50.88px`, `font-weight: 700`, `letter-spacing: -1.2px`); CSS variables `--TextH2: clamp(30px, 3.9vw, 48px)`; rule `h2` (`font-size: var( --e-global-typography-se...`, `line-height: var( --e-global-typog...`, `letter-spacing: var( --e-global-typog...`, `font-weight: var( --e-glob...`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24.8px`, `font-weight: 400`); CSS variables `--Body: Inter`, `--TextBody: 16px`; rule `p` (`font-size: 16px`, `line-height: 20px`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24.8px`, `font-weight: 400`); CSS variables `--TextSmall: 15px`, `--e-global-typography-primary-letter-spacing: -0.025em`, `--e-global-typography-secondary-letter-spacing: -0.025em`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `reelmotion-fit` (`Reel Motion: Turn Workout Videos Into Exercise Routines`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.elementor> — `reelmotion-fit`)**:
   - DOM & Selectors: Landmark `<nav class="elementor elementor-15">` (`1440x0px`) hosting `Reel Motion: Turn Workout Videos Int` navigation (`Reel Motion · Home · Features · How it works · Pricing`), DOM attributes (`data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-elementor-device-mode="desktop"`), and stylesheet rule `html { line-height:1.15;-webkit-text-size-adjust:100% }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.elementor> — `reelmotion-fit`)` (`reelmotion-fit`) adapts across `@media (max-width:767px)`, `@media (max-width:1024px)`, `@media (min-width:-1)`, `@media (max-width:-1)` with `cubic-bezier(.47,0,.74,.71)`, `cubic-bezier(.22,.61,.36,1)`, `cubic-bezier(.5,0,.14,1)` transitions and links `Reel Motion · Home · Features · How it works · Pricing`.
2. **Hero Stage & Focal Lead (<section.elementor-element> — `Any workout video becomes a routin`)**:
   - DOM & Selectors: Landmark `<section class="elementor-element elementor-element-rmfeatsec">` presenting display lead `Any workout video becomes a routine you can` and copy excerpt *"Paste a link from YouTube, Instagram, or TikTok. Get illustrated "* over `#f5f7fb` canvas and `#0e1116` ink.
   - Responsive Contract: Hero stage (`1280×4968px` desktop / `390×2616px` mobile) sets `#f5f7fb` background with `#0e1116` headline `Any workout video becomes a routine you can`.
3. **Primary Showcase & Content Grid (<section.elementor-element-rmhowsec> — `Read once, run hands-free`)**:
   - DOM & Selectors: Landmark `<section class="elementor-element elementor-element-rmhowsec">` rendering section `Read once, run hands-free` with copy *"Reel Motion reads the video for you, then hands back a workout yo"*, asset references (`fonts.googleapis.com`, `embed`, `reset.css`, `theme.css`), and grid rule `before { box-sizing:border-box }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.elementor-element-rmhowsec> — `Read once, run hands-free`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1304px`, `gap: var(--row-gap)`) on desktop and Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.elementor-element-rmpricesec> — `Illustrated exercises`)**:
   - DOM & Selectors: Landmark `<section class="elementor-element elementor-element-rmpricesec">` framing `Illustrated exercises` and `Hands-free control` (*"Start and finish positions, drawn for every move."*) with `#ffffff` surface cards, `#0d95e8` accents, and `pre { font-family:monospace;font-size:1em;white-space:pre-wrap }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.elementor-element-rmpricesec> — `Illustrated exercises`)` uses `999px`, `3px`, `var(--border-radius)`, `2px` radii, `#0d95e8` highlights, and assets (fonts.googleapis.com, embed, reset.css).
5. **Colophon & Global Directory Footer (<footer.elementor> — `https://reelmotion.fit/`)**:
   - DOM & Selectors: Landmark `<footer class="elementor elementor-68">` anchoring `Reel Motion: Turn Workout Videos` footer links (`Reel Motion · Home · Features · How it works · Pricing`), copy *"Say start, next, or done. Your phone stays on the floor."*, and `#cccccc` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.elementor> — `https://reelmotion.fit/`)` aligns to `1304px` (measured widest bounded `<section>` landmark width on `1440px` desktop) with `.5rem` lateral canvas padding with `var(--row-gap)` grid gap and attributes (data-wp-strategy="defer", data-wp-strategy="defer", data-wp-strategy="defer").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Paste a link from YouTube, Instagram, or TikTok. Get illustrated exercises, step-b..."*
- Copy Excerpt 2: *"Reel Motion reads the video for you, then hands back a workout you can run without..."*
- Copy Excerpt 3: *"Start and finish positions, drawn for every move."*
- Copy Excerpt 4: *"Say start, next, or done. Your phone stays on the floor."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.47,0,.74,.71)`, `cubic-bezier(.22,.61,.36,1)`, `cubic-bezier(.5,0,.14,1)`
- **Extracted Stylesheet Rules (`reelmotion-fit`)**:
- `html { line-height:1.15;-webkit-text-size-adjust:100% }`
- `before { box-sizing:border-box }`
- `pre { font-family:monospace;font-size:1em;white-space:pre-wrap }`
- `a:hover { color:336 }`
- `hover { color:inherit;text-decoration:none }`
- **Per-Selector Transition Rules**:
- **Selector `textarea`**: `transition: all .3s` extracted from `reelmotion-fit` stylesheet.
- **Selector `button`**: `transition: all .3s` extracted from `reelmotion-fit` stylesheet.
- **Selector `entor .elementor-background-video...`**: `transition: opacity 1s` extracted from `reelmotion-fit` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.47,0,.74,.71)`)**: Governs interactive state transitions across `<nav.elementor>` and `<section.elementor-element-rmhowsec>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `4938px` across 6 distinct viewport chapters using GSAP/ScrollTrigger.
- **Vertical Chapter Sequence**: Any workout video becomes a... (0%) -> Read once, run hands-free (21%) -> How it works (42%) -> Every plan unlocks the whol... (63%) -> Your next workout is one li... (84%) -> Footer (100%).
- **Hover Micro-Interaction (`primary_cta`)**: Animate `backgroundColor, boxShadow` with `0.2s, 0.2s ease, ease`.
- **Multi-Page Routes**: Scaffold internal routes `/support/` (other, MPA) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `reelmotion-fit`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | Any workout video becomes a routine you can | `1` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `21%` | Read once, run hands-free | `1` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `1700px` | `42%` | How it works | `1` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `2550px` | `63%` | Every plan unlocks the whole app | `1` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `3400px` | `84%` | Your next workout is one link away. | `1` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `4038px` | `100%` | Footer | `1` | [desktop-step-06.webp](assets/desktop-step-06.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | Any workout video becomes a routine you can | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `3168px` | `50%` | Run the workout | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `6336px` | `100%` | Footer | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `other` | `https://reelmotion.fit/support/` | Need a hand? | `2646px` | `MPA` (`4382ms`) | [subpage-01-support.webp](assets/subpage-01-support.webp) |

