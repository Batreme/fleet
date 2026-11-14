---
title: "APIs & Protocols: www-discoverforgiveness-org"
date: 2026-11-14
target: "[[overview|www-discoverforgiveness-org]]"
---

# Discovered APIs & Protocols: www-discoverforgiveness-org

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/64b81f977202559487efb843/6536f1d8d42c74fdfbf0a5db_T7ArU3Wk1Y.json` | `200` | REST endpoint |
| `GET` | `/sites/clnjqfmug00020jtp08nv0z5a` | `200` | REST endpoint |
| `GET` | `/favorites` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /64b81f977202559487efb843/6536f1d8d42c74fdfbf0a5db_T7ArU3Wk1Y.json
```json
{
  "type": "object",
  "properties": {
    "nm": {
      "type": "string"
    },
    "ddd": {
      "type": "number"
    },
    "h": {
      "type": "number"
    },
    "w": {
      "type": "number"
    },
    "meta": {
      "type": "object",
      "properties": {
        "g": {
          "type": "string"
        }
      }
    },
    "layers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "ty": {
            "type": "any"
          },
          "nm": {
            "type": "any"
          },
          "sr": {
            "type": "any"
          },
          "st": {
            "type": "any"
          },
          "op": {
            "type": "any"
          },
          "ip": {
            "type": "any"
          },
          "hd": {
            "type": "any"
          },
          "ddd": {
            "type": "any"
          },
          "bm": {
            "type": "any"
          },
          "hasMask": {
            "type": "any"
          },
          "ao": {
            "type": "any"
          },
          "ks": {
            "type": "any"
          },
          "ef": {
            "type": "any"
          },
          "ind": {
            "type": "any"
          }
        }
      }
    },
    "v": {
      "type": "string"
    },
    "fr": {
      "type": "number"
    },
    "op": {
      "type": "number"
    },
    "ip": {
      "type": "number"
    },
    "assets": {
      "type": "array",
      "items": "any"
    }
  }
}
```
### `GET` /sites/clnjqfmug00020jtp08nv0z5a
```json
{
  "type": "object",
  "properties": {
    "mainScriptUrl": {
      "type": "string"
    },
    "backwardsCompatScriptUrl": {
      "type": "string"
    },
    "boosters": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "boosterType": {
            "type": "any"
          },
          "shortId": {
            "type": "any"
          },
          "data": {
            "type": "any"
          },
          "powerUpConfig": {
            "type": "any"
          },
          "referenceCollection": {
            "type": "any"
          }
        }
      }
    },
    "plugins": {
      "type": "array",
      "items": "any"
    },
    "branchVersion": {
      "type": "null"
    },
    "majorVersion": {
      "type": "number"
    },
    "minorVersion": {
      "type": "number"
    },
    "patchVersion": {
      "type": "number"
    }
  }
}
```
### `GET` /favorites
```json
{
  "type": "array",
  "items": "any"
}
```

