# UI & UX Architecture: heronaiapp-com

## Overview & Design Identity
- **Target**: `heronaiapp-com` (**Heron AI · Works inside your design tools**)
- **Production URL**: [https://heronaiapp.com/](https://heronaiapp.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#b3b3af` / `#b4b4b0`)
- **Summary**: Heron sees your model, spots problems, and suggests fixes as you design. When you approve, it makes the edit itself, all without leaving...
- **Total Clean CSS Variables Extracted**: `43` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geistmono`
- **Body Font Stack**: `BT Grotesk`
- **Monospace / Technical Font Stack**: `Geistmono`
- **Hero Display (`H1`)**: rule `h1` (`font-size: 7.2rem`, `line-height: 1em`, `font-weight: 500`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 2.4rem`, `line-height: 1.1em`, `letter-spacing: -.02em`, `font-weight: 500`)
- **Body Copy**: rule `p` (`font-size: 1rem`, `line-height: 1.1em`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `80%`, `75%`, `1em`, `14px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#b3b3af` | `var(--content--border)` in `:root` |
| **Primary Typography Ink** | `#fa3600` | `var(--content--brand)` in `:root` |
| **Elevated Surface / Card Substrate** | `#282828` | `var(--content--primary)` in `:root` |
| **Interactive Accent / Highlight** | `#b4b4b0` | `var(--content--disable)` in `:root` |
| **Secondary / Muted Copy** | `#72726f` | `var(--content--surface)` in `:root` |
| **Structural Hairline Border** | `#626260` | `var(--content--granite-gray)` in `:root` |
| **Variable Token (`--content--terriary`)** | `#282828b8` | `var(--content--terriary)` in `:root` |
| **Variable Token (`--content--secondary`)** | `#414140` | `var(--content--secondary)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--content--terriary` | `#282828b8` | Color / Atmospheric Token |
| `--size--padding-hero` | `calc(4.4rem + 1rem*2)` | Layout / Spatial Grid Token |
| `--size--max-screen-height` | `calc(100dvh - 1.6rem)` | Layout / Spatial Grid Token |
| `--content--border` | `#b3b3af` | Elevation / Border Token |
| `--size--border` | `max(1px,.1rem)` | Layout / Spatial Grid Token |
| `--content--brand` | `#fa3600` | Brand / Palette Token |
| `--content--primary` | `#282828` | Brand / Palette Token |
| `--content--white` | `white` | Canvas / Surface Token |
| `--content--disable` | `#b4b4b0` | Color / Atmospheric Token |
| `--content--surface` | `#72726f` | Canvas / Surface Token |
| `--content--granite-gray` | `#626260` | Color / Atmospheric Token |
| `--content--transparent` | `transparent` | Design System Custom Token |
| `--content--secondary` | `#414140` | Brand / Palette Token |
| `--size--line` | `0px` | Layout / Spatial Grid Token |
| `--trans-percent` | `0%` | Dimension / Scale Token |
| `--mask-percent` | `0%` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `heronaiapp-com`)**:
   - Landmark `<header class="header">` hosting `Heron AI · Works inside your design ` navigation (`Menu · Pricing Pricing · Insights Insights · About About`), DOM attributes (`data-wf-domain="heronai.webflow.io"`, `data-wf-page="6a4b5161f0d11f1602cc3ba1"`, `data-wf-site="6a4b5161f0d11f1602cc3bbf"`, `data-resources-saver-cleanup="branding"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.home-hero> — `An AI agent that works inside your`)**:
   - Landmark `<section class="home-hero">` presenting display lead `An AI agent that works inside your design tools` and copy excerpt *"This website uses cookies. Learn more"* over `#b3b3af` canvas and `#282828` ink.
3. **Primary Showcase & Content Grid (<section.home-intro> — `T H E R E P E T I T I V E P A R T `)**:
   - Landmark `<section class="home-intro">` rendering section `T H E R E P E T I T I V E P A R T S O F M O D E L...` with copy *"Heron Chat Widget Heron Chat Widget"*, asset references (`cdn.prod.website-files.com`, `heronai.webflow.shared.9f21166e0....`, `clarity.js`, `xxzxds4q6a`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.home-problem> — `Your design tools do what you tell`)**:
   - Landmark `<section class="home-problem">` framing `Your design tools do what you tell them, nothing...` and `RUN AN AGENT NATIVELY IN YOUR MODEL` (*"Heron Dashboard Heron Dashboard"*) with `#282828` surface cards, `#b4b4b0` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://heronaiapp.com/`)**:
   - Landmark `<footer class="footer">` anchoring `Heron AI · Works inside your des` footer links (`Menu · Pricing Pricing · Insights Insights · About About`), copy *"Resources Resources"*, and `#626260` structural dividers.
