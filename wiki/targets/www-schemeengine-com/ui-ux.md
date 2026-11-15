# UI & UX Architecture: www-schemeengine-com

## Overview & Design Identity
- **Target**: `www-schemeengine-com` (**Home - Scheme Engine**)
- **Production URL**: [https://www.schemeengine.com/](https://www.schemeengine.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#1d0524` / `#b47054`)
- **Summary**: Scheme Engine is a BIPOC-owned production company and TV/Film studio founded to provoke and reimagine the status quo.
- **Total Clean CSS Variables Extracted**: `55` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Champagne Cartel`
- **Body Font Stack**: `Neuepower Ultra`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: CSS variables `--font-family-mono: Menlo, Monaco, Consolas, "Droid Sans Mono", monospace`; rule `small` (`font-size: 80%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#1d0524` | `var(--purple)` in `:root` |
| **Primary Typography Ink** | `#fef9ef` | `var(--white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#000` | `var(--black)` in `:root` |
| **Interactive Accent / Highlight** | `#b47054` | `var(--brown)` in `:root` |
| **Secondary / Muted Copy** | `#1f1f1f` | `var(--background-color)` in `:root` |
| **Structural Hairline Border** | `#ebebeb` | `var(--text-color)` in `:root` |
| **Variable Token (`--title-background-color`)** | `#111111` | `var(--title-background-color)` in `:root` |
| **Variable Token (`--widget-color`)** | `#424242` | `var(--widget-color)` in `:root` |
| **Variable Token (`--hover-color`)** | `#4f4f4f` | `var(--hover-color)` in `:root` |
| **Variable Token (`--focus-color`)** | `#595959` | `var(--focus-color)` in `:root` |
| **Variable Token (`--number-color`)** | `#2cc9ff` | `var(--number-color)` in `:root` |
| **Variable Token (`--string-color`)** | `#a2db3c` | `var(--string-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--purple` | `#1d0524` | Color / Atmospheric Token |
| `--white` | `#fef9ef` | Canvas / Surface Token |
| `--black` | `#000` | Canvas / Surface Token |
| `--brown` | `#b47054` | Color / Atmospheric Token |
| `--background-color` | `#1f1f1f` | Canvas / Surface Token |
| `--text-color` | `#ebebeb` | Typography Ink Token |
| `--title-background-color` | `#111111` | Canvas / Surface Token |
| `--title-text-color` | `#ebebeb` | Typography Ink Token |
| `--widget-color` | `#424242` | Brand / Palette Token |
| `--hover-color` | `#4f4f4f` | Brand / Palette Token |
| `--focus-color` | `#595959` | Brand / Palette Token |
| `--number-color` | `#2cc9ff` | Brand / Palette Token |
| `--string-color` | `#a2db3c` | Brand / Palette Token |
| `--font-size` | `11px` | Typography / Scale Token |
| `--input-font-size` | `11px` | Typography / Scale Token |
| `--font-family` | `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `www-schemeengine-com`)**:
   - Landmark `<header class="header">` hosting `Home - Scheme Engine` navigation (`D i r e c t o r s · W o r k · F i l m & t v · C o n t a c t`), DOM attributes (`data-wf-domain="www.schemeengine.com"`, `data-wf-page="6856ec97d986105f5589bbe0"`, `data-wf-site="6856ec97d986105f5589bbd7"`, `data-word="Directors"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.section> — `Shader Controls`)**:
   - Landmark `<section class="section">` presenting display lead `Shader Controls` and copy excerpt *"Skip to main content"* over `#1d0524` canvas and `#fef9ef` ink.
3. **Primary Showcase & Content Grid (<section.section> — `We create from the culture we live`)**:
   - Landmark `<section class="section">` rendering section `We create from the culture we live.` with copy *"Scheme Engine is a culture-first production company championing t"*, asset references (`cdn.prod.website-files.com`, `schemeengine.webflow.shared.3fbb9...`, `soy0bmb.js`, `68b845cb16daf25e488bd7a5_scheme-e...`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.section> — `Scheme Engine is a culture-first p`)**:
   - Landmark `<section class="section">` framing `Scheme Engine is a culture-first production comp` and `Our award-winning directors and creatives work a` (*"Our award-winning directors and creatives work across formats, al"*) with `#000` surface cards, `#b47054` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.wf-active> — `https://www.schemeengine.com/`)**:
   - Landmark `<footer class="wf-active">` anchoring `Home - Scheme Engine` footer links (`D i r e c t o r s · W o r k · F i l m & t v · C o n t a c t`), copy *"Impactful, resonant storytelling is rooted in lived experien"*, and `#ebebeb` structural dividers.
