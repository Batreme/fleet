---
title: "APIs & Protocols: runtimewire-com"
date: 2026-11-14
target: "[[overview|runtimewire-com]]"
---

# Discovered APIs & Protocols: runtimewire-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/public/pageview-token` | `200` | REST endpoint |
| `GET` | `/api/me` | `401` | REST endpoint |
| `GET` | `/api/membership/status` | `200` | REST endpoint |
| `GET` | `/api/public/giveaway` | `200` | REST endpoint |
| `GET` | `/api/public/giveaway/me` | `200` | REST endpoint |
| `GET` | `/api/public/ios-launch` | `200` | REST endpoint |
| `GET` | `/api/public/article-likes` | `200` | REST endpoint |
| `GET` | `/api/public/earnings/watching` | `200` | REST endpoint |
| `GET` | `/api/public/live/config` | `200` | REST endpoint |
| `GET` | `/api/public/leaderboard` | `200` | REST endpoint |
| `GET` | `/api/public/infra-status` | `200` | REST endpoint |
| `GET` | `/api/public/video-posters/eyJzb3VyY2VQYXRoIjoidHdlZXQtdmlkZW9zL2NsYXVkZS1jb2RlLWRlc2t0b3AtY3VzdG9tLXRoZW1lcy1tb2RzLThhNjJjNDAzLm1wNCIsInNvdXJjZVJldmlzaW9uIjpudWxsfQ.ac6WJnJD4wk2jMA57Nx6eaSQkyDQxVGcwmVBvFrUbL4` | `302` | REST endpoint |
| `GET` | `/api/public/video-posters/eyJzb3VyY2VQYXRoIjoidHdlZXQtdmlkZW9zL252aWRpYS1ncjAwdC0yLXJvYm90LW1vZGVsLWh1bWFuLXZpZGVvLWRkNjg3NTY4Lm1wNCIsInNvdXJjZVJldmlzaW9uIjpudWxsfQ.O0vFJr65VSIOpFdK4_ZNC6ffelTkjAuJD-V6j9tRXSw` | `302` | REST endpoint |
| `GET` | `/api/public/video-posters/eyJzb3VyY2VQYXRoIjoidHdlZXQtdmlkZW9zL2dyb2stYm90LWpvaW4tbWVldGluZ3MtdGFrZS13b3JrLWNhbGwtNTVjMjM2MDIubXA0Iiwic291cmNlUmV2aXNpb24iOm51bGx9.UXs2rE1AszijGq3EaoIDvI-X_AHe9_BGZhPNWtQGUL4` | `302` | REST endpoint |
| `GET` | `/api/public/ads/frontend-settings` | `200` | REST endpoint |
| `GET` | `/api/auth/apple/config` | `200` | REST endpoint |
| `GET` | `/api/auth/line/config` | `200` | REST endpoint |
| `GET` | `/api/auth/google/one-tap/config` | `200` | REST endpoint |
| `GET` | `/api/public/gravity/config` | `200` | REST endpoint |
| `POST` | `/api/public/giveaway/action` | `200` | REST endpoint |
| `POST` | `/api/public/giveaway/action` | `200` | REST endpoint |
| `POST` | `/api/public/giveaway/action` | `200` | REST endpoint |
| `POST` | `/api/public/giveaway/action` | `200` | REST endpoint |
| `POST` | `/api/public/pageview` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/public/pageview-token
```json
{
  "type": "object",
  "properties": {
    "token": {
      "type": "string"
    },
    "expiresAt": {
      "type": "string"
    }
  }
}
```
### `GET` /api/me
```json
{
  "type": "object",
  "properties": {
    "error": {
      "type": "string"
    }
  }
}
```
### `GET` /api/membership/status
```json
{
  "type": "object",
  "properties": {
    "visible": {
      "type": "boolean"
    },
    "purchasesAvailable": {
      "type": "boolean"
    },
    "signedIn": {
      "type": "boolean"
    },
    "isPro": {
      "type": "boolean"
    },
    "tier": {
      "type": "null"
    },
    "realtime": {
      "type": "boolean"
    },
    "prompts": {
      "type": "object",
      "properties": {
        "liveMonthly": {
          "type": "string"
        },
        "proMonthly": {
          "type": "string"
        },
        "intelligenceMonthly": {
          "type": "string"
        },
        "intro": {
          "type": "null"
        }
      }
    },
    "upgrade": {
      "type": "null"
    },
    "lapsed": {
      "type": "boolean"
    },
    "accountAgeDays": {
      "type": "null"
    },
    "readerGrace": {
      "type": "null"
    },
    "freeRss": {
      "type": "null"
    }
  }
}
```
### `GET` /api/public/giveaway
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "title": {
      "type": "string"
    },
    "tagline": {
      "type": "string"
    },
    "status": {
      "type": "string"
    },
    "entriesOpen": {
      "type": "boolean"
    },
    "promotionActive": {
      "type": "boolean"
    },
    "closesAt": {
      "type": "string"
    },
    "verificationEndsAt": {
      "type": "string"
    },
    "drawAt": {
      "type": "string"
    },
    "rulesVersion": {
      "type": "string"
    },
    "rulesText": {
      "type": "string"
    },
    "privacyText": {
      "type": "string"
    },
    "supportEmail": {
      "type": "string"
    },
    "siteKey": {
      "type": "string"
    },
    "imageUrl": {
      "type": "string"
    },
    "blockers": {
      "type": "array",
      "items": "any"
    },
    "eligibility": {
      "type": "string"
    }
  }
}
```
### `GET` /api/public/giveaway/me
```json
{
  "type": "object",
  "properties": {
    "state": {
      "type": "string"
    },
    "signedIn": {
      "type": "boolean"
    },
    "acceptedEntries": {
      "type": "number"
    },
    "acceptedReferrals": {
      "type": "number"
    },
    "pendingReferrals": {
      "type": "number"
    },
    "freeBonuses": {
      "type": "number"
    },
    "newsletterConsent": {
      "type": "boolean"
    },
    "referralUrl": {
      "type": "null"
    },
    "isTest": {
      "type": "boolean"
    },
    "reason": {
      "type": "null"
    },
    "country": {
      "type": "null"
    },
    "region": {
      "type": "null"
    },
    "rulesVersion": {
      "type": "string"
    },
    "arm": {
      "type": "string"
    },
    "promptAllowed": {
      "type": "boolean"
    },
    "appeals": {
      "type": "array",
      "items": "any"
    }
  }
}
```
### `GET` /api/public/ios-launch
```json
{
  "type": "object",
  "properties": {
    "launchId": {
      "type": "string"
    },
    "phase": {
      "type": "string"
    },
    "promotionsActive": {
      "type": "boolean"
    },
    "temporaryPromotionsActive": {
      "type": "boolean"
    },
    "appStoreUrl": {
      "type": "string"
    },
    "landingPath": {
      "type": "string"
    },
    "articleUrl": {
      "type": "string"
    },
    "endsAt": {
      "type": "string"
    }
  }
}
```
### `GET` /api/public/article-likes
```json
{
  "type": "object",
  "properties": {
    "likedArticleIds": {
      "type": "array",
      "items": "any"
    }
  }
}
```
### `GET` /api/public/earnings/watching
```json
{
  "type": "object",
  "properties": {
    "watching": {
      "type": "array",
      "items": "any"
    },
    "unavailable": {
      "type": "array",
      "items": "any"
    },
    "upcoming": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "eventId": {
            "type": "any"
          },
          "companyName": {
            "type": "any"
          },
          "ticker": {
            "type": "any"
          },
          "expectedDate": {
            "type": "any"
          },
          "timeOfDay": {
            "type": "any"
          },
          "windowStart": {
            "type": "any"
          },
          "windowEnd": {
            "type": "any"
          },
          "alertEligible": {
            "type": "any"
          },
          "status": {
            "type": "any"
          }
        }
      }
    },
    "published": {
      "type": "array",
      "items": "any"
    }
  }
}
```
### `GET` /api/public/live/config
```json
{
  "type": "object",
  "properties": {
    "live": {
      "type": "boolean"
    },
    "platform": {
      "type": "null"
    },
    "youtubeVideoId": {
      "type": "null"
    },
    "youtubeChannelId": {
      "type": "null"
    },
    "twitchChannel": {
      "type": "null"
    },
    "twitchVideoId": {
      "type": "null"
    },
    "facebookHref": {
      "type": "null"
    },
    "linkedinUrn": {
      "type": "null"
    },
    "xStatusId": {
      "type": "null"
    },
    "xBroadcastId": {
      "type": "null"
    },
    "xHandle": {
      "type": "string"
    }
  }
}
```
### `GET` /api/public/leaderboard
```json
{
  "type": "object",
  "properties": {
    "period": {
      "type": "string"
    },
    "entries": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "rank": {
            "type": "any"
          },
          "displayName": {
            "type": "any"
          },
          "avatarUrl": {
            "type": "any"
          },
          "level": {
            "type": "any"
          },
          "levelName": {
            "type": "any"
          },
          "avatarFrame": {
            "type": "any"
          },
          "xp": {
            "type": "any"
          },
          "isMe": {
            "type": "any"
          }
        }
      }
    }
  }
}
```

