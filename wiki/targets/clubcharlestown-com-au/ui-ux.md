---
title: "UI & UX Architecture: clubcharlestown-com-au"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: clubcharlestown-com-au

## Overview & Design Identity
- **Target**: `clubcharlestown-com-au` (**Home · Club Charlestown**)
- **Production URL**: [https://clubcharlestown.com.au/](https://clubcharlestown.com.au/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×5796px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#333333` ink, `#eb8f00` accent)
- **Summary**: We're a vibrant, family-friendly club where everyone belongs. Come in and discover a place to relax, have fun, and connect with friends a...
- **Total Clean CSS Variables Extracted**: `429` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `gotham`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 16px`, `line-height: 18.4px`, `font-weight: 400`); CSS variables `--page-title-display: block`, `--display: flex`, `--n-menu-wrapper-display: flex`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 90px`, `line-height: 90px`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: var(--form-desc-size)`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--label-padding: 0px 0px 5px 0px`, `--arrow-prev-caption-spacing: 15px`, `--arrow-next-caption-spacing: 15px`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#333333` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f9fafb` | `var(--bg-color-disabled)` in `:root` |
| **Interactive Accent / Highlight** | `#eb8f00` | `.ui-state-active a:visited { color: #eb8f00 }` |
| **Secondary / Muted Copy** | `#8d8d8d` | `var(--ss-font-placeholder-color)` in `:root` |
| **Structural Hairline Border** | `#dcdee2` | `var(--ss-border-color)` in `:root` |
| **Variable Token (`--ss-primary-color`)** | `#5897fb` | `var(--ss-primary-color)` in `:root` |
| **Variable Token (`--ss-font-color`)** | `#4d4d4d` | `var(--ss-font-color)` in `:root` |
| **Variable Token (`--ss-highlight-color`)** | `#fffb8c` | `var(--ss-highlight-color)` in `:root` |
| **Variable Token (`--ss-success-color`)** | `#00b755` | `var(--ss-success-color)` in `:root` |
| **Variable Token (`--ss-error-color`)** | `#dc3545` | `var(--ss-error-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ss-primary-color` | `#5897fb` | Brand / Palette Token |
| `--ss-bg-color` | `#ffffff` | Canvas / Surface Token |
| `--ss-font-color` | `#4d4d4d` | Brand / Palette Token |
| `--ss-font-placeholder-color` | `#8d8d8d` | Brand / Palette Token |
| `--ss-disabled-color` | `#dcdee2` | Brand / Palette Token |
| `--ss-border-color` | `#dcdee2` | Brand / Palette Token |
| `--ss-highlight-color` | `#fffb8c` | Canvas / Surface Token |
| `--ss-success-color` | `#00b755` | Brand / Palette Token |
| `--ss-error-color` | `#dc3545` | Brand / Palette Token |
| `--ss-focus-color` | `#5897fb` | Brand / Palette Token |
| `--ss-main-height` | `30px` | Layout / Spatial Grid Token |
| `--ss-content-height` | `300px` | Layout / Spatial Grid Token |
| `--ss-spacing-l` | `7px` | Layout / Spatial Grid Token |
| `--ss-spacing-m` | `5px` | Layout / Spatial Grid Token |
| `--ss-spacing-s` | `3px` | Layout / Spatial Grid Token |
| `--ss-animation-timing` | `0.2s` | Motion / Easing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.elementor> — `clubcharlestown-com-au`)**:
   - Landmark `<header class="elementor elementor-27">` (`1440x163px`) hosting `Home · Club Charlestown` navigation (`What's On What's On · What's On · Functions · Courtesy Bus · Bowls Bowls`), DOM attributes (`data-elementor-device-mode="desktop"`, `data-elementor-type="header"`, `data-elementor-id="27"`, `data-elementor-post-type="elementor_library"`), and stylesheet rule `.tk-gotham-xnarrow { font-family: "gotham-xnarrow",sans-serif; }`.
2. **Hero Stage & Focal Lead (<main.site-main> — `Welcome To Club Charlestown`)**:
   - Landmark `<main class="site-main post-7">` presenting display lead `Welcome To Club Charlestown` and copy excerpt *"We’re a vibrant, family-friendly club where everyone belongs. Com"* over `#ffffff` canvas and `#333333` ink.
3. **Primary Showcase & Content Grid (<main.post-7> — `Welcome to Club Charlestown`)**:
   - Landmark `<main class="site-main post-7">` rendering section `Welcome to Club Charlestown` with copy *"Explore our Bistro & Bars Explore our Bistro & Bars"*, asset references (`recaptcha__en.js`, `www.googletagmanager.com`, `embed`, `ckx4srt.css`), and grid rule `.tk-gotham-narrow { font-family: "gotham-narrow",sans-serif; }`.
4. **Interactive Detail & Feature Matrix (<main.page> — `Beyond a Club, It's a Community`)**:
   - Landmark `<main class="site-main post-7">` framing `Beyond a Club, It's a Community` and `Club Lambton` (*"Explore our Bistro & Bars"*) with `#f9fafb` surface cards, `#eb8f00` accents, and `.tk-gotham-condensed { font-family: "gotham-condensed",sans-serif; }`.
5. **Colophon & Global Directory Footer (<footer.elementor> — `https://clubcharlestown.com.au/`)**:
   - Landmark `<footer class="elementor elementor-63">` anchoring `Home · Club Charlestown` footer links (`What's On What's On · What's On · Functions · Courtesy Bus · Bowls Bowls`), copy *"Book a Table Book a Table"*, and `#dcdee2` structural dividers.
