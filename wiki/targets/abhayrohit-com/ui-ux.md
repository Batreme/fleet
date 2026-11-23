---
title: "UI & UX Architecture: abhayrohit-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: abhayrohit-com

## Overview & Design Identity
- **Target**: `abhayrohit-com` (**Abhay Rohit — Creative Product Engineer**)
- **Production URL**: [https://abhayrohit.com/](https://abhayrohit.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#de3834` / `#ff0000`)
- **Summary**: Abhay Rohit is a creative product engineer in Indore, India, specializing in frontend engineering and interactive design with React, Next...
- **Total Clean CSS Variables Extracted**: `174` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `anton`
- **Body Font Stack**: `antonStudio`
- **Monospace / Technical Font Stack**: `jetbrainsMono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 338.4px`, `line-height: 338.4px`, `font-weight: 400`); CSS variables `--archive-display: "display", "display Fallback", Impact`, `--qi-font-display: "anton", "anton Fallback", Impact, Arial Narrow, sans-serif`, `--qi-font-studio-display: "antonStudio", "antonStudio Fallback"`; rule `h1` (`font-size: clamp(58px,8.8vw,144px)`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 150px`, `line-height: 150px`, `font-weight: 400`); CSS variables `--opening-subtitle: clamp(34.72px,3.224cqw,59.52px)`; rule `h2` (`letter-spacing: -.04em`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 16px`, `line-height: 1.75`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--archive-mono: "mono", "mono Fallback", Courier New`, `--qi-font-mono: "jetbrainsMono", ui-monospace, monospace`; rule `nav` (`font-size: 14px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#de3834` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#efeade` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#241910` | `var(--paper)` in `:root` |
| **Interactive Accent / Highlight** | `#ff0000` | `.PNc5aa_header nav a:hover { color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#919599` | `var(--qi-muted)` in `:root` |
| **Structural Hairline Border** | `#b83530` | `var(--editorial-rule)` in `:root` (`29291f36`) |
| **Variable Token (`--qi-studio`)** | `#a52d2b` | `var(--qi-studio)` in `:root` |
| **Variable Token (`--qi-ink`)** | `#07090d` | `var(--qi-ink)` in `:root` |
| **Variable Token (`--qi-hero-carmine`)** | `#c42d2a` | `var(--qi-hero-carmine)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--qi-studio` | `#a52d2b` | Color / Atmospheric Token |
| `--qi-ink` | `#07090d` | Typography Ink Token |
| `--qi-bone` | `#efeade` | Color / Atmospheric Token |
| `--qi-muted` | `#919599` | Color / Atmospheric Token |
| `--qi-carmine` | `#de3834` | Color / Atmospheric Token |
| `--qi-hero-carmine` | `#c42d2a` | Color / Atmospheric Token |
| `--s-3` | `16px` | Dimension / Scale Token |
| `--s-4` | `24px` | Dimension / Scale Token |
| `--s-6` | `64px` | Dimension / Scale Token |
| `--ease-out` | `cubic-bezier(.22, 1, .36, 1)` | Motion / Easing Token |
| `--t-fast` | `.18s` | Motion / Timing Token |
| `--sound-right` | `calc(12px + env(safe-area-inset-right))` | Dimension / Scale Token |
| `--sound-bottom` | `calc(16px + env(safe-area-inset-bottom))` | Dimension / Scale Token |
| `--sound-width` | `72px` | Layout / Spatial Grid Token |
| `--sound-height` | `66px` | Layout / Spatial Grid Token |
| `--sound-clear-inline` | `calc(var(--sound-right) + var(--sound-width) + 16px)` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.MLPEba_header> — `abhayrohit-com`)**:
   - Landmark `<header class="MLPEba_header">` (`1440x96px`) hosting `Abhay Rohit — Creative Product Engin` navigation (`01 Car care · 02 Schoolbus Karo · 03 Accounting · 04 Hyre Me · 05 Khajuraho Expo`), DOM attributes (`data-film-entry="cold-home"`, `data-preload-tier="desktop"`, `data-preload-bytes="153382"`, `data-scroll-motion="inertia"`), and stylesheet rule `.UOQEPW_process :after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.MLPEba_hero> — `A B H A Y R O H I T`)**:
   - Landmark `<section class="MLPEba_hero">` presenting display lead `A B H A Y R O H I T` and copy excerpt *"Creative mind. Engineer by craft."* over `#de3834` canvas and `#efeade` ink.
3. **Primary Showcase & Content Grid (<section.KKuYoa_variable> — `My first engineering job.`)**:
   - Landmark `<section class="KKuYoa_variable">` rendering section `My first engineering job.` with copy *"Drag the grip to explore; release to return home. Tap to visit th"*, asset references (`anton_full_entry_subset-s.p.0dq58...`, `anton_kinetic_margin-s.p.1o1u0v9k...`, `instrument_sans_latin_wdth_normal...`, `jetbrains_mono_latin_wght_normal_...`), and grid rule `.UOQEPW_process summary { cursor:pointer;-webkit-tap-highlight-color:0000;list-style:none }`.
4. **Interactive Detail & Feature Matrix (<article.rojSVa_variable> — `Where care begins.`)**:
   - Landmark `<article class="rojSVa_variable">` framing `Where care begins.` and `A clearer experience for patients.` (*"Gaming. A miniature world of music, gaming, photography and train"*) with `#241910` surface cards, `#ff0000` accents, and `process summary::-webkit-details-... { display:none }`.
5. **Colophon & Global Directory Footer (<footer.jFvPUW_footer> — `https://abhayrohit.com/`)**:
   - Landmark `<footer class="jFvPUW_footer">` anchoring `Abhay Rohit — Creative Product E` footer links (`01 Car care · 02 Schoolbus Karo · 03 Accounting · 04 Hyre Me · 05 Khajuraho Expo`), copy *"Engineer by craft."*, and `#b83530` structural dividers.
