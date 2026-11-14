---
title: "APIs & Protocols: www-qissa-co-uk"
date: 2026-11-14
target: "[[overview|www-qissa-co-uk]]"
---

# Discovered APIs & Protocols: www-qissa-co-uk

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/wp-json/contact-form-7/v1/contact-forms/10/feedback/schema` | `200` | REST endpoint |
| `GET` | `/wp-json/contact-form-7/v1/contact-forms/10/refill` | `200` | REST endpoint |
| `POST` | `/eventbus/web` | `202` | REST endpoint |
| `POST` | `/eventbus/web` | `202` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /wp-json/contact-form-7/v1/contact-forms/10/feedback/schema
```json
{
  "type": "object",
  "properties": {
    "version": {
      "type": "string"
    },
    "locale": {
      "type": "string"
    },
    "rules": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "rule": {
            "type": "any"
          },
          "field": {
            "type": "any"
          },
          "error": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /wp-json/contact-form-7/v1/contact-forms/10/refill
```json
{
  "type": "array",
  "items": "any"
}
```

