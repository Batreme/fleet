---
title: "UI & UX Architecture: microdose-studio"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: microdose-studio

## Overview & Design Identity
- **Target**: `microdose-studio` (**Microdose Studio - Design & Development Agency for Startups**)
- **Production URL**: [https://microdose.studio/](https://microdose.studio/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#0000ff`)
- **Summary**: Microdose Studio helps tech startups turn ideas into products through strategy, brand and product design, React/Next.js development, and...
- **Total Clean CSS Variables Extracted**: `63` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 72px`, `line-height: 80px`, `font-weight: 400`, `letter-spacing: -4.32px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 72px`, `line-height: 80px`, `font-weight: 400`, `letter-spacing: -4.32px`); rule `h2` (`font-size: 26px`, `line-height: 42px`, `letter-spacing: -1.56px`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `body` (`font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0c152a` | live computed `button` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e8e8ec` | `var(--color-card-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#0000ff` | `.legal-block a:hover { color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#6b6c71` | `var(--color-muted)` in `:root` |
| **Structural Hairline Border** | `#eae5e5` | `var(--color-footer-border)` in `:root` (`rgba(116, 84, 84, 0.15)`) |
| **Variable Token (`--color-black`)** | `#19171b` | `var(--color-black)` in `:root` |
| **Variable Token (`--color-bg-dark`)** | `#121113` | `var(--color-bg-dark)` in `:root` |
| **Variable Token (`--color-blue-start`)** | `#1935d9` | `var(--color-blue-start)` in `:root` |
| **Variable Token (`--color-blue-end`)** | `#2f2be2` | `var(--color-blue-end)` in `:root` |
| **Variable Token (`--color-blue-border`)** | `#1f34c9` | `var(--color-blue-border)` in `:root` |
| **Variable Token (`--color-grey-cool`)** | `#818a94` | `var(--color-grey-cool)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-black` | `#19171b` | Canvas / Surface Token |
| `--color-dark` | `#0c152a` | Canvas / Surface Token |
| `--color-muted` | `#6b6c71` | Brand / Palette Token |
| `--color-white` | `#ffffff` | Canvas / Surface Token |
| `--color-bg-dark` | `#121113` | Canvas / Surface Token |
| `--color-card-bg` | `#e8e8ec` | Canvas / Surface Token |
| `--color-blue-start` | `#1935d9` | Brand / Palette Token |
| `--color-blue-end` | `#2f2be2` | Brand / Palette Token |
| `--color-blue-border` | `#1f34c9` | Brand / Palette Token |
| `--color-footer-border` | `rgba(116, 84, 84, 0.15)` | Brand / Palette Token |
| `--color-white-50` | `rgba(255, 255, 255, 0.5)` | Canvas / Surface Token |
| `--color-grey-cool` | `#818a94` | Brand / Palette Token |
| `--font-primary` | `'Geist', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif` | Brand / Palette Token |
| `--font-accent` | `'Metal', serif` | Brand / Palette Token |
| `--radius-lg` | `16px` | Elevation / Border Token |
| `--radius-xl` | `24px` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.nav> — `microdose-studio`)**:
   - Landmark `<nav class="nav blur-fade-in">` (`1440x80px`) hosting `Microdose Studio - Design & Developm` navigation (`microdose .studio · About us 01 · Case Studies 02 · Services 03 · Labs 04`), DOM attributes (`data-scroll-indicator="home"`, `data-consent="deny"`, `data-consent="accept"`, `data-chrome="nav"`), and stylesheet rule `after { margin: 0; padding: 0; box-sizing: border-box; }`.
2. **Hero Stage & Focal Lead (<section.hero> — `We build AI-first products for sta`)**:
   - Landmark `<section class="hero blur-fade-in">` presenting display lead `We build AI-first products for startups and enter...` and copy excerpt *"We use cookies to improve experience and performance of our websi"* over `#ffffff` canvas and `#0c152a` ink.
3. **Primary Showcase & Content Grid (<section.portfolio-carousel> — `W e b u i l d A I - f i r s t p r `)**:
   - Landmark `<section class="portfolio-carousel">` rendering section `W e b u i l d A I - f i r s t p r o d u c t s f o...` with copy *"Accepting new projects"*, asset references (`favicon-96x96.png`, `favicon.ico`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `selection { background-color: var(--color-blue-start); color: var(--color-white); te... }`.
4. **Interactive Detail & Feature Matrix (<section.about> — `O u r s e l e c t e d p r o j e c `)**:
   - Landmark `<section class="about">` framing `O u r s e l e c t e d p r o j e c t s .` and `M o b i l e A p p f o r H y p e r P e r s o n a l...` (*"Your Design & Dev Partner."*) with `#e8e8ec` surface cards, `#0000ff` accents, and `html { -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale;... }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://microdose.studio/`)**:
   - Landmark `<footer class="footer">` anchoring `Microdose Studio - Design & Deve` footer links (`microdose .studio · About us 01 · Case Studies 02 · Services 03 · Labs 04`), copy *"e n t e r p r i s e s ."*, and `#eae5e5` structural dividers.
