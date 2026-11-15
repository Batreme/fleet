# UI & UX Architecture: levigav-com

## Overview & Design Identity
- **Target**: `levigav-com` (**Levi Gavrilut · I build what I want to exist**)
- **Production URL**: [https://levigav.com](https://levigav.com)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#22201e`)
- **Summary**: Levi Gavrilut, 16. Designer and developer from Switzerland. Websites, web apps and small tools built with care. I ♥ Jesus.
- **Total Clean CSS Variables Extracted**: `153` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Instrument Serif`
- **Body Font Stack**: `Inter Variable`
- **Monospace / Technical Font Stack**: `JetBrains Mono Variable`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11px`, `clamp(44px,9vw,112px)`, `clamp(24px,3.6vw,40px)`, `clamp(18px,2.2vw,22px)`, `10.5px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `11px`, `clamp(44px,9vw,112px)`, `clamp(24px,3.6vw,40px)`, `clamp(18px,2.2vw,22px)`, `10.5px`)
- **Body Copy**: rule `p` (`font-size: clamp(18px,2.2vw,22px)`, `line-height: 1.4`)
- **Metadata & Labels**: rule `small` (`font-size: 9.5px`, `letter-spacing: .08em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#121110` | `var(--panel)` in `:root` |
| **Elevated Surface / Card Substrate** | `#191816` | `var(--panel-2)` in `:root` |
| **Interactive Accent / Highlight** | `#22201e` | `var(--panel-3)` in `:root` |
| **Secondary / Muted Copy** | `#f4f2ec` | `var(--fg)` in `:root` |
| **Structural Hairline Border** | `#b6b2aa` | `var(--fg-2)` in `:root` |
| **Variable Token (`--glass`)** | `#1e1c1ab8` | `var(--glass)` in `:root` |
| **Variable Token (`--fg-3`)** | `#8f8a82` | `var(--fg-3)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--charge` | `0` | Design System Custom Token |
| `--orb` | `clamp(104px, 9vw, 136px)` | Dimension / Scale Token |
| `--sfx-ease` | `cubic-bezier(.16, 1, .3, 1)` | Motion / Easing Token |
| `--sfx-c` | `246, 205, 27` | Design System Custom Token |
| `--sfx-nudge` | `sfx-hop` | Design System Custom Token |
| `--pad` | `clamp(22px, 2.2vw, 34px)` | Layout / Spatial Grid Token |
| `--band-top` | `30px` | Dimension / Scale Token |
| `--fs` | `88px` | Dimension / Scale Token |
| `--bg` | `#000` | Canvas / Surface Token |
| `--panel` | `#121110` | Color / Atmospheric Token |
| `--panel-2` | `#191816` | Color / Atmospheric Token |
| `--panel-3` | `#22201e` | Color / Atmospheric Token |
| `--glass` | `#1e1c1ab8` | Color / Atmospheric Token |
| `--fg` | `#f4f2ec` | Typography Ink Token |
| `--fg-2` | `#b6b2aa` | Typography Ink Token |
| `--fg-3` | `#8f8a82` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav> — `levigav-com`)**:
   - Landmark `<header class="nav">` hosting `Levi Gavrilut · I build what I want ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-edition="gold"`, `data-welcome="out"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.nf__lead { font-family:var(--serif,serif);color:var(--yellow,f6cd1b);margin:0;font-... }`.
2. **Hero Stage & Focal Lead (<section.prologue> — `Choose your language · Alege-ți li`)**:
   - Landmark `<section class="prologue is-quiet">` presenting display lead `Choose your language · Alege-ți limba · Wähle dei...` and copy excerpt *"Jesus Christ Isus Hristos Jesus Christus"* over `#000` canvas and `#f4f2ec` ink.
3. **Primary Showcase & Content Grid (<article.pro-verse> — `Choose your edition · Alege-ți edi`)**:
   - Landmark `<article class="pro-verse">` rendering section `Choose your edition · Alege-ți ediția · Wähle dei...` with copy *"Welcome back Bine ai revenit Willkommen zurück"*, asset references (`1sm_p255ynpf-.css`, `2fu8m418vo0kb.css`, `2fo6lh-lqntob.css`, `2w31v64880cal.css`), and grid rule `.nf__verse { gap:10px;max-width:34em;margin:clamp(8px,2vw,18px) 0 0;display:grid }`.
4. **Interactive Detail & Feature Matrix (<section.hero> — `Levi Gavrilut`)**:
   - Landmark `<section class="hero shell">` framing `Levi Gavrilut` and `02 Home` (*"Jesus loves you Isus te iubește Jesus liebt dich"*) with `#191816` surface cards, `#22201e` accents, and `.nf__verse p { font-family:var(--serif,serif);color:var(--fg-2,b6b2aa);margin:0;font-si... }`.
5. **Colophon & Global Directory Footer (<footer.in-prologue> — `https://levigav.com`)**:
   - Landmark `<footer class="in-prologue">` anchoring `Levi Gavrilut · I build what I w` footer links (`Overview · Index · Archive · About · Contact`), copy *"LVG Street edition Ediția Street Street-Ausgabe Drop 001"*, and `#b6b2aa` structural dividers.
