---
title: "UI & UX Architecture: www-schlosshotel-kitzbuehel-com_en"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-schlosshotel-kitzbuehel-com_en

## Overview & Design Identity
- **Target**: `www-schlosshotel-kitzbuehel-com_en` (**Schlosshotel Kitzbühel – a premium experience**)
- **Production URL**: [https://www.schlosshotel-kitzbuehel.com/en](https://www.schlosshotel-kitzbuehel.com/en)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×4140px`, Mobile `390×2616px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#300316` canvas, `#ffffff` ink, `#42041e` accent)
- **Summary**: A beacon of elegance, exclusivity, and warmth – Schlosshotel Kitzbühel is a truly unparalleled retreat.
- **Total Clean CSS Variables Extracted**: `65` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Assistant`
- **Body Font Stack**: `Assistant`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 9.008px`, `line-height: 10.8096px`, `font-weight: 600`, `letter-spacing: 2.2px`); rule `h1` (`line-height: 1.2`, `font-weight: 500`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 18.9168px`, `line-height: 29.5102px`, `font-weight: 700`); rule `h2` (`font-size: 1em`, `line-height: 1.2`, `font-weight: 500`)
- **Body Copy**: live computed `body` (`font-size: 9.008px`, `line-height: 14.0525px`, `font-weight: 400`); rule `p` (`font-size: 12px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 9.008px`, `line-height: 14.0525px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#300316` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#42041e` | `.branDNAmic .DNA-button--cta-bo... { color: #42041e }` |
| **Secondary / Muted Copy** | `#999999` | live computed `button` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#2865ad` | `var(--BN-dynform--clr-button-border)` in `:root` |
| **Variable Token (`--BN-dynform--clr-scrollbar-thumb`)** | `#c4c4c4` | `var(--BN-dynform--clr-scrollbar-thumb)` in `:root` |
| **Variable Token (`--BN-dynform--clr-selection-text`)** | `#0b0b0b` | `var(--BN-dynform--clr-selection-text)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--dna-tldr-bg` | `#300316` | Canvas / Surface Token |
| `--dna-tldr-text` | `#FFFFFF` | Typography Ink Token |
| `--dna-tldr-fs-desktop` | `2.1em` | Dimension / Scale Token |
| `--dna-tldr-fs-mobile` | `1.6em` | Dimension / Scale Token |
| `--BN-dynform--ff` | `inherit` | Design System Custom Token |
| `--BN-dynform--fw-bold` | `700` | Design System Custom Token |
| `--BN-dynform--fw-light` | `300` | Canvas / Surface Token |
| `--BN-dynform--fw-regular` | `400` | Design System Custom Token |
| `--BN-dynform--clr-scrollbar-thumb` | `#C4C4C4` | Color / Atmospheric Token |
| `--BN-dynform--clr-scrollbar-track` | `transparent` | Design System Custom Token |
| `--BN-dynform--clr-selection-bg` | `#C4C4C4` | Canvas / Surface Token |
| `--BN-dynform--clr-selection-text` | `#0B0B0B` | Typography Ink Token |
| `--BN-dynform--clr-form-bg` | `#ffffff` | Canvas / Surface Token |
| `--BN-dynform--clr-button-bg` | `#2865AD` | Canvas / Surface Token |
| `--BN-dynform--clr-button-border` | `#2865AD` | Elevation / Border Token |
| `--BN-dynform--clr-button-text` | `#ffffff` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.SECT-Header> — `www-schlosshotel-kitzbuehel-com_en`)**:
   - Landmark `<header class="SECT-Header DNA-section">` (`1440x0px`) hosting `Schlosshotel Kitzbühel – a premium e` navigation (`Book · Enquire · Spa · Rooms and Suites · Meetings & Events`), DOM attributes (`data-asset-id="Scss/presets"`, `data-asset-id="Scss/vendors"`, `data-asset-id="Globals/Main"`, `data-asset-id="Sections/Header"`), and stylesheet rule `from { transform:translateX(0) }`.
2. **Hero Stage & Focal Lead (<section.MOD-RoomsTeaser> — `SCHLOSSHOTEL KITZBÜHEL`)**:
   - Landmark `<section class="MOD-RoomsTeaser DNA-module">` presenting display lead `SCHLOSSHOTEL KITZBÜHEL` and copy excerpt *"Some places whisper rather than shout. Schlosshotel Kitzbühel is "* over `#300316` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.MOD-OffersTeaser> — `Schlosshotel Kitzbühel`)**:
   - Landmark `<section class="MOD-OffersTeaser DNA-module">` rendering section `Schlosshotel Kitzbühel` with copy *"Schlosshotel Kitzbühel"*, asset references (`favicon-96x96.png`, `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `page { margin:.5cm }`.
4. **Interactive Detail & Feature Matrix (<section.MOD-Text> — `Welcome to the threshold of the ex`)**:
   - Landmark `<section class="MOD-Text DNA-module">` framing `Welcome to the threshold of the extraordinary` and `For people of refined taste. For you.` (*"Welcome to the threshold of the extraordinary"*) with `#000000` surface cards, `#42041e` accents, and `body { font-family:Arial,sans-serif;font-size:12px }`.
5. **Colophon & Global Directory Footer (<footer.SECT-Footer> — `https://www.schlosshotel-kitzbuehel.com/en`)**:
   - Landmark `<footer class="SECT-Footer DNA-section">` anchoring `Schlosshotel Kitzbühel – a premi` footer links (`Book · Enquire · Spa · Rooms and Suites · Meetings & Events`), copy *"No flashy façade. No hollow shine. Instead: real stone benea"*, and `#2865ad` structural dividers.
