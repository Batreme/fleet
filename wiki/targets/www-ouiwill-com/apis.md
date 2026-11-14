---
title: "APIs & Protocols: www-ouiwill-com"
date: 2026-11-14
target: "[[overview|www-ouiwill-com]]"
---

# Discovered APIs & Protocols: www-ouiwill-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/main/` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /main/
```json
{
  "type": "object",
  "properties": {
    "nav": {
      "type": "string"
    },
    "loader": {
      "type": "string"
    },
    "skin": {
      "type": "string"
    },
    "title": {
      "type": "string"
    },
    "cookies": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "_key": {
            "type": "any"
          },
          "_type": {
            "type": "any"
          },
          "cKID": {
            "type": "any"
          },
          "cKalw": {
            "type": "any"
          },
          "cKcat": {
            "type": "any"
          },
          "cKdur": {
            "type": "any"
          },
          "cKlist": {
            "type": "any"
          },
          "cKprov": {
            "type": "any"
          },
          "cKscript": {
            "type": "any"
          },
          "s_": {
            "type": "any"
          },
          "t_": {
            "type": "any"
          }
        }
      }
    },
    "coo": {
      "type": "object",
      "properties": {
        "modo": {
          "type": "string"
        },
        "fijo": {
          "type": "boolean"
        },
        "exp": {
          "type": "number"
        },
        "ver": {
          "type": "number"
        },
        "txt": {
          "type": "object",
          "properties": {
            "optout": {
              "type": "any"
            },
            "gpc": {
              "type": "any"
            }
          }
        },
        "embeds": {
          "type": "boolean"
        },
        "gpcBanner": {
          "type": "boolean"
        },
        "urlpass": {
          "type": "boolean"
        }
      }
    },
    "time": {
      "type": "number"
    }
  }
}
```

