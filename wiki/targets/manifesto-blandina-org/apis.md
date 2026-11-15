---
title: "APIs & Protocols: manifesto-blandina-org"
date: 2026-11-14
target: "manifesto-blandina-org"
---

# Discovered APIs & Protocols: manifesto-blandina-org

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/_payload.json` | `200` | REST endpoint |
| `GET` | `/_nuxt/builds/meta/1db3be7a-9be0-46d0-98df-8f78403d6958.json` | `200` | REST endpoint |

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
### `GET` /_nuxt/builds/meta/1db3be7a-9be0-46d0-98df-8f78403d6958.json
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

