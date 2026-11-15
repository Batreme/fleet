---
title: "APIs & Protocols: kohenavocats-com_avocats-droit-famille-paris"
date: 2026-11-14
target: "kohenavocats-com_avocats-droit-famille-paris"
---

# Discovered APIs & Protocols: kohenavocats-com_avocats-droit-famille-paris

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

