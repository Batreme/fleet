---
title: "APIs & Protocols: realevate-agency"
date: 2026-11-14
target: "[[overview|realevate-agency]]"
---

# Discovered APIs & Protocols: realevate-agency

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/cdn-cgi/speculation` | `200` | REST endpoint |

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

