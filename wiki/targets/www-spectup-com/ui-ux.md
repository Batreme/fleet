---
title: "UI & Design System: www-spectup-com"
date: 2026-11-14
target: "[[overview|www-spectup-com]]"
---

# UI Architecture & Design Tokens: www-spectup-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--hero-vh` | `100svh` |
| `--hero-bar` | `0px` |
| `--ink` | `#121212` |
| `--light` | `#FAFAFA` |
| `--yellow` | `#F8F32B` |
| `--g-d` | `#8A8A8A` |
| `--g-l` | `#6B6B6B` |
| `--line-d` | `rgba(250,250,250,.14)` |
| `--line-l` | `rgba(18,18,18,.13)` |
| `--t-hero` | `clamp(40px,6.4vw,102px)` |
| `--t-h1` | `clamp(30px,4.2vw,64px)` |
| `--t-h2` | `clamp(22px,2.5vw,36px)` |
| `--t-h3` | `clamp(17px,1.6vw,21px)` |
| `--t-lede` | `clamp(16px,1.3vw,19px)` |
| `--t-body` | `15px` |
| `--t-meta` | `12.5px` |
| `--t-micro` | `12px` |
| `--t-fig` | `clamp(38px,5.2vw,84px)` |
| `--w-wide` | `min(1760px,100vw)` |
| `--w-read` | `720px` |
| `--pad` | `72px` |
| `--gut` | `max(var(--pad),calc((100% - var(--w-wide)) / 2 + var(--pad))` |
| `--r` | `34px` |
| `--mono` | `ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospa` |
| `--s1` | `8px` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `nav` | `` |
| `<nav>` | `-` | `lf-sp-idx` |
| `<nav>` | `-` | `ft-ls` |
| `<nav>` | `-` | `ft-ls` |
| `<nav>` | `-` | `ft-ls` |
| `<nav>` | `-` | `ft-ls` |
| `<aside>` | `-` | `lf-sp-aside` |
| `<main>` | `main` | `` |
| `<footer>` | `-` | `ft has-canvas offrest` |
| `<dialog>` | `txm` | `pop pop--scroll pop--media txm` |
