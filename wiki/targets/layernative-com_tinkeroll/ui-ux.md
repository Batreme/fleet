# UI & UX Architecture: layernative-com_tinkeroll

## Overview & Design Identity
- **Target**: `layernative-com_tinkeroll` (**Tinkeroll — Build the road. Tilt the marble.**)
- **Production URL**: [https://layernative.com/tinkeroll/](https://layernative.com/tinkeroll/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f3efe7` / `#4a453d`)
- **Summary**: Tinkeroll is a tilt-to-roll puzzle game for iPhone and iPad. Place the missing pieces, tilt your phone, and roll the marble home. 52 leve...
- **Total Clean CSS Variables Extracted**: `23` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `Geist Mono`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(48px, 7vw, 92px)`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 28px`)
- **Body Copy**: rule `p` (`font-size: 15px`, `line-height: 1.55`)
- **Metadata & Labels**: CSS variables `--mono: "Geist Mono", ui-monospace, SFMono-Regular, Menlo, monospace`; rule `.label` (`font-size: 9px`, `letter-spacing: .08em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f3efe7` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#e9e3d8` | `var(--paper-2)` in `:root` |
| **Elevated Surface / Card Substrate** | `#15130f` | `var(--ink)` in `:root` |
| **Interactive Accent / Highlight** | `#4a453d` | `var(--ink-2)` in `:root` |
| **Secondary / Muted Copy** | `#8a8378` | `var(--ink-3)` in `:root` |
| **Structural Hairline Border** | `#d9663f` | `var(--accent)` in `:root` |
| **Variable Token (`--gold`)** | `#c9a24a` | `var(--gold)` in `:root` |
| **Variable Token (`--sage`)** | `#8fb39a` | `var(--sage)` in `:root` |
| **Variable Token (`--night`)** | `#0e1024` | `var(--night)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#f3efe7` | Canvas / Surface Token |
| `--fg` | `var(--ink)` | Typography Ink Token |
| `--paper` | `#f3efe7` | Canvas / Surface Token |
| `--paper-2` | `#e9e3d8` | Canvas / Surface Token |
| `--ink` | `#15130f` | Typography Ink Token |
| `--ink-2` | `#4a453d` | Typography Ink Token |
| `--ink-3` | `#8a8378` | Typography Ink Token |
| `--line` | `rgba(21, 19, 15, .14)` | Color / Atmospheric Token |
| `--accent` | `#d9663f` | Brand / Palette Token |
| `--gold` | `#c9a24a` | Color / Atmospheric Token |
| `--sage` | `#8fb39a` | Color / Atmospheric Token |
| `--night` | `#0e1024` | Color / Atmospheric Token |
| `--radius` | `22px` | Elevation / Border Token |
| `--wrap` | `1240px` | Layout / Spatial Grid Token |
| `--serif` | `"Geist", ui-sans-serif, system-ui, -apple-system, sans-serif` | Typography / Scale Token |
| `--sans` | `"Geist", ui-sans-serif, system-ui, -apple-system, sans-serif` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav> — `layernative-com_tinkeroll`)**:
   - Landmark `<header class="nav">` hosting `Tinkeroll — Build the road. Tilt the` navigation (`Worlds · Parts box · Tournaments · FAQ`), DOM attributes (`data-load`, `data-load-dots`, `data-engine="three.js r160"`, `data-text="Tinkeroll"`), and stylesheet rule `.home { overflow-x: clip; }`.
2. **Hero Stage & Focal Lead (<section.s-hero> — `B u i l d t h e r o a d . T i l t `)**:
   - Landmark `<section class="s-hero">` presenting display lead `B u i l d t h e r o a d . T i l t t h e m a r b l...` and copy excerpt *"Laying the road ..."* over `#f3efe7` canvas and `#15130f` ink.
3. **Primary Showcase & Content Grid (<section.s-missing> — `E v e r y l e v e l i s m i s s i `)**:
   - Landmark `<section class="s-missing">` rendering section `E v e r y l e v e l i s m i s s i n g a f e w p i...` with copy *"Compete Tournaments"*, asset references (`icon-64.png`, `icon-180.png`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `world { position: fixed; inset: 0; width: 100vw; height: 100vh; height: 100lvh;... }`.
4. **Interactive Detail & Feature Matrix (<section.s-world> — `Place the pieces`)**:
   - Landmark `<section class="s-world w-left">` framing `Place the pieces` and `Tilt your phone` (*"Support Privacy hello@layernative.com"*) with `#15130f` surface cards, `#4a453d` accents, and `.no-gl body { background: linear-gradient(cfdde6, f3efe7 40%, e6cfd6 70%, 0e1024); }`.
5. **Colophon & Global Directory Footer (<footer.foot> — `https://layernative.com/tinkeroll/`)**:
   - Landmark `<footer class="foot">` anchoring `Tinkeroll — Build the road. Tilt` footer links (`Worlds · Parts box · Tournaments · FAQ`), copy *"hello@layernative.com"*, and `#d9663f` structural dividers.
