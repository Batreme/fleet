# UI & UX Architecture: pankow-band

## Overview & Design Identity
- **Target**: `pankow-band` (**Die Pankow Zeitmaschine - Website der Berliner Rockband PANKOW**)
- **Production URL**: [https://pankow.band](https://pankow.band)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff7ee` canvas, `#000000` ink, `#ddd` accent)
- **Summary**: Die PANKOW Zeitmaschine ist die Band-Website der Rolling Stones des Ostens mit Diskografie, Videos, Chronik, Fangeschichten und Bildern a...
- **Total Clean CSS Variables Extracted**: `31` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Rowdies`
- **Body Font Stack**: `Poppins`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(2rem, 5vw, 3rem)`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(1.2rem, 2.2vw, 2rem)`)
- **Body Copy**: rule `p` (`font-size: clamp(1.05rem, 2vw, 1.35rem)`, `line-height: 1.55`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `1.2rem`, `clamp(1.05rem, 2vw, 1.35rem)`, `2rem`, `0.9rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff7ee` | `var(--farbe-schrift-auf-dunkel)` in `:root` |
| **Primary Typography Ink** | `#080808` | `var(--farbe-schrift-auf-hell)` in `:root` |
| **Elevated Surface / Card Substrate** | `#B82608` | `var(--farbe-fokus)` in `:root` |
| **Interactive Accent / Highlight** | `#ddd` | `var(--zeitmaschine-card-border)` in `:root` |
| **Secondary / Muted Copy** | `#000000` | `html { background: black }` (`#000000`) |
| **Structural Hairline Border** | `#BA0108` | `.section-title-h2 { background-color: #BA0108 }` |

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
   - Landmark `<header class="font-global">` hosting `Die Pankow Zeitmaschine - Website de` navigation (`Home · Info · Zeitmaschine · Kontakt`), DOM attributes (`data-nav-anchor="main"`, `data-nav-anchor="info"`, `data-nav-anchor="zeitmaschine"`, `data-nav-anchor="kontakt"`), and stylesheet rule `font-palette-values --palette0 { font-family: "pankow-icons"; base-palette: 0; }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Die Pankow-Zeitmaschine`)**:
   - Landmark `<section class="hero">` presenting display lead `Die Pankow-Zeitmaschine` and copy excerpt *"Zum Inhalt springen"* over `#fff7ee` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.info> — `Willkommen auf der Website der Ban`)**:
   - Landmark `<section class="info inhalts-section">` rendering section `Willkommen auf der Website der Band PANKOW (1981-...` with copy *"Ich habe mir einen Ort gewünscht, an dem man sich an die Band PAN"*, asset references (`favicon.ico`, `rubik-dirt-v2-latin-regular.woff2`, `pankow-hero-grunge-overlay-unten....`, `major.css`), and grid rule `.palette0 { font-palette: --palette0; color: currentColor; }`.
4. **Interactive Detail & Feature Matrix (<section.zeitmaschine-compat-message> — `Deine Technik ist leider zu alt od`)**:
   - Landmark `<section class="zeitmaschine-compat-message">` framing `Deine Technik ist leider zu alt oder Du lässt kei...` and `ALBEN` (*"Mein Dank geht an Monika Herold von SoulSite Design für die Zusam"*) with `#B82608` surface cards, `#ddd` accents, and `.icon-arrows-vertical:before { content: "\fb85"; }`.
5. **Colophon & Global Directory Footer (<footer.main-menu> — `https://pankow.band`)**:
   - Landmark `<footer class="main-menu">` anchoring `Die Pankow Zeitmaschine - Websit` footer links (`Home · Info · Zeitmaschine · Kontakt`), copy *"Stöbere mit der Zeitmaschine durch die Band-Historie, alle A"*, and `#BA0108` structural dividers.
