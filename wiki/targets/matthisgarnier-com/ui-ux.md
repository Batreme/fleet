# UI & UX Architecture: matthisgarnier-com

## Overview & Design Identity
- **Target**: `matthisgarnier-com` (**Matthis Garnier · Head of Creative Engineering, Polymarket**)
- **Production URL**: [https://matthisgarnier.com](https://matthisgarnier.com)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fcfcfc` / `#ececec`)
- **Summary**: Matthis Garnier, Head of Creative Engineering at Polymarket, New York. Previously design director at SVZ and Hours Global; founded Cohem...
- **Total Clean CSS Variables Extracted**: `253` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `handFont`
- **Body Font Stack**: `handFont Fallback`
- **Monospace / Technical Font Stack**: `arealMono`
- **Hero Display (`H1`)**: rule `h1` (`font-size: 18px`, `letter-spacing: 0`, `font-weight: 500`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 13px`, `line-height: 1.4`, `letter-spacing: 0`, `font-weight: 500`)
- **Body Copy**: CSS variables `--vcr-tv-body: #d9d3c5`; rule `p` (`font-size: 12px`)
- **Metadata & Labels**: CSS variables `--vcr-tape-label: #efeadf`, `--mono-font: var(--font-areal), system-ui, sans-serif`, `--wm-mono: var(--font-areal-mono)`; rule `.meta` (`font-size: 11px`, `line-height: 1.25`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fcfcfc` | `var(--g-0)` in `:root` |
| **Primary Typography Ink** | `#fafafa` | `var(--g-1)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f3f3f3` | `var(--g-2)` in `:root` |
| **Interactive Accent / Highlight** | `#ececec` | `var(--g-3)` in `:root` |
| **Secondary / Muted Copy** | `#e2e2e2` | `var(--g-4)` in `:root` |
| **Structural Hairline Border** | `#d4d4d4` | `var(--g-5)` in `:root` |
| **Variable Token (`--g-6`)** | `#bcbcbc` | `var(--g-6)` in `:root` |
| **Variable Token (`--g-7`)** | `#8e8e8e` | `var(--g-7)` in `:root` |
| **Variable Token (`--g-8`)** | `#6a6a6a` | `var(--g-8)` in `:root` |
| **Variable Token (`--g-9`)** | `#474747` | `var(--g-9)` in `:root` |
| **Variable Token (`--g-10`)** | `#2a2a2a` | `var(--g-10)` in `:root` |
| **Variable Token (`--g-11`)** | `#181818` | `var(--g-11)` in `:root` |
| **Variable Token (`--g-12`)** | `#0a0a0a` | `var(--g-12)` in `:root` |
| **Variable Token (`--shade`)** | `#00000024` | `var(--shade)` in `:root` |
| **Variable Token (`--shade-deep`)** | `#00000038` | `var(--shade-deep)` in `:root` |
| **Variable Token (`--sticker-paper`)** | `#f7f4ec` | `var(--sticker-paper)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--g-0` | `#fcfcfc` | Color / Atmospheric Token |
| `--g-1` | `#fafafa` | Color / Atmospheric Token |
| `--g-2` | `#f3f3f3` | Color / Atmospheric Token |
| `--g-3` | `#ececec` | Color / Atmospheric Token |
| `--g-4` | `#e2e2e2` | Color / Atmospheric Token |
| `--g-5` | `#d4d4d4` | Color / Atmospheric Token |
| `--g-6` | `#bcbcbc` | Color / Atmospheric Token |
| `--g-7` | `#8e8e8e` | Color / Atmospheric Token |
| `--g-8` | `#6a6a6a` | Color / Atmospheric Token |
| `--g-9` | `#474747` | Color / Atmospheric Token |
| `--g-10` | `#2a2a2a` | Color / Atmospheric Token |
| `--g-11` | `#181818` | Color / Atmospheric Token |
| `--g-12` | `#0a0a0a` | Color / Atmospheric Token |
| `--shade` | `#00000024` | Color / Atmospheric Token |
| `--shade-deep` | `#00000038` | Color / Atmospheric Token |
| `--sticker-paper` | `#f7f4ec` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.topbar> — `matthisgarnier-com`)**:
   - Landmark `<nav class="topbar">` hosting `Matthis Garnier · Head of Creative E` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-theme="light"`, `data-three="off"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.xp .mecard { width:min(300px,100% - 32px) }`.
2. **Hero Stage & Focal Lead (<section.story-desk-module__g7DRpa__win> — `Matthis Garnier`)**:
   - Landmark `<section class="story-desk-module__g7DRpa__win story-desk-module__g7DRpa__cover">` presenting display lead `Matthis Garnier` and copy excerpt *"NYC 10:07 LA 07:07 PAR 16:07 TUL 10:07 NYC 10:07 LA 07:07 PAR 16:"* over `#fcfcfc` canvas and `#d4d4d4` ink.
3. **Primary Showcase & Content Grid (<section.story-desk-module__g7DRpa__win> — `Building for an information market`)**:
   - Landmark `<section class="story-desk-module__g7DRpa__win story-desk-module__g7DRpa__index">` rendering section `Building for an information market.` with copy *"Head of Creative Engineering at Polymarket"*, asset references (`7ebf22b5a21034f8-s.p.3strvg7o-g5v...`, `ABCArealMonoVariable-s.p.28z6jix4...`, `ABCArealVariable-s.p.0r-_z7ct5is3...`, `DaftFont-s.p.1r6c1opwgow9_.woff2`), and grid rule `button { opacity:.5;border-radius:9px;width:36px;height:36px;padding:0;transition... }`.
4. **Interactive Detail & Feature Matrix (<section.story-desk-module__g7DRpa__win> — `Posters`)**:
   - Landmark `<section class="story-desk-module__g7DRpa__win story-desk-module__g7DRpa__year">` framing `Posters` and `Experiments` (*"Founded Cohem, a creative and consulting studio for small and mid"*) with `#f3f3f3` surface cards, `#ececec` accents, and `button>span:first-child { border-radius:9px;width:36px;height:36px;display:block }`.
5. **Colophon & Global Directory Footer (<footer.taskbar> — `https://matthisgarnier.com`)**:
   - Landmark `<footer class="taskbar">` anchoring `Matthis Garnier · Head of Creati` footer links (`Overview · Index · Archive · About · Contact`), copy *"Finsweet Multidisciplinary Designer"*, and `#d4d4d4` structural dividers.
