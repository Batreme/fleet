---
title: "UI & UX Architecture: awards-racing"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: awards-racing

## Overview & Design Identity
- **Target**: `awards-racing` (**Awards Racing**)
- **Production URL**: [https://awards.racing](https://awards.racing)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#2c2c2c` ink, `#ffc500` accent)
- **Summary**: Customize your car and race through parody award shows and galleries in Awards Racing (also known as Versus Racing and Versus: Design Gra...
- **Total Clean CSS Variables Extracted**: `57` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Druk Wide Cy TT`
- **Body Font Stack**: `Druk Wide Cy TT`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 138px`, `line-height: 126.96px`, `font-weight: 900`)
- **Section Heading (`H2`)**: observed font-size ladder: `138px`, `16px`, `24px`, `var(--base-font-size)`, `9px`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 500`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 24px`, `line-height: normal`, `font-weight: 500`, `letter-spacing: 0.72px`); CSS variables `--small-size: 50px`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#2c2c2c` | live computed `button` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e9e9e9` | `var(--color-bg-gray-default)` in `:root` |
| **Interactive Accent / Highlight** | `#ffc500` | `var(--color-accent)` in `:root` |
| **Secondary / Muted Copy** | `#d9d9d9` | `var(--color-text-disabled)` in `:root` |
| **Structural Hairline Border** | `#ff6464` | `var(--color-line-4)` in `:root` |
| **Variable Token (`--color-theme`)** | `#f00000` | `var(--color-theme)` in `:root` |
| **Variable Token (`--color-theme-dark`)** | `#c00000` | `var(--color-theme-dark)` in `:root` |
| **Variable Token (`--color-line-3`)** | `#c60000` | `var(--color-line-3)` in `:root` |
| **Variable Token (`--color-text-black`)** | `#000000` | `var(--color-text-black)` in `:root` |
| **Variable Token (`--color-text-gray-dark`)** | `#505050` | `var(--color-text-gray-dark)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-primary` | `"Druk Wide Cy TT",sans-serif` | Brand / Palette Token |
| `--base-font-size` | `16px` | Typography / Scale Token |
| `--color-theme` | `#f00000` | Brand / Palette Token |
| `--color-theme-dark` | `#c00000` | Canvas / Surface Token |
| `--color-theme-overlay` | `rgba(166,33,55,.44)` | Brand / Palette Token |
| `--color-theme-selection` | `rgba(255,6,6,.6)` | Brand / Palette Token |
| `--color-line-1` | `#fff` | Brand / Palette Token |
| `--color-line-2` | `#f00000` | Brand / Palette Token |
| `--color-line-3` | `#c60000` | Brand / Palette Token |
| `--color-line-4` | `#ff6464` | Brand / Palette Token |
| `--color-accent` | `#ffc500` | Brand / Palette Token |
| `--color-text-white` | `#fff` | Canvas / Surface Token |
| `--color-text-black` | `#000` | Canvas / Surface Token |
| `--color-text-gray-light` | `silver` | Canvas / Surface Token |
| `--color-text-gray-dark` | `#505050` | Canvas / Surface Token |
| `--color-text-disabled` | `#d9d9d9` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.macos> — `awards-racing`)**:
   - Landmark `<header class="macos">` (`1440px`) hosting `Awards Racing` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-theme="green"`, `data-onloadfired="true"`, `data-nuxt-data="nuxt-app"`, `data-ssr="true"`), and stylesheet rule `root { --header-offset-top:14px;--header-offset-inline:24px }`.
2. **Hero Stage & Focal Lead (<div.desktop> — `AWARDS RACING`)**:
   - Landmark `<div class="desktop">` presenting display lead `AWARDS RACING` and copy excerpt *"Customize your car and race through parody award shows and galler"* over `#ffffff` canvas and `#2c2c2c` ink.
3. **Primary Showcase & Content Grid (<div.landscape> — `awards racing`)**:
   - Landmark `<div class="landscape">` rendering section `awards racing` with copy *"AWARDS RACING"*, asset references (`entry.BqrIyN9y.css`, `index.B6ocAFgr.css`, `shareState.CxNBlIw1.css`, `useWaitlistAvailable.C-zekLsB.css`), and grid rule `before { -webkit-box-sizing:border-box;box-sizing:border-box }`.
4. **Interactive Detail & Feature Matrix (<div.view> — `awards-racing Interactive Matrix`)**:
   - Landmark `<div class="view">` framing `awards-racing Interactive Matrix` and `awards-racing Archive & Directory` (*"awards racing"*) with `#e9e9e9` surface cards, `#ffc500` accents, and `button { background-color:transparent;border:0;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.preloader> — `https://awards.racing`)**:
   - Landmark `<footer class="preloader">` anchoring `Awards Racing` footer links (`Overview · Index · Archive · About · Contact`), copy *"awards-racing Interactive Matrix"*, and `#ff6464` structural dividers.
