---
title: "UI & Design System: aizeitgeist-tv"
date: 2026-11-14
target: "[[overview|aizeitgeist-tv]]"
---

# UI Architecture & Design Tokens: aizeitgeist-tv

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--bg` | `#000` |
| `--fg` | `#f5f5f7` |
| `--fg-2` | `rgb(245 245 247 / .62)` |
| `--fg-3` | `rgb(245 245 247 / .5)` |
| `--fg-4` | `rgb(245 245 247 / .36)` |
| `--line` | `rgb(245 245 247 / .14)` |
| `--pill-line` | `rgb(245 245 247 / .3)` |
| `--sheen` | `rgb(245 245 247 / .32)` |
| `--pill-bg` | `rgb(20 20 20 / .72)` |
| `--pop-bg` | `rgb(16 16 16 / .92)` |
| `--kbd-line` | `rgb(245 245 247 / .28)` |
| `--kbd-bg` | `rgb(245 245 247 / .08)` |
| `--accent` | `#00ff66` |
| `--grid-alpha` | `.075` |
| `--font` | `"Schibsted Grotesk", "Helvetica Neue", Helvetica, Arial, san` |
| `--pill-h` | `60px` |
| `--stoerer-h` | `44px` |
| `--bg` | `#f5f5f7` |
| `--fg` | `#000` |
| `--fg-2` | `rgb(0 0 0 / .62)` |
| `--fg-3` | `rgb(0 0 0 / .55)` |
| `--fg-4` | `rgb(0 0 0 / .4)` |
| `--line` | `rgb(0 0 0 / .14)` |
| `--pill-line` | `rgb(0 0 0 / .3)` |
| `--sheen` | `rgb(0 0 0 / .22)` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `menu-grid` |
| `<nav>` | `-` | `search-topics mm-topics` |
| `<nav>` | `pill` | `pill` |
| `<nav>` | `search-topics` | `search-topics` |
| `<header>` | `brand` | `brand` |
| `<main>` | `-` | `below` |
| `<footer>` | `-` | `foot` |
| `<dialog>` | `ei-privacy` | `ei-privacy` |
| `<dialog>` | `site-menu` | `site-menu` |
| `<dialog>` | `nl-modal` | `intro nl-modal` |
| `<dialog>` | `source-dialog` | `source` |
| `<dialog>` | `lightbox` | `lightbox` |
| `<dialog>` | `intro-dialog` | `intro` |
| `<dialog>` | `ask-dialog` | `ask-dlg` |
| `<dialog>` | `reel-dialog` | `lightbox reel-dlg` |
