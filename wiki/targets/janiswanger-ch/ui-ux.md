# UI & UX Architecture: janiswanger-ch

## Overview & Design Identity
- **Target**: `janiswanger-ch` (**Janis Wanger — Creative Engineer in Bern**)
- **Production URL**: [https://janiswanger.ch](https://janiswanger.ch)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#e5e5e5`)
- **Summary**: Portfolio of Janis Wanger, a creative Frontend Engineer in Bern working across design and code. Projects, experience, and how to get in t...
- **Total Clean CSS Variables Extracted**: `76` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `PolySans`
- **Body Font Stack**: `Georgia`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.36rem`, `1em`, `80%`, `75%`, `var(--text-xs)`)
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: 1.33333`
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: 1.5`
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: 1.33333`, `--text-sm: .875rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#5bb872` | `var(--color-focus)` in `:root` |
| **Interactive Accent / Highlight** | `#e5e5e5` | `var(--color-surface)` in `:root` |
| **Secondary / Muted Copy** | `#ff8a3d` | `var(--color-accent)` in `:root` |
| **Structural Hairline Border** | `#341804` | `var(--color-on-accent)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `PolySans, ui-sans-serif, system-ui, sans-serif` | Typography / Scale Token |
| `--font-serif` | `Georgia, ui-serif, "Times New Roman", Times, serif` | Typography / Scale Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `1.33333` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `1.42857` | Typography Ink Token |
| `--text-base` | `1rem` | Typography Ink Token |
| `--text-base--line-height` | `1.5` | Typography Ink Token |
| `--text-lg` | `1.125rem` | Typography Ink Token |
| `--text-lg--line-height` | `1.55556` | Typography Ink Token |
| `--text-2xl` | `1.5rem` | Typography Ink Token |
| `--text-2xl--line-height` | `1.33333` | Typography Ink Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--font-weight-semibold` | `600` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.hero-home> — `janiswanger-ch`)**:
   - Landmark `<header class="hero-home relative">` hosting `Janis Wanger — Creative Engineer in ` navigation (`Main navigation · Skip to content`), DOM attributes (`data-hid="canonical"`, `data-hid="hreflang-de-CH"`, `data-hid="hreflang-en"`, `data-hid="hreflang-x-default"`), and stylesheet rule `webkit-media-controls { display:none!important }`.
2. **Hero Stage & Focal Lead (<section.py-32> — `Janis is a Bern-based creative Fro`)**:
   - Landmark `<section class="py-32 relative">` presenting display lead `Janis is a Bern-based creative Frontend Engineer...` and copy excerpt *"Janis Wanger Frontend Engineer"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.py-32> — `Soft skills`)**:
   - Landmark `<section class="py-32 relative">` rendering section `Soft skills` with copy *"O P E N T O G E T T I N G H I R E D ☆ ♡ ✧ O P E N T O G E T T I N"*, asset references (`entry.I4GIEjMK.css`, `HireBadge.BgIwIulx.css`, `AutoplayVideo.ulh4C2Gx.css`, `B7fVWpKZ.js`), and grid rule `it-media-controls-start-playback-... { display:none!important }`.
4. **Interactive Detail & Feature Matrix (<article.skills-enter> — `Technical skills`)**:
   - Landmark `<article class="skills-enter relative">` framing `Technical skills` and `Want to work together ?` (*"Sometimes the frequencies just match"*) with `#5bb872` surface cards, `#e5e5e5` accents, and `before { content:"";pointer-events:none;border-radius:50%;position:absolute;inset... }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://janiswanger.ch`)**:
   - Landmark `<footer class="site-footer relative">` anchoring `Janis Wanger — Creative Engineer` footer links (`Main navigation · Skip to content`), copy *"so beautiful patterns emerge."*, and `#341804` structural dividers.
