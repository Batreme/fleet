# UI & UX Architecture: www-vibr-studio

## Overview & Design Identity
- **Target**: `www-vibr-studio` (**Vibr — Figma to code for designers who ship**)
- **Production URL**: [https://www.vibr.studio/](https://www.vibr.studio/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f5f5f7` / `#1d1d1f`)
- **Summary**: Your design is the code. Vibr compiles your Figma file into a real, responsive Next.js site you own, edit with Claude Code or Codex, and...
- **Total Clean CSS Variables Extracted**: `80` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter Fallback`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--m-h1: 32px`, `--m-h1-lh: 1.1`
- **Section Heading (`H2`)**: CSS variables `--m-h2: 24px`, `--m-h2-lh: 1.2`
- **Body Copy**: CSS variables `--m-body: 16px`, `--m-body-lh: 1.4`
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(16px,5.8cqi,42px)`, `clamp(16px,1.04cqw,20px)`, `15px`, `var(--m-h2)`, `var(--m-body)`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f5f5f7` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--surface)` in `:root` |
| **Elevated Surface / Card Substrate** | `#e8e8ed` | `var(--surface-hover)` in `:root` |
| **Interactive Accent / Highlight** | `#1d1d1f` | `var(--text)` in `:root` |
| **Secondary / Muted Copy** | `#6e6e73` | `var(--text-secondary)` in `:root` |
| **Structural Hairline Border** | `#aeaeb2` | `var(--text-tertiary)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--panel-w` | `min(440px,calc(100vw - 40px))` | Dimension / Scale Token |
| `--panel-h` | `calc(100dvh - 100px)` | Dimension / Scale Token |
| `--panel-inset` | `20px` | Dimension / Scale Token |
| `--content-top` | `65px` | Dimension / Scale Token |
| `--bleed` | `32px` | Dimension / Scale Token |
| `--gutter` | `clamp(20px,7vw,56px)` | Layout / Spatial Grid Token |
| `--card-zoom` | `.6` | Design System Custom Token |
| `--hero-mark` | `316px` | Dimension / Scale Token |
| `--hero-gap` | `clamp(32px,3.34cqw,64px)` | Layout / Spatial Grid Token |
| `--hero-bottom-block` | `199px` | Dimension / Scale Token |
| `--hero-bottom-offset` | `clamp(90px,8cqw,154px)` | Dimension / Scale Token |
| `--hero-clear` | `24px` | Dimension / Scale Token |
| `--hero-phone-top` | `70px` | Dimension / Scale Token |
| `--watch-card-w` | `246px` | Dimension / Scale Token |
| `--watch-card-h` | `239.38px` | Dimension / Scale Token |
| `--watch-card-right` | `clamp(20px,2.76cqw,53px)` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.hero-module__sup1Jq__hero> — `www-vibr-studio`)**:
   - Landmark `<header class="hero-module__sup1Jq__hero">` hosting `Vibr — Figma to code for designers w` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-dgst="BAILOUT_TO_CLIENT_SID..."`, `data-landing-section="hero"`), and stylesheet rule `.about-me-module__qpLcqW__headlin... { width:100%;display:block }`.
2. **Hero Stage & Focal Lead (<main.landing-page-module__p_mWBW__page> — `Vibr : Figma to code for designers`)**:
   - Landmark `<main class="landing-page-module__p_mWBW__page">` presenting display lead `Vibr : Figma to code for designers who ship` and copy excerpt *"Your design is the code - Your design is the code - Your design i"* over `#f5f5f7` canvas and `#1d1d1f` ink.
3. **Primary Showcase & Content Grid (<main.landing-page-module__p_mWBW__page> — `Vibr starts with your actual desig`)**:
   - Landmark `<main class="landing-page-module__p_mWBW__page">` rendering section `Vibr starts with your actual design.` with copy *"Your design is the code -"*, asset references (`83afe278b6a6bb3c-s.p.3a6ba036.woff2`, `8780dfd0812b997c-s.p.5704523e.woff2`, `8800dfc60902df36-s.p.d48c4d68.woff2`, `Grain_Variable_Trial-s.p.2731fd70...`), and grid rule `.about-me-module__qpLcqW__authorIcon { flex-shrink:0;width:22px;height:22px;position:relative }`.
4. **Interactive Detail & Feature Matrix (<main.landing-page-module__p_mWBW__page> — `Figma Build your sections`)**:
   - Landmark `<main class="landing-page-module__p_mWBW__page">` framing `Figma Build your sections` and `Compile Click to edit anything` (*": Figma to code for designers who ship"*) with `#e8e8ed` surface cards, `#1d1d1f` accents, and `.about-me-module__qpLcqW__authorG... { width:62.5%;height:62.5%;position:absolute;top:18.87%;left:18.75%;overfl... }`.
5. **Colophon & Global Directory Footer (<footer.landing-footer-module__8-2yDa__root> — `https://www.vibr.studio/`)**:
   - Landmark `<footer class="landing-footer-module__8-2yDa__root">` anchoring `Vibr — Figma to code for designe` footer links (`Overview · Index · Archive · About · Contact`), copy *"Vibr Studio came out of years of handoff frustration. I got "*, and `#aeaeb2` structural dividers.
