# UI & UX Architecture: michellekayewashington-com

## Overview & Design Identity
- **Target**: `michellekayewashington-com` (**Michelle Kaye — Fine Arts · Contemporary Artist, Charleston SC**)
- **Production URL**: [https://michellekayewashington.com/](https://michellekayewashington.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fffdf8` canvas, `#120a09` ink, `#2b201d` accent)
- **Summary**: Michelle Kaye is a contemporary artist in Charleston, SC, exploring humanity’s relationship with the natural world. See Against the Grain...
- **Total Clean CSS Variables Extracted**: `42` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Cormorant`
- **Body Font Stack**: `Cormorant`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(17px, 1.05vw + 10px, 21px)`, `1.35rem`, `0.85rem`, `1.15rem`, `0.75rem`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(17px, 1.05vw + 10px, 21px)`, `1.35rem`, `0.85rem`, `1.15rem`, `0.75rem`)
- **Body Copy**: rule `body` (`font-size: clamp(17px, 1.05vw + 10px, 21px)`, `line-height: 1.45`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(17px, 1.05vw + 10px, 21px)`, `1.35rem`, `0.85rem`, `1.15rem`, `0.75rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fffdf8` | `var(--paper)` in `:root` |
| **Primary Typography Ink** | `#f6f0e8` | `var(--paper-2)` in `:root` |
| **Elevated Surface / Card Substrate** | `#120a09` | `var(--ink)` in `:root` |
| **Interactive Accent / Highlight** | `#2b201d` | `var(--ink-2)` in `:root` |
| **Secondary / Muted Copy** | `#9a675c` | `var(--rose)` in `:root` |
| **Structural Hairline Border** | `#c68f81` | `var(--rose-2)` in `:root` |
| **Variable Token (`--tan`)** | `#b7a397` | `var(--tan)` in `:root` |
| **Variable Token (`--muted`)** | `#7a6560` | `var(--muted)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--paper` | `#fffdf8` | Canvas / Surface Token |
| `--paper-2` | `#f6f0e8` | Canvas / Surface Token |
| `--ink` | `#120a09` | Typography Ink Token |
| `--ink-2` | `#2b201d` | Typography Ink Token |
| `--rose` | `#9a675c` | Color / Atmospheric Token |
| `--rose-2` | `#c68f81` | Color / Atmospheric Token |
| `--tan` | `#b7a397` | Color / Atmospheric Token |
| `--rule` | `rgb(18 10 9 / 14%)` | Color / Atmospheric Token |
| `--fg` | `var(--ink)` | Typography Ink Token |
| `--bg` | `var(--paper)` | Canvas / Surface Token |
| `--muted` | `#7a6560` | Color / Atmospheric Token |
| `--nav-w` | `clamp(190px, 15vw, 300px)` | Layout / Spatial Grid Token |
| `--pad` | `clamp(1.25rem, 3.2vw, 4rem)` | Layout / Spatial Grid Token |
| `--ease` | `cubic-bezier(0.22, 1, 0.36, 1)` | Motion / Easing Token |
| `--ease-io` | `cubic-bezier(0.65, 0, 0.35, 1)` | Motion / Easing Token |
| `--serif` | `"Cormorant", Georgia, "Times New Roman", serif` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.shell> — `michellekayewashington-com`)**:
   - Landmark `<header class="shell">` hosting `Michelle Kaye — Fine Arts · Contempo` navigation (`01 Michelle · 02 Gallery · 03 Socials · Charleston Magazine`), DOM attributes (`data-page="index"`, `data-ready="index"`, `data-shell`, `data-nav="index"`), and stylesheet rule `html { --room-title: var(--fg); }`.
2. **Hero Stage & Focal Lead (<section.home> — `Michelle Kaye`)**:
   - Landmark `<section class="home">` presenting display lead `Michelle Kaye` and copy excerpt *"Michelle Kaye Fine Arts"* over `#fffdf8` canvas and `#120a09` ink.
3. **Primary Showcase & Content Grid (<section.home> — `About the Artist`)**:
   - Landmark `<section class="home">` rendering section `About the Artist` with copy *"Drummond Studio Gallery"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `after { box-sizing: border-box; }`.
4. **Interactive Detail & Feature Matrix (<section.home> — `Questions for the Artist?`)**:
   - Landmark `<section class="home">` framing `Questions for the Artist?` and `Leaving this site` (*"Charleston City Paper"*) with `#120a09` surface cards, `#2b201d` accents, and `body { margin: 0; height: 100%; }`.
5. **Colophon & Global Directory Footer (<footer.mkl-cam> — `https://michellekayewashington.com/`)**:
   - Landmark `<footer class="mkl-cam">` anchoring `Michelle Kaye — Fine Arts · Cont` footer links (`01 Michelle · 02 Gallery · 03 Socials · Charleston Magazine`), copy *"Charleston Magazine"*, and `#c68f81` structural dividers.
