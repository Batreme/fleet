# UI & UX Architecture: tribeofgiants-com

## Overview & Design Identity
- **Target**: `tribeofgiants-com` (**Mindset Coaching & Personal Growth — The Tribe of Giants**)
- **Production URL**: [https://tribeofgiants.com/](https://tribeofgiants.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fe7624` canvas, `#111` ink, `#f89a29` accent)
- **Summary**: Name the pattern that's been running your life — then outgrow it. 12 guided journeys, Rimi your AI guide, the Mirror, and a tribe that wa...
- **Total Clean CSS Variables Extracted**: `86` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Merriweather`
- **Body Font Stack**: `Merriweather Fallback`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(24px,4vw,32px)`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 1.45em`)
- **Body Copy**: CSS variables `--font-body: Lato, system-ui, sans-serif`; rule `p` (`line-height: 1.7`)
- **Metadata & Labels**: rule `small` (`font-size: 13px`, `font-weight: 700`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fe7624` | `var(--giant-orange)` in `:root` |
| **Primary Typography Ink** | `#42abdb` | `var(--giant-blue)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0b9444` | `var(--growth-green)` in `:root` |
| **Interactive Accent / Highlight** | `#f89a29` | `var(--legacy-peach)` in `:root` |
| **Secondary / Muted Copy** | `#3b2313` | `var(--root-brown)` in `:root` |
| **Structural Hairline Border** | `#111` | `var(--foundation-black)` in `:root` |
| **Variable Token (`--potential-white`)** | `#fff` | `var(--potential-white)` in `:root` |
| **Variable Token (`--gold`)** | `#f2b25c` | `var(--gold)` in `:root` |
| **Variable Token (`--gold-deep`)** | `#c9a96a` | `var(--gold-deep)` in `:root` |
| **Variable Token (`--eyebrow`)** | `#a8430a` | `var(--eyebrow)` in `:root` |
| **Variable Token (`--lit`)** | `#ffffff61` | `var(--lit)` in `:root` |
| **Variable Token (`--bg`)** | `#f5efe3` | `var(--bg)` in `:root` |
| **Variable Token (`--surface`)** | `#fffcf6` | `var(--surface)` in `:root` |
| **Variable Token (`--surface-2`)** | `#f4ede0` | `var(--surface-2)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--giant-orange` | `#fe7624` | Color / Atmospheric Token |
| `--giant-blue` | `#42abdb` | Color / Atmospheric Token |
| `--growth-green` | `#0b9444` | Color / Atmospheric Token |
| `--legacy-peach` | `#f89a29` | Color / Atmospheric Token |
| `--root-brown` | `#3b2313` | Color / Atmospheric Token |
| `--foundation-black` | `#111` | Canvas / Surface Token |
| `--potential-white` | `#fff` | Canvas / Surface Token |
| `--font-heading` | `Merriweather, Georgia, serif` | Typography Ink Token |
| `--font-body` | `Lato, system-ui, sans-serif` | Typography / Scale Token |
| `--gold` | `#f2b25c` | Color / Atmospheric Token |
| `--gold-deep` | `#c9a96a` | Color / Atmospheric Token |
| `--eyebrow` | `#a8430a` | Color / Atmospheric Token |
| `--lit` | `#ffffff61` | Color / Atmospheric Token |
| `--bg` | `#f5efe3` | Canvas / Surface Token |
| `--surface` | `#fffcf6` | Canvas / Surface Token |
| `--surface-2` | `#f4ede0` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lp-hero-cinema> — `tribeofgiants-com`)**:
   - Landmark `<header class="lp-hero-cinema">` hosting `Mindset Coaching & Personal Growth —` navigation (`Why the Tribe · Journeys · Blog · Podcast · Books`), DOM attributes (`data-si="1"`, `data-theme="dark"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `iframe { max-width:100% }`.
2. **Hero Stage & Focal Lead (<section.lp-section> — `Name the pattern that's been runni`)**:
   - Landmark `<section class="lp-section ins">` presenting display lead `Name the pattern that's been running your life. T...` and copy excerpt *"The Tribe of Giants"* over `#fe7624` canvas and `#111` ink.
3. **Primary Showcase & Content Grid (<section.lp-section> — `A day inside the Tribe`)**:
   - Landmark `<section class="lp-section fbk-section">` rendering section `A day inside the Tribe` with copy *"Home of the 12 Journeys — where every Giant was once a Small"*, asset references (`248e1dc0efc99276-s.p.0dq1pb0w2tem...`, `345c85a432359eed-s.p.24jxsbewvqxg...`, `8e451580e5e95631-s.p.0ic9f6t6i9np...`, `9be384ea93fe3f49-s.p.0oq27de-d8s-...`), and grid rule `html { background:var(--bg) }`.
4. **Interactive Detail & Feature Matrix (<article.fbk-card> — `One honest question`)**:
   - Landmark `<article class="fbk-card">` framing `One honest question` and `Your page, read back` (*"You've read the books. You've heard the podcasts. You've collecte"*) with `#0b9444` surface cards, `#f89a29` accents, and `body { background:0 0 }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://tribeofgiants.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Mindset Coaching & Personal Grow` footer links (`Why the Tribe · Journeys · Blog · Podcast · Books`), copy *"Join free, for life. Your seat in the Tribe, Journey 1 and t"*, and `#111` structural dividers.
