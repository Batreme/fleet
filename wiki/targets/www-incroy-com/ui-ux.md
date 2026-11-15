# UI & UX Architecture: www-incroy-com

## Overview & Design Identity
- **Target**: `www-incroy-com` (**Incroy · Webflow Certified Development Agency**)
- **Production URL**: [https://www.incroy.com/](https://www.incroy.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#171717` ink, `#aaa` accent)
- **Summary**: Incroy is a Webflow agency serving medium to large businesses. We handle design, development, copywriting, and ongoing site management un...
- **Total Clean CSS Variables Extracted**: `84` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Suisseintl Book`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: rule `small` (`font-size: 80%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--base-color-neutral--white)` in `:root` |
| **Primary Typography Ink** | `#6053e5` | `var(--base-color-brand--brand-primary)` in `:root` |
| **Elevated Surface / Card Substrate** | `#d2cef9` | `var(--base-color-brand--brand-light)` in `:root` |
| **Interactive Accent / Highlight** | `#aaa` | `var(--base-color-neutral--neutral-light)` in `:root` |
| **Secondary / Muted Copy** | `#171717` | `var(--base-color-neutral--black)` in `:root` |
| **Structural Hairline Border** | `#ebebeb` | `var(--base-color-neutral--neutral-lightest)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--link-color--link-primary` | `var(--base-color-brand--brand-primary)` | Typography Ink Token |
| `--background-color--background-primary` | `var(--base-color-neutral--black)` | Canvas / Surface Token |
| `--text-color--text-alternate` | `var(--base-color-neutral--white)` | Typography Ink Token |
| `--text-color--text-primary` | `var(--base-color-neutral--black)` | Typography Ink Token |
| `--text-color--text-secondary` | `var(--base-color-neutral--neutral-darker)` | Typography Ink Token |
| `--background-color--background-success` | `var(--base-color-system--success-green)` | Canvas / Surface Token |
| `--text-color--text-success` | `var(--base-color-system--success-green-dark)` | Typography Ink Token |
| `--base-color-neutral--white` | `#fff` | Canvas / Surface Token |
| `--border-color--border-primary` | `var(--base-color-neutral--neutral-lightest)` | Brand / Palette Token |
| `--background-color--background-alternate` | `var(--base-color-neutral--white)` | Canvas / Surface Token |
| `--background-color--background-secondary` | `var(--base-color-brand--brand-primary)` | Canvas / Surface Token |
| `--background-color--background-tertiary` | `var(--base-color-brand--pink)` | Canvas / Surface Token |
| `--background-color--background-error` | `var(--base-color-system--error-red)` | Canvas / Surface Token |
| `--text-color--text-error` | `var(--base-color-system--error-red-dark)` | Typography Ink Token |
| `--border-color--border-subtle` | `var(--base-color-neutral--neutral-dark)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.navigation> — `www-incroy-com`)**:
   - Landmark `<nav class="navigation">` hosting `Incroy · Webflow Certified Developme` navigation (`H o m e · W o r k · P r o c e s s · W h o a r e w e ? · C o n t a c t`), DOM attributes (`data-wf-domain="www.incroy.com"`, `data-wf-page="6a21b959b61cf447eaaeea89"`, `data-wf-site="6a21b956b61cf447eaaeea3c"`, `data-settings="("apiEndpoint":"https..."`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.section-dots> — `Heading`)**:
   - Landmark `<section class="section-dots">` presenting display lead `Heading` and copy excerpt *"I f y o u n e e d a b e a u t i f u l w e b s i t e t h a t r e f"* over `#fff` canvas and `#171717` ink.
3. **Primary Showcase & Content Grid (<section.section-dots> — `W e m i g h t n o t b e y o u r f `)**:
   - Landmark `<section class="section-dots">` rendering section `W e m i g h t n o t b e y o u r f i r s t , b u t...` with copy *"L e t ’ s g o s i t e s e e i n g"*, asset references (`cdn.prod.website-files.com`, `incroy-v2.shared.e656a73ee.css`, `clarity.js`, `radar.min.js`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.section-dots> — `W h a t i n t h e w o r l d w i d `)**:
   - Landmark `<section class="section-dots">` framing `W h a t i n t h e w o r l d w i d e w e b h a s h...` and `T h a t ’ s w h e r e w e c o m e i n` (*"W e d e s i g n a n d d e v e l o p w e b s i t e s t h a t l o o"*) with `#d2cef9` surface cards, `#aaa` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.hide> — `https://www.incroy.com/`)**:
   - Landmark `<footer class="hide">` anchoring `Incroy · Webflow Certified Devel` footer links (`H o m e · W o r k · P r o c e s s · W h o a r e w e ? · C o n t a c t`), copy *"d e v e l o p m e n t ,"*, and `#ebebeb` structural dividers.
