---
title: "UI & UX Architecture: ksenpanchenko-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: ksenpanchenko-com

## Overview & Design Identity
- **Target**: `ksenpanchenko-com` (**Ksen Panchenko — UX/UI & Product Designer in Dublin · FinTech & SaaS**)
- **Production URL**: [https://ksenpanchenko.com/](https://ksenpanchenko.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f1f0ec` / `#c63a10`)
- **Summary**: Ksen (Kseniia) Panchenko, independent UX/UI & Product Designer in Dublin: websites, products and design systems for FinTech and SaaS — pl...
- **Total Clean CSS Variables Extracted**: `240` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `GeistSans`
- **Body Font Stack**: `GeistSans`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 32px`, `line-height: normal`, `font-weight: 400`); CSS variables `--type-display-size: 220px`, `--type-display-line-height: 198px`, `--type-display-letter-spacing: -6.6px`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 64px`, `line-height: 64px`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--type-body-lead-size: 24px`, `--type-body-lead-line-height: 31.2px`, `--type-body-lead-letter-spacing: 0px`; rule `p` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--font-family-mono: "JetBrains Mono",ui-monospace,monospace`, `--type-display-letter-spacing: -6.6px`, `--type-heading-large-letter-spacing: 0px`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f1f0ec` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `button` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `.hero__pill { background: #ffffff }` |
| **Interactive Accent / Highlight** | `#c63a10` | `var(--color-text-accent-strong)` in `:root` |
| **Secondary / Muted Copy** | `#141414` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#828280` | `:before { border-color: #828280 }` |
| **Variable Token (`--color-neutral-50`)** | `#f4f1ec` | `var(--color-neutral-50)` in `:root` |
| **Variable Token (`--color-neutral-400`)** | `#a8a8a6` | `var(--color-neutral-400)` in `:root` |
| **Variable Token (`--color-neutral-500`)** | `#6b6b6b` | `var(--color-neutral-500)` in `:root` |
| **Variable Token (`--color-neutral-800`)** | `#2b2b2b` | `var(--color-neutral-800)` in `:root` |
| **Variable Token (`--color-orange-500`)** | `#ff5c2e` | `var(--color-orange-500)` in `:root` |
| **Variable Token (`--color-orange-600`)** | `#e8461a` | `var(--color-orange-600)` in `:root` |
| **Variable Token (`--color-green-500`)** | `#4dd973` | `var(--color-green-500)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-neutral-0` | `#ffffff` | Brand / Palette Token |
| `--color-neutral-50` | `#f4f1ec` | Brand / Palette Token |
| `--color-neutral-100` | `#f1f0ec` | Brand / Palette Token |
| `--color-neutral-400` | `#a8a8a6` | Brand / Palette Token |
| `--color-neutral-500` | `#6b6b6b` | Brand / Palette Token |
| `--color-neutral-800` | `#2b2b2b` | Brand / Palette Token |
| `--color-neutral-950` | `#141414` | Brand / Palette Token |
| `--color-orange-500` | `#ff5c2e` | Brand / Palette Token |
| `--color-orange-600` | `#e8461a` | Brand / Palette Token |
| `--color-green-500` | `#4dd973` | Brand / Palette Token |
| `--font-family-serif` | `var(--font-serif-loaded,"Instrument Serif"),Georgia,serif` | Typography / Scale Token |
| `--font-family-sans` | `"Geist",system-ui,sans-serif` | Typography / Scale Token |
| `--font-family-mono` | `"JetBrains Mono",ui-monospace,monospace` | Typography / Scale Token |
| `--space-0` | `0px` | Layout / Spatial Grid Token |
| `--space-4` | `4px` | Layout / Spatial Grid Token |
| `--space-8` | `8px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav> — `ksenpanchenko-com`)**:
   - Landmark `<header class="nav">` (`1440x56px`) hosting `Ksen Panchenko — UX/UI & Product Des` navigation (`Work · About`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-end="1"`), and stylesheet rule `.hero__center { position:relative;width:733px;max-width:100%;margin:0 auto;padding-top:21px }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Ksen Panchenko — UX/UI & Product D`)**:
   - Landmark `<section class="hero">` presenting display lead `Ksen Panchenko — UX/UI & Product Designer in Dubl...` and copy excerpt *"Available for projects"* over `#f1f0ec` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.sw> — `Selected work`)**:
   - Landmark `<section class="sw">` rendering section `Selected work` with copy *"Gold London Design Awards 2026 · Emerald24 · UI Design"*, asset references (`7cb8e1b9ab81be17-s.p.woff2`, `dbccb4a9e22cbf0d-s.p.woff2`, `e872e3f251959e82-s.p.woff2`, `kseniia-cutout.webp`), and grid rule `.hero__name { display:grid;margin:0;font-weight:400 }`.
4. **Interactive Detail & Feature Matrix (<section.philo> — `Product & UX`)**:
   - Landmark `<section class="philo">` framing `Product & UX` and `Web & Systems` (*"London Design Awards 2026 · Emerald24 · UI Design"*) with `#ffffff` surface cards, `#c63a10` accents, and `.hero__name>.text-display-hero { padding-left:131px }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://ksenpanchenko.com/`)**:
   - Landmark `<footer class="footer">` anchoring `Ksen Panchenko — UX/UI & Product` footer links (`Work · About`), copy *"Ksen Panchenko — UX/UI & Product Designer in Dublin."*, and `#828280` structural dividers.
