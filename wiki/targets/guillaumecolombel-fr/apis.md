---
title: "APIs & Protocols: guillaumecolombel-fr"
date: 2026-11-14
target: "guillaumecolombel-fr"
---

# Discovered APIs & Protocols: guillaumecolombel-fr

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/assets/fonts/integral-msdf.json` | `200` | REST endpoint |
| `GET` | `/_payload.json` | `200` | REST endpoint |
| `POST` | `/api/send` | `200` | REST endpoint |
| `GET` | `/_nuxt/builds/meta/4d34585f-908b-4abe-ab37-fe6648c821c9.json` | `200` | REST endpoint |
| `GET` | `/_payload.json` | `200` | REST endpoint |
| `GET` | `/about/_payload.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /assets/fonts/integral-msdf.json
```json
{
  "type": "object",
  "properties": {
    "pages": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "chars": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "index": {
            "type": "any"
          },
          "char": {
            "type": "any"
          },
          "width": {
            "type": "any"
          },
          "height": {
            "type": "any"
          },
          "xoffset": {
            "type": "any"
          },
          "yoffset": {
            "type": "any"
          },
          "xadvance": {
            "type": "any"
          },
          "chnl": {
            "type": "any"
          },
          "x": {
            "type": "any"
          },
          "y": {
            "type": "any"
          },
          "page": {
            "type": "any"
          }
        }
      }
    },
    "info": {
      "type": "object",
      "properties": {
        "face": {
          "type": "string"
        },
        "size": {
          "type": "number"
        },
        "bold": {
          "type": "number"
        },
        "italic": {
          "type": "number"
        },
        "charset": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "unicode": {
          "type": "number"
        },
        "stretchH": {
          "type": "number"
        },
        "smooth": {
          "type": "number"
        },
        "aa": {
          "type": "number"
        },
        "padding": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "spacing": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "outline": {
          "type": "number"
        }
      }
    },
    "common": {
      "type": "object",
      "properties": {
        "lineHeight": {
          "type": "number"
        },
        "base": {
          "type": "number"
        },
        "scaleW": {
          "type": "number"
        },
        "scaleH": {
          "type": "number"
        },
        "pages": {
          "type": "number"
        },
        "packed": {
          "type": "number"
        },
        "alphaChnl": {
          "type": "number"
        },
        "redChnl": {
          "type": "number"
        },
        "greenChnl": {
          "type": "number"
        },
        "blueChnl": {
          "type": "number"
        }
      }
    },
    "distanceField": {
      "type": "object",
      "properties": {
        "fieldType": {
          "type": "string"
        },
        "distanceRange": {
          "type": "number"
        }
      }
    },
    "kernings": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "first": {
            "type": "any"
          },
          "second": {
            "type": "any"
          },
          "amount": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /_payload.json
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "data": {
        "type": "number"
      },
      "prerenderedAt": {
        "type": "number"
      }
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
### `GET` /_nuxt/builds/meta/4d34585f-908b-4abe-ab37-fe6648c821c9.json
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "timestamp": {
      "type": "number"
    },
    "prerendered": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  }
}
```
### `GET` /_payload.json
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "data": {
        "type": "number"
      },
      "prerenderedAt": {
        "type": "number"
      }
    }
  }
}
```
### `GET` /about/_payload.json
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "data": {
        "type": "number"
      },
      "prerenderedAt": {
        "type": "number"
      }
    }
  }
}
```

