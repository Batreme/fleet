---
title: "APIs & Protocols: jetalto-com"
date: 2026-11-14
target: "[[overview|jetalto-com]]"
---

# Discovered APIs & Protocols: jetalto-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/geo.php` | `200` | REST endpoint |
| `GET` | `/data/airports-top.json` | `200` | REST endpoint |
| `POST` | `/api/track.php` | `200` | REST endpoint |
| `GET` | `/api/geo.php` | `200` | REST endpoint |
| `GET` | `/data/airports.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/geo.php
```json
{
  "type": "object",
  "properties": {
    "country": {
      "type": "string"
    },
    "source": {
      "type": "string"
    },
    "airport": {
      "type": "object",
      "properties": {
        "iata": {
          "type": "string"
        },
        "icao": {
          "type": "string"
        },
        "city": {
          "type": "string"
        },
        "name": {
          "type": "string"
        },
        "co": {
          "type": "string"
        },
        "lat": {
          "type": "number"
        },
        "lon": {
          "type": "number"
        }
      }
    }
  }
}
```
### `GET` /data/airports-top.json
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "n": {
        "type": "string"
      },
      "c": {
        "type": "string"
      },
      "co": {
        "type": "string"
      },
      "i": {
        "type": "string"
      },
      "ic": {
        "type": "string"
      },
      "lat": {
        "type": "number"
      },
      "lon": {
        "type": "number"
      }
    }
  }
}
```
### `POST` /api/track.php
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
### `GET` /api/geo.php
```json
{
  "type": "object",
  "properties": {
    "country": {
      "type": "string"
    },
    "source": {
      "type": "string"
    },
    "airport": {
      "type": "object",
      "properties": {
        "iata": {
          "type": "string"
        },
        "icao": {
          "type": "string"
        },
        "city": {
          "type": "string"
        },
        "name": {
          "type": "string"
        },
        "co": {
          "type": "string"
        },
        "lat": {
          "type": "number"
        },
        "lon": {
          "type": "number"
        }
      }
    }
  }
}
```
### `GET` /data/airports.json
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "n": {
        "type": "string"
      },
      "c": {
        "type": "string"
      },
      "co": {
        "type": "string"
      },
      "i": {
        "type": "string"
      },
      "ic": {
        "type": "string"
      },
      "lat": {
        "type": "number"
      },
      "lon": {
        "type": "number"
      }
    }
  }
}
```

