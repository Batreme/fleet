---
title: "UI & UX Architecture: foxvaluations-com-au"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: foxvaluations-com-au

## Overview & Design Identity
- **Target**: `foxvaluations-com-au` (**Property valuations Brisbane · Fox Valuations**)
- **Production URL**: [https://foxvaluations.com.au](https://foxvaluations.com.au)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×4968px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fbfaf7` canvas, `#131a24` ink, `#d96b3f` accent)
- **Summary**: Independent property valuations across Brisbane and South East Queensland by registered valuer Sebastian Fox. Fixed fee, quoted free.
- **Total Clean CSS Variables Extracted**: `29` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Mona Sans`
- **Body Font Stack**: `Mona Sans`
- **Monospace / Technical Font Stack**: `Spline Sans Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 64px`, `line-height: 66.56px`, `font-weight: 500`, `letter-spacing: -0.896px`); CSS variables `--display-ls: -0.032em`; rule `h1` (`font-size: clamp(2.6rem, 6vw, 4.5rem)`, `line-height: 1.04`, `letter-spacing: -0.015em`, `font-weight: 500`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 44.8px`, `line-height: 47.488px`, `font-weight: 500`, `letter-spacing: -0.6272px`); rule `h2` (`font-size: clamp(1.5rem, 2.6vw, 2.05rem)`, `line-height: 1.12`, `letter-spacing: -0.01em`, `font-weight: 500`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 26.4px`, `font-weight: 400`); rule `p` (`font-size: 1rem`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 26.4px`, `font-weight: 400`); CSS variables `--mono: "Spline Sans Mono", "SF Mono", Consolas, monospace`, `--label: 0.8rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fbfaf7` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#131a24` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#fafaf8` | `var(--paper)` in `:root` |
| **Interactive Accent / Highlight** | `#d96b3f` | live computed `a` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#414b58` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#dad8d0` | `var(--line)` in `:root` |
| **Variable Token (`--ink`)** | `#16202f` | `var(--ink)` in `:root` |
| **Variable Token (`--ink-2`)** | `#1c2839` | `var(--ink-2)` in `:root` |
| **Variable Token (`--ink-line`)** | `#2c3b50` | `var(--ink-line)` in `:root` |
| **Variable Token (`--plaster`)** | `#f1f1ed` | `var(--plaster)` in `:root` |
| **Variable Token (`--graphite`)** | `#262e3c` | `var(--graphite)` in `:root` |
| **Variable Token (`--slate`)** | `#5b6473` | `var(--slate)` in `:root` |
| **Variable Token (`--rust`)** | `#b14d2b` | `var(--rust)` in `:root` |
| **Variable Token (`--dark-body`)** | `#b8bfc9` | `var(--dark-body)` in `:root` |
| **Variable Token (`--dark-dim`)** | `#9aa3b0` | `var(--dark-dim)` in `:root` |
| **Variable Token (`--dark-bright`)** | `#f5f4f0` | `var(--dark-bright)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#16202F` | Typography Ink Token |
| `--ink-2` | `#1C2839` | Typography Ink Token |
| `--ink-line` | `#2C3B50` | Typography Ink Token |
| `--paper` | `#FAFAF8` | Canvas / Surface Token |
| `--plaster` | `#F1F1ED` | Color / Atmospheric Token |
| `--graphite` | `#262E3C` | Color / Atmospheric Token |
| `--slate` | `#5B6473` | Color / Atmospheric Token |
| `--rust` | `#B14D2B` | Color / Atmospheric Token |
| `--rust-bright` | `#D96B3F` | Color / Atmospheric Token |
| `--line` | `#DAD8D0` | Color / Atmospheric Token |
| `--dark-body` | `#B8BFC9` | Canvas / Surface Token |
| `--dark-dim` | `#9AA3B0` | Canvas / Surface Token |
| `--dark-bright` | `#F5F4F0` | Canvas / Surface Token |
| `--mono` | `"Spline Sans Mono", "SF Mono", Consolas, monospace` | Typography / Scale Token |
| `--label` | `0.8rem` | Dimension / Scale Token |
| `--shell` | `1240px` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-head> — `foxvaluations-com-au`)**:
   - Landmark `<header class="site-head site-head-cine">` (`1440x72px`) hosting `Property valuations Brisbane · Fox V` navigation (`Valuations · The standard · From the den · Tools · About`), DOM attributes (`data-website-id="dc310766-8aa8-41ef-af..."`, `data-portrait="1"`, `data-slot="svc-residential"`, `data-slot="svc-commercial"`), and stylesheet rule `html { scroll-behavior: smooth }`.
2. **Hero Stage & Focal Lead (<section.landing> — `What is your property worth?`)**:
   - Landmark `<section class="landing">` presenting display lead `What is your property worth?` and copy excerpt *"Independent property valuations by a registered valuer. Brisbane "* over `#fbfaf7` canvas and `#131a24` ink.
3. **Primary Showcase & Content Grid (<section.cred-strip> — `A figure you can act on.`)**:
   - Landmark `<section class="cred-strip">` rendering section `A figure you can act on.` with copy *"Registered valuer · Valuers Registration Board of Queensland · Me"*, asset references (`favicon-rust.png`, `analytics.blackshard.com.au`, `fox-mark-rust.png`, `fox-run-first-v2.webp`), and grid rule `img { display: block;max-width: 100%;height: auto }`.
4. **Interactive Detail & Feature Matrix (<section.standard> — `What do you need valued?`)**:
   - Landmark `<section class="standard standard-band">` framing `What do you need valued?` and `Meet the director` (*"Every property is inspected in person. Every figure is built from"*) with `#fafaf8` surface cards, `#d96b3f` accents, and `focus-visible { outline: 2px solid var(--rust);outline-offset: 3px }`.
5. **Colophon & Global Directory Footer (<footer.site-foot> — `https://foxvaluations.com.au`)**:
   - Landmark `<footer class="site-foot">` anchoring `Property valuations Brisbane · F` footer links (`Valuations · The standard · From the den · Tools · About`), copy *"Houses, units and townhouses, for a purchase, a sale or peac"*, and `#dad8d0` structural dividers.
