---
title: "UI & UX Architecture: premotio-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: premotio-com

## Overview & Design Identity
- **Target**: `premotio-com` (**premotio — finished design into polished motion**)
- **Production URL**: [https://premotio.com/](https://premotio.com/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f5f5f7` / `#f59e0b`)
- **Summary**: premotio turns finished design into polished motion without sending you into a video editor. Pick a preset, drop in your work and export...
- **Total Clean CSS Variables Extracted**: `445` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter Tight`
- **Body Font Stack**: `Inter Tight`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 99.9999px`, `line-height: 89.9999px`, `font-weight: 500`); CSS variables `--font-size-h1: 6.25rem`, `--font-size-tablet-h1: 5rem`, `--font-size-mobile-h1: 3.5rem`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 24px`, `line-height: 26.4px`, `font-weight: 700`); CSS variables `--font-size-h2: 3.25rem`, `--font-size-tablet-h2: 2.75rem`, `--font-size-mobile-h2: 2rem`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 17.6px`, `font-weight: 600`); CSS variables `--font-size-paragraph: 1rem`, `--font-size-body: 1.0625rem`, `--font-size-mobile-body: 1rem`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 17.6px`, `font-weight: 600`); CSS variables `--font-size-label: .9375rem`, `--font-size-meta: .75rem`, `--leading-label: 1`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f5f5f7` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1d1d1f` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#f59e0b` | `var(--color-amber-500)` in `:root` |
| **Secondary / Muted Copy** | `#98989d` | `var(--inverse-muted)` in `:root` |
| **Structural Hairline Border** | `#e5e5ea` | `var(--border)` in `:root` |
| **Variable Token (`--on-fg`)** | `#ffffff` | `var(--on-fg)` in `:root` |
| **Variable Token (`--fg-muted`)** | `#6e6e73` | `var(--fg-muted)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#f5f5f7` | Canvas / Surface Token |
| `--bg-rgb` | `245,245,247` | Canvas / Surface Token |
| `--fg` | `#1d1d1f` | Typography Ink Token |
| `--fg-rgb` | `29,29,31` | Typography Ink Token |
| `--on-fg` | `#ffffff` | Typography Ink Token |
| `--on-fg-rgb` | `255,255,255` | Typography Ink Token |
| `--on-media` | `var(--bg)` | Design System Custom Token |
| `--glass` | `rgba(255, 255, 255, 0.5)` | Color / Atmospheric Token |
| `--glass-rgb` | `255,255,255` | Design System Custom Token |
| `--hairline` | `rgba(29, 29, 31, 0.1)` | Color / Atmospheric Token |
| `--hairline-rgb` | `29,29,31` | Design System Custom Token |
| `--logo` | `#000000` | Color / Atmospheric Token |
| `--logo-rgb` | `0,0,0` | Design System Custom Token |
| `--fg-muted` | `#6e6e73` | Typography Ink Token |
| `--fg-muted-rgb` | `110,110,115` | Typography Ink Token |
| `--fg-secondary` | `rgba(29, 29, 31, 0.8)` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.app-nav> — `premotio-com`)**:
   - Landmark `<header class="app-nav app-nav--active">` (`1312x56px`) hosting `premotio — finished design into poli` navigation (`Library · How it works · MCP · Pricing · Contact`), DOM attributes (`data-v-a799f99b`, `data-v-a3457c20`, `data-v-39640a56`, `data-v-f9a31650`), and stylesheet rule `before { content:attr(data-word) }`.
2. **Hero Stage & Focal Lead (<section.hero> — `D e s i g n e d a l r e a d y N o `)**:
   - Landmark `<section class="hero is-on">` presenting display lead `D e s i g n e d a l r e a d y N o w m a k e i t (...` and copy excerpt *"D e s i g n e d a l r e a d y"* over `#f5f5f7` canvas and `#1d1d1f` ink.
3. **Primary Showcase & Content Grid (<section.library> — `S t a r t w i t h t h e g o o d p `)**:
   - Landmark `<section class="library">` rendering section `S t a r t w i t h t h e g o o d p a r t` with copy *"N o w m a k e i t ( move )"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `_payload.json`), and grid rule `.reveal-line-mask { clip-path:inset(0 -100vw -.2em -.15em) }`.
4. **Interactive Detail & Feature Matrix (<section.categories> — `Preset categories`)**:
   - Landmark `<section class="categories">` framing `Preset categories` and `T a k e t h e s h o r t c u t . K i l l t h e ( t...` (*"Designed already Now make it move"*) with `#000000` surface cards, `#f59e0b` accents, and `focus-visible { outline:2px solid var(--fg);outline-offset:.125rem }`.
5. **Colophon & Global Directory Footer (<footer.app-footer> — `https://premotio.com/`)**:
   - Landmark `<footer class="app-footer">` anchoring `premotio — finished design into ` footer links (`Library · How it works · MCP · Pricing · Contact`), copy *"Drop in your work. Pick a starting point. Take it as far as "*, and `#e5e5ea` structural dividers.
