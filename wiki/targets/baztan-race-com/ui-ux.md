---
title: "UI & UX Architecture: baztan-race-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: baztan-race-com

## Overview & Design Identity
- **Target**: `baztan-race-com` (**Baztan Race**)
- **Production URL**: [https://baztan-race.com](https://baztan-race.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#dcf241` accent)
- **Summary**: Venez affronter la route mythique de la vallée du Baztan entre Bayonne et Pampelune. Entre cols somptueux et forêts mystérieuses, vivez l...
- **Total Clean CSS Variables Extracted**: `126` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Apple Color Emoji`
- **Body Font Stack**: `Apple Color Emoji`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-4xl: 3.5rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 4rem`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 220px`, `line-height: 220px`, `font-weight: 400`); CSS variables `--text-2xl: 2.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 3rem`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: 14px`, `font-weight: 300`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono",`, `--text-xs: 0.875rem`, `--text-xs--line-height: calc(1 / 0.75)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#eeeeee` | `.wpml-ls-legacy-dropdown a:hover { background: #eeeeee }` |
| **Interactive Accent / Highlight** | `#dcf241` | `var(--m2ccb-link)` in `:root` |
| **Secondary / Muted Copy** | `#979797` | `var(--color-text-secondary)` in `:root` |
| **Structural Hairline Border** | `#dcf241` | `var(--m2ccb-border)` in `:root` |
| **Variable Token (`--m2ccb-bg`)** | `#1d1d1b` | `var(--m2ccb-bg)` in `:root` |
| **Variable Token (`--m2ccb-text`)** | `#f4f2e9` | `var(--m2ccb-text)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--m2ccb-bg` | `#1d1d1b` | Canvas / Surface Token |
| `--m2ccb-text` | `#f4f2e9` | Typography Ink Token |
| `--m2ccb-primary-bg` | `#f4f2e9` | Canvas / Surface Token |
| `--m2ccb-primary-text` | `#1d1d1b` | Typography Ink Token |
| `--m2ccb-secondary-bg` | `#1d1d1b` | Canvas / Surface Token |
| `--m2ccb-secondary-text` | `#f4f2e9` | Typography Ink Token |
| `--m2ccb-link` | `#dcf241` | Typography Ink Token |
| `--m2ccb-border` | `#dcf241` | Elevation / Border Token |
| `--m2ccb-switch-on` | `#dcf241` | Color / Atmospheric Token |
| `--m2ccb-focus` | `#dcf241` | Color / Atmospheric Token |
| `--m2ccb-radius` | `8px` | Elevation / Border Token |
| `--m2ccb-btn-radius` | `6px` | Elevation / Border Token |
| `--m2ccb-bar` | `1200px` | Dimension / Scale Token |
| `--m2ccb-box` | `440px` | Dimension / Scale Token |
| `--m2ccb-font` | `inherit` | Typography / Scale Token |
| `--m2ccb-scale` | `1` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.main-header> — `baztan-race-com`)**:
   - Landmark `<header class="main-header top-0">` (`1440x87px`) hosting `Baztan Race` navigation (`L’épreuve · Les parcours · Galerie · Infos pratiques · Français`), DOM attributes (`data-rocket-prefetch`, `data-rocket-preload`, `data-nowprocket`, `data-cfasync="false"`), and stylesheet rule `m2ccb:focus { outline:none }`.
2. **Hero Stage & Focal Lead (<section.hero-full> — `Sur les traces du basajaun`)**:
   - Landmark `<section class="hero-full z-100">` presenting display lead `Sur les traces du basajaun` and copy excerpt *"MERCI POUR CETTE 1ÈRE ÉDITION !"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.text-intro> — `Sur les traces du B a s a j a u n`)**:
   - Landmark `<section class="text-intro py-8">` rendering section `Sur les traces du B a s a j a u n` with copy *"Revivez la 1ère édition Voir l'aftermovie"*, asset references (`fonts.googleapis.com`, `fonts.gstatic.com`, `connect.facebook.net`, `matomo.mak2com.fr`), and grid rule `.m2ccb-ph a { color:var(--m2ccb-link, inherit);text-decoration:underline;text-underlin... }`.
4. **Interactive Detail & Feature Matrix (<section.title-section> — `Choisis ta course`)**:
   - Landmark `<section class="title-section relative">` framing `Choisis ta course` and `BAZTAN REAL #1` (*"Une cyclosportive unique, exigeante et inoubliable, au cœur des c"*) with `#eeeeee` surface cards, `#dcf241` accents, and `.m2ccb-ph a:hover { text-decoration-thickness:.125em }`.
5. **Colophon & Global Directory Footer (<footer.bg-dark-1> — `https://baztan-race.com`)**:
   - Landmark `<footer class="bg-dark-1 pb-16">` anchoring `Baztan Race` footer links (`L’épreuve · Les parcours · Galerie · Infos pratiques · Français`), copy *"Ligne de vie basque et chemin de pèlerinage vers Compostelle"*, and `#dcf241` structural dividers.
