---
title: "UI & UX Architecture: wndws-space"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: wndws-space

## Overview & Design Identity
- **Target**: `wndws-space` (**windows · place is temporary. you are not.**)
- **Production URL**: [https://wndws.space/](https://wndws.space/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#cacaca` / `#efefef`)
- **Summary**: Upload your window — tell what chapter of life you're living through.
- **Total Clean CSS Variables Extracted**: `13` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: observed font-size ladder: `24px`, `16px`, `13px`, `13.3333px`, `64px`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 24px`, `line-height: normal`, `font-weight: 700`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#cacaca` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#efefef` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#efefef` | live computed `button` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#ffffff` | `.prelude-route ::-moz-selection { color: #ffffff }` |
| **Structural Hairline Border** | `#ffffff` | `tml.prelude-route::-webkit-scro... { border-color: #ffffff }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--text-reveal-duration` | `.92s` | Typography Ink Token |
| `--text-reveal-ease` | `cubic-bezier(.22,1,.36,1)` | Typography Ink Token |
| `--frame` | `10px` | Dimension / Scale Token |
| `--frame-radius` | `6px` | Elevation / Border Token |
| `--nav-drop` | `8px` | Layout / Spatial Grid Token |
| `--fr` | `var(--frame-radius)` | Dimension / Scale Token |
| `--edge` | `linear-gradient(#000,#000)` | Color / Atmospheric Token |
| `--band` | `10px` | Dimension / Scale Token |
| `--logo-h` | `25px` | Dimension / Scale Token |
| `--lift` | `0px` | Dimension / Scale Token |
| `--slide` | `-7px` | Dimension / Scale Token |
| `--tilt` | `-2.5deg` | Design System Custom Token |
| `--teaser-i` | `0` | Motion / Easing Token |
| `--wndws-space-bg` | `#cacaca` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--wndws-space-ink` | `#000000` | Primary Typography Ink (computed-derived) |
| `--wndws-space-surface` | `#efefef` | Surface Substrate (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.nav> — `wndws-space`)**:
   - Landmark `<nav class="nav">` (`1x1px`) hosting `windows · place is temporary. you ar` navigation (`prelude prelude`), DOM attributes (`data-v-20a15833`, `data-v-045ed839`, `data-v-feaf1087`, `data-v-d791c00f`), and stylesheet rule `before { box-sizing:border-box;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<div.custom-cursor-enabled> — `105 windows`)**:
   - Landmark `<div class="custom-cursor-enabled">` presenting display lead `105 windows` and copy excerpt *"windows · place is temporary. you are not."* over `#cacaca` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<div.nuxt-route-announcer> — `windows · place is temporary. you `)**:
   - Landmark `<div class="nuxt-route-announcer">` rendering section `windows · place is temporary. you are not.` with copy *"Vsevolod — Moscow, Russia"*, asset references (`fonts.googleapis.com`, `fonts.gstatic.com`, `css2`, `entry.DtyUHzly.css`), and grid rule `html::-webkit-scrollbar { width:10px }`.
4. **Interactive Detail & Feature Matrix (<div.route-stage> — `Vsevolod — Moscow, Russia`)**:
   - Landmark `<div class="route-stage">` framing `Vsevolod — Moscow, Russia` and `Sergey Savinykh — Moscow, Russia` (*"Sergey Savinykh — Moscow, Russia"*) with `#efefef` surface cards, `#efefef` accents, and `html::-webkit-scrollbar-track { background:transparent }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://wndws.space/`)**:
   - Landmark `<footer class="site-footer">` anchoring `windows · place is temporary. yo` footer links (`prelude prelude`), copy *"Polina — Chelyabinsk, Russia"*, and `#ffffff` structural dividers.
