# UI & UX Architecture: www-ouiwill-com

## Overview & Design Identity
- **Target**: `www-ouiwill-com` (**Oui Will · Brand Transformation & Digital Experiences**)
- **Production URL**: [https://www.ouiwill.com/](https://www.ouiwill.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#878787`)
- **Summary**: Oui Will is an independent digital agency shaping ambitious brands through strategy, identity, digital experiences, and technology.
- **Total Clean CSS Variables Extracted**: `102` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `base`
- **Body Font Stack**: `sf`
- **Monospace / Technical Font Stack**: `mono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `18px`, `1.2rem`, `12px`, `13px`, `10px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `18px`, `1.2rem`, `12px`, `13px`, `10px`)
- **Body Copy**: rule `p` (`font-size: 1.2rem`, `line-height: 1.3`, `letter-spacing: -.02em`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `18px`, `1.2rem`, `12px`, `13px`, `10px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--aClkInk)` in `:root` |
| **Primary Typography Ink** | `#6b6c68` | `var(--aTitBase)` in `:root` |
| **Elevated Surface / Card Substrate** | `#060606` | `var(--autoTX)` in `:root` |
| **Interactive Accent / Highlight** | `#878787` | `var(--autoLI)` in `:root` |
| **Secondary / Muted Copy** | `#9f9f9f` | `var(--autoL)` in `:root` |
| **Structural Hairline Border** | `#6b6c69` | `.sizes { background: #6b6c69 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--csk-rev` | `"csk-ffec67d3-72a4-404e-9353-3cf2742cdeb5"` | Design System Custom Token |
| `--Tprg` | `0` | Design System Custom Token |
| `--mobileMax` | `834` | Design System Custom Token |
| `--resp` | `1194` | Design System Custom Token |
| `--padgrid` | `4rem` | Layout / Spatial Grid Token |
| `--multi` | `calc(((100vw - 1440px) / 1440 * -5))` | Dimension / Scale Token |
| `--prg1` | `1` | Design System Custom Token |
| `--prg2` | `1` | Design System Custom Token |
| `--bndB` | `calc(100% * var(--bnd,.15))` | Dimension / Scale Token |
| `--bndS` | `calc(100% + 2 * var(--bndB))` | Dimension / Scale Token |
| `--hovS` | `calc(var(--hovt,.7) * var(--hovd,1))` | Design System Custom Token |
| `--hovO` | `min(0, var(--hovS))` | Design System Custom Token |
| `--hovd` | `-1` | Design System Custom Token |
| `--padgut` | `calc(var(--gutgrid) + var(--padgrid))` | Layout / Spatial Grid Token |
| `--padgut-s` | `calc(var(--gutgrid) + var(--padgrid-s))` | Layout / Spatial Grid Token |
| `--sizegrid` | `calc(100vw - ((var(--padgut)) * 2))` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.nav> — `www-ouiwill-com`)**:
   - Landmark `<nav class="nav">` hosting `Oui Will · Brand Transformation & Di` navigation (`Home Home · Work Work · About About · Careers Careers · Awwwards`), DOM attributes (`data-deck="[("lg":"/uploads/fina..."`, `data-req="true"`, `data-engine="three.js r182 webgpu"`, `data-id="contact"`), and stylesheet rule `root { --csk-rev:"csk-ffec67d3-72a4-404e-9353-3cf2742cdeb5" }`.
2. **Hero Stage & Focal Lead (<section.home_intro> — `Shaping the next generation of bra`)**:
   - Landmark `<section class="home_intro">` presenting display lead `Shaping the next generation of brands that matter...` and copy excerpt *"We use essential cookies to make this site work. Analytics and ad"* over `#fff` canvas and `#060606` ink.
3. **Primary Showcase & Content Grid (<section.home_reel> — `About`)**:
   - Landmark `<section class="home_reel GRI-vw">` rendering section `About` with copy *"Accept all Accept all"*, asset references (`favicon.svg`, `favicon.ico`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `after { box-sizing:border-box }`.
4. **Interactive Detail & Feature Matrix (<section.home_aboutlog> — `Selected Work Selected Work`)**:
   - Landmark `<section class="home_aboutlog GRI">` framing `Selected Work Selected Work` and `Oura` (*"Cookie settings Cookie settings"*) with `#060606` surface cards, `#878787` accents, and `html { -webkit-text-size-adjust:none;-moz-text-size-adjust:none;text-size-adjus... }`.
5. **Colophon & Global Directory Footer (<footer.foot> — `https://www.ouiwill.com/`)**:
   - Landmark `<footer class="foot">` anchoring `Oui Will · Brand Transformation ` footer links (`Home Home · Work Work · About About · Careers Careers · Awwwards`), copy *"They make the site work: session, security and your preferen"*, and `#6b6c69` structural dividers.
