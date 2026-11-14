---
title: "UI & Design System: www-3d-discovery-fr"
date: 2026-11-14
target: "[[overview|www-3d-discovery-fr]]"
---

# UI Architecture & Design Tokens: www-3d-discovery-fr

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--sg-grade` | `url(#sg-grade)}.sg-ungraded,.sg-ungraded img{--sg-grade:none` |
| `--header-cell` | `56px` |
| `--header-cell` | `64px}}.header .container{max-width:none` |
| `--menu-offset` | `calc(56px + 2px)}@media (min-width:768px){.mobile-menu__pane` |
| `--primary` | `hover:not(:disabled){background:var(--text-secondary)}.butto` |
| `--secondary` | `hover:not(:disabled){background:var(--text-primary)` |
| `--ghost` | `hover:not(:disabled){color:var(--text-primary)` |
| `--outline` | `hover:not(:disabled){background:var(--text-primary)` |
| `--glass` | `hover:not(:disabled){background:var(--bg-glass-hover)` |
| `--gold` | `hover:not(:disabled){background:var(--text-secondary)}.butto` |
| `--hover` | `hover{box-shadow:none` |
| `--hover` | `hover .card__image img{transform:scale(1.05)}.card__content{` |
| `--dot` | `before{content:""` |
| `--pulse` | `before{content:""` |
| `--error` | `focus,.form__select--error:focus,.form__textarea--error:focu` |
| `--required` | `after{content:" *"` |
| `--error` | `focus{box-shadow:0 0 0 3px #ef444426}.input--success{backgro` |
| `--success` | `focus{box-shadow:0 0 0 3px #22c55e26}.input--sm{border-radiu` |
| `--c` | `#fff` |
| `--em-bg` | `var(--bg-body)` |
| `--em-fg` | `var(--text-primary)` |
| `--em-border` | `var(--border-default)` |
| `--em-muted` | `var(--text-muted)}[data-theme=dark] .embed-modal{--em-border` |
| `--launch` | `before,.sg-tile--launch:after{z-index:2}.sg-tile--launch .sg` |
| `--launch` | `hover .sg-launch-mark{color:var(--sg-bg)}.sg-tile--launch:ho` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `header__nav` |
| `<nav>` | `-` | `mobile-menu__nav` |
| `<header>` | `-` | `header` |
| `<main>` | `main` | `` |
| `<footer>` | `-` | `sg-footer` |
