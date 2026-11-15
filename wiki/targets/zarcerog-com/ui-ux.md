# UI & UX Architecture: zarcerog-com

## Overview & Design Identity
- **Target**: `zarcerog-com` (**Nicolás Zarcero — Box Office**)
- **Production URL**: [https://zarcerog.com](https://zarcerog.com)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#e8b3a9` canvas, `#241417` ink, `#f4e6cb` accent)
- **Summary**: Two shows tonight: a portfolio in five acts, with an intermission; and a picture about a church that is running late. Nicolás Zarcero, en...
- **Total Clean CSS Variables Extracted**: `32` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Jost`
- **Body Font Stack**: `Jost Fallback`
- **Monospace / Technical Font Stack**: `Courier Prime`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `30px`, `clamp(16px,1.7vw,26px)`, `12px`, `clamp(34px,7vw,110px)`, `15px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `30px`, `clamp(16px,1.7vw,26px)`, `12px`, `clamp(34px,7vw,110px)`, `15px`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `30px`, `clamp(16px,1.7vw,26px)`, `12px`, `clamp(34px,7vw,110px)`, `15px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `30px`, `clamp(16px,1.7vw,26px)`, `12px`, `clamp(34px,7vw,110px)`, `15px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#e8b3a9` | `var(--pink)` in `:root` |
| **Primary Typography Ink** | `#86192a` | `var(--burgundy)` in `:root` |
| **Elevated Surface / Card Substrate** | `#c9a24a` | `var(--gold)` in `:root` |
| **Interactive Accent / Highlight** | `#f4e6cb` | `var(--cream)` in `:root` |
| **Secondary / Muted Copy** | `#f2c230` | `var(--yellow)` in `:root` |
| **Structural Hairline Border** | `#241417` | `var(--ink)` in `:root` |
| **Variable Token (`--red`)** | `#d8262e` | `var(--red)` in `:root` |
| **Variable Token (`--sub`)** | `#f7d23e` | `var(--sub)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bx-sans` | `var(--f-sans,Jost), Jost, Futura, "Helvetica Neue", sans-serif` | Typography / Scale Token |
| `--bx-type` | `var(--f-type,"Courier Prime"), "Courier Prime", "Courier New", monospace` | Typography / Scale Token |
| `--bx-marquee` | `var(--f-marquee,Limelight), Limelight, var(--f-serif,"Bodoni Moda"), serif` | Design System Custom Token |
| `--bx-anton` | `var(--f-anton,Anton), Anton, Impact, "Arial Narrow", sans-serif` | Design System Custom Token |
| `--pink` | `#e8b3a9` | Typography Ink Token |
| `--burgundy` | `#86192a` | Color / Atmospheric Token |
| `--gold` | `#c9a24a` | Color / Atmospheric Token |
| `--cream` | `#f4e6cb` | Color / Atmospheric Token |
| `--yellow` | `#f2c230` | Color / Atmospheric Token |
| `--ink` | `#241417` | Typography Ink Token |
| `--red` | `#d8262e` | Color / Atmospheric Token |
| `--sub` | `#f7d23e` | Color / Atmospheric Token |
| `--px` | `0` | Design System Custom Token |
| `--py` | `0` | Design System Custom Token |
| `--tx` | `0` | Design System Custom Token |
| `--ty` | `0` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.bx-layer> — `zarcerog-com`)**:
   - Landmark `<nav class="bx-layer bx-layer--tickets">` hosting `Nicolás Zarcero — Box Office` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`, `data-sdkv="1.6.1"`), and stylesheet rule `body { background:e8b3a9;margin:0 }`.
2. **Hero Stage & Focal Lead (<main.bx-root> — `Nicolás Zarcero : box office. Two `)**:
   - Landmark `<main class="bx-root">` presenting display lead `Nicolás Zarcero : box office. Two shows tonight —...` and copy excerpt *"The Zarcero Theatre presents A Portfolio in Five Acts with an int"* over `#e8b3a9` canvas and `#241417` ink.
3. **Primary Showcase & Content Grid (<main.bx-root> — `The Zarcero Theatre presents A Por`)**:
   - Landmark `<main class="bx-root">` rendering section `The Zarcero Theatre presents A Portfolio in Five` with copy *"The Zarcero Theatre"*, asset references (`52b5d5098cb87ddd-s.p.3r2y_bth_sjs...`, `5f440d3eea613716-s.p.1xmps1tcyqv3...`, `612bd71aa396cae6-s.p.0y-3ea_6ee5g...`, `81cef6a21128489e-s.p.2csanl8cs02r...`), and grid rule `.bx-sr { clip-path:inset(50%);white-space:nowrap;width:1px;height:1px;position:ab... }`.
4. **Interactive Detail & Feature Matrix (<main.bx-root> — `The Zarcero Theatre`)**:
   - Landmark `<main class="bx-root">` framing `The Zarcero Theatre` and `A Portfolio in Five Acts` (*"A Portfolio in Five Acts"*) with `#c9a24a` surface cards, `#f4e6cb` accents, and `.bx-layer { transition:transform .9s cubic-bezier(.2,.7,.2,1);position:absolute;inset:0 }`.
5. **Colophon & Global Directory Footer (<footer.bx-foot> — `https://zarcerog.com`)**:
   - Landmark `<footer class="bx-foot">` anchoring `Nicolás Zarcero — Box Office` footer links (`Overview · Index · Archive · About · Contact`), copy *"with an intermission · starring Nicolás Zarcero"*, and `#241417` structural dividers.
