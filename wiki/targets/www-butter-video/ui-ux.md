---
title: "UI & UX Architecture: www-butter-video"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-butter-video

## Overview & Design Identity
- **Target**: `www-butter-video` (**Butter Video · Online Video Editor Engineered for Creativity**)
- **Production URL**: [https://www.butter.video/](https://www.butter.video/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×1656px`, Mobile `390×1744px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#00ffd0`)
- **Summary**: The first video editor and design platform built with creative code for creative teams. It's a whole new timeline.
- **Total Clean CSS Variables Extracted**: `40` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `DieGrotesk`
- **Body Font Stack**: `DieGrotesk`
- **Monospace / Technical Font Stack**: `monospace)`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 107.568px`, `line-height: 106.708px`, `font-weight: 400`, `letter-spacing: 0.344219px`); rule `h1` (`font-size: clamp(5.6rem,6.6vw,12.5rem)`, `line-height: .92`, `letter-spacing: -1px`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 60.4px`, `line-height: 58.588px`, `font-weight: 400`, `letter-spacing: 0.3624px`); rule `h2` (`font-size: clamp(3.2rem,6vw,7rem)`, `line-height: .94`, `letter-spacing: -.5px`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 18px`, `line-height: 27px`, `font-weight: 400`); rule `p` (`font-size: clamp(1.05rem,1.5vw,1.25rem)`, `line-height: 1.45`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 18px`, `line-height: 27px`, `font-weight: 400`); rule `small` (`font-size: inherit`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0f0f0f` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ededed` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#00ffd0` | `var(--perf-gradient-primary)` in `:root` |
| **Secondary / Muted Copy** | `#808080` | live computed `hr` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#fdfdfd` | `.CreatorSlice_secondaryButton__... { border-color: #fdfdfd }` |
| **Variable Token (`--butter-white`)** | `#fafafa` | `var(--butter-white)` in `:root` |
| **Variable Token (`--butter-off-white`)** | `#f7f7f7` | `var(--butter-off-white)` in `:root` |
| **Variable Token (`--butter-black`)** | `#1e1e1e` | `var(--butter-black)` in `:root` |
| **Variable Token (`--butter-charcoal`)** | `#3c3c3c` | `var(--butter-charcoal)` in `:root` |
| **Variable Token (`--butter-dark-grey`)** | `#e2e2e2` | `var(--butter-dark-grey)` in `:root` |
| **Variable Token (`--butter-light`)** | `#ebebeb` | `var(--butter-light)` in `:root` |
| **Variable Token (`--butter-red`)** | `#ff3333` | `var(--butter-red)` in `:root` |
| **Variable Token (`--butter-blue`)** | `#4dc5e5` | `var(--butter-blue)` in `:root` |
| **Variable Token (`--butter-green`)** | `#63ad45` | `var(--butter-green)` in `:root` |
| **Variable Token (`--butter-yellow`)** | `#e9d352` | `var(--butter-yellow)` in `:root` |
| **Variable Token (`--butter-pink`)** | `#f9abff` | `var(--butter-pink)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--butter-white` | `#FAFAFA` | Canvas / Surface Token |
| `--butter-off-white` | `#F7F7F7` | Canvas / Surface Token |
| `--butter-black` | `#1E1E1E` | Canvas / Surface Token |
| `--butter-true-black` | `#0F0F0F` | Canvas / Surface Token |
| `--butter-charcoal` | `#3C3C3C` | Color / Atmospheric Token |
| `--butter-light-grey` | `#EDEDED` | Canvas / Surface Token |
| `--butter-dark-grey` | `#E2E2E2` | Canvas / Surface Token |
| `--butter-light` | `#EBEBEB` | Canvas / Surface Token |
| `--butter-red` | `#FF3333` | Color / Atmospheric Token |
| `--butter-blue` | `#4DC5E5` | Color / Atmospheric Token |
| `--butter-green` | `#63AD45` | Color / Atmospheric Token |
| `--butter-yellow` | `#E9D352` | Color / Atmospheric Token |
| `--butter-pink` | `#F9ABFF` | Typography Ink Token |
| `--butter-font-primary` | `'DieGrotesk','DieGrotesk Fallback'` | Brand / Palette Token |
| `--butter-font-secondary` | `'ABCDiatype','ABCDiatype Fallback'` | Brand / Palette Token |
| `--butter-ease-out` | `cubic-bezier(0.200, 0.715, 0.205, 0.990)` | Motion / Easing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.kbhUnc> — `www-butter-video`)**:
   - Landmark `<header class="kbhUnc">` (`1440x88px`) hosting `Butter Video · Online Video Editor E` navigation (`Product Product · Blocks Blocks · Templates Templates · Pricing Pricing · Blog Blog`), DOM attributes (`data-auth="out"`, `data-precedence="next"`, `data-precedence="next"`, `data-styled="active"`), and stylesheet rule `.__className_8d5843 { font-family:DieGrotesk,DieGrotesk Fallback;font-weight:400;font-style:no... }`.
2. **Hero Stage & Focal Lead (<section.hsoZjO> — `Engineered for Creativity Engineer`)**:
   - Landmark `<section class="hsoZjO">` presenting display lead `Engineered for Creativity Engineered for Creativity` and copy excerpt *"It's a whole new timeline."* over `#ffffff` canvas and `#0f0f0f` ink.
3. **Primary Showcase & Content Grid (<section.glnUmG> — `Butter is the first video editor w`)**:
   - Landmark `<section class="glnUmG">` rendering section `Butter is the first video editor where creatives...` with copy *"Co-Create Co-Create"*, asset references (`5fb8d156cdd6d753-s.p.woff2`, `da60608f2183158e-s.p.woff2`, `2836d44e2fdcb041.css`, `6294d87c4b6dbd81.css`), and grid rule `.__className_210739 { font-family:ABCDiatype,ABCDiatype Fallback;font-weight:400;font-style:no... }`.
4. **Interactive Detail & Feature Matrix (<section.lhNRew> — `Browse curated blocks for motion g`)**:
   - Landmark `<section class="lhNRew">` framing `Browse curated blocks for motion graphics, kineti...` and `Make blocks your own with intuitive dials, slider...` (*"Templates Templates"*) with `#ededed` surface cards, `#00ffd0` accents, and `.CreatorSlice_inner__5XvuM { width:100%;max-width:1920px;margin-inline:auto }`.
5. **Colophon & Global Directory Footer (<footer.bdNowa> — `https://www.butter.video/`)**:
   - Landmark `<footer class="bdNowa">` anchoring `Butter Video · Online Video Edit` footer links (`Product Product · Blocks Blocks · Templates Templates · Pricing Pricing · Blog Blog`), copy *"Product Product Explore features Explore features"*, and `#fdfdfd` structural dividers.
