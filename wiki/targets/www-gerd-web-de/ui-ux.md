# UI & UX Architecture: www-gerd-web-de

## Overview & Design Identity
- **Target**: `www-gerd-web-de` (**Gerd Web 3 Second - Design**)
- **Production URL**: [https://www.gerd-web.de](https://www.gerd-web.de)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#080c16` canvas, `#e6edf8` ink, `#a855f7` accent)
- **Summary**: Design ist unsere Leidenschaft. Wir begleiten Ihr Webprojekt ganzheitlich – vom prägnanten Logo über ausdrucksstarke Bildwelten bis hin z...
- **Total Clean CSS Variables Extracted**: `23` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Dancing Script`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `12px`, `78px`, `clamp(1.4rem, 4vw, 1.875rem)`, `1rem`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `12px`, `78px`, `clamp(1.4rem, 4vw, 1.875rem)`, `1rem`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `12px`, `78px`, `clamp(1.4rem, 4vw, 1.875rem)`, `1rem`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `12px`, `78px`, `clamp(1.4rem, 4vw, 1.875rem)`, `1rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#080c16` | `var(--bg-base)` in `:root` |
| **Primary Typography Ink** | `#101c36` | `var(--bg-center)` in `:root` |
| **Elevated Surface / Card Substrate** | `#00f0ff` | `var(--net-color)` in `:root` |
| **Interactive Accent / Highlight** | `#a855f7` | `var(--active-color)` in `:root` |
| **Secondary / Muted Copy** | `#d8b4fe` | `var(--cursor-ring-color)` in `:root` |
| **Structural Hairline Border** | `#e6edf8` | `var(--text-color)` in `:root` |
| **Variable Token (`--text-muted`)** | `#94a3b8` | `var(--text-muted)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg-base` | `#080c16` | Canvas / Surface Token |
| `--bg-center` | `#101c36` | Canvas / Surface Token |
| `--card-bg` | `rgba(14, 23, 42, 0.7)` | Canvas / Surface Token |
| `--net-color` | `#00f0ff` | Brand / Palette Token |
| `--net-glow` | `rgba(0, 240, 255, 0.35)` | Color / Atmospheric Token |
| `--btn-bg` | `rgba(13, 22, 41, 0.88)` | Canvas / Surface Token |
| `--btn-border` | `#00f0ff` | Elevation / Border Token |
| `--btn-hover-border` | `#00f0ff` | Elevation / Border Token |
| `--btn-hover-glow` | `rgba(0, 240, 255, 0.7)` | Color / Atmospheric Token |
| `--active-color` | `#a855f7` | Brand / Palette Token |
| `--active-glow` | `rgba(168, 85, 247, 0.75)` | Color / Atmospheric Token |
| `--cursor-ring-color` | `#d8b4fe` | Brand / Palette Token |
| `--cursor-ring-glow` | `rgba(168, 85, 247, 0.85)` | Elevation / Border Token |
| `--text-color` | `#e6edf8` | Typography Ink Token |
| `--text-muted` | `#94a3b8` | Typography Ink Token |
| `--section-spacing` | `40px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.menu-container> — `www-gerd-web-de`)**:
   - Landmark `<nav class="menu-container">` hosting `Gerd Web 3 Second - Design` navigation (`Home · Web · Plakate · Spiele · Foto`), DOM attributes (`data-target="www-gerd-web-de"`), and stylesheet rule `cursor-dot { opacity: 0 !important; }`.
2. **Hero Stage & Focal Lead (<section.impressum-section> — `Webdesign mit Charakter`)**:
   - Landmark `<section class="impressum-section">` presenting display lead `Webdesign mit Charakter` and copy excerpt *"Design ist unsere Leidenschaft. Wir begleiten Ihr Webprojekt ganz"* over `#080c16` canvas and `#e6edf8` ink.
3. **Primary Showcase & Content Grid (<section.impressum-section> — `Design für Werbung und Unterhaltun`)**:
   - Landmark `<section class="impressum-section">` rendering section `Design für Werbung und Unterhaltung` with copy *"Jede Website wird von Grund auf individuell konzipiert und passge"*, asset references (`logo.png (Logo)`, `banner-index.jpg (Willkommen Banner)`, `index-webseite.jpg (Titelbild Startseite)`, `index-design.jpg (Fotografie Startseite)`), and grid rule `custom-cursor.hovering { box-shadow: 0 0 18px var(--active-glow), 0 0 28px rgba(168, 85, 247, 0.6); }`.
4. **Interactive Detail & Feature Matrix (<section.impressum-section> — `Fotografie & Porträts`)**:
   - Landmark `<section class="impressum-section">` framing `Fotografie & Porträts` and `Über mich` (*"Neben Webseiten gestalten wir unter anderem Interfaces und Visual"*) with `#00f0ff` surface cards, `#a855f7` accents, and `cursor-logo.rotated { opacity: 1; }`.
5. **Colophon & Global Directory Footer (<footer.sound-control> — `https://www.gerd-web.de`)**:
   - Landmark `<footer class="sound-control">` anchoring `Gerd Web 3 Second - Design` footer links (`Home · Web · Plakate · Spiele · Foto`), copy *"Ob Smartphone, Tablet oder Desktop: Dank Responsive Design p"*, and `#e6edf8` structural dividers.
