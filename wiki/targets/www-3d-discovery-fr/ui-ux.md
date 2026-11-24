---
title: "UI & UX Architecture: www-3d-discovery-fr"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-3d-discovery-fr

## Overview & Design Identity
- **Target**: `www-3d-discovery-fr` (**3D Discovery · Exploring New Dimensions**)
- **Production URL**: [https://www.3d-discovery.fr/](https://www.3d-discovery.fr/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ebebeb` / `#f59e0b`)
- **Summary**: Turn your spaces, projects and products into immersive web experiences: 3D exploration, content and interaction in one place to showcase,...
- **Total Clean CSS Variables Extracted**: `81` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Sora`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 80px`, `line-height: 76px`, `font-weight: 500`, `letter-spacing: -1.6px`); rule `,.h1` (`font-size: 2.25rem`, `line-height: 1.1`, `letter-spacing: -.025em`, `font-weight: 700`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 80px`, `line-height: 76px`, `font-weight: 500`, `letter-spacing: -1.6px`); rule `,.h2` (`font-size: 1.875rem`, `line-height: 1.1`, `letter-spacing: -.025em`, `font-weight: 700`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--tra-body-h: 16rem`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ebebeb` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1a1a1a` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e2e2e2` | `var(--bg-elevated)` in `:root` |
| **Interactive Accent / Highlight** | `#f59e0b` | `.badge--solid.badge--warning { background: #f59e0b }` |
| **Secondary / Muted Copy** | `#666666` | `var(--input-placeholder)` in `:root` |
| **Structural Hairline Border** | `#d4d4d4` | `var(--border-default)` in `:root` |
| **Variable Token (`--color-primary-light`)** | `#2e2e2e` | `var(--color-primary-light)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--sg-grade` | `url(#sg-grade)` | Design System Custom Token |
| `--color-primary` | `#1a1a1a` | Brand / Palette Token |
| `--color-primary-light` | `#2e2e2e` | Canvas / Surface Token |
| `--color-primary-dark` | `#1a1a1a` | Canvas / Surface Token |
| `--color-secondary` | `#1a1a1a` | Brand / Palette Token |
| `--header-height` | `64px` | Layout / Spatial Grid Token |
| `--header-height-mobile` | `56px` | Layout / Spatial Grid Token |
| `--container-padding` | `1.5rem` | Layout / Spatial Grid Token |
| `--transition-fast` | `.15s ease` | Motion / Easing Token |
| `--transition-base` | `.2s ease` | Motion / Easing Token |
| `--transition-slow` | `.3s ease` | Motion / Easing Token |
| `--transition-theme` | `.2s ease` | Brand / Palette Token |
| `--z-header` | `30` | Layout / Spatial Grid Token |
| `--z-modal` | `50` | Elevation / Border Token |
| `--z-tooltip` | `70` | Elevation / Border Token |
| `--bg-body` | `#ebebeb` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `www-3d-discovery-fr`)**:
   - Landmark `<header class="header">` (`1440x66px`) hosting `3D Discovery · Exploring New Dimensi` navigation (`Solutions · Experiences · Features · Blog`), DOM attributes (`data-theme="light"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.sg-section> — `TURN YOUR SPACES INTO IMMERSIVE EX`)**:
   - Landmark `<section class="sg-section">` presenting display lead `TURN YOUR SPACES INTO IMMERSIVE EXPERIENCES` and copy excerpt *"3D DISCOVERY · ©2026"* over `#ebebeb` canvas and `#1a1a1a` ink.
3. **Primary Showcase & Content Grid (<section.sg-section--seq> — `Turn your spaces into immersive ex`)**:
   - Landmark `<section class="sg-section sg-section--seq">` rendering section `Turn your spaces into immersive experiences` with copy *"3D Discovery · ©2026"*, asset references (`83afe278b6a6bb3c-s.p.0q-301v4kxxn...`, `c41ca59f1c34ba31-s.p.0xxb547n1hn7...`, `0ghcmdv7avfm..css`, `04vxxuqck~drg.css`), and grid rule `html:focus-within { scroll-behavior:smooth }`.
4. **Interactive Detail & Feature Matrix (<section.sg-solutions> — `Choose your field`)**:
   - Landmark `<section class="sg-section sg-solutions">` framing `Choose your field` and `Seeing is understanding` (*"Exploring new dimensions"*) with `#e2e2e2` surface cards, `#f59e0b` accents, and `body { min-height:100vh;line-height:1.5 }`.
5. **Colophon & Global Directory Footer (<footer.sg-footer> — `https://www.3d-discovery.fr/`)**:
   - Landmark `<footer class="sg-footer">` anchoring `3D Discovery · Exploring New Dim` footer links (`Solutions · Experiences · Features · Blog`), copy *"A single web experience for 3D exploration, content and inte"*, and `#d4d4d4` structural dividers.
