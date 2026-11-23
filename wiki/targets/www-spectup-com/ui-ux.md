---
title: "UI & UX Architecture: www-spectup-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-spectup-com

## Overview & Design Identity
- **Target**: `www-spectup-com` (**Private Capital Advisory: Capital Raising and M&A · spectup**)
- **Production URL**: [https://www.spectup.com/](https://www.spectup.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#121212` / `#ffff00`)
- **Summary**: Private capital advisory with $760M+ advised, raised or placed since 2022: capital raising for companies and funds, fund placement and M&...
- **Total Clean CSS Variables Extracted**: `162` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 196px`, `line-height: 176.4px`, `font-weight: 620`, `letter-spacing: -10.192px`); CSS variables `--t-h1: clamp(30px,4.2vw,64px)`, `--kh-h1: 196.0px`; rule `.h1` (`font-size: clamp(19px,min(2.05vw,3.3vh),...`, `letter-spacing: -.018em`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 60.48px`, `line-height: 63.504px`, `font-weight: 500`, `letter-spacing: -1.69344px`); CSS variables `--t-h2: clamp(22px,2.5vw,36px)`; rule `h2` (`font-size: clamp(24px,2.9vw,52px)`, `line-height: 1.06`, `letter-spacing: -.032em`, `font-weight: 500`)
- **Body Copy**: live computed `body` (`font-size: 15px`, `line-height: 23.25px`, `font-weight: 400`, `letter-spacing: 0.03px`); CSS variables `--t-body: 15px`; rule `p` (`font-size: clamp(13px,1.05vw,17px)`, `line-height: 1.5`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 15px`, `line-height: 23.25px`, `font-weight: 400`, `letter-spacing: 0.03px`); CSS variables `--t-meta: 12.5px`, `--mono: ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospace`, `--ck-mono: ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospace`; rule `.meta` (`font-size: var(--t-meta)`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#121212` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#fafafa` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#1d1d1b` | `.btn--ink:hover { background: #1d1d1b }` |
| **Interactive Accent / Highlight** | `#ffff00` | `.navlinks a:hover i { color: yellow }` (`#ffff00`) |
| **Secondary / Muted Copy** | `#8a8a84` | `.trow .tt { color: #8a8a84 }` |
| **Structural Hairline Border** | `#323232` | `var(--line-d)` in `:root` (`rgba(250,250,250,.14)`) |
| **Variable Token (`--yellow`)** | `#f8f32b` | `var(--yellow)` in `:root` |
| **Variable Token (`--g-d`)** | `#8a8a8a` | `var(--g-d)` in `:root` |
| **Variable Token (`--g-l`)** | `#6b6b6b` | `var(--g-l)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--hero-vh` | `100svh` | Layout / Spatial Grid Token |
| `--hero-bar` | `0px` | Dimension / Scale Token |
| `--ink` | `#121212` | Typography Ink Token |
| `--light` | `#FAFAFA` | Canvas / Surface Token |
| `--yellow` | `#F8F32B` | Color / Atmospheric Token |
| `--g-d` | `#8A8A8A` | Color / Atmospheric Token |
| `--g-l` | `#6B6B6B` | Color / Atmospheric Token |
| `--line-d` | `rgba(250,250,250,.14)` | Color / Atmospheric Token |
| `--line-l` | `rgba(18,18,18,.13)` | Color / Atmospheric Token |
| `--t-hero` | `clamp(40px,6.4vw,102px)` | Dimension / Scale Token |
| `--t-h1` | `clamp(30px,4.2vw,64px)` | Typography / Scale Token |
| `--t-h2` | `clamp(22px,2.5vw,36px)` | Typography / Scale Token |
| `--t-h3` | `clamp(17px,1.6vw,21px)` | Typography / Scale Token |
| `--t-lede` | `clamp(16px,1.3vw,19px)` | Dimension / Scale Token |
| `--t-body` | `15px` | Dimension / Scale Token |
| `--t-meta` | `12.5px` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.mo> — `www-spectup-com`)**:
   - Landmark `<nav class="mo">` (`1440x92px`) hosting `Private Capital Advisory: Capital Ra` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-nosnippet`, `data-mnbound="1"`, `data-l="The firm"`, `data-lf-cf`), and stylesheet rule `view-transition { navigation:auto }`.
2. **Hero Stage & Focal Lead (<section.kh> — `PRIVATE CAPITAL ADVISORY : Access `)**:
   - Landmark `<section class="kh in">` presenting display lead `PRIVATE CAPITAL ADVISORY : Access to private capi...` and copy excerpt *"spectup is a private capital advisory firm running capital raisin"* over `#121212` canvas and `#fafafa` ink.
3. **Primary Showcase & Content Grid (<section.s--light> — `Private capital advisory : A c c e`)**:
   - Landmark `<section class="s--light">` rendering section `Private capital advisory : A c c e s s t o p r i...` with copy *"Private capital advisory :"*, asset references (`insight.min.js`, `favicon.ico`, `favicon-32.png`, `favicon-192.png`), and grid rule `from { opacity:0;transform:translateY(10px) }`.
4. **Interactive Detail & Feature Matrix (<section.s--flush> — `spectup’s track record`)**:
   - Landmark `<section class="s--light s--flush">` framing `spectup’s track record` and `How we get capital raises, M&A deals and secondar...` (*"p r i v a t e c a p i t a l ."*) with `#1d1d1b` surface cards, `#ffff00` accents, and `nav { view-transition-name:sitenav }`.
5. **Colophon & Global Directory Footer (<footer.ft> — `https://www.spectup.com/`)**:
   - Landmark `<footer class="ft has-canvas">` anchoring `Private Capital Advisory: Capita` footer links (`Overview · Index · Archive · About · Contact`), copy *"Top Capital Market Consulting Company 2026 18 Clutch reviews"*, and `#323232` structural dividers.
