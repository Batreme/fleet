---
title: "APIs & Protocols: www-peryton-film-com"
date: 2026-11-14
target: "www-peryton-film-com"
---

# Discovered APIs & Protocols: www-peryton-film-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/62592e43fcc89072cd807fdc/6261c1e3231ac921b318b5bd_lf30_editor_wxbp4r2d.json` | `200` | REST endpoint |
| `POST` | `/api/send` | `200` | REST endpoint |
| `POST` | `/api/send` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /62592e43fcc89072cd807fdc/6261c1e3231ac921b318b5bd_lf30_editor_wxbp4r2d.json
```json
{
  "type": "object",
  "properties": {
    "v": {
      "type": "string"
    },
    "meta": {
      "type": "object",
      "properties": {
        "g": {
          "type": "string"
        },
        "a": {
          "type": "string"
        },
        "k": {
          "type": "string"
        },
        "d": {
          "type": "string"
        },
        "tc": {
          "type": "string"
        }
      }
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
          "layers": {
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
### `POST` /api/send
```json
{
  "type": "object",
  "properties": {
    "cache": {
      "type": "string"
    },
    "sessionId": {
      "type": "string"
    },
    "visitId": {
      "type": "string"
    }
  }
}
```
### `POST` /api/send
```json
{
  "type": "object",
  "properties": {
    "cache": {
      "type": "string"
    },
    "sessionId": {
      "type": "string"
    },
    "visitId": {
      "type": "string"
    }
  }
}
```

