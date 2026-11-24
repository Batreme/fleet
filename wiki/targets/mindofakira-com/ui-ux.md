---
title: "UI & UX Architecture: mindofakira-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: mindofakira-com

## Overview & Design Identity
- **Target**: `mindofakira-com` (**Mind of Akira**)
- **Production URL**: [http://mindofakira.com](http://mindofakira.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#e9e7e1` / `#2bd96b`)
- **Summary**: Mind of Akira: graphic designer working where streetwear, gaming culture and music meet. Branding, apparel, cover art, type and streaming...
- **Total Clean CSS Variables Extracted**: `35` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Archivo`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 128px`, `line-height: 108.8px`, `font-weight: 900`, `letter-spacing: -5.76px`); CSS variables `--f-display: "Archivo", "Arial Black", "Helvetica Neue", Arial, sans-serif`; rule `h1` (`font-size: var(--s1)`, `line-height: 1.15`, `letter-spacing: -0.01em`, `font-weight: 500`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 216px`, `line-height: 177.12px`, `font-weight: 900`, `letter-spacing: -8.64px`); rule `h2` (`font-size: var(--s1)`, `letter-spacing: -0.01em`, `font-weight: 700`)
- **Body Copy**: live computed `body` (`font-size: 18px`, `line-height: 27px`, `font-weight: 400`); CSS variables `--f-body: "Archivo", "Helvetica Neue", Arial, sans-serif`; rule `body` (`font-size: var(--s0)`, `line-height: 1.5`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 18px`, `line-height: 27px`, `font-weight: 400`); CSS variables `--f-mono: "JetBrains Mono", ui-monospace, "SFMono-Regular", Menlo, monospace`; rule `.mono` (`font-size: var(--s-1)`, `letter-spacing: 0.04em`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#e9e7e1` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#131216` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#3ddc84` | `.dot { background: #3ddc84 }` |
| **Interactive Accent / Highlight** | `#2bd96b` | `.arc-hud #arcTarget { color: #2bd96b }` |
| **Secondary / Muted Copy** | `#8f8b98` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#e9e8e1` | `var(--line)` in `:root` (`rgba(236, 235, 228, 0.14)`) |
| **Variable Token (`--bg`)** | `#0c0b0f` | `var(--bg)` in `:root` |
| **Variable Token (`--bg-2`)** | `#15131a` | `var(--bg-2)` in `:root` |
| **Variable Token (`--fg`)** | `#ecebe4` | `var(--fg)` in `:root` |
| **Variable Token (`--accent`)** | `#5b6bff` | `var(--accent)` in `:root` |
| **Variable Token (`--accent-ink`)** | `#f4f3ff` | `var(--accent-ink)` in `:root` |
| **Variable Token (`--vinyl`)** | `#050407` | `var(--vinyl)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#0c0b0f` | Canvas / Surface Token |
| `--bg-2` | `#15131a` | Canvas / Surface Token |
| `--fg` | `#ecebe4` | Typography Ink Token |
| `--muted` | `#8f8b98` | Color / Atmospheric Token |
| `--line` | `rgba(236, 235, 228, 0.14)` | Color / Atmospheric Token |
| `--accent` | `#5b6bff` | Brand / Palette Token |
| `--accent-ink` | `#f4f3ff` | Typography Ink Token |
| `--vinyl` | `#050407` | Color / Atmospheric Token |
| `--f-display` | `"Archivo", "Arial Black", "Helvetica Neue", Arial, sans-serif` | Dimension / Scale Token |
| `--f-body` | `"Archivo", "Helvetica Neue", Arial, sans-serif` | Dimension / Scale Token |
| `--f-mono` | `"JetBrains Mono", ui-monospace, "SFMono-Regular", Menlo, monospace` | Typography / Scale Token |
| `--s-1` | `clamp(0.75rem, 0.7rem + 0.2vw, 0.8125rem)` | Dimension / Scale Token |
| `--s0` | `clamp(1rem, 0.95rem + 0.25vw, 1.125rem)` | Dimension / Scale Token |
| `--s1` | `clamp(1.375rem, 1.1rem + 1.2vw, 2rem)` | Dimension / Scale Token |
| `--s2` | `clamp(2rem, 1.3rem + 3.2vw, 4rem)` | Dimension / Scale Token |
| `--s3` | `clamp(3.2rem, 1rem + 10vw, 11rem)` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.top> — `mindofakira-com`)**:
   - Landmark `<header class="top">` (`1440x68px`) hosting `Mind of Akira` navigation (`Work · About · Services · Contact`), DOM attributes (`data-cursor="Play"`, `data-cursor="Enter"`, `data-cursor="Go"`, `data-cursor="Go"`), and stylesheet rule `after { box-sizing: border-box; }`.
2. **Hero Stage & Focal Lead (<section.hero> — `MIND OF AKIRA`)**:
   - Landmark `<section class="hero">` presenting display lead `MIND OF AKIRA` and copy excerpt *"MOA-001 SIDE A / SIDE B ℗ 2026"* over `#e9e7e1` canvas and `#131216` ink.
3. **Primary Showcase & Content Grid (<section.intro> — `Visuals for streetwear, gaming and`)**:
   - Landmark `<section class="intro wrap">` rendering section `Visuals for streetwear, gaming and music that fee...` with copy *"Available for projects"*, asset references (`favicon.svg`, `fonts.googleapis.com`, `fonts.gstatic.com`, `css2`), and grid rule `html { scroll-behavior: smooth; -webkit-text-size-adjust: 100%; }`.
4. **Interactive Detail & Feature Matrix (<article.tape-note> — `Photoshop and Illustrator, cracked`)**:
   - Landmark `<article class="tape-note">` framing `Photoshop and Illustrator, cracked open.` and `Mind of Akira starts.` (*"Groove pitch ≈ 0.1 mm"*) with `#3ddc84` surface cards, `#2bd96b` accents, and `canvas { max-width: 100%; display: block; }`.
5. **Colophon & Global Directory Footer (<footer.foot> — `http://mindofakira.com`)**:
   - Landmark `<footer class="foot wrap">` anchoring `Mind of Akira` footer links (`Work · About · Services · Contact`), copy *"Every groove is a waveform. Every Akira project starts the s"*, and `#e9e8e1` structural dividers.
