---
title: "UI & UX Architecture: vault-hyperiux-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: vault-hyperiux-com

## Overview & Design Identity
- **Target**: `vault-hyperiux-com` (**Hyperiux Vault - React & Next.js Interaction Effects.**)
- **Production URL**: [https://vault.hyperiux.com](https://vault.hyperiux.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#111111` / `#ff5f00`)
- **Summary**: Start with 70+ free source-first effects. Upgrade to Pro for 180+ effects.
- **Total Clean CSS Variables Extracted**: `159` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `aeonikPro`
- **Body Font Stack**: `avenirNext`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 92.16px`, `line-height: 103.219px`, `font-weight: 400`, `letter-spacing: -3.2256px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`; rule `h1` (`font-size: 2.5rem`, `line-height: 1.2`, `letter-spacing: -.025em`, `font-weight: 700`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 66.24px`, `line-height: 76.176px`, `font-weight: 400`, `letter-spacing: -2.3184px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 1.75rem`, `line-height: 1.3`, `font-weight: 700`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#111111` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ff5f00` | `var(--primary)` in `:root` |
| **Secondary / Muted Copy** | `#d2d2d2` | `var(--muted-on-dark)` in `:root` |
| **Structural Hairline Border** | `#272727` | `var(--blog-border-color)` in `:root` |
| **Variable Token (`--secondary`)** | `#d9d9d9` | `var(--secondary)` in `:root` |
| **Variable Token (`--primary-hover`)** | `#ff9253` | `var(--primary-hover)` in `:root` |
| **Variable Token (`--dark-card`)** | `#161616` | `var(--dark-card)` in `:root` |
| **Variable Token (`--border`)** | `#bcbcbc` | `var(--border)` in `:root` |
| **Variable Token (`--light-grey`)** | `#939393` | `var(--light-grey)` in `:root` |
| **Variable Token (`--light`)** | `#f4f4f4` | `var(--light)` in `:root` |
| **Variable Token (`--ink`)** | `#1d1d1d` | `var(--ink)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--vault-ctl-h` | `max(44px,calc(var(--hx-vw,1vw) * 1.725 + 1rem))` | Dimension / Scale Token |
| `--cvw` | `min(1vw,15.36px)` | Layout / Spatial Grid Token |
| `--background` | `#111` | Canvas / Surface Token |
| `--white` | `#fff` | Canvas / Surface Token |
| `--foreground` | `var(--white)` | Typography Ink Token |
| `--secondary` | `#d9d9d9` | Brand / Palette Token |
| `--primary` | `#ff5f00` | Brand / Palette Token |
| `--primary-hover` | `#ff9253` | Brand / Palette Token |
| `--dark-card` | `#161616` | Canvas / Surface Token |
| `--border` | `#bcbcbc` | Elevation / Border Token |
| `--muted-on-dark` | `#d2d2d2` | Canvas / Surface Token |
| `--muted` | `var(--muted-on-dark)` | Design System Custom Token |
| `--grey` | `#272727` | Color / Atmospheric Token |
| `--light-grey` | `#939393` | Canvas / Surface Token |
| `--light` | `#f4f4f4` | Canvas / Surface Token |
| `--ink` | `#1d1d1d` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.z-900> — `vault-hyperiux-com`)**:
   - Landmark `<nav class="z-900 top-0">` (`1440x102px`) hosting `Hyperiux Vault - React & Next.js Int` navigation (`Docs D o c s Docs · Blog B l o g Blog`), DOM attributes (`data-sidebar="expanded"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `root { --g-shift:0px }`.
2. **Hero Stage & Focal Lead (<section.relative> — `The Interaction Layer Your Website`)**:
   - Landmark `<section class="relative z-10">` presenting display lead `The Interaction Layer Your Website Is Missing.` and copy excerpt *"This website uses cookies. Learn More"* over `#111111` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.section-x> — `The Interaction Layer Your Website`)**:
   - Landmark `<section class="section-x text-ink">` rendering section `The Interaction Layer Your Website Is Missing .` with copy *"Source-first scroll systems, cursor effects, text reveals, page t"*, asset references (`homepage-hero.webp`, `45c5b69ac3104145.css`, `b68a34d2a9030372.css`, `ee41bfcc83e4e14b.css`), and grid rule `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<article.flex> — `Source-first scroll systems, curso`)**:
   - Landmark `<article class="flex flex-col">` framing `Source-first scroll systems, cursor effects, tex` and `Read Docs R e a d D o c s Read Docs` (*"Read Docs R e a d D o c s Read Docs"*) with `#000000` surface cards, `#ff5f00` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.z-200> — `https://vault.hyperiux.com`)**:
   - Landmark `<footer class="z-200 overflow-x-clip">` anchoring `Hyperiux Vault - React & Next.js` footer links (`Docs D o c s Docs · Blog B l o g Blog`), copy *"Browse All Effects B r o w s e A l l E f f e c t s Browse Al"*, and `#272727` structural dividers.
