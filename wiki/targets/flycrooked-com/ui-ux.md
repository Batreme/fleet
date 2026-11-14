---
title: "UI & Design System: flycrooked-com"
date: 2026-11-14
target: "[[overview|flycrooked-com]]"
---

# UI Architecture & Design Tokens: flycrooked-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--ground` | `#0A0B0E` |
| `--bg` | `#0E0F13` |
| `--panel` | `#111318` |
| `--panel2` | `#191B23` |
| `--well` | `#16181E` |
| `--ink` | `#F4F6F9` |
| `--ink2` | `#C7CBD2` |
| `--muted` | `#9197A1` |
| `--faint` | `#737985` |
| `--ghost` | `#5C616C` |
| `--rule` | `#1F2128` |
| `--rule2` | `#2C2F38` |
| `--pink` | `#FF3D81` |
| `--live` | `#1CF2A6` |
| `--paper` | `#F4F6F9` |
| `--paper-ink` | `#0E0F13` |
| `--paper-2` | `#E4E7ED` |
| `--display` | `'Barlow Condensed','Arial Narrow',Impact,sans-serif` |
| `--wide` | `'Archivo','Helvetica Neue',Arial,sans-serif` |
| `--body` | `'Public Sans',system-ui,-apple-system,'Segoe UI',sans-serif` |
| `--mono` | `'IBM Plex Mono',ui-monospace,Menlo,monospace` |
| `--mark` | `'Crow Audiowide','Audiowide','Saira Extra Condensed','Arial ` |
| `--sf` | `-apple-system,BlinkMacSystemFont,'SF Pro Display','Public Sa` |
| `--gutter-l` | `max(16px,env(safe-area-inset-left,0px))` |
| `--gutter-r` | `max(16px,env(safe-area-inset-right,0px))` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `nav-links` |
| `<nav>` | `twBar` | `twbar` |
| `<nav>` | `-` | `sf-nav` |
| `<header>` | `nav` | `nav` |
| `<main>` | `top` | `` |
| `<footer>` | `sfoot` | `sfoot` |
