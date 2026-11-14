---
title: "APIs & Protocols: santalarch-com"
date: 2026-11-14
target: "[[overview|santalarch-com]]"
---

# Discovered APIs & Protocols: santalarch-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/_nuxt/builds/meta/08bc0b24-806f-4d88-b7d6-f5aecb73dfb7.json` | `200` | REST endpoint |
| `GET` | `/sequences/watch_white.json` | `200` | REST endpoint |
| `GET` | `/sequences/room.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /_nuxt/builds/meta/08bc0b24-806f-4d88-b7d6-f5aecb73dfb7.json
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
    "matcher": {
      "type": "object",
      "properties": {
        "static": {
          "type": "object",
          "properties": {}
        },
        "wildcard": {
          "type": "object",
          "properties": {}
        },
        "dynamic": {
          "type": "object",
          "properties": {}
        }
      }
    },
    "prerendered": {
      "type": "array",
      "items": "any"
    }
  }
}
```
### `GET` /sequences/watch_white.json
```json
{
  "type": "object",
  "properties": {
    "codec": {
      "type": "string"
    },
    "width": {
      "type": "number"
    },
    "height": {
      "type": "number"
    },
    "fps": {
      "type": "number"
    },
    "description": {
      "type": "string"
    },
    "totalFrames": {
      "type": "number"
    },
    "chunks": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "file": {
            "type": "any"
          },
          "size": {
            "type": "any"
          }
        }
      }
    },
    "frames": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "c": {
            "type": "any"
          },
          "o": {
            "type": "any"
          },
          "l": {
            "type": "any"
          },
          "t": {
            "type": "any"
          },
          "ty": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /sequences/room.json
```json
{
  "type": "object",
  "properties": {
    "codec": {
      "type": "string"
    },
    "width": {
      "type": "number"
    },
    "height": {
      "type": "number"
    },
    "fps": {
      "type": "number"
    },
    "description": {
      "type": "string"
    },
    "totalFrames": {
      "type": "number"
    },
    "chunks": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "file": {
            "type": "any"
          },
          "size": {
            "type": "any"
          }
        }
      }
    },
    "frames": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "c": {
            "type": "any"
          },
          "o": {
            "type": "any"
          },
          "l": {
            "type": "any"
          },
          "t": {
            "type": "any"
          },
          "ty": {
            "type": "any"
          }
        }
      }
    }
  }
}
```

