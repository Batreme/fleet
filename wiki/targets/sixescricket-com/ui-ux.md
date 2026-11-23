---
title: "UI & UX Architecture: sixescricket-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: sixescricket-com

## Overview & Design Identity
- **Target**: `sixescricket-com` (**Sixes Party Cricket · Let's Play · Nets & Simulator · Sixes Social Cricket**)
- **Production URL**: [https://sixescricket.com/](https://sixescricket.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff5e0` / `#185abc`)
- **Summary**: Cricket, but not as you know it. We've re-imagined the age old game of cricket for the modern socialite.
- **Total Clean CSS Variables Extracted**: `240` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `fontSoehneMono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-6xl: 3.75rem`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 164px`, `line-height: 131.2px`, `font-weight: 400`, `letter-spacing: 3.28px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 1.75rem`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-soehne-mono: "fontSoehneMono", "fontSoehneMono Fallback"`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fff5e0` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#590707` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `html { background-color: white }` (`#ffffff`) |
| **Interactive Accent / Highlight** | `#185abc` | `.rc-2fa-submit-button-holder bu... { background-color: #185abc }` |
| **Secondary / Muted Copy** | `#02b875` | `:hover { color: #02b875 }` |
| **Structural Hairline Border** | `#6a7282` | `select { border-color: #6a7282 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--fa-font-solid` | `normal 900 1em/1 'Font Awesome 7 Free'` | Typography / Scale Token |
| `--fa-font-regular` | `normal 400 1em/1 'Font Awesome 7 Free'` | Typography / Scale Token |
| `--fa-font-light` | `normal 300 1em/1 'Font Awesome 7 Pro'` | Canvas / Surface Token |
| `--fa-font-thin` | `normal 100 1em/1 'Font Awesome 7 Pro'` | Typography / Scale Token |
| `--fa-font-duotone` | `normal 900 1em/1 'Font Awesome 7 Duotone'` | Typography / Scale Token |
| `--fa-font-duotone-regular` | `normal 400 1em/1 'Font Awesome 7 Duotone'` | Typography / Scale Token |
| `--fa-font-duotone-light` | `normal 300 1em/1 'Font Awesome 7 Duotone'` | Canvas / Surface Token |
| `--fa-font-duotone-thin` | `normal 100 1em/1 'Font Awesome 7 Duotone'` | Typography / Scale Token |
| `--fa-font-brands` | `normal 400 1em/1 'Font Awesome 7 Brands'` | Brand / Palette Token |
| `--fa-font-sharp-solid` | `normal 900 1em/1 'Font Awesome 7 Sharp'` | Typography / Scale Token |
| `--fa-font-sharp-regular` | `normal 400 1em/1 'Font Awesome 7 Sharp'` | Typography / Scale Token |
| `--fa-font-sharp-light` | `normal 300 1em/1 'Font Awesome 7 Sharp'` | Canvas / Surface Token |
| `--fa-font-sharp-thin` | `normal 100 1em/1 'Font Awesome 7 Sharp'` | Typography / Scale Token |
| `--fa-font-sharp-duotone-solid` | `normal 900 1em/1 'Font Awesome 7 Sharp Duotone'` | Typography / Scale Token |
| `--fa-font-sharp-duotone-regular` | `normal 400 1em/1 'Font Awesome 7 Sharp Duotone'` | Typography / Scale Token |
| `--fa-font-sharp-duotone-light` | `normal 300 1em/1 'Font Awesome 7 Sharp Duotone'` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.top-0> — `sixescricket-com`)**:
   - Landmark `<header class="top-0 h-nav">` (`1440x116px`) hosting `Sixes Party Cricket · Let's Play · N` navigation (`Venues · Cricket · Food & Drink · Events · Live Sport`), DOM attributes (`data-scroll-behavior="smooth"`, `data-sentry-component="RootLayout"`, `data-sentry-source-file="layout.tsx"`, `data-precedence="next"`), and stylesheet rule `.elmvdc0 { white-space:nowrap;text-overflow:ellipsis;display:block;overflow:clip }`.
2. **Hero Stage & Focal Lead (<section.stack> — `Sixes Social Cricket`)**:
   - Landmark `<section class="stack overflow-clip">` presenting display lead `Sixes Social Cricket` and copy excerpt *"Take a swing at Party Cricket. A carnival of fast bowls, flowing "* over `#fff5e0` canvas and `#590707` ink.
3. **Primary Showcase & Content Grid (<article.overlay> — `Nothing Beats Hitting Sixes`)**:
   - Landmark `<article class="overlay overlay-b">` rendering section `Nothing Beats Hitting Sixes` with copy *"Nothing Beats Hitting Sixes"*, asset references (`6gknobew.api.sanity.io`, `83afe278b6a6bb3c-s.p.45535valc9rz...`, `soehne_mono-s.p.1h8tgkdilcgxe.woff2`, `0dvybyowk9yut.css`), and grid rule `._1b6o2se1 { animation:.5s linear infinite _1b6o2se0 }`.
4. **Interactive Detail & Feature Matrix (<article.overlay-b> — `Book Party Cricket`)**:
   - Landmark `<article class="overlay overlay-b">` framing `Book Party Cricket` and `Swing your heart out` (*"Inspired by the Age old game"*) with `#ffffff` surface cards, `#185abc` accents, and `._1lyk8y0 { align-items:center }`.
5. **Colophon & Global Directory Footer (<footer.bg-mahogany-500> — `https://sixescricket.com/`)**:
   - Landmark `<footer class="bg-mahogany-500 px-buffer">` anchoring `Sixes Party Cricket · Let's Play` footer links (`Venues · Cricket · Food & Drink · Events · Live Sport`), copy *"Take a swing at Party Cricket"*, and `#6a7282` structural dividers.
