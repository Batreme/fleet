---
title: "UI & UX Architecture: www-mynobs-co"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-mynobs-co

## Overview & Design Identity
- **Target**: `www-mynobs-co` (**NoBS - No Brief Shit**)
- **Production URL**: [https://www.mynobs.co](https://www.mynobs.co)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×1820px`, Mobile `390×1492px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fcfaf7` canvas, `#0a0a0a` ink, `#ff0066` accent)
- **Summary**: 💩 It's simple: drop in the buzzword-stuffed brief, and NoBS cuts the BS, handing back only what you need to know to start your job.
- **Total Clean CSS Variables Extracted**: `25` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Sugra`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 150px`, `line-height: 138px`, `font-weight: 400`, `letter-spacing: 5px`); rule `.hero-title` (`font-size: 150px`, `line-height: 0.92`, `letter-spacing: 5px`, `font-weight: normal`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 40px`, `line-height: 40px`, `font-weight: 700`, `letter-spacing: 1px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--fs-body: 18px`, `--lh-body: 1.55`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fcfaf7` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0a0a0a` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffd9ee` | `body.is-demo .nbs-topbar { background: #ffd9ee }` |
| **Interactive Accent / Highlight** | `#ff0066` | `.nbs-footer-link:hover { color: #ff0066 }` |
| **Secondary / Muted Copy** | `#ec4899` | `var(--pink)` in `:root` |
| **Structural Hairline Border** | `#a7a6a4` | `.nbs-account-row { border-bottom: #a7a6a4 }` |
| **Variable Token (`--purple`)** | `#7e5af2` | `var(--purple)` in `:root` |
| **Variable Token (`--purple-deep`)** | `#5b3bc4` | `var(--purple-deep)` in `:root` |
| **Variable Token (`--purple-dark`)** | `#2d1b69` | `var(--purple-dark)` in `:root` |
| **Variable Token (`--yellow`)** | `#facc15` | `var(--yellow)` in `:root` |
| **Variable Token (`--yellow-deep`)** | `#c2a011` | `var(--yellow-deep)` in `:root` |
| **Variable Token (`--peach-deep`)** | `#c2691a` | `var(--peach-deep)` in `:root` |
| **Variable Token (`--pink-deep`)** | `#b8276f` | `var(--pink-deep)` in `:root` |
| **Variable Token (`--peach`)** | `#fb923c` | `var(--peach)` in `:root` |
| **Variable Token (`--lime`)** | `#84cc16` | `var(--lime)` in `:root` |
| **Variable Token (`--sky`)** | `#0ea5e9` | `var(--sky)` in `:root` |
| **Variable Token (`--cream-darker`)** | `#f5f1e8` | `var(--cream-darker)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--purple` | `#7E5AF2` | Color / Atmospheric Token |
| `--purple-deep` | `#5B3BC4` | Color / Atmospheric Token |
| `--purple-dark` | `#2D1B69` | Canvas / Surface Token |
| `--pink` | `#EC4899` | Typography Ink Token |
| `--yellow` | `#FACC15` | Color / Atmospheric Token |
| `--yellow-deep` | `#C2A011` | Color / Atmospheric Token |
| `--peach-deep` | `#C2691A` | Color / Atmospheric Token |
| `--pink-deep` | `#B8276F` | Typography Ink Token |
| `--peach` | `#FB923C` | Color / Atmospheric Token |
| `--lime` | `#84CC16` | Color / Atmospheric Token |
| `--sky` | `#0EA5E9` | Color / Atmospheric Token |
| `--cream` | `#FCFAF7` | Color / Atmospheric Token |
| `--cream-darker` | `#F5F1E8` | Canvas / Surface Token |
| `--ink` | `#0A0A0A` | Typography Ink Token |
| `--fs-body` | `18px` | Dimension / Scale Token |
| `--lh-body` | `1.55` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nbs-topbar> — `www-mynobs-co`)**:
   - Landmark `<header class="nbs-topbar">` (`1440x80px`) hosting `NoBS - No Brief Shit` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-nobs-sentry-sdk="1"`, `data-page="login"`, `data-auth="out"`, `data-nav="exit-demo"`), and stylesheet rule `.nbs-logo { display: inline-flex; align-items: center; text-decoration: none; line-h... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `IF YOUR BRIEF IS A LET'S CUT THE B`)**:
   - Landmark `<section class="hero">` presenting display lead `IF YOUR BRIEF IS A LET'S CUT THE BS` and copy excerpt *"Type, paste, or drop your brief. No Brief Shit (or NoBS, if we're"* over `#fcfaf7` canvas and `#0a0a0a` ink.
3. **Primary Showcase & Content Grid (<section.hero:nth(2)> — `Type, paste, or drop your brief. N`)**:
   - Landmark `<section class="hero">` rendering section `Type, paste, or drop your brief. No Brief Shit (` with copy *"Strictly necessary"*, asset references (`favicon.svg`, `fonts.googleapis.com`, `fonts.gstatic.com`, `css2`), and grid rule `.nbs-logo img { display: block; height: 60px; width: auto; }`.
4. **Interactive Detail & Feature Matrix (<section.hero:nth(3)> — `Strictly necessary`)**:
   - Landmark `<section class="hero">` framing `Strictly necessary` and `Without this, nothing else loads.` (*"Without this, nothing else loads."*) with `#ffd9ee` surface cards, `#ff0066` accents, and `.nbs-topbar-skeleton { position: sticky; top: 0; z-index: 100; background: var(--cream); min-he... }`.
5. **Colophon & Global Directory Footer (<footer.nbs-footer> — `https://www.mynobs.co`)**:
   - Landmark `<footer class="nbs-footer">` anchoring `NoBS - No Brief Shit` footer links (`Overview · Index · Archive · About · Contact`), copy *"Makes NoBS remember the little things."*, and `#a7a6a4` structural dividers.
