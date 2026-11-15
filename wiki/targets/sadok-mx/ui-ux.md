# UI & UX Architecture: sadok-mx

## Overview & Design Identity
- **Target**: `sadok-mx` (**Sadok Cervantes · \Designer \Engineer \Entrepreneur**)
- **Production URL**: [https://sadok.mx/](https://sadok.mx/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#202020` / `#3890f8`)
- **Summary**: Sadok Cervantes designs and builds products that have reached over 100 million people. He is one of Fast Company’s Most Innovative People.
- **Total Clean CSS Variables Extracted**: `76` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Emerald Bold`
- **Body Font Stack**: `Handjet`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--font-display: Handjet, system-ui, sans-serif`, `--kh-display: contents`; rule `h1` (`font-size: 32px`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`)
- **Body Copy**: rule `p` (`font-size: 16px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(18px,4.4vw + 4px,44px)`, `clamp(17px,15px + .4vw,20px)`, `10px`, `clamp(13px,2.6vw + 4px,22px)`, `15px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#202020` | `var(--box-ink)` in `:root` |
| **Primary Typography Ink** | `#a0a0a0` | `var(--box-gap)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f8f8f8` | `var(--box-fill)` in `:root` |
| **Interactive Accent / Highlight** | `#3890f8` | `var(--exp)` in `:root` |
| **Secondary / Muted Copy** | `#b8d8f8` | `var(--exp-flash)` in `:root` |
| **Structural Hairline Border** | `#0f1110` | `var(--bg-0)` in `:root` |
| **Variable Token (`--bg-1`)** | `#171a18` | `var(--bg-1)` in `:root` |
| **Variable Token (`--bg-2`)** | `#232724` | `var(--bg-2)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--box-ink` | `#202020` | Typography Ink Token |
| `--box-gap` | `#a0a0a0` | Layout / Spatial Grid Token |
| `--box-fill` | `#f8f8f8` | Color / Atmospheric Token |
| `--pad` | `calc(2 * var(--u) + 28px)` | Layout / Spatial Grid Token |
| `--ratio` | `2725 / 4368` | Design System Custom Token |
| `--exp` | `#3890f8` | Color / Atmospheric Token |
| `--exp-flash` | `#b8d8f8` | Color / Atmospheric Token |
| `--delay` | `calc(var(--i) * .2s)` | Motion / Easing Token |
| `--fill` | `calc(var(--n) * 32ms)` | Design System Custom Token |
| `--slot` | `36px` | Dimension / Scale Token |
| `--back-bottom` | `calc(2 * (var(--gutter) + env(safe-area-inset-top)) + 46px)` | Dimension / Scale Token |
| `--px` | `2px` | Dimension / Scale Token |
| `--sep` | `2.8em` | Dimension / Scale Token |
| `--bg-0` | `#0f1110` | Canvas / Surface Token |
| `--bg-1` | `#171a18` | Canvas / Surface Token |
| `--bg-2` | `#232724` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.meta> — `sadok-mx`)**:
   - Landmark `<header class="meta">` hosting `Sadok Cervantes · \Designer \Enginee` navigation (`BACK`), DOM attributes (`data-island="ready"`, `data-gb-state="loading"`, `data-gb-load="background"`, `data-gb-view="device"`), and stylesheet rule `.ab-footer { animation:.2s ease-out backwards ab-in }`.
2. **Hero Stage & Focal Lead (<section.landing-list> — `Sadok Cervantes, Product Designer `)**:
   - Landmark `<section class="landing-list">` presenting display lead `Sadok Cervantes, Product Designer and Engineer` and copy excerpt *"Sadok Cervantes is a"* over `#202020` canvas and `#f8f8f8` ink.
3. **Primary Showcase & Content Grid (<section.landing-list> — `Projects`)**:
   - Landmark `<section class="landing-list">` rendering section `Projects` with copy *"\Designer \Engineer \Entrepreneur"*, asset references (`fonts.googleapis.com`, `fonts.gstatic.com`, `css2`, `sitemap-index.xml`), and grid rule `.ab { --box-ink:202020;--box-gap:a0a0a0;--box-fill:f8f8f8;--u:4px;font-family:... }`.
4. **Interactive Detail & Feature Matrix (<section.landing-list> — `\Designer \Engineer \Entrepreneur`)**:
   - Landmark `<section class="landing-list">` framing `\Designer \Engineer \Entrepreneur` and `You are player/visitor # 64,248` (*"You are player/visitor # 64,248"*) with `#f8f8f8` surface cards, `#3890f8` accents, and `.ab-footer :focus-visible { outline-color:currentColor }`.
5. **Colophon & Global Directory Footer (<footer.meta__is> — `https://sadok.mx/`)**:
   - Landmark `<footer class="meta__is">` anchoring `Sadok Cervantes · \Designer \Eng` footer links (`BACK`), copy *"You are player/visitor"*, and `#0f1110` structural dividers.
