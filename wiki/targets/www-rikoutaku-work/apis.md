---
title: "APIs & Protocols: www-rikoutaku-work"
date: 2026-11-14
target: "www-rikoutaku-work"
---

# Discovered APIs & Protocols: www-rikoutaku-work

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/models/layouts.json` | `200` | REST endpoint |
| `GET` | `/rest/v1/messages` | `-1` | REST endpoint |
| `GET` | `/rest/v1/messages` | `-1` | REST endpoint |
| `GET` | `/rest/v1/messages` | `-1` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /models/layouts.json
```json
{
  "type": "object",
  "properties": {
    "generated": {
      "type": "string"
    },
    "source": {
      "type": "string"
    },
    "space": {
      "type": "string"
    },
    "static": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "frozen": {
      "type": "array",
      "items": "any"
    },
    "names": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "layouts": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "collection": {
            "type": "any"
          },
          "t": {
            "type": "any"
          },
          "q": {
            "type": "any"
          },
          "_moved": {
            "type": "any"
          },
          "_substituted": {
            "type": "any"
          },
          "_offset": {
            "type": "any"
          },
          "_anchorSpreadMm": {
            "type": "any"
          },
          "_anchors": {
            "type": "any"
          }
        }
      }
    }
  }
}
```

