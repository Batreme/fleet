---
title: "UI & UX Architecture: dailymoscow-ru_mirpay"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: dailymoscow-ru_mirpay

## Overview & Design Identity
- **Target**: `dailymoscow-ru_mirpay` (**Спорт без лишних действий — Mir Pay × Daily Moscow**)
- **Production URL**: [https://dailymoscow.ru/mirpay](https://dailymoscow.ru/mirpay)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f4f7fc` canvas, `#000000` ink, `#007bff` accent)
- **Summary**: Бокс, гольф, бассейн, падел, скалодром и йога — и ни одного лишнего движения, когда дело доходит до оплаты
- **Total Clean CSS Variables Extracted**: `22` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `MP Graphik`
- **Body Font Stack**: `Manrope`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 103.68px`, `line-height: 101.606px`, `font-weight: 700`, `letter-spacing: -3.1104px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 67.68px`, `line-height: 67.68px`, `font-weight: 700`, `letter-spacing: -2.7072px`); rule `.section-title` (`font-weight: 800`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 20.8px`, `font-weight: 400`); rule `p` (`font-size: 14px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 20.8px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f4f7fc` | live computed `section` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `.main-btn.active { background: #ffffff }` |
| **Interactive Accent / Highlight** | `#007bff` | `.privacy-consent__link { color: #007bff }` |
| **Secondary / Muted Copy** | `#9d9da4` | `var(--dmf-muted)` in `:root` |
| **Structural Hairline Border** | `#f6f8fc` | `var(--dmf-rule)` in `:root` (`rgba(255, 255, 255, .14)`) |
| **Variable Token (`--dmf-dim`)** | `#7b7b81` | `var(--dmf-dim)` in `:root` |
| **Variable Token (`--blue`)** | `#1f5bd7` | `var(--blue)` in `:root` |
| **Variable Token (`--sky`)** | `#00aaff` | `var(--sky)` in `:root` |
| **Variable Token (`--green`)** | `#00a263` | `var(--green)` in `:root` |
| **Variable Token (`--green-t`)** | `#008452` | `var(--green-t)` in `:root` |
| **Variable Token (`--green-d`)** | `#0b4d31` | `var(--green-d)` in `:root` |
| **Variable Token (`--ink`)** | `#0f1530` | `var(--ink)` in `:root` |
| **Variable Token (`--text`)** | `#2a3150` | `var(--text)` in `:root` |
| **Variable Token (`--mute`)** | `#5d6683` | `var(--mute)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--dmf-bg` | `#000` | Canvas / Surface Token |
| `--dmf-ink` | `#fff` | Typography Ink Token |
| `--dmf-muted` | `#9d9da4` | Color / Atmospheric Token |
| `--dmf-dim` | `#7b7b81` | Color / Atmospheric Token |
| `--dmf-rule` | `rgba(255, 255, 255, .14)` | Color / Atmospheric Token |
| `--dmf-surface` | `rgba(255, 255, 255, .05)` | Canvas / Surface Token |
| `--dmf-gap` | `32px` | Layout / Spatial Grid Token |
| `--dmf-rail` | `340px` | Dimension / Scale Token |
| `--blue` | `#1f5bd7` | Color / Atmospheric Token |
| `--sky` | `#00aaff` | Color / Atmospheric Token |
| `--green` | `#00a263` | Color / Atmospheric Token |
| `--green-t` | `#008452` | Color / Atmospheric Token |
| `--green-d` | `#0b4d31` | Color / Atmospheric Token |
| `--ink` | `#0f1530` | Typography Ink Token |
| `--text` | `#2a3150` | Typography Ink Token |
| `--mute` | `#5d6683` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `dailymoscow-ru_mirpay`)**:
   - Landmark `<header class="header header-news">` (`1440x120px`) hosting `Спорт без лишних действий — Mir Pay ` navigation (`Бокс · Гольф · Бассейн · Падел · Скалодром`), DOM attributes (`data-pd="26"`, `data-mx="-.4"`, `data-sp=".5"`, `data-pd="-40"`), and stylesheet rule `.dm-footer__wrapper { max-width: 1280px; margin: 0 auto; padding: 0 16px; }`.
2. **Hero Stage & Focal Lead (<article.m3-body> — `СПОРТ БЕЗ ЛИШНИХ ДЕЙСТВИЙ`)**:
   - Landmark `<article class="m3-body">` presenting display lead `СПОРТ БЕЗ ЛИШНИХ ДЕЙСТВИЙ` and copy excerpt *"Бокс, гольф, бассейн, падел, скалодром и йога — и ни одного лишне"* over `#f4f7fc` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.m3-sec> — `Спорт без лишних действий`)**:
   - Landmark `<section class="m3-sec">` rendering section `Спорт без лишних действий` with copy *"Елена Карнеева редактор Daily Moscow"*, asset references (`tag.js`, `mirpay`, `footer-v2.css`, `components.css`), and grid rule `.dm-footer__logo { display: block; line-height: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.m3-sec:nth(2)> — `Начинала я с бокса`)**:
   - Landmark `<section class="m3-sec">` framing `Начинала я с бокса` and `Потом был гольф` (*"редактор Daily Moscow"*) with `#ffffff` surface cards, `#007bff` accents, and `.dm-footer__logo img { width: 220px; height: auto; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://dailymoscow.ru/mirpay`)**:
   - Landmark `<footer class="footer dm-footer">` anchoring `Спорт без лишних действий — Mir ` footer links (`Бокс · Гольф · Бассейн · Падел · Скалодром`), copy *"Я не спортсменка. Я женщина, которая время от времени вспоми"*, and `#f6f8fc` structural dividers.
