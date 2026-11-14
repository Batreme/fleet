---
title: "APIs & Protocols: www-stellarmanagement-com"
date: 2026-11-14
target: "[[overview|www-stellarmanagement-com]]"
---

# Discovered APIs & Protocols: www-stellarmanagement-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/_nuxt/builds/meta/d89dab32-f18b-490a-aa4f-f3d141c70e9b.json` | `200` | REST endpoint |
| `GET` | `/cmsapi/news` | `200` | REST endpoint |
| `GET` | `/pagead/conversion/989561706/` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /_nuxt/builds/meta/d89dab32-f18b-490a-aa4f-f3d141c70e9b.json
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
### `GET` /cmsapi/news
```json
{
  "type": "object",
  "properties": {
    "newsList": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "newsID": {
            "type": "any"
          },
          "heading": {
            "type": "any"
          },
          "summary": {
            "type": "any"
          },
          "datePublish": {
            "type": "any"
          },
          "photo1": {
            "type": "any"
          },
          "timeToRead": {
            "type": "any"
          },
          "newsURL": {
            "type": "any"
          },
          "publisher": {
            "type": "any"
          }
        }
      }
    },
    "filters": {
      "type": "object",
      "properties": {
        "years": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    },
    "totalNews": {
      "type": "number"
    }
  }
}
```

