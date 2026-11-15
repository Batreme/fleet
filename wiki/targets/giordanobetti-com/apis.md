---
title: "APIs & Protocols: giordanobetti-com"
date: 2026-11-14
target: "giordanobetti-com"
---

# Discovered APIs & Protocols: giordanobetti-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/cdn-cgi/speculation` | `200` | REST endpoint |
| `GET` | `/_nuxt/builds/meta/9a96bf43-b302-42c8-8fa2-141f8c5aa1e8.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /cdn-cgi/speculation
```json
{
  "type": "object",
  "properties": {
    "tag": {
      "type": "string"
    },
    "prefetch": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "eagerness": {
            "type": "any"
          },
          "source": {
            "type": "any"
          },
          "where": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /_nuxt/builds/meta/9a96bf43-b302-42c8-8fa2-141f8c5aa1e8.json
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
      "items": "any"
    }
  }
}
```

