# UI & UX Architecture: twohalves-co

## Overview & Design Identity
- **Target**: `twohalves-co` (**Two Halves — design & development studio, Cairo**)
- **Production URL**: [https://twohalves.co/](https://twohalves.co/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#f2e9e2`)
- **Summary**: We design and build websites people remember — motion, 3D and stories — for brands in Egypt and everywhere.
- **Total Clean CSS Variables Extracted**: `27` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Cutive Mono`
- **Body Font Stack**: `Cutive Mono Fallback`
- **Monospace / Technical Font Stack**: `Cutive Mono`
- **Hero Display (`H1`)**: CSS variables `--font-display-src: "Cutive Mono", "Cutive Mono Fallback"`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `15px`, `13px`, `13.9px`, `.9em`, `12.5px`)
- **Body Copy**: CSS variables `--font-body-src: "aileron", "aileron Fallback"`; rule `p` (`font-size: clamp(20px,1.9vw,30px)`, `line-height: 1.3`)
- **Metadata & Labels**: rule `small` (`font-size: .55em`, `font-weight: 400`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#161616` | `var(--ink-3)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff5ee` | `var(--paper)` in `:root` |
| **Interactive Accent / Highlight** | `#f2e9e2` | `var(--paper-2)` in `:root` |
| **Secondary / Muted Copy** | `#9a9a9a` | `var(--mute)` in `:root` |
| **Structural Hairline Border** | `#6e6e6e` | `var(--mute-2)` in `:root` |
| **Variable Token (`--crease`)** | `#8c8c8c` | `var(--crease)` in `:root` |
| **Variable Token (`--line`)** | `#fff5ee29` | `var(--line)` in `:root` |
| **Variable Token (`--line-ink`)** | `#00000024` | `var(--line-ink)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-display-src` | `"Cutive Mono", "Cutive Mono Fallback"` | Typography / Scale Token |
| `--font-body-src` | `"aileron", "aileron Fallback"` | Typography / Scale Token |
| `--ink` | `#000` | Typography Ink Token |
| `--ink-2` | `#000` | Typography Ink Token |
| `--ink-3` | `#161616` | Typography Ink Token |
| `--paper` | `#fff5ee` | Canvas / Surface Token |
| `--paper-2` | `#f2e9e2` | Canvas / Surface Token |
| `--white` | `#fff5ee` | Canvas / Surface Token |
| `--mute` | `#9a9a9a` | Color / Atmospheric Token |
| `--mute-2` | `#6e6e6e` | Color / Atmospheric Token |
| `--crease` | `#8c8c8c` | Motion / Easing Token |
| `--fill` | `#fff5ee` | Color / Atmospheric Token |
| `--on-fill` | `#000` | Color / Atmospheric Token |
| `--seam` | `#8c8c8c` | Color / Atmospheric Token |
| `--line` | `#fff5ee29` | Color / Atmospheric Token |
| `--line-ink` | `#00000024` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav> — `twohalves-co`)**:
   - Landmark `<header class="nav">` hosting `Two Halves — design & development st` navigation (`Work · Services · Studio · Contact`), DOM attributes (`data-precedence="next"`, `data-tone="split"`, `data-hide="0"`, `data-side="a"`), and stylesheet rule `.oFPQLq_className { font-family:Cutive Mono,Cutive Mono Fallback;font-style:normal;font-weig... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `You build it Physically, Two Halve`)**:
   - Landmark `<section class="hero">` presenting display lead `You build it Physically, Two Halves — websites de...` and copy excerpt *"T w o H a l v e s ™"* over `#000` canvas and `#fff5ee` ink.
3. **Primary Showcase & Content Grid (<section.st> — `Work that moves.`)**:
   - Landmark `<section class="st">` rendering section `Work that moves.` with copy *"Start a project ↗︎"*, asset references (`512857af647c3544-s.p.25m0iq9x76hr...`, `aileron_latin_400_normal-s.p.1kb3...`, `aileron_latin_700_normal-s.p.1x-w...`, `2tzoz6ksak9sc.css`), and grid rule `.oFPQLq_variable { --font-display-src:"Cutive Mono", "Cutive Mono Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.wk> — `What we make.`)**:
   - Landmark `<section class="wk">` framing `What we make.` and `Websites that move` (*"Get your digital half →"*) with `#fff5ee` surface cards, `#f2e9e2` accents, and `.n4YeuW_className { font-family:aileron,aileron Fallback }`.
5. **Colophon & Global Directory Footer (<footer.foot> — `https://twohalves.co/`)**:
   - Landmark `<footer class="foot">` anchoring `Two Halves — design & developmen` footer links (`Work · Services · Studio · Contact`), copy *"Click a cube to open it, or hold it to turn it Scroll for th"*, and `#6e6e6e` structural dividers.
