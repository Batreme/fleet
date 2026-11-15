# UI & UX Architecture: phin-helenadang-work

## Overview & Design Identity
- **Target**: `phin-helenadang-work` (**PHIN PHIN · Saigon coffee, stirred by you**)
- **Production URL**: [https://phin.helenadang.work/](https://phin.helenadang.work/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffd23f` / `#a3170f`)
- **Summary**: PHIN PHIN is a made-up Saigon coffee shop. Watch your coffee drip, then stir it yourself. A concept by Helena Dang.
- **Total Clean CSS Variables Extracted**: `64` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Phudu`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(4.25rem,11.5vw,12rem)`, `clamp(.875rem,2.42vw,2.4rem)`, `clamp(.8125rem,2.12vw,2.4rem)`, `clamp(4.25rem,min(14.385vw,17.05v...`, `.1525em`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(4.25rem,11.5vw,12rem)`, `clamp(.875rem,2.42vw,2.4rem)`, `clamp(.8125rem,2.12vw,2.4rem)`, `clamp(4.25rem,min(14.385vw,17.05v...`, `.1525em`)
- **Body Copy**: CSS variables `--font-body: "Inter", system-ui, -apple-system, "Segoe UI", sans-serif`
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(4.25rem,11.5vw,12rem)`, `clamp(.875rem,2.42vw,2.4rem)`, `clamp(.8125rem,2.12vw,2.4rem)`, `clamp(4.25rem,min(14.385vw,17.05v...`, `.1525em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ffd23f` | `var(--sign-yellow)` in `:root` |
| **Primary Typography Ink** | `#f0a51f` | `var(--sign-yellow-shade)` in `:root` |
| **Elevated Surface / Card Substrate** | `#d7261e` | `var(--sign-red)` in `:root` |
| **Interactive Accent / Highlight** | `#a3170f` | `var(--sign-red-shade)` in `:root` |
| **Secondary / Muted Copy** | `#1e4fd8` | `var(--enamel-blue)` in `:root` |
| **Structural Hairline Border** | `#1336a0` | `var(--enamel-blue-shade)` in `:root` |
| **Variable Token (`--tin-sky`)** | `#9fd3e6` | `var(--tin-sky)` in `:root` |
| **Variable Token (`--tin-sky-shade`)** | `#62a9c6` | `var(--tin-sky-shade)` in `:root` |
| **Variable Token (`--ink`)** | `#111` | `var(--ink)` in `:root` |
| **Variable Token (`--coffee`)** | `#5b2a12` | `var(--coffee)` in `:root` |
| **Variable Token (`--coffee-shade`)** | `#3a1708` | `var(--coffee-shade)` in `:root` |
| **Variable Token (`--caramel`)** | `#a8653a` | `var(--caramel)` in `:root` |
| **Variable Token (`--caramel-shade`)** | `#7e4524` | `var(--caramel-shade)` in `:root` |
| **Variable Token (`--milk`)** | `#fff1b8` | `var(--milk)` in `:root` |
| **Variable Token (`--milk-shade`)** | `#f2d77c` | `var(--milk-shade)` in `:root` |
| **Variable Token (`--white`)** | `#fff` | `var(--white)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--sign-yellow` | `#ffd23f` | Color / Atmospheric Token |
| `--sign-yellow-shade` | `#f0a51f` | Color / Atmospheric Token |
| `--sign-red` | `#d7261e` | Color / Atmospheric Token |
| `--sign-red-shade` | `#a3170f` | Color / Atmospheric Token |
| `--enamel-blue` | `#1e4fd8` | Color / Atmospheric Token |
| `--enamel-blue-shade` | `#1336a0` | Color / Atmospheric Token |
| `--tin-sky` | `#9fd3e6` | Color / Atmospheric Token |
| `--tin-sky-shade` | `#62a9c6` | Color / Atmospheric Token |
| `--ink` | `#111` | Typography Ink Token |
| `--coffee` | `#5b2a12` | Color / Atmospheric Token |
| `--coffee-shade` | `#3a1708` | Color / Atmospheric Token |
| `--caramel` | `#a8653a` | Color / Atmospheric Token |
| `--caramel-shade` | `#7e4524` | Color / Atmospheric Token |
| `--milk` | `#fff1b8` | Color / Atmospheric Token |
| `--milk-shade` | `#f2d77c` | Color / Atmospheric Token |
| `--white` | `#fff` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `phin-helenadang-work`)**:
   - Landmark `<header class="site-header">` hosting `PHIN PHIN · Saigon coffee, stirred b` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-engine="three.js r186"`, `data-js-only`, `data-from="sign-yellow"`, `data-to="tin-sky"`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<section.beat> — `PHIN PHIN`)**:
   - Landmark `<section class="beat beat-sign">` presenting display lead `PHIN PHIN` and copy excerpt *"Skip to the coffee"* over `#ffd23f` canvas and `#a3170f` ink.
3. **Primary Showcase & Content Grid (<section.beat> — `Good coffee takes four minutes.`)**:
   - Landmark `<section class="beat beat-brew">` rendering section `Good coffee takes four minutes.` with copy *"Chuyên bán: đen đá · sữa đá · bạc xỉu"*, asset references (`favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`, `index-BrMebdgu.js`), and grid rule `.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<section.beat> — `Now stir. Like you mean it.`)**:
   - Landmark `<section class="beat beat-stir">` framing `Now stir. Like you mean it.` and `Pick your poison. (It's coffee.)` (*"330/2 Hẻm Mèo kính mời"*) with `#d7261e` surface cards, `#a3170f` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.wrap> — `https://phin.helenadang.work/`)**:
   - Landmark `<footer class="wrap site-footer">` anchoring `PHIN PHIN · Saigon coffee, stirr` footer links (`Overview · Index · Archive · About · Contact`), copy *"Saigon coffee. Brewed slow, stirred by you."*, and `#1336a0` structural dividers.
