---
title: "UI & UX Architecture: www-weisslameraner-com_en"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-weisslameraner-com_en

## Overview & Design Identity
- **Target**: `www-weisslameraner-com_en` (**Weiss & Lameraner Media Group – Lifestyle Media House Vienna**)
- **Production URL**: [https://www.weisslameraner.com/en](https://www.weisslameraner.com/en)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#171717` accent)
- **Summary**: Vienna media house: STYLE UP YOUR LIFE!, Y, OBEGG and ADIWEISS.TV. Advertising in print, online, social and TV, plus content and events f...
- **Total Clean CSS Variables Extracted**: `152` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `figtreeUpright`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 72px`, `line-height: 77.76px`, `font-weight: 300`, `letter-spacing: -1.8px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: live computed `h2 (largest visible desktop heading)` (`font-size: 60px`, `line-height: 1.2`, `font-weight: 400`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: inherit`, `line-height: normal`, `letter-spacing: normal`, `font-weight: inherit`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`; rule `small` (`font-size: .36em`, `letter-spacing: .02em`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `section` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#808080` | `.bg-gray-100 { background-color: gray }` (`#808080`) |
| **Interactive Accent / Highlight** | `#171717` | `var(--primary)` in `:root` |
| **Secondary / Muted Copy** | `#737373` | `var(--muted-foreground)` in `:root` |
| **Structural Hairline Border** | `#e5e5e5` | `var(--border)` in `:root` |
| **Variable Token (`--foreground`)** | `#0a0a0a` | `var(--foreground)` in `:root` |
| **Variable Token (`--primary-foreground`)** | `#fafafa` | `var(--primary-foreground)` in `:root` |
| **Variable Token (`--secondary`)** | `#f5f5f5` | `var(--secondary)` in `:root` |
| **Variable Token (`--destructive`)** | `#e40014` | `var(--destructive)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--radius` | `.625rem` | Elevation / Border Token |
| `--background` | `#fff` | Canvas / Surface Token |
| `--foreground` | `#0a0a0a` | Typography Ink Token |
| `--card` | `#fff` | Color / Atmospheric Token |
| `--card-foreground` | `#0a0a0a` | Typography Ink Token |
| `--popover` | `#fff` | Color / Atmospheric Token |
| `--popover-foreground` | `#0a0a0a` | Typography Ink Token |
| `--primary` | `#171717` | Brand / Palette Token |
| `--primary-foreground` | `#fafafa` | Typography Ink Token |
| `--secondary` | `#f5f5f5` | Brand / Palette Token |
| `--secondary-foreground` | `#171717` | Typography Ink Token |
| `--muted` | `#f5f5f5` | Color / Atmospheric Token |
| `--muted-foreground` | `#737373` | Typography Ink Token |
| `--accent` | `#f5f5f5` | Brand / Palette Token |
| `--accent-foreground` | `#171717` | Typography Ink Token |
| `--destructive` | `#e40014` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.top-0> — `www-weisslameraner-com_en`)**:
   - Landmark `<header class="top-0 left-0">` (`1440x85px`) hosting `Weiss & Lameraner Media Group – Life` navigation (`About · Services · Media · Brand Events · WLX`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="cms-o9gdh8"`, `data-href="cms-o9gdh8"`), and stylesheet rule `ight_6c9c2d2c-module__T-NGCq__cla... { font-family:figtreeUpright,figtreeUpright Fallback }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Lifestyle media for your brand.`)**:
   - Landmark `<section class="relative bg-white">` presenting display lead `Lifestyle media for your brand.` and copy excerpt *"Since 2009 we have been taking brands to where their audience is:"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.bg-white> — `Brands that work with us.`)**:
   - Landmark `<section class="bg-white py-16">` rendering section `Brands that work with us.` with copy *"Media Data 2027 Media Data 2027"*, asset references (`Figtree_VariableFont_wght-s.p.0r5...`, `3emm7imx_eab9.css`, `1lfjsiuslldzn.css`, `37mpl03i35te0.js`), and grid rule `right_6c9c2d2c-module__T-NGCq__va... { --font-figtree:"figtreeUpright", "figtreeUpright Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.bg-stone-950> — `Austria's media house for lifestyl`)**:
   - Landmark `<section class="bg-stone-950 relative">` framing `Austria's media house for lifestyle.` and `Guide for brands What do you want to achieve? Dis...` (*"(opens in a new window)"*) with `#808080` surface cards, `#171717` accents, and `alic_2112d0a2-module__njfJ-W__cla... { font-family:figtreeItalic,figtreeItalic Fallback }`.
5. **Colophon & Global Directory Footer (<footer.bg-stone-950> — `https://www.weisslameraner.com/en`)**:
   - Landmark `<footer class="bg-stone-950 font-sans">` anchoring `Weiss & Lameraner Media Group – ` footer links (`About · Services · Media · Brand Events · WLX`), copy *"Austria's media house"*, and `#e5e5e5` structural dividers.
