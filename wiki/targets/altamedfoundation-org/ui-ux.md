---
title: "UI & UX Architecture: altamedfoundation-org"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: altamedfoundation-org

## Overview & Design Identity
- **Target**: `altamedfoundation-org` (**AltaMed Foundation · AltaMed Foundation**)
- **Production URL**: [https://altamedfoundation.org/](https://altamedfoundation.org/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×4140px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#242029` accent)
- **Summary**: AltaMed ensures everyone in our community has access to quality health care, enabling them to live healthy, happy lives.
- **Total Clean CSS Variables Extracted**: `175` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `proxima-nova`
- **Body Font Stack**: `proxima-nova`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 45px`, `line-height: 50px`, `font-weight: 600`); CSS variables `--text-3xl: 1.875rem`, `--text-3xl--line-height: calc(2.25 / 1.875)`, `--text-title-lg: 34px`
- **Body Copy**: live computed `body` (`font-size: 20px`, `line-height: 30px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`, `--font-size-body: 18px`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 20px`, `line-height: 30px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `p` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffa500` | `.bg-campaign-orange { background-color: orange }` (`#ffa500`) |
| **Interactive Accent / Highlight** | `#242029` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#737373` | `var(--muted-foreground)` in `:root` |
| **Structural Hairline Border** | `#e5e5e5` | `var(--border)` in `:root` |
| **Variable Token (`--foreground`)** | `#0a0a0a` | `var(--foreground)` in `:root` |
| **Variable Token (`--primary`)** | `#171717` | `var(--primary)` in `:root` |
| **Variable Token (`--primary-foreground`)** | `#fafafa` | `var(--primary-foreground)` in `:root` |
| **Variable Token (`--secondary`)** | `#f5f5f5` | `var(--secondary)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--sticky-cta-height` | `calc(.75rem + 3.5rem + max(.75rem, env(safe-area-inset-bottom)))` | Brand / Palette Token |
| `--radius` | `.5rem` | Elevation / Border Token |
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

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.relative> — `altamedfoundation-org`)**:
   - Landmark `<header class="relative z-50">` (`1440x129px`) hosting `AltaMed Foundation · AltaMed Foundat` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-scroll-behavior="smooth"`, `data-precedence="next"`, `data-href="/_next/static/immutab..."`, `data-nimg="1"`), and stylesheet rule `.tk-proxima-nova { font-family: "proxima-nova",sans-serif; }`.
2. **Hero Stage & Focal Lead (<section.bg-white> — `H.E.L.P. Campaign`)**:
   - Landmark `<section class="bg-white py-12">` presenting display lead `H.E.L.P. Campaign` and copy excerpt *"AltaMed ensures everyone in our community has access to quality h"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.scroll-mt-24> — `Impact Stories`)**:
   - Landmark `<section class="scroll-mt-24 bg-purple">` rendering section `Impact Stories` with copy *"Health. Equity. Life. Programs."*, asset references (`vdqo9h3n.api.sanity.io`, `altamed-foundation-logo.svg`, `3kc4s5-t1h7ps.js`, `1h6ujiewnnn1_.js`), and grid rule `.tk-gotham-xnarrow { font-family: "gotham-xnarrow",sans-serif; }`.
4. **Interactive Detail & Feature Matrix (<section.py-12> — `Homeward Bound: Preemie Twins’ Inc`)**:
   - Landmark `<section class="scroll-mt-24 bg-white">` framing `Homeward Bound: Preemie Twins’ Incredible Journey...` and `Make a Difference` (*"Learn More about the H.E.L.P. Campaign"*) with `#ffa500` surface cards, `#242029` accents, and `.tk-gotham-narrow { font-family: "gotham-narrow",sans-serif; }`.
5. **Colophon & Global Directory Footer (<footer.pt-8> — `https://altamedfoundation.org/`)**:
   - Landmark `<footer class="pt-8 pb-8">` anchoring `AltaMed Foundation · AltaMed Fou` footer links (`Overview · Index · Archive · About · Contact`), copy *"about the H.E.L.P. Campaign"*, and `#e5e5e5` structural dividers.
