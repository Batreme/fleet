# UI & UX Architecture: www-serko-ai

## Overview & Design Identity
- **Target**: `www-serko-ai` (**Serko.ai · AI Travel Agent**)
- **Production URL**: [https://www.serko.ai](https://www.serko.ai)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#b93fce` / `#f6f6f6`)
- **Summary**: Explore a smarter way to manage business travel with Serko.ai, the AI-native travel platform. It learns how you like to travel and handle...
- **Total Clean CSS Variables Extracted**: `590` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Jokker`
- **Body Font Stack**: `pretty`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--library_typography---font-size--h1: 5.25rem`, `--library_typography---font-size--display: 6rem`, `--osano-display-position: "bottom-left"`
- **Section Heading (`H2`)**: CSS variables `--library_typography---font-size--h2: 4rem`
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--library_typography---font-s...`, `var(--_typography---font-size--te...`, `var(--_text-style---font-size)`, `var(--_heading-style---font-size)`, `var(--_typography---font-size--h4)`)
- **Metadata & Labels**: CSS variables `--library_heading-style---letter-spacing: var(--library_typography---letter-spacing--0em)`, `--library_text-style---letter-spacing: var(--library_typography---letter-spacing--0em)`, `--library_spacing---section-space--small: 5rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#b93fce` | `var(--library---swatch--purple-500)` in `:root` |
| **Primary Typography Ink** | `#0078d4` | `var(--library---swatch--blue-500)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f13931` | `var(--_swatch---error)` in `:root` |
| **Interactive Accent / Highlight** | `#f6f6f6` | `var(--_swatch---light-2)` in `:root` |
| **Secondary / Muted Copy** | `#e8f3fe` | `var(--_swatch---light-3)` in `:root` |
| **Structural Hairline Border** | `#c0f2b5` | `var(--_swatch---positive-200)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--library_text-style---font-family` | `var(--library_typography---font--primary-family)` | Typography Ink Token |
| `--library_text-style---font-size` | `var(--library_typography---font-size--text-main)` | Typography Ink Token |
| `--library_text-style---line-height` | `var(--library_typography---line-height--1-5)` | Typography Ink Token |
| `--library_text-style---font-weight` | `var(--library_typography---font--primary-medium)` | Typography Ink Token |
| `--library_heading-style---margin-top` | `var(--library_spacing---space--4)` | Typography Ink Token |
| `--library_heading-style---margin-bottom` | `var(--library_spacing---space--4)` | Typography Ink Token |
| `--library_heading-style---font-family` | `var(--library_typography---font--primary-family)` | Typography Ink Token |
| `--library_heading-style---font-size` | `var(--library_typography---font-size--text-main)` | Typography Ink Token |
| `--library_heading-style---line-height` | `var(--library_typography---line-height--1-5)` | Typography Ink Token |
| `--library_heading-style---font-weight` | `var(--library_typography---font--primary-regular)` | Typography Ink Token |
| `--library_heading-style---letter-spacing` | `var(--library_typography---letter-spacing--0em)` | Typography Ink Token |
| `--library_text-style---margin-top` | `var(--library_spacing---space--4)` | Typography Ink Token |
| `--library_text-style---margin-bottom` | `var(--library_spacing---space--4)` | Typography Ink Token |
| `--library_spacing---space--6` | `2rem` | Layout / Spatial Grid Token |
| `--library_text-style---letter-spacing` | `var(--library_typography---letter-spacing--0em)` | Typography Ink Token |
| `--library_spacing---space--7` | `3rem` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav1_header> — `www-serko-ai`)**:
   - Landmark `<header class="nav1_header">` hosting `Serko.ai · AI Travel Agent` navigation (`Home · Platform · For companies · About · Log in`), DOM attributes (`data-wf-domain="www.serko.ai"`, `data-wf-page="6aa12b65e6dd0b96a2a83430"`, `data-wf-site="6aa12b65e6dd0b96a2a8345b"`, `data-wf-intellimize-customer-id="117114932"`), and stylesheet rule `img { object-fit:cover;width:100%;max-width:100% }`.
2. **Hero Stage & Focal Lead (<section.hero1_wrap> — `AI travel agent`)**:
   - Landmark `<section class="hero1_wrap u-gradient-bg-1">` presenting display lead `AI travel agent` and copy excerpt *"Opens in a new window"* over `#b93fce` canvas and `#f6f6f6` ink.
3. **Primary Showcase & Content Grid (<section.feature1_wrap> — `The last travel agent you’ll ever `)**:
   - Landmark `<section class="feature1_wrap u-background-3">` rendering section `The last travel agent you’ll ever need.` with copy *"Opens an external website"*, asset references (`cdn.prod.website-files.com`, `serko-ai.webflow.shared.96cab25cb...`, `serko-ai.webflow.6aa12b65e6dd0b96...`, `gtm.js`), and grid rule `strong { font-weight:700 }`.
4. **Interactive Detail & Feature Matrix (<section.feature2_wrap> — `Stress-free cancellation`)**:
   - Landmark `<section class="feature2_wrap">` framing `Stress-free cancellation` and `Book like it's refundable. Because it is.` (*"Opens an external website in a new window"*) with `#f13931` surface cards, `#f6f6f6` accents, and `blockquote { border-style:none;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.osano-cm-window> — `https://www.serko.ai`)**:
   - Landmark `<footer class="osano-cm-window">` anchoring `Serko.ai · AI Travel Agent` footer links (`Home · Platform · For companies · About · Log in`), copy *"<!---->Close this consent banner<!---->"*, and `#c0f2b5` structural dividers.
