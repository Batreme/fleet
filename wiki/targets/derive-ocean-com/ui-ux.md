# UI & UX Architecture: derive-ocean-com

## Overview & Design Identity
- **Target**: `derive-ocean-com` (**Dérive — a contemplative game: a rowing boat on an endless ocean**)
- **Production URL**: [https://derive-ocean.com/](https://derive-ocean.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f6eedf` / `#5a4531`)
- **Summary**: Ramez sur un océan sans fin, observez baleines et bancs de poissons, remplissez le carnet d’une naturaliste. Un jeu contemplatif gratuit,...
- **Total Clean CSS Variables Extracted**: `86` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `EB Garamond`
- **Body Font Stack**: `La Belle Aurore`
- **Monospace / Technical Font Stack**: `SF Mono`
- **Hero Display (`H1`)**: rule `h1` (`font-size: 136px`, `line-height: .95`, `letter-spacing: -.01em`, `font-weight: 400`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 34px`, `font-weight: 400`)
- **Body Copy**: rule `p` (`font-size: 16px`, `line-height: 1.45`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `18px`, `15px`, `16px`, `20px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f6eedf` | `var(--sea-text)` in `:root` |
| **Primary Typography Ink** | `#f3eada` | `var(--paper)` in `:root` |
| **Elevated Surface / Card Substrate** | `#d9c9aa` | `var(--paper-deep)` in `:root` |
| **Interactive Accent / Highlight** | `#5a4531` | `var(--binding)` in `:root` |
| **Secondary / Muted Copy** | `#2a241d` | `var(--ink)` in `:root` |
| **Structural Hairline Border** | `#3e3326` | `var(--ink-soft)` in `:root` |
| **Variable Token (`--sea-shadow`)** | `#06222899` | `var(--sea-shadow)` in `:root` |
| **Variable Token (`--sea-button`)** | `#08262a29` | `var(--sea-button)` in `:root` |
| **Variable Token (`--sea-line`)** | `#f6eedf52` | `var(--sea-line)` in `:root` |
| **Variable Token (`--sea-dim`)** | `#0412148c` | `var(--sea-dim)` in `:root` |
| **Variable Token (`--paper-gutter`)** | `#5e482a2e` | `var(--paper-gutter)` in `:root` |
| **Variable Token (`--ink-muted`)** | `#5e4e3b` | `var(--ink-muted)` in `:root` |
| **Variable Token (`--ink-faint`)** | `#7a6a55` | `var(--ink-faint)` in `:root` |
| **Variable Token (`--rule`)** | `#5e4e3b4d` | `var(--rule)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-text` | `"EB Garamond", "Iowan Old Style", Georgia, serif` | Typography Ink Token |
| `--font-hand` | `"La Belle Aurore", "Snell Roundhand", cursive` | Typography / Scale Token |
| `--sea-text` | `#f6eedf` | Typography Ink Token |
| `--sea-shadow` | `0 1px 8px #06222899` | Elevation / Border Token |
| `--sea-button` | `#08262a29` | Color / Atmospheric Token |
| `--sea-line` | `#f6eedf52` | Color / Atmospheric Token |
| `--sea-dim` | `#0412148c` | Color / Atmospheric Token |
| `--paper` | `#f3eada` | Canvas / Surface Token |
| `--paper-deep` | `#d9c9aa` | Canvas / Surface Token |
| `--paper-gutter` | `#5e482a2e` | Canvas / Surface Token |
| `--binding` | `#5a4531` | Color / Atmospheric Token |
| `--ink` | `#2a241d` | Typography Ink Token |
| `--ink-soft` | `#3e3326` | Typography Ink Token |
| `--ink-muted` | `#5e4e3b` | Typography Ink Token |
| `--ink-faint` | `#7a6a55` | Typography Ink Token |
| `--rule` | `#5e4e3b4d` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.intro-menu> — `derive-ocean-com`)**:
   - Landmark `<nav class="intro-menu">` hosting `Dérive — a contemplative game: a row` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-carte="d"`, `data-carte-v="Xyo-u2Gt"`, `data-paper="162430"`, `data-teach="photo"`), and stylesheet rule `html { scroll-padding-top:env(safe-area-inset-top,0px) }`.
2. **Hero Stage & Focal Lead (<div.hud-settings> — `Dérive`)**:
   - Landmark `<div class="hud-settings">` presenting display lead `Dérive` and copy excerpt *"A rowing boat, an endless ocean, and what swims beneath."* over `#f6eedf` canvas and `#2a241d` ink.
3. **Primary Showcase & Content Grid (<div.hud-camera> — `A rowing boat, an endless ocean, a`)**:
   - Landmark `<div class="hud-camera">` rendering section `A rowing boat, an endless ocean, and what swims ` with copy *"Sign in to find your game"*, asset references (`favicon-32.png`, `favicon-48.png`, `apple-touch-icon.png`, `en-BwLAseLg.js`), and grid rule `body { background:var(--deep);overscroll-behavior:none;height:100%;margin:0;ove... }`.
4. **Interactive Detail & Feature Matrix (<div.hud-carnet> — `Sign in to find your game`)**:
   - Landmark `<div class="hud-carnet">` framing `Sign in to find your game` and `Touch and hold the sea, or the arrows or WASD, t` (*"Touch and hold the sea, or the arrows or WASD, to row About The m"*) with `#d9c9aa` surface cards, `#5a4531` accents, and `root { height:100% }`.
5. **Colophon & Global Directory Footer (<footer.tools> — `https://derive-ocean.com/`)**:
   - Landmark `<footer class="tools">` anchoring `Dérive — a contemplative game: a` footer links (`Overview · Index · Archive · About · Contact`), copy *"Touch and hold the sea, or the arrows or WASD, to row"*, and `#3e3326` structural dividers.
