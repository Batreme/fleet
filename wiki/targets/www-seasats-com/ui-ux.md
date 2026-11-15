# UI & UX Architecture: www-seasats-com

## Overview & Design Identity
- **Target**: `www-seasats-com` (**Seasats · Ocean Autonomy That Works**)
- **Production URL**: [https://www.seasats.com/](https://www.seasats.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#2b3922` / `#4e9a85`)
- **Summary**: Missions completed for defense, science, and commercial customers around the world.
- **Total Clean CSS Variables Extracted**: `133` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `seasonMix`
- **Body Font Stack**: `seasonMix Fallback`
- **Monospace / Technical Font Stack**: `supplyMono`
- **Hero Display (`H1`)**: rule `h1` (`font-size: 4.8rem`, `line-height: 1`, `letter-spacing: -.01em`, `font-weight: 400`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 2.4rem`, `line-height: 1.2`, `letter-spacing: 0`, `font-weight: 400`)
- **Body Copy**: CSS variables `--body-adjustOffset: calc(59.8rem / -2)`, `--body-adjustScale: 0.66`, `--body-adjustScalePrecise: 0.585`
- **Metadata & Labels**: CSS variables `--fontSupplyMono: "supplyMono","supplyMono Fallback",monospace`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#2b3922` | `var(--icon-background)` in `:root` |
| **Primary Typography Ink** | `#fffdfd` | `var(--icon-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--colorText)` in `:root` |
| **Interactive Accent / Highlight** | `#4e9a85` | `var(--modal-barBackgroundColor)` in `:root` |
| **Secondary / Muted Copy** | `#e3ede4` | `var(--button-background)` in `:root` |
| **Structural Hairline Border** | `#232323` | `var(--formField-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--icon-background` | `#2b3922` | Canvas / Surface Token |
| `--icon-color` | `#fffdfd` | Brand / Palette Token |
| `--icon-size` | `3rem` | Layout / Spatial Grid Token |
| `--icon-progress` | `1` | Design System Custom Token |
| `--colorText` | `#fff` | Typography Ink Token |
| `--button-outline` | `#fffdfd` | Elevation / Border Token |
| `--gridLayout-columns` | `var(--columns)` | Layout / Spatial Grid Token |
| `--button-maskPadding` | `0.1rem` | Layout / Spatial Grid Token |
| `--button-maskFade` | `0.1rem` | Dimension / Scale Token |
| `--paddingTop` | `6.4rem` | Layout / Spatial Grid Token |
| `--paddingBottom` | `6.4rem` | Layout / Spatial Grid Token |
| `--modal-contentMaxWidth` | `60.8rem` | Layout / Spatial Grid Token |
| `--modal-contentBackgroundColor` | `#fffdfd` | Canvas / Surface Token |
| `--modal-barBackgroundColor` | `#4e9a85` | Canvas / Surface Token |
| `--modal-barColor` | `#fffdfd` | Brand / Palette Token |
| `--button-background` | `#e3ede4` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.Header_container__U6gzw> — `www-seasats-com`)**:
   - Landmark `<header class="Header_container__U6gzw">` hosting `Seasats · Ocean Autonomy That Works` navigation (`Home · 01 Capabilities · 02 Past Missions · Products · 01 Comparison`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.not-found_title__bgpas { font-size:min(36rem,36vh) }`.
2. **Hero Stage & Focal Lead (<main.browser-ui-overlay> — `Ocean Autonomy That Works`)**:
   - Landmark `<main class="browser-ui-overlay">` presenting display lead `Ocean Autonomy That Works` and copy excerpt *"Ocean Autonomy That Works"* over `#2b3922` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<main.browser-ui-overlay--top> — `Deploy in minutes.`)**:
   - Landmark `<main class="browser-ui-overlay--top">` rendering section `Deploy in minutes.` with copy *"E x p l o r e p r o d u c t s E x p l o r e p r o d u c t s"*, asset references (`d11d81b0342c0709.css`, `a14bc365605f91b3.css`, `110e11ba57841c1c.css`, `5ef63a433e26978c.css`), and grid rule `.not-found_media__ko4tq { position:absolute;inset:0;background-image:linear-gradient(180deg,1d344a... }`.
4. **Interactive Detail & Feature Matrix (<main.ThemeBackground_background__xCT8k> — `Detect from miles.`)**:
   - Landmark `<main class="ThemeBackground_background__xCT8k">` framing `Detect from miles.` and `React at once.` (*"E x p l o r e p r o d u c t s"*) with `#fff` surface cards, `#4e9a85` accents, and `.AnimatedText_animatedText__MS50q { display:block;position:relative }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.seasats.com/`)**:
   - Landmark `<footer class="footer Footer_container__kRlyj">` anchoring `Seasats · Ocean Autonomy That Wo` footer links (`Home · 01 Capabilities · 02 Past Missions · Products · 01 Comparison`), copy *"The coordinates of the ghost fleet."*, and `#232323` structural dividers.
