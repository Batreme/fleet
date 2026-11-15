# UI & UX Architecture: robertoattanasio-com_en

## Overview & Design Identity
- **Target**: `robertoattanasio-com_en` (**Roberto Attanasio**)
- **Production URL**: [https://robertoattanasio.com/en](https://robertoattanasio.com/en)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#222`)
- **Summary**: I write code by day and words by night. Projects, music and poems, all hidden in my digital world: drag the field and find them.
- **Total Clean CSS Variables Extracted**: `66` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Mononoki`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: `Mononoki`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `.875rem`, `.75rem`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `.875rem`, `.75rem`)
- **Body Copy**: CSS variables `--text-base: 1rem`; rule `,body` (`line-height: 1.5`)
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-sm: .875rem`, `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--margo-color-neutral)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--margo-color-on-neutral)` in `:root` |
| **Elevated Surface / Card Substrate** | `#eceaea` | `var(--margo-color-main)` in `:root` |
| **Interactive Accent / Highlight** | `#222` | `var(--margo-color-on-main)` in `:root` |
| **Secondary / Muted Copy** | `#9c0ea3` | `var(--margo-color-primary)` in `:root` |
| **Structural Hairline Border** | `#7d0b82` | `var(--margo-color-primary-darken)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-md` | `28rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-base` | `1rem` | Typography Ink Token |
| `--text-xl` | `1.75rem` | Typography Ink Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--tracking-widest` | `.1em` | Typography / Scale Token |
| `--leading-relaxed` | `1.625` | Typography / Scale Token |
| `--ease-out` | `cubic-bezier(0, 0, .2, 1)` | Motion / Easing Token |
| `--blur-sm` | `8px` | Elevation / Border Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |
| `--font-primary` | `var(--margo-font-family-primary)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.fixed> — `robertoattanasio-com_en`)**:
   - Landmark `<header class="fixed top-6">` hosting `Roberto Attanasio` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="default"`, `data-root="true"`, `data-cursor="idle"`, `data-scrim-anchor="true"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.sr-only> — `Roberto Attanasio`)**:
   - Landmark `<section class="sr-only">` presenting display lead `Roberto Attanasio` and copy excerpt *"Hi, I'm a Frontend Web Developer with five years of experience."* over `#fff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<article.flex> — `Hi, I'm a Frontend Web Developer w`)**:
   - Landmark `<article class="flex flex-col">` rendering section `Hi, I'm a Frontend Web Developer with five years` with copy *"I write code by day and words by night. In between there's the pi"*, asset references (`index-D4Xf2DBZ.css`, `index-D8wnR5rE.js`, `route-C0O9SbwD.js`, `use-cursor-hint-Yyqb97NY.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<article.flex> — `I write code by day and words by n`)**:
   - Landmark `<article class="flex flex-col">` framing `I write code by day and words by night. In betwe` and `r.attanasio90@gmail.com r.attanasio90@gmail.com ` (*"r.attanasio90@gmail.com r.attanasio90@gmail.com *86V6+--·2V-7:X8R"*) with `#eceaea` surface cards, `#222` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.flex> — `https://robertoattanasio.com/en`)**:
   - Landmark `<footer class="flex">` anchoring `Roberto Attanasio` footer links (`Overview · Index · Archive · About · Contact`), copy *"r.attanasio90@gmail.com"*, and `#7d0b82` structural dividers.
