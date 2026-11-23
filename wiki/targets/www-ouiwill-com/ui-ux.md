---
title: "UI & UX Architecture: www-ouiwill-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: www-ouiwill-com

## Overview & Design Identity
- **Target**: `www-ouiwill-com` (**Oui Will · Brand Transformation & Digital Experiences**)
- **Production URL**: [https://www.ouiwill.com/](https://www.ouiwill.com/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#33ff96`)
- **Summary**: Oui Will is an independent digital agency shaping ambitious brands through strategy, identity, digital experiences, and technology.
- **Total Clean CSS Variables Extracted**: `106` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `base`
- **Body Font Stack**: `base`
- **Monospace / Technical Font Stack**: `mono`
- **Hero Display (`H1`)**: observed font-size ladder: `60px`, `18px`, `14px`, `12px`, `2.66667vw`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 60px`, `line-height: 63px`, `font-weight: 400`, `letter-spacing: -1.2px`)
- **Body Copy**: live computed `body` (`font-size: 14px`, `line-height: 14px`, `font-weight: 400`); rule `p` (`font-size: 1.2rem`, `line-height: 1.3`, `letter-spacing: -.02em`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 14px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#060606` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#00ffff` | `.HLP_GD .GRI-CL div:before { background: #00ffff }` |
| **Interactive Accent / Highlight** | `#33ff96` | `.aBtn.A { background-color: #33ff96 }` |
| **Secondary / Muted Copy** | `#878787` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#d9d9d9` | `.aBtn-dkB { border: #d9d9d9 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--csk-rev` | `"csk-ffec67d3-72a4-404e-9353-3cf2742cdeb5"` | Design System Custom Token |
| `--mobileMax` | `834` | Design System Custom Token |
| `--resp` | `1194` | Design System Custom Token |
| `--padgrid` | `4rem` | Layout / Spatial Grid Token |
| `--multi` | `calc(((100vw - 1440px) / 1440 * -5))` | Dimension / Scale Token |
| `--prg1` | `1` | Design System Custom Token |
| `--prg2` | `1` | Design System Custom Token |
| `--bndB` | `calc(100% * var(--bnd,.15))` | Dimension / Scale Token |
| `--bndS` | `calc(100% + 2 * var(--bndB))` | Dimension / Scale Token |
| `--hovS` | `calc(var(--hovt,.7) * var(--hovd,1))` | Design System Custom Token |
| `--hovO` | `min(0, var(--hovS))` | Design System Custom Token |
| `--hovd` | `-1` | Design System Custom Token |
| `--padgut` | `calc(var(--gutgrid) + var(--padgrid))` | Layout / Spatial Grid Token |
| `--padgut-s` | `calc(var(--gutgrid) + var(--padgrid-s))` | Layout / Spatial Grid Token |
| `--sizegrid` | `calc(100vw - ((var(--padgut)) * 2))` | Layout / Spatial Grid Token |
| `--gutgrid` | `1rem` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.nav> — `www-ouiwill-com`)**:
   - Landmark `<nav class="nav">` (`1440x900px`) hosting `Oui Will · Brand Transformation & Di` navigation (`Home Home · Work Work · About About · Careers Careers · Awwwards`), DOM attributes (`data-deck="[("lg":"/uploads/fina..."`, `data-req="true"`, `data-engine="three.js r182 webgpu"`, `data-id="contact"`), and stylesheet rule `root { --csk-rev:"csk-ffec67d3-72a4-404e-9353-3cf2742cdeb5" }`.
2. **Hero Stage & Focal Lead (<section.home_intro> — `Shaping the next generation of bra`)**:
   - Landmark `<section class="home_intro">` presenting display lead `Shaping the next generation of brands that matter...` and copy excerpt *"We use essential cookies to make this site work. Analytics and ad"* over `#ffffff` canvas and `#060606` ink.
3. **Primary Showcase & Content Grid (<section.home_reel> — `Selected Work Selected Work`)**:
   - Landmark `<section class="home_reel GRI-vw">` rendering section `Selected Work Selected Work` with copy *"Shaping the next generation of brands that matter."*, asset references (`favicon.svg`, `favicon.ico`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `after { box-sizing:border-box }`.
4. **Interactive Detail & Feature Matrix (<section.home_aboutlog> — `About`)**:
   - Landmark `<section class="home_aboutlog GRI">` framing `About` and `Oura` (*"Play Showreel Play Showreel"*) with `#00ffff` surface cards, `#33ff96` accents, and `html { -webkit-text-size-adjust:none;-moz-text-size-adjust:none;text-size-adjus... }`.
5. **Colophon & Global Directory Footer (<footer.foot> — `https://www.ouiwill.com/`)**:
   - Landmark `<footer class="foot">` anchoring `Oui Will · Brand Transformation ` footer links (`Home Home · Work Work · About About · Careers Careers · Awwwards`), copy *"0 0 : 0 0 / 0 0 : 0 0"*, and `#d9d9d9` structural dividers.
