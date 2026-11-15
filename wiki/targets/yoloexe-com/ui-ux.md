# UI & UX Architecture: yoloexe-com

## Overview & Design Identity
- **Target**: `yoloexe-com` (**YOLO — DxL**)
- **Production URL**: [https://yoloexe.com](https://yoloexe.com)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0a0014` / `#ff2bd6`)
- **Summary**: A loud, scrolling crash course in YOLO: how computers spot things in pictures, in one look. Then run 27 real YOLO models in your browser.
- **Total Clean CSS Variables Extracted**: `29` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Bungee Shade`
- **Body Font Stack**: `Bungee`
- **Monospace / Technical Font Stack**: `Space Mono`
- **Hero Display (`H1`)**: CSS variables `--display: "Bungee", "Impact", system-ui, sans-serif`; rule `.title` (`letter-spacing: -.01em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(30px,4.4vw,54px)`, `line-height: 1`, `font-weight: 400`)
- **Body Copy**: CSS variables `--body: "Space Grotesk", ui-sans-serif, system-ui, sans-serif`; rule `p` (`font-size: 19px`)
- **Metadata & Labels**: CSS variables `--mono: "Space Mono", ui-monospace, monospace`; rule `small` (`font-size: 14px`, `letter-spacing: .2em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0a0014` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#fff6fd` | `var(--ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#c9b6dd` | `var(--muted)` in `:root` |
| **Interactive Accent / Highlight** | `#ff2bd6` | `var(--pink)` in `:root` |
| **Secondary / Muted Copy** | `#00f0ff` | `var(--cyan)` in `:root` |
| **Structural Hairline Border** | `#e6ff00` | `var(--acid)` in `:root` |
| **Variable Token (`--orange`)** | `#ff7a1a` | `var(--orange)` in `:root` |
| **Variable Token (`--violet`)** | `#8a2bff` | `var(--violet)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--dxl-mark-font` | `700 12px/1 var(--mono)` | Typography / Scale Token |
| `--dxl-mark-tracking` | `.25em` | Typography / Scale Token |
| `--dxl-mark-case` | `uppercase` | Design System Custom Token |
| `--dxl-mark-fg` | `var(--acid)` | Typography Ink Token |
| `--dxl-mark-bg` | `transparent` | Canvas / Surface Token |
| `--dxl-mark-opacity` | `.9` | Design System Custom Token |
| `--bg` | `#0a0014` | Canvas / Surface Token |
| `--ink` | `#fff6fd` | Typography Ink Token |
| `--muted` | `#c9b6dd` | Color / Atmospheric Token |
| `--pink` | `#ff2bd6` | Typography Ink Token |
| `--cyan` | `#00f0ff` | Color / Atmospheric Token |
| `--acid` | `#e6ff00` | Color / Atmospheric Token |
| `--orange` | `#ff7a1a` | Color / Atmospheric Token |
| `--violet` | `#8a2bff` | Color / Atmospheric Token |
| `--card` | `rgba(14, 0, 32, .78)` | Color / Atmospheric Token |
| `--display` | `"Bungee", "Impact", system-ui, sans-serif` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.dots> — `yoloexe-com`)**:
   - Landmark `<nav class="dots">` hosting `YOLO — DxL` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-engine="three.js r180"`, `data-yolo="button"`, `data-yolo="button"`, `data-i="0"`), and stylesheet rule `html { scroll-behavior:auto;overflow-x:clip }`.
2. **Hero Stage & Focal Lead (<section.chap> — `YOLO edition`)**:
   - Landmark `<section class="chap hero">` presenting display lead `YOLO edition` and copy excerpt *"🔊 This one talks. Turn your sound up."* over `#0a0014` canvas and `#fff6fd` ink.
3. **Primary Showcase & Content Grid (<section.chap> — `YOU ONLY LOOK ONCE`)**:
   - Landmark `<section class="chap">` rendering section `YOU ONLY LOOK ONCE` with copy *"or start without sound"*, asset references (`favicon.svg`, `apple-touch-icon.png`, `sitemap-index.xml`, `script.js`), and grid rule `body { margin:0;background:var(--bg);color:var(--ink);font-family:var(--body);f... }`.
4. **Interactive Detail & Feature Matrix (<section.chap> — `YOUR TURN.`)**:
   - Landmark `<section class="chap">` framing `YOUR TURN.` and `NOW YOU KNOW YOLO.` (*"How computers spot things in pictures. Then try it on your camera"*) with `#c9b6dd` surface cards, `#ff2bd6` accents, and `selection { background:var(--acid);color:000 }`.
5. **Colophon & Global Directory Footer (<footer.hud> — `https://yoloexe.com`)**:
   - Landmark `<footer class="hud">` anchoring `YOLO — DxL` footer links (`Overview · Index · Archive · About · Contact`), copy *"This is how YOLO works"*, and `#e6ff00` structural dividers.
