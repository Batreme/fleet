---
title: "UI & UX Architecture: henrietta-wearetattoodigital-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: henrietta-wearetattoodigital-com

## Overview & Design Identity
- **Target**: `henrietta-wearetattoodigital-com` (**Henrietta Said : Scandalously Spicy**)
- **Production URL**: [https://henrietta.wearetattoodigital.com/](https://henrietta.wearetattoodigital.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#e3a898` / `#ffa500`)
- **Summary**: It’s hard to contain this kind of spiciness. That’s why we’re bringing our scandalously spicy selves to the mainstream with bold wing-fla...
- **Total Clean CSS Variables Extracted**: `21` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Sink`
- **Body Font Stack**: `Helvetica Neue`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 403.2px`, `line-height: 362.88px`, `font-weight: 900`, `letter-spacing: 4.32px`); rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: live computed `body` (`font-size: 14px`, `line-height: 20px`, `font-weight: 400`); rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 20px`, `font-weight: 400`); rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#e3a898` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#333333` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#dddddd` | live computed `nav` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ffa500` | `.button-v-1.buffalo { color: orange }` (`#ffa500`) |
| **Secondary / Muted Copy** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Structural Hairline Border** | `#e2e2e2` | `blockquote { border-left: #e2e2e2 }` |
| **Variable Token (`--kimchi-red`)** | `#d32929` | `var(--kimchi-red)` in `:root` |
| **Variable Token (`--light-grey`)** | `#eae6e3` | `var(--light-grey)` in `:root` |
| **Variable Token (`--brown-chicken`)** | `#8b231a` | `var(--brown-chicken)` in `:root` |
| **Variable Token (`--orange`)** | `#f45016` | `var(--orange)` in `:root` |
| **Variable Token (`--lemon`)** | `#efc415` | `var(--lemon)` in `:root` |
| **Variable Token (`--dark`)** | `#2d2a26` | `var(--dark)` in `:root` |
| **Variable Token (`--white`)** | `#ffffff` | `var(--white)` in `:root` |
| **Variable Token (`--black`)** | `#0e0e0e` | `var(--black)` in `:root` |
| **Variable Token (`--salmon`)** | `#f7894e` | `var(--salmon)` in `:root` |
| **Variable Token (`--dark-red`)** | `#761615` | `var(--dark-red)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--body` | `#e3a898` | Color / Atmospheric Token |
| `--kimchi-red` | `#d32929` | Color / Atmospheric Token |
| `--light-grey` | `#eae6e3` | Canvas / Surface Token |
| `--brown-chicken` | `#8b231a` | Color / Atmospheric Token |
| `--orange` | `#f45016` | Color / Atmospheric Token |
| `--lemon` | `#efc415` | Color / Atmospheric Token |
| `--dark` | `#2d2a26` | Canvas / Surface Token |
| `--white` | `#fff` | Canvas / Surface Token |
| `--black` | `#0E0E0E` | Canvas / Surface Token |
| `--salmon` | `#f7894e` | Color / Atmospheric Token |
| `--dark-red` | `#761615` | Canvas / Surface Token |
| `--blush` | `#e3a898` | Color / Atmospheric Token |
| `--hst-duration-exit` | `0.8s` | Motion / Easing Token |
| `--hst-duration-enter` | `0.95s` | Motion / Easing Token |
| `--hst-easing` | `cubic-bezier(0.76, 0, 0.24, 1)` | Motion / Easing Token |
| `--hst-scale` | `0.9` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.our-products-list> — `henrietta-wearetattoodigital-com`)**:
   - Landmark `<nav class="our-products-list w-dropdown-list">` (`1440px`) hosting `Henrietta Said : Scandalously Spicy` navigation (`ancho kimchi · original buffalo · lemon pepper`), DOM attributes (`data-wf-domain="henrietta.wearetattoo..."`, `data-wf-page="69fc9bd508ea045856fc2e42"`, `data-wf-site="69fc9bd208ea045856fc2c0a"`, `data-preloader-counter`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<div.preloader> — `KIMCHI`)**:
   - Landmark `<div class="preloader">` presenting display lead `KIMCHI` and copy excerpt *"Jumbo roasted peanuts with a fusion of flavorfully fun ancho kimc"* over `#e3a898` canvas and `#333333` ink.
3. **Primary Showcase & Content Grid (<div.preloader:nth(2)> — `Jumbo roasted peanuts with a fusio`)**:
   - Landmark `<div class="preloader">` rendering section `Jumbo roasted peanuts with a fusion of flavorful` with copy *"Jumbo roasted peanuts with bodaciously bold Nashville hot Chicken"*, asset references (`cdn.prod.website-files.com`, `henrietta-said.webflow.shared.afe...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<div.preloader:nth(3)> — `Jumbo roasted peanuts with bodacio`)**:
   - Landmark `<div class="preloader">` framing `Jumbo roasted peanuts with bodaciously bold Nash` and `Jumbo roasted peanuts with totally twangy buffal` (*"Jumbo roasted peanuts with totally twangy buffalo vinegar seasoni"*) with `#dddddd` surface cards, `#ffa500` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.w-mod-ix3> — `https://henrietta.wearetattoodigital.com/`)**:
   - Landmark `<footer class="w-mod-ix3">` anchoring `Henrietta Said : Scandalously Sp` footer links (`ancho kimchi · original buffalo · lemon pepper`), copy *"Jumbo roasted peanuts with primarily primo lemon pepper seas"*, and `#e2e2e2` structural dividers.
