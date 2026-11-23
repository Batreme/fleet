---
title: "UI & UX Architecture: michellekayewashington-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: michellekayewashington-com

## Overview & Design Identity
- **Target**: `michellekayewashington-com` (**Michelle Kaye — Fine Arts · Contemporary Artist, Charleston SC**)
- **Production URL**: [https://michellekayewashington.com/](https://michellekayewashington.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fffdf8` canvas, `#120a09` ink, `#7a6560` accent)
- **Summary**: Michelle Kaye is a contemporary artist in Charleston, SC, exploring humanity’s relationship with the natural world. See Against the Grain...
- **Total Clean CSS Variables Extracted**: `42` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Cormorant`
- **Body Font Stack**: `Cormorant`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 115.2px`, `line-height: 103.68px`, `font-weight: 300`, `letter-spacing: -2.304px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 12.48px`, `line-height: 18.096px`, `font-weight: 500`, `letter-spacing: 2.7456px`)
- **Body Copy**: live computed `body` (`font-size: 21px`, `line-height: 30.45px`, `font-weight: 400`); rule `body` (`font-size: clamp(17px, 1.05vw + 10px, 21px)`, `line-height: 1.45`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 21px`, `line-height: 30.45px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fffdf8` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#120a09` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f6f0e8` | `var(--paper-2)` in `:root` |
| **Interactive Accent / Highlight** | `#7a6560` | live computed `button` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#9a675c` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#dedbd7` | `var(--rule)` in `:root` (`rgb(18 10 9 / 14%)`) |
| **Variable Token (`--ink-2`)** | `#2b201d` | `var(--ink-2)` in `:root` |
| **Variable Token (`--rose-2`)** | `#c68f81` | `var(--rose-2)` in `:root` |
| **Variable Token (`--tan`)** | `#b7a397` | `var(--tan)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--paper` | `#fffdf8` | Canvas / Surface Token |
| `--paper-2` | `#f6f0e8` | Canvas / Surface Token |
| `--ink` | `#120a09` | Typography Ink Token |
| `--ink-2` | `#2b201d` | Typography Ink Token |
| `--rose` | `#9a675c` | Color / Atmospheric Token |
| `--rose-2` | `#c68f81` | Color / Atmospheric Token |
| `--tan` | `#b7a397` | Color / Atmospheric Token |
| `--rule` | `rgb(18 10 9 / 14%)` | Color / Atmospheric Token |
| `--fg` | `var(--ink)` | Typography Ink Token |
| `--bg` | `var(--paper)` | Canvas / Surface Token |
| `--muted` | `#7a6560` | Color / Atmospheric Token |
| `--nav-w` | `clamp(190px, 15vw, 300px)` | Layout / Spatial Grid Token |
| `--pad` | `clamp(1.25rem, 3.2vw, 4rem)` | Layout / Spatial Grid Token |
| `--ease` | `cubic-bezier(0.22, 1, 0.36, 1)` | Motion / Easing Token |
| `--ease-io` | `cubic-bezier(0.65, 0, 0.35, 1)` | Motion / Easing Token |
| `--serif` | `"Cormorant", Georgia, "Times New Roman", serif` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.shell> — `michellekayewashington-com`)**:
   - Landmark `<header class="shell">` (`216x900px`) hosting `Michelle Kaye — Fine Arts · Contempo` navigation (`01 Michelle · 02 Gallery · 03 Socials · Charleston Magazine`), DOM attributes (`data-page="index"`, `data-ready="index"`, `data-shell`, `data-nav="index"`), and stylesheet rule `html { --room-title: var(--fg); }`.
2. **Hero Stage & Focal Lead (<section.home> — `Michelle Kaye`)**:
   - Landmark `<section class="home">` presenting display lead `Michelle Kaye` and copy excerpt *"Michelle Kaye explores the human condition through humanity’s rel"* over `#fffdf8` canvas and `#120a09` ink.
3. **Primary Showcase & Content Grid (<section.home:nth(2)> — `About the Artist`)**:
   - Landmark `<section class="home">` rendering section `About the Artist` with copy *"Ways to get in touch"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `after { box-sizing: border-box; }`.
4. **Interactive Detail & Feature Matrix (<section.home:nth(3)> — `Ways to get in touch`)**:
   - Landmark `<section class="home">` framing `Ways to get in touch` and `Keep scrolling to the Gallery` (*"Keep scrolling to the Gallery"*) with `#f6f0e8` surface cards, `#7a6560` accents, and `body { margin: 0; height: 100%; }`.
5. **Colophon & Global Directory Footer (<footer.wordmark-name> — `https://michellekayewashington.com/`)**:
   - Landmark `<footer class="wordmark-name">` anchoring `Michelle Kaye — Fine Arts · Cont` footer links (`01 Michelle · 02 Gallery · 03 Socials · Charleston Magazine`), copy *"Ways to get in touch"*, and `#dedbd7` structural dividers.
