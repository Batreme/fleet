---
title: "UI & UX Architecture: sinedogma-com-tr"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: sinedogma-com-tr

## Overview & Design Identity
- **Target**: `sinedogma-com-tr` (**sinedogma**)
- **Production URL**: [https://sinedogma.com.tr/](https://sinedogma.com.tr/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#111111` ink, `#ffcc00` accent)
- **Summary**: sinedogma ve dogma yayın: dijital arşiv, dergiler, kitaplar, haberler ve satış noktaları.
- **Total Clean CSS Variables Extracted**: `203` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `EB Garamond Local`
- **Body Font Stack**: `EB Garamond Local`
- **Monospace / Technical Font Stack**: `Consolas`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 78px`, `line-height: 73.32px`, `font-weight: 400`, `letter-spacing: -3.12px`); rule `h1` (`font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 54px`, `line-height: 54px`, `font-weight: 400`, `letter-spacing: -1.62px`); rule `h2` (`font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 17px`, `line-height: 24.65px`, `font-weight: 400`); rule `p` (`font-size: 15px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 20.3px`, `font-weight: 400`); rule `small` (`font-size: .72rem`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#111111` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#dddddd` | `.community-card { background: #dddddd }` |
| **Interactive Accent / Highlight** | `#ffcc00` | `crubber-button.ytp-swatch-backg... { background-color: #ffcc00 }` |
| **Secondary / Muted Copy** | `#6f6f6f` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#d9d9d9` | `var(--line)` in `:root` |
| **Variable Token (`--soft`)** | `#f5f5f3` | `var(--soft)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--paper` | `#fff` | Canvas / Surface Token |
| `--ink` | `#111` | Typography Ink Token |
| `--muted` | `#6f6f6f` | Color / Atmospheric Token |
| `--line` | `#d9d9d9` | Color / Atmospheric Token |
| `--soft` | `#f5f5f3` | Color / Atmospheric Token |
| `--max` | `1080px` | Dimension / Scale Token |
| `--reading` | `680px` | Dimension / Scale Token |
| `--motion-fast` | `160ms` | Motion / Easing Token |
| `--motion-base` | `220ms` | Motion / Easing Token |
| `--motion-slow` | `300ms` | Motion / Easing Token |
| `--motion-ease` | `cubic-bezier(.22,.61,.36,1)` | Motion / Easing Token |
| `--garamond-tracking` | `0em` | Typography / Scale Token |
| `--garamond-heading-tracking` | `-0.025em` | Typography Ink Token |
| `--link-underline-offset` | `.16em` | Typography Ink Token |
| `--link-underline-thickness` | `1px` | Typography Ink Token |
| `--link-underline-color` | `rgba(17,17,17,.48)` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `sinedogma-com-tr`)**:
   - Landmark `<header class="site-header">` (`1440x57px`) hosting `sinedogma` navigation (`haberler · satış noktaları · hakkımızda`), DOM attributes (`data-path="/"`, `data-path="/haberler"`, `data-path="/satis-noktalari"`, `data-path="/hakkimizda"`), and stylesheet rule `root { --paper: fff; --ink: 111; --muted: 6f6f6f; --line: d9d9d9; --soft: f5f5f3; }`.
2. **Hero Stage & Focal Lead (<section.hero> — `iki yayın tek dolaşım`)**:
   - Landmark `<section class="hero shell">` presenting display lead `iki yayın tek dolaşım` and copy excerpt *"sinedogma / dogma yayın"* over `#ffffff` canvas and `#111111` ink.
3. **Primary Showcase & Content Grid (<section.section> — `sinedogma dijital arşiv`)**:
   - Landmark `<section class="section shell">` rendering section `sinedogma dijital arşiv` with copy *"sinedogma · güz 2026 güz 2026 beş sayı antoloji koleksiyonu özel "*, asset references (`EBGaramond-VariableFont_wght.woff2`, `favicon-32x32.png`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `html { scroll-behavior: smooth; }`.
4. **Interactive Detail & Feature Matrix (<article.article-card> — `“bu ben değilim” yönetmenleri ile `)**:
   - Landmark `<article class="article-card">` framing `“bu ben değilim” yönetmenleri ile bir söyleşi` and `+1 belgesel: jim’le tanışmak "kısa incelemesi"` (*"sinedogma · güz 2026"*) with `#dddddd` surface cards, `#ffcc00` accents, and `input { font: inherit; text-transform: lowercase; }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://sinedogma.com.tr/`)**:
   - Landmark `<footer class="site-footer">` anchoring `sinedogma` footer links (`haberler · satış noktaları · hakkımızda`), copy *"dogma yayın · atakan akar max stirner'in biricik felsefesi i"*, and `#d9d9d9` structural dividers.
