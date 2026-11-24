---
title: "UI & UX Architecture: tridentstars-maserati-com_en"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: tridentstars-maserati-com_en

## Overview & Design Identity
- **Target**: `tridentstars-maserati-com_en` (**Discover Maserati’s Trident Constellation in the Sky**)
- **Production URL**: [https://tridentstars.maserati.com/en/](https://tridentstars.maserati.com/en/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×872px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#2285f7`)
- **Summary**: A real constellation of stars created to celebrate 100 years of vision, performance and iconic design.
- **Total Clean CSS Variables Extracted**: `89` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `TWK Everett`
- **Body Font Stack**: `TWK Everett`
- **Monospace / Technical Font Stack**: `Roboto Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 64px`, `line-height: 64px`, `font-weight: 200`); rule `h1` (`font-size: 1.5rem`, `line-height: 1.2`)
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: 1.33333`; rule `h2` (`font-size: 1.5rem`, `line-height: 1.25`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 300`); rule `p` (`font-size: .75em`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 11px`, `line-height: 15px`, `font-weight: 500`, `letter-spacing: 1px`); CSS variables `--text-sm: .875rem`, `--text-sm--line-height: 1.42857`, `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#2d2d2d` | `var(--tl-thumb-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#2285f7` | `etrust-pc-sdk #clear-filters-ha... { color: #2285f7 }` |
| **Secondary / Muted Copy** | `#78808e` | `.ot-leg-btn-container .ot-inact... { color: #78808e }` |
| **Structural Hairline Border** | `#2d2d2d` | `var(--tl-border-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--easing` | `cubic-brazier(.19,.39,0,1.04)` | Motion / Easing Token |
| `--tl-border-color` | `#2d2d2d` | Brand / Palette Token |
| `--tl-thumb-bg` | `#2d2d2d` | Canvas / Surface Token |
| `--spin` | `0deg` | Design System Custom Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-xl` | `36rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `1.42857` | Typography Ink Token |
| `--text-xl` | `1.25rem` | Typography Ink Token |
| `--text-xl--line-height` | `1.4` | Typography Ink Token |
| `--text-2xl` | `1.5rem` | Typography Ink Token |
| `--text-2xl--line-height` | `1.33333` | Typography Ink Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.top-0> — `tridentstars-maserati-com_en`)**:
   - Landmark `<header class="top-0 right-0">` (`1440x90px`) hosting `Discover Maserati’s Trident Constell` navigation (`the manifesto · discover more`), DOM attributes (`data-domain-script="81be852f-f22f-496a-87..."`, `data-document-language="true"`, `data-hid="adobe-launch"`, `data-hid="adobe-data-layer"`), and stylesheet rule `.external-link-icon__arrow { transition:translate .3s }`.
2. **Hero Stage & Focal Lead (<section.ot-sdk-row> — `100 YEARS OF THE TRIDENT LOGO 1 0 `)**:
   - Landmark `<section class="ot-sdk-row ot-cat-grp">` presenting display lead `100 YEARS OF THE TRIDENT LOGO 1 0 0 Y E A R S O F...` and copy excerpt *"SCROLL TO EXPLORE THE TRIDENT CONSTELLATION"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.ot-hide> — `SCROLL TO EXPLORE THE TRIDENT CONS`)**:
   - Landmark `<section class="ot-hide ot-hosts-ui">` rendering section `SCROLL TO EXPLORE THE TRIDENT CONSTELLATION` with copy *"100 YEARS OF THE TRIDENT LOGO 1 0 0 Y E A R S O F T H E T R I D E"*, asset references (`entry.Btz3ffrH.css`, `default.CffeYOeI.css`, `MoleculesExternalLink.BgGEM1Uz.css`, `MoleculesPopup.CyDrrBxz.css`), and grid rule `hover .external-link-icon__arrow { translate:2px -2px }`.
4. **Interactive Detail & Feature Matrix (<section.left-0> — `100 YEARS OF THE TRIDENT LOGO 1 0 `)**:
   - Landmark `<section class="left-0">` framing `100 YEARS OF THE TRIDENT LOGO 1 0 0 Y E A R S O ` and `100 YEARS OF THE TRIDENT LOGO` (*"100 YEARS OF THE TRIDENT LOGO"*) with `#2d2d2d` surface cards, `#2285f7` accents, and `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.z-header> — `https://tridentstars.maserati.com/en/`)**:
   - Landmark `<footer class="z-header">` anchoring `Discover Maserati’s Trident Cons` footer links (`the manifesto · discover more`), copy *"1 0 0 Y E A R S O F T H E T R I D E N T L O G O"*, and `#2d2d2d` structural dividers.
