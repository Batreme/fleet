---
title: "APIs & Protocols: north-cloud"
date: 2026-11-14
target: "north-cloud"
---

# Discovered APIs & Protocols: north-cloud

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/pixel-config/v1/CAXMmsTgtUKh8VYkh17d9o.json` | `200` | REST endpoint |
| `GET` | `/pixel/ip-info` | `200` | REST endpoint |
| `POST` | `/v1/sdk/events` | `202` | REST endpoint |
| `GET` | `/pixel/8230244d-c798-4378-b9db-b8bc08374ec5/settings` | `200` | REST endpoint |
| `POST` | `/events` | `200` | REST endpoint |
| `GET` | `/pixel/phoenix/rp/j` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /pixel-config/v1/CAXMmsTgtUKh8VYkh17d9o.json
```json
{
  "type": "object",
  "properties": {
    "automatic_advanced_matching_enabled": {
      "type": "boolean"
    }
  }
}
```
### `GET` /pixel/ip-info
```json
{
  "type": "object",
  "properties": {
    "ipInfo": {
      "type": "object",
      "properties": {
        "as": {
          "type": "string"
        },
        "city": {
          "type": "string"
        },
        "country": {
          "type": "string"
        },
        "countryCode": {
          "type": "string"
        },
        "isp": {
          "type": "string"
        },
        "lat": {
          "type": "number"
        },
        "lon": {
          "type": "number"
        },
        "org": {
          "type": "string"
        },
        "query": {
          "type": "string"
        },
        "region": {
          "type": "string"
        },
        "regionName": {
          "type": "string"
        },
        "status": {
          "type": "string"
        },
        "timezone": {
          "type": "string"
        },
        "zip": {
          "type": "string"
        }
      }
    },
    "isCloudProvider": {
      "type": "boolean"
    }
  }
}
```
### `GET` /pixel/8230244d-c798-4378-b9db-b8bc08374ec5/settings
```json
{
  "type": "object",
  "properties": {
    "pixelUseCerebroWaterfall": {
      "type": "boolean"
    },
    "pixelNonUsIpCompanyLookup": {
      "type": "boolean"
    },
    "pixelNonUsVisitors": {
      "type": "string"
    },
    "pixelNonUsIpCompanyLookupEnabled": {
      "type": "boolean"
    },
    "tartarus": {
      "type": "boolean"
    },
    "pixelMode": {
      "type": "string"
    }
  }
}
```
### `GET` /pixel/phoenix/rp/j
```json
{
  "type": "object",
  "properties": {
    "bakers": {
      "type": "array",
      "items": "any"
    }
  }
}
```

