---
title: "UI & UX Architecture: spykercars-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: spykercars-com

## Overview & Design Identity
- **Target**: `spykercars-com` (**Hand-Built Super Sports Cars Since 1880 · Spyker Cars**)
- **Production URL**: [https://spykercars.com/](https://spykercars.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#0000ff` accent)
- **Summary**: Spyker builds highly exclusive, hand-built super sports cars in the Netherlands. Discover the C8 Preliator XXV Coupé and the marque's sto...
- **Total Clean CSS Variables Extracted**: `169` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `futura-pt-condensed`
- **Body Font Stack**: `swiss721`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 56px`, `line-height: 47.6px`, `font-weight: 500`, `letter-spacing: 2.24px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 56px`, `line-height: 47.6px`, `font-weight: 500`, `letter-spacing: 2.24px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 38px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`; rule `p` (`font-size: var(--text-sm)`, `line-height: var(--tw-leading,var(...`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-mono: ui-monospace,SFMono-Regular,monospace`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `p` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f24822` | `.animated-grid__col { background-color: #f24822 }` |
| **Interactive Accent / Highlight** | `#0000ff` | `.border-blue-600 { border-color: #0000ff }` |
| **Secondary / Muted Copy** | `#101010` | live computed `h2` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e5e5e5` | `10 { border-color: #e5e5e5 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background` | `oklch(100% 0 0)` | Canvas / Surface Token |
| `--foreground` | `oklch(14.5% 0 0)` | Typography Ink Token |
| `--card` | `oklch(96.5% .005 265)` | Color / Atmospheric Token |
| `--card-foreground` | `oklch(14.5% 0 0)` | Typography Ink Token |
| `--popover` | `oklch(100% 0 0)` | Color / Atmospheric Token |
| `--popover-foreground` | `oklch(14.5% 0 0)` | Typography Ink Token |
| `--primary` | `oklch(20.5% 0 0)` | Brand / Palette Token |
| `--primary-foreground` | `oklch(98.5% 0 0)` | Typography Ink Token |
| `--secondary` | `oklch(97% 0 0)` | Brand / Palette Token |
| `--secondary-foreground` | `oklch(20.5% 0 0)` | Typography Ink Token |
| `--muted` | `oklch(97% 0 0)` | Color / Atmospheric Token |
| `--muted-foreground` | `oklch(55.6% 0 0)` | Typography Ink Token |
| `--accent` | `oklch(97% 0 0)` | Brand / Palette Token |
| `--accent-foreground` | `oklch(20.5% 0 0)` | Typography Ink Token |
| `--destructive` | `oklch(57.7% .245 27.325)` | Color / Atmospheric Token |
| `--destructive-foreground` | `oklch(57.7% .245 27.325)` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.py-4> — `spykercars-com`)**:
   - Landmark `<nav class="py-4 container">` (`1425x88px`) hosting `Hand-Built Super Sports Cars Since 1` navigation (`Home · Heritage · Boutique · News · Contact`), DOM attributes (`data-theme="light"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.__className_e6d04a { font-family:swiss721,swiss721 Fallback }`.
2. **Hero Stage & Focal Lead (<article.lenis-autoToggle> — `THE NEXT CHAPTER OF SPYKER`)**:
   - Landmark `<article class="lenis-autoToggle">` presenting display lead `THE NEXT CHAPTER OF SPYKER` and copy excerpt *"We use cookies to run the site, and optionally for analytics and "* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.w-full> — `The next chapter of Spyker T h e n`)**:
   - Landmark `<section class="w-full relative">` rendering section `The next chapter of Spyker T h e n e x t c h a p...` with copy *"T h e b e g i n n i n g o f X X V"*, asset references (`f13a7bda184fa931.css`, `86c130d7567786c0.css`, `3c4afd8b2a3df79a.css`, `cdb4fb19178d4946.css`), and grid rule `.__variable_e6d04a { --font-swiss-721:"swiss721","swiss721 Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.fixed> — `P u r e P a s s i o n`)**:
   - Landmark `<section class="fixed">` framing `P u r e P a s s i o n` and `N u l l a T e n a c i I n v i a E s t V i a` (*"The next chapter of Spyker"*) with `#f24822` surface cards, `#0000ff` accents, and `.__className_83cf94 { font-family:"PT Serif","PT Serif Fallback";font-weight:400;font-style:no... }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://spykercars.com/`)**:
   - Landmark `<footer class="relative z-30">` anchoring `Hand-Built Super Sports Cars Sin` footer links (`Home · Heritage · Boutique · News · Contact`), copy *"T h e n e x t c h a p t e r o f S p y k e r"*, and `#e5e5e5` structural dividers.
