---
title: "APIs & Protocols: launch-joinautopilot-com"
date: 2026-11-14
target: "[[overview|launch-joinautopilot-com]]"
---

# Discovered APIs & Protocols: launch-joinautopilot-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/marketing-profiles` | `200` | REST endpoint |
| `GET` | `/api/platform-stats` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/marketing-profiles
```json
{
  "type": "object",
  "properties": {
    "list": {
      "type": "string"
    },
    "profiles": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "key": {
            "type": "any"
          },
          "teamKey": {
            "type": "any"
          },
          "name": {
            "type": "any"
          },
          "bio": {
            "type": "any"
          },
          "imageUrl": {
            "type": "any"
          },
          "pilotingSince": {
            "type": "any"
          },
          "totalAum": {
            "type": "any"
          },
          "totalSubscribers": {
            "type": "any"
          },
          "portfolioCount": {
            "type": "any"
          },
          "muxPlaybackId": {
            "type": "any"
          },
          "thumbnailUrl": {
            "type": "any"
          }
        }
      }
    },
    "fetchedAt": {
      "type": "string"
    }
  }
}
```
### `GET` /api/platform-stats
```json
{
  "type": "object",
  "properties": {
    "stats": {
      "type": "object",
      "properties": {
        "totalAssetsConnected": {
          "type": "number"
        },
        "amountInvested": {
          "type": "number"
        },
        "totalPayouts": {
          "type": "number"
        },
        "updatedAt": {
          "type": "string"
        }
      }
    },
    "fetchedAt": {
      "type": "string"
    }
  }
}
```

