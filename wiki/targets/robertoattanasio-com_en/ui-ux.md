---
title: "UI & UX Architecture: robertoattanasio-com_en"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: robertoattanasio-com_en

## Overview & Design Identity
- **Target**: `robertoattanasio-com_en` (**Roberto Attanasio**)
- **Production URL**: [https://robertoattanasio.com/en](https://robertoattanasio.com/en)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×872px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#080808` / `#9c0ea3`)
- **Summary**: I write code by day and words by night. Projects, music and poems, all hidden in my digital world: drag the field and find them.
- **Total Clean CSS Variables Extracted**: `65` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Mononoki`
- **Body Font Stack**: `Mononoki`
- **Monospace / Technical Font Stack**: `Mononoki`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 14px`, `line-height: 22.75px`, `font-weight: 400`, `letter-spacing: 1.4px`)
- **Section Heading (`H2`)**: observed font-size ladder: `14px`, `16px`, `12px`, `10px`, `1em`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`; rule `,body` (`line-height: 1.5`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 10px`, `line-height: 15px`, `font-weight: 400`, `letter-spacing: 1px`); CSS variables `--text-xs: .75rem`, `--text-sm: .875rem`, `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#080808` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f3f3f3` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#080808` | transparent/inherited card surface over live computed `body` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#9c0ea3` | `var(--margo-color-primary)` in `:root` |
| **Secondary / Muted Copy** | `#f5cb77` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#cecece` | `var(--margo-color-border)` in `:root` |
| **Variable Token (`--margo-color-neutral`)** | `#ffffff` | `var(--margo-color-neutral)` in `:root` |
| **Variable Token (`--margo-color-on-neutral`)** | `#000000` | `var(--margo-color-on-neutral)` in `:root` |
| **Variable Token (`--margo-color-main`)** | `#eceaea` | `var(--margo-color-main)` in `:root` |
| **Variable Token (`--margo-color-on-main`)** | `#222222` | `var(--margo-color-on-main)` in `:root` |
| **Variable Token (`--margo-color-primary-darken`)** | `#7d0b82` | `var(--margo-color-primary-darken)` in `:root` |
| **Variable Token (`--margo-color-medium`)** | `#787878` | `var(--margo-color-medium)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--margo-radius` | `.5rem` | Elevation / Border Token |
| `--margo-radius-sm` | `calc(var(--margo-radius) * 3 / 4)` | Elevation / Border Token |
| `--margo-radius-xs` | `calc(var(--margo-radius) / 2)` | Elevation / Border Token |
| `--margo-radius-mc` | `calc(var(--margo-radius) / 4)` | Elevation / Border Token |
| `--margo-border` | `2px` | Elevation / Border Token |
| `--lightningcss-light` | `initial` | Canvas / Surface Token |
| `--margo-color-neutral` | `#fff` | Brand / Palette Token |
| `--margo-color-on-neutral` | `#000` | Brand / Palette Token |
| `--margo-color-main` | `#eceaea` | Brand / Palette Token |
| `--margo-color-on-main` | `#222` | Brand / Palette Token |
| `--margo-color-primary` | `#9c0ea3` | Brand / Palette Token |
| `--margo-color-primary-darken` | `#7d0b82` | Canvas / Surface Token |
| `--margo-color-low` | `var(--margo-color-on-main)` | Brand / Palette Token |
| `--margo-color-low-alpha` | `var(--margo-color-on-main)` | Brand / Palette Token |
| `--margo-color-medium` | `#787878` | Brand / Palette Token |
| `--margo-color-border` | `#cecece` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.inset-x-0> — `robertoattanasio-com_en`)**:
   - Landmark `<header class="inset-x-0 top-6">` (`1440x15px`) hosting `Roberto Attanasio` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="default"`, `data-root="true"`, `data-cursor="expand"`, `data-cursor-silent="true"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.sr-only> — `ROBERTO ATTANASIO`)**:
   - Landmark `<section class="sr-only">` presenting display lead `ROBERTO ATTANASIO` and copy excerpt *"Hi, I'm a Frontend Web Developer with five years of experience."* over `#080808` canvas and `#f3f3f3` ink.
3. **Primary Showcase & Content Grid (<article.box-content> — `Roberto Attanasio`)**:
   - Landmark `<article class="box-content py-5">` rendering section `Roberto Attanasio` with copy *"poetry poetry poetry"*, asset references (`index-G4udTFpP.css`, `index-DUR-Fu7l.js`, `graft-DQAKSCm4.js`, `route-BfXHpA5q.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<article.py-5> — `poetry poetry poetry`)**:
   - Landmark `<article class="box-content py-5">` framing `poetry poetry poetry` and `I write code by day and words by night. In betwe` (*"I write code by day and words by night. In between there's the pi"*) with `#080808` surface cards, `#9c0ea3` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.flex> — `https://robertoattanasio.com/en`)**:
   - Landmark `<footer class="flex">` anchoring `Roberto Attanasio` footer links (`Overview · Index · Archive · About · Contact`), copy *"r.attanasio90@gmail.com r.attanasio90@gmail.com KV12·3N+T7VX"*, and `#cecece` structural dividers.
