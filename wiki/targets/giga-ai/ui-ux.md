# UI & UX Architecture: giga-ai

## Overview & Design Identity
- **Target**: `giga-ai` (**Giga: AI support agents that improve your metrics**)
- **Production URL**: [https://giga.ai/](https://giga.ai/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#161413` / `#fb2c36`)
- **Summary**: Giga builds enterprise AI agents for customer support that resolve complex conversations across chat, voice, and email. Deployed in weeks...
- **Total Clean CSS Variables Extracted**: `531` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `InterVariable`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: CSS variables `--display: inter, interExt, "InterVariable", system-ui, sans-serif`, `--text-4xl: 2rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 2rem`, `line-height: 1.1`, `letter-spacing: var(--tracking-display)`, `font-weight: 400`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`, `--rx-body: 15px`; rule `p` (`font-size: 13.5px`, `line-height: 20px`)
- **Metadata & Labels**: CSS variables `--mono: "Geist Mono", ui-monospace, monospace`, `--key-mono: 400 11px/14px "Geist Mono", geistMono, monospace`, `--font-mono-source: "geistMono", "geistMono Fallback"`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#161413` | `var(--panel)` in `:root` |
| **Primary Typography Ink** | `#0b0a09` | `var(--cinema-room)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--cinema-ink)` in `:root` |
| **Interactive Accent / Highlight** | `#fb2c36` | `var(--color-red-500)` in `:root` |
| **Secondary / Muted Copy** | `#fcbb00` | `var(--color-amber-400)` in `:root` |
| **Structural Hairline Border** | `#00bb7f` | `var(--color-emerald-500)` in `:root` |
| **Variable Token (`--key-face`)** | `#3b3b3e` | `var(--key-face)` in `:root` |
| **Variable Token (`--key-face`)** | `#2a2a2d` | `var(--key-face)` in `:root` |
| **Variable Token (`--key-edge`)** | `#ffffff1f` | `var(--key-edge)` in `:root` |
| **Variable Token (`--key-lit`)** | `#ffffff14` | `var(--key-lit)` in `:root` |
| **Variable Token (`--key-ink`)** | `#e8edefe0` | `var(--key-ink)` in `:root` |
| **Variable Token (`--key-shadow`)** | `#00000080` | `var(--key-shadow)` in `:root` |
| **Variable Token (`--key-shadow`)** | `#0009` | `var(--key-shadow)` in `:root` |
| **Variable Token (`--key-ring`)** | `#e8edef99` | `var(--key-ring)` in `:root` |
| **Variable Token (`--okey-face`)** | `#f7732b` | `var(--okey-face)` in `:root` |
| **Variable Token (`--okey-face`)** | `#dd520c` | `var(--okey-face)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--sans` | `"Geist", system-ui, sans-serif` | Typography / Scale Token |
| `--mono` | `"Geist Mono", ui-monospace, monospace` | Typography / Scale Token |
| `--display` | `inter, interExt, "InterVariable", system-ui, sans-serif` | Dimension / Scale Token |
| `--text` | `inter, interExt, "InterVariable", system-ui, sans-serif` | Typography Ink Token |
| `--key-radius` | `8px` | Elevation / Border Token |
| `--key-face` | `linear-gradient(123.37deg, #3b3b3e 13.97%, #2a2a2d 87.5%)` | Color / Atmospheric Token |
| `--key-edge` | `#ffffff1f` | Color / Atmospheric Token |
| `--key-lit` | `inset 1px 1px 0 #ffffff14` | Color / Atmospheric Token |
| `--key-ink` | `#e8edefe0` | Typography Ink Token |
| `--key-shadow` | `4px 6px 5px #00000080, 2px 4px 2.5px #0009` | Elevation / Border Token |
| `--key-shadow-down` | `1px 2px 2px #00000080, 1px 1px 1px #0009` | Elevation / Border Token |
| `--key-hover` | `brightness(1.12)` | Design System Custom Token |
| `--key-ring` | `1.5px solid #e8edef99` | Elevation / Border Token |
| `--key-release` | `.15s cubic-bezier(.16,.84,.32,1)` | Motion / Easing Token |
| `--key-mono` | `400 11px/14px "Geist Mono", geistMono, monospace` | Typography / Scale Token |
| `--okey-face` | `linear-gradient(155.7deg, #f7732b 13.97%, #dd520c 87.5%)` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.docked> — `giga-ai`)**:
   - Landmark `<header class="docked">` hosting `Giga: AI support agents that improve` navigation (`Platform overview · Build agents · Observe outcomes · Improve with Scout · Agent Canvas`), DOM attributes (`data-theme="dark"`, `data-consent-region="gdpr"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.part { visibility:hidden }`.
2. **Hero Stage & Focal Lead (<section.banner-off> — `We value your privacy`)**:
   - Landmark `<section class="banner-off">` presenting display lead `We value your privacy` and copy excerpt *"We use cookies to run giga.ai, remember your preferences, measure"* over `#161413` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.hero-fixed> — `No time to wait.`)**:
   - Landmark `<section class="hero-fixed">` rendering section `No time to wait.` with copy *"Strictly necessary"*, asset references (`geist_mono_400_latin-s.p.2qleaeww...`, `geist_pixel_line-s.p.1gvmpev-r-ty...`, `geist_sans_400-s.p.18rrztdh9mmoo....`, `geist_sans_500-s.p.08803r3rti4jl....`), and grid rule `.part.on { visibility:visible }`.
4. **Interactive Detail & Feature Matrix (<section.armed> — `DoorDash handles delivery issues e`)**:
   - Landmark `<section class="armed">` framing `DoorDash handles delivery issues end to end with...` and `See what Giga would resolve at your company.` (*"Required for the site to work. Always active."*) with `#fff` surface cards, `#fb2c36` accents, and `.sh { opacity:var(--room);pointer-events:none;position:absolute }`.
5. **Colophon & Global Directory Footer (<footer.giga-cc--gdpr> — `https://giga.ai/`)**:
   - Landmark `<footer class="giga-cc--gdpr">` anchoring `Giga: AI support agents that imp` footer links (`Platform overview · Build agents · Observe outcomes · Improve with Scout · Agent Canvas`), copy *"Remembers choices like region and saved settings."*, and `#00bb7f` structural dividers.
