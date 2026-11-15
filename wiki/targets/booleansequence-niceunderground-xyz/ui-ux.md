# UI & UX Architecture: booleansequence-niceunderground-xyz

## Overview & Design Identity
- **Target**: `booleansequence-niceunderground-xyz` (**booleanSequence · generative art by niceunderground**)
- **Production URL**: [https://booleansequence.niceunderground.xyz/](https://booleansequence.niceunderground.xyz/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#ff0000` / `#000000`)
- **Summary**: booleanSequence by niceunderground: generative visuals built on two values and nothing else. A modern yin and yang of contrasts that swap...
- **Total Clean CSS Variables Extracted**: `10` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `JetBrains Mono`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `13px`, `clamp(5rem,21vw,22rem)`, `12px`, `14px`)
- **Section Heading (`H2`)**: CSS variables `--rule-h2: clamp(2rem, 4.6vw, 5.6rem)`; rule `.h2` (`font-size: clamp(2.1rem,5vw,6rem)`)
- **Body Copy**: rule `p` (`font-size: clamp(15px,1.05vw,17px)`, `line-height: 1.4`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `13px`, `clamp(5rem,21vw,22rem)`, `12px`, `14px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ff0000` | `var(--err)` in `:root` |
| **Primary Typography Ink** | `#0000ff` | `var(--pt)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ffffff` | `var(--pf)` in `:root` |
| **Interactive Accent / Highlight** | `#000000` | `<meta name="theme-color" content="#000000">` in `dom.html` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--err` | `#ff0000` | Color / Atmospheric Token |
| `--fd` | `"Archivo", "Helvetica Neue", Arial, sans-serif` | Dimension / Scale Token |
| `--fm` | `"JetBrains Mono", ui-monospace, "SFMono-Regular", Menlo, monospace` | Design System Custom Token |
| `--pad` | `clamp(16px, 2.2vw, 40px)` | Layout / Spatial Grid Token |
| `--hud` | `clamp(30px, 2.4vw, 38px)` | Dimension / Scale Token |
| `--ease` | `cubic-bezier(.7, 0, .2, 1)` | Motion / Easing Token |
| `--wp` | `.1em` | Dimension / Scale Token |
| `--rule-h2` | `clamp(2rem, 4.6vw, 5.6rem)` | Typography / Scale Token |
| `--pt` | `#0000ff` | Color / Atmospheric Token |
| `--pf` | `#ffffff` | Color / Atmospheric Token |
| `--booleansequence--bg` | `#ff0000` | Canvas Substrate (from `var(--err)` in `:root`) |
| `--booleansequence--ink` | `#ffffff` | Primary Typography Ink (stylesheet-derived) |
| `--booleansequence--surface` | `#ffffff` | Surface Substrate (stylesheet-derived) |
| `--booleansequence--accent` | `#000000` | Interactive Accent (stylesheet-derived) |
| `--booleansequence--muted` | `#ffffff` | Secondary Ink (stylesheet-derived) |
| `--booleansequence--border` | `#ffffff` | Structural Border (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.hud> — `booleansequence-niceunderground-xyz`)**:
   - Landmark `<header class="hud">` hosting `booleanSequence · generative art by ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-live`, `data-magnetic`, `data-set="plus"`, `data-set="bin"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.hero> — `boolean Sequence`)**:
   - Landmark `<section class="hero">` presenting display lead `boolean Sequence` and copy excerpt *"two values, nothing else"* over `#ff0000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.statement> — `01 Concept`)**:
   - Landmark `<section class="statement">` rendering section `01 Concept` with copy *"niceunderground generative visuals"*, asset references (`llms.txt`, `favicon.svg`, `favicon-32.png`, `favicon-48.png`), and grid rule `html { -webkit-text-size-adjust:100% }`.
4. **Interactive Detail & Feature Matrix (<section.above> — `Seen from above, it looks like a s`)**:
   - Landmark `<section class="above">` framing `Seen from above, it looks like a society.` and `One rule, four verbs.` (*"generative visuals"*) with `#ffffff` surface cards, `#000000` accents, and `html.lenis body { height:auto }`.
5. **Colophon & Global Directory Footer (<footer.foot> — `https://booleansequence.niceunderground.xyz/`)**:
   - Landmark `<footer class="foot">` anchoring `booleanSequence · generative art` footer links (`Overview · Index · Archive · About · Contact`), copy *"A modern yin and yang. Two values, nothing else."*, and `#ffffff` structural dividers.
