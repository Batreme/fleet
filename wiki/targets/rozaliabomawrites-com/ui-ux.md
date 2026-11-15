# UI & UX Architecture: rozaliabomawrites-com

## Overview & Design Identity
- **Target**: `rozaliabomawrites-com` (**Rozalia Boma — Multicultural Romance Author**)
- **Production URL**: [https://rozaliabomawrites.com/](https://rozaliabomawrites.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#9ca3af`)
- **Summary**: Official site of Rozalia Boma, author of multicultural YA romance. Books, diary entries, guestbook and newsletter.
- **Total Clean CSS Variables Extracted**: `268` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Gochi Hand Fallback`
- **Body Font Stack**: `Barlow Condensed`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `6em`)
- **Section Heading (`H2`)**: rule `h2` (`letter-spacing: -.02em`, `font-weight: 400`)
- **Body Copy**: rule `p` (`line-height: 1.65`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `6em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--w2w-start-background-color)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--normal-bg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#e5e7eb` | `:after { border-color: #e5e7eb }` |
| **Interactive Accent / Highlight** | `#9ca3af` | `textarea::-moz-placeholder { color: #9ca3af }` |
| **Secondary / Muted Copy** | `#ffa500` | `.os-window--orange { border-color: orange }` (`#ffa500`) |
| **Structural Hairline Border** | `#93ceec` | `.os-window--babyblue { border-color: #93ceec }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background` | `290 80% 92%` | Canvas / Surface Token |
| `--foreground` | `320 60% 18%` | Typography Ink Token |
| `--card` | `0 0% 100%` | Dimension / Scale Token |
| `--card-foreground` | `320 60% 18%` | Typography Ink Token |
| `--popover` | `0 0% 100%` | Dimension / Scale Token |
| `--popover-foreground` | `320 60% 18%` | Typography Ink Token |
| `--primary` | `330 95% 60%` | Brand / Palette Token |
| `--primary-foreground` | `0 0% 100%` | Typography Ink Token |
| `--secondary` | `280 85% 78%` | Brand / Palette Token |
| `--secondary-foreground` | `320 60% 18%` | Typography Ink Token |
| `--muted` | `320 60% 95%` | Dimension / Scale Token |
| `--muted-foreground` | `320 25% 45%` | Typography Ink Token |
| `--accent` | `195 90% 75%` | Brand / Palette Token |
| `--accent-foreground` | `320 60% 18%` | Typography Ink Token |
| `--destructive` | `0 84% 60%` | Dimension / Scale Token |
| `--destructive-foreground` | `0 0% 100%` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.fixed> — `rozaliabomawrites-com`)**:
   - Landmark `<nav class="fixed top-0">` hosting `Rozalia Boma — Multicultural Romance` navigation (`Home · Author · Books · Blog · Guestbook`), DOM attributes (`data-artifact-kind="dwl_content_hash"`, `data-artifact-id="db5c4db312500dfaed9e3..."`, `data-commit-sha="37366776bd44c18a989e4..."`, `data-context-token="v1.eyJwcm9qZWN0X2lkIj..."`), and stylesheet rule `after { box-sizing:border-box;border-width:0;border-style:solid;border-color:e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.fixed> — `Rozalia Boma — writing multicultur`)**:
   - Landmark `<section class="fixed">` presenting display lead `Rozalia Boma — writing multicultural romances` and copy excerpt *"Rozalia Boma Writes is loading"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `w r i t i n g m u l t i c u l t u `)**:
   - Landmark `<section class="relative min-h-screen">` rendering section `w r i t i n g m u l t i c u l t u r a l r o m a n...` with copy *"Beware! Black Eastern European baddies on the rise!"*, asset references (`holo-sky-bg-C4iYYOxV.webp`, `fonts.googleapis.com`, `fonts.gstatic.com`, `sykz-yx0lLcxQaSIhS23-w.woff2`), and grid rule `body { margin:0;line-height:inherit }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `H i ! I ' m R o z a l i a B o m a `)**:
   - Landmark `<section class="relative w-full">` framing `H i ! I ' m R o z a l i a B o m a .` and `T h e B o o k` (*"w r i t i n g m u l t i c u l t u r a l"*) with `#e5e7eb` surface cards, `#9ca3af` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://rozaliabomawrites.com/`)**:
   - Landmark `<footer class="relative z-10">` anchoring `Rozalia Boma — Multicultural Rom` footer links (`Home · Author · Books · Blog · Guestbook`), copy *"m u l t i c u l t u r a l"*, and `#93ceec` structural dividers.
