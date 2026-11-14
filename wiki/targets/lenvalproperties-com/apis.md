---
title: "APIs & Protocols: lenvalproperties-com"
date: 2026-11-14
target: "[[overview|lenvalproperties-com]]"
---

# Discovered APIs & Protocols: lenvalproperties-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/tftl-logo_white.json` | `200` | REST endpoint |
| `GET` | `/sketch/sketch-repair-layout.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /tftl-logo_white.json
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
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "w": {
            "type": "any"
          },
          "h": {
            "type": "any"
          },
          "u": {
            "type": "any"
          },
          "p": {
            "type": "any"
          },
          "e": {
            "type": "any"
          }
        }
      }
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
          "cl": {
            "type": "any"
          },
          "refId": {
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
    }
  }
}
```
### `GET` /sketch/sketch-repair-layout.json
```json
{
  "type": "object",
  "properties": {
    "sourceGeometrySHA256": {
      "type": "string"
    },
    "kind": {
      "type": "string"
    },
    "indexCount": {
      "type": "number"
    },
    "patches": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "triangles": {
            "type": "any"
          },
          "uv": {
            "type": "any"
          }
        }
      }
    }
  }
}
```

