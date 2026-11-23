---
title: "UI & UX Architecture: sibaldesign-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: sibaldesign-com

## Overview & Design Identity
- **Target**: `sibaldesign-com` (**Jeff Sibal — Visual & Digital Designer · SIBALDESIGN**)
- **Production URL**: [https://sibaldesign.com/](https://sibaldesign.com/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#080c15` / `#5fe0ff`)
- **Summary**: Jeff Sibal, visual and digital designer in Southern California. Twenty-plus years across web, UI/UX, email, video and photography. I desi...
- **Total Clean CSS Variables Extracted**: `28` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Chakra Petch`
- **Body Font Stack**: `Chakra Petch`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 104px`, `line-height: 97.76px`, `font-weight: 700`, `letter-spacing: -0.52px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 34px`, `line-height: 54.4px`, `font-weight: 600`, `letter-spacing: 6.12px`)
- **Body Copy**: live computed `body` (`font-size: 15px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: 15px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 11px`, `line-height: 17.6px`, `font-weight: 400`, `letter-spacing: 2.64px`); CSS variables `--mono: "JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace`; rule `small` (`font-size: 7px`, `letter-spacing: .22em`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#080c15` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#eaf1ff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0d1320` | live computed `a` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#5fe0ff` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#7f90b4` | live computed `footer` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#232e45` | `var(--line)` in `:root` |
| **Variable Token (`--ink-000`)** | `#04060b` | `var(--ink-000)` in `:root` |
| **Variable Token (`--ink-300`)** | `#131b2b` | `var(--ink-300)` in `:root` |
| **Variable Token (`--line-hi`)** | `#33415f` | `var(--line-hi)` in `:root` |
| **Variable Token (`--mid`)** | `#a3b4d4` | `var(--mid)` in `:root` |
| **Variable Token (`--fg`)** | `#c3d0e8` | `var(--fg)` in `:root` |
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
   - Landmark `<header class="nav">` (`1440x56px`) hosting `Jeff Sibal — Visual & Digital Design` navigation (`PROFILE · PROJECTS · EXPERIENCE · PHOTOS · EQUIPMENT`), DOM attributes (`data-boot="splash"`, `data-line`, `data-nav`, `data-text="A VISUAL &"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.hero> — `A VISUAL & DIGITAL DESIGNER`)**:
   - Landmark `<section class="hero">` presenting display lead `A VISUAL & DIGITAL DESIGNER` and copy excerpt *"COPYRIGHT 2026 · CREATED BY JEFF SIBAL"* over `#080c15` canvas and `#eaf1ff` ink.
3. **Primary Showcase & Content Grid (<section.sec> — `Video Testimonial Service`)**:
   - Landmark `<section class="sec">` rendering section `Video Testimonial Service` with copy *"« JEFF.OF.ALL.TRADES"*, asset references (`favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`, `fonts.googleapis.com`), and grid rule `body { height:100% }`.
4. **Interactive Detail & Feature Matrix (<section.hz> — `Agency Project Board`)**:
   - Landmark `<section class="sec hz">` framing `Agency Project Board` and `Credit Union Campaigns` (*"Twenty-plus years across web, UI/UX, email marketing, video and p"*) with `#0d1320` surface cards, `#5fe0ff` accents, and `button { font:inherit;color:inherit;background:none;border:0;cursor:pointer }`.
5. **Colophon & Global Directory Footer (<footer.foot> — `https://sibaldesign.com/`)**:
   - Landmark `<footer class="foot">` anchoring `Jeff Sibal — Visual & Digital De` footer links (`PROFILE · PROJECTS · EXPERIENCE · PHOTOS · EQUIPMENT`), copy *"SOUTHERN CALIFORNIA"*, and `#232e45` structural dividers.
