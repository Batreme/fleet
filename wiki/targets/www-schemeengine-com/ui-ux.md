---
title: "UI & UX Architecture: www-schemeengine-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-schemeengine-com

## Overview & Design Identity
- **Target**: `www-schemeengine-com` (**Home - Scheme Engine**)
- **Production URL**: [https://www.schemeengine.com/](https://www.schemeengine.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#0082f3`)
- **Summary**: Scheme Engine is a BIPOC-owned production company and TV/Film studio founded to provoke and reimagine the status quo.
- **Total Clean CSS Variables Extracted**: `55` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Neuepower Ultra`
- **Body Font Stack**: `neue-haas-grotesk-display`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 64px`, `line-height: 57.6px`, `font-weight: 400`); rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 24px`, `line-height: 30px`, `font-weight: 700`); rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 20.8px`, `font-weight: 500`); rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 20.8px`, `font-weight: 500`); CSS variables `--font-family-mono: Menlo, Monaco, Consolas, "Droid Sans Mono", monospace`; rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `button` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#333333` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#ebebeb` | `var(--text-color)` in `:root` |
| **Structural Hairline Border** | `#3898ec` | `.w-select:focus { border-color: #3898ec }` |
| **Variable Token (`--purple`)** | `#1d0524` | `var(--purple)` in `:root` |
| **Variable Token (`--white`)** | `#fef9ef` | `var(--white)` in `:root` |
| **Variable Token (`--brown`)** | `#b47054` | `var(--brown)` in `:root` |
| **Variable Token (`--main-light`)** | `#d18221` | `var(--main-light)` in `:root` |
| **Variable Token (`--background-color`)** | `#140d16` | `var(--background-color)` in `:root` |
| **Variable Token (`--title-background-color`)** | `#111111` | `var(--title-background-color)` in `:root` |
| **Variable Token (`--widget-color`)** | `#424242` | `var(--widget-color)` in `:root` |
| **Variable Token (`--hover-color`)** | `#4f4f4f` | `var(--hover-color)` in `:root` |
| **Variable Token (`--focus-color`)** | `#595959` | `var(--focus-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--purple` | `#1d0524` | Color / Atmospheric Token |
| `--white` | `#fef9ef` | Canvas / Surface Token |
| `--black` | `#000` | Canvas / Surface Token |
| `--brown` | `#b47054` | Color / Atmospheric Token |
| `--main-dark` | `#000000` | Canvas / Surface Token |
| `--main-light` | `#D18221` | Canvas / Surface Token |
| `--visual-hidden` | `0` | Design System Custom Token |
| `--main-space` | `10vw` | Layout / Spatial Grid Token |
| `--background-color` | `#140D16` | Canvas / Surface Token |
| `--book-width` | `35vmin` | Layout / Spatial Grid Token |
| `--text-color` | `#ebebeb` | Typography Ink Token |
| `--title-background-color` | `#111111` | Canvas / Surface Token |
| `--title-text-color` | `#ebebeb` | Typography Ink Token |
| `--widget-color` | `#424242` | Brand / Palette Token |
| `--hover-color` | `#4f4f4f` | Brand / Palette Token |
| `--focus-color` | `#595959` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `www-schemeengine-com`)**:
   - Landmark `<header class="header">` (`1440x104px`) hosting `Home - Scheme Engine` navigation (`D i r e c t o r s · W o r k · F i l m & t v · C o n t a c t`), DOM attributes (`data-wf-domain="www.schemeengine.com"`, `data-wf-page="6856ec97d986105f5589bbe0"`, `data-wf-site="6856ec97d986105f5589bbd7"`, `data-word="Directors"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.section> — `We create from the culture we live`)**:
   - Landmark `<section class="section">` presenting display lead `We create from the culture we live.` and copy excerpt *"Scheme Engine is a culture-first production company championing t"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.section:nth(2)> — `Scheme Engine is a culture-first p`)**:
   - Landmark `<section class="section">` rendering section `Scheme Engine is a culture-first production comp` with copy *"Our award-winning directors and creatives work across formats, al"*, asset references (`cdn.prod.website-files.com`, `schemeengine.webflow.shared.3fbb9...`, `soy0bmb.js`, `68b845cb16daf25e488bd7a5_scheme-e...`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.section:nth(3)> — `Our award-winning directors and cr`)**:
   - Landmark `<section class="section">` framing `Our award-winning directors and creatives work a` and `Impactful, resonant storytelling is rooted in li` (*"Impactful, resonant storytelling is rooted in lived experience. W"*) with `#333333` surface cards, `#0082f3` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.wf-active> — `https://www.schemeengine.com/`)**:
   - Landmark `<footer class="wf-active">` anchoring `Home - Scheme Engine` footer links (`D i r e c t o r s · W o r k · F i l m & t v · C o n t a c t`), copy *"The future does not look like the past. Neither do we."*, and `#3898ec` structural dividers.
