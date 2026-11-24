---
title: "UI & UX Architecture: diversify-nz"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: diversify-nz

## Overview & Design Identity
- **Target**: `diversify-nz` (**diversify.nz**)
- **Production URL**: [https://diversify.nz](https://diversify.nz)
- **Final Redirected URL**: [https://www.diversify.nz/](https://www.diversify.nz/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×4140px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#ff8900` accent)
- **Summary**: Think differently. Act courageously. Create lasting change.
- **Total Clean CSS Variables Extracted**: `54` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Montserrat`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `.title` (`font-size: 18px`, `letter-spacing: 0`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 36px`, `line-height: 43.2px`, `font-weight: 400`); rule `h2` (`font-size: 26px`)
- **Body Copy**: live computed `body` (`font-size: 14px`, `line-height: 14px`, `font-weight: 400`); rule `p` (`font-size: 12px`, `line-height: 1.2`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`); rule `.label` (`font-size: 20px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#efefef` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ff8900` | `.edit-btn:hover { background-color: #ff8900 }` |
| **Secondary / Muted Copy** | `#3937b9` | `var(--textColor)` in `:root` |
| **Structural Hairline Border** | `#ebebeb` | `.popover-title { border-bottom: #ebebeb }` |
| **Variable Token (`--main-color`)** | `#21206c` | `var(--main-color)` in `:root` |
| **Variable Token (`--s-pre-color0`)** | `#09081b` | `var(--s-pre-color0)` in `:root` |
| **Variable Token (`--s-pre-color1`)** | `#21206a` | `var(--s-pre-color1)` in `:root` |
| **Variable Token (`--s-pre-color3`)** | `#7f7dd8` | `var(--s-pre-color3)` in `:root` |
| **Variable Token (`--s-pre-color4`)** | `#cdccf0` | `var(--s-pre-color4)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--carousel-button-width` | `48px` | Layout / Spatial Grid Token |
| `--carousel-button-height` | `48px` | Layout / Spatial Grid Token |
| `--carousel-button-svg-width` | `24px` | Layout / Spatial Grid Token |
| `--carousel-button-svg-height` | `24px` | Layout / Spatial Grid Token |
| `--carousel-button-svg-stroke-width` | `2.5` | Layout / Spatial Grid Token |
| `--carousel-button-svg-filter` | `drop-shadow(1px 1px 1px rgba(0,0,0,0.4))` | Color / Atmospheric Token |
| `--main-color` | `#21206c` | Brand / Palette Token |
| `--s-pre-color0` | `#09081b` | Brand / Palette Token |
| `--s-pre-color0-rgb` | `9,8,27` | Brand / Palette Token |
| `--s-pre-color1` | `#21206a` | Brand / Palette Token |
| `--s-pre-color1-rgb` | `33,32,106` | Brand / Palette Token |
| `--s-pre-color2` | `#3937b9` | Brand / Palette Token |
| `--s-pre-color2-rgb` | `57,55,185` | Brand / Palette Token |
| `--s-pre-color3` | `#7f7dd8` | Brand / Palette Token |
| `--s-pre-color3-rgb` | `127,125,216` | Brand / Palette Token |
| `--s-pre-color4` | `#cdccf0` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.show> — `diversify-nz`)**:
   - Landmark `<header class="show">` (`1440px`) hosting `diversify.nz` navigation (`Home · About · Services · Blog · Past work`), DOM attributes (`data-mobile-new-breakpoint-stage="1"`, `data-id="491220"`, `data-hypernova-key="SiteBootstrapper"`, `data-hypernova-id="0f36ac11-658b-43d6-88..."`), and stylesheet rule `.clearfix { position:relative }`.
2. **Hero Stage & Focal Lead (<div.locale-en> — `Think differently.`)**:
   - Landmark `<div class="locale-en">` presenting display lead `Think differently.` and copy excerpt *"CLICK THE PICS ABOVE TO JUMP TO OTHER SITE PAGES."* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<div.s-variation-default> — `Act courageously.`)**:
   - Landmark `<div class="s-variation-default">` rendering section `Act courageously.` with copy *"… Home About Services Blog Past work Testimonials Media Contact"*, asset references (`ga.js`, `static-fonts-css.strikinglycdn.com`, `main_v4.700681709f0b2a82b40c.bund...`, `650606_331305.png`), and grid rule `.clearfix:after { display:table;content:"";clear:both }`.
4. **Interactive Detail & Feature Matrix (<div.s-custom-colors> — `Create lasting change.`)**:
   - Landmark `<div class="s-custom-colors">` framing `Create lasting change.` and `WHAT DIVERSIFY NZ BRINGS` (*"CLICK THE PICS ABOVE TO JUMP TO OTHER SITE PAGES. Whakaanui kē. T"*) with `#efefef` surface cards, `#ff8900` accents, and `.ib { display:inline-block;zoom:1 }`.
5. **Colophon & Global Directory Footer (<footer.s-font-body-helvetica> — `https://diversify.nz`)**:
   - Landmark `<footer class="s-font-body-helvetica">` anchoring `diversify.nz` footer links (`Home · About · Services · Blog · Past work`), copy *"Think differently."*, and `#ebebeb` structural dividers.
