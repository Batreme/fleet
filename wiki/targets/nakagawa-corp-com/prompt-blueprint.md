---
title: "UI Prompt Blueprint: nakagawa-corp-com"
date: 2026-11-15
target: "nakagawa-corp-com"
status: analyzed
capture: dom
capture_desktop: dom
capture_mobile: dom
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#202020` canvas, `#D6B996` ink, `#AD8A72` accent)"
---

# UI Design System & Master Generation Blueprint: nakagawa-corp-com

> **久留米・うきはで注文住宅を建てるなら株式会社ナカガワ（ナカガワホーム）** (https://nakagawa-corp.com/) — 【1963年創業、久留米・うきはで60年以上】株式会社ナカガワ(本社:福岡県久留米市)は、真っ白な図面から一邸ずつ設計する完全自由設計の工務店です。注文住宅・分譲住宅・土地探しまで、暮らしに合わせてご提案します。

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **久留米・うきはで注文住宅を建てるなら株式会社ナカガワ（ナカガワホーム）** (`https://nakagawa-corp.com/`). 【1963年創業、久留米・うきはで60年以上】株式会社ナカガワ(本社:福岡県久留米市)は、真っ白な図面から一邸ずつ設計する完全自由設計の工務店です。注文住宅・分譲住宅・土地探しまで、暮らしに合わせてご提案します。
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#202020` canvas, `#D6B996` ink, `#AD8A72` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#202020` (`var(--clr-primary-default)` in `:root`) paired with `#D6B996` primary typography and `#AD8A72` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Cardo` for display copy (`あなたは出会う。 思い描く、その先の暮らしに。`) with `Jost` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `767px` container bounds (`gap: 24px`, padding `1.5rem`) with `cubic-bezier(0.4,0,0.2,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `767px` extracted from `nakagawa-corp-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `1.5rem` lateral canvas padding with `24px` grid gap.
- **Border Radius Scale**: `var(--leap-project-radius-default)`, `var(--leap-project-radius-none)`, `var(--leap-project-radius-max)`, `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 767px`, `gap: 24px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1.5rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width: 767px)`, `@media screen and (min-width: 768px)`, `@media screen and (max-width: 47.9375em)`, `@media screen and (max-width: 67.5em)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#202020` | `var(--clr-primary-default)` in `:root` |
| **Primary Typography Ink** | `#0F0F0F` | `var(--clr-primary-dark)` in `:root` |
| **Elevated Surface / Card Substrate** | `#4A4A4A` | `var(--clr-primary-light)` in `:root` |
| **Interactive Accent / Highlight** | `#AD8A72` | `var(--clr-secondary-default)` in `:root` |
| **Secondary / Muted Copy** | `#5F433E` | `var(--clr-secondary-dark)` in `:root` |
| **Structural Hairline Border** | `#D6B996` | `var(--clr-secondary-light)` in `:root` |
| **Variable Token (`--leap-project-main`)** | `#0073aa` | `var(--leap-project-main)` in `:root` |
| **Variable Token (`--leap-project-text-primary`)** | `#404044` | `var(--leap-project-text-primary)` in `:root` |
| **Variable Token (`--leap-project-wh`)** | `#fff` | `var(--leap-project-wh)` in `:root` |
| **Variable Token (`--leap-project-bg`)** | `#F7F7F4` | `var(--leap-project-bg)` in `:root` |
| **Variable Token (`--leap-project-mono-01`)** | `#F2F2F2` | `var(--leap-project-mono-01)` in `:root` |
| **Variable Token (`--leap-project-mono-02`)** | `#BABDC4` | `var(--leap-project-mono-02)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--leap-project-main` | `var(--clr-primary-default, #0073aa)` | Color / Atmospheric Token |
| `--leap-project-text-primary` | `var(--clr-text-primary, #404044)` | Typography Ink Token |
| `--leap-project-wh` | `var(--clr-wht, #fff)` | Color / Atmospheric Token |
| `--leap-project-bg` | `var(--clr-bg-01, #F7F7F4)` | Canvas / Surface Token |
| `--leap-project-mono-01` | `var(--clr-mono-01, #F2F2F2)` | Typography / Scale Token |
| `--leap-project-mono-02` | `var(--clr-mono-03, #BABDC4)` | Typography / Scale Token |
| `--leap-project-bold` | `var(--font-weight-bold, 600)` | Design System Custom Token |
| `--leap-project-radius-none` | `0` | Elevation / Border Token |
| `--leap-project-radius-default` | `var(--border-radius-primary, .5rem)` | Elevation / Border Token |
| `--leap-project-radius-max` | `var(--border-radius-max, 100vmax)` | Elevation / Border Token |
| `--fz` | `16` | Design System Custom Token |
| `--rem` | `calc(1 / var(--fz) * 1rem)` | Dimension / Scale Token |
| `--header-hgt` | `96` | Layout / Spatial Grid Token |
| `--header-hgt-fx` | `80` | Layout / Spatial Grid Token |
| `--inner-xs` | `720` | Design System Custom Token |
| `--inner-sm` | `1080` | Design System Custom Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Cardo`.
- **Primary Body Stack**: `Jost`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--font-en-display: "Cardo", serif`, `--display-lg: 160`, `--display-md: 120`.
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--font-size-heading6)`, `0.875rem`, `1rem`, `1.125rem`, `0.75rem`).
- **Body Copy**: rule `body` (`line-height: 1`).
- **Metadata & Navigation Labels**: CSS variables `--leap-project-mono-01: var(--clr-mono-01, #F2F2F2)`, `--leap-project-mono-02: var(--clr-mono-03, #BABDC4)`, `--clr-mono-01: #EEEEEE`; rule `small` (`font-size: max(12px, 0.875rem)`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.4,0,0.2,1)`, `cubic-bezier(0.77,0,0.18,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `:hover`**: `transition: var(--transit-default)` extracted from `nakagawa-corp-com` stylesheet.
- **Selector `svg`**: `transition: var(--transit-default)` extracted from `nakagawa-corp-com` stylesheet.
- **Selector `dia (prefers-reduced-motion: no-p...`**: `transition: opacity 0.6s ease-out, translate 0.6s ease-out` extracted from `nakagawa-corp-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.4,0,0.2,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.home-works>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.home-intro>` and `<section.home-works>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — 久留米・うきはで注文住宅を建てるなら株式会社ナカガワ（ナカガワホーム）        │
│ ====================================================================== │
│ [ <header.header>          | ナカガワホームの家づくり · 私たちについて · 快適な住まいづくり · 徹 ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.home-intro>                                 |   │
│ | H1: あなたは出会う。 思い描く、その先の暮らしに。                                      |   │
│ | Substrate: #202020    | Ink: #D6B996    | Accent: #AD8A72        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.home-works>      ) max-w: 767px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | 「応える」だけでなく、 「提案する」。          |  | ご要望の、その先まで。                  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 24px  ) | │
│ | [<header.header>] -> [<section.home-intr] -> [<section.home-work] |  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>       ) | https://nakagawa-corp.com/         │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.header> — `nakagawa-corp-com`)**:
   - Landmark `<header class="header header-main">` hosting `久留米・うきはで注文住宅を建てるなら株式会社ナカガワ（ナカガワホーム）` navigation (`ナカガワホームの家づくり · 私たちについて · 快適な住まいづくり · 徹底したこだわり · 家づくりの流れ・アフターサポート`), DOM attributes (`data-js-parallax`, `data-speed="-0.08"`, `data-speed="0.05"`, `data-speed="-0.12"`), and stylesheet rule `.leap_table thead th { background-color: var(--leap-project-main); color: var(--leap-project-wh); }`.
2. **Hero Stage & Focal Lead (<section.home-intro> — `あなたは出会う。 思い描く、その先の暮らしに。`)**:
   - Landmark `<section class="home-intro">` presenting display lead `あなたは出会う。 思い描く、その先の暮らしに。` and copy excerpt *"Tel.0120-168-350 10:00–18:00 CLOSE 火曜日・水曜日"* over `#202020` canvas and `#D6B996` ink.
3. **Primary Showcase & Content Grid (<section.home-works> — `「応える」だけでなく、 「提案する」。`)**:
   - Landmark `<section class="home-works">` rendering section `「応える」だけでなく、 「提案する」。` with copy *"10:00–18:00 CLOSE 火曜日・水曜日"*, asset references (`gtm.js`, `embed`, `front.css`, `style.css`), and grid rule `.box--ttl { font-size: var(--font-size-heading6); font-family: var(--font-jp-heading); }`.
4. **Interactive Detail & Feature Matrix (<section.home-event> — `ご要望の、その先まで。`)**:
   - Landmark `<section class="home-event section_pdg-md-top">` framing `ご要望の、その先まで。` and `提案のための、余白を残す。` (*"あなたは出会う。 思い描く、その先の暮らしに。"*) with `#4A4A4A` surface cards, `#AD8A72` accents, and `.leap_box.leap_box-01 { padding: 1rem 1.5rem; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://nakagawa-corp.com/`)**:
   - Landmark `<footer class="footer">` anchoring `久留米・うきはで注文住宅を建てるなら株式会社ナカガワ（ナカガワホ` footer links (`ナカガワホームの家づくり · 私たちについて · 快適な住まいづくり · 徹底したこだわり · 家づくりの流れ・アフターサポート`), copy *"福岡・佐賀・大分で60年以上。 まだ言葉になっていない理想まで、形にする工務店。"*, and `#D6B996` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: nakagawa-corp-com (久留米・うきはで注文住宅を建てるなら株式会社ナカガワ（ナカガワホーム）)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `nakagawa-corp-com` (**久留米・うきはで注文住宅を建てるなら株式会社ナカガワ（ナカガワホーム）** — `https://nakagawa-corp.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#202020` canvas, `#D6B996` ink, `#AD8A72` accent).
