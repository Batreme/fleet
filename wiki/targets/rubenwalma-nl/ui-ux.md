---
title: "UI & UX Architecture: rubenwalma-nl"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: rubenwalma-nl

## Overview & Design Identity
- **Target**: `rubenwalma-nl` (**Ruben Walma – Filmmaker & videoproductie Groningen**)
- **Production URL**: [https://rubenwalma.nl/](https://rubenwalma.nl/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×4968px`, Mobile `390×2616px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#121212` / `#0000ee`)
- **Summary**: Filmmaker uit Groningen voor aftermovies, campagnes en creatieve videoproducties. Dynamische video’s met tempo, sfeer en een eigen stijl.
- **Total Clean CSS Variables Extracted**: `58` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Pacaembu`
- **Body Font Stack**: `Pacaembu`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 19.0476px`, `line-height: 20.9524px`, `font-weight: 600`, `letter-spacing: -2%`); rule `h1` (`font-size: 2.66em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 65.2952px`, `line-height: 81.619px`, `font-weight: 600`, `letter-spacing: -2%`); rule `h2` (`font-size: 2.35em`, `line-height: 1.3`)
- **Body Copy**: live computed `body` (`font-size: 9.52381px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: calc(var(--size-font)*2)`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 9.52381px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#121212` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#202623` | `var(--button-040-color-arrow-background)` in `:root` |
| **Interactive Accent / Highlight** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#ffffff` | `media-play-button path { stroke: #ffffff }` |
| **Variable Token (`--primary`)** | `#5766ab` | `var(--primary)` in `:root` |
| **Variable Token (`--grey`)** | `#1d1d1d` | `var(--grey)` in `:root` |
| **Variable Token (`--button-040-color`)** | `#131313` | `var(--button-040-color)` in `:root` |
| **Variable Token (`--button-040-color-arrow`)** | `#efeeec` | `var(--button-040-color-arrow)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--primary` | `#5766ab` | Brand / Palette Token |
| `--black` | `#121212` | Canvas / Surface Token |
| `--white` | `#fff` | Canvas / Surface Token |
| `--grey` | `#1D1D1D` | Color / Atmospheric Token |
| `--size-container-ideal` | `390` | Layout / Spatial Grid Token |
| `--size-container-min` | `320px` | Layout / Spatial Grid Token |
| `--size-container-max` | `479px` | Layout / Spatial Grid Token |
| `--size-container` | `clamp(var(--size-container-min), 100vw, var(--size-container-max))` | Layout / Spatial Grid Token |
| `--size-unit` | `10` | Layout / Spatial Grid Token |
| `--grid-columns` | `4` | Layout / Spatial Grid Token |
| `--grid-gap` | `1em` | Layout / Spatial Grid Token |
| `--container-padding` | `2em` | Layout / Spatial Grid Token |
| `--button-040-color` | `#131313` | Brand / Palette Token |
| `--button-040-color-background` | `#fff` | Canvas / Surface Token |
| `--button-040-color-arrow` | `#efeeec` | Brand / Palette Token |
| `--button-040-color-arrow-background` | `#202623` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `rubenwalma-nl`)**:
   - Landmark `<header class="lenis">` (`1425x121px`) hosting `Ruben Walma – Filmmaker & videoprodu` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-barba="wrapper"`, `data-scrolling-started="false"`, `data-scrolling-direction="up"`, `data-page-theme="light"`), and stylesheet rule `root { --size-container-ideal:550;--size-container-min:480px;--size-container-m... }`.
2. **Hero Stage & Focal Lead (<main.logo> — `Videoproductie Groningen`)**:
   - Landmark `<main class="logo">` presenting display lead `Videoproductie Groningen` and copy excerpt *"Ik ben Ruben. Filmmaker uit Groningen en al veel te lang bezig me"* over `#121212` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<main.menu-toggle> — `F i l m m a k e r u i t G r o n i `)**:
   - Landmark `<main class="menu-toggle">` rendering section `F i l m m a k e r u i t G r o n i n g e n u u t G...` with copy *"u i t G r o n i n g e n u u t G r u n n V e r h a l e n d i e b l"*, asset references (`favicon-dark2.png`, `favicon-white.png`, `sitemap.xml`, `stream.mux.com`), and grid rule `selection { background-color:var(--primary);color:fff }`.
4. **Interactive Detail & Feature Matrix (<main.menu-toggle__label> — `Over Ruben`)**:
   - Landmark `<main class="menu-toggle__label">` framing `Over Ruben` and `u i t G r o n i n g e n` (*"u i t G r o n i n g e n"*) with `#202623` surface cards, `#0000ee` accents, and `html { background-color:var(--black);color:var(--white);scrollbar-gutter:stable... }`.
5. **Colophon & Global Directory Footer (<footer.hamburger> — `https://rubenwalma.nl/`)**:
   - Landmark `<footer class="hamburger">` anchoring `Ruben Walma – Filmmaker & videop` footer links (`Overview · Index · Archive · About · Contact`), copy *"Groningen stad Regiofilm"*, and `#ffffff` structural dividers.
