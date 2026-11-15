# UI & UX Architecture: www-spectup-com

## Overview & Design Identity
- **Target**: `www-spectup-com` (**Private Capital Advisory: Capital Raising and M&A · spectup**)
- **Production URL**: [https://www.spectup.com/](https://www.spectup.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#121212` / `#8A8A8A`)
- **Summary**: Private capital advisory with $760M+ advised, raised or placed since 2022: capital raising for companies and funds, fund placement and M&...
- **Total Clean CSS Variables Extracted**: `162` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `A5A5A3`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--t-h1: clamp(30px,4.2vw,64px)`, `--kh-h1: 196.0px`; rule `.h1` (`font-size: clamp(19px,min(2.05vw,3.3vh),...`, `letter-spacing: -.018em`, `font-weight: 400`)
- **Section Heading (`H2`)**: CSS variables `--t-h2: clamp(22px,2.5vw,36px)`; rule `h2` (`font-size: clamp(24px,2.9vw,52px)`, `line-height: 1.06`, `letter-spacing: -.032em`, `font-weight: 500`)
- **Body Copy**: CSS variables `--ck-body: #A5A5A3`, `--t-body: 15px`; rule `p` (`font-size: 13px`, `line-height: 1.6`)
- **Metadata & Labels**: CSS variables `--ck-mono: ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospace`, `--t-meta: 12.5px`, `--mono: ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospace`; rule `.meta` (`font-size: var(--t-meta)`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#121212` | `var(--ck-ink)` in `:root` |
| **Primary Typography Ink** | `#FAFAFA` | `var(--ck-light)` in `:root` |
| **Elevated Surface / Card Substrate** | `#F8F32B` | `var(--ck-yellow)` in `:root` |
| **Interactive Accent / Highlight** | `#8A8A8A` | `var(--ck-grey)` in `:root` |
| **Secondary / Muted Copy** | `#A5A5A3` | `var(--ck-body)` in `:root` |
| **Structural Hairline Border** | `#8E8E8C` | `var(--ck-fine)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ck-ink` | `#121212` | Typography Ink Token |
| `--ck-light` | `#FAFAFA` | Canvas / Surface Token |
| `--ck-yellow` | `#F8F32B` | Color / Atmospheric Token |
| `--ck-line` | `rgba(250,250,250,.14)` | Color / Atmospheric Token |
| `--ck-line-2` | `rgba(250,250,250,.24)` | Color / Atmospheric Token |
| `--ck-grey` | `#8A8A8A` | Color / Atmospheric Token |
| `--ck-body` | `#A5A5A3` | Color / Atmospheric Token |
| `--ck-fine` | `#8E8E8C` | Color / Atmospheric Token |
| `--ck-mono` | `ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospace` | Typography / Scale Token |
| `--ck-e` | `var(--e,cubic-bezier(.16,1,.3,1))` | Motion / Timing Token |
| `--ck-e-in` | `var(--e-in,cubic-bezier(.7,0,.84,0))` | Motion / Timing Token |
| `--ck-d1` | `320ms` | Motion / Timing Token |
| `--ck-d2` | `700ms` | Motion / Timing Token |
| `--ck-d3` | `1200ms` | Motion / Timing Token |
| `--ck-fade` | `var(--d-fade,460ms)` | Design System Custom Token |
| `--ck-rise-d` | `var(--d-rise,520ms)` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.mo> — `www-spectup-com`)**:
   - Landmark `<nav class="mo">` hosting `Private Capital Advisory: Capital Ra` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-nosnippet`, `data-mnbound="1"`, `data-l="The firm"`, `data-lf-cf`), and stylesheet rule `.cknote { width:min(372px,calc(100vw - 32px));padding:16px 18px 6px }`.
2. **Hero Stage & Focal Lead (<section.kh> — `Private capital advisory : A c c e`)**:
   - Landmark `<section class="kh in">` presenting display lead `Private capital advisory : A c c e s s t o p r i...` and copy excerpt *"Startup fundraising"* over `#121212` canvas and `#FAFAFA` ink.
3. **Primary Showcase & Content Grid (<section.s--light> — `spectup’s track record`)**:
   - Landmark `<section class="s--light offrest">` rendering section `spectup’s track record` with copy *"Capital introduction"*, asset references (`favicon.ico`, `favicon-32.png`, `favicon-192.png`, `apple-touch-icon.png`), and grid rule `.ckhd { display:flex;align-items:center;justify-content:space-between;gap:16px;m... }`.
4. **Interactive Detail & Feature Matrix (<section.s--light> — `How we get capital raises, M&A dea`)**:
   - Landmark `<section class="s--light s--flush">` framing `How we get capital raises, M&A deals and secondar...` and `Private capital advisory: capital raising and M&A` (*"Secondary advisory"*) with `#F8F32B` surface cards, `#8A8A8A` accents, and `.ckix { font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;font-weig... }`.
5. **Colophon & Global Directory Footer (<footer.ft> — `https://www.spectup.com/`)**:
   - Landmark `<footer class="ft has-canvas">` anchoring `Private Capital Advisory: Capita` footer links (`Overview · Index · Archive · About · Contact`), copy *"Everything we publish"*, and `#8E8E8C` structural dividers.
