---
title: "APIs & Protocols: vault-hyperiux-com"
date: 2026-11-14
target: "vault-hyperiux-com"
---

# Discovered APIs & Protocols: vault-hyperiux-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/pricing-region` | `200` | REST endpoint |
| `GET` | `/api/effects/search-index` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/pricing-region
```json
{
  "type": "object",
  "properties": {
    "currency": {
      "type": "string"
    }
  }
}
```
### `GET` /api/effects/search-index
```json
{
  "type": "object",
  "properties": {
    "effects": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "any"
          },
          "title": {
            "type": "any"
          },
          "description": {
            "type": "any"
          },
          "categories": {
            "type": "any"
          },
          "slug": {
            "type": "any"
          },
          "effectSlug": {
            "type": "any"
          },
          "categorySlug": {
            "type": "any"
          },
          "tier": {
            "type": "any"
          },
          "addedAt": {
            "type": "any"
          },
          "dependencies": {
            "type": "any"
          },
          "href": {
            "type": "any"
          }
        }
      }
    },
    "total": {
      "type": "number"
    }
  }
}
```

