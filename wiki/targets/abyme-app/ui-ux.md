# UI & UX Architecture: abyme-app

## Overview & Design Identity
- **Target**: `abyme-app` (**Curiouser and Curiouser**)
- **Production URL**: [https://abyme.app](https://abyme.app)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0a0705` / `#2c130f`)
- **Summary**: An endless fall through a keyhole into hundreds of mathematical worlds, each holding the next. An art project by Dane Petersen.
- **Total Clean CSS Variables Extracted**: `61` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `IBM Plex Mono`
- **Body Font Stack**: `IM Fell English`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **Hero Display (`H1`)**: rule `.title` (`font-weight: 400`)
- **Section Heading (`H2`)**: rule `h2` (`letter-spacing: -0.005em`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `8px`, `3px`, `1.3em`, `var(--t-pica)`, `0.78em`)
- **Metadata & Labels**: rule `.label` (`letter-spacing: 0.16em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0a0705` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#15100b` | `var(--smoke)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1d0c0a` | `var(--cloth)` in `:root` |
| **Interactive Accent / Highlight** | `#2c130f` | `var(--cloth-hi)` in `:root` |
| **Secondary / Muted Copy** | `#efe5cf` | `var(--paper)` in `:root` |
| **Structural Hairline Border** | `#b4a689` | `var(--paper-dim)` in `:root` |
| **Variable Token (`--paper-faint`)** | `#8a7e69` | `var(--paper-faint)` in `:root` |
| **Variable Token (`--card`)** | `#e9ddc2` | `var(--card)` in `:root` |
| **Variable Token (`--card-ink`)** | `#2a1a10` | `var(--card-ink)` in `:root` |
| **Variable Token (`--card-dim`)** | `#6c5843` | `var(--card-dim)` in `:root` |
| **Variable Token (`--rubric`)** | `#8f2a1b` | `var(--rubric)` in `:root` |
| **Variable Token (`--gilt`)** | `#d8af5c` | `var(--gilt)` in `:root` |
| **Variable Token (`--lamp`)** | `#ffc46a` | `var(--lamp)` in `:root` |
| **Variable Token (`--brass`)** | `#a8834a` | `var(--brass)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#0a0705` | Typography Ink Token |
| `--smoke` | `#15100b` | Color / Atmospheric Token |
| `--cloth` | `#1d0c0a` | Color / Atmospheric Token |
| `--cloth-hi` | `#2c130f` | Color / Atmospheric Token |
| `--paper` | `#efe5cf` | Canvas / Surface Token |
| `--paper-dim` | `#b4a689` | Canvas / Surface Token |
| `--paper-faint` | `#8a7e69` | Canvas / Surface Token |
| `--card` | `#e9ddc2` | Color / Atmospheric Token |
| `--card-ink` | `#2a1a10` | Typography Ink Token |
| `--card-dim` | `#6c5843` | Color / Atmospheric Token |
| `--rubric` | `#8f2a1b` | Color / Atmospheric Token |
| `--gilt` | `#d8af5c` | Color / Atmospheric Token |
| `--gilt-dim` | `rgba(216, 175, 92, 0.42)` | Color / Atmospheric Token |
| `--gilt-faint` | `rgba(216, 175, 92, 0.17)` | Color / Atmospheric Token |
| `--lamp` | `#ffc46a` | Color / Atmospheric Token |
| `--brass` | `#a8834a` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.bar> — `abyme-app`)**:
   - Landmark `<header class="bar">` hosting `Curiouser and Curiouser` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-engine="three.js r170"`, `data-on="false"`, `data-do="record"`, `data-pace="slow"`), and stylesheet rule `root { padding-top:env(safe-area-inset-top);padding-bottom:env(safe-area-inset-... }`.
2. **Hero Stage & Focal Lead (<section.intro> — `Curiouser and Curiouser`)**:
   - Landmark `<section class="intro">` presenting display lead `Curiouser and Curiouser` and copy excerpt *"Would the fall never come to an end?"* over `#0a0705` canvas and `#efe5cf` ink.
3. **Primary Showcase & Content Grid (<section.plate> — `The shader`)**:
   - Landmark `<section class="plate">` rendering section `The shader` with copy *"An art project by Dane Petersen"*, asset references (`icon-180.png`, `three.module.min.js`, `UnrealBloomPass.js`, `Pass.js`), and grid rule `body { margin:0;font:14px system-ui;background:0a0705 }`.
4. **Interactive Detail & Feature Matrix (<section.help-sec> — `Dream a world`)**:
   - Landmark `<section class="help-sec help-fine">` framing `Dream a world` and `Breed with…` (*"Step in now, and let the room finish furnishing itself"*) with `#1d0c0a` surface cards, `#2c130f` accents, and `img { max-width:100% }`.
5. **Colophon & Global Directory Footer (<footer.ring> — `https://abyme.app`)**:
   - Landmark `<footer class="ring">` anchoring `Curiouser and Curiouser` footer links (`Overview · Index · Archive · About · Contact`), copy *"Click, or press any key. Tap to step in. The music begins as"*, and `#b4a689` structural dividers.
