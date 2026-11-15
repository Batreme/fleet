# UI & UX Architecture: akaiito-ai

## Overview & Design Identity
- **Target**: `akaiito-ai` (**Akai Ito — Your twin dates millions. You go on one date.**)
- **Production URL**: [https://akaiito.ai](https://akaiito.ai)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ecebe5` / `#e4322b`)
- **Summary**: Akai Ito builds a digital twin of you. It goes on millions of first dates, lives ten thousand lives with your best match, then books one...
- **Total Clean CSS Variables Extracted**: `28` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geist Fallback`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `clamp(3rem, 7vw, 7.75rem)`, `clamp(2.375rem, 5vw, 5.5rem)`, `clamp(1.75rem, 2.6vw, 2.75rem)`, `clamp(1rem, 1.3vw, 1.25rem)`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(44px, 6.4vw, 120px)`)
- **Body Copy**: rule `p` (`font-size: .9375rem`)
- **Metadata & Labels**: CSS variables `--mono: "Geist","Geist Fallback","Inter",system-ui,sans-serif`; rule `small` (`font-size: .74rem`, `line-height: 1.25`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ecebe5` | `var(--paper)` in `:root` |
| **Primary Typography Ink** | `#111113` | `var(--ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fbfaf7` | `var(--card)` in `:root` |
| **Interactive Accent / Highlight** | `#e4322b` | `var(--red)` in `:root` |
| **Secondary / Muted Copy** | `#6f6e6a` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#1a73e8` | `var(--blue)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--fit` | `1` | Design System Custom Token |
| `--paper` | `#ecebe5` | Canvas / Surface Token |
| `--ink` | `#111113` | Typography Ink Token |
| `--card` | `#fbfaf7` | Color / Atmospheric Token |
| `--red` | `#e4322b` | Color / Atmospheric Token |
| `--muted` | `#6f6e6a` | Color / Atmospheric Token |
| `--line` | `rgba(17,17,19,.12)` | Color / Atmospheric Token |
| `--blue` | `#1a73e8` | Color / Atmospheric Token |
| `--sans` | `"Geist","Geist Fallback","Inter",system-ui,-apple-system,sans-serif` | Typography / Scale Token |
| `--mono` | `"Geist","Geist Fallback","Inter",system-ui,sans-serif` | Typography / Scale Token |
| `--ii` | `clamp(1.125rem, 2.4vw, 1.875rem)` | Dimension / Scale Token |
| `--tr` | `-.8deg` | Design System Custom Token |
| `--nf` | `var(--ink)` | Design System Custom Token |
| `--nr` | `-1.2deg` | Design System Custom Token |
| `--cr` | `1.6deg` | Design System Custom Token |
| `--bg` | `#ecebe5` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.ahd> — `akaiito-ai`)**:
   - Landmark `<header class="ahd">` hosting `Akai Ito — Your twin dates millions.` navigation (`Akai Ito · App · How it works · The model · Simulation`), DOM attributes (`data-slot="head"`, `data-d="-1"`, `data-d="1"`, `data-slot="body"`), and stylesheet rule `html { background:var(--paper);font-size:16px;overflow-x:clip }`.
2. **Hero Stage & Focal Lead (<section.sec> — `Akai Ito — your twin dates million`)**:
   - Landmark `<section class="sec opener">` presenting display lead `Akai Ito — your twin dates millions. You go on on...` and copy excerpt *"100% · Tying the thread"* over `#ecebe5` canvas and `#111113` ink.
3. **Primary Showcase & Content Grid (<section.hero> — `Your twin dates millions. You go o`)**:
   - Landmark `<section class="hero sec">` rendering section `Your twin dates millions. You go on one date.` with copy *"Akai Ito is for grown-ups. Are you 18 or older?"*, asset references (`icon.webp`, `favicon.png`, `apple-touch.png`, `phone.webp`), and grid rule `body { overflow-x:clip }`.
4. **Interactive Detail & Feature Matrix (<section.sec> — `1 window awake on this block Every`)**:
   - Landmark `<section class="sec appsec">` framing `1 window awake on this block Everyone you could l...` and `Your twin lives in your pocket.` (*"Come back on your 18th birthday. Your twin will wait."*) with `#fbfaf7` surface cards, `#e4322b` accents, and `stage { position:fixed;inset:0;width:100%;height:100%;display:block;z-index:0 }`.
5. **Colophon & Global Directory Footer (<footer.anim-off> — `https://akaiito.ai`)**:
   - Landmark `<footer class="anim-off">` anchoring `Akai Ito — Your twin dates milli` footer links (`Akai Ito · App · How it works · The model · Simulation`), copy *"Akai Ito is a concept for an AI dating service. You connect "*, and `#1a73e8` structural dividers.
