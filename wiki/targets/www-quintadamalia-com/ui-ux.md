---
title: "UI & UX Architecture: www-quintadamalia-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-quintadamalia-com

## Overview & Design Identity
- **Target**: `www-quintadamalia-com` (**Quinta D. Amália - Redefining Luxury Living in Portugal**)
- **Production URL**: [https://www.quintadamalia.com/](https://www.quintadamalia.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#1e1e1e` ink, `#007fff` accent)
- **Summary**: Set in the heart of Vila Nova de Gaia, Quinta D. Amália is more than a residence - it’s a lifestyle defined by exclusivity, wellness & na...
- **Total Clean CSS Variables Extracted**: `574` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Marcellus`
- **Body Font Stack**: `Syne`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 140px`, `line-height: 140px`, `font-weight: 400`, `letter-spacing: -5.6px`); CSS variables `--page-title-display: block`, `--display: flex`; rule `,h1` (`font-size: calc(1.375rem + 1.5vw)`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 200px`, `line-height: 200px`, `font-weight: 400`, `letter-spacing: -4px`); rule `,h2` (`font-size: calc(1.325rem + .9vw)`)
- **Body Copy**: live computed `body` (`font-size: 14px`, `line-height: 26px`, `font-weight: 400`); CSS variables `--bs-body-font-family: var(--bs-font-sans-serif)`, `--bs-body-font-size: 1rem`, `--bs-body-font-weight: 400`; rule `p` (`font-size: 22px`, `line-height: 1.36`, `letter-spacing: -.02em`, `font-weight: 500`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 26px`, `font-weight: 400`); rule `,small` (`font-size: .875em`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1e1e1e` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f5f7f5` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#007fff` | `a.ui-button:active { background: #007fff }` |
| **Secondary / Muted Copy** | `#7a7a7a` | `var(--e-global-color-text)` in `:root` |
| **Structural Hairline Border** | `#9ec5fe` | `var(--bs-primary-border-subtle)` in `:root` |
| **Variable Token (`--bs-blue`)** | `#0d6efd` | `var(--bs-blue)` in `:root` |
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
| **Variable Token (`--bs-gray`)** | `#6c757d` | `var(--bs-gray)` in `:root` |
| **Variable Token (`--bs-gray-dark`)** | `#343a40` | `var(--bs-gray-dark)` in `:root` |
| **Variable Token (`--bs-gray-100`)** | `#f8f9fa` | `var(--bs-gray-100)` in `:root` |
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
1. **Brand Header & Navigation Bar (<header.qda-header> — `www-quintadamalia-com`)**:
   - Landmark `<header class="qda-header">` (`1440x78px`) hosting `Quinta D. Amália - Redefining Luxury` navigation (`Home · About · Apartments · Lifestyle · Contact`), DOM attributes (`data-rocket-preload`, `data-wpr-hosted-gf-parameters="family=Big+Shoulders+..."`, `data-wpr-hosted-gf-parameters="family=Big+Shoulders+..."`, `data-wpr-hosted-gf-parameters`), and stylesheet rule `.themepure-theme-btn:hover { background-color:var(--tp-common-white);border-color:var(--tp-common-bla... }`.
2. **Hero Stage & Focal Lead (<div.elementor> — `Where luxury meets serenity`)**:
   - Landmark `<div class="elementor elementor-385">` presenting display lead `Where luxury meets serenity` and copy excerpt *"Contact us today to clear any questions, get more information and"* over `#ffffff` canvas and `#1e1e1e` ink.
3. **Primary Showcase & Content Grid (<div.elementor-385> — `Contact us today to clear any ques`)**:
   - Landmark `<div class="elementor elementor-385">` rendering section `Contact us today to clear any questions, get mor` with copy *"Quinta D. Amália is more than a residence - it’s a lifestyle defi"*, asset references (`ff19e2716e4af741afc51614093bc.css`, `8vIH7w4qzmVxm2BL9A.woff2`, `marcellus-weo_ebrok8hqldviaf81vvo...`, `css2`), and grid rule `.themepure-theme-btn span { display:inline-block }`.
4. **Interactive Detail & Feature Matrix (<div.elementor:nth(2)> — `Quinta D. Amália is more than a re`)**:
   - Landmark `<div class="elementor elementor-385">` framing `Quinta D. Amália is more than a residence - it’s` and `Every residence is a masterpiece of craftsmanshi` (*"Every residence is a masterpiece of craftsmanship, featuring prem"*) with `#f5f7f5` surface cards, `#007fff` accents, and `.themepure-theme-btn img { object-fit:cover }`.
5. **Colophon & Global Directory Footer (<footer.home> — `https://www.quintadamalia.com/`)**:
   - Landmark `<footer class="home">` anchoring `Quinta D. Amália - Redefining Lu` footer links (`Home · About · Apartments · Lifestyle · Contact`), copy *"With construction beginning in Q4 2026, Quinta D. Amália is "*, and `#9ec5fe` structural dividers.
