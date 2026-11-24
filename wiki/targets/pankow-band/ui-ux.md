---
title: "UI & UX Architecture: pankow-band"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: pankow-band

## Overview & Design Identity
- **Target**: `pankow-band` (**Die Pankow Zeitmaschine - Website der Berliner Rockband PANKOW**)
- **Production URL**: [https://pankow.band](https://pankow.band)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×4968px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#e3bd8e` canvas, `#000000` ink, `#ffff00` accent)
- **Summary**: Die PANKOW Zeitmaschine ist die Band-Website der Rolling Stones des Ostens mit Diskografie, Videos, Chronik, Fangeschichten und Bildern a...
- **Total Clean CSS Variables Extracted**: `31` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Poppins`
- **Body Font Stack**: `Poppins`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 32px`, `line-height: normal`, `font-weight: 700`); rule `h1` (`font-size: clamp(2rem, 5vw, 3rem)`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 80px`, `line-height: 96px`, `font-weight: 400`, `letter-spacing: -6.4px`); rule `h2` (`font-size: clamp(1.2rem, 2.2vw, 2rem)`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 500`); rule `p` (`font-size: clamp(1.05rem, 2vw, 1.35rem)`, `line-height: 1.55`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 19.2px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#e3bd8e` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `nav` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `.skip-link { background: #ffffff }` |
| **Interactive Accent / Highlight** | `#ffff00` | `.button-consent { background: yellow }` (`#ffff00`) |
| **Secondary / Muted Copy** | `#b95d47` | live computed `footer` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#dddddd` | `var(--zeitmaschine-card-border)` in `:root` |
| **Variable Token (`--farbe-schrift-auf-dunkel`)** | `#fff7ee` | `var(--farbe-schrift-auf-dunkel)` in `:root` |
| **Variable Token (`--farbe-schrift-auf-hell`)** | `#080808` | `var(--farbe-schrift-auf-hell)` in `:root` |
| **Variable Token (`--farbe-fokus`)** | `#b82608` | `var(--farbe-fokus)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--farbe-schrift-auf-dunkel` | `#fff7ee` | Color / Atmospheric Token |
| `--farbe-schrift-auf-hell` | `#080808` | Color / Atmospheric Token |
| `--farbe-link` | `rgba(181, 47, 14, 0.7)` | Typography Ink Token |
| `--farbe-link-auf-dunkel` | `rgb(185, 93, 71)` | Typography Ink Token |
| `--farbe-fokus` | `#B82608` | Color / Atmospheric Token |
| `--farbe-headline` | `rgba(181, 47, 14, 0.8)` | Color / Atmospheric Token |
| `--zeitmaschine-card-passive-mehr-bg` | `rgba(255, 255, 255, 0.3)` | Canvas / Surface Token |
| `--zeitmaschine-card-active-mehr-bg` | `rgba(181, 47, 14, 0.3)` | Canvas / Surface Token |
| `--overlay-article-bg` | `rgba(181, 47, 14, 0.2)` | Canvas / Surface Token |
| `--overlay-nav-elemente-color-lightbg` | `rgba(181, 47, 14, 0.6)` | Canvas / Surface Token |
| `--overlay-nav-elemente-color-darkbg` | `rgba(246, 100, 64, 0.4)` | Canvas / Surface Token |
| `--zeitmaschine-card-border` | `#ddd` | Elevation / Border Token |
| `--zeitmaschine-card-active-weniger-bg` | `url("../bgs/zeitmaschine/pankow-card-bg-weniger-active.jpg")` | Canvas / Surface Token |
| `--zeitmaschine-card-passive-weniger-bg` | `url("../bgs/zeitmaschine/pankow-card-bg-weniger-passive.jpg")` | Canvas / Surface Token |
| `--menu-width-closed` | `6rem` | Layout / Spatial Grid Token |
| `--menu-width-open` | `400px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.font-global> — `pankow-band`)**:
   - Landmark `<header class="font-global">` (`96x80px`) hosting `Die Pankow Zeitmaschine - Website de` navigation (`Home · Info · Zeitmaschine · Kontakt`), DOM attributes (`data-nav-anchor="main"`, `data-nav-anchor="info"`, `data-nav-anchor="zeitmaschine"`, `data-nav-anchor="kontakt"`), and stylesheet rule `font-palette-values --palette0 { font-family: "pankow-icons"; base-palette: 0; }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Die Pankow-Zeitmaschine`)**:
   - Landmark `<section class="hero">` presenting display lead `Die Pankow-Zeitmaschine` and copy excerpt *"Ich habe mir einen Ort gewünscht, an dem man sich an die Band PAN"* over `#e3bd8e` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.info> — `Willkommen auf der Website der Ban`)**:
   - Landmark `<section class="info inhalts-section">` rendering section `Willkommen auf der Website der Band PANKOW (1981-...` with copy *"Mein Dank geht an Monika Herold von SoulSite Design für die Zusam"*, asset references (`favicon.ico`, `rubik-dirt-v2-latin-regular.woff2`, `pankow-hero-grunge-overlay-unten....`, `major.css`), and grid rule `.palette0 { font-palette: --palette0; color: currentColor; }`.
4. **Interactive Detail & Feature Matrix (<section.zeitmaschine-compat-message> — `Deine Technik ist leider zu alt od`)**:
   - Landmark `<section class="zeitmaschine-compat-message">` framing `Deine Technik ist leider zu alt oder Du lässt kei...` and `Hans im Glück` (*"Stöbere mit der Zeitmaschine durch die Band-Historie, alle Alben "*) with `#ffffff` surface cards, `#ffff00` accents, and `.icon-arrows-vertical:before { content: "\fb85"; }`.
5. **Colophon & Global Directory Footer (<footer.main-menu> — `https://pankow.band`)**:
   - Landmark `<footer class="main-menu">` anchoring `Die Pankow Zeitmaschine - Websit` footer links (`Home · Info · Zeitmaschine · Kontakt`), copy *"Deshalb kann die Zeitmaschine hier nicht richtig angezeigt u"*, and `#dddddd` structural dividers.
