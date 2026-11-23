---
title: "UI & UX Architecture: templates-preview-oxvo-app_t-oxvo-original-studio-max-commerce-3d-latest"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: templates-preview-oxvo-app_t-oxvo-original-studio-max-commerce-3d-latest

## Overview & Design Identity
- **Target**: `templates-preview-oxvo-app_t-oxvo-original-studio-max-commerce-3d-latest` (**SOLARA HALO S1 · Sound with presence.**)
- **Production URL**: [https://templates-preview.oxvo.app/t/oxvo-original-studio-max-commerce-3d/latest/#/](https://templates-preview.oxvo.app/t/oxvo-original-studio-max-commerce-3d/latest/#/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0b0c0f` canvas, `#f9f6ef` ink, `#b29af3` accent)
- **Summary**: Explore SOLARA HALO S1: a portable spatial speaker with a tactile acoustic shell. Choose a finish and try the local reservation preview.
- **Total Clean CSS Variables Extracted**: `92` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geist Variable`
- **Body Font Stack**: `Geist Variable`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 69.12px`, `line-height: 67.7376px`, `font-weight: 750`, `letter-spacing: -3.8016px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 69.12px`, `line-height: 67.7376px`, `font-weight: 750`, `letter-spacing: -3.8016px`); rule `h2` (`font-size: 23px`, `letter-spacing: -.04em`, `font-weight: 800`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: 11px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--default-mono-font-family: var(--font-mono)`, `--materials-caption-h: 57px`, `--materials-caption-gap: 12px`; rule `small` (`font-size: 10px`, `letter-spacing: .12em`, `font-weight: 600`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0b0c0f` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f9f6ef` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#101114` | live computed `header` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#b29af3` | `var(--studio-accent)` in `:root` |
| **Secondary / Muted Copy** | `#b2b1b8` | `var(--studio-muted)` in `:root` |
| **Structural Hairline Border** | `#48434e` | `var(--commerce-border)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background` | `oklch(100% 0 0)` | Canvas / Surface Token |
| `--foreground` | `oklch(14.5% 0 0)` | Typography Ink Token |
| `--card` | `oklch(100% 0 0)` | Color / Atmospheric Token |
| `--card-foreground` | `oklch(14.5% 0 0)` | Typography Ink Token |
| `--popover` | `oklch(100% 0 0)` | Color / Atmospheric Token |
| `--popover-foreground` | `oklch(14.5% 0 0)` | Typography Ink Token |
| `--primary` | `oklch(20.5% 0 0)` | Brand / Palette Token |
| `--primary-foreground` | `oklch(98.5% 0 0)` | Typography Ink Token |
| `--secondary` | `oklch(97% 0 0)` | Brand / Palette Token |
| `--secondary-foreground` | `oklch(20.5% 0 0)` | Typography Ink Token |
| `--muted` | `oklch(97% 0 0)` | Color / Atmospheric Token |
| `--muted-foreground` | `oklch(55.6% 0 0)` | Typography Ink Token |
| `--accent` | `oklch(97% 0 0)` | Brand / Palette Token |
| `--accent-foreground` | `oklch(20.5% 0 0)` | Typography Ink Token |
| `--destructive` | `oklch(57.7% .245 27.325)` | Color / Atmospheric Token |
| `--border` | `oklch(92.2% 0 0)` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `templates-preview-oxvo-app_t-oxvo-original-studio-max-commerce-3d-latest`)**:
   - Landmark `<header class="site-header">` (`1280x62px`) hosting `SOLARA HALO S1 · Sound with presence` navigation (`The idea · Design · Finishes · Specifications`), DOM attributes (`data-first-load="done"`, `data-first-load-path="cold@4131"`, `data-oxvo-mounted-static-preview-router`, `data-product-runtime-ready="false"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.immersive-hero> — `SOUND THAT HOLDS THE ROOM.`)**:
   - Landmark `<section class="immersive-hero">` presenting display lead `SOUND THAT HOLDS THE ROOM.` and copy excerpt *"Preparing your experience"* over `#0b0c0f` canvas and `#f9f6ef` ink.
3. **Primary Showcase & Content Grid (<section.content-band> — `WRAPPED AROUND AIR.`)**:
   - Landmark `<section class="content-band promise-band">` rendering section `WRAPPED AROUND AIR.` with copy *"Portable spatial speaker"*, asset references (`index-B571lmvU.js`, `index-CiVtvupN.css`, `geist-latin-wght-normal-Dm3htQBi....`, `PersistentProductCanvas-m78oPoe0.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<article.sr-only> — `TACTILE BY DESIGN.`)**:
   - Landmark `<article class="sr-only">` framing `TACTILE BY DESIGN.` and `BUILT FOR THE SECOND ROOM.` (*"Use the left and right arrow keys to turn the product, up and dow"*) with `#101114` surface cards, `#b29af3` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://templates-preview.oxvo.app/t/oxvo-original-studio-max-commerce-3d/latest/#/`)**:
   - Landmark `<footer class="site-footer">` anchoring `SOLARA HALO S1 · Sound with pres` footer links (`The idea · Design · Finishes · Specifications`), copy *"A portable spatial speaker tuned for wide projection and dai"*, and `#48434e` structural dividers.
