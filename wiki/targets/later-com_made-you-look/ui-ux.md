---
title: "UI & UX Architecture: later-com_made-you-look"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: later-com_made-you-look

## Overview & Design Identity
- **Target**: `later-com_made-you-look` (**Made You Look: Campaigns so good you break the algorithm.**)
- **Production URL**: [https://later.com/made-you-look/](https://later.com/made-you-look/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f8f2ea` canvas, `#000000` ink, `#0057ff` accent)
- **Summary**: Meet the creators shaping culture through bold ideas and obsessive craft—and see how brands partner with them to build standout influence...
- **Total Clean CSS Variables Extracted**: `823` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Super X sans Display`
- **Body Font Stack**: `Inter Tight`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--h1-2xl: 3.5rem`, `--h1-xl: 3.125rem`, `--h1-l: 2.5rem`; rule `h1` (`font-size: 5rem`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 144px`, `line-height: 136.8px`, `font-weight: 800`, `letter-spacing: 0.72px`); CSS variables `--h2: 2.125rem`, `--h2-s: 1.875rem`, `--text-2xl: 1.25rem`; rule `h2` (`font-size: 13px`, `line-height: 15px`, `font-weight: 500`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 20px`, `font-weight: 400`); CSS variables `--font-body: Inter Tight,Helvetica Neue,Helvetica,Arial,sans-serif`, `--body-line-height: 1.5`, `--body-letter-spacing: 0.01em`; rule `p` (`line-height: 18px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 20px`, `font-weight: 400`); CSS variables `--text-xs: 0.875rem`, `--heading-letter-spacing: 0.005em`, `--body-letter-spacing: 0.01em`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f8f2ea` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f3f4f5` | `var(--grey-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#0057ff` | `var(--highlight-purple)` in `:root` |
| **Secondary / Muted Copy** | `#239dff` | `var(--purple-secondary)` in `:root` |
| **Structural Hairline Border** | `#a075ff` | `var(--outline-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--delay` | `0ms` | Motion / Easing Token |
| `--scrollbar-width` | `0px` | Layout / Spatial Grid Token |
| `--outline-width` | `0.25rem` | Layout / Spatial Grid Token |
| `--outline-color` | `#a075ff` | Brand / Palette Token |
| `--outline-offset` | `0.375rem` | Elevation / Border Token |
| `--0-5` | `0.25rem` | Dimension / Scale Token |
| `--1-5` | `0.75rem` | Dimension / Scale Token |
| `--2-5` | `1.25rem` | Dimension / Scale Token |
| `--3-5` | `1.75rem` | Dimension / Scale Token |
| `--10` | `5rem` | Dimension / Scale Token |
| `--11` | `5.5rem` | Dimension / Scale Token |
| `--12` | `6rem` | Dimension / Scale Token |
| `--13` | `6.5rem` | Dimension / Scale Token |
| `--14` | `7rem` | Dimension / Scale Token |
| `--15` | `7.5rem` | Dimension / Scale Token |
| `--20` | `10rem` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `later-com_made-you-look`)**:
   - Landmark `<header class="lenis">` (`1440px`) hosting `Made You Look: Campaigns so good you` navigation (`halo perez-gallardo · Timothy Goodman · Jeremy Jankowski · Megna Paula · Julian McCleary`), DOM attributes (`data-root="true"`, `data-gatsby-head="true"`, `data-gatsby-head="true"`, `data-gatsby-head="true"`), and stylesheet rule `.html5-video-player.ytp-fullscree... { -webkit-transition:opacity .25s cubic-bezier(0,0,.2,1);transition:opacit... }`.
2. **Hero Stage & Focal Lead (<section.NnFvv> — `Campaigns so good you break the al`)**:
   - Landmark `<section class="NnFvv">` presenting display lead `Campaigns so good you break the algorithm.` and copy excerpt *"That’s what happens when brands stop chasing trends and start wor"* over `#f8f2ea` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.NnFvv:nth(2)> — `Made you look`)**:
   - Landmark `<section class="NnFvv">` rendering section `Made you look` with copy *"At Later, we help brands partner with those creators—bringing tog"*, asset references (`InterTight-VariableFont_wght.woff2`, `superx-extrabold.woff2`, `superx-semibold.woff2`, `rss.xml`), and grid rule `.ytp-contextmenu { -ms-high-contrast-adjust:none;forced-color-adjust:none }`.
4. **Interactive Detail & Feature Matrix (<section.NnFvv:nth(3)> — `halo perez-gallardo`)**:
   - Landmark `<section class="NnFvv">` framing `halo perez-gallardo` and `Timothy Goodman` (*"Because breakthrough campaigns aren’t louder. They’re more credib"*) with `#f3f4f5` surface cards, `#0057ff` accents, and `.ytp-big-mode { font-size:17px }`.
5. **Colophon & Global Directory Footer (<footer.vWCKd> — `https://later.com/made-you-look/`)**:
   - Landmark `<footer class="vWCKd">` anchoring `Made You Look: Campaigns so good` footer links (`halo perez-gallardo · Timothy Goodman · Jeremy Jankowski · Megna Paula · Julian McCleary`), copy *"Learn more about Later's services"*, and `#a075ff` structural dividers.
