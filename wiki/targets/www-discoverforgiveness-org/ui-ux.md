# UI & UX Architecture: www-discoverforgiveness-org

## Overview & Design Identity
- **Target**: `www-discoverforgiveness-org` (**Discover Forgiveness · Templeton World Charity Foundation**)
- **Production URL**: [https://www.discoverforgiveness.org/](https://www.discoverforgiveness.org/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fefefb` canvas, `#433f35` ink, `#abaa9c` accent)
- **Summary**: Explore the transformative power of forgiveness at Discover Forgiveness. Our experts, from psychologists to spiritual leaders, offer insi...
- **Total Clean CSS Variables Extracted**: `28` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Area Normal`
- **Body Font Stack**: `Queens`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **Hero Display (`H1`)**: CSS variables `--blush1: #f5bccb`; rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: CSS variables `--blush2: #eab`; rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: rule `small` (`font-size: 80%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fefefb` | `var(--off-white)` in `:root` |
| **Primary Typography Ink** | `#433f35` | `var(--dark)` in `:root` |
| **Elevated Surface / Card Substrate** | `#6251d2` | `var(--purple3)` in `:root` |
| **Interactive Accent / Highlight** | `#abaa9c` | `var(--tan5)` in `:root` |
| **Secondary / Muted Copy** | `#fbfaf4` | `var(--tan)` in `:root` |
| **Structural Hairline Border** | `#777269` | `var(--dk-gray)` in `:root` |
| **Variable Token (`--purple_transp`)** | `#8170f033` | `var(--purple_transp)` in `:root` |
| **Variable Token (`--tan4`)** | `#cbc8be` | `var(--tan4)` in `:root` |
| **Variable Token (`--tan3`)** | `#e2e2d5` | `var(--tan3)` in `:root` |
| **Variable Token (`--tan2`)** | `#f0f0e5` | `var(--tan2)` in `:root` |
| **Variable Token (`--transparent`)** | `#0000` | `var(--transparent)` in `:root` |
| **Variable Token (`--purple1`)** | `#d8d8e9` | `var(--purple1)` in `:root` |
| **Variable Token (`--purple2`)** | `#bfbee0` | `var(--purple2)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--off-white` | `#fefefb` | Canvas / Surface Token |
| `--dark` | `#433f35` | Canvas / Surface Token |
| `--purple3` | `#6251d2` | Color / Atmospheric Token |
| `--black` | `black` | Canvas / Surface Token |
| `--white` | `white` | Canvas / Surface Token |
| `--tan5` | `#abaa9c` | Color / Atmospheric Token |
| `--tan` | `#fbfaf4` | Color / Atmospheric Token |
| `--purple_transp` | `#8170f033` | Color / Atmospheric Token |
| `--dk-gray` | `#777269` | Color / Atmospheric Token |
| `--tan4` | `#cbc8be` | Color / Atmospheric Token |
| `--tan3` | `#e2e2d5` | Color / Atmospheric Token |
| `--tan2` | `#f0f0e5` | Color / Atmospheric Token |
| `--transparent` | `#0000` | Color / Atmospheric Token |
| `--purple1` | `#d8d8e9` | Color / Atmospheric Token |
| `--purple2` | `#bfbee0` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.section_header37> — `www-discoverforgiveness-org`)**:
   - Landmark `<header class="section_header37">` hosting `Discover Forgiveness · Templeton Wor` navigation (`Educators · Faith Leaders · Anthropology · Art · Digital Landscape`), DOM attributes (`data-wf-domain="www.discoverforgivene..."`, `data-wf-page="64b81f977202559487efb8c0"`, `data-wf-site="64b81f977202559487efb843"`, `data-animation="default"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.section_layout134> — `Discover Forgiveness`)**:
   - Landmark `<section class="section_layout134">` presenting display lead `Discover Forgiveness` and copy excerpt *"Discover Forgiveness"* over `#fefefb` canvas and `#433f35` ink.
3. **Primary Showcase & Content Grid (<section.section_layout349> — `What is Discover forgiveness?`)**:
   - Landmark `<section class="section_layout349">` rendering section `What is Discover forgiveness?` with copy *"Frontline workers include mental health professionals, faith lead"*, asset references (`cdn.prod.website-files.com`, `discover-forgiveness.webflow.shar...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.section_blog41> — `Forgiveness Tools`)**:
   - Landmark `<section class="section_blog41">` framing `Forgiveness Tools` and `Research` (*"Curious About Forgiveness Science"*) with `#6251d2` surface cards, `#abaa9c` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.footer3_component> — `https://www.discoverforgiveness.org/`)**:
   - Landmark `<footer class="footer3_component">` anchoring `Discover Forgiveness · Templeton` footer links (`Educators · Faith Leaders · Anthropology · Art · Digital Landscape`), copy *"Mental Health Professionals"*, and `#777269` structural dividers.
