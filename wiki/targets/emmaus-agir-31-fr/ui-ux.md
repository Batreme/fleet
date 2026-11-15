# UI & UX Architecture: emmaus-agir-31-fr

## Overview & Design Identity
- **Target**: `emmaus-agir-31-fr` (**Emmaüs A.G.I.R. — Boutiques solidaires à Toulouse et autour**)
- **Production URL**: [https://emmaus-agir-31.fr/](https://emmaus-agir-31.fr/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f1ece1` / `#5f5d57`)
- **Summary**: Donnez une seconde vie à vos objets. Emmaüs A.G.I.R. collecte, trie et revend vos dons dans six boutiques solidaires à Toulouse et autour...
- **Total Clean CSS Variables Extracted**: `70` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Bricolage Grotesque`
- **Body Font Stack**: `Bricolage Grotesque Fallback`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--fs-display: clamp(3.2rem,0.8rem + 7.2vw,11.5rem)`
- **Section Heading (`H2`)**: CSS variables `--fs-h2: clamp(2.5rem,1.3rem + 4.6vw,6.5rem)`; rule `.h2` (`font-size: clamp(1.5rem,8dvh,2.6rem)`)
- **Body Copy**: CSS variables `--fs-body: clamp(1rem,0.95rem + 0.2vw,1.125rem)`; rule `p` (`font-size: var(--fs-lead)`, `line-height: 1.45`)
- **Metadata & Labels**: CSS variables `--fs-small: 0.9375rem`, `--fs-label: clamp(0.75rem,0.72rem + 0.12vw,0.8125rem)`; rule `.label` (`font-size: .6875rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f1ece1` | `var(--fond)` in `:root` |
| **Primary Typography Ink** | `#e7e1d3` | `var(--fond-2)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1b1b1b` | `var(--gris)` in `:root` |
| **Interactive Accent / Highlight** | `#5f5d57` | `var(--gris-doux)` in `:root` |
| **Secondary / Muted Copy** | `#ebc017` | `var(--jaune)` in `:root` |
| **Structural Hairline Border** | `#33669b` | `var(--bleu)` in `:root` |
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
   - Landmark `<header class="header">` hosting `Emmaüs A.G.I.R. — Boutiques solidair` navigation (`0 1 Accueil Accueil · 05 61 63 14 94 · 05 61 52 02 23 · 09 53 53 93 05 · 09 84 12 80 62`), DOM attributes (`data-next-head`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`), and stylesheet rule `.__className_2a1a39 { font-family:Bricolage Grotesque,Bricolage Grotesque Fallback;font-style:... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `S e c o n d e v i e , s e c o n d `)**:
   - Landmark `<section class="hero">` presenting display lead `S e c o n d e v i e , s e c o n d e c h a n c e .` and copy excerpt *"Chargement du site"* over `#f1ece1` canvas and `#1b1b1b` ink.
3. **Primary Showcase & Content Grid (<section.activites> — `Le parcours d’un don.`)**:
   - Landmark `<section class="activites">` rendering section `Le parcours d’un don.` with copy *"0 1 Accueil Accueil"*, asset references (`logo.svg`, `favicon.ico`, `favicon-32x32.png`, `apple-icon-180x180.png`), and grid rule `.__className_ae301a { font-family:"Instrument Serif","Instrument Serif Fallback";font-weight:400 }`.
4. **Interactive Detail & Feature Matrix (<article.activites__text> — `Réception des dons`)**:
   - Landmark `<article class="activites__text is-active">` framing `Réception des dons` and `Tri par catégorie` (*"0 2 Activités Activités"*) with `#1b1b1b` surface cards, `#5f5d57` accents, and `before { box-sizing:border-box }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://emmaus-agir-31.fr/`)**:
   - Landmark `<footer class="footer">` anchoring `Emmaüs A.G.I.R. — Boutiques soli` footer links (`0 1 Accueil Accueil · 05 61 63 14 94 · 05 61 52 02 23 · 09 53 53 93 05 · 09 84 12 80 62`), copy *"Activités Activités"*, and `#33669b` structural dividers.
