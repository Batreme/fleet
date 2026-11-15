# UI & UX Architecture: both-sides-the7eye-org-il_en

## Overview & Design Identity
- **Target**: `both-sides-the7eye-org-il_en` (**Extremists on Both Sides**)
- **Production URL**: [https://both-sides.the7eye.org.il/en/](https://both-sides.the7eye.org.il/en/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#FDFCFF` / `#E1E1E1`)
- **Summary**: We collected thousands of political actions carried out in public space over the past four years. Decide for yourself — who are the extre...
- **Total Clean CSS Variables Extracted**: `91` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Assistant`
- **Body Font Stack**: `Josefin Slab`
- **Monospace / Technical Font Stack**: `IBM Plex Sans Arabic`
- **Hero Display (`H1`)**: CSS variables `--se-cap-display: block`
- **Section Heading (`H2`)**: rule `.section-title` (`font-size: 36px`, `line-height: 1.2`)
- **Body Copy**: CSS variables `--font-body: 'Assistant', sans-serif`
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `18px`, `16px`, `36px`, `26px`, `14px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#FDFCFF` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#111` | `var(--ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#767676` | `var(--muted-ui)` in `:root` |
| **Interactive Accent / Highlight** | `#E1E1E1` | `var(--line-light)` in `:root` |
| **Secondary / Muted Copy** | `#25D366` | `var(--brand)` in `:root` |
| **Structural Hairline Border** | `#393239` | `var(--se-ink)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#FDFCFF` | Canvas / Surface Token |
| `--card-w` | `min(456px, 100vw - 48px)` | Dimension / Scale Token |
| `--card-top` | `4.4vh` | Dimension / Scale Token |
| `--ink` | `#111` | Typography Ink Token |
| `--ink-soft` | `rgba(0, 0, 0, 0.81)` | Typography Ink Token |
| `--ink-note` | `rgba(0, 0, 0, 0.85)` | Typography Ink Token |
| `--muted-ui` | `#767676` | Color / Atmospheric Token |
| `--line-light` | `#E1E1E1` | Canvas / Surface Token |
| `--font-body` | `'Assistant', sans-serif` | Typography / Scale Token |
| `--font-title` | `'Discordia', serif` | Typography / Scale Token |
| `--font-ar` | `'IBM Plex Sans Arabic', 'Assistant', sans-serif` | Typography / Scale Token |
| `--ui-fade-ms` | `180ms` | Motion / Timing Token |
| `--tray-ms` | `.85s` | Motion / Timing Token |
| `--tray-ease` | `cubic-bezier(0.22, 1, 0.36, 1)` | Motion / Easing Token |
| `--fade-ms` | `.35s` | Motion / Timing Token |
| `--p9-pop-ms` | `280ms` | Motion / Timing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.lang-wrap> — `both-sides-the7eye-org-il_en`)**:
   - Landmark `<nav class="lang-wrap">` hosting `Extremists on Both Sides` navigation (`עברית · English · العربية`), DOM attributes (`data-page="0"`, `data-page="1"`, `data-page="2"`, `data-page="3"`), and stylesheet rule `html { touch-action: pan-x pan-y; }`.
2. **Hero Stage & Focal Lead (<section.a11y-only> — `Text description of the data`)**:
   - Landmark `<section class="a11y-only">` presenting display lead `Text description of the data` and copy excerpt *"The project shows 14,300 documented political actions that took p"* over `#FDFCFF` canvas and `#111` ink.
3. **Primary Showcase & Content Grid (<section.text-section> — `By camp and group`)**:
   - Landmark `<section class="text-section">` rendering section `By camp and group` with copy *"Haredi Jewish protesters: 492 documented actions"*, asset references (`favicon.svg`, `favicon-32.png`, `favicon-192.png`, `apple-touch-icon.png`), and grid rule `body { background: var(--bg); }`.
4. **Interactive Detail & Feature Matrix (<section.text-section> — `The Netanyahu Coalition — 8,499 do`)**:
   - Landmark `<section class="text-section">` framing `The Netanyahu Coalition — 8,499 documented actions` and `The Change Bloc — 5,801 documented actions` (*"West Bank settler movements: 7,698 documented actions"*) with `#767676` surface cards, `#E1E1E1` accents, and `after { -webkit-user-select: none !important; user-select: none !important; -web... }`.
5. **Colophon & Global Directory Footer (<footer.page0-dots-overlay> — `https://both-sides.the7eye.org.il/en/`)**:
   - Landmark `<footer class="page0-dots-overlay">` anchoring `Extremists on Both Sides` footer links (`עברית · English · العربية`), copy *"Conservative right-wing groups: 309 documented actions"*, and `#393239` structural dividers.
