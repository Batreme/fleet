---
title: "APIs & Protocols: wild-ag-ch"
date: 2026-11-14
target: "[[overview|wild-ag-ch]]"
---

# Discovered APIs & Protocols: wild-ag-ch

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/tracker/assets/nocodelytics.js` | `200` | REST endpoint |
| `GET` | `/68ffa3d5dcafaaf81d62a778/69c2635134330f9a9fdad551_wild-ag-loader.json` | `200` | REST endpoint |
| `GET` | `/api/tracker/uuid` | `200` | REST endpoint |
| `GET` | `/api/tracker/metrics` | `200` | REST endpoint |
| `GET` | `/api/tracker/n` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /68ffa3d5dcafaaf81d62a778/69c2635134330f9a9fdad551_wild-ag-loader.json
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
          "shapes": {
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
    }
  }
}
```
### `GET` /api/tracker/uuid
```json
{
  "type": "array",
  "items": {
    "type": "string"
  }
}
```
### `GET` /api/tracker/metrics
```json
{
  "type": "array",
  "items": "any"
}
```
### `GET` /api/tracker/n
```json
{
  "type": "object",
  "properties": {
    "jobId": {
      "type": "object",
      "properties": {
        "stream": {
          "type": "string"
        },
        "seq": {
          "type": "number"
        },
        "duplicate": {
          "type": "boolean"
        }
      }
    },
    "logs": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  }
}
```

