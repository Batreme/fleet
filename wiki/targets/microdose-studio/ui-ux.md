# UI & UX Architecture: microdose-studio

## Overview & Design Identity
- **Target**: `microdose-studio` (**Microdose Studio - Design & Development Agency for Startups**)
- **Production URL**: [https://microdose.studio/](https://microdose.studio/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#19171b` / `#ffffff`)
- **Summary**: Microdose Studio helps tech startups turn ideas into products through strategy, brand and product design, React/Next.js development, and...
- **Total Clean CSS Variables Extracted**: `61` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `Instrument Serif`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `20px`, `18px`, `16px`, `14px`, `10px`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 26px`, `line-height: 42px`, `letter-spacing: -1.56px`, `font-weight: 400`)
- **Body Copy**: rule `body` (`font-weight: 400`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `20px`, `18px`, `16px`, `14px`, `10px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#19171b` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#0c152a` | `var(--color-dark)` in `:root` |
| **Elevated Surface / Card Substrate** | `#6b6c71` | `var(--color-muted)` in `:root` |
| **Interactive Accent / Highlight** | `#ffffff` | `var(--color-white)` in `:root` |
| **Secondary / Muted Copy** | `#121113` | `var(--color-bg-dark)` in `:root` |
| **Structural Hairline Border** | `#e8e8ec` | `var(--color-card-bg)` in `:root` |
| **Variable Token (`--color-blue-start`)** | `#1935d9` | `var(--color-blue-start)` in `:root` |
| **Variable Token (`--color-blue-end`)** | `#2f2be2` | `var(--color-blue-end)` in `:root` |
| **Variable Token (`--color-blue-border`)** | `#1f34c9` | `var(--color-blue-border)` in `:root` |
| **Variable Token (`--color-grey-cool`)** | `#818a94` | `var(--color-grey-cool)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-black` | `#19171b` | Canvas / Surface Token |
| `--color-dark` | `#0c152a` | Canvas / Surface Token |
| `--color-muted` | `#6b6c71` | Brand / Palette Token |
| `--color-white` | `#ffffff` | Canvas / Surface Token |
| `--color-bg-dark` | `#121113` | Canvas / Surface Token |
| `--color-card-bg` | `#e8e8ec` | Canvas / Surface Token |
| `--color-blue-start` | `#1935d9` | Brand / Palette Token |
| `--color-blue-end` | `#2f2be2` | Brand / Palette Token |
| `--color-blue-border` | `#1f34c9` | Brand / Palette Token |
| `--color-footer-border` | `rgba(116, 84, 84, 0.15)` | Brand / Palette Token |
| `--color-white-50` | `rgba(255, 255, 255, 0.5)` | Canvas / Surface Token |
| `--color-grey-cool` | `#818a94` | Brand / Palette Token |
| `--font-primary` | `'Geist', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif` | Brand / Palette Token |
| `--font-accent` | `'Metal', serif` | Brand / Palette Token |
| `--radius-lg` | `16px` | Elevation / Border Token |
| `--radius-xl` | `24px` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.nav> — `microdose-studio`)**:
   - Landmark `<nav class="nav blur-fade-in">` hosting `Microdose Studio - Design & Developm` navigation (`microdose .studio · About us 01 · Case Studies 02 · Services 03 · Labs 04`), DOM attributes (`data-scroll-indicator="home"`, `data-chrome="nav"`, `data-gt-open="call"`, `data-btn-hover-ready="true"`), and stylesheet rule `after { margin: 0; padding: 0; box-sizing: border-box; }`.
2. **Hero Stage & Focal Lead (<section.hero> — `W e b u i l d A I - f i r s t p r `)**:
   - Landmark `<section class="hero blur-fade-in">` presenting display lead `W e b u i l d A I - f i r s t p r o d u c t s f o...` and copy excerpt *"Accepting new projects"* over `#19171b` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.portfolio-carousel> — `O u r s e l e c t e d p r o j e c `)**:
   - Landmark `<section class="portfolio-carousel">` rendering section `O u r s e l e c t e d p r o j e c t s .` with copy *"Your Design & Dev Partner."*, asset references (`favicon-96x96.png`, `favicon.ico`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `selection { background-color: var(--color-blue-start); color: var(--color-white); te... }`.
4. **Interactive Detail & Feature Matrix (<section.about> — `M o b i l e A p p f o r H y p e r `)**:
   - Landmark `<section class="about">` framing `M o b i l e A p p f o r H y p e r P e r s o n a l...` and `U n i f y i n g a G l o b a l G T M A n a l y t i...` (*"e n t e r p r i s e s ."*) with `#6b6c71` surface cards, `#ffffff` accents, and `html { -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale;... }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://microdose.studio/`)**:
   - Landmark `<footer class="footer">` anchoring `Microdose Studio - Design & Deve` footer links (`microdose .studio · About us 01 · Case Studies 02 · Services 03 · Labs 04`), copy *"Microdose Studio shapes your ideas, drives your launch, and "*, and `#e8e8ec` structural dividers.
