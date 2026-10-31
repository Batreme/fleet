---
title: "APIs & Protocols: almirakho-com"
date: 2026-10-31
target: "[[overview|almirakho-com]]"
---

# Discovered APIs & Protocols: almirakho-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/v2026-07-22/data/query/production` | `200` | REST endpoint |
| `GET` | `/v2026-07-22/data/query/production` | `200` | REST endpoint |
| `GET` | `/v2026-07-22/data/query/production` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /v2026-07-22/data/query/production
```json
{
  "type": "object",
  "properties": {
    "query": {
      "type": "string"
    },
    "result": {
      "type": "object",
      "properties": {
        "email": {
          "type": "string"
        },
        "instagram": {
          "type": "string"
        }
      }
    },
    "syncTags": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "ms": {
      "type": "number"
    }
  }
}
```
### `GET` /v2026-07-22/data/query/production
```json
{
  "type": "object",
  "properties": {
    "query": {
      "type": "string"
    },
    "result": {
      "type": "object",
      "properties": {
        "cover": {
          "type": "object",
          "properties": {
            "_type": {
              "type": "any"
            },
            "asset": {
              "type": "any"
            }
          }
        },
        "description": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "projects": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    },
    "syncTags": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "ms": {
      "type": "number"
    }
  }
}
```
### `GET` /v2026-07-22/data/query/production
```json
{
  "type": "object",
  "properties": {
    "query": {
      "type": "string"
    },
    "result": {
      "type": "object",
      "properties": {
        "cover": {
          "type": "object",
          "properties": {
            "_type": {
              "type": "any"
            },
            "asset": {
              "type": "any"
            }
          }
        },
        "description": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "projects": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    },
    "syncTags": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "ms": {
      "type": "number"
    }
  }
}
```

