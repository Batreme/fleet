---
title: "APIs & Protocols: www-incroy-com"
date: 2026-11-14
target: "[[overview|www-incroy-com]]"
---

# Discovered APIs & Protocols: www-incroy-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/tracker/event` | `200` | REST endpoint |
| `GET` | `/bp/sOFXBWhqPK/settings` | `200` | REST endpoint |
| `GET` | `/6a21b956b61cf447eaaeea3c/6a5d0b12cd56089dc7cb077d_chat-icon.json` | `200` | REST endpoint |
| `GET` | `/6a21b956b61cf447eaaeea3c/6a5d0b1286cf13ef3e601118_globe-icon.json` | `200` | REST endpoint |
| `GET` | `/6a21b956b61cf447eaaeea3c/6a5d0b12cd56089dc7cb077d_chat-icon.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /bp/sOFXBWhqPK/settings
```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean"
    },
    "data": {
      "type": "object",
      "properties": {
        "tracking_script_id": {
          "type": "string"
        },
        "workspace_uuid": {
          "type": "string"
        },
        "active": {
          "type": "boolean"
        },
        "settings": {
          "type": "object",
          "properties": {
            "features": {
              "type": "any"
            },
            "integrations": {
              "type": "any"
            },
            "countryAllowed": {
              "type": "any"
            },
            "urlFilters": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `GET` /6a21b956b61cf447eaaeea3c/6a5d0b12cd56089dc7cb077d_chat-icon.json
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
          "refId": {
            "type": "any"
          },
          "w": {
            "type": "any"
          },
          "h": {
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
          }
        }
      }
    }
  }
}
```
### `GET` /6a21b956b61cf447eaaeea3c/6a5d0b1286cf13ef3e601118_globe-icon.json
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
          "refId": {
            "type": "any"
          },
          "w": {
            "type": "any"
          },
          "h": {
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
          }
        }
      }
    }
  }
}
```
### `GET` /6a21b956b61cf447eaaeea3c/6a5d0b12cd56089dc7cb077d_chat-icon.json
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
          "refId": {
            "type": "any"
          },
          "w": {
            "type": "any"
          },
          "h": {
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
          }
        }
      }
    }
  }
}
```

