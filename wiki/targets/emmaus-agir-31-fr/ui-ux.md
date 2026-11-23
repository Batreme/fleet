---
title: "UI & UX Architecture: emmaus-agir-31-fr"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: emmaus-agir-31-fr

## Overview & Design Identity
- **Target**: `emmaus-agir-31-fr` (**Emmaüs A.G.I.R. — Boutiques solidaires à Toulouse et autour**)
- **Production URL**: [https://emmaus-agir-31.fr/](https://emmaus-agir-31.fr/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f1ece1` / `#ebc017`)
- **Summary**: Donnez une seconde vie à vos objets. Emmaüs A.G.I.R. collecte, trie et revend vos dons dans six boutiques solidaires à Toulouse et autour...
- **Total Clean CSS Variables Extracted**: `70` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Bricolage Grotesque`
- **Body Font Stack**: `Bricolage Grotesque`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 164.8px`, `line-height: 138.432px`, `font-weight: 740`, `letter-spacing: -6.592px`); CSS variables `--fs-display: clamp(3.2rem,0.8rem + 7.2vw,11.5rem)`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 27px`, `line-height: 40.5px`, `font-weight: 700`); CSS variables `--fs-h2: clamp(2.5rem,1.3rem + 4.6vw,6.5rem)`; rule `.h2` (`font-size: clamp(1.5rem,8dvh,2.6rem)`)
- **Body Copy**: live computed `body` (`font-size: 18px`, `line-height: 27px`, `font-weight: 400`); CSS variables `--fs-body: clamp(1rem,0.95rem + 0.2vw,1.125rem)`; rule `p` (`font-size: var(--fs-lead)`, `line-height: 1.45`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 21px`, `font-weight: 400`); CSS variables `--fs-small: 0.9375rem`, `--fs-label: clamp(0.75rem,0.72rem + 0.12vw,0.8125rem)`; rule `.label` (`font-size: .6875rem`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f1ece1` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1b1b1b` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ebc017` | live computed `a` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ebc017` | live computed `a` `background-color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#5f5d57` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#d1cdc3` | `.menu__shop { border-top: #d1cdc3 }` |
| **Variable Token (`--fond-2`)** | `#e7e1d3` | `var(--fond-2)` in `:root` |
| **Variable Token (`--bleu`)** | `#33669b` | `var(--bleu)` in `:root` |
| **Variable Token (`--vert`)** | `#43744e` | `var(--vert)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--fond` | `#f1ece1` | Color / Atmospheric Token |
| `--fond-2` | `#e7e1d3` | Color / Atmospheric Token |
| `--gris` | `#1b1b1b` | Color / Atmospheric Token |
| `--gris-doux` | `#5f5d57` | Color / Atmospheric Token |
| `--ligne` | `rgba(27,27,27,0.18)` | Color / Atmospheric Token |
| `--jaune` | `#ebc017` | Color / Atmospheric Token |
| `--bleu` | `#33669b` | Color / Atmospheric Token |
| `--vert` | `#43744e` | Color / Atmospheric Token |
| `--ink` | `var(--gris)` | Typography Ink Token |
| `--header-h` | `clamp(56px,8vw,88px)` | Layout / Spatial Grid Token |
| `--radius-pill` | `999px` | Elevation / Border Token |
| `--tap` | `44px` | Dimension / Scale Token |
| `--z-flower` | `2` | Elevation / Border Token |
| `--z-guide` | `3` | Elevation / Border Token |
| `--z-scene` | `4` | Elevation / Border Token |
| `--z-scene-raised` | `5` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `emmaus-agir-31-fr`)**:
   - Landmark `<header class="header">` (`1440x88px`) hosting `Emmaüs A.G.I.R. — Boutiques solidair` navigation (`0 1 Accueil Accueil · 05 61 63 14 94 · 05 61 52 02 23 · 09 53 53 93 05 · 09 84 12 80 62`), DOM attributes (`data-next-head`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`), and stylesheet rule `.__className_2a1a39 { font-family:Bricolage Grotesque,Bricolage Grotesque Fallback;font-style:... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Seconde vie, seconde chance.`)**:
   - Landmark `<section class="hero">` presenting display lead `Seconde vie, seconde chance.` and copy excerpt *"ASSOCIATION GARONNAISE D’INSERTION PAR LA RÉCUPÉRATION"* over `#f1ece1` canvas and `#1b1b1b` ink.
3. **Primary Showcase & Content Grid (<section.activites> — `S e c o n d e v i e , s e c o n d `)**:
   - Landmark `<section class="activites">` rendering section `S e c o n d e v i e , s e c o n d e c h a n c e .` with copy *"Association Garonnaise d’Insertion par la Récupération"*, asset references (`logo.svg`, `favicon.ico`, `favicon-32x32.png`, `apple-icon-180x180.png`), and grid rule `.__className_ae301a { font-family:"Instrument Serif","Instrument Serif Fallback";font-weight:400 }`.
4. **Interactive Detail & Feature Matrix (<article.activites__text> — `Le parcours d’un don.`)**:
   - Landmark `<article class="activites__text is-active">` framing `Le parcours d’un don.` and `Réception des dons` (*"S e c o n d e v i e ,"*) with `#ebc017` surface cards, `#ebc017` accents, and `before { box-sizing:border-box }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://emmaus-agir-31.fr/`)**:
   - Landmark `<footer class="footer">` anchoring `Emmaüs A.G.I.R. — Boutiques soli` footer links (`0 1 Accueil Accueil · 05 61 63 14 94 · 05 61 52 02 23 · 09 53 53 93 05 · 09 84 12 80 62`), copy *"s e c o n d e c h a n c e ."*, and `#d1cdc3` structural dividers.
