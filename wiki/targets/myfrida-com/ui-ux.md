---
title: "UI & UX Architecture: myfrida-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: myfrida-com

## Overview & Design Identity
- **Target**: `myfrida-com` (**My Frida · Chocolate-Covered Fruit, Smoothies & Cake Bars**)
- **Production URL**: [https://myfrida.com/](https://myfrida.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#020a0a` ink, `#0d6efd` accent)
- **Summary**: Discover My Frida: real fruit wrapped in chocolate, fruity Choco Smoothies, frozen treats and layered Fridika Cake Bars. Find your favour...
- **Total Clean CSS Variables Extracted**: `497` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Source Sans Pro`
- **Body Font Stack**: `Source Sans Pro`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 40px`, `line-height: 48px`, `font-weight: 900`); rule `,.h1` (`line-height: 1.2`, `font-weight: 500`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 110.16px`, `line-height: 92.8649px`, `font-weight: 900`); rule `,.h2` (`font-size: calc(1.325rem + 0.9vw)`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--bs-body-font-family: var(--bs-font-sans-serif)`, `--bs-body-font-size: 1rem`, `--bs-body-font-weight: 400`; rule `p` (`font-size: min(1vw,20px)`, `line-height: 1.2`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#020a0a` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f8f9fa` | `var(--bs-tertiary-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#0d6efd` | `var(--bs-primary)` in `:root` |
| **Secondary / Muted Copy** | `#6c757d` | `var(--bs-secondary)` in `:root` |
| **Structural Hairline Border** | `#9ec5fe` | `var(--bs-primary-border-subtle)` in `:root` |
| **Variable Token (`--bs-indigo`)** | `#6610f2` | `var(--bs-indigo)` in `:root` |
| **Variable Token (`--bs-purple`)** | `#6f42c1` | `var(--bs-purple)` in `:root` |
| **Variable Token (`--bs-pink`)** | `#d63384` | `var(--bs-pink)` in `:root` |
| **Variable Token (`--bs-red`)** | `#dc3545` | `var(--bs-red)` in `:root` |
| **Variable Token (`--bs-orange`)** | `#fd7e14` | `var(--bs-orange)` in `:root` |
| **Variable Token (`--bs-yellow`)** | `#ffc107` | `var(--bs-yellow)` in `:root` |
| **Variable Token (`--bs-green`)** | `#198754` | `var(--bs-green)` in `:root` |
| **Variable Token (`--bs-teal`)** | `#20c997` | `var(--bs-teal)` in `:root` |
| **Variable Token (`--bs-cyan`)** | `#0dcaf0` | `var(--bs-cyan)` in `:root` |
| **Variable Token (`--bs-black`)** | `#000000` | `var(--bs-black)` in `:root` |
| **Variable Token (`--bs-gray-dark`)** | `#343a40` | `var(--bs-gray-dark)` in `:root` |
| **Variable Token (`--bs-gray-200`)** | `#e9ecef` | `var(--bs-gray-200)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bs-blue` | `#0d6efd` | Color / Atmospheric Token |
| `--bs-indigo` | `#6610f2` | Color / Atmospheric Token |
| `--bs-purple` | `#6f42c1` | Color / Atmospheric Token |
| `--bs-pink` | `#d63384` | Typography Ink Token |
| `--bs-red` | `#dc3545` | Color / Atmospheric Token |
| `--bs-orange` | `#fd7e14` | Color / Atmospheric Token |
| `--bs-yellow` | `#ffc107` | Color / Atmospheric Token |
| `--bs-green` | `#198754` | Color / Atmospheric Token |
| `--bs-teal` | `#20c997` | Color / Atmospheric Token |
| `--bs-cyan` | `#0dcaf0` | Color / Atmospheric Token |
| `--bs-black` | `#000` | Canvas / Surface Token |
| `--bs-white` | `#fff` | Canvas / Surface Token |
| `--bs-gray` | `#6c757d` | Color / Atmospheric Token |
| `--bs-gray-dark` | `#343a40` | Canvas / Surface Token |
| `--bs-gray-100` | `#f8f9fa` | Color / Atmospheric Token |
| `--bs-gray-200` | `#e9ecef` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.webp> — `myfrida-com`)**:
   - Landmark `<header class="webp">` (`1440x114px`) hosting `My Frida · Chocolate-Covered Fruit, ` navigation (`Meet Frida · Contact us`), DOM attributes (`data-smush-preload`, `data-rocket-prefetch`, `data-rocket-preload`, `data-minify="1"`), and stylesheet rule `.fa-lg { font-size:1.33333em;line-height:.75em;vertical-align:-.0667em }`.
2. **Hero Stage & Focal Lead (<section.tf-hero> — `My Frida my moment`)**:
   - Landmark `<section class="tf-hero">` presenting display lead `My Frida my moment` and copy excerpt *"Frida always had a way of making moments a little sweeter."* over `#ffffff` canvas and `#020a0a` ink.
3. **Primary Showcase & Content Grid (<section.tf-uvod> — `Whatever you call her,`)**:
   - Landmark `<section class="tf-uvod container-fluid">` rendering section `Whatever you call her,` with copy *"Choco Fruits Frozen ›"*, asset references (`myfrida-hero-frozen-1200.webp`, `b4751355.assetcdn.net`, `www.googletagmanager.com`, `myfrida-source-sans-pro-400-latin...`), and grid rule `.fa-xs { font-size:.75em }`.
4. **Interactive Detail & Feature Matrix (<section.tf-marquee> — `Choco Fruits`)**:
   - Landmark `<section class="tf-marquee container-fluid">` framing `Choco Fruits` and `Choco Smoothies` (*"Frida always had a way of"*) with `#f8f9fa` surface cards, `#0d6efd` accents, and `.fa-sm { font-size:.875em }`.
5. **Colophon & Global Directory Footer (<footer.home> — `https://myfrida.com/`)**:
   - Landmark `<footer class="home">` anchoring `My Frida · Chocolate-Covered Fru` footer links (`Meet Frida · Contact us`), copy *"making moments a little sweeter."*, and `#9ec5fe` structural dividers.
