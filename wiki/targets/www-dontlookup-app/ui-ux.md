# UI & UX Architecture: www-dontlookup-app

## Overview & Design Identity
- **Target**: `www-dontlookup-app` (**Don't Look Up — a game about keeping everyone looking down**)
- **Production URL**: [https://www.dontlookup.app/](https://www.dontlookup.app/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f4f3ef` / `#9abeef`)
- **Summary**: You are very rich, very tall, and standing on quite a lot of people. Keep them distracted and they keep paying. Let them look up, and the...
- **Total Clean CSS Variables Extracted**: `20` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Marsipan`
- **Body Font Stack**: `Luckiest Guy`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `16px`, `10px`, `clamp(24px, 3.4vw, 40px)`, `11px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `16px`, `10px`, `clamp(24px, 3.4vw, 40px)`, `11px`)
- **Body Copy**: CSS variables `--body: 'Nunito', ui-rounded, "SF Pro Rounded", system-ui, sans-serif`
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `16px`, `10px`, `clamp(24px, 3.4vw, 40px)`, `11px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f4f3ef` | `var(--paper)` in `:root` |
| **Primary Typography Ink** | `#14140f` | `var(--ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#c0342a` | `var(--red)` in `:root` |
| **Interactive Accent / Highlight** | `#9abeef` | `var(--convert)` in `:root` |
| **Secondary / Muted Copy** | `#2b5a9b` | `var(--follow)` in `:root` |
| **Structural Hairline Border** | `#f8e08a` | `var(--y1)` in `:root` |
| **Variable Token (`--y2`)** | `#f2c31a` | `var(--y2)` in `:root` |
| **Variable Token (`--y3`)** | `#c98f06` | `var(--y3)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--paper` | `#f4f3ef` | Canvas / Surface Token |
| `--ink` | `#14140f` | Typography Ink Token |
| `--red` | `#c0342a` | Color / Atmospheric Token |
| `--btn-h` | `44px` | Dimension / Scale Token |
| `--convert` | `#9abeef` | Color / Atmospheric Token |
| `--follow` | `#2b5a9b` | Color / Atmospheric Token |
| `--y1` | `#f8e08a` | Color / Atmospheric Token |
| `--y2` | `#f2c31a` | Color / Atmospheric Token |
| `--y3` | `#c98f06` | Color / Atmospheric Token |
| `--btn-r` | `14px` | Dimension / Scale Token |
| `--body` | `'Nunito', ui-rounded, "SF Pro Rounded", system-ui, sans-serif` | Dimension / Scale Token |
| `--font` | `var(--body)` | Typography / Scale Token |
| `--hand` | `var(--body)` | Design System Custom Token |
| `--bw` | `2.5px` | Dimension / Scale Token |
| `--lift` | `5px` | Dimension / Scale Token |
| `--rail-n` | `8` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.mcell> — `www-dontlookup-app`)**:
   - Landmark `<header class="mcell">` hosting `Don't Look Up — a game about keeping` navigation (`here`), DOM attributes (`data-engine="three.js r170"`), and stylesheet rule `stage { position: fixed; inset: 0; }`.
2. **Hero Stage & Focal Lead (<div.lbl> — `Don't Look Up — a game about keepi`)**:
   - Landmark `<div class="lbl">` presenting display lead `Don't Look Up — a game about keeping everyone lo` and copy excerpt *"Plant a distraction space"* over `#f4f3ef` canvas and `#14140f` ink.
3. **Primary Showcase & Content Grid (<div.legend> — `Featured Work & Interactive Showca`)**:
   - Landmark `<div class="legend">` rendering section `Featured Work & Interactive Showcase` with copy *"Plant a distraction"*, asset references (`favicon.ico`, `favicon-32.png`, `icon-192.png`, `apple-touch-icon.png`), and grid rule `stage canvas { display: block; touch-action: none; }`.
4. **Interactive Detail & Feature Matrix (<div.lrow> — `Technical Architecture & Narrative`)**:
   - Landmark `<div class="lrow">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"We count runs, not people. Anonymously, through Google Analytics,"*) with `#c0342a` surface cards, `#9abeef` accents, and `bubbles { position: fixed; inset: 0; pointer-events: none; overflow: hidden; }`.
5. **Colophon & Global Directory Footer (<footer.lsw> — `https://www.dontlookup.app/`)**:
   - Landmark `<footer class="lsw">` anchoring `Don't Look Up — a game about kee` footer links (`here`), copy *"Yellow has noticed. Pays nothing, talks the others round, an"*, and `#f8e08a` structural dividers.
