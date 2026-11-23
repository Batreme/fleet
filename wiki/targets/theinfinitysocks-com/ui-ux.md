---
title: "UI & UX Architecture: theinfinitysocks-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: theinfinitysocks-com

## Overview & Design Identity
- **Target**: `theinfinitysocks-com` (**Infinity Socks — Performance Basketball Socks**)
- **Production URL**: [https://theinfinitysocks.com/](https://theinfinitysocks.com/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ede4d2` / `#c96f4a`)
- **Summary**: Infinity performance basketball socks. Court System™ — four technologies engineered for the hardwood. Tested by professional players. Pro...
- **Total Clean CSS Variables Extracted**: `174` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `FK Screamer`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 100.8px`, `line-height: 90.72px`, `font-weight: 900`); CSS variables `--text-4xl: 2.25em`, `--display: var(--font-heading)`, `--h1-top: 18.2%`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 30px`, `line-height: 42.9px`, `font-weight: 400`, `letter-spacing: 0.6px`); CSS variables `--text-2xl: 1.5em`, `--text-3xl: 1.875em`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 22.88px`, `font-weight: 400`); CSS variables `--font-body: "Geist", system-ui, sans-serif`, `--text-base: .875em`, `--body: var(--font-body)`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 10.5px`, `line-height: 15.015px`, `font-weight: 400`, `letter-spacing: 1.47px`); CSS variables `--font-mono: "Geist Mono", ui-monospace, Menlo, monospace`, `--text-xs: .75em`, `--text-sm: .8125em`; rule `small` (`font-size: calc(var(--size-font) * .6875)`, `letter-spacing: .26em`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ede4d2` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#211a12` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f6f0e2` | live computed `a` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#c96f4a` | `.cc__banner .cc__link:hover { color: #c96f4a }` |
| **Secondary / Muted Copy** | `#6b6b6b` | `var(--cc-color-muted)` in `:root` |
| **Structural Hairline Border** | `#f1e9d9` | `var(--hairline)` in `:root` (`rgba(255, 250, 240, .22)`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--fsa` | `.5` | Design System Custom Token |
| `--size-unit` | `16` | Layout / Spatial Grid Token |
| `--size-container-ideal` | `1440` | Layout / Spatial Grid Token |
| `--size-container-min` | `992px` | Layout / Spatial Grid Token |
| `--size-container-max` | `6000px` | Layout / Spatial Grid Token |
| `--size-container` | `clamp(var(--size-container-min), 100vw, var(--size-container-max))` | Layout / Spatial Grid Token |
| `--font-body` | `"Geist", system-ui, sans-serif` | Typography / Scale Token |
| `--font-heading` | `"FK Screamer", "Arial Narrow", Impact, sans-serif` | Typography Ink Token |
| `--font-mono` | `"Geist Mono", ui-monospace, Menlo, monospace` | Typography / Scale Token |
| `--text-xs` | `.75em` | Typography Ink Token |
| `--text-sm` | `.8125em` | Typography Ink Token |
| `--text-base` | `.875em` | Typography Ink Token |
| `--text-md` | `1em` | Typography Ink Token |
| `--text-lg` | `1.125em` | Typography Ink Token |
| `--text-xl` | `1.25em` | Typography Ink Token |
| `--text-2xl` | `1.5em` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.cc__dialog-head> — `theinfinitysocks-com`)**:
   - Landmark `<header class="cc__dialog-head">` (`1440px`) hosting `Infinity Socks — Performance Basketb` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-skip`, `data-motion-toggle`, `data-motion-label`, `data-cc-host`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.hero> — `High-Performance Socks High-Perfor`)**:
   - Landmark `<section class="hero hero--h1a">` presenting display lead `High-Performance Socks High-Performance Socks Hig...` and copy excerpt *"“Still dry — even though I played a whole game.”"* over `#ede4d2` canvas and `#211a12` ink.
3. **Primary Showcase & Content Grid (<section.court> — `Trusted every possession.`)**:
   - Landmark `<section class="court">` rendering section `Trusted every possession.` with copy *"High-Performance Socks High-Performance Socks High-Performance So"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `button { font:inherit;color:inherit;background:none;border:0;margin:0;cursor:poin... }`.
4. **Interactive Detail & Feature Matrix (<section.qq> — `One pair of socks. Four quarters o`)**:
   - Landmark `<section class="qq">` framing `One pair of socks. Four quarters of excellence.` and `ImpactShield™` (*"High-Performance Socks"*) with `#f6f0e2` surface cards, `#c96f4a` accents, and `.cc__placeholder :focus-visible { outline:2px solid var(--cc-color-focus);outline-offset:2px }`.
5. **Colophon & Global Directory Footer (<footer.cc__dialog-actions> — `https://theinfinitysocks.com/`)**:
   - Landmark `<footer class="cc__dialog-actions cc__actions">` anchoring `Infinity Socks — Performance Bas` footer links (`Overview · Index · Archive · About · Contact`), copy *"Engineered for the Hardwood"*, and `#f1e9d9` structural dividers.
