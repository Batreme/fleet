# UI & UX Architecture: sibaldesign-com

## Overview & Design Identity
- **Target**: `sibaldesign-com` (**Jeff Sibal — Visual & Digital Designer · SIBALDESIGN**)
- **Production URL**: [https://sibaldesign.com/](https://sibaldesign.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#04060b` / `#131b2b`)
- **Summary**: Jeff Sibal, visual and digital designer in Southern California. Twenty-plus years across web, UI/UX, email, video and photography. I desi...
- **Total Clean CSS Variables Extracted**: `28` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Chakra Petch`
- **Body Font Stack**: `JetBrains Mono`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `15px`, `clamp(24px,3.6vw,34px)`, `10px`, `11px`, `9px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `15px`, `clamp(24px,3.6vw,34px)`, `10px`, `11px`, `9px`)
- **Body Copy**: rule `p` (`font-size: 15px`)
- **Metadata & Labels**: CSS variables `--mono: "JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace`; rule `small` (`font-size: 7px`, `letter-spacing: .22em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#04060b` | `var(--ink-000)` in `:root` |
| **Primary Typography Ink** | `#080c15` | `var(--ink-100)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0d1320` | `var(--ink-200)` in `:root` |
| **Interactive Accent / Highlight** | `#131b2b` | `var(--ink-300)` in `:root` |
| **Secondary / Muted Copy** | `#232e45` | `var(--line)` in `:root` |
| **Structural Hairline Border** | `#33415f` | `var(--line-hi)` in `:root` |
| **Variable Token (`--dim`)** | `#7f90b4` | `var(--dim)` in `:root` |
| **Variable Token (`--mid`)** | `#a3b4d4` | `var(--mid)` in `:root` |
| **Variable Token (`--fg`)** | `#c3d0e8` | `var(--fg)` in `:root` |
| **Variable Token (`--white`)** | `#eaf1ff` | `var(--white)` in `:root` |
| **Variable Token (`--accent`)** | `#5fe0ff` | `var(--accent)` in `:root` |
| **Variable Token (`--flash`)** | `#7ce9ff` | `var(--flash)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink-000` | `#04060b` | Typography Ink Token |
| `--ink-100` | `#080c15` | Typography Ink Token |
| `--ink-200` | `#0d1320` | Typography Ink Token |
| `--ink-300` | `#131b2b` | Typography Ink Token |
| `--panel` | `rgba(20,27,42,.66)` | Color / Atmospheric Token |
| `--panel-hi` | `rgba(30,40,60,.72)` | Color / Atmospheric Token |
| `--line` | `#232e45` | Color / Atmospheric Token |
| `--line-hi` | `#33415f` | Color / Atmospheric Token |
| `--dim` | `#7f90b4` | Color / Atmospheric Token |
| `--mid` | `#a3b4d4` | Color / Atmospheric Token |
| `--fg` | `#c3d0e8` | Typography Ink Token |
| `--white` | `#eaf1ff` | Canvas / Surface Token |
| `--accent` | `#5fe0ff` | Brand / Palette Token |
| `--flash` | `#7ce9ff` | Color / Atmospheric Token |
| `--accent-lo` | `rgba(95,224,255,.14)` | Brand / Palette Token |
| `--mono` | `"JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav> — `sibaldesign-com`)**:
   - Landmark `<header class="nav">` hosting `Jeff Sibal — Visual & Digital Design` navigation (`PROFILE · PROJECTS · EXPERIENCE · PHOTOS · EQUIPMENT`), DOM attributes (`data-boot="splash"`, `data-line`, `data-nav`, `data-text="A VISUAL &"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.boot> — `A VISUAL & DIGITAL DESIGNER`)**:
   - Landmark `<section class="boot">` presenting display lead `A VISUAL & DIGITAL DESIGNER` and copy excerpt *"JEFF SIBAL · PRESENTS"* over `#04060b` canvas and `#33415f` ink.
3. **Primary Showcase & Content Grid (<section.boot> — `PROFILE`)**:
   - Landmark `<section class="boot">` rendering section `PROFILE` with copy *"EST.2000 [PORTFOLIO / 2026]"*, asset references (`favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`, `fonts.googleapis.com`), and grid rule `body { height:100% }`.
4. **Interactive Detail & Feature Matrix (<section.hero> — `PROJECTS`)**:
   - Landmark `<section class="hero">` framing `PROJECTS` and `Video Testimonial Service` (*"ENGINEERED IN VANILLA JS ◤"*) with `#0d1320` surface cards, `#131b2b` accents, and `button { font:inherit;color:inherit;background:none;border:0;cursor:pointer }`.
5. **Colophon & Global Directory Footer (<footer.foot> — `https://sibaldesign.com/`)**:
   - Landmark `<footer class="foot">` anchoring `Jeff Sibal — Visual & Digital De` footer links (`PROFILE · PROJECTS · EXPERIENCE · PHOTOS · EQUIPMENT`), copy *"COPYRIGHT 2026 · CREATED BY JEFF SIBAL"*, and `#33415f` structural dividers.
