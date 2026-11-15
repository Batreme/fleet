# UI & UX Architecture: www-raomuhammadhamza-tech

## Overview & Design Identity
- **Target**: `www-raomuhammadhamza-tech` (**Rao Muhammad Hamza, AI Engineer**)
- **Production URL**: [https://www.raomuhammadhamza.tech/](https://www.raomuhammadhamza.tech/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0f1220` / `#f4e7e2`)
- **Summary**: Rao Muhammad Hamza, AI Engineer. RAG pipelines, LLM orchestration and agentic workflows, built to hold up in production.
- **Total Clean CSS Variables Extracted**: `27` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Space Grotesk`
- **Body Font Stack**: `Space Mono`
- **Monospace / Technical Font Stack**: `Space Mono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `11px`, `12px`, `clamp(15px,1.45vw,21px)`, `19px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `11px`, `12px`, `clamp(15px,1.45vw,21px)`, `19px`)
- **Body Copy**: rule `p` (`letter-spacing: .16em`)
- **Metadata & Labels**: CSS variables `--d-mono: "Space Mono", ui-monospace, monospace`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0f1220` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#ff9ebb` | `var(--screen)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1b1f33` | `var(--screen-ink)` in `:root` |
| **Interactive Accent / Highlight** | `#f4e7e2` | `var(--text)` in `:root` |
| **Secondary / Muted Copy** | `#b9b2c4` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#1a1a26` | `var(--d-surf)` in `:root` |
| **Variable Token (`--tv-edge`)** | `#ff9ebb33` | `var(--tv-edge)` in `:root` |
| **Variable Token (`--tv-bg`)** | `#161a30db` | `var(--tv-bg)` in `:root` |
| **Variable Token (`--tv-bg`)** | `#0c0e1ce6` | `var(--tv-bg)` in `:root` |
| **Variable Token (`--tv-glow`)** | `#ffffff08` | `var(--tv-glow)` in `:root` |
| **Variable Token (`--tv-glow`)** | `#ff9ebb12` | `var(--tv-glow)` in `:root` |
| **Variable Token (`--tv-glow`)** | `#00000073` | `var(--tv-glow)` in `:root` |
| **Variable Token (`--scan`)** | `#ffffff09` | `var(--scan)` in `:root` |
| **Variable Token (`--grid-line`)** | `#ffffff0f` | `var(--grid-line)` in `:root` |
| **Variable Token (`--d-surf2`)** | `#222232` | `var(--d-surf2)` in `:root` |
| **Variable Token (`--d-line`)** | `#ffffff14` | `var(--d-line)` in `:root` |
| **Variable Token (`--d-ink`)** | `#e9e3ef` | `var(--d-ink)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#0f1220` | Typography Ink Token |
| `--screen` | `#ff9ebb` | Color / Atmospheric Token |
| `--screen-ink` | `#1b1f33` | Typography Ink Token |
| `--text` | `#f4e7e2` | Typography Ink Token |
| `--muted` | `#b9b2c4` | Color / Atmospheric Token |
| `--tv-edge` | `#ff9ebb33` | Color / Atmospheric Token |
| `--tv-bg` | `linear-gradient(180deg, #161a30db, #0c0e1ce6)` | Canvas / Surface Token |
| `--tv-glow` | `inset 0 0 0 1px #ffffff08, inset 0 0 22px #ff9ebb12, 0 12px 40px #00000073` | Color / Atmospheric Token |
| `--scan` | `repeating-linear-gradient(0deg, #ffffff09 0 1px, transparent 1px 3px)` | Color / Atmospheric Token |
| `--tv-radius` | `12px` | Elevation / Border Token |
| `--grid-line` | `linear-gradient(#ffffff0f, #ffffff0f)` | Layout / Spatial Grid Token |
| `--sheet-bottom` | `84px` | Dimension / Scale Token |
| `--d-surf` | `#1a1a26` | Color / Atmospheric Token |
| `--d-surf2` | `#222232` | Color / Atmospheric Token |
| `--d-line` | `#ffffff14` | Color / Atmospheric Token |
| `--d-ink` | `#e9e3ef` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.ui> — `www-raomuhammadhamza-tech`)**:
   - Landmark `<header class="ui sig">` hosting `Rao Muhammad Hamza, AI Engineer` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-sound="on"`, `data-sound="off"`, `data-go="projects"`, `data-go="experience"`), and stylesheet rule `font-face { font-family:Space Mono;src:url(/fonts/SpaceMono-400.woff2)format("woff2"... }`.
2. **Hero Stage & Focal Lead (<section.surface> — `R a o M u h a m m a d H a m z a`)**:
   - Landmark `<section class="surface desk">` presenting display lead `R a o M u h a m m a d H a m z a` and copy excerpt *"$ python train.py --model hamza-1 --data ./room"* over `#0f1220` canvas and `#f4e7e2` ink.
3. **Primary Showcase & Content Grid (<article.case> — `Projects`)**:
   - Landmark `<article class="case">` rendering section `Projects` with copy *"step 0/6000 · 0.0k tok/s · gpu 0%"*, asset references (`favicon.svg`, `SpaceGrotesk-Variable.woff2`, `index.58LUSp4D.css`, `edi-poster.webp`), and grid rule `body { color:f4e7e2;background:0f1220;height:100%;font-family:Space Grotesk,sys... }`.
4. **Interactive Detail & Feature Matrix (<article.case> — `EDI`)**:
   - Landmark `<article class="case">` framing `EDI` and `ResumeWesume` (*"Drag to look around"*) with `#1b1f33` surface cards, `#f4e7e2` accents, and `.loader.done { opacity:0;visibility:hidden }`.
5. **Colophon & Global Directory Footer (<footer.train-chart> — `https://www.raomuhammadhamza.tech/`)**:
   - Landmark `<footer class="train-chart">` anchoring `Rao Muhammad Hamza, AI Engineer` footer links (`Overview · Index · Archive · About · Contact`), copy *"I build AI that ships."*, and `#1a1a26` structural dividers.
