# UI & UX Architecture: www-hollywoodexhibit2026-com

## Overview & Design Identity
- **Target**: `www-hollywoodexhibit2026-com` (**ELLE & Esquire, The New Hollywood Photography Exhibition**)
- **Production URL**: [https://www.hollywoodexhibit2026.com](https://www.hollywoodexhibit2026.com)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#000000`)
- **Summary**: Hearst Galleries presented a joint photography exhibition for ELLE and Esquire, ELLE: The New Hollywood and Esquire Goes to Hollywood, fe...
- **Total Clean CSS Variables Extracted**: `44` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Instrument Sans`
- **Body Font Stack**: `Instrument Sans Fallback`
- **Monospace / Technical Font Stack**: `safiraMarch`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-headline-10)`, `var(--text-headline-18)`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-headline-10)`, `var(--text-headline-18)`)
- **Body Copy**: CSS variables `--text-body-10--font-weight: 400`, `--text-body-10--line-height: 1.25`, `--text-body-10--letter-spacing: -2%`
- **Metadata & Labels**: CSS variables `--text-label--font-weight: 400`, `--text-label--line-height: 1`, `--text-label--letter-spacing: .03em`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0000` | `textarea { background-color: #0000 }` |
| **Interactive Accent / Highlight** | `#000000` | `.border-black { border-color: black }` (`#000000`) |
| **Secondary / Muted Copy** | `#ffffff` | `50 { border-color: white }` (`#ffffff`) |
| **Structural Hairline Border** | `#fff3` | `20 { background-color: #fff3 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--spacing` | `.0625rem` | Layout / Spatial Grid Token |
| `--font-weight-light` | `300` | Canvas / Surface Token |
| `--animate-spin` | `spin 1s linear infinite` | Motion / Easing Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4,0,.2,1)` | Motion / Easing Token |
| `--fluid-min-w` | `var(--layout-min-w,375)` | Design System Custom Token |
| `--fluid-max-w` | `var(--layout-max-w,1920)` | Layout / Spatial Grid Token |
| `--text-label--font-weight` | `400` | Typography Ink Token |
| `--text-label--line-height` | `1` | Typography Ink Token |
| `--text-label--letter-spacing` | `.03em` | Typography Ink Token |
| `--text-body-10--font-weight` | `400` | Typography Ink Token |
| `--text-body-10--line-height` | `1.25` | Typography Ink Token |
| `--text-body-10--letter-spacing` | `-2%` | Typography Ink Token |
| `--text-headline-10--font-weight` | `400` | Typography Ink Token |
| `--text-headline-10--line-height` | `1` | Typography Ink Token |
| `--text-headline-10--letter-spacing` | `normal` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.wf-ivyprestodisplay-n3-active> — `www-hollywoodexhibit2026-com`)**:
   - Landmark `<header class="wf-ivyprestodisplay-n3-active">` hosting `ELLE & Esquire, The New Hollywood Ph` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-engine="three.js r182"`, `data-nscript="afterInteractive"`, `data-nscript="afterInteractive"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<main.wf-ivyprestodisplay-i3-active> — `THE ELLE ESQUIRE HOLLYWOOD`)**:
   - Landmark `<main class="wf-ivyprestodisplay-i3-active">` presenting display lead `THE ELLE ESQUIRE HOLLYWOOD` and copy excerpt *"THE ELLE ESQUIRE HOLLYWOOD"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<main.wf-helveticaltpro-i7-active> — `THE ELLE ESQUIRE HOLLYWOOD`)**:
   - Landmark `<main class="wf-helveticaltpro-i7-active">` rendering section `THE ELLE ESQUIRE HOLLYWOOD` with copy *"As seen in the Hearst Tower, located in"*, asset references (`ABCArizonaVariable-s.p.6844b0f6.w...`, `Haigrast-s.p.42f2de84.woff2`, `IvyPrestoHeadline_Thin-s.p.830ff3...`, `IvyPrestoText_Thin-s.p.3ba47ad4.w...`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<main.wf-helveticaltpro-i4-active> — `As seen in the Hearst Tower, locat`)**:
   - Landmark `<main class="wf-helveticaltpro-i4-active">` framing `As seen in the Hearst Tower, located in` and `www-hollywoodexhibit2026-com Archive & Directory` (*"THE ELLE ESQUIRE HOLLYWOOD"*) with `#0000` surface cards, `#000000` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.wf-helveticaltpro-n7-active> — `https://www.hollywoodexhibit2026.com`)**:
   - Landmark `<footer class="wf-helveticaltpro-n7-active">` anchoring `ELLE & Esquire, The New Hollywoo` footer links (`Overview · Index · Archive · About · Contact`), copy *"As seen in the Hearst Tower, located in"*, and `#fff3` structural dividers.
