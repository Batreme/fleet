---
title: "APIs & Protocols: southandstonestudio-com"
date: 2026-11-14
target: "[[overview|southandstonestudio-com]]"
---

# Discovered APIs & Protocols: southandstonestudio-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/v3/` | `200` | REST endpoint |
| `GET` | `/wp-json/wp/v2/edd-downloads` | `200` | REST endpoint |
| `GET` | `/v3/m-outer-0edadf75b42c6ef7240c043f3272f3f9.html` | `200` | REST endpoint |
| `GET` | `/v3/fingerprinted/js/m-outer-df5ee3b49f88025f22168cdfc5823764.js` | `200` | REST endpoint |
| `POST` | `/6` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /wp-json/wp/v2/edd-downloads
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": {
        "type": "number"
      },
      "slug": {
        "type": "string"
      },
      "title": {
        "type": "object",
        "properties": {
          "rendered": {
            "type": "any"
          }
        }
      },
      "edd-tags": {
        "type": "array",
        "items": "any"
      },
      "_links": {
        "type": "object",
        "properties": {
          "self": {
            "type": "any"
          },
          "collection": {
            "type": "any"
          },
          "about": {
            "type": "any"
          },
          "author": {
            "type": "any"
          },
          "version-history": {
            "type": "any"
          },
          "predecessor-version": {
            "type": "any"
          },
          "wp:featuredmedia": {
            "type": "any"
          },
          "wp:attachment": {
            "type": "any"
          },
          "wp:term": {
            "type": "any"
          },
          "curies": {
            "type": "any"
          }
        }
      },
      "_embedded": {
        "type": "object",
        "properties": {
          "wp:featuredmedia": {
            "type": "any"
          },
          "wp:term": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `POST` /6
```json
{
  "type": "object",
  "properties": {
    "muid": {
      "type": "string"
    },
    "guid": {
      "type": "string"
    },
    "sid": {
      "type": "string"
    }
  }
}
```

