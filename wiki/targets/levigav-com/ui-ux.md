---
title: "UI & UX Architecture: levigav-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: levigav-com

## Overview & Design Identity
- **Target**: `levigav-com` (**Levi Gavrilut · I build what I want to exist**)
- **Production URL**: [https://levigav.com](https://levigav.com)
- **Final Redirected URL**: [https://www.levigav.com/](https://www.levigav.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×872px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#ffff00`)
- **Summary**: Levi Gavrilut, 16. Designer and developer from Switzerland. Websites, web apps and small tools built with care. I ♥ Jesus.
- **Total Clean CSS Variables Extracted**: `153` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Instrument Serif`
- **Body Font Stack**: `Inter Variable`
- **Monospace / Technical Font Stack**: `JetBrains Mono Variable`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 216px`, `line-height: 172.8px`, `font-weight: 400`, `letter-spacing: -5.4px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 244.8px`, `line-height: 190.944px`, `font-weight: 400`, `letter-spacing: -9.792px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: clamp(16px,1.25vw,21px)`, `line-height: 1.2`, `letter-spacing: -.03em`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `small` (`font-size: 9px`, `letter-spacing: .1em`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#121110` | `var(--panel)` in `:root` |
| **Interactive Accent / Highlight** | `#ffff00` | `.btn--give:hover { background: yellow }` (`#ffff00`) |
| **Secondary / Muted Copy** | `#8f8a82` | `var(--fg-3)` in `:root` |
| **Structural Hairline Border** | `#141414` | `var(--line)` in `:root` (`ffffff14`) |
| **Variable Token (`--panel-2`)** | `#191816` | `var(--panel-2)` in `:root` |
| **Variable Token (`--panel-3`)** | `#22201e` | `var(--panel-3)` in `:root` |
| **Variable Token (`--glass`)** | `#1e1c1a` | `var(--glass)` in `:root` |
| **Variable Token (`--fg`)** | `#f4f2ec` | `var(--fg)` in `:root` |
| **Variable Token (`--fg-2`)** | `#b6b2aa` | `var(--fg-2)` in `:root` |
| **Variable Token (`--fg-4`)** | `#403e3a` | `var(--fg-4)` in `:root` |
| **Variable Token (`--yellow`)** | `#f6cd1b` | `var(--yellow)` in `:root` |
| **Variable Token (`--give`)** | `#e6b814` | `var(--give)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#000` | Canvas / Surface Token |
| `--panel` | `#121110` | Color / Atmospheric Token |
| `--panel-2` | `#191816` | Color / Atmospheric Token |
| `--panel-3` | `#22201e` | Color / Atmospheric Token |
| `--glass` | `#1e1c1ab8` | Color / Atmospheric Token |
| `--fg` | `#f4f2ec` | Typography Ink Token |
| `--fg-2` | `#b6b2aa` | Typography Ink Token |
| `--fg-3` | `#8f8a82` | Typography Ink Token |
| `--fg-4` | `#403e3a` | Typography Ink Token |
| `--line` | `#ffffff14` | Color / Atmospheric Token |
| `--line-2` | `#ffffff26` | Color / Atmospheric Token |
| `--line-3` | `#ffffff47` | Color / Atmospheric Token |
| `--yellow` | `#f6cd1b` | Color / Atmospheric Token |
| `--give` | `#e6b814` | Color / Atmospheric Token |
| `--yellow-ink` | `#000` | Typography Ink Token |
| `--yellow-glow` | `#f6cd1b66` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav> — `levigav-com`)**:
   - Landmark `<header class="nav">` (`1440x346px`) hosting `Levi Gavrilut · I build what I want ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-edition="gold"`, `data-welcome="out"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.prologue> — `Levi Gavrilut`)**:
   - Landmark `<section class="prologue is-quiet">` presenting display lead `Levi Gavrilut` and copy excerpt *"G picks Gold, S picks Street. You can switch any time. · G alege "* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<article.pro-verse> — `07 Gethsemane`)**:
   - Landmark `<article class="pro-verse">` rendering section `07 Gethsemane` with copy *"Prologue · best with sound"*, asset references (`1sm_p255ynpf-.css`, `2fu8m418vo0kb.css`, `2fo6lh-lqntob.css`, `2w31v64880cal.css`), and grid rule `html { overflow-x:hidden }`.
4. **Interactive Detail & Feature Matrix (<section.hero> — `08 The Cross`)**:
   - Landmark `<section class="hero shell">` framing `08 The Cross` and `10 The Burial` (*"Faith. Code. A story."*) with `#121110` surface cards, `#ffff00` accents, and `html.lenis body { height:auto }`.
5. **Colophon & Global Directory Footer (<footer.in-prologue> — `https://levigav.com`)**:
   - Landmark `<footer class="in-prologue">` anchoring `Levi Gavrilut · I build what I w` footer links (`Overview · Index · Archive · About · Contact`), copy *"or scroll at your own pace"*, and `#141414` structural dividers.
