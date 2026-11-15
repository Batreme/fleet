# UI & UX Architecture: chanpan-com-ar

## Overview & Design Identity
- **Target**: `chanpan-com-ar` (**ChanPan · AI Video Production, Commercials & Creative Studio — Argentina**)
- **Production URL**: [https://chanpan.com.ar](https://chanpan.com.ar)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#C1BBAE` canvas, `#17130D` ink, `#F15A24` accent)
- **Summary**: AI-driven video production, commercials, branded content, branding and 2D/3D animation. A creative studio from Corrientes, Argentina, wor...
- **Total Clean CSS Variables Extracted**: `12` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **Hero Display (`H1`)**: CSS variables `--display: 'Archivo',sans-serif`
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(26px,3.2vw,42px)`, `font-weight: 800`)
- **Body Copy**: CSS variables `--body: 'Inter',system-ui,sans-serif`; rule `body` (`line-height: 1.6`)
- **Metadata & Labels**: CSS variables `--mono: 'JetBrains Mono',ui-monospace,monospace`; rule `small` (`font-size: 9.5px`, `letter-spacing: .14em`, `font-weight: 600`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#C1BBAE` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#17130D` | `var(--ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#524B3D` | `var(--ink-soft)` in `:root` |
| **Interactive Accent / Highlight** | `#F15A24` | `var(--brand)` in `:root` |
| **Secondary / Muted Copy** | `#A8360C` | `var(--brand-text)` in `:root` |
| **Structural Hairline Border** | `#EEE9DE` | `var(--paper)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#C1BBAE` | Canvas / Surface Token |
| `--ink` | `#17130D` | Typography Ink Token |
| `--ink-soft` | `#524B3D` | Typography Ink Token |
| `--brand` | `#F15A24` | Brand / Palette Token |
| `--brand-text` | `#A8360C` | Typography Ink Token |
| `--paper` | `#EEE9DE` | Canvas / Surface Token |
| `--line` | `rgba(23,19,13,.16)` | Color / Atmospheric Token |
| `--display` | `'Archivo',sans-serif` | Dimension / Scale Token |
| `--body` | `'Inter',system-ui,sans-serif` | Dimension / Scale Token |
| `--mono` | `'JetBrains Mono',ui-monospace,monospace` | Typography / Scale Token |
| `--mx` | `clamp(22px,5.5vw,88px)` | Dimension / Scale Token |
| `--band-bottom` | `0px` | Dimension / Scale Token |
| `--chanpan-com-ar-bg` | `#C1BBAE` | Canvas Substrate (from `var(--bg)` in `:root`) |
| `--chanpan-com-ar-ink` | `#17130D` | Primary Typography Ink (stylesheet-derived) |
| `--chanpan-com-ar-surface` | `#524B3D` | Surface Substrate (stylesheet-derived) |
| `--chanpan-com-ar-accent` | `#F15A24` | Interactive Accent (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.hd> — `chanpan-com-ar`)**:
   - Landmark `<header class="hd">` hosting `ChanPan · AI Video Production, Comme` navigation (`Home · Demo Reel · Services · Work · Contact`), DOM attributes (`data-clip="s1-loop"`, `data-clip="s2-scrub"`, `data-scrub`, `data-clip="s3-scrub"`), and stylesheet rule `html { -webkit-text-size-adjust:100% }`.
2. **Hero Stage & Focal Lead (<section.hero> — `ChanPan — AI video production and `)**:
   - Landmark `<section class="hero">` presenting display lead `ChanPan — AI video production and creative studio` and copy excerpt *"Message us on WhatsApp"* over `#C1BBAE` canvas and `#17130D` ink.
3. **Primary Showcase & Content Grid (<section.drive> — `First, perspective.`)**:
   - Landmark `<section class="drive">` rendering section `First, perspective.` with copy *"Corrientes, Argentina"*, asset references (`favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `body.is-loading { overflow:hidden }`.
4. **Interactive Detail & Feature Matrix (<section.drive> — `Our terrain.`)**:
   - Landmark `<section class="drive">` framing `Our terrain.` and `Twenty years climbing.` (*"Production company"*) with `#524B3D` surface cards, `#F15A24` accents, and `button { font:inherit;color:inherit }`.
5. **Colophon & Global Directory Footer (<footer.ft> — `https://chanpan.com.ar`)**:
   - Landmark `<footer class="ft">` anchoring `ChanPan · AI Video Production, C` footer links (`Home · Demo Reel · Services · Work · Contact`), copy *"AI · Film · Design"*, and `#EEE9DE` structural dividers.
