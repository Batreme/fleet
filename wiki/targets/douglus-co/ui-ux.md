---
title: "UI & UX Architecture: douglus-co"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: douglus-co

## Overview & Design Identity
- **Target**: `douglus-co` (**Douglus Nguyen — Web Designer from Vietnam**)
- **Production URL**: [https://douglus.co](https://douglus.co)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×846px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#1e1e1e` / `#fefff8`)
- **Summary**: Independent web designer based in Vietnam, focused on website design, interaction design, and front-end development.
- **Total Clean CSS Variables Extracted**: `94` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Neue Montreal`
- **Body Font Stack**: `Neue Montreal`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 78.88px`, `line-height: 70.992px`, `font-weight: 400`, `letter-spacing: -5.5216px`)
- **Section Heading (`H2`)**: observed font-size ladder: `78.88px`, `16px`, `13px`, `100%`, `clamp(.75rem,.81vw,.875rem)`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`); rule `p` (`font-size: clamp(.875rem, var(--gw) * .2...`, `line-height: 1.2`, `letter-spacing: -.045em`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#1e1e1e` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#fefff8` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | `.c-scrollbar_thumb { background-color: #000000 }` |
| **Interactive Accent / Highlight** | `#fefff8` | live computed `button` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#ebebeb` | `var(--muted-color)` in `:root` |
| **Structural Hairline Border** | `#ebebeb` | hairline divider derived from `var(--muted-color)` in `:root` |
| **Variable Token (`--neutral-color`)** | `#292724` | `var(--neutral-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--page-padding` | `clamp(20px, 2.3vw, 40px)` | Layout / Spatial Grid Token |
| `--header-height` | `112px` | Layout / Spatial Grid Token |
| `--footer-right-width` | `clamp(38.75rem, 45.14vw, 48.75rem)` | Layout / Spatial Grid Token |
| `--white-color` | `#fefff8` | Canvas / Surface Token |
| `--black-color` | `#1e1e1e` | Canvas / Surface Token |
| `--neutral-color` | `#292724` | Brand / Palette Token |
| `--muted-color` | `#ebebeb` | Brand / Palette Token |
| `--default-easing` | `cubic-bezier(.25, 1, .5, 1)` | Motion / Easing Token |
| `--gw` | `4.16667vw` | Dimension / Scale Token |
| `--rv-ease` | `var(--default-easing)` | Motion / Easing Token |
| `--rv-ease-img` | `cubic-bezier(.76, 0, .24, 1)` | Motion / Easing Token |
| `--rv-d-s` | `.5s` | Motion / Timing Token |
| `--rv-d-m` | `.7s` | Motion / Timing Token |
| `--rv-d-l` | `.9s` | Motion / Timing Token |
| `--rv-step-t` | `40ms` | Motion / Timing Token |
| `--rv-step-l` | `80ms` | Motion / Timing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `douglus-co`)**:
   - Landmark `<header class="site-header">` (`1440x112px`) hosting `Douglus Nguyen — Web Designer from V` navigation (`H ome · W orks · P layground · A bout · C ontact`), DOM attributes (`data-scroll-direction="vertical"`, `data-barba="wrapper"`, `data-preloader`, `data-fragment="1"`), and stylesheet rule `video { font-size:100%;font:inherit;vertical-align:baseline;border:0;margin:0;pa... }`.
2. **Hero Stage & Focal Lead (<section.home-hero> — `D ouglus N guyen`)**:
   - Landmark `<section class="home-hero">` presenting display lead `D ouglus N guyen` and copy excerpt *"Just a designer & developer trying to make good things for the we"* over `#1e1e1e` canvas and `#fefff8` ink.
3. **Primary Showcase & Content Grid (<section.home-hero:nth(2)> — `Just a designer & developer trying`)**:
   - Landmark `<section class="home-hero">` rendering section `Just a designer & developer trying to make good ` with copy *"Based in Ho Chi Minh City, Vietnam, working with clients worldwid"*, asset references (`favicon.ico`, `favicon-32x32.png`, `favicon-16x16.png`, `apple-touch-icon.png`), and grid rule `section { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.home-hero:nth(3)> — `Based in Ho Chi Minh City, Vietnam`)**:
   - Landmark `<section class="home-hero">` framing `Based in Ho Chi Minh City, Vietnam, working with` and `From Vietnam with Love.` (*"From Vietnam with Love."*) with `#000000` surface cards, `#fefff8` accents, and `body { line-height:1 }`.
5. **Colophon & Global Directory Footer (<footer.preloader__subject> — `https://douglus.co`)**:
   - Landmark `<footer class="preloader__subject">` anchoring `Douglus Nguyen — Web Designer fr` footer links (`H ome · W orks · P layground · A bout · C ontact`), copy *"+84 39 327 7584 +84 39 327 7584"*, and `#ebebeb` structural dividers.
