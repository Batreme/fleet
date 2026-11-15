# UI & UX Architecture: www-palaraiffeisen-ch

## Overview & Design Identity
- **Target**: `www-palaraiffeisen-ch` (**Il palazzetto dello sport di Lugano — Palaraiffeisen**)
- **Production URL**: [https://www.palaraiffeisen.ch](https://www.palaraiffeisen.ch)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#e7d3d3`)
- **Summary**: Il PalaRaiffeisen, il nuovo palazzetto dello sport di Lugano. Eventi, competizioni e attività per tutti.
- **Total Clean CSS Variables Extracted**: `323` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `APK Systema Regular`
- **Body Font Stack**: `APK-Narrative-Regular`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `3.7333333333vw`, `1.25vw`, `4.2666666667vw`, `1.1111111111vw`, `6.6666666667vw`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `3.7333333333vw`, `1.25vw`, `4.2666666667vw`, `1.1111111111vw`, `6.6666666667vw`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `3.7333333333vw`, `1.25vw`, `4.2666666667vw`, `1.1111111111vw`, `6.6666666667vw`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `3.7333333333vw`, `1.25vw`, `4.2666666667vw`, `1.1111111111vw`, `6.6666666667vw`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--c-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--c-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fb2c36` | `var(--c-red)` in `:root` |
| **Interactive Accent / Highlight** | `#e7d3d3` | `var(--c-light-1)` in `:root` |
| **Secondary / Muted Copy** | `#eee` | `var(--c-light-2)` in `:root` |
| **Structural Hairline Border** | `#023911` | `var(--c-green-dark)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--scaleX` | `0` | Design System Custom Token |
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

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `www-palaraiffeisen-ch`)**:
   - Landmark `<header class="lenis">` hosting `Il palazzetto dello sport di Lugano ` navigation (`Il Palazzetto · Le società residenti · Organizza un evento · News · Scopri di più`), DOM attributes (`data-infer`, `data-cookiescriptreport="report"`, `data-tres="tresjs 5.8.1"`, `data-engine="three.js r180"`), and stylesheet rule `.svg-icon-close svg { display:block;width:100%;height:100% }`.
2. **Hero Stage & Focal Lead (<section.page-home-hero> — `B E N V E N U T I A L P A L A R A `)**:
   - Landmark `<section class="page-home-hero">` presenting display lead `B E N V E N U T I A L P A L A R A I F F E I S E N...` and copy excerpt *"Le società residenti"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.page-home-3d> — `Un nuovo quartiere per Lugano Un n`)**:
   - Landmark `<section class="page-home-3d">` rendering section `Un nuovo quartiere per Lugano Un nuovo quartiere...` with copy *"Organizza un evento"*, asset references (`kirby.palaraiffeisen.ch`, `entry.DiBOf5nH.css`, `Writer.C_JpA5xq.css`, `Media.C_3wTCR8.css`), and grid rule `.app-webgl-front-card { gap:2.1333333333vw;padding:4.2666666667vw }`.
4. **Interactive Detail & Feature Matrix (<section.page-banner-fullscreen> — `u n a n u o v a d e s t i n a z i `)**:
   - Landmark `<section class="page-banner-fullscreen">` framing `u n a n u o v a d e s t i n a z i o n e p e r e v...` and `PALARAIFFEISEN PALARAIFFEISEN` (*"INAUGURAZIONE SETTEMBRE 2027 INAUGURAZIONE SETTEMBRE 2027"*) with `#fb2c36` surface cards, `#e7d3d3` accents, and `.app-webgl-front-card__close { position:absolute;top:.5555555556vw;right:.5555555556vw;width:1.38888888... }`.
5. **Colophon & Global Directory Footer (<footer.app-footer> — `https://www.palaraiffeisen.ch`)**:
   - Landmark `<footer class="app-footer block-inner">` anchoring `Il palazzetto dello sport di Lug` footer links (`Il Palazzetto · Le società residenti · Organizza un evento · News · Scopri di più`), copy *"INAUGURAZIONE SETTEMBRE 2027"*, and `#023911` structural dividers.
