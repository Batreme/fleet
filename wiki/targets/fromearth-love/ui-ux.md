---
title: "UI & Design System: fromearth-love"
date: 2026-11-14
target: "[[overview|fromearth-love]]"
---

# UI Architecture & Design Tokens: fromearth-love

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--earth-ease` | `cubic-bezier(.19,1,.22,1)}
#earth-shell[open]{display:grid` |
| `--encre` | `#051236` |
| `--encre-2` | `#071a45` |
| `--encre-3` | `#0b2358` |
| `--texte` | `#FFFDE2` |
| `--muter` | `rgba(255, 253, 226, 0.6)` |
| `--efface` | `rgba(255, 253, 226, 0.3)` |
| `--hairline` | `rgba(255, 253, 226, 0.16)` |
| `--bleu` | `#1740A9` |
| `--ease` | `cubic-bezier(0.165, 0.84, 0.44, 1)` |
| `--ease-inout` | `cubic-bezier(0.76, 0, 0.24, 1)` |
| `--police` | `"TWK Lausanne", "Inter", -apple-system, sans-serif` |
| `--serif` | `var(--police)` |
| `--herbik` | `"Herbik", "Cormorant Garamond", serif` |
| `--mono` | `var(--police)` |
| `--p` | `0%` |
| `--p` | `100%` |
| `--noir` | `#000000` |
| `--filet` | `rgba(255, 253, 226, 0.16)` |
| `--police` | `"Terra Entry", -apple-system, sans-serif` |
| `--fiche-fond` | `#080b0ee8` |
| `--fiche-secondaire` | `#b5bec8` |
| `--fiche-ligne` | `#ffffff20` |
| `--police` | `'Hiragino Kaku Gothic ProN','Yu Gothic',Meiryo,sans-serif` |
| `--herbik` | `'Hiragino Mincho ProN','Yu Mincho',serif` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `calques` | `` |
| `<header>` | `titre` | `panneau` |
| `<header>` | `-` | `fiche-entete` |
| `<header>` | `-` | `` |
| `<aside>` | `filter-summary` | `` |
| `<aside>` | `model-notice` | `` |
| `<aside>` | `dossier` | `` |
| `<main>` | `earth-letter-main` | `` |
| `<footer>` | `-` | `actions` |
| `<dialog>` | `earth-shell` | `` |
| `<dialog>` | `language-dialog` | `` |
| `<dialog>` | `city-comparison` | `` |
| `<dialog>` | `view-sources` | `ux-dialog` |
| `<dialog>` | `view-share` | `ux-dialog` |
| `<dialog>` | `view-compare` | `ux-dialog` |
