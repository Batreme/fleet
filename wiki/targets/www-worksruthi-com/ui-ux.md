---
title: "UI & UX Architecture: www-worksruthi-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-worksruthi-com

## Overview & Design Identity
- **Target**: `www-worksruthi-com` (**meet Sruthi. a copywriter, marketer and artist with chutzpah.**)
- **Production URL**: [https://www.worksruthi.com/](https://www.worksruthi.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f3f3e9` / `#e33529`)
- **Summary**: you've built something good and nobody's talking about it yet? i write and design the art that helps capitalists sell their stuff. loudly.
- **Total Clean CSS Variables Extracted**: `205` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Impact`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 161.973px`, `line-height: 126.339px`, `font-weight: 400`); CSS variables `--font-display: "Impact", "Arial Narrow", sans-serif`, `--h1: calc(clamp(72px, calc(28.17px + 11.24vw), 190px) * var(--vp-scale))`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 46px`, `line-height: 46px`, `font-weight: 400`); CSS variables `--h2: calc(clamp(62px, calc(28.57px + 8.57vw), 152px) * var(--vp-scale))`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 22.4px`, `font-weight: 400`); rule `p` (`font-size: calc(var(--h9) * .7)`, `line-height: 1.3`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 22.4px`, `font-weight: 400`); CSS variables `--font-mono: "Geist Mono", "SF Mono", Menlo, monospace`, `--lh-small: 1.14`, `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f3f3e9` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1c1b1a` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f4f0e5` | `.cork-paper { background: #f4f0e5 }` |
| **Interactive Accent / Highlight** | `#e33529` | live computed `button` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#e33529` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#808080` | `.f-col .lead { border-bottom: #808080 }` |
| **Variable Token (`--cherub`)** | `#f4ced3` | `var(--cherub)` in `:root` |
| **Variable Token (`--sail`)** | `#afd8fb` | `var(--sail)` in `:root` |
| **Variable Token (`--cobalt`)** | `#2b52d9` | `var(--cobalt)` in `:root` |
| **Variable Token (`--marigold`)** | `#f2a900` | `var(--marigold)` in `:root` |
| **Variable Token (`--grey`)** | `#6b6862` | `var(--grey)` in `:root` |
| **Variable Token (`--grey-soft`)** | `#a09c92` | `var(--grey-soft)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-display` | `"Impact", "Arial Narrow", sans-serif` | Typography / Scale Token |
| `--font-bayon` | `"Bayon", "Arial Narrow", sans-serif` | Typography / Scale Token |
| `--font-sans` | `"Geist", "Helvetica Neue", Helvetica, Arial, sans-serif` | Typography / Scale Token |
| `--font-mono` | `"Geist Mono", "SF Mono", Menlo, monospace` | Typography / Scale Token |
| `--font-helvetica` | `"Helvetica Neue", Helvetica, Arial, sans-serif` | Typography / Scale Token |
| `--spring` | `#f3f3e9` | Elevation / Border Token |
| `--ink` | `#1c1b1a` | Typography Ink Token |
| `--cinnabar` | `#e33529` | Color / Atmospheric Token |
| `--cherub` | `#f4ced3` | Color / Atmospheric Token |
| `--sail` | `#afd8fb` | Color / Atmospheric Token |
| `--cobalt` | `#2b52d9` | Color / Atmospheric Token |
| `--marigold` | `#f2a900` | Color / Atmospheric Token |
| `--grey` | `#6b6862` | Color / Atmospheric Token |
| `--grey-soft` | `#a09c92` | Color / Atmospheric Token |
| `--cream` | `var(--spring)` | Design System Custom Token |
| `--red` | `var(--cinnabar)` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.has-tc> — `www-worksruthi-com`)**:
   - Landmark `<header class="has-tc">` (`1440x64px`) hosting `meet Sruthi. a copywriter, marketer ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`, `data-sdkv="2.0.1"`), and stylesheet rule `.pf canvas { width:100%;height:100%;display:block }`.
2. **Hero Stage & Focal Lead (<section.hero> — `SRUTHI`)**:
   - Landmark `<section class="hero in">` presenting display lead `SRUTHI` and copy excerpt *"handmade with 🫀 and 🧠 and"* over `#f3f3e9` canvas and `#1c1b1a` ink.
3. **Primary Showcase & Content Grid (<section.bq> — `sruthi`)**:
   - Landmark `<section class="bq">` rendering section `sruthi` with copy *"MY WEBSITE IS NOW ON AWWWARDS??!! VOTE FOR MEEE <3<3<3 MY WEBSITE"*, asset references (`Impact.woff2`, `0_vr5kr4-0c-u.css`, `3y62y2uuds32t.css`, `1mlftcslf095m.js`), and grid rule `.pf:focus-visible { outline:2px solid var(--cobalt);outline-offset:-8px;border-radius:16px }`.
4. **Interactive Detail & Feature Matrix (<section.sfold> — `MY WEBSITE IS NOW ON AWWWARDS??!! `)**:
   - Landmark `<section class="sfold">` framing `MY WEBSITE IS NOW ON AWWWARDS??!! VOTE FOR MEEE ` and `MY WEBSITE IS NOW ON AWWWARDS??!! VOTE FOR MEEE ` (*"MY WEBSITE IS NOW ON AWWWARDS??!! VOTE FOR MEEE <3<3<3"*) with `#f4f0e5` surface cards, `#e33529` accents, and `.pl-frame { justify-content:center;align-items:center;display:flex;position:absolute... }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://www.worksruthi.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `meet Sruthi. a copywriter, marke` footer links (`Overview · Index · Archive · About · Contact`), copy *"a copywriter/marketer/artist with chutzpah. a c o p y w r i "*, and `#808080` structural dividers.
