# UI & UX Architecture: members-play-lacoste-com_ace-breaker-rg

## Overview & Design Identity
- **Target**: `members-play-lacoste-com_ace-breaker-rg` (**Lacoste - Ace breaker**)
- **Production URL**: [https://members-play.lacoste.com/ace-breaker-rg](https://members-play.lacoste.com/ace-breaker-rg)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#b762ff` / `#ee5f62`)
- **Summary**: Play and break as many bricks as you can
- **Total Clean CSS Variables Extracted**: `51` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `MonaSans`
- **Body Font Stack**: `Arial`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: var(--title)`, `line-height: 1.1`, `letter-spacing: -.06em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 1.5em`, `font-weight: bold`)
- **Body Copy**: rule `p` (`font-size: 20px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--cta-text)`, `1em`, `14px`, `var(--home-title)`, `.4em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#b762ff` | `var(--bonus-racket)` in `:root` |
| **Primary Typography Ink** | `#f58c58` | `var(--bonus-multiball)` in `:root` |
| **Elevated Surface / Card Substrate** | `#50caff` | `var(--bonus-defensive-wall)` in `:root` |
| **Interactive Accent / Highlight** | `#ee5f62` | `var(--bonus-powershot)` in `:root` |
| **Secondary / Muted Copy** | `#ffa7f0` | `var(--bonus-heavy-ball)` in `:root` |
| **Structural Hairline Border** | `#8eff9b` | `var(--bonus-smash)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cta-text` | `calc((22.5px) * var(--h-demult, 1))` | Typography Ink Token |
| `--home-title` | `calc((45px) * var(--h-demult, 1))` | Dimension / Scale Token |
| `--prize-title` | `calc((45px) * var(--h-demult, 1))` | Dimension / Scale Token |
| `--prize-text` | `calc((22px) * var(--h-demult, 1))` | Typography Ink Token |
| `--padding-header` | `calc((10px) * var(--h-demult, 1))` | Layout / Spatial Grid Token |
| `--size` | `calc((400px) * var(--h-demult, 1))` | Layout / Spatial Grid Token |
| `--prize-mult` | `calc((24px) * var(--h-demult, 1))` | Dimension / Scale Token |
| `--intro-title` | `calc((30px) * var(--h-demult, 1))` | Dimension / Scale Token |
| `--desc` | `calc((15px) * var(--h-demult, 1))` | Dimension / Scale Token |
| `--bonus-racket` | `#b762ff` | Color / Atmospheric Token |
| `--bonus-multiball` | `#f58c58` | Color / Atmospheric Token |
| `--bonus-defensive-wall` | `#50caff` | Color / Atmospheric Token |
| `--bonus-powershot` | `#ee5f62` | Color / Atmospheric Token |
| `--bonus-heavy-ball` | `#ffa7f0` | Color / Atmospheric Token |
| `--bonus-smash` | `#8eff9b` | Color / Atmospheric Token |
| `--game-size` | `calc((15px) * var(--h-demult, 1))` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.desktop> — `members-play-lacoste-com_ace-breaker-rg`)**:
   - Landmark `<header class="desktop">` hosting `Lacoste - Ace breaker` navigation (`our 3 partners`), DOM attributes (`data-nosnippet="true"`, `data-lang-dir="ltr"`, `data-testid="notice"`, `data-v-app`), and stylesheet rule `path { fill:fcd757 }`.
2. **Hero Stage & Focal Lead (<main.ui> — `Lacoste - Ace breaker`)**:
   - Landmark `<main class="ui">` presenting display lead `Lacoste - Ace breaker` and copy excerpt *"With your agreement, we and our 3 partners use cookies or similar"* over `#b762ff` canvas and `#8eff9b` ink.
3. **Primary Showcase & Content Grid (<main.ui> — `Featured Work & Interactive Showca`)**:
   - Landmark `<main class="ui">` rendering section `Featured Work & Interactive Showcase` with copy *"We and our partners process data for the following purposes: Pers"*, asset references (`loader.js`, `favicon.ico`, `favicon_dark.svg`, `favicon_light.svg`), and grid rule `disabled { pointer-events:none;opacity:.5 }`.
4. **Interactive Detail & Feature Matrix (<main.ui> — `Technical Architecture & Narrative`)**:
   - Landmark `<main class="ui">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"We and our partners process data for the following purposes:"*) with `#50caff` surface cards, `#ee5f62` accents, and `hover { background:fff;transform:scale(1.05) }`.
5. **Colophon & Global Directory Footer (<footer.didomi-popup-open> — `https://members-play.lacoste.com/ace-breaker-rg`)**:
   - Landmark `<footer class="didomi-popup-open">` anchoring `Lacoste - Ace breaker` footer links (`our 3 partners`), copy *"Personalised advertising and content, advertising and conten"*, and `#8eff9b` structural dividers.
