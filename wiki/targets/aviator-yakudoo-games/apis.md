---
title: "APIs & Protocols: aviator-yakudoo-games"
date: 2026-11-14
target: "aviator-yakudoo-games"
---

# Discovered APIs & Protocols: aviator-yakudoo-games

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/api/plays` | `201` | REST endpoint |
| `GET` | `/api/leaderboard` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /api/plays
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "seed": {
      "type": "number"
    },
    "simBuild": {
      "type": "string"
    }
  }
}
```
### `GET` /api/leaderboard
```json
{
  "type": "object",
  "properties": {
    "entries": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "rank": {
            "type": "any"
          },
          "pseudo": {
            "type": "any"
          },
          "score": {
            "type": "any"
          }
        }
      }
    },
    "me": {
      "type": "null"
    }
  }
}
```

