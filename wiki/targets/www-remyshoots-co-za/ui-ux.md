---
title: "UI & UX Architecture: www-remyshoots-co-za"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-remyshoots-co-za

## Overview & Design Identity
- **Target**: `www-remyshoots-co-za` (**Remy Shoots**)
- **Production URL**: [https://www.remyshoots.co.za/](https://www.remyshoots.co.za/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#111111` canvas, `#ffffff` ink, `#808080` accent)
- **Summary**: Documenting emotion, movement and meaning. Since ©2016 — the photography portfolio of Remy.
- **Total Clean CSS Variables Extracted**: `45` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Helvetica Neue`
- **Body Font Stack**: `Roboto Mono`
- **Monospace / Technical Font Stack**: `Roboto Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 93.6px`, `line-height: 93.6px`, `font-weight: 800`, `letter-spacing: -2.808px`)
- **Section Heading (`H2`)**: observed font-size ladder: `93.6px`, `16px`, `24.336px`, `15.12px`, `clamp(13px,1.05vw,18px)`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 600`); rule `p` (`font-size: clamp(13px,1.05vw,18px)`, `line-height: 1.2`, `letter-spacing: -.04em`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 15.12px`, `line-height: 18.144px`, `font-weight: 600`, `letter-spacing: -0.3024px`); CSS variables `--vt-meta-dur: .45s`, `--vt-meta-out-delay: 0s`, `--vt-meta-in-delay: .45s`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#111111` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `a` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#2e2e2e` | `var(--panel)` in `:root` |
| **Interactive Accent / Highlight** | `#808080` | `.studio-chrome .nav-works-link { color: gray }` (`#808080`) |
| **Secondary / Muted Copy** | `#ff3131` | live computed `h1` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#2e2e2e` | `.gesture-tutorial { border: #2e2e2e }` |
| **Variable Token (`--cream`)** | `#fcf8ef` | `var(--cream)` in `:root` |
| **Variable Token (`--gray-150`)** | `#cbc7c2` | `var(--gray-150)` in `:root` |
| **Variable Token (`--gray-200`)** | `#b2aeab` | `var(--gray-200)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cream` | `#fcf8ef` | Color / Atmospheric Token |
| `--gray-150` | `#cbc7c2` | Color / Atmospheric Token |
| `--gray-200` | `#b2aeab` | Color / Atmospheric Token |
| `--red` | `#ff3131` | Color / Atmospheric Token |
| `--panel` | `#2e2e2e` | Color / Atmospheric Token |
| `--bg` | `#111` | Canvas / Surface Token |
| `--stage-lift` | `24px` | Dimension / Scale Token |
| `--vcaret-x` | `calc(8.33vw + 219px)` | Dimension / Scale Token |
| `--vig-size` | `45%` | Layout / Spatial Grid Token |
| `--vig-radius` | `min(114vh, 114vw)` | Elevation / Border Token |
| `--vig-open` | `1.2` | Design System Custom Token |
| `--nav-caret-lane` | `28px` | Layout / Spatial Grid Token |
| `--nav-caret-gap` | `8px` | Layout / Spatial Grid Token |
| `--nav-caret-size` | `.9em` | Layout / Spatial Grid Token |
| `--vt-stage-dur` | `1.6s` | Motion / Timing Token |
| `--vt-stage-ease` | `cubic-bezier(.887, 0, .113, 1)` | Motion / Easing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.chrome> — `www-remyshoots-co-za`)**:
   - Landmark `<header class="chrome">` (`1360x0px`) hosting `Remy Shoots` navigation (`works(21) works(21) · motion(8) motion(8) · About About · contact contact`), DOM attributes (`data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`, `data-sdkv="2.0.1"`, `data-disable-auto-track="1"`), and stylesheet rule `nter_d7e32889-module__94mdca__cla... { font-family:Inter,Inter Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<div.view-slider> — `REMYSHOOTS®`)**:
   - Landmark `<div class="view-slider">` presenting display lead `REMYSHOOTS®` and copy excerpt *"documenting emotion, documenting emotion, movement and meaning. m"* over `#111111` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<div.chrome-slider> — `documenting emotion, documenting e`)**:
   - Landmark `<div class="chrome-slider">` rendering section `documenting emotion, documenting emotion, moveme` with copy *"documenting emotion, documenting emotion,"*, asset references (`2f13ad8e538108e0-s.p.22iyan98j1_2...`, `83afe278b6a6bb3c-s.p.2bn3s6zvc0dy...`, `under-armour.svg`, `playhead.svg`), and grid rule `inter_d7e32889-module__94mdca__va... { --font-sans:"Inter", "Inter Fallback" }`.
4. **Interactive Detail & Feature Matrix (<div.chrome> — `documenting emotion, documenting e`)**:
   - Landmark `<div class="chrome">` framing `documenting emotion, documenting emotion,` and `documenting emotion,` (*"documenting emotion,"*) with `#2e2e2e` surface cards, `#808080` accents, and `mono_955658b9-module__SfQagW__cla... { font-family:Roboto Mono,Roboto Mono Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.logo> — `https://www.remyshoots.co.za/`)**:
   - Landmark `<footer class="logo">` anchoring `Remy Shoots` footer links (`works(21) works(21) · motion(8) motion(8) · About About · contact contact`), copy *"movement and meaning. movement and meaning."*, and `#2e2e2e` structural dividers.
