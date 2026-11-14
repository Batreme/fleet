---
title: "APIs & Protocols: ads-apple-com"
date: 2026-11-14
target: "[[overview|ads-apple-com]]"
---

# Discovered APIs & Protocols: ads-apple-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/.language-selector.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /.language-selector.json
```json
{
  "type": "object",
  "properties": {
    "docs": {
      "type": "object",
      "properties": {
        "footerLocaleList": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    },
    "current": {
      "type": "object",
      "properties": {
        "href": {
          "type": "string"
        },
        "data": {
          "type": "string"
        }
      }
    },
    "status": {
      "type": "string"
    }
  }
}
```

