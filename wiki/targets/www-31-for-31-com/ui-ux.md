# UI & UX Architecture: www-31-for-31-com

## Overview & Design Identity
- **Target**: `www-31-for-31-com` (**31 for 31 · One scary movie for every night of October**)
- **Production URL**: [https://www.31-for-31.com/](https://www.31-for-31.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#07090c` / `#8d8a80`)
- **Summary**: Thirty one horror movies, one for each night of October. Rate them, find where to stream them, and scroll through the whole tape.
- **Total Clean CSS Variables Extracted**: `18` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `OC Blimp`
- **Body Font Stack**: `Zombie Punks`
- **Monospace / Technical Font Stack**: `Saans Mono`
- **Hero Display (`H1`)**: rule `.title` (`line-height: 0`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(28px, 3.4vw, 52px)`, `line-height: 1`, `font-weight: 400`)
- **Body Copy**: CSS variables `--font-body: "Saans", system-ui, -apple-system, "Helvetica Neue", sans-serif`; rule `body` (`font-size: 17px`, `line-height: 1.6`)
- **Metadata & Labels**: rule `small` (`font-size: 15px`, `letter-spacing: .3em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#07090c` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#0d1218` | `var(--bg-2)` in `:root` |
| **Elevated Surface / Card Substrate** | `#e8e4d8` | `var(--ink)` in `:root` |
| **Interactive Accent / Highlight** | `#8d8a80` | `var(--muted)` in `:root` |
| **Secondary / Muted Copy** | `#4dff8c` | `var(--green)` in `:root` |
| **Structural Hairline Border** | `#1f8f4e` | `var(--green-dim)` in `:root` |
| **Variable Token (`--orange`)** | `#ff6a1a` | `var(--orange)` in `:root` |
| **Variable Token (`--red`)** | `#ff2d55` | `var(--red)` in `:root` |
| **Variable Token (`--cyan`)** | `#2ee6ff` | `var(--cyan)` in `:root` |
| **Variable Token (`--block-a`)** | `#b8321f` | `var(--block-a)` in `:root` |
| **Variable Token (`--block-b`)** | `#1f3d2b` | `var(--block-b)` in `:root` |
| **Variable Token (`--block-c`)** | `#2a1f45` | `var(--block-c)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#07090c` | Canvas / Surface Token |
| `--bg-2` | `#0d1218` | Canvas / Surface Token |
| `--ink` | `#e8e4d8` | Typography Ink Token |
| `--muted` | `#8d8a80` | Color / Atmospheric Token |
| `--green` | `#4dff8c` | Color / Atmospheric Token |
| `--green-dim` | `#1f8f4e` | Color / Atmospheric Token |
| `--orange` | `#ff6a1a` | Color / Atmospheric Token |
| `--red` | `#ff2d55` | Color / Atmospheric Token |
| `--cyan` | `#2ee6ff` | Color / Atmospheric Token |
| `--block-a` | `#b8321f` | Color / Atmospheric Token |
| `--block-b` | `#1f3d2b` | Color / Atmospheric Token |
| `--block-c` | `#2a1f45` | Color / Atmospheric Token |
| `--font-spooky` | `"Creepster", "Impact", cursive` | Typography / Scale Token |
| `--font-blimp` | `"OC Blimp", "Creepster", "Impact", cursive` | Typography / Scale Token |
| `--font-osd` | `"Saans Mono", ui-monospace, "SF Mono", Menlo, "Courier New", monospace` | Typography / Scale Token |
| `--font-body` | `"Saans", system-ui, -apple-system, "Helvetica Neue", sans-serif` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.topbar> — `www-31-for-31-com`)**:
   - Landmark `<header class="topbar">` hosting `31 for 31 · One scary movie for ever` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-sound-toggle`, `data-view="scroll"`, `data-label="Scroll"`, `data-view="gallery"`), and stylesheet rule `focus { outline: none; }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Rope`)**:
   - Landmark `<section class="hero">` presenting display lead `Rope` and copy excerpt *"One scary movie for every night of October. Thirty one tapes, rew"* over `#07090c` canvas and `#e8e4d8` ink.
3. **Primary Showcase & Content Grid (<section.film> — `Mandy`)**:
   - Landmark `<section class="film">` rendering section `Mandy` with copy *"1948 DIR. ALFRED HITCHCOCK"*, asset references (`apple-touch-icon.png`, `Saans-Regular.woff`, `SaansMono-Regular.woff`, `style.css`), and grid rule `focus-visible { outline: 2px solid var(--green); outline-offset: 3px; box-shadow: 0 0 0... }`.
4. **Interactive Detail & Feature Matrix (<section.film> — `Wes Craven's New Nightmare`)**:
   - Landmark `<section class="film">` framing `Wes Craven's New Nightmare` and `Candyman` (*"DIR. ALFRED HITCHCOCK"*) with `#e8e4d8` surface cards, `#8d8a80` accents, and `.stream a:focus-visible { outline-offset: 2px; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.31-for-31.com/`)**:
   - Landmark `<footer class="footer">` anchoring `31 for 31 · One scary movie for ` footer links (`Overview · Index · Archive · About · Contact`), copy *"Two college friends strangle a classmate, hide the body in a"*, and `#1f8f4e` structural dividers.
