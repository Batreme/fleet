---
title: "UI & UX Architecture: departmentofemotions-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: departmentofemotions-com

## Overview & Design Identity
- **Target**: `departmentofemotions-com` (**Department of Emotions**)
- **Production URL**: [https://departmentofemotions.com/](https://departmentofemotions.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×1656px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f9f9f3` canvas, `#000000` ink, `#212c24` accent)
- **Summary**: Explore your emotions with an interactive feeling wheel, body-language examples, somatic sensations, and behavioral experiences.
- **Total Clean CSS Variables Extracted**: `11` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Gilda Display`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 42px`, `line-height: 47.04px`, `font-weight: 400`, `letter-spacing: -0.6px`); rule `h1` (`font-size: 48px`, `line-height: 1.12`, `letter-spacing: -.6px`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 11px`, `line-height: 13.2px`, `font-weight: 650`, `letter-spacing: 1.6px`); rule `h2` (`font-size: 11px`, `letter-spacing: 1.4px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 14px`, `line-height: 1.7`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f9f9f3` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `html { background: #ffffff }` |
| **Interactive Accent / Highlight** | `#212c24` | live computed `button` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#212c24` | live computed `button` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#6f7f74` | `.explorer-page button:focus-vis... { border-color: #6f7f74 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `oklch(28% .022 154)` | Typography Ink Token |
| `--muted` | `oklch(49% .016 154)` | Color / Atmospheric Token |
| `--line` | `oklch(86% .012 125)` | Color / Atmospheric Token |
| `--paper` | `oklch(98% .008 105)` | Canvas / Surface Token |
| `--desktop-wheel-size` | `clamp(74vw, 120svh, 92vw)` | Layout / Spatial Grid Token |
| `--mobile-wheel-size` | `min(160vw, 820px)` | Layout / Spatial Grid Token |
| `--landscape-wheel-size` | `clamp(560px, 160svh, 92vw)` | Layout / Spatial Grid Token |
| `--lab-toolbar-height` | `0px` | Layout / Spatial Grid Token |
| `--phone-wheel-size` | `213.75vw` | Layout / Spatial Grid Token |
| `--wheel-muted-opacity` | `0.38` | Design System Custom Token |
| `--wheel-fade-duration` | `180ms` | Motion / Easing Token |
| `--departmentofemot-bg` | `#f9f9f3` | Canvas Substrate (from live computed `html` `background-color` (`computed_styles.json`)) |
| `--departmentofemot-ink` | `#000000` | Primary Typography Ink (computed-derived) |
| `--departmentofemot-surface` | `#ffffff` | Surface Substrate (computed-derived) |
| `--departmentofemot-accent` | `#212c24` | Interactive Accent (computed-derived) |
| `--departmentofemot-muted` | `#212c24` | Secondary Ink (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.lab-switcher> — `departmentofemotions-com`)**:
   - Landmark `<nav class="lab-switcher">` (`400x42px`) hosting `Department of Emotions` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-wheel="feelings"`, `data-moving="true"`, `data-sector-index="0"`, `data-emotion="Anger"`), and stylesheet rule `.privacy-page { max-width:648px;margin-inline:auto;padding:64px 24px;color:212c24;font:1... }`.
2. **Hero Stage & Focal Lead (<section.wheel-workspace> — `Joy`)**:
   - Landmark `<section class="wheel-workspace">` presenting display lead `Joy` and copy excerpt *"A bright sense of pleasure, connection, or delight in being alive"* over `#f9f9f3` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.experience-section> — `How it may feel in the body`)**:
   - Landmark `<section class="experience-section">` rendering section `How it may feel in the body` with copy *"01 Warmth spreading through the chest."*, asset references (`favicon.ico`, `favicon-32.png`, `favicon.svg`, `apple-touch-icon.png`), and grid rule `.privacy-brand { display:inline-flex;align-items:center;gap:5px;font-weight:650;font-size... }`.
4. **Interactive Detail & Feature Matrix (<section.experience-section:nth(2)> — `Possible body language & behaviors`)**:
   - Landmark `<section class="experience-section">` framing `Possible body language & behaviors` and `Warmth spreading through the chest.` (*"Warmth spreading through the chest."*) with `#ffffff` surface cards, `#212c24` accents, and `.privacy-page h1 { margin:40px 0 24px;font:400 42px/1.2 Gilda Display,Georgia,serif }`.
5. **Colophon & Global Directory Footer (<footer.sidebar-footer> — `https://departmentofemotions.com/`)**:
   - Landmark `<footer class="sidebar-footer">` anchoring `Department of Emotions` footer links (`Overview · Index · Archive · About · Contact`), copy *"02 A light, energetic feeling in the body."*, and `#6f7f74` structural dividers.
