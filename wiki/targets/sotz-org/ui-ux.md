# UI & UX Architecture: sotz-org

## Overview & Design Identity
- **Target**: `sotz-org` (**Shout out to Zanzibar**)
- **Production URL**: [https://sotz.org/](https://sotz.org/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#b9ae95` canvas, `#2b2f33` ink, `#8a7f68` accent)
- **Summary**: S h o u t o u t t o Z a n z i b a r :
- **Total Clean CSS Variables Extracted**: `13` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Caveat`
- **Body Font Stack**: `Oswald`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(22px, 4.2vw, 54px)`, `line-height: 1.05`, `letter-spacing: .04em`, `font-weight: 700`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(18px, 2.6vw, 33px)`, `letter-spacing: .06em`, `font-weight: 500`)
- **Body Copy**: rule `p` (`font-size: clamp(11px, 1.35vw, 17px)`, `letter-spacing: .02em`, `font-weight: 300`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(13px, 1.4vw, 17px)`, `clamp(24px, 3vw, 38px)`, `clamp(12px, 1.2vw, 14px)`, `clamp(22px, 4.2vw, 54px)`, `clamp(18px, 2.6vw, 33px)`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#b9ae95` | `.site-footer { border-top: #b9ae95 }` |
| **Primary Typography Ink** | `#e9e2d3` | `.site-footer { background: #e9e2d3 }` |
| **Elevated Surface / Card Substrate** | `#4a4233` | `.site-footer { color: #4a4233 }` |
| **Interactive Accent / Highlight** | `#8a7f68` | `.site-footer .ftag { color: #8a7f68 }` |
| **Secondary / Muted Copy** | `#8a6b47` | `.site-footer .flinks a:focus-vi... { border-color: #8a6b47 }` |
| **Structural Hairline Border** | `#2b2f33` | `.stage { background: #2b2f33 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--dd` | `0s` | Motion / Timing Token |
| `--breath-time` | `5.2s` | Motion / Timing Token |
| `--breath-delay` | `-.9s` | Motion / Easing Token |
| `--breath-x` | `1.5px` | Dimension / Scale Token |
| `--breath-y` | `-2.5px` | Dimension / Scale Token |
| `--sd` | `4.2s` | Motion / Timing Token |
| `--sdd` | `0s` | Motion / Timing Token |
| `--fx` | `-15.405954996532616px` | Dimension / Scale Token |
| `--fy` | `-20.362394431859627px` | Dimension / Scale Token |
| `--fd` | `6.658141834401523s` | Motion / Timing Token |
| `--fdd` | `-0.2258515335672815s` | Motion / Timing Token |
| `--gd` | `2.658352322306388s` | Motion / Timing Token |
| `--gdd` | `-2.123038911815748s` | Motion / Timing Token |
| `--sotz-org-bg` | `#b9ae95` | Canvas Substrate (from `.site-footer { border-top: #b9ae95 }`) |
| `--sotz-org-ink` | `#2b2f33` | Primary Typography Ink (stylesheet-derived) |
| `--sotz-org-surface` | `#4a4233` | Surface Substrate (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.headline> — `sotz-org`)**:
   - Landmark `<header class="headline">` hosting `Shout out to Zanzibar` navigation (`Home · About Us · Pictures · Writings · Projects`), DOM attributes (`data-story="mission"`, `data-story="tanzania"`, `data-story="work"`, `data-story="school"`), and stylesheet rule `.site-footer .flinks { display: flex; flex-wrap: wrap; justify-content: center; gap: clamp(14px... }`.
2. **Hero Stage & Focal Lead (<article.story-panel> — `S h o u t o u t t o Z a n z i b a `)**:
   - Landmark `<article class="story-panel">` presenting display lead `S h o u t o u t t o Z a n z i b a r :` and copy excerpt *"Where every small hand holds a big dream — beneath Kilimanjaro’s "* over `#b9ae95` canvas and `#2b2f33` ink.
3. **Primary Showcase & Content Grid (<article.story-panel> — `No Pity but for the Future of Chil`)**:
   - Landmark `<article class="story-panel">` rendering section `No Pity but for the Future of Children` with copy *"EXPLORE OUR STORY →"*, asset references (`sotz_logo.png`, `fonts.googleapis.com`, `fonts.gstatic.com`, `css2`), and grid rule `.site-footer .flinks a:focus-visible { border-color: 8a6b47; color: 4a4233; }`.
4. **Interactive Detail & Feature Matrix (<article.story-panel> — `Our Story`)**:
   - Landmark `<article class="story-panel">` framing `Our Story` and `Mission` (*"Shout out to Zanzibar"*) with `#4a4233` surface cards, `#8a7f68` accents, and `.stage-art { position: absolute; inset: 0; }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://sotz.org/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Shout out to Zanzibar` footer links (`Home · About Us · Pictures · Writings · Projects`), copy *"SOTZ, Shout out to Zanzibar is the non-profit organization d"*, and `#2b2f33` structural dividers.
