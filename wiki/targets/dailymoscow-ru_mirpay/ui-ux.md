# UI & UX Architecture: dailymoscow-ru_mirpay

## Overview & Design Identity
- **Target**: `dailymoscow-ru_mirpay` (**Спорт без лишних действий — Mir Pay × Daily Moscow**)
- **Production URL**: [https://dailymoscow.ru/mirpay](https://dailymoscow.ru/mirpay)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#7b7b81` accent)
- **Summary**: Бокс, гольф, бассейн, падел, скалодром и йога — и ни одного лишнего движения, когда дело доходит до оплаты
- **Total Clean CSS Variables Extracted**: `22` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Manrope`
- **Body Font Stack**: `Lora`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `20px`, `6px`, `14px`, `10px`, `12px`)
- **Section Heading (`H2`)**: rule `.section-title` (`font-weight: 800`)
- **Body Copy**: rule `p` (`font-size: 14px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `20px`, `6px`, `14px`, `10px`, `12px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--dmf-bg)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--dmf-ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#9d9da4` | `var(--dmf-muted)` in `:root` |
| **Interactive Accent / Highlight** | `#7b7b81` | `var(--dmf-dim)` in `:root` |
| **Secondary / Muted Copy** | `#1f5bd7` | `var(--blue)` in `:root` |
| **Structural Hairline Border** | `#00aaff` | `var(--sky)` in `:root` |
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
   - Landmark `<header class="header header-news">` hosting `Спорт без лишних действий — Mir Pay ` navigation (`Бокс · Гольф · Бассейн · Падел · Скалодром`), DOM attributes (`data-pd="26"`, `data-mx="-.4"`, `data-sp=".5"`, `data-pd="-40"`), and stylesheet rule `body.body-dark .category-main { border-color:1f1f1f }`.
2. **Hero Stage & Focal Lead (<section.main> — `Спорт без лишних действий`)**:
   - Landmark `<section class="main m3">` presenting display lead `Спорт без лишних действий` and copy excerpt *"Бокс, гольф, бассейн, падел, скалодром и йога — и ни одного лишне"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<article.m3-body> — `Начинала я с бокса`)**:
   - Landmark `<article class="m3-body">` rendering section `Начинала я с бокса` with copy *"ЕК Елена Карнеева редактор Daily Moscow"*, asset references (`tag.js`, `mirpay`, `footer-v2.css`, `components.css`), and grid rule `body.body-dark .category-main__name { color:fff }`.
4. **Interactive Detail & Feature Matrix (<section.m3-sec> — `Потом был гольф`)**:
   - Landmark `<section class="m3-sec">` framing `Потом был гольф` and `Дальше была вода, то есть аквакомплекс` (*"Елена Карнеева редактор Daily Moscow"*) with `#9d9da4` surface cards, `#7b7b81` accents, and `body.body-dark .category-quote__s... { color:7b7b81 }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://dailymoscow.ru/mirpay`)**:
   - Landmark `<footer class="footer dm-footer">` anchoring `Спорт без лишних действий — Mir ` footer links (`Бокс · Гольф · Бассейн · Падел · Скалодром`), copy *"редактор Daily Moscow"*, and `#00aaff` structural dividers.
