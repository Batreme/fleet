# UI & UX Architecture: www-rtmaudio-com

## Overview & Design Identity
- **Target**: `www-rtmaudio-com` (**RTM Audio · Audio plug-ins for mixing and mastering**)
- **Production URL**: [https://www.rtmaudio.com](https://www.rtmaudio.com)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0e0f10` / `#b08b5c`)
- **Summary**: Mixing and mastering plug-ins, built by working engineers. Judge the change. Not the volume.
- **Total Clean CSS Variables Extracted**: `72` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Instrument Serif`
- **Body Font Stack**: `Outfit`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **Hero Display (`H1`)**: CSS variables `--display-weight: 500`, `--t-display: clamp(3.0518rem,2.3212rem + 2.7188vw,4.7684rem)`, `--lh-display: .94`; rule `h1` (`letter-spacing: -.02em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(2.8rem,8vw,8rem)`, `line-height: .84`, `letter-spacing: -.045em`, `font-weight: 500`)
- **Body Copy**: CSS variables `--t-body: 1rem`, `--lh-body: 24px`, `--tr-body: 0`; rule `body` (`letter-spacing: .018em`)
- **Metadata & Labels**: CSS variables `--mono: "JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace`, `--t-label: .8rem`, `--m-label: .8rem`; rule `small` (`font-size: .65rem`, `letter-spacing: .13em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0e0f10` | `var(--void)` in `:root` |
| **Primary Typography Ink** | `#f0e9dc` | `var(--ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#d6c5a3` | `var(--ink-2)` in `:root` |
| **Interactive Accent / Highlight** | `#b08b5c` | `var(--ink-dim)` in `:root` |
| **Secondary / Muted Copy** | `#57c279` | `var(--green)` in `:root` |
| **Structural Hairline Border** | `#07080a` | `var(--well)` in `:root` |
| **Variable Token (`--raise`)** | `#121315` | `var(--raise)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--display-weight` | `500` | Design System Custom Token |
| `--void` | `#0e0f10` | Color / Atmospheric Token |
| `--ink` | `#f0e9dc` | Typography Ink Token |
| `--ink-2` | `#d6c5a3` | Typography Ink Token |
| `--ink-dim` | `#b08b5c` | Typography Ink Token |
| `--green` | `#57c279` | Color / Atmospheric Token |
| `--line` | `rgba(240,233,220,.10)` | Color / Atmospheric Token |
| `--line-2` | `rgba(240,233,220,.22)` | Color / Atmospheric Token |
| `--wash` | `rgba(240,233,220,.05)` | Color / Atmospheric Token |
| `--well` | `#07080a` | Color / Atmospheric Token |
| `--raise` | `#121315` | Color / Atmospheric Token |
| `--glass` | `rgba(14,15,16,.72)` | Color / Atmospheric Token |
| `--acc` | `#b08b5c` | Color / Atmospheric Token |
| `--edge` | `inset 0 1px 0 rgba(240,233,220,.07)` | Color / Atmospheric Token |
| `--e1` | `var(--edge),0 1px 0 rgba(0,0,0,.5),0 34px 68px -34px rgba(0,0,0,.7)` | Color / Atmospheric Token |
| `--vignette` | `inset 0 0 34px 6px rgba(0,0,0,.55),inset 0 0 96px 20px rgba(8,6,4,.34)` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.campaigns-head> — `www-rtmaudio-com`)**:
   - Landmark `<header class="campaigns-head">` hosting `RTM Audio · Audio plug-ins for mixin` navigation (`Plugins Plugins · Store Store · About About · Account Account`), DOM attributes (`data-consent="pending"`, `data-i18n-key="RTM Audio · Audio plu..."`, `data-i18n-content="Mixing and mastering..."`, `data-i18n-content="Mixing and mastering..."`), and stylesheet rule `root { --display-weight:500; }`.
2. **Hero Stage & Focal Lead (<section.take> — `Judge the change. Not the volume.`)**:
   - Landmark `<section class="take">` presenting display lead `Judge the change. Not the volume.` and copy excerpt *"See the Black Friday page →"* over `#0e0f10` canvas and `#f0e9dc` ink.
3. **Primary Showcase & Content Grid (<section.campaigns> — `CXB`)**:
   - Landmark `<section class="campaigns">` rendering section `CXB` with copy *"Starts Mon 16 Nov, 18:00 CET"*, asset references (`soehne-breit-kraftig.woff2`, `fonts.css`, `site.css`, `black-friday-poster.js`), and grid rule `body { letter-spacing:.018em }`.
4. **Interactive Detail & Feature Matrix (<article.campaign-panel> — `One knob moves the pair.`)**:
   - Landmark `<article class="campaign-panel material-light">` framing `One knob moves the pair.` and `Depth and Speed, band by band.` (*"Every plug-in on sale until Wed 2 Dec, 08:59 CET."*) with `#d6c5a3` surface cards, `#b08b5c` accents, and `.hero h1 { letter-spacing:-.02em }`.
5. **Colophon & Global Directory Footer (<footer.cn-ground> — `https://www.rtmaudio.com`)**:
   - Landmark `<footer class="cn-ground">` anchoring `RTM Audio · Audio plug-ins for m` footer links (`Plugins Plugins · Store Store · About About · Account Account`), copy *"May Meta and Microsoft see your visit? If you accept, Meta, "*, and `#07080a` structural dividers.
