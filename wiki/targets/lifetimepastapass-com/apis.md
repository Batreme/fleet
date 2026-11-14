---
title: "APIs & Protocols: lifetimepastapass-com"
date: 2026-11-14
target: "[[overview|lifetimepastapass-com]]"
---

# Discovered APIs & Protocols: lifetimepastapass-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/home-counters` | `200` | REST endpoint |
| `GET` | `/game/score` | `200` | REST endpoint |
| `GET` | `/api/recent-votes` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/home-counters
```json
{
  "type": "object",
  "properties": {
    "unique_visitors": {
      "type": "number"
    },
    "total_votes": {
      "type": "number"
    },
    "dri_quote": {
      "type": "object",
      "properties": {
        "price": {
          "type": "number"
        },
        "change": {
          "type": "number"
        },
        "change_percent": {
          "type": "number"
        },
        "updated_at": {
          "type": "number"
        }
      }
    }
  }
}
```
### `GET` /game/score
```json
{
  "type": "object",
  "properties": {
    "score": {
      "type": "number"
    }
  }
}
```
### `GET` /api/recent-votes
```json
{
  "type": "object",
  "properties": {
    "votes": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "time": {
            "type": "any"
          },
          "pasta": {
            "type": "any"
          },
          "sauce": {
            "type": "any"
          },
          "second_sauce": {
            "type": "any"
          },
          "topping": {
            "type": "any"
          },
          "region": {
            "type": "any"
          },
          "country": {
            "type": "any"
          }
        }
      }
    }
  }
}
```

