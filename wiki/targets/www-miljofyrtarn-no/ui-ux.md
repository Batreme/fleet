# UI & UX Architecture: www-miljofyrtarn-no

## Overview & Design Identity
- **Target**: `www-miljofyrtarn-no` (**Hjem · Miljøfyrtårn**)
- **Production URL**: [https://www.miljofyrtarn.no/](https://www.miljofyrtarn.no/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#0000` canvas, `#000` ink, `#00aceb` accent)
- **Summary**: Miljøfyrtårn er Norges ledende miljøsertifisering. Kom i gang med sertifisering og miljøledelse i LUMA – et verktøy som gjør arbeidet enk...
- **Total Clean CSS Variables Extracted**: `29` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `matterFont`
- **Body Font Stack**: `matterFont Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `1.75rem`, `2rem`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 1.75rem`, `line-height: 1`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `1.75rem`, `2rem`)
- **Metadata & Labels**: CSS variables `--media-caption-h: 4rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0000` | `textarea { background-color: #0000 }` |
| **Primary Typography Ink** | `#808080` | `::backdrop { border-color: gray }` (`#808080`) |
| **Elevated Surface / Card Substrate** | `#f73146` | `.custom-underline.orange:after { background-color: #f73146 }` |
| **Interactive Accent / Highlight** | `#00aceb` | `.custom-underline.blue:after { background-color: #00aceb }` |
| **Secondary / Muted Copy** | `#000` | `.border-black { border-color: #000 }` |
| **Structural Hairline Border** | `#1cc600` | `.border-green { border-color: #1cc600 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-matter` | `"matterFont", "matterFont Fallback"` | Typography / Scale Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-xl` | `36rem` | Layout / Spatial Grid Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--font-weight-semibold` | `600` | Typography / Scale Token |
| `--font-weight-bold` | `700` | Typography / Scale Token |
| `--leading-tight` | `1.25` | Typography / Scale Token |
| `--leading-normal` | `1.5` | Typography / Scale Token |
| `--radius-md` | `.375rem` | Elevation / Border Token |
| `--radius-lg` | `.5rem` | Elevation / Border Token |
| `--radius-xl` | `.75rem` | Elevation / Border Token |
| `--radius-2xl` | `1rem` | Elevation / Border Token |
| `--ease-out` | `cubic-bezier(0, 0, .2, 1)` | Motion / Easing Token |
| `--ease-in-out` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--animate-pulse` | `pulse 2s cubic-bezier(.4, 0, .6, 1) infinite` | Motion / Easing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.top-bar> — `www-miljofyrtarn-no`)**:
   - Landmark `<nav class="top-bar pointer-events-none">` hosting `Hjem · Miljøfyrtårn` navigation (`Interaktiv veiviser · Start registrering · Finn konsulent · Kundehistorier`), DOM attributes (`data-precedence="next"`, `data-href="/_next/static/chunks/..."`, `data-nosnippet`, `data-template="popup"`), and stylesheet rule `font_3b00f4b4-module__5KZDLG__cla... { font-family:matterFont,matterFont Fallback }`.
2. **Hero Stage & Focal Lead (<section.stage> — `Norges mest brukte miljøsertifiser`)**:
   - Landmark `<section class="stage relative">` presenting display lead `Norges mest brukte miljøsertifisering` and copy excerpt *"Nødvendig 24 Nødvendige cookies bidra til å gjøre en nettside bru"* over `#0000` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.image-fullscreen> — `Fordi bærekraft er konkurransekraf`)**:
   - Landmark `<section class="image-fullscreen lines-scope">` rendering section `Fordi bærekraft er konkurransekraft` with copy *"Cloudflare 1 Lær mer om denne leverandøren cf.turnstile.u Denne i"*, asset references (`MatterMedium-s.p.02fj0~m~0rj1..woff2`, `MatterRegular-s.p.111lwj_hik8ci.w...`, `MatterRegularItalic-s.p.013o7st81...`, `MatterSemiBold-s.p.0kyaxl0f.k2ut....`), and grid rule `rfont_3b00f4b4-module__5KZDLG__va... { --font-matter:"matterFont", "matterFont Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.image-group> — `Fornøyde kunder sier`)**:
   - Landmark `<section class="image-group lines-scope">` framing `Fornøyde kunder sier` and `Hvorfor bli Miljøfyrtårn` (*"Lær mer om denne leverandøren"*) with `#f73146` surface cards, `#00aceb` accents, and `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.lines-scope> — `https://www.miljofyrtarn.no/`)**:
   - Landmark `<footer class="lines-scope overflow-clip">` anchoring `Hjem · Miljøfyrtårn` footer links (`Interaktiv veiviser · Start registrering · Finn konsulent · Kundehistorier`), copy *"Denne informasjonskapselen brukes til å skille mellom mennes"*, and `#1cc600` structural dividers.
