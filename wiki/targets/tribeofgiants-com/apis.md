---
title: "APIs & Protocols: tribeofgiants-com"
date: 2026-11-14
target: "tribeofgiants-com"
---

# Discovered APIs & Protocols: tribeofgiants-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/access` | `200` | REST endpoint |
| `GET` | `/api/creators` | `200` | REST endpoint |
| `GET` | `/api/testimonials` | `200` | REST endpoint |
| `GET` | `/api/director` | `200` | REST endpoint |
| `POST` | `/api/track/land` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/access
```json
{
  "type": "object",
  "properties": {
    "signedIn": {
      "type": "boolean"
    },
    "member": {
      "type": "boolean"
    },
    "scenes": {
      "type": "object",
      "properties": {
        "faq": {
          "type": "string"
        },
        "how": {
          "type": "string"
        },
        "ends": {
          "type": "string"
        },
        "hero": {
          "type": "string"
        },
        "sort": {
          "type": "string"
        },
        "final": {
          "type": "string"
        },
        "spare": {
          "type": "string"
        },
        "inside": {
          "type": "string"
        },
        "mc_card": {
          "type": "string"
        },
        "mc_drop": {
          "type": "string"
        },
        "mc_swap": {
          "type": "string"
        },
        "char_liv": {
          "type": "string"
        },
        "char_noa": {
          "type": "string"
        },
        "journeys": {
          "type": "string"
        },
        "mc_dodge": {
          "type": "string"
        },
        "mc_guard": {
          "type": "string"
        },
        "mc_ledge": {
          "type": "string"
        },
        "mc_plank": {
          "type": "string"
        },
        "mc_share": {
          "type": "string"
        },
        "room_own": {
          "type": "string"
        }
      }
    }
  }
}
```
### `GET` /api/creators
```json
{
  "type": "object",
  "properties": {
    "creators": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "kind": {
            "type": "any"
          },
          "name": {
            "type": "any"
          },
          "title": {
            "type": "any"
          },
          "bio": {
            "type": "any"
          },
          "image_url": {
            "type": "any"
          },
          "link_url": {
            "type": "any"
          },
          "link_label": {
            "type": "any"
          },
          "location": {
            "type": "any"
          },
          "certified": {
            "type": "any"
          },
          "fee_note": {
            "type": "any"
          },
          "booking_url": {
            "type": "any"
          },
          "featured": {
            "type": "any"
          },
          "sort": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /api/testimonials
```json
{
  "type": "object",
  "properties": {
    "testimonials": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "name": {
            "type": "any"
          },
          "role": {
            "type": "any"
          },
          "location": {
            "type": "any"
          },
          "quote": {
            "type": "any"
          },
          "image_url": {
            "type": "any"
          },
          "rating": {
            "type": "any"
          },
          "result_note": {
            "type": "any"
          },
          "material_connection": {
            "type": "any"
          },
          "results_vary": {
            "type": "any"
          },
          "featured": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /api/director
```json
{
  "type": "object",
  "properties": {
    "signedIn": {
      "type": "boolean"
    }
  }
}
```
### `POST` /api/track/land
```json
{
  "type": "object",
  "properties": {
    "ok": {
      "type": "boolean"
    }
  }
}
```

