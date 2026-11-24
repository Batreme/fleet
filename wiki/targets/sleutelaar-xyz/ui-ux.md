---
title: "UI & UX Architecture: sleutelaar-xyz"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: sleutelaar-xyz

## Overview & Design Identity
- **Target**: `sleutelaar-xyz` (**Hans Sleutelaar · Officiële website**)
- **Production URL**: [https://sleutelaar.xyz/](https://sleutelaar.xyz/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#0000ff`)
- **Summary**: Digitaal archief over dichter, journalist en Nieuwe Stijl-oprichter Hans Sleutelaar (1935–2020). Gedichten, essays, foto's en bibliografie.
- **Total Clean CSS Variables Extracted**: `11` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `ABC Monument Grotesk`
- **Body Font Stack**: `ABC Monument Grotesk`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: observed font-size ladder: `36px`, `12px`, `15px`, `1em`, `80%`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 36px`, `line-height: 43.2px`, `font-weight: 500`, `letter-spacing: -0.72px`)
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: 18px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 15px`, `line-height: 15px`, `font-weight: 500`, `letter-spacing: -0.300001px`); CSS variables `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0d0d0d` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0000ff` | `.bg-blue { background-color: blue }` (`#0000ff`) |
| **Interactive Accent / Highlight** | `#0000ff` | `.bg-blue { background-color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#0000ff` | `html.blue ::selection { color: blue }` (`#0000ff`) |
| **Structural Hairline Border** | `#0000ff` | hairline divider derived from `html.blue ::selection { color: blue }` (`#0000ff`) |
| **Variable Token (`--color-blue`)** | `#009dd8` | `var(--color-blue)` in `:root` |
| **Variable Token (`--color-beige`)** | `#f0e6db` | `var(--color-beige)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-black` | `#0d0d0d` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |
| `--color-blue` | `#009dd8` | Brand / Palette Token |
| `--color-beige` | `#f0e6db` | Brand / Palette Token |
| `--z-index-filter-clone` | `20` | Elevation / Border Token |
| `--z-index-chrome` | `100` | Elevation / Border Token |
| `--tw-translate-x` | `0` | Design System Custom Token |
| `--tw-translate-y` | `0` | Design System Custom Token |
| `--tw-translate-z` | `0` | Design System Custom Token |
| `--sleutelaar-xyz-bg` | `#ffffff` | Canvas Substrate (from live computed `html` `background-color` (`computed_styles.json`)) |
| `--sleutelaar-xyz-ink` | `#0d0d0d` | Primary Typography Ink (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.uppercase> — `sleutelaar-xyz`)**:
   - Landmark `<header class="uppercase left-0">` (`1440x45px`) hosting `Hans Sleutelaar · Officiële website` navigation (`Biografie · Index · Gedichten · Archief`), DOM attributes (`data-sveltekit-preload-data="hover"`, `data-engine="three.js r185"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.grid-cols-12> — `Uitgevers en instituties`)**:
   - Landmark `<section class="grid-cols-12 text-48">` presenting display lead `Uitgevers en instituties` and copy excerpt *"Hans Sleutelaar (22 september 1935 – 25 juni 2020). Dichter - Jou"* over `#ffffff` canvas and `#0d0d0d` ink.
3. **Primary Showcase & Content Grid (<section.gap-y-20> — `Samen met`)**:
   - Landmark `<section class="gap-y-20 text-48">` rendering section `Samen met` with copy *"Voor het betere schrijfwerk Sleutelaar groeide op als enigs kind "*, asset references (`ABCMonumentGroteskTrial-Regular.otf`, `ABCMonumentGroteskTrial-Medium.otf`, `6b9a08feb31cdbce07aca8010c8613f21...`, `0.CvILTd3z.css`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.text-48> — `Voor het betere schrijfwerk Sleute`)**:
   - Landmark `<section class="gap-y-20 text-48">` framing `Voor het betere schrijfwerk Sleutelaar groeide o` and `Hij bleef nauw betrokken bij het behoud, het red` (*"Hij bleef nauw betrokken bij het behoud, het redigeren en heruitg"*) with `#0000ff` surface cards, `#0000ff` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.items-center> — `https://sleutelaar.xyz/`)**:
   - Landmark `<footer class="items-center">` anchoring `Hans Sleutelaar · Officiële webs` footer links (`Biografie · Index · Gedichten · Archief`), copy *"2018 International Film Festival Rotterdam (IFFR) - première"*, and `#0000ff` structural dividers.
