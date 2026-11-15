# UI & UX Architecture: wedding-s-tmro-com

## Overview & Design Identity
- **Target**: `wedding-s-tmro-com` (**Wedding Invitation · Yuri & Tomoro**)
- **Production URL**: [https://wedding.s-tmro.com/](https://wedding.s-tmro.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#333333` / `#f2f2f2`)
- **Summary**: 結婚式へのご招待です。日時は2026年11月29日（いい肉の日）、10:00に受付、10:30に開始です。会場は桜通線「国際センター」駅近くのレストラン「recipe」です。
- **Total Clean CSS Variables Extracted**: `16` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Italianno`
- **Body Font Stack**: `Stack Sans Headline`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 3em`, `font-weight: 700`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 2em`)
- **Body Copy**: rule `body` (`line-height: 1`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `100%`, `3em`, `2em`, `1em`, `16px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#333333` | `var(--s-color-e2b900cc)` in `:root` |
| **Primary Typography Ink** | `#fff` | `body { background: #fff }` |
| **Elevated Surface / Card Substrate** | `#ccc` | `hr { border-top: #ccc }` |
| **Interactive Accent / Highlight** | `#f2f2f2` | `table { border: #f2f2f2 }` |
| **Secondary / Muted Copy** | `#1a1a1a` | `table { color: #1a1a1a }` |
| **Structural Hairline Border** | `#eee` | `p > code { background: #eee }` |
| **Variable Token (`--s-color-34930474`)** | `#333333ff` | `var(--s-color-34930474)` in `:root` |
| **Variable Token (`--s-color-27b6cb51`)** | `#f2f2f2ff` | `var(--s-color-27b6cb51)` in `:root` |
| **Variable Token (`--s-color-c8b6c400`)** | `#f7f7f7ff` | `var(--s-color-c8b6c400)` in `:root` |
| **Variable Token (`--s-color-54b90296`)** | `#ffffffff` | `var(--s-color-54b90296)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--s-font-c796e0a2` | `'Stack Sans Notch'` | Typography / Scale Token |
| `--s-font-c89837a8` | `'Stack Sans Headline'` | Typography / Scale Token |
| `--s-font-e28f2a0c` | `'Stack Sans Text'` | Typography / Scale Token |
| `--s-font-75b0f13c` | `Italianno` | Typography / Scale Token |
| `--s-font-11bbee0d` | `'Zen Old Mincho'` | Typography / Scale Token |
| `--img-current` | `var(--img-small)` | Design System Custom Token |
| `--s-color-34930474` | `#333333ff` | Brand / Palette Token |
| `--s-color-27b6cb51` | `#f2f2f2ff` | Brand / Palette Token |
| `--s-color-c8b6c400` | `#f7f7f7ff` | Brand / Palette Token |
| `--s-color-c69a0a1a` | `rgb(240, 240, 240)` | Brand / Palette Token |
| `--s-color-54b90296` | `linear-gradient(90deg, #ffffffff, #ffffffff)` | Brand / Palette Token |
| `--s-color-eea30069` | `rgba(150, 150, 150, 0)` | Brand / Palette Token |
| `--s-color-e2b900cc` | `#333333` | Brand / Palette Token |
| `--gap-h` | `0px` | Layout / Spatial Grid Token |
| `--gap-v` | `0px` | Layout / Spatial Grid Token |
| `--ha` | `1` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `wedding-s-tmro-com`)**:
   - Landmark `<header class="lenis">` hosting `Wedding Invitation · Yuri & Tomoro` navigation (`@recipe · MESSAGE · INFORMATION · YOUR REPLY · @recipe @recipe`), DOM attributes (`data-appear`, `data-inited-appear`, `data-sd-img-src="https://storage.googl..."`, `data-sd-img-src="https://storage.googl..."`), and stylesheet rule `html.lenis body { height: auto; }`.
2. **Hero Stage & Focal Lead (<section.section> — `Wedding Invitation · Yuri & Tomoro`)**:
   - Landmark `<section class="section">` presenting display lead `Wedding Invitation · Yuri & Tomoro` and copy excerpt *"Yuri Kunimatsu & Tomoro Sugawara Wedding Ceremony"* over `#333333` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.section> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="section">` rendering section `Featured Work & Interactive Showcase` with copy *"“ii-fuku-nohi” & “ii-niku-nohi”"*, asset references (`84a82c89-316b-4152-8b5a-bb944f91e1b1`, `fonts.googleapis.com`, `fonts.gstatic.com`, `css2`), and grid rule `.lenis-stopped { overflow: clip; }`.
4. **Interactive Detail & Feature Matrix (<section.section> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="section">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"mixture restaurant"*) with `#ccc` surface cards, `#f2f2f2` accents, and `.lenis.lenis-smooth iframe { pointer-events: none; }`.
5. **Colophon & Global Directory Footer (<footer.text> — `https://wedding.s-tmro.com/`)**:
   - Landmark `<footer class="text">` anchoring `Wedding Invitation · Yuri & Tomo` footer links (`@recipe · MESSAGE · INFORMATION · YOUR REPLY · @recipe @recipe`), copy *"Good clothes Good meats Good Fortunes"*, and `#eee` structural dividers.
