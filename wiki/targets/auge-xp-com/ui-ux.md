# UI & UX Architecture: auge-xp-com

## Overview & Design Identity
- **Target**: `auge-xp-com` (**Digital Experience Studio · AUGE Experience**)
- **Production URL**: [https://auge-xp.com/](https://auge-xp.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#fdf48b`)
- **Summary**: AUGE Experience is an independent digital experience studio creating websites, digital products, interactive installations and creative t...
- **Total Clean CSS Variables Extracted**: `37` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `ppNeueMontreal`
- **Body Font Stack**: `ppNeueMontreal Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--font-farnham-display: "farnhamDisplay", "farnhamDisplay Fallback"`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-content-lg)`, `var(--text-content-md)`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-content-lg)`, `var(--text-content-md)`)
- **Metadata & Labels**: CSS variables `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#edeee5` | `var(--color-background)` in `:root` |
| **Interactive Accent / Highlight** | `#fdf48b` | `var(--color-accent)` in `:root` |
| **Secondary / Muted Copy** | `#0000` | `textarea { background-color: #0000 }` |
| **Structural Hairline Border** | `#000000` | `.bg-black { background-color: black }` (`#000000`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `"ppNeueMontreal", "ppNeueMontreal Fallback"` | Typography / Scale Token |
| `--font-greed-bold` | `"greedBold", "greedBold Fallback"` | Typography / Scale Token |
| `--font-farnham-display` | `"farnhamDisplay", "farnhamDisplay Fallback"` | Typography / Scale Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--leading-tight` | `1.25` | Typography / Scale Token |
| `--leading-normal` | `1.5` | Typography / Scale Token |
| `--aspect-video` | `16 / 9` | Design System Custom Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |
| `--color-background` | `#edeee5` | Canvas / Surface Token |
| `--color-foreground` | `#000` | Typography Ink Token |
| `--color-accent` | `#fdf48b` | Brand / Palette Token |
| `--font-greed` | `var(--font-greed-bold), sans-serif` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.text-foreground> — `auge-xp-com`)**:
   - Landmark `<header class="text-foreground">` hosting `Digital Experience Studio · AUGE Exp` navigation (`Works · About · Let's talk`), DOM attributes (`data-precedence="next"`, `data-cbid="ced38b07-60a9-4c9f-ba..."`, `data-blockingmode="auto"`, `data-culture="EN"`), and stylesheet rule `real_f02daa13-module__qtcTEa__cla... { font-family:ppNeueMontreal,ppNeueMontreal Fallback }`.
2. **Hero Stage & Focal Lead (<main.relative> — `Viru Group`)**:
   - Landmark `<main class="relative min-h-dvh">` presenting display lead `Viru Group` and copy excerpt *"Necessary 2 Necessary cookies help make a website usable by enabl"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<main.relative> — `Maison AUGE`)**:
   - Landmark `<main class="relative min-h-dvh">` rendering section `Maison AUGE` with copy *"Cookiebot 1 Learn more about this provider CookieConsent Stores t"*, asset references (`HJGhjOeW_p3Yd8NW_viru-cover.3.jpg`, `nTk2Qb6LITpLW8TG_maison_cover.jpg`, `pUkcTZHGA7KhlJZ0_lunarossa_cover_...`, `VsNqcjWTy0U8igpA_don-molinico-cov...`), and grid rule `treal_f02daa13-module__qtcTEa__va... { --font-sans:"ppNeueMontreal", "ppNeueMontreal Fallback" }`.
4. **Interactive Detail & Feature Matrix (<main.relative> — `AC40 Lunarossa`)**:
   - Landmark `<main class="relative min-h-dvh">` framing `AC40 Lunarossa` and `Don Molinico` (*"Learn more about this provider"*) with `#edeee5` surface cards, `#fdf48b` accents, and `font-face { font-family:greedBold;src:url(../media/Greed_Bold-s.p.2gpcionblp7lf.woff... }`.
5. **Colophon & Global Directory Footer (<footer.CybotCookiebotDialogContentWrapper> — `https://auge-xp.com/`)**:
   - Landmark `<footer class="CybotCookiebotDialogContentWrapper">` anchoring `Digital Experience Studio · AUGE` footer links (`Works · About · Let's talk`), copy *"Stores the user's cookie consent state for the current domai"*, and `#000000` structural dividers.