- **Identity & Domain Context**: 【1963年創業、久留米・うきはで60年以上】株式会社ナカガワ(本社:福岡県久留米市)は、真っ白な図面から一邸ずつ設計する完全自由設計の工務店です。注文住宅・分譲住宅・土地探しまで、暮らしに合わせてご提案します。
- **Primary Substrate**: `#202020` (`var(--clr-primary-default)` in `:root`), **Primary Ink**: `#D6B996`, **Accent / Highlight**: `#AD8A72`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#202020` (`var(--clr-primary-default)` in `:root`) paired with `#D6B996` primary typography and `#AD8A72` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Cardo` for display copy (`あなたは出会う。 思い描く、その先の暮らしに。`) with `Jost` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `767px` container bounds (`gap: 24px`, padding `1.5rem`) with `cubic-bezier(0.4,0,0.2,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `nakagawa-corp-com` in your global stylesheet:

:root {
  /* 久留米・うきはで注文住宅を建てるなら株式会社ナカガワ（ナカガワホーム） (nakagawa-corp-com) — Ground-Truth Extracted CSS Variables */
  --leap-project-main: var(--clr-primary-default, #0073aa); /* Color / Atmospheric Token (nakagawa-corp-com) */
  --leap-project-text-primary: var(--clr-text-primary, #404044); /* Typography Ink Token (nakagawa-corp-com) */
  --leap-project-wh: var(--clr-wht, #fff); /* Color / Atmospheric Token (nakagawa-corp-com) */
  --leap-project-bg: var(--clr-bg-01, #F7F7F4); /* Canvas / Surface Token (nakagawa-corp-com) */
  --leap-project-mono-01: var(--clr-mono-01, #F2F2F2); /* Typography / Scale Token (nakagawa-corp-com) */
  --leap-project-mono-02: var(--clr-mono-03, #BABDC4); /* Typography / Scale Token (nakagawa-corp-com) */
  --leap-project-bold: var(--font-weight-bold, 600); /* Design System Custom Token (nakagawa-corp-com) */
  --leap-project-radius-none: 0; /* Elevation / Border Token (nakagawa-corp-com) */
  --leap-project-radius-default: var(--border-radius-primary, .5rem); /* Elevation / Border Token (nakagawa-corp-com) */
  --leap-project-radius-max: var(--border-radius-max, 100vmax); /* Elevation / Border Token (nakagawa-corp-com) */
  --fz: 16; /* Design System Custom Token (nakagawa-corp-com) */
  --rem: calc(1 / var(--fz) * 1rem); /* Dimension / Scale Token (nakagawa-corp-com) */
  --header-hgt: 96; /* Layout / Spatial Grid Token (nakagawa-corp-com) */
  --header-hgt-fx: 80; /* Layout / Spatial Grid Token (nakagawa-corp-com) */
  --inner-xs: 720; /* Design System Custom Token (nakagawa-corp-com) */
  --inner-sm: 1080; /* Design System Custom Token (nakagawa-corp-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#202020` — grounded in `var(--clr-primary-default)` in `:root`
- **Primary Typography Ink**: `#0F0F0F` — grounded in `var(--clr-primary-dark)` in `:root`
- **Elevated Surface / Card Substrate**: `#4A4A4A` — grounded in `var(--clr-primary-light)` in `:root`
- **Interactive Accent / Highlight**: `#AD8A72` — grounded in `var(--clr-secondary-default)` in `:root`
- **Secondary / Muted Copy**: `#5F433E` — grounded in `var(--clr-secondary-dark)` in `:root`
- **Structural Hairline Border**: `#D6B996` — grounded in `var(--clr-secondary-light)` in `:root`
- **Variable Token (`--leap-project-main`)**: `#0073aa` — grounded in `var(--leap-project-main)` in `:root`
- **Variable Token (`--leap-project-text-primary`)**: `#404044` — grounded in `var(--leap-project-text-primary)` in `:root`
- **Variable Token (`--leap-project-wh`)**: `#fff` — grounded in `var(--leap-project-wh)` in `:root`
- **Variable Token (`--leap-project-bg`)**: `#F7F7F4` — grounded in `var(--leap-project-bg)` in `:root`
- **Variable Token (`--leap-project-mono-01`)**: `#F2F2F2` — grounded in `var(--leap-project-mono-01)` in `:root`
- **Variable Token (`--leap-project-mono-02`)**: `#BABDC4` — grounded in `var(--leap-project-mono-02)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `767px` extracted from `nakagawa-corp-com` stylesheet
- **Padding & Gutters**: `1.5rem` lateral canvas padding with `24px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 767px`, `gap: 24px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1.5rem` horizontal padding
- **Media Queries**: `@media screen and (max-width: 767px)`, `@media screen and (min-width: 768px)`, `@media screen and (max-width: 47.9375em)`, `@media screen and (max-width: 67.5em)`
- **Corner Radii**: `var(--leap-project-radius-default)`, `var(--leap-project-radius-none)`, `var(--leap-project-radius-max)`, `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Cardo`
- **Body Font Stack**: `Jost`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--font-en-display: "Cardo", serif`, `--display-lg: 160`, `--display-md: 120`
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--font-size-heading6)`, `0.875rem`, `1rem`, `1.125rem`, `0.75rem`)
- **Body Copy Rule**: rule `body` (`line-height: 1`)
- **Metadata & Index Rule**: CSS variables `--leap-project-mono-01: var(--clr-mono-01, #F2F2F2)`, `--leap-project-mono-02: var(--clr-mono-03, #BABDC4)`, `--clr-mono-01: #202020`; rule `small` (`font-size: max(12px, 0.875rem)`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `nakagawa-corp-com` (`久留米・うきはで注文住宅を建てるなら株式会社ナカガワ（ナカガワホーム）`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header> — `nakagawa-corp-com`)**:
   - DOM & Selectors: Landmark `<header class="header header-main">` hosting `久留米・うきはで注文住宅を建てるなら株式会社ナカガワ（ナカガワホーム）` navigation (`ナカガワホームの家づくり · 私たちについて · 快適な住まいづくり · 徹底したこだわり · 家づくりの流れ・アフターサポート`), DOM attributes (`data-js-parallax`, `data-speed="-0.08"`, `data-speed="0.05"`, `data-speed="-0.12"`), and stylesheet rule `.leap_table thead th { background-color: var(--leap-project-main); color: var(--leap-project-wh); }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header> — `nakagawa-corp-com`)` (`nakagawa-corp-com`) adapts across `@media screen and (max-width: 767px)`, `@media screen and (min-width: 768px)`, `@media screen and (max-width: 47.9375em)`, `@media screen and (max-width: 67.5em)` with `cubic-bezier(0.4,0,0.2,1)`, `cubic-bezier(0.77,0,0.18,1)` transitions and links `ナカガワホームの家づくり · 私たちについて · 快適な住まいづくり · 徹底したこだわり · 家づくりの流れ・アフターサポート`.
2. **Hero Stage & Focal Lead (<section.home-intro> — `あなたは出会う。 思い描く、その先の暮らしに。`)**:
   - DOM & Selectors: Landmark `<section class="home-intro">` presenting display lead `あなたは出会う。 思い描く、その先の暮らしに。` and copy excerpt *"Tel.0120-168-350 10:00–18:00 CLOSE 火曜日・水曜日"* over `#202020` canvas and `#D6B996` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#202020` background with `#D6B996` headline `あなたは出会う。 思い描く、その先の暮らしに。`.
3. **Primary Showcase & Content Grid (<section.home-works> — `「応える」だけでなく、 「提案する」。`)**:
   - DOM & Selectors: Landmark `<section class="home-works">` rendering section `「応える」だけでなく、 「提案する」。` with copy *"10:00–18:00 CLOSE 火曜日・水曜日"*, asset references (`gtm.js`, `embed`, `front.css`, `style.css`), and grid rule `.box--ttl { font-size: var(--font-size-heading6); font-family: var(--font-jp-heading); }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.home-works> — `「応える」だけでなく、 「提案する」。`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 767px`, `gap: 24px`) on desktop and Single-column vertical stack at `390px` viewport width with `1.5rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.home-event> — `ご要望の、その先まで。`)**:
   - DOM & Selectors: Landmark `<section class="home-event section_pdg-md-top">` framing `ご要望の、その先まで。` and `提案のための、余白を残す。` (*"あなたは出会う。 思い描く、その先の暮らしに。"*) with `#4A4A4A` surface cards, `#AD8A72` accents, and `.leap_box.leap_box-01 { padding: 1rem 1.5rem; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.home-event> — `ご要望の、その先まで。`)` uses `var(--leap-project-radius-default)`, `var(--leap-project-radius-none)`, `var(--leap-project-radius-max)`, `50%` radii, `#AD8A72` highlights, and assets (gtm.js, embed, front.css).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://nakagawa-corp.com/`)**:
   - DOM & Selectors: Landmark `<footer class="footer">` anchoring `久留米・うきはで注文住宅を建てるなら株式会社ナカガワ（ナカガワホ` footer links (`ナカガワホームの家づくり · 私たちについて · 快適な住まいづくり · 徹底したこだわり · 家づくりの流れ・アフターサポート`), copy *"福岡・佐賀・大分で60年以上。 まだ言葉になっていない理想まで、形にする工務店。"*, and `#D6B996` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://nakagawa-corp.com/`)` aligns to `767px` extracted from `nakagawa-corp-com` stylesheet with `1.5rem` lateral canvas padding with `24px` grid gap and attributes (data-js-parallax, data-speed="-0.08", data-speed="0.05").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Tel.0120-168-350 10:00–18:00 CLOSE 火曜日・水曜日"*
- Copy Excerpt 2: *"10:00–18:00 CLOSE 火曜日・水曜日"*
- Copy Excerpt 3: *"あなたは出会う。 思い描く、その先の暮らしに。"*
- Copy Excerpt 4: *"福岡・佐賀・大分で60年以上。 まだ言葉になっていない理想まで、形にする工務店。"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.4,0,0.2,1)`, `cubic-bezier(0.77,0,0.18,1)`
- **Extracted Stylesheet Rules (`nakagawa-corp-com`)**:
- `.leap_table thead th { background-color: var(--leap-project-main); color: var(--leap-project-wh); }`
- `.box--ttl { font-size: var(--font-size-heading6); font-family: var(--font-jp-heading); }`
- `.leap_box.leap_box-01 { padding: 1rem 1.5rem; }`
- `.leap_box.leap_box-02 { padding: 1rem 1.5rem; }`
- `.leap_box.leap_box-02-2 { padding: 1rem 1.5rem; }`
- **Per-Selector Transition Rules**:
- **Selector `:hover`**: `transition: var(--transit-default)` extracted from `nakagawa-corp-com` stylesheet.
- **Selector `svg`**: `transition: var(--transit-default)` extracted from `nakagawa-corp-com` stylesheet.
- **Selector `dia (prefers-reduced-motion: no-p...`**: `transition: opacity 0.6s ease-out, translate 0.6s ease-out` extracted from `nakagawa-corp-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.4,0,0.2,1)`)**: Governs interactive state transitions across `<header.header>` and `<section.home-works>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.home-intro>` and `<section.home-works>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `nakagawa-corp-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
