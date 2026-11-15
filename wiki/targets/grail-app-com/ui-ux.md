# UI & UX Architecture: grail-app-com

## Overview & Design Identity
- **Target**: `grail-app-com` (**Grail: Real-world quests, every day**)
- **Production URL**: [https://grail-app.com/](https://grail-app.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#c9a24a` / `#f2f2f7`)
- **Summary**: Grail pulls you out of autopilot with one real-world quest a day. Grow four stats: Strength, Intellect, Charisma, Wisdom. When you gradua...
- **Total Clean CSS Variables Extracted**: `83` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Switzer`
- **Body Font Stack**: `PP Pangaia`
- **Monospace / Technical Font Stack**: `SF Mono`
- **Hero Display (`H1`)**: rule `h1` (`font-size: 44px`, `line-height: 1.05`, `font-weight: 400`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `44px`, `14px`, `32px`, `clamp(46px,6vw,92px)`)
- **Body Copy**: CSS variables `--pill-body: #18181899`; rule `p` (`font-size: 14px`, `line-height: 1.45`)
- **Metadata & Labels**: CSS variables `--font-mono: "SF Mono", ui-monospace, "Menlo", monospace`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#c9a24a` | `var(--accent)` in `:root` |
| **Primary Typography Ink** | `#ffcdff` | `var(--pill-accent)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--bg-primary)` in `:root` |
| **Interactive Accent / Highlight** | `#f2f2f7` | `var(--bg-secondary)` in `:root` |
| **Secondary / Muted Copy** | `#000` | `var(--text-primary)` in `:root` |
| **Structural Hairline Border** | `#8e8e93` | `var(--text-secondary)` in `:root` |
| **Variable Token (`--pill-btn-bg`)** | `#ffffff24` | `var(--pill-btn-bg)` in `:root` |
| **Variable Token (`--pill-body`)** | `#18181899` | `var(--pill-body)` in `:root` |
| **Variable Token (`--bg-card`)** | `#00000008` | `var(--bg-card)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--accent` | `#c9a24a` | Brand / Palette Token |
| `--fill` | `0%` | Dimension / Scale Token |
| `--blurk` | `max(0, 1 - var(--g8off,0) * 4)` | Elevation / Border Token |
| `--out` | `clamp(0, calc((var(--g8morph,0) * 90 - var(--i,0)) / 6), 1)` | Design System Custom Token |
| `--tailx` | `calc(100% - 46px)` | Dimension / Scale Token |
| `--pill-accent` | `#ffcdff` | Brand / Palette Token |
| `--pill-btn-bg` | `#ffffff24` | Canvas / Surface Token |
| `--pill-btn-fg` | `#ffcdff` | Typography Ink Token |
| `--pill-body` | `#18181899` | Color / Atmospheric Token |
| `--pill-border` | `#ffffff24` | Elevation / Border Token |
| `--bg-primary` | `#fff` | Canvas / Surface Token |
| `--bg-secondary` | `#f2f2f7` | Canvas / Surface Token |
| `--bg-grouped` | `#f2f2f7` | Canvas / Surface Token |
| `--bg-card` | `#00000008` | Canvas / Surface Token |
| `--text-primary` | `#000` | Typography Ink Token |
| `--text-secondary` | `#8e8e93` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `grail-app-com`)**:
   - Landmark `<header class="lenis">` hosting `Grail: Real-world quests, every day` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-controls="true"`, `data-guild-title="true"`, `data-tile="true"`, `data-side="right"`), and stylesheet rule `._root_1bp3t_1 { color:efe9f2;font-family:var(--font-sans);--accent:c9a24a;background:000... }`.
2. **Hero Stage & Focal Lead (<section.lenis-stopped> — `R e c l a i m y o u r l i f e`)**:
   - Landmark `<section class="lenis-stopped">` presenting display lead `R e c l a i m y o u r l i f e` and copy excerpt *"One real-world quest a day. Four stats that go up when you do thi"* over `#c9a24a` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.home-root> — `Everyone's out living. You're watc`)**:
   - Landmark `<section class="home-root">` rendering section `Everyone's out living. You're watching them do it...` with copy *"Same week, over and over, until you can't tell them apart. You ke"*, asset references (`Fav.svg`, `Fav.png`, `Switzer-Variable.woff2`, `PPPangaia-Light.woff2`), and grid rule `._embed_1bp3t_12 { --accent:c9a24a;position:absolute;inset:0;overflow:hidden }`.
4. **Interactive Detail & Feature Matrix (<section.sr-only> — `Quest accepted. Clock's running.`)**:
   - Landmark `<section class="sr-only">` framing `Quest accepted. Clock's running.` and `Quest accepted. Clock’s running.` (*"Now there’s a clock on it. Forty-eight hours to go do the thing, "*) with `#fff` surface cards, `#f2f2f7` accents, and `._canvas_1bp3t_19 { touch-action:pan-y;width:100%;height:100%;display:block;position:absolut... }`.
5. **Colophon & Global Directory Footer (<footer> — `https://grail-app.com/`)**:
   - Landmark `<footer>` landmark anchoring `Grail: Real-world quests, every ` footer links (`Overview · Index · Archive · About · Contact`), copy *"Not 24, since a day is too easy to lose to work or weather o"*, and `#8e8e93` structural dividers.
