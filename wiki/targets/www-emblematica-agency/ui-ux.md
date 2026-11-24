---
title: "UI & UX Architecture: www-emblematica-agency"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-emblematica-agency

## Overview & Design Identity
- **Target**: `www-emblematica-agency` (**emblematica — concept-led brand & web design agency in barcelona**)
- **Production URL**: [https://www.emblematica.agency](https://www.emblematica.agency)
- **Final Redirected URL**: [https://emblematica.agency/](https://emblematica.agency/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#dadada` canvas, `#0e0c0d` ink, `#ff5490` accent)
- **Summary**: emblematica is a concept-led design agency in Barcelona creating brand identities and websites that help businesses stand out in competit...
- **Total Clean CSS Variables Extracted**: `60` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter Tight`
- **Body Font Stack**: `Inter Tight`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 14px`, `line-height: 16.38px`, `font-weight: 800`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 70px`, `line-height: 71.4px`, `font-weight: 500`, `letter-spacing: -2.1px`); rule `h2` (`font-size: calc(58 * var(--u))`, `line-height: 0.92`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 800`); rule `body` (`font-weight: 800`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 800`); CSS variables `--loop-caption-alpha: 0.000`; rule `.caption` (`font-size: calc(14 * var(--u))`, `line-height: 1.17`, `letter-spacing: 0`, `font-weight: inherit`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#dadada` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0e0c0d` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `.t-mbfix { background-color: white }` (`#ffffff`) |
| **Interactive Accent / Highlight** | `#ff5490` | `.about-link:focus-visible { color: #ff5490 }` |
| **Secondary / Muted Copy** | `#323232` | live computed `button` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#323232` | hairline divider derived from live computed `button` `color` (`computed_styles.json`) |
| **Variable Token (`--white`)** | `#fbfbfb` | `var(--white)` in `:root` |
| **Variable Token (`--acid`)** | `#d5ff69` | `var(--acid)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#0e0c0d` | Typography Ink Token |
| `--paper` | `#dadada` | Canvas / Surface Token |
| `--white` | `#fbfbfb` | Canvas / Surface Token |
| `--acid` | `#d5ff69` | Color / Atmospheric Token |
| `--t-headline-font` | `'InterTight',Arial,sans-serif` | Typography / Scale Token |
| `--t-text-font` | `'InterTight',Arial,sans-serif` | Typography Ink Token |
| `--menu-edge-gap` | `calc(12 * var(--u))` | Layout / Spatial Grid Token |
| `--menu-anchor-left` | `calc(50vw - (45 * var(--u)))` | Dimension / Scale Token |
| `--menu-anchor-top` | `var(--menu-edge-gap)` | Design System Custom Token |
| `--menu-drawer-padding-left` | `calc(28 * var(--u))` | Layout / Spatial Grid Token |
| `--menu-origin-x` | `0px` | Dimension / Scale Token |
| `--menu-origin-y` | `0px` | Dimension / Scale Token |
| `--menu-origin-scale-x` | `0.12` | Design System Custom Token |
| `--menu-origin-scale-y` | `0.05` | Design System Custom Token |
| `--preloader-size` | `220` | Layout / Spatial Grid Token |
| `--preloader-delay` | `70ms` | Motion / Easing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.t-records> — `www-emblematica-agency`)**:
   - Landmark `<header class="t-records t-records_animated">` (`1389x38px`) hosting `emblematica — concept-led brand & we` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-hook="blocks-collection-con..."`, `data-tilda-project-id="13693937"`, `data-tilda-page-id="189979109"`, `data-tilda-formskey="f0b53f0bdbcb91ba7a098..."`), and stylesheet rule `.csssize { height:3344px }`.
2. **Hero Stage & Focal Lead (<section.manifesto> — `WE CREATE DESIGN, IDENTITIES AND W`)**:
   - Landmark `<section class="manifesto">` presenting display lead `WE CREATE DESIGN, IDENTITIES AND WEBSITES THAT HE...` and copy excerpt *"CONCEPT-LED DESIGN AGENCY"* over `#dadada` canvas and `#0e0c0d` ink.
3. **Primary Showcase & Content Grid (<section.manifesto-runout> — `We create design, identities and w`)**:
   - Landmark `<section class="manifesto-runout">` rendering section `We create design, identities and websites that he...` with copy *"concept-led design agency"*, asset references (`emblematica.agency`, `ws.tildacdn.com`, `static.tildacdn.com`, `Frame_2087327053.png`), and grid rule `body { --t-headline-font:'InterTight',Arial,sans-serif;--t-text-font:'InterTigh... }`.
4. **Interactive Detail & Feature Matrix (<section.services> — `concept-led design agency`)**:
   - Landmark `<section class="services">` framing `concept-led design agency` and `let's meet in barcelona` (*"let's meet in barcelona"*) with `#ffffff` surface cards, `#ff5490` accents, and `.t-body { margin:0px }`.
5. **Colophon & Global Directory Footer (<footer.t-records> — `https://www.emblematica.agency`)**:
   - Landmark `<footer class="t-records">` anchoring `emblematica — concept-led brand ` footer links (`Overview · Index · Archive · About · Contact`), copy *"At Emblematica, we believe"*, and `#323232` structural dividers.
