# UI & UX Architecture: www-upscayl-app

## Overview & Design Identity
- **Target**: `www-upscayl-app` (**Upscale Image Online Free – Upscale to 8K with AI · Upscayl**)
- **Production URL**: [https://www.upscayl.app](https://www.upscayl.app)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#9ca3af` ink, `#f59e0b` accent)
- **Summary**: Enhance blurry, pixelated, or low-resolution photos online with AI-powered upscaling. Choose an enhancement mode, preview the result, and...
- **Total Clean CSS Variables Extracted**: `77` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.5rem`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 1.875rem!important`)
- **Body Copy**: rule `p` (`font-size: .875rem!important`, `line-height: 1.25rem!important`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.5rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--normal-bg)` in `:root` |
| **Primary Typography Ink** | `#e5e7eb` | `:before { border: #e5e7eb }` |
| **Elevated Surface / Card Substrate** | `#9ca3af` | `textarea::placeholder { color: #9ca3af }` |
| **Interactive Accent / Highlight** | `#f59e0b` | `.fill-amber-500 { fill: #f59e0b }` |
| **Secondary / Muted Copy** | `#facc15` | `.fill-yellow-400 { fill: #facc15 }` |
| **Structural Hairline Border** | `#6ee7b7` | `.decoration-emerald-300 { color: #6ee7b7 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--sidebar-background` | `var(--background)` | Canvas / Surface Token |
| `--sidebar-foreground` | `var(--foreground)` | Typography Ink Token |
| `--sidebar-primary` | `var(--primary)` | Brand / Palette Token |
| `--sidebar-primary-foreground` | `var(--primary-foreground)` | Typography Ink Token |
| `--sidebar-accent` | `var(--background)` | Brand / Palette Token |
| `--sidebar-accent-foreground` | `var(--primary)` | Typography Ink Token |
| `--sidebar-border` | `var(--border)` | Elevation / Border Token |
| `--sidebar-ring` | `var(--ring)` | Elevation / Border Token |
| `--background` | `0 0% 100%` | Canvas / Surface Token |
| `--foreground` | `20 14.3% 4.1%` | Typography Ink Token |
| `--card` | `0 0% 100%` | Dimension / Scale Token |
| `--card-foreground` | `20 14.3% 4.1%` | Typography Ink Token |
| `--popover` | `0 0% 100%` | Dimension / Scale Token |
| `--popover-foreground` | `20 14.3% 4.1%` | Typography Ink Token |
| `--primary` | `175 82% 42%` | Brand / Palette Token |
| `--primary-foreground` | `0 0% 100%` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.relative> — `www-upscayl-app`)**:
   - Landmark `<header class="relative z-50">` hosting `Upscale Image Online Free – Upscale ` navigation (`AI Photo Editor · Image Enhancer · AI Image Tools · Pricing · API`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-nimg="1"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Upscale Image Online Free with AI`)**:
   - Landmark `<section class="relative py-8">` presenting display lead `Upscale Image Online Free with AI` and copy excerpt *"Upscale Image Online Free with AI"* over `#fff` canvas and `#9ca3af` ink.
3. **Primary Showcase & Content Grid (<section.py-12> — `Upscayl AI Image Upscaler`)**:
   - Landmark `<section class="py-12 bg-gradient-to-b">` rendering section `Upscayl AI Image Upscaler` with copy *"The ultimate Upscayl AI Image Upscaler for crystal-clear 4K image"*, asset references (`5544ee6471eef55b.css`, `46fac02034242723.css`, `c50624e23d0abf09.css`, `webpack-c03deb5affb2ddad.js`), and grid rule `body { margin:0;line-height:inherit }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Explore other tools`)**:
   - Landmark `<section class="relative overflow-hidden">` framing `Explore other tools` and `Upscayl AI Image Upscaler Features` (*"Enhance blurry, pixelated, or low-resolution photos online with A"*) with `#9ca3af` surface cards, `#f59e0b` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.antialiased> — `https://www.upscayl.app`)**:
   - Landmark `<footer class="antialiased">` anchoring `Upscale Image Online Free – Upsc` footer links (`AI Photo Editor · Image Enhancer · AI Image Tools · Pricing · API`), copy *"Try Upscayl AI Image Upscaler for Free"*, and `#6ee7b7` structural dividers.
