---
title: "UI & UX Architecture: henwoodcourt-co-uk"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: henwoodcourt-co-uk

## Overview & Design Identity
- **Target**: `henwoodcourt-co-uk` (**Henwood Court · Where financial freedom meets fulfilment**)
- **Production URL**: [https://henwoodcourt.co.uk](https://henwoodcourt.co.uk)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fffbed` canvas, `#48265f` ink, `#383737` accent)
- **Summary**: You work hard for your money. At Henwood Court we work hard to turn your wealth into a life you love.
- **Total Clean CSS Variables Extracted**: `61` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Moulin Trial`
- **Body Font Stack**: `Euclid Circular B`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 60px`, `line-height: 72px`, `font-weight: 300`); CSS variables `--font-display: "Moulin Trial", Georgia, "Times New Roman", serif`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 60px`, `line-height: 72px`, `font-weight: 300`)
- **Body Copy**: live computed `body` (`font-size: 17px`, `line-height: 25.5px`, `font-weight: 400`); CSS variables `--font-body: "Euclid Circular B", Arial, Helvetica, sans-serif`, `--text-body-small: 14px`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 17px`, `line-height: 25.5px`, `font-weight: 400`); CSS variables `--default-mono-font-family: var(--font-mono)`, `--text-body-small: 14px`, `--text-label: 14px`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fffbed` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#48265f` | live computed `h2` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `select { background-color: #ffffff }` |
| **Interactive Accent / Highlight** | `#383737` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#7b7283` | `var(--color-muted-purple)` in `:root` |
| **Structural Hairline Border** | `#6a7282` | `select { border-color: #6a7282 }` |
| **Variable Token (`--color-black`)** | `#000000` | `var(--color-black)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `var(--font-body)` | Typography / Scale Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-sm` | `24rem` | Layout / Spatial Grid Token |
| `--container-md` | `28rem` | Layout / Spatial Grid Token |
| `--container-lg` | `32rem` | Layout / Spatial Grid Token |
| `--container-xl` | `36rem` | Layout / Spatial Grid Token |
| `--container-2xl` | `42rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |
| `--container-4xl` | `56rem` | Layout / Spatial Grid Token |
| `--container-5xl` | `64rem` | Layout / Spatial Grid Token |
| `--container-6xl` | `72rem` | Layout / Spatial Grid Token |
| `--font-weight-light` | `300` | Canvas / Surface Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.top-0> — `henwoodcourt-co-uk`)**:
   - Landmark `<header class="top-0 inset-x-0">` (`1440x72px`) hosting `Henwood Court · Where financial free` navigation (`Manage your money · Plan your retirement · Our approach · Investment strategy · FAQs`), DOM attributes (`data-theme-url="https://henwoodcourt...."`, `data-ajax-url="https://henwoodcourt...."`, `data-ratio="xMidYMid meet"`, `data-path="https://henwoodcourt...."`), and stylesheet rule `.dashicons-admin-appearance:before { content:"\f100" }`.
2. **Hero Stage & Focal Lead (<article.shadow-card> — `Where financial freedom meets fulf`)**:
   - Landmark `<article class="shadow-card p-5">` presenting display lead `Where financial freedom meets fulfilment` and copy excerpt *"You work hard for your money. At Henwood Court we work hard to tu"* over `#fffbed` canvas and `#48265f` ink.
3. **Primary Showcase & Content Grid (<article.p-5> — `Helping you live a rich life, not `)**:
   - Landmark `<article class="shadow-card p-5">` rendering section `Helping you live a rich life, not just a wealthy one` with copy *"Great financial planning can change your life."*, asset references (`euclid-circular-b-regular.woff2`, `euclid-circular-b-medium.woff2`, `moulin-light.woff2`, `player.vimeo.com`), and grid rule `.dashicons-admin-collapse:before { content:"\f148" }`.
4. **Interactive Detail & Feature Matrix (<article.bg-white> — `I’m a business owner`)**:
   - Landmark `<article class="shadow-card p-5">` framing `I’m a business owner` and `I’m looking to invest` (*"As award-winning chartered financial planners, we don’t just advi"*) with `#ffffff` surface cards, `#383737` accents, and `.dashicons-admin-comments:before { content:"\f101" }`.
5. **Colophon & Global Directory Footer (<footer.bg-linear-to-b> — `https://henwoodcourt.co.uk`)**:
   - Landmark `<footer class="bg-linear-to-b from-med-purple">` anchoring `Henwood Court · Where financial ` footer links (`Manage your money · Plan your retirement · Our approach · Investment strategy · FAQs`), copy *"We know what it’s like to work so hard on your business that"*, and `#6a7282` structural dividers.
