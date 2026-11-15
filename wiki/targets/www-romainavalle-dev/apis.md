---
title: "APIs & Protocols: www-romainavalle-dev"
date: 2026-11-14
target: "www-romainavalle-dev"
---

# Discovered APIs & Protocols: www-romainavalle-dev

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/_payload.json` | `200` | REST endpoint |
| `GET` | `/_nuxt/builds/meta/9fd1e7ca-d36d-4832-8526-3ee7b6574157.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /_payload.json
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "data": {
        "type": "number"
      },
      "prerenderedAt": {
        "type": "number"
      }
    }
  }
}
```
### `GET` /_nuxt/builds/meta/9fd1e7ca-d36d-4832-8526-3ee7b6574157.json
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "timestamp": {
      "type": "number"
    },
    "prerendered": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  }
}
```

