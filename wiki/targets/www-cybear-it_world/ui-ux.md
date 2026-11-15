# UI & UX Architecture: www-cybear-it_world

## Overview & Design Identity
- **Target**: `www-cybear-it_world` (**Cybear World**)
- **Production URL**: [https://www.cybear.it/world/](https://www.cybear.it/world/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#7fc4ef` / `#2b211b`)
- **Summary**: Cybear World: il mondo 3D di Cybear da esplorare con l'orso, tra i cinque amici del Metodo Ecosistema, i case history, la mostra fotograf...
- **Total Clean CSS Variables Extracted**: `22` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Antonio`
- **Body Font Stack**: `Figtree`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--font-display: "Antonio","Arial Narrow","Roboto Condensed",sans-serif`
- **Section Heading (`H2`)**: rule `h2` (`letter-spacing: .005em`)
- **Body Copy**: rule `p` (`font-size: 16px`, `line-height: 1.45`)
- **Metadata & Labels**: rule `small` (`font-weight: 500`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#7fc4ef` | `var(--sky-top)` in `:root` |
| **Primary Typography Ink** | `#bfe3f6` | `var(--sky)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f5efd4` | `var(--haze)` in `:root` |
| **Interactive Accent / Highlight** | `#2b211b` | `var(--fg)` in `:root` |
| **Secondary / Muted Copy** | `#5b4d43` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#7a4a24` | `var(--accent)` in `:root` |
| **Variable Token (`--bubble-bg`)** | `#ffffff` | `var(--bubble-bg)` in `:root` |
| **Variable Token (`--focus`)** | `#c0682a` | `var(--focus)` in `:root` |
| **Variable Token (`--meter-fg`)** | `#f6f1e7` | `var(--meter-fg)` in `:root` |
| **Variable Token (`--a1`)** | `#d9622b` | `var(--a1)` in `:root` |
| **Variable Token (`--a2`)** | `#2f6fc4` | `var(--a2)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--sky-top` | `#7fc4ef` | Color / Atmospheric Token |
| `--sky` | `#bfe3f6` | Color / Atmospheric Token |
| `--haze` | `#f5efd4` | Color / Atmospheric Token |
| `--fg` | `#2b211b` | Typography Ink Token |
| `--muted` | `#5b4d43` | Color / Atmospheric Token |
| `--accent` | `#7a4a24` | Brand / Palette Token |
| `--chip-bg` | `rgba(255,255,255,.84)` | Canvas / Surface Token |
| `--chip-line` | `rgba(43,33,27,.14)` | Color / Atmospheric Token |
| `--bubble-bg` | `#ffffff` | Canvas / Surface Token |
| `--bubble-fg` | `#2b211b` | Typography Ink Token |
| `--bubble-line` | `#2b211b` | Color / Atmospheric Token |
| `--focus` | `#c0682a` | Color / Atmospheric Token |
| `--meter-bg` | `rgba(18,14,10,.8)` | Canvas / Surface Token |
| `--meter-fg` | `#f6f1e7` | Typography Ink Token |
| `--a1` | `#d9622b` | Color / Atmospheric Token |
| `--a2` | `#2f6fc4` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.top> — `www-cybear-it_world`)**:
   - Landmark `<header class="top">` hosting `Cybear World` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-engine="three.js r160"`, `data-src="img/cybear-world-logo..."`, `data-code="KeyW"`, `data-code="KeyA"`), and stylesheet rule `body { height:100% }`.
2. **Hero Stage & Focal Lead (<article.rd> — `You’ve met the whole ecosystem!`)**:
   - Landmark `<article class="rd">` presenting display lead `You’ve met the whole ecosystem!` and copy excerpt *"Text version of the world"* over `#7fc4ef` canvas and `#2b211b` ink.
3. **Primary Showcase & Content Grid (<article.rd> — `Text version of the world`)**:
   - Landmark `<article class="rd">` rendering section `Text version of the world` with copy *"The world of Cybear is ready!"*, asset references (`icon-32.png`, `icon-180.png`, `testo.html`, `antonio-600.woff2`), and grid rule `.stage.over-bear { cursor:grab }`.
4. **Interactive Detail & Feature Matrix (<article.rd> — `The world of Cybear is ready!`)**:
   - Landmark `<article class="rd">` framing `The world of Cybear is ready!` and `Best with the sound on` (*"Best with the sound on"*) with `#f5efd4` surface cards, `#2b211b` accents, and `.stage.over-thing { cursor:pointer }`.
5. **Colophon & Global Directory Footer (<footer.stage> — `https://www.cybear.it/world/`)**:
   - Landmark `<footer class="stage">` anchoring `Cybear World` footer links (`Overview · Index · Archive · About · Contact`), copy *"Coins, visits and your choice of path will be reset: the Exp"*, and `#7a4a24` structural dividers.
