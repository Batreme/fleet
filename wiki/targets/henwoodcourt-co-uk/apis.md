---
title: "APIs & Protocols: henwoodcourt-co-uk"
date: 2026-11-14
target: "[[overview|henwoodcourt-co-uk]]"
---

# Discovered APIs & Protocols: henwoodcourt-co-uk

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/player.js` | `200` | REST endpoint |
| `GET` | `/wp-content/themes/henwood-court/animations/logo.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /wp-content/themes/henwood-court/animations/logo.json
```json
{
  "type": "object",
  "properties": {
    "v": {
      "type": "string"
    },
    "fr": {
      "type": "number"
    },
    "ip": {
      "type": "number"
    },
    "op": {
      "type": "number"
    },
    "w": {
      "type": "number"
    },
    "h": {
      "type": "number"
    },
    "nm": {
      "type": "string"
    },
    "ddd": {
      "type": "number"
    },
    "assets": {
      "type": "array",
      "items": "any"
    },
    "layers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "ddd": {
            "type": "any"
          },
          "ind": {
            "type": "any"
          },
          "ty": {
            "type": "any"
          },
          "nm": {
            "type": "any"
          },
          "sr": {
            "type": "any"
          },
          "ks": {
            "type": "any"
          },
          "ao": {
            "type": "any"
          },
          "ip": {
            "type": "any"
          },
          "op": {
            "type": "any"
          },
          "st": {
            "type": "any"
          },
          "bm": {
            "type": "any"
          }
        }
      }
    },
    "markers": {
      "type": "array",
      "items": "any"
    },
    "props": {
      "type": "object",
      "properties": {}
    }
  }
}
```

