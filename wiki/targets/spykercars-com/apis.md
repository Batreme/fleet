---
title: "APIs & Protocols: spykercars-com"
date: 2026-10-31
target: "[[overview|spykercars-com]]"
---

# Discovered APIs & Protocols: spykercars-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/next/currency` | `200` | REST endpoint |
| `GET` | `/api/users/me` | `200` | REST endpoint |
| `GET` | `/api/users/me` | `200` | REST endpoint |
| `GET` | `/lottie/logo-reveal.json` | `200` | REST endpoint |
| `GET` | `/lottie/icon-navigation.json` | `200` | REST endpoint |
| `GET` | `/lottie/icon-boutique.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /next/currency
```json
{
  "type": "object",
  "properties": {
    "currency": {
      "type": "string"
    }
  }
}
```
### `GET` /api/users/me
```json
{
  "type": "object",
  "properties": {
    "user": {
      "type": "null"
    },
    "message": {
      "type": "string"
    }
  }
}
```
### `GET` /api/users/me
```json
{
  "type": "object",
  "properties": {
    "user": {
      "type": "null"
    },
    "message": {
      "type": "string"
    }
  }
}
```
### `GET` /lottie/logo-reveal.json
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
          "ct": {
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
### `GET` /lottie/icon-navigation.json
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
          "ct": {
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
      "items": {
        "type": "object",
        "properties": {
          "tm": {
            "type": "any"
          },
          "cm": {
            "type": "any"
          },
          "dr": {
            "type": "any"
          }
        }
      }
    },
    "props": {
      "type": "object",
      "properties": {}
    }
  }
}
```
### `GET` /lottie/icon-boutique.json
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
          "td": {
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
          "ct": {
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
      "items": {
        "type": "object",
        "properties": {
          "tm": {
            "type": "any"
          },
          "cm": {
            "type": "any"
          },
          "dr": {
            "type": "any"
          }
        }
      }
    },
    "props": {
      "type": "object",
      "properties": {}
    }
  }
}
```

