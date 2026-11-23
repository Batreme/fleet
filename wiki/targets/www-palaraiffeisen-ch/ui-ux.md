---
title: "UI & UX Architecture: www-palaraiffeisen-ch"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: www-palaraiffeisen-ch

## Overview & Design Identity
- **Target**: `www-palaraiffeisen-ch` (**Il palazzetto dello sport di Lugano — Palaraiffeisen**)
- **Production URL**: [https://www.palaraiffeisen.ch](https://www.palaraiffeisen.ch)
- **Final Redirected URL**: [https://palaraiffeisen.ch/](https://palaraiffeisen.ch/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#e52528`)
- **Summary**: Il PalaRaiffeisen, il nuovo palazzetto dello sport di Lugano. Eventi, competizioni e attività per tutti.
- **Total Clean CSS Variables Extracted**: `323` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `APK Systema Regular`
- **Body Font Stack**: `APK-Narrative-Regular`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 56px`, `line-height: 56px`, `font-weight: 400`, `letter-spacing: -0.84px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f0f0f0` | `.page-home-3d { background-color: #f0f0f0 }` |
| **Interactive Accent / Highlight** | `#e52528` | `var(--c-primary-300)` in `:root` |
| **Secondary / Muted Copy** | `#000000` | secondary opacity step of live computed `h1` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#000000` | `.app-elements-list li { border: #000000 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--c-black` | `#000` | Canvas / Surface Token |
| `--c-black-0` | `transparent` | Canvas / Surface Token |
| `--c-black-10` | `rgba(0,0,0,.1)` | Canvas / Surface Token |
| `--c-black-20` | `rgba(0,0,0,.2)` | Canvas / Surface Token |
| `--c-black-30` | `rgba(0,0,0,.3)` | Canvas / Surface Token |
| `--c-black-40` | `rgba(0,0,0,.4)` | Canvas / Surface Token |
| `--c-black-50` | `rgba(0,0,0,.5)` | Canvas / Surface Token |
| `--c-black-60` | `rgba(0,0,0,.6)` | Canvas / Surface Token |
| `--c-black-70` | `rgba(0,0,0,.7)` | Canvas / Surface Token |
| `--c-black-80` | `rgba(0,0,0,.8)` | Canvas / Surface Token |
| `--c-black-90` | `rgba(0,0,0,.9)` | Canvas / Surface Token |
| `--c-black-100` | `#000` | Canvas / Surface Token |
| `--c-white` | `#fff` | Canvas / Surface Token |
| `--c-white-0` | `hsla(0,0%,100%,0)` | Canvas / Surface Token |
| `--c-white-10` | `hsla(0,0%,100%,.1)` | Canvas / Surface Token |
| `--c-white-20` | `hsla(0,0%,100%,.2)` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `www-palaraiffeisen-ch`)**:
   - Landmark `<header class="lenis">` (`1440px`) hosting `Il palazzetto dello sport di Lugano ` navigation (`Il Palazzetto · Le società residenti · Organizza un evento · News · Scopri di più`), DOM attributes (`data-infer`, `data-cookiescriptreport="report"`, `data-tres="tresjs 5.8.1"`, `data-engine="three.js r180"`), and stylesheet rule `.P2.no-selectable { -webkit-user-select:none;-moz-user-select:none;user-select:none }`.
2. **Hero Stage & Focal Lead (<section.page-home-hero> — `BENVENUTI AL PALARAIFFEISEN BENVEN`)**:
   - Landmark `<section class="page-home-hero">` presenting display lead `BENVENUTI AL PALARAIFFEISEN BENVENUTI AL PALARAIF...` and copy excerpt *"La nuova casa dello sport e degli eventi a Lugano."* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.page-home-3d> — `B E N V E N U T I A L P A L A R A `)**:
   - Landmark `<section class="page-home-3d">` rendering section `B E N V E N U T I A L P A L A R A I F F E I S E N...` with copy *"INAUGURAZIONE SETTEMBRE 2027 INAUGURAZIONE SETTEMBRE 2027"*, asset references (`kirby.palaraiffeisen.ch`, `entry.DiBOf5nH.css`, `Writer.C_JpA5xq.css`, `Media.C_3wTCR8.css`), and grid rule `.app-elements-list { display:flex;flex-direction:column;list-style:none;padding:0;margin:0 }`.
4. **Interactive Detail & Feature Matrix (<section.page-banner-fullscreen> — `Un nuovo quartiere per Lugano Un n`)**:
   - Landmark `<section class="page-banner-fullscreen">` framing `Un nuovo quartiere per Lugano Un nuovo quartiere...` and `u n a n u o v a d e s t i n a z i o n e p e r e v...` (*"INAUGURAZIONE SETTEMBRE 2027"*) with `#f0f0f0` surface cards, `#e52528` accents, and `.app-elements-list li { border:1px solid var(--c-black);margin-top:-1px;padding:.2777777778vw;di... }`.
5. **Colophon & Global Directory Footer (<footer.app-footer> — `https://www.palaraiffeisen.ch`)**:
   - Landmark `<footer class="app-footer block-inner">` anchoring `Il palazzetto dello sport di Lug` footer links (`Il Palazzetto · Le società residenti · Organizza un evento · News · Scopri di più`), copy *"B E N V E N U T I A L P A L A R A I F F E I S E N"*, and `#000000` structural dividers.
