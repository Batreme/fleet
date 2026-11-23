---
title: "UI & UX Architecture: flycrooked-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: flycrooked-com

## Overview & Design Identity
- **Target**: `flycrooked-com` (**Crow · Trip planner and flight finder for iPhone**)
- **Production URL**: [https://flycrooked.com/](https://flycrooked.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#ad2450` / `#ff3d81`)
- **Summary**: Your iPhone travel companion. Plan a trip, compare flight routes, track delays and gate changes, and carry a blunt local guide when you l...
- **Total Clean CSS Variables Extracted**: `61` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Barlow Condensed`
- **Body Font Stack**: `Barlow`
- **Monospace / Technical Font Stack**: `mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 262.74px`, `line-height: 215.447px`, `font-weight: 900`, `letter-spacing: -1.3137px`); CSS variables `--display: var(--font-display),"Arial Narrow",Arial,sans-serif`, `--font-display: "display","display Fallback"`; rule `h1` (`letter-spacing: -.005em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 18px`, `line-height: 27px`, `font-weight: 400`); rule `h2` (`letter-spacing: -.005em`)
- **Body Copy**: live computed `body` (`font-size: 18px`, `line-height: 27px`, `font-weight: 400`); CSS variables `--body: var(--font-body),-apple-system,"Segoe UI",sans-serif`, `--font-body: "body","body Fallback"`; rule `p` (`font-size: 16px`, `line-height: 1.75`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 15px`, `line-height: 22.5px`, `font-weight: 500`); CSS variables `--mono: var(--font-mono),ui-monospace,"SF Mono",Menlo,monospace`, `--font-mono: "mono"`, `--default-mono-font-family: var(--font-mono)`; rule `nav` (`font-size: 15px`, `font-weight: 500`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ad2450` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#fff5f8` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#1c1e24` | `var(--panel-black)` in `:root` |
| **Interactive Accent / Highlight** | `#ff3d81` | `var(--accent)` in `:root` |
| **Secondary / Muted Copy** | `#bec2ca` | `var(--cp-muted)` in `:root` |
| **Structural Hairline Border** | `#33373f` | `var(--surface-line)` in `:root` |
| **Variable Token (`--concourse`)** | `#eceff3` | `var(--concourse)` in `:root` |
| **Variable Token (`--sign-black`)** | `#17181c` | `var(--sign-black)` in `:root` |
| **Variable Token (`--night`)** | `#0e0f13` | `var(--night)` in `:root` |
| **Variable Token (`--surface`)** | `#1e2128` | `var(--surface)` in `:root` |
| **Variable Token (`--ink`)** | `#1b1c21` | `var(--ink)` in `:root` |
| **Variable Token (`--ink-2`)** | `#5b616b` | `var(--ink-2)` in `:root` |
| **Variable Token (`--card`)** | `#ffffff` | `var(--card)` in `:root` |
| **Variable Token (`--rule`)** | `#d7dce3` | `var(--rule)` in `:root` |
| **Variable Token (`--green`)** | `#1e7b4d` | `var(--green)` in `:root` |
| **Variable Token (`--dgreen`)** | `#00c16a` | `var(--dgreen)` in `:root` |
| **Variable Token (`--dorange`)** | `#ff7a1a` | `var(--dorange)` in `:root` |
| **Variable Token (`--dorange-deep`)** | `#c2510a` | `var(--dorange-deep)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--concourse` | `#eceff3` | Color / Atmospheric Token |
| `--sign-black` | `#17181c` | Canvas / Surface Token |
| `--panel-black` | `#1c1e24` | Canvas / Surface Token |
| `--accent` | `#ff3d81` | Brand / Palette Token |
| `--accent-rgb` | `255,61,129` | Brand / Palette Token |
| `--night` | `#0e0f13` | Color / Atmospheric Token |
| `--surface` | `#1e2128` | Canvas / Surface Token |
| `--surface-line` | `#33373f` | Canvas / Surface Token |
| `--ink` | `#1b1c21` | Typography Ink Token |
| `--ink-2` | `#5b616b` | Typography Ink Token |
| `--card` | `#fff` | Color / Atmospheric Token |
| `--rule` | `#d7dce3` | Color / Atmospheric Token |
| `--green` | `#1e7b4d` | Color / Atmospheric Token |
| `--dgreen` | `#00c16a` | Color / Atmospheric Token |
| `--dorange` | `#ff7a1a` | Color / Atmospheric Token |
| `--dorange-deep` | `#c2510a` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.js> — `flycrooked-com`)**:
   - Landmark `<nav class="js">` (`1461x106px`) hosting `Crow · Trip planner and flight finde` navigation (`Crow · Guides · Get Crow`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="story"`, `data-booted="1"`), and stylesheet rule `.__className_2063d3 { font-family:display,display Fallback }`.
2. **Hero Stage & Focal Lead (<section.hero> — `FLY CROOKED.`)**:
   - Landmark `<section class="hero one">` presenting display lead `FLY CROOKED.` and copy excerpt *"F l y c r o o k e d ."* over `#ad2450` canvas and `#fff5f8` ink.
3. **Primary Showcase & Content Grid (<section.one> — `F l y c r o o k e d .`)**:
   - Landmark `<section class="hero one">` rendering section `F l y c r o o k e d .` with copy *"I’m the travel AI with opinions. I plan your trip, come along for"*, asset references (`06ac09dcb8ec7d56.p.woff2`, `4224042929936d69-s.p.woff2`, `422bb7078d9b61dc.p.woff2`, `532b6dda9c49d302-s.p.woff2`), and grid rule `.__variable_2063d3 { --font-display:"display","display Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.side> — `I’m the travel AI with opinions. I`)**:
   - Landmark `<section class="hero one">` framing `I’m the travel AI with opinions. I plan your tri` and `Most apps leave when you land.` (*"Most apps leave when you land."*) with `#1c1e24` surface cards, `#ff3d81` accents, and `.__className_c3828f { font-family:mono }`.
5. **Colophon & Global Directory Footer (<footer.foot> — `https://flycrooked.com/`)**:
   - Landmark `<footer class="foot">` anchoring `Crow · Trip planner and flight f` footer links (`Crow · Guides · Get Crow`), copy *"Day three. The temple, early."*, and `#33373f` structural dividers.
