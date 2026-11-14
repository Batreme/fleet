---
title: "APIs & Protocols: m3-pg-de"
date: 2026-11-14
target: "[[overview|m3-pg-de]]"
---

# Discovered APIs & Protocols: m3-pg-de

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/wp-json/contact-form-7/v1/contact-forms/37/feedback/schema` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /wp-json/contact-form-7/v1/contact-forms/37/feedback/schema
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

