---
title: "UI & Design System: layersoftime-studio"
date: 2026-11-14
target: "[[overview|layersoftime-studio]]"
---

# UI Architecture & Design Tokens: layersoftime-studio

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--primary` | `hover{background:var(--fg)` |
| `--bg` | `#08090b` |
| `--panel` | `#0e1013` |
| `--panel-2` | `#14171b` |
| `--fg` | `#e9ecef` |
| `--muted` | `#8a9099` |
| `--faint` | `#767c85` |
| `--line` | `#e9ecef1f` |
| `--line-strong` | `#e9ecef47` |
| `--signal` | `#d4178f` |
| `--signal-live` | `#ff29c4` |
| `--signal-fill` | `#8f0e66` |
| `--parallax` | `#22d3ee` |
| `--parsec` | `#a3e635` |
| `--font-sans` | `"Söhne", -apple-system, BlinkMacSystemFont, "Segoe UI", Robo` |
| `--font-mono` | `"Söhne Mono", "JetBrains Mono", ui-monospace, SFMono-Regular` |
| `--ease` | `cubic-bezier(.22, .61, .36, 1)` |
| `--d-fast` | `.16s` |
| `--d-base` | `.32s` |
| `--d-slow` | `.64s` |
| `--gutter` | `16px` |
| `--col-gap` | `16px` |
| `--max` | `1680px` |
| `--header-h` | `56px` |
| `--fs-hero` | `clamp(2.75rem, 8vw, 9rem)` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `nav` |
| `<nav>` | `-` | `footer__col` |
| `<nav>` | `-` | `footer__col` |
| `<nav>` | `-` | `footer__col` |
| `<header>` | `-` | `header` |
| `<aside>` | `awwwards` | `awwwards` |
| `<main>` | `main` | `main` |
| `<footer>` | `-` | `footer` |
