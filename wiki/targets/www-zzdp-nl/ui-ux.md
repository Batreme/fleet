# UI & UX Architecture: www-zzdp-nl

## Overview & Design Identity
- **Target**: `www-zzdp-nl` (**Al meer dan 70 jaar betekenisvolle architectuur · ZZDP**)
- **Production URL**: [https://www.zzdp.nl/](https://www.zzdp.nl/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#8746e3` ink, `#c7c6be` accent)
- **Summary**: Bij ZZDP combineren we vakmanschap en visie in betekenisvolle architectuur. Met meer dan 70 jaar ervaring realiseren we ontwerpen waarin...
- **Total Clean CSS Variables Extracted**: `207` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `helveticaNowDisplay`
- **Body Font Stack**: `helveticaNowDisplay Fallback`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--font-helvetica-now-display: "helveticaNowDisplay", "helveticaNowDisplay Fallback"`; rule `h1` (`font-size: 13.3333vw`, `line-height: 82%`, `letter-spacing: -.07em`, `font-weight: 400`)
- **Section Heading (`H2`)**: CSS variables `--subtitle-color: #656657`; rule `h2` (`font-size: 8vw`, `line-height: 105%`, `letter-spacing: .01em`, `font-weight: 400`)
- **Body Copy**: CSS variables `--body-color: #656657`; rule `p` (`font-size: 3.73333vw`, `line-height: 132%`, `letter-spacing: 0`, `font-weight: 400`)
- **Metadata & Labels**: CSS variables `--primary-ui-label-default-color: #fff`, `--primary-ui-label-hover-color: #fff`, `--primary-ui-label-disabled-color: #c7c6be`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--background-color)` in `:root` |
| **Primary Typography Ink** | `#656657` | `var(--title-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#8746e3` | `var(--accent-color)` in `:root` |
| **Interactive Accent / Highlight** | `#c7c6be` | `var(--primary-ui-label-disabled-color)` in `:root` |
| **Secondary / Muted Copy** | `#b5b899` | `var(--primary-ui-background-hover-color)` in `:root` |
| **Structural Hairline Border** | `#ebeae1` | `var(--primary-ui-background-disabled-color)` in `:root` |
| **Variable Token (`--line-color`)** | `#1a163019` | `var(--line-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background-color` | `#fff` | Canvas / Surface Token |
| `--title-color` | `#656657` | Brand / Palette Token |
| `--subtitle-color` | `#656657` | Brand / Palette Token |
| `--body-color` | `#656657` | Typography Ink Token |
| `--line-color` | `#1a163019` | Brand / Palette Token |
| `--accent-color` | `#8746e3` | Brand / Palette Token |
| `--primary-ui-label-default-color` | `#fff` | Brand / Palette Token |
| `--primary-ui-label-hover-color` | `#fff` | Brand / Palette Token |
| `--primary-ui-label-disabled-color` | `#c7c6be` | Brand / Palette Token |
| `--primary-ui-background-default-color` | `#656657` | Canvas / Surface Token |
| `--primary-ui-background-hover-color` | `#b5b899` | Canvas / Surface Token |
| `--primary-ui-background-disabled-color` | `#ebeae1` | Canvas / Surface Token |
| `--primary-ui-stroke-default-color` | `#656657` | Brand / Palette Token |
| `--primary-ui-stroke-hover-color` | `#b5b899` | Brand / Palette Token |
| `--primary-ui-stroke-disabled-color` | `#ebeae1` | Brand / Palette Token |
| `--secondary-ui-label-default-color` | `#656657` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.lenis> — `www-zzdp-nl`)**:
   - Landmark `<nav class="lenis">` hosting `Al meer dan 70 jaar betekenisvolle a` navigation (`Home · Projecten · Over ons · Nieuws en inzichten · Vacatures`), DOM attributes (`data-next-head`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`), and stylesheet rule `.u-underline-link:after { height:.266667vw }`.
2. **Hero Stage & Focal Lead (<section.theme--mossLight> — `ZZDP`)**:
   - Landmark `<section class="theme--mossLight">` presenting display lead `ZZDP` and copy excerpt *"Deze website gebruikt essentiële cookies voor functionaliteit en "* over `#fff` canvas and `#8746e3` ink.
3. **Primary Showcase & Content Grid (<section.vjs-styles-dimensions> — `Bij ZZDP geloven wij dat architect`)**:
   - Landmark `<section class="vjs-styles-dimensions">` rendering section `Bij ZZDP geloven wij dat architectuur meer is dan...` with copy *"Accepteren Accepteren"*, asset references (`favicon.svg`, `HelveticaNowDisplay_Regular-s.p.1...`, `HelveticaNowDisplay_Md-s.p.16ns3u...`, `PPNeueMachina_PlainRegular-s.p.39...`), and grid rule `.default-in-animation { transform:translateY(26.6667vw) }`.
4. **Interactive Detail & Feature Matrix (<section.theme--white> — `Ons Werk`)**:
   - Landmark `<section class="theme--white">` framing `Ons Werk` and `Nieuws` (*"Instellingen Instellingen"*) with `#8746e3` surface cards, `#c7c6be` accents, and `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;line-height:1.15 }`.
5. **Colophon & Global Directory Footer (<footer.theme--white> — `https://www.zzdp.nl/`)**:
   - Landmark `<footer class="theme--white">` anchoring `Al meer dan 70 jaar betekenisvol` footer links (`Home · Projecten · Over ons · Nieuws en inzichten · Vacatures`), copy *"Nieuws en inzichten"*, and `#ebeae1` structural dividers.
