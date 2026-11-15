# UI & UX Architecture: www-gianpaolotucci-com_work-html

## Overview & Design Identity
- **Target**: `www-gianpaolotucci-com_work-html` (**Gianpaolo Tucci — Creative Director, Berlin · AI-native experiences**)
- **Production URL**: [https://www.gianpaolotucci.com/work.html](https://www.gianpaolotucci.com/work.html)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#F5F1E7` / `#BEB9AC`)
- **Summary**: Gianpaolo Tucci is a Berlin-based creative director and experience design director shaping AI-native products, luxury digital experiences...
- **Total Clean CSS Variables Extracted**: `17` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `DM Mono`
- **Body Font Stack**: `Doto`
- **Monospace / Technical Font Stack**: `DM Mono`
- **Hero Display (`H1`)**: CSS variables `--f-display: "Instrument Sans","Helvetica Neue",Helvetica,Arial,sans-serif`; rule `h1` (`font-size: clamp(72px,16vw,250px)`, `line-height: .84`, `letter-spacing: -.055em`, `font-weight: var(--hl-w)`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(64px,11vw,170px)`, `line-height: .84`, `letter-spacing: -.055em`, `font-weight: 500`)
- **Body Copy**: rule `p` (`font-size: 17px`, `line-height: 1.5`)
- **Metadata & Labels**: CSS variables `--f-mono: "DM Mono",ui-monospace,"SFMono-Regular",Menlo,monospace`; rule `.mono` (`font-size: 11px`, `letter-spacing: .02em`, `font-weight: 400`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#F5F1E7` | `var(--paper)` in `:root` |
| **Primary Typography Ink** | `#0D0D0C` | `var(--ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#6F6B62` | `var(--mute)` in `:root` |
| **Interactive Accent / Highlight** | `#BEB9AC` | `var(--faint)` in `:root` |
| **Secondary / Muted Copy** | `#1F2BD6` | `var(--accent)` in `:root` |
| **Structural Hairline Border** | `#F8F5EE` | `var(--sheet)` in `:root` |
| **Variable Token (`--go`)** | `#13A35E` | `var(--go)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--paper` | `#F5F1E7` | Canvas / Surface Token |
| `--ink` | `#0D0D0C` | Typography Ink Token |
| `--mute` | `#6F6B62` | Color / Atmospheric Token |
| `--faint` | `#BEB9AC` | Color / Atmospheric Token |
| `--dot` | `#0D0D0C` | Color / Atmospheric Token |
| `--accent` | `#1F2BD6` | Brand / Palette Token |
| `--sheet` | `#F8F5EE` | Color / Atmospheric Token |
| `--f-display` | `"Instrument Sans","Helvetica Neue",Helvetica,Arial,sans-serif` | Design System Custom Token |
| `--f-serif` | `"Instrument Serif","Times New Roman",Georgia,serif` | Typography / Scale Token |
| `--f-dot` | `"Doto","DM Mono",ui-monospace,monospace` | Design System Custom Token |
| `--f-mono` | `"DM Mono",ui-monospace,"SFMono-Regular",Menlo,monospace` | Typography / Scale Token |
| `--ease` | `cubic-bezier(.22,1,.36,1)` | Motion / Easing Token |
| `--go` | `#13A35E` | Color / Atmospheric Token |
| `--pc` | `#13A35E` | Color / Atmospheric Token |
| `--hl-w` | `500` | Design System Custom Token |
| `--hl-wd` | `"wdth" 100` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.idx-head> — `www-gianpaolotucci-com_work-html`)**:
   - Landmark `<header class="idx-head">` hosting `Gianpaolo Tucci — Creative Director,` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-go="work"`, `data-go="index"`, `data-go="about"`, `data-go="contact"`), and stylesheet rule `body { height:100% }`.
2. **Hero Stage & Focal Lead (<section.sr-only> — `Gianpaolo Tucci — Creative Directo`)**:
   - Landmark `<section class="sr-only">` presenting display lead `Gianpaolo Tucci — Creative Director, Berlin` and copy excerpt *"Gianpaolo Tucci is a Berlin-based creative director and experienc"* over `#F5F1E7` canvas and `#0D0D0C` ink.
3. **Primary Showcase & Content Grid (<section.boot> — `Selected work`)**:
   - Landmark `<section class="boot">` rendering section `Selected work` with copy *"This is not a portfolio. This is a timeline of a shift."*, asset references (`favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `button { font:inherit;color:inherit;background:none;border:0;padding:0;cursor:poi... }`.
4. **Interactive Detail & Feature Matrix (<section.col> — `Versace Biggies`)**:
   - Landmark `<section class="col">` framing `Versace Biggies` and `Moncler City of Genius` (*"Versace Biggies 2024 · Creative direction · Global campaign. One "*) with `#6F6B62` surface cards, `#BEB9AC` accents, and `img { max-width:100% }`.
5. **Colophon & Global Directory Footer (<footer.lcol> — `https://www.gianpaolotucci.com/work.html`)**:
   - Landmark `<footer class="lcol">` anchoring `Gianpaolo Tucci — Creative Direc` footer links (`Overview · Index · Archive · About · Contact`), copy *"2024 · Creative direction · Global campaign. One campaign ac"*, and `#F8F5EE` structural dividers.
