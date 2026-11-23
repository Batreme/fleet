---
title: "UI & UX Architecture: diversify-nz"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: diversify-nz

## Overview & Design Identity
- **Target**: `diversify-nz` (**diversify.nz**)
- **Production URL**: [https://diversify.nz](https://diversify.nz)
- **Final Redirected URL**: [https://www.diversify.nz/](https://www.diversify.nz/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#00c1ff` accent)
- **Summary**: Think differently. Act courageously. Create lasting change.
- **Total Clean CSS Variables Extracted**: `48` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Montserrat`
- **Body Font Stack**: `brandon-grotesque`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `.title` (`font-weight: 700`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 28px`, `line-height: 42px`, `font-weight: 400`); rule `h2` (`font-size: 26px`)
- **Body Copy**: live computed `body` (`font-size: 14px`, `line-height: 14px`, `font-weight: 400`); rule `p` (`line-height: 1.5`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`); rule `.label` (`font-size: 16px`, `font-weight: normal`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#efefef` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#00c1ff` | `.s-kit-btn.twitter-blue:hover { background: #00c1ff }` |
| **Secondary / Muted Copy** | `#3937b9` | `var(--textColor)` in `:root` |
| **Structural Hairline Border** | `#1bb0e6` | `t-select-tags .s-kit-select-sel... { border-color: #1bb0e6 }` |
| **Variable Token (`--s-pre-color0`)** | `#09081b` | `var(--s-pre-color0)` in `:root` |
| **Variable Token (`--s-pre-color1`)** | `#21206a` | `var(--s-pre-color1)` in `:root` |
| **Variable Token (`--s-pre-color3`)** | `#7f7dd8` | `var(--s-pre-color3)` in `:root` |
| **Variable Token (`--s-pre-color4`)** | `#cdccf0` | `var(--s-pre-color4)` in `:root` |
| **Variable Token (`--s-pre-color5`)** | `#1a232d` | `var(--s-pre-color5)` in `:root` |
| **Variable Token (`--s-pre-color6`)** | `#3f546e` | `var(--s-pre-color6)` in `:root` |
| **Variable Token (`--s-pre-color7`)** | `#6a87a9` | `var(--s-pre-color7)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--s-pre-color0` | `#09081b` | Brand / Palette Token |
| `--s-pre-color0-rgb` | `9,8,27` | Brand / Palette Token |
| `--s-pre-color1` | `#21206a` | Brand / Palette Token |
| `--s-pre-color1-rgb` | `33,32,106` | Brand / Palette Token |
| `--s-pre-color2` | `#3937b9` | Brand / Palette Token |
| `--s-pre-color2-rgb` | `57,55,185` | Brand / Palette Token |
| `--s-pre-color3` | `#7f7dd8` | Brand / Palette Token |
| `--s-pre-color3-rgb` | `127,125,216` | Brand / Palette Token |
| `--s-pre-color4` | `#cdccf0` | Brand / Palette Token |
| `--s-pre-color4-rgb` | `205,204,240` | Brand / Palette Token |
| `--s-pre-color5` | `#1a232d` | Brand / Palette Token |
| `--s-pre-color5-rgb` | `26,35,45` | Brand / Palette Token |
| `--s-pre-color6` | `#3f546e` | Brand / Palette Token |
| `--s-pre-color6-rgb` | `63,84,110` | Brand / Palette Token |
| `--s-pre-color7` | `#6a87a9` | Brand / Palette Token |
| `--s-pre-color7-rgb` | `106,135,169` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.show> — `diversify-nz`)**:
   - Landmark `<header class="show">` (`1440px`) hosting `diversify.nz` navigation (`Home · About · Services · Blog · Past work`), DOM attributes (`data-emotion`, `data-s`, `data-webpack="bobcat-monorepo:chunk..."`, `data-mobile-new-breakpoint-stage="1"`), and stylesheet rule `tent.s-font-body-helvetica .s-fon... { font-family:helvetica,arial,sans-serif }`.
2. **Hero Stage & Focal Lead (<div.locale-en> — `Think differently.`)**:
   - Landmark `<div class="locale-en">` presenting display lead `Think differently.` and copy excerpt *"CLICK THE PICS ABOVE TO JUMP TO OTHER SITE PAGES."* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<div.s-variation-default> — `Act courageously.`)**:
   - Landmark `<div class="s-variation-default">` rendering section `Act courageously.` with copy *"… Home About Services Blog Past work Testimonials Media Contact"*, asset references (`bugsnag-3.min.js`, `keen.min.js`, `ga.js`, `static-fonts-css.strikinglycdn.com`), and grid rule `font-heading-helvetica .s-font-he... { font-family:helvetica,arial,sans-serif }`.
4. **Interactive Detail & Feature Matrix (<div.s-custom-colors> — `Create lasting change.`)**:
   - Landmark `<div class="s-custom-colors">` framing `Create lasting change.` and `WHAT DIVERSIFY NZ BRINGS` (*"CLICK THE PICS ABOVE TO JUMP TO OTHER SITE PAGES. Whakaanui kē. T"*) with `#efefef` surface cards, `#00c1ff` accents, and `ont-nav_item-helvetica .s-font-na... { font-family:helvetica,arial,sans-serif }`.
5. **Colophon & Global Directory Footer (<footer.s-font-body-helvetica> — `https://diversify.nz`)**:
   - Landmark `<footer class="s-font-body-helvetica">` anchoring `diversify.nz` footer links (`Home · About · Services · Blog · Past work`), copy *"Think differently."*, and `#1bb0e6` structural dividers.
