---
title: "UI & UX Architecture: cobaltaf-org"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: cobaltaf-org

## Overview & Design Identity
- **Target**: `cobaltaf-org` (**Cobalt Abortion Fund**)
- **Production URL**: [https://cobaltaf.org/](https://cobaltaf.org/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#0000ff` accent)
- **Summary**: Read privacy and digital security tips here →
- **Total Clean CSS Variables Extracted**: `249` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `bookmania`
- **Body Font Stack**: `Poppins`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 95.368px`, `line-height: 100.136px`, `font-weight: 400`); rule `,h1` (`font-size: clamp(2.5658rem,1.4795rem + 5...`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 61.0352px`, `line-height: 64.087px`, `font-weight: 500`); rule `,h2` (`font-size: clamp(2.0273rem,1.4553rem + 2...`, `font-weight: 500`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 19.2px`, `font-weight: 400`); rule `p` (`font-size: var(--form-desc-size)`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 19.2px`, `font-weight: 400`); CSS variables `--container-small: 76rem`, `--label-padding: 0px 0px 5px 0px`; rule `,small` (`font-size: clamp(.8rem,.9173rem + -.1422...`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#dddddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Interactive Accent / Highlight** | `#0000ff` | `#sb_instagram .sbi_follow_btn a { background: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#468847` | `var(--success-text-color)` in `:root` |
| **Structural Hairline Border** | `#dcdee2` | `var(--ss-border-color)` in `:root` |
| **Variable Token (`--ss-primary-color`)** | `#5897fb` | `var(--ss-primary-color)` in `:root` |
| **Variable Token (`--ss-font-color`)** | `#4d4d4d` | `var(--ss-font-color)` in `:root` |
| **Variable Token (`--ss-font-placeholder-color`)** | `#8d8d8d` | `var(--ss-font-placeholder-color)` in `:root` |
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
1. **Brand Header & Navigation Bar (<header.header> — `cobaltaf-org`)**:
   - Landmark `<header class="header js-header">` (`1440x89px`) hosting `Cobalt Abortion Fund` navigation (`Support · Services · Find A Clinic · Resources · Necesito Apoyo`), DOM attributes (`data-acsb-sr-alert="true"`, `data-acsb-sr-only="true"`, `data-acsb-force-visible="true"`, `data-acsb`), and stylesheet rule `.with_frm_style .frm_button.frm_h... { display:none; }`.
2. **Hero Stage & Focal Lead (<section.section> — `Abortion Seekers`)**:
   - Landmark `<section class="section section-1">` presenting display lead `Abortion Seekers` and copy excerpt *"Read privacy and digital security tips here →"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.section-2> — `Cobalt Abortion Fund provides dire`)**:
   - Landmark `<section class="section section-2">` rendering section `Cobalt Abortion Fund provides direct financial as...` with copy *"Cobalt Abortion Fund provides direct financial assistance for abo"*, asset references (`analytics.js`, `gtm.js`, `static.addtoany.com`, `maps.googleapis.com`), and grid rule `le .frm-show-form div.frm_descrip... { text-align: var(--form-align); }`.
4. **Interactive Detail & Feature Matrix (<section.section-3> — `Whatever your reason is for gettin`)**:
   - Landmark `<section class="section section-3">` framing `Whatever your reason is for getting an abortion,...` and `Our Services` (*"We exist to support anyone seeking abortion care at one of the cl"*) with `#dddddd` surface cards, `#0000ff` accents, and `input:-webkit-autofill { -webkit-box-shadow: 0 0 0 30px white inset; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://cobaltaf.org/`)**:
   - Landmark `<footer class="footer">` anchoring `Cobalt Abortion Fund` footer links (`Support · Services · Find A Clinic · Resources · Necesito Apoyo`), copy *"We know there are many barriers people face while trying to "*, and `#dcdee2` structural dividers.
