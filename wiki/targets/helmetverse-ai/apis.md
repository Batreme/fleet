---
title: "APIs & Protocols: helmetverse-ai"
date: 2026-11-14
target: "[[overview|helmetverse-ai]]"
---

# Discovered APIs & Protocols: helmetverse-ai

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/graphql` | `200` | GraphQL: `GetCompetitions` |

---

## 📦 Inferred Payload Schemas

### `POST` /graphql
```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "activeCompetition": {
          "type": "object",
          "properties": {
            "slug": {
              "type": "any"
            },
            "year": {
              "type": "any"
            },
            "season_number": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "status": {
              "type": "any"
            },
            "submissions_open_at": {
              "type": "any"
            },
            "submissions_close_at": {
              "type": "any"
            },
            "voting_open_at": {
              "type": "any"
            },
            "voting_close_at": {
              "type": "any"
            },
            "__typename": {
              "type": "any"
            }
          }
        },
        "previousCompetition": {
          "type": "object",
          "properties": {
            "slug": {
              "type": "any"
            },
            "year": {
              "type": "any"
            },
            "season_number": {
              "type": "any"
            },
            "winningEntry": {
              "type": "any"
            },
            "__typename": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```

