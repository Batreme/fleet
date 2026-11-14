---
title: "APIs & Protocols: loopsii-com"
date: 2026-11-14
target: "[[overview|loopsii-com]]"
---

# Discovered APIs & Protocols: loopsii-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/geo` | `200` | REST endpoint |
| `GET` | `/lotties/logo-left.json` | `200` | REST endpoint |
| `GET` | `/lotties/logo-right.json` | `200` | REST endpoint |
| `GET` | `/lotties/logo-loop.json` | `200` | REST endpoint |
| `GET` | `/lotties/logo.json` | `200` | REST endpoint |
| `GET` | `/api/users-count` | `200` | REST endpoint |
| `GET` | `/lotties/logo-loop.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/geo
```json
{
  "type": "object",
  "properties": {
    "$geoip_country_code": {
      "type": "string"
    },
    "$geoip_country_name": {
      "type": "string"
    },
    "$geoip_continent_code": {
      "type": "string"
    },
    "$geoip_continent_name": {
      "type": "string"
    },
    "$geoip_subdivision_1_code": {
      "type": "string"
    },
    "$geoip_city_name": {
      "type": "string"
    },
    "$geoip_postal_code": {
      "type": "string"
    },
    "$geoip_latitude": {
      "type": "number"
    },
    "$geoip_longitude": {
      "type": "number"
    },
    "$geoip_time_zone": {
      "type": "string"
    }
  }
}
```
### `GET` /lotties/logo-left.json
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
          "nm": {
            "type": "any"
          },
          "fr": {
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
          "tm": {
            "type": "any"
          },
          "w": {
            "type": "any"
          },
          "h": {
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
### `GET` /lotties/logo-right.json
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
          "nm": {
            "type": "any"
          },
          "fr": {
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
          "tt": {
            "type": "any"
          },
          "tp": {
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
          "tm": {
            "type": "any"
          },
          "w": {
            "type": "any"
          },
          "h": {
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
### `GET` /lotties/logo-loop.json
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
          "nm": {
            "type": "any"
          },
          "fr": {
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
          "tm": {
            "type": "any"
          },
          "w": {
            "type": "any"
          },
          "h": {
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
### `GET` /lotties/logo.json
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
          "nm": {
            "type": "any"
          },
          "fr": {
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
          "tt": {
            "type": "any"
          },
          "tp": {
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
          "tm": {
            "type": "any"
          },
          "w": {
            "type": "any"
          },
          "h": {
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
### `GET` /api/users-count
```json
{
  "type": "object",
  "properties": {
    "count": {
      "type": "number"
    }
  }
}
```
### `GET` /lotties/logo-loop.json
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
          "nm": {
            "type": "any"
          },
          "fr": {
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
          "tm": {
            "type": "any"
          },
          "w": {
            "type": "any"
          },
          "h": {
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

