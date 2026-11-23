---
title: "UI & UX Architecture: white-desert-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: white-desert-com

## Overview & Design Identity
- **Target**: `white-desert-com` (**Luxury Adventures in Antarctica · White Desert**)
- **Production URL**: [https://white-desert.com/](https://white-desert.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#1f2a44` ink, `#0000ff` accent)
- **Summary**: White Desert is the world’s leading luxury Antarctic expedition company, offering once-in-a-lifetime journeys to the South Pole and Emper...
- **Total Clean CSS Variables Extracted**: `117` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Oswald`
- **Body Font Stack**: `Inter Tight`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 256px`, `line-height: 256px`, `font-weight: 400`); rule `h1` (`font-size: var(--size-375)`, `line-height: 100%`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 90px`, `line-height: normal`, `font-weight: 500`); rule `h2` (`font-size: var(--size-2)`, `line-height: var(--lh-120)`, `font-weight: 500`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 14px`, `line-height: 1.4`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1f2a44` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f5f5f5` | `.global-flyout_content-item { background-color: #f5f5f5 }` |
| **Interactive Accent / Highlight** | `#0000ff` | `.nav-link { color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#a8acb3` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#1f2330` | `var(--border)` in `:root` |
| **Variable Token (`--surface`)** | `#12141a` | `var(--surface)` in `:root` |
| **Variable Token (`--primary`)** | `#6aa5ff` | `var(--primary)` in `:root` |
| **Variable Token (`--primary-contrast`)** | `#0b0c0f` | `var(--primary-contrast)` in `:root` |
| **Variable Token (`--black`)** | `#000000` | `var(--black)` in `:root` |
| **Variable Token (`--dark-bg`)** | `#090b10` | `var(--dark-bg)` in `:root` |
| **Variable Token (`--wd_deep-blue`)** | `#0e1118` | `var(--wd_deep-blue)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#fff` | Canvas / Surface Token |
| `--surface` | `#12141a` | Canvas / Surface Token |
| `--text` | `var(--wd_dark-blue)` | Typography Ink Token |
| `--quote-accent` | `var(--WD_Dark-Blue,#1f2a44)` | Brand / Palette Token |
| `--muted` | `#a8acb3` | Color / Atmospheric Token |
| `--primary` | `#6aa5ff` | Brand / Palette Token |
| `--primary-contrast` | `#0b0c0f` | Brand / Palette Token |
| `--border` | `#1f2330` | Elevation / Border Token |
| `--white` | `#fff` | Canvas / Surface Token |
| `--black` | `#000` | Canvas / Surface Token |
| `--black-faded` | `rgba(0,0,0,.5)` | Canvas / Surface Token |
| `--dark-bg` | `#090b10` | Canvas / Surface Token |
| `--background` | `var(--bg)` | Canvas / Surface Token |
| `--foreground` | `var(--text)` | Typography Ink Token |
| `--wd_dark-blue` | `#1f2a44` | Canvas / Surface Token |
| `--wd_deep-blue` | `#0e1118` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.lenis> — `white-desert-com`)**:
   - Landmark `<nav class="lenis">` (`1440x80px`) hosting `Luxury Adventures in Antarctica · Wh` navigation (`Rates · Enquire · Home · Enquire now · Dates & Prices`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.basic-banner_bg { z-index:0;position:absolute;top:0;bottom:0;left:0;right:0 }`.
2. **Hero Stage & Focal Lead (<section.padding-top-large-bottom-medium> — `ANTARCTICA`)**:
   - Landmark `<section class="padding-top-large-bottom-medium m-pb-625">` presenting display lead `ANTARCTICA` and copy excerpt *"Luxury and adventure in the most remote place on Earth"* over `#ffffff` canvas and `#1f2a44` ink.
3. **Primary Showcase & Content Grid (<section.tall-parallax-banner> — `Antarctica`)**:
   - Landmark `<section class="tall-parallax-banner">` rendering section `Antarctica` with copy *"The Last Continent"*, asset references (`cabcbbbe485680be.css`, `7e7f4251c3582625.css`, `5dd7b716df5564d7.css`, `112bdbe21ebfd0e0.css`), and grid rule `.basic-banner_overlay { z-index:1;background-color:rgba(0,0,0,.2);position:absolute;top:0;bottom... }`.
4. **Interactive Detail & Feature Matrix (<section.bg-white> — `Vast, majestic and unimaginably be`)**:
   - Landmark `<section class="padding-top-large-bottom-medium bg-white">` framing `Vast, majestic and unimaginably beautiful — setti...` and `Baby Penguins & Blue Tunnels` (*"Between November and February, during the short polar summer, we "*) with `#f5f5f5` surface cards, `#0000ff` accents, and `.basic-banner_content { z-index:2;width:100%;color:var(--white);text-align:center;position:relative }`.
5. **Colophon & Global Directory Footer (<footer.custom-cursor_dot> — `https://white-desert.com/`)**:
   - Landmark `<footer class="custom-cursor_dot">` anchoring `Luxury Adventures in Antarctica ` footer links (`Rates · Enquire · Home · Enquire now · Dates & Prices`), copy *"Witness the Emperor chicks as they take their first steps an"*, and `#1f2330` structural dividers.
