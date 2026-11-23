---
title: "UI & UX Architecture: supermodels-phototypelabs-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: supermodels-phototypelabs-com

## Overview & Design Identity
- **Target**: `supermodels-phototypelabs-com` (**SUPERMODELS — Image, Video, Voice & Music, Pay Per Use**)
- **Production URL**: [https://supermodels.phototypelabs.com](https://supermodels.phototypelabs.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×2400px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#57d778`)
- **Summary**: SUPERMODELS is a creative platform for images, video, voice, music, and text with leading models. Pay per use, with no subscription.
- **Total Clean CSS Variables Extracted**: `123` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Manrope`
- **Body Font Stack**: `DM Sans`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 58.32px`, `line-height: 60.6528px`, `font-weight: 500`, `letter-spacing: -3.7908px`); CSS variables `--font-display: "Manrope", var(--font-sans)`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 74.88px`, `line-height: 79.3728px`, `font-weight: 500`, `letter-spacing: -4.1184px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--landing-body-size: .9375rem`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--font-mono: "IBM Plex Mono", "SF Mono", monospace`, `--landing-label-size: .75rem`, `--hero-brand-letter-spacing: 0.02em`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f7f6f2` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#171715` | live computed `header` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#57d778` | `var(--category-accent)` in `:root` |
| **Secondary / Muted Copy** | `#5f5f5a` | `var(--editorial-muted)` in `:root` |
| **Structural Hairline Border** | `#39352e` | `var(--workspace-dark-rule)` in `:root` |
| **Variable Token (`--editorial-ground`)** | `#ecebe7` | `var(--editorial-ground)` in `:root` |
| **Variable Token (`--editorial-paper-quiet`)** | `#efeee9` | `var(--editorial-paper-quiet)` in `:root` |
| **Variable Token (`--editorial-rule`)** | `#c9c8c3` | `var(--editorial-rule)` in `:root` |
| **Variable Token (`--workspace-sand`)** | `#ded5c5` | `var(--workspace-sand)` in `:root` |
| **Variable Token (`--workspace-sand-muted`)** | `#a9a08f` | `var(--workspace-sand-muted)` in `:root` |
| **Variable Token (`--surface-dark-muted`)** | `#b8af9e` | `var(--surface-dark-muted)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--site-frame` | `#000` | Color / Atmospheric Token |
| `--editorial-ground` | `#ecebe7` | Color / Atmospheric Token |
| `--editorial-paper` | `#f7f6f2` | Canvas / Surface Token |
| `--editorial-paper-quiet` | `#efeee9` | Canvas / Surface Token |
| `--editorial-ink` | `#171715` | Typography Ink Token |
| `--editorial-muted` | `#5f5f5a` | Color / Atmospheric Token |
| `--editorial-rule` | `#c9c8c3` | Color / Atmospheric Token |
| `--workspace-sand` | `#ded5c5` | Layout / Spatial Grid Token |
| `--workspace-sand-muted` | `#a9a08f` | Layout / Spatial Grid Token |
| `--workspace-dark-rule` | `#39352e` | Canvas / Surface Token |
| `--surface-light-text` | `var(--editorial-ink)` | Canvas / Surface Token |
| `--surface-light-muted` | `var(--editorial-muted)` | Canvas / Surface Token |
| `--surface-dark-text` | `var(--workspace-sand)` | Canvas / Surface Token |
| `--surface-dark-muted` | `#b8af9e` | Canvas / Surface Token |
| `--editorial-accent` | `#5f5f5a` | Brand / Palette Token |
| `--font-sans` | `"DM Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.editorial-header> — `supermodels-phototypelabs-com`)**:
   - Landmark `<header class="editorial-header">` (`1440x78px`) hosting `SUPERMODELS — Image, Video, Voice & ` navigation (`Models · Providers · Pricing · Examples · News`), DOM attributes (`data-landing-brand="SUPERMODELS"`, `data-landing-brand-weight="700"`, `data-landing-brand-spacing="0.02"`, `data-landing-font="Onest"`), and stylesheet rule `webkit-slider-runnable-track { background:0 0;height:.32rem }`.
2. **Hero Stage & Focal Lead (<section.editorial-hero> — `Your ideas. One creative platform.`)**:
   - Landmark `<section class="editorial-hero">` presenting display lead `Your ideas. One creative platform.` and copy excerpt *"Explore leading models for images, video, voice, music, and text."* over `#000000` canvas and `#f7f6f2` ink.
3. **Primary Showcase & Content Grid (<section.principles-section> — `Model choice`)**:
   - Landmark `<section class="principles-section platform-overview">` rendering section `Model choice` with copy *"Pick a model. Type a prompt. Get a result."*, asset references (`favicon.svg`, `favicon.png`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `moz-range-track { background:0 0;height:.32rem }`.
4. **Interactive Detail & Feature Matrix (<article.editorial-landing> — `Batch comparisons`)**:
   - Landmark `<article class="editorial-landing">` framing `Batch comparisons` and `Explore for free` (*"No subscription. Add wallet credit from $10 and see the estimated"*) with `#171715` surface cards, `#57d778` accents, and `active::-webkit-slider-thumb { transform:scale(1.24) }`.
5. **Colophon & Global Directory Footer (<footer.creative-footer> — `https://supermodels.phototypelabs.com`)**:
   - Landmark `<footer class="creative-footer">` anchoring `SUPERMODELS — Image, Video, Voic` footer links (`Models · Providers · Pricing · Examples · News`), copy *"Explore about 47 published models from OpenAI, Google, Anthr"*, and `#39352e` structural dividers.
