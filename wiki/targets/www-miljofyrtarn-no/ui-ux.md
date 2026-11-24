---
title: "UI & UX Architecture: www-miljofyrtarn-no"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-miljofyrtarn-no

## Overview & Design Identity
- **Target**: `www-miljofyrtarn-no` (**Hjem · Miljøfyrtårn**)
- **Production URL**: [https://www.miljofyrtarn.no/](https://www.miljofyrtarn.no/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#00aceb` accent)
- **Summary**: Miljøfyrtårn er Norges ledende miljøsertifisering. Kom i gang med sertifisering og miljøledelse i LUMA – et verktøy som gjør arbeidet enk...
- **Total Clean CSS Variables Extracted**: `29` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `matterFont`
- **Body Font Stack**: `matterFont`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 87.984px`, `line-height: 87.984px`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 63.936px`, `line-height: 63.936px`, `font-weight: 400`); rule `h2` (`font-size: 1.75rem`, `line-height: 1`)
- **Body Copy**: live computed `body` (`font-size: 15.984px`, `line-height: 23.976px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 15.984px`, `line-height: 23.976px`, `font-weight: 400`); CSS variables `--media-caption-h: 4rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e6e6e6` | `.bg-grey-20 { background-color: #e6e6e6 }` |
| **Interactive Accent / Highlight** | `#00aceb` | `stom-button.button-light .icon... { color: #00aceb }` |
| **Secondary / Muted Copy** | `#00aceb` | `stom-button.button-light .icon... { color: #00aceb }` |
| **Structural Hairline Border** | `#e5e5e5` | `10 { border-color: #e5e5e5 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--lines-gutter` | `clamp(.9rem, 1.11vw, 1.25rem)` | Layout / Spatial Grid Token |
| `--media-max-h` | `calc(100svh - 4.5rem - 3.25rem)` | Dimension / Scale Token |
| `--media-caption-h` | `4rem` | Dimension / Scale Token |
| `--media-min-w` | `24rem` | Dimension / Scale Token |
| `--font-matter` | `"matterFont", "matterFont Fallback"` | Typography / Scale Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-xl` | `36rem` | Layout / Spatial Grid Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--font-weight-semibold` | `600` | Typography / Scale Token |
| `--font-weight-bold` | `700` | Typography / Scale Token |
| `--leading-tight` | `1.25` | Typography / Scale Token |
| `--leading-normal` | `1.5` | Typography / Scale Token |
| `--radius-md` | `.375rem` | Elevation / Border Token |
| `--radius-lg` | `.5rem` | Elevation / Border Token |
| `--radius-xl` | `.75rem` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.top-bar> — `www-miljofyrtarn-no`)**:
   - Landmark `<nav class="top-bar pointer-events-none">` (`1440x96px`) hosting `Hjem · Miljøfyrtårn` navigation (`Interaktiv veiviser · Start registrering · Finn konsulent · Kundehistorier · Om oss Om oss`), DOM attributes (`data-precedence="next"`, `data-href="/_next/static/chunks/..."`, `data-dgst`, `data-section="0"`), and stylesheet rule `._5KZDLG_className { font-family:matterFont,matterFont Fallback }`.
2. **Hero Stage & Focal Lead (<section.stage> — `Norges mest brukte miljøsertifiser`)**:
   - Landmark `<section class="stage relative">` presenting display lead `Norges mest brukte miljøsertifisering` and copy excerpt *"Bli Miljøfyrtårn? Prøv vår interaktive veiviser!"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.image-fullscreen> — `Fordi bærekraft er konkurransekraf`)**:
   - Landmark `<section class="image-fullscreen lines-scope">` rendering section `Fordi bærekraft er konkurransekraft` with copy *"Norges mest brukte miljøsertifisering"*, asset references (`MatterMedium-s.p.07t3y7_ykvrde.woff2`, `MatterRegular-s.p.3jjuiv35wp9rz.w...`, `MatterRegularItalic-s.p.03ktjrzd9...`, `MatterSemiBold-s.p.1twnp8ioanuv2....`), and grid rule `._5KZDLG_variable { --font-matter:"matterFont", "matterFont Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.image-group> — `Fornøyde kunder sier`)**:
   - Landmark `<section class="image-group lines-scope">` framing `Fornøyde kunder sier` and `Hvorfor bli Miljøfyrtårn` (*"Norges mest brukte"*) with `#e6e6e6` surface cards, `#00aceb` accents, and `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.lines-scope> — `https://www.miljofyrtarn.no/`)**:
   - Landmark `<footer class="lines-scope overflow-clip">` anchoring `Hjem · Miljøfyrtårn` footer links (`Interaktiv veiviser · Start registrering · Finn konsulent · Kundehistorier · Om oss Om oss`), copy *"miljøsertifisering"*, and `#e5e5e5` structural dividers.
