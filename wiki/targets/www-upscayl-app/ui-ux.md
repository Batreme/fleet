---
title: "UI & UX Architecture: www-upscayl-app"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-upscayl-app

## Overview & Design Identity
- **Target**: `www-upscayl-app` (**Upscale Image Online Free – Upscale to 8K with AI · Upscayl**)
- **Production URL**: [https://www.upscayl.app](https://www.upscayl.app)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#0c0a09` ink, `#2563eb` accent)
- **Summary**: Enhance blurry, pixelated, or low-resolution photos online with AI-powered upscaling. Choose an enhancement mode, preview the result, and...
- **Total Clean CSS Variables Extracted**: `77` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 72px`, `line-height: 72px`, `font-weight: 700`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 48px`, `line-height: 48px`, `font-weight: 700`); rule `h2` (`font-size: 1.875rem`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: .875rem`, `line-height: 1.25rem`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0c0a09` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f3ede4` | `:hover { background: #f3ede4 }` |
| **Interactive Accent / Highlight** | `#2563eb` | `.accent-blue-600 { color: #2563eb }` |
| **Secondary / Muted Copy** | `#628481` | live computed `button` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#def1e9` | `65 { border-color: #def1e9 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background` | `0 0% 100%` | Canvas / Surface Token |
| `--foreground` | `20 14.3% 4.1%` | Typography Ink Token |
| `--card` | `0 0% 100%` | Dimension / Scale Token |
| `--card-foreground` | `20 14.3% 4.1%` | Typography Ink Token |
| `--popover` | `0 0% 100%` | Dimension / Scale Token |
| `--popover-foreground` | `20 14.3% 4.1%` | Typography Ink Token |
| `--primary` | `175 82% 42%` | Brand / Palette Token |
| `--primary-foreground` | `0 0% 100%` | Typography Ink Token |
| `--secondary` | `180 25% 95%` | Brand / Palette Token |
| `--secondary-foreground` | `175 25% 15%` | Typography Ink Token |
| `--muted` | `180 20% 95%` | Dimension / Scale Token |
| `--muted-foreground` | `175 15% 45%` | Typography Ink Token |
| `--accent` | `180 25% 95%` | Brand / Palette Token |
| `--accent-foreground` | `175 25% 15%` | Typography Ink Token |
| `--destructive` | `0 84.2% 60.2%` | Dimension / Scale Token |
| `--destructive-foreground` | `60 9.1% 97.8%` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.bg-background> — `www-upscayl-app`)**:
   - Landmark `<header class="bg-background relative">` (`1440x65px`) hosting `Upscale Image Online Free – Upscale ` navigation (`AI Photo Editor · Image Enhancer · AI Image Tools · Pricing · API`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.py-8> — `Upscale Image Online Free with AI`)**:
   - Landmark `<section class="py-8 bg-gradient-to-br">` presenting display lead `Upscale Image Online Free with AI` and copy excerpt *"The ultimate Upscayl AI Image Upscaler for crystal-clear 4K image"* over `#ffffff` canvas and `#0c0a09` ink.
3. **Primary Showcase & Content Grid (<section.bg-gradient-to-b> — `Upscayl AI Image Upscaler`)**:
   - Landmark `<section class="bg-gradient-to-b via-white">` rendering section `Upscayl AI Image Upscaler` with copy *"Upscale Image Online Free with AI"*, asset references (`5544ee6471eef55b.css`, `a4aeb68a5f6d17c2.css`, `c50624e23d0abf09.css`, `520cfa8ebc6f0a4b.css`), and grid rule `body { margin:0;line-height:inherit }`.
4. **Interactive Detail & Feature Matrix (<section.py-10> — `Explore other tools`)**:
   - Landmark `<section class="py-10 relative">` framing `Explore other tools` and `Upscayl AI Image Upscaler Features` (*"Enhance blurry, pixelated, or low-resolution photos online with A"*) with `#f3ede4` surface cards, `#2563eb` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.antialiased> — `https://www.upscayl.app`)**:
   - Landmark `<footer class="antialiased">` anchoring `Upscale Image Online Free – Upsc` footer links (`AI Photo Editor · Image Enhancer · AI Image Tools · Pricing · API`), copy *"Try Upscayl AI Image Upscaler for Free"*, and `#def1e9` structural dividers.
