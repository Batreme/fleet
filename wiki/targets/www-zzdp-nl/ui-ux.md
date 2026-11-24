---
title: "UI & UX Architecture: www-zzdp-nl"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-zzdp-nl

## Overview & Design Identity
- **Target**: `www-zzdp-nl` (**Al meer dan 70 jaar betekenisvolle architectuur · ZZDP**)
- **Production URL**: [https://www.zzdp.nl/](https://www.zzdp.nl/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#12366b` ink, `#ff2800` accent)
- **Summary**: Bij ZZDP combineren we vakmanschap en visie in betekenisvolle architectuur. Met meer dan 70 jaar ervaring realiseren we ontwerpen waarin...
- **Total Clean CSS Variables Extracted**: `191` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `HelveticaNowDisplay`
- **Body Font Stack**: `HelveticaNowDisplay`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 32px`, `line-height: 48px`, `font-weight: 700`); CSS variables `--font-helvetica-now-display: "helveticaNowDisplay", "helveticaNowDisplay Fallback"`; rule `h1` (`font-size: 13.3333vw`, `line-height: 82%`, `letter-spacing: -.07em`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 120px`, `line-height: 98.4px`, `font-weight: 400`, `letter-spacing: -8.4px`); rule `h2` (`font-size: 8vw`, `line-height: 105%`, `letter-spacing: .01em`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: 3.73333vw`, `line-height: 132%`, `letter-spacing: 0`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#12366b` | live computed `p` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ebeae1` | live computed `section` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ff2800` | live computed `a` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#c7c6be` | `var(--secondary-ui-label-disabled-color)` in `:root` |
| **Structural Hairline Border** | `#b5b899` | `var(--primary-ui-stroke-hover-color)` in `:root` |
| **Variable Token (`--title-color`)** | `#656657` | `var(--title-color)` in `:root` |
| **Variable Token (`--line-color`)** | `#1a1630` | `var(--line-color)` in `:root` |
| **Variable Token (`--accent-color`)** | `#8746e3` | `var(--accent-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background-color` | `#fff` | Canvas / Surface Token |
| `--title-color` | `#656657` | Brand / Palette Token |
| `--subtitle-color` | `#656657` | Brand / Palette Token |
| `--body-color` | `#656657` | Typography Ink Token |
| `--line-color` | `#1a163019` | Brand / Palette Token |
| `--accent-color` | `#8746e3` | Brand / Palette Token |
| `--primary-ui-label-default-color` | `#fff` | Brand / Palette Token |
| `--primary-ui-label-hover-color` | `#fff` | Brand / Palette Token |
| `--primary-ui-label-disabled-color` | `#c7c6be` | Brand / Palette Token |
| `--primary-ui-background-default-color` | `#656657` | Canvas / Surface Token |
| `--primary-ui-background-hover-color` | `#b5b899` | Canvas / Surface Token |
| `--primary-ui-background-disabled-color` | `#ebeae1` | Canvas / Surface Token |
| `--primary-ui-stroke-default-color` | `#656657` | Brand / Palette Token |
| `--primary-ui-stroke-hover-color` | `#b5b899` | Brand / Palette Token |
| `--primary-ui-stroke-disabled-color` | `#ebeae1` | Brand / Palette Token |
| `--secondary-ui-label-default-color` | `#656657` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.lenis> — `www-zzdp-nl`)**:
   - Landmark `<nav class="lenis">` (`227x18px`) hosting `Al meer dan 70 jaar betekenisvolle a` navigation (`Home · Projecten · Over ons · Nieuws en inzichten · Vacatures`), DOM attributes (`data-next-head`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`), and stylesheet rule `.u-underline-link:after { height:.266667vw }`.
2. **Hero Stage & Focal Lead (<section.theme--mossLight> — `ZZDP`)**:
   - Landmark `<section class="theme--mossLight">` presenting display lead `ZZDP` and copy excerpt *"We staan op de schouders van onze voorgangers. Met meer dan 70 ja"* over `#ffffff` canvas and `#12366b` ink.
3. **Primary Showcase & Content Grid (<section.vjs-styles-dimensions> — `Bij ZZDP geloven wij dat architect`)**:
   - Landmark `<section class="vjs-styles-dimensions">` rendering section `Bij ZZDP geloven wij dat architectuur meer is dan...` with copy *"Video Player is loading."*, asset references (`favicon.svg`, `HelveticaNowDisplay_Regular-s.p.1...`, `HelveticaNowDisplay_Md-s.p.16ns3u...`, `PPNeueMachina_PlainRegular-s.p.39...`), and grid rule `.default-in-animation { transform:translateY(26.6667vw) }`.
4. **Interactive Detail & Feature Matrix (<section.theme--white> — `Gedreven door nalatenschap`)**:
   - Landmark `<section class="theme--white">` framing `Gedreven door nalatenschap` and `Partners in design` (*"Seek to live, currently behind live"*) with `#ebeae1` surface cards, `#ff2800` accents, and `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;line-height:1.15 }`.
5. **Colophon & Global Directory Footer (<footer.theme--white> — `https://www.zzdp.nl/`)**:
   - Landmark `<footer class="theme--white">` anchoring `Al meer dan 70 jaar betekenisvol` footer links (`Home · Projecten · Over ons · Nieuws en inzichten · Vacatures`), copy *"descriptions off , selected"*, and `#b5b899` structural dividers.
