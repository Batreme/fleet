---
title: "APIs & Protocols: www-gravelleduparc-com"
date: 2026-11-14
target: "www-gravelleduparc-com"
---

# Discovered APIs & Protocols: www-gravelleduparc-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/anonymous` | `200` | REST endpoint |
| `GET` | `/v1/archive` | `200` | REST endpoint |
| `GET` | `/v1/archive` | `200` | REST endpoint |
| `GET` | `/v1/archive` | `200` | REST endpoint |
| `GET` | `/v1/archive` | `429` | REST endpoint |
| `GET` | `/v1/archive` | `200` | REST endpoint |
| `GET` | `/v1/archive` | `200` | REST endpoint |
| `GET` | `/v1/archive` | `200` | REST endpoint |
| `GET` | `/v1/archive` | `200` | REST endpoint |
| `GET` | `/v1/archive` | `200` | REST endpoint |
| `GET` | `/v1/archive` | `200` | REST endpoint |
| `POST` | `/anonymous` | `200` | REST endpoint |
| `GET` | `/auth/web/access-token` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /v1/archive
```json
{
  "type": "object",
  "properties": {
    "latitude": {
      "type": "number"
    },
    "longitude": {
      "type": "number"
    },
    "generationtime_ms": {
      "type": "number"
    },
    "utc_offset_seconds": {
      "type": "number"
    },
    "timezone": {
      "type": "string"
    },
    "timezone_abbreviation": {
      "type": "string"
    },
    "elevation": {
      "type": "number"
    },
    "daily_units": {
      "type": "object",
      "properties": {
        "time": {
          "type": "string"
        },
        "temperature_2m_max": {
          "type": "string"
        },
        "temperature_2m_min": {
          "type": "string"
        },
        "precipitation_sum": {
          "type": "string"
        },
        "snowfall_sum": {
          "type": "string"
        }
      }
    },
    "daily": {
      "type": "object",
      "properties": {
        "time": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "temperature_2m_max": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "temperature_2m_min": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "precipitation_sum": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "snowfall_sum": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /v1/archive
```json
{
  "type": "object",
  "properties": {
    "latitude": {
      "type": "number"
    },
    "longitude": {
      "type": "number"
    },
    "generationtime_ms": {
      "type": "number"
    },
    "utc_offset_seconds": {
      "type": "number"
    },
    "timezone": {
      "type": "string"
    },
    "timezone_abbreviation": {
      "type": "string"
    },
    "elevation": {
      "type": "number"
    },
    "daily_units": {
      "type": "object",
      "properties": {
        "time": {
          "type": "string"
        },
        "temperature_2m_max": {
          "type": "string"
        },
        "temperature_2m_min": {
          "type": "string"
        },
        "precipitation_sum": {
          "type": "string"
        },
        "snowfall_sum": {
          "type": "string"
        }
      }
    },
    "daily": {
      "type": "object",
      "properties": {
        "time": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "temperature_2m_max": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "temperature_2m_min": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "precipitation_sum": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "snowfall_sum": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /v1/archive
```json
{
  "type": "object",
  "properties": {
    "latitude": {
      "type": "number"
    },
    "longitude": {
      "type": "number"
    },
    "generationtime_ms": {
      "type": "number"
    },
    "utc_offset_seconds": {
      "type": "number"
    },
    "timezone": {
      "type": "string"
    },
    "timezone_abbreviation": {
      "type": "string"
    },
    "elevation": {
      "type": "number"
    },
    "daily_units": {
      "type": "object",
      "properties": {
        "time": {
          "type": "string"
        },
        "temperature_2m_max": {
          "type": "string"
        },
        "temperature_2m_min": {
          "type": "string"
        },
        "precipitation_sum": {
          "type": "string"
        },
        "snowfall_sum": {
          "type": "string"
        }
      }
    },
    "daily": {
      "type": "object",
      "properties": {
        "time": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "temperature_2m_max": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "temperature_2m_min": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "precipitation_sum": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "snowfall_sum": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /v1/archive
```json
{
  "type": "object",
  "properties": {
    "reason": {
      "type": "string"
    },
    "error": {
      "type": "boolean"
    }
  }
}
```
### `GET` /v1/archive
```json
{
  "type": "object",
  "properties": {
    "latitude": {
      "type": "number"
    },
    "longitude": {
      "type": "number"
    },
    "generationtime_ms": {
      "type": "number"
    },
    "utc_offset_seconds": {
      "type": "number"
    },
    "timezone": {
      "type": "string"
    },
    "timezone_abbreviation": {
      "type": "string"
    },
    "elevation": {
      "type": "number"
    },
    "daily_units": {
      "type": "object",
      "properties": {
        "time": {
          "type": "string"
        },
        "temperature_2m_max": {
          "type": "string"
        },
        "temperature_2m_min": {
          "type": "string"
        },
        "precipitation_sum": {
          "type": "string"
        },
        "snowfall_sum": {
          "type": "string"
        }
      }
    },
    "daily": {
      "type": "object",
      "properties": {
        "time": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "temperature_2m_max": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "temperature_2m_min": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "precipitation_sum": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "snowfall_sum": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /v1/archive
```json
{
  "type": "object",
  "properties": {
    "latitude": {
      "type": "number"
    },
    "longitude": {
      "type": "number"
    },
    "generationtime_ms": {
      "type": "number"
    },
    "utc_offset_seconds": {
      "type": "number"
    },
    "timezone": {
      "type": "string"
    },
    "timezone_abbreviation": {
      "type": "string"
    },
    "elevation": {
      "type": "number"
    },
    "daily_units": {
      "type": "object",
      "properties": {
        "time": {
          "type": "string"
        },
        "temperature_2m_max": {
          "type": "string"
        },
        "temperature_2m_min": {
          "type": "string"
        },
        "precipitation_sum": {
          "type": "string"
        },
        "snowfall_sum": {
          "type": "string"
        }
      }
    },
    "daily": {
      "type": "object",
      "properties": {
        "time": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "temperature_2m_max": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "temperature_2m_min": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "precipitation_sum": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "snowfall_sum": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /v1/archive
```json
{
  "type": "object",
  "properties": {
    "latitude": {
      "type": "number"
    },
    "longitude": {
      "type": "number"
    },
    "generationtime_ms": {
      "type": "number"
    },
    "utc_offset_seconds": {
      "type": "number"
    },
    "timezone": {
      "type": "string"
    },
    "timezone_abbreviation": {
      "type": "string"
    },
    "elevation": {
      "type": "number"
    },
    "daily_units": {
      "type": "object",
      "properties": {
        "time": {
          "type": "string"
        },
        "temperature_2m_max": {
          "type": "string"
        },
        "temperature_2m_min": {
          "type": "string"
        },
        "precipitation_sum": {
          "type": "string"
        },
        "snowfall_sum": {
          "type": "string"
        }
      }
    },
    "daily": {
      "type": "object",
      "properties": {
        "time": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "temperature_2m_max": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "temperature_2m_min": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "precipitation_sum": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "snowfall_sum": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /v1/archive
```json
{
  "type": "object",
  "properties": {
    "latitude": {
      "type": "number"
    },
    "longitude": {
      "type": "number"
    },
    "generationtime_ms": {
      "type": "number"
    },
    "utc_offset_seconds": {
      "type": "number"
    },
    "timezone": {
      "type": "string"
    },
    "timezone_abbreviation": {
      "type": "string"
    },
    "elevation": {
      "type": "number"
    },
    "daily_units": {
      "type": "object",
      "properties": {
        "time": {
          "type": "string"
        },
        "temperature_2m_max": {
          "type": "string"
        },
        "temperature_2m_min": {
          "type": "string"
        },
        "precipitation_sum": {
          "type": "string"
        },
        "snowfall_sum": {
          "type": "string"
        }
      }
    },
    "daily": {
      "type": "object",
      "properties": {
        "time": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "temperature_2m_max": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "temperature_2m_min": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "precipitation_sum": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "snowfall_sum": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /v1/archive
```json
{
  "type": "object",
  "properties": {
    "latitude": {
      "type": "number"
    },
    "longitude": {
      "type": "number"
    },
    "generationtime_ms": {
      "type": "number"
    },
    "utc_offset_seconds": {
      "type": "number"
    },
    "timezone": {
      "type": "string"
    },
    "timezone_abbreviation": {
      "type": "string"
    },
    "elevation": {
      "type": "number"
    },
    "daily_units": {
      "type": "object",
      "properties": {
        "time": {
          "type": "string"
        },
        "temperature_2m_max": {
          "type": "string"
        },
        "temperature_2m_min": {
          "type": "string"
        },
        "precipitation_sum": {
          "type": "string"
        },
        "snowfall_sum": {
          "type": "string"
        }
      }
    },
    "daily": {
      "type": "object",
      "properties": {
        "time": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "temperature_2m_max": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "temperature_2m_min": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "precipitation_sum": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "snowfall_sum": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    }
  }
}
```

