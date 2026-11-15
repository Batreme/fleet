# UI & UX Architecture: www-remyshoots-co-za

## Overview & Design Identity
- **Target**: `www-remyshoots-co-za` (**Remy Shoots**)
- **Production URL**: [https://www.remyshoots.co.za/](https://www.remyshoots.co.za/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fcf8ef` canvas, `#111` ink, `#ff3131` accent)
- **Summary**: Documenting emotion, movement and meaning. Since ©2016 — the photography portfolio of Remy.
- **Total Clean CSS Variables Extracted**: `45` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter Fallback`
- **Monospace / Technical Font Stack**: `Roboto Mono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(13px,1.05vw,18px)`, `clamp(22px,1.69vw,30px)`, `.64em`, `.75rem`, `14px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(13px,1.05vw,18px)`, `clamp(22px,1.69vw,30px)`, `.64em`, `.75rem`, `14px`)
- **Body Copy**: rule `p` (`font-size: clamp(13px,1.05vw,18px)`, `line-height: 1.2`, `letter-spacing: -.04em`)
- **Metadata & Labels**: CSS variables `--font-mono: "Roboto Mono", "Roboto Mono Fallback"`, `--vt-meta-dur: .45s`, `--vt-meta-out-delay: 0s`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fcf8ef` | `var(--cream)` in `:root` |
| **Primary Typography Ink** | `#cbc7c2` | `var(--gray-150)` in `:root` |
| **Elevated Surface / Card Substrate** | `#b2aeab` | `var(--gray-200)` in `:root` |
| **Interactive Accent / Highlight** | `#ff3131` | `var(--red)` in `:root` |
| **Secondary / Muted Copy** | `#2e2e2e` | `var(--panel)` in `:root` |
| **Structural Hairline Border** | `#111` | `var(--bg)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `"Inter", "Inter Fallback"` | Typography / Scale Token |
| `--font-mono` | `"Roboto Mono", "Roboto Mono Fallback"` | Typography / Scale Token |
| `--cream` | `#fcf8ef` | Color / Atmospheric Token |
| `--gray-150` | `#cbc7c2` | Color / Atmospheric Token |
| `--gray-200` | `#b2aeab` | Color / Atmospheric Token |
| `--red` | `#ff3131` | Color / Atmospheric Token |
| `--panel` | `#2e2e2e` | Color / Atmospheric Token |
| `--bg` | `#111` | Canvas / Surface Token |
| `--stage-lift` | `24px` | Dimension / Scale Token |
| `--vcaret-x` | `calc(8.33vw + 219px)` | Dimension / Scale Token |
| `--vig-size` | `45%` | Layout / Spatial Grid Token |
| `--vig-radius` | `min(114vh, 114vw)` | Elevation / Border Token |
| `--vig-open` | `1.2` | Design System Custom Token |
| `--nav-caret-lane` | `28px` | Layout / Spatial Grid Token |
| `--nav-caret-gap` | `8px` | Layout / Spatial Grid Token |
| `--nav-caret-size` | `.9em` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.chrome> — `www-remyshoots-co-za`)**:
   - Landmark `<header class="chrome">` hosting `Remy Shoots` navigation (`works(21) works(21) · motion(8) motion(8) · About About · contact contact`), DOM attributes (`data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`, `data-sdkv="2.0.1"`, `data-disable-auto-track="1"`), and stylesheet rule `nter_d7e32889-module__94mdca__cla... { font-family:Inter,Inter Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<div.view-slider> — `RemyShoots ®`)**:
   - Landmark `<div class="view-slider">` presenting display lead `RemyShoots ®` and copy excerpt *"documenting emotion, documenting emotion, movement and meaning. m"* over `#fcf8ef` canvas and `#111` ink.
3. **Primary Showcase & Content Grid (<div.chrome-slider> — `documenting emotion, documenting e`)**:
   - Landmark `<div class="chrome-slider">` rendering section `documenting emotion, documenting emotion, moveme` with copy *"documenting emotion, documenting emotion,"*, asset references (`2f13ad8e538108e0-s.p.22iyan98j1_2...`, `83afe278b6a6bb3c-s.p.2bn3s6zvc0dy...`, `under-armour.svg`, `playhead.svg`), and grid rule `inter_d7e32889-module__94mdca__va... { --font-sans:"Inter", "Inter Fallback" }`.
4. **Interactive Detail & Feature Matrix (<div.chrome> — `documenting emotion, documenting e`)**:
   - Landmark `<div class="chrome">` framing `documenting emotion, documenting emotion,` and `documenting emotion,` (*"documenting emotion,"*) with `#b2aeab` surface cards, `#ff3131` accents, and `mono_955658b9-module__SfQagW__cla... { font-family:Roboto Mono,Roboto Mono Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.logo> — `https://www.remyshoots.co.za/`)**:
   - Landmark `<footer class="logo">` anchoring `Remy Shoots` footer links (`works(21) works(21) · motion(8) motion(8) · About About · contact contact`), copy *"movement and meaning. movement and meaning."*, and `#111` structural dividers.
