---
title: "APIs & Protocols: www-tedxportland-com"
date: 2026-11-14
target: "www-tedxportland-com"
---

# Discovered APIs & Protocols: www-tedxportland-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/cdn-cgi/speculation` | `200` | REST endpoint |
| `POST` | `/cdn-cgi/rum` | `204` | REST endpoint |

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

