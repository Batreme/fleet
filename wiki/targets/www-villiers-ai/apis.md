---
title: "APIs & Protocols: www-villiers-ai"
date: 2026-11-14
target: "www-villiers-ai"
---

# Discovered APIs & Protocols: www-villiers-ai

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/api/analytics/track` | `200` | REST endpoint |
| `POST` | `/api/analytics/track` | `200` | REST endpoint |
| `GET` | `/api/geo-airports` | `200` | REST endpoint |
| `GET` | `/api/recent-searches` | `200` | REST endpoint |
| `GET` | `/api/geo-airports` | `200` | REST endpoint |
| `GET` | `/api/geo-airports` | `200` | REST endpoint |
| `GET` | `/api/recent-searches` | `200` | REST endpoint |
| `POST` | `/api/split/assign` | `200` | REST endpoint |
| `GET` | `/api/geo-airports` | `200` | REST endpoint |
| `GET` | `/api/recent-searches` | `200` | REST endpoint |
| `GET` | `/api/v1/agent/rollout` | `200` | REST endpoint |
| `GET` | `/api/recent-searches` | `200` | REST endpoint |
| `GET` | `/api/auth/me` | `200` | REST endpoint |
| `GET` | `/api/v1/public/contact-number` | `200` | REST endpoint |
| `GET` | `/api/exchange-rates` | `200` | REST endpoint |
| `GET` | `/api/exchange-rates` | `200` | REST endpoint |
| `GET` | `/api/exchange-rates` | `200` | REST endpoint |
| `GET` | `/api/exchange-rates` | `200` | REST endpoint |
| `GET` | `/api/v1/aircraft/8831b8d6-b5cc-4a35-819b-ae9225756835/photo/0` | `200` | REST endpoint |
| `GET` | `/api/v1/aircraft/f6f86867-7700-4145-9c12-cd948a398f5d/photo/0` | `200` | REST endpoint |
| `GET` | `/api/v1/aircraft/88d8ccdf-d15c-49c4-b25e-1f7a005533f5/photo/0` | `200` | REST endpoint |
| `GET` | `/api/v1/aircraft/cbd87a37-a2cb-483b-bf8a-1006abac6c2b/photo/0` | `200` | REST endpoint |
| `GET` | `/api/v1/aircraft/048b113a-3f88-4d44-91dd-b6882d892ee9/photo/0` | `200` | REST endpoint |
| `GET` | `/api/v1/aircraft/1b3afab8-15f3-431f-b32e-c689ae053381/photo/0` | `200` | REST endpoint |
| `GET` | `/api/v1/aircraft/cbacca09-ec34-4081-adc4-5c4a88623093/photo/0` | `200` | REST endpoint |
| `GET` | `/api/v1/aircraft/4f8dba71-a9ac-47f6-9658-55e57f525ef9/photo/0` | `200` | REST endpoint |
| `GET` | `/api/v1/aircraft/2b7c7fc3-2a6a-489c-ab63-801a2502caff/photo/0` | `200` | REST endpoint |
| `GET` | `/api/v1/aircraft/73d095d0-9a12-4028-9bea-8a6d709bc422/photo/0` | `200` | REST endpoint |
| `GET` | `/api/v1/aircraft/b3e7b8dd-e6fd-4ac7-b0c0-786ad9689f91/photo/0` | `200` | REST endpoint |
| `POST` | `/api/v1/agent/funnel` | `202` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /api/analytics/track
```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean"
    },
    "data": {
      "type": "object",
      "properties": {
        "success": {
          "type": "boolean"
        }
      }
    }
  }
}
```
### `POST` /api/analytics/track
```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean"
    },
    "data": {
      "type": "object",
      "properties": {
        "success": {
          "type": "boolean"
        }
      }
    }
  }
}
```
### `GET` /api/geo-airports
```json
{
  "type": "object",
  "properties": {
    "airports": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "code": {
            "type": "any"
          },
          "city": {
            "type": "any"
          },
          "name": {
            "type": "any"
          },
          "flag": {
            "type": "any"
          }
        }
      }
    },
    "city": {
      "type": "string"
    },
    "detected": {
      "type": "boolean"
    }
  }
}
```
### `GET` /api/recent-searches
```json
{
  "type": "object",
  "properties": {
    "searches": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "departureDate": {
            "type": "any"
          },
          "passengers": {
            "type": "any"
          },
          "searchedAt": {
            "type": "any"
          },
          "origin": {
            "type": "any"
          },
          "destination": {
            "type": "any"
          },
          "categoryEstimates": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /api/geo-airports
```json
{
  "type": "object",
  "properties": {
    "airports": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "code": {
            "type": "any"
          },
          "city": {
            "type": "any"
          },
          "name": {
            "type": "any"
          },
          "flag": {
            "type": "any"
          }
        }
      }
    },
    "city": {
      "type": "string"
    },
    "detected": {
      "type": "boolean"
    }
  }
}
```
### `GET` /api/geo-airports
```json
{
  "type": "object",
  "properties": {
    "airports": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "code": {
            "type": "any"
          },
          "city": {
            "type": "any"
          },
          "name": {
            "type": "any"
          },
          "flag": {
            "type": "any"
          }
        }
      }
    },
    "city": {
      "type": "string"
    },
    "detected": {
      "type": "boolean"
    }
  }
}
```
### `GET` /api/recent-searches
```json
{
  "type": "object",
  "properties": {
    "searches": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "departureDate": {
            "type": "any"
          },
          "passengers": {
            "type": "any"
          },
          "searchedAt": {
            "type": "any"
          },
          "origin": {
            "type": "any"
          },
          "destination": {
            "type": "any"
          },
          "categoryEstimates": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `POST` /api/split/assign
```json
{
  "type": "object",
  "properties": {
    "assignment": {
      "type": "object",
      "properties": {
        "test_id": {
          "type": "string"
        },
        "arm": {
          "type": "string"
        },
        "policy": {
          "type": "string"
        },
        "policy_version": {
          "type": "string"
        },
        "model_version": {
          "type": "null"
        },
        "assignment_id": {
          "type": "string"
        },
        "surface_key": {
          "type": "string"
        }
      }
    }
  }
}
```
### `GET` /api/geo-airports
```json
{
  "type": "object",
  "properties": {
    "airports": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "code": {
            "type": "any"
          },
          "city": {
            "type": "any"
          },
          "name": {
            "type": "any"
          },
          "flag": {
            "type": "any"
          }
        }
      }
    },
    "city": {
      "type": "string"
    },
    "detected": {
      "type": "boolean"
    }
  }
}
```
### `GET` /api/recent-searches
```json
{
  "type": "object",
  "properties": {
    "searches": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "departureDate": {
            "type": "any"
          },
          "passengers": {
            "type": "any"
          },
          "searchedAt": {
            "type": "any"
          },
          "origin": {
            "type": "any"
          },
          "destination": {
            "type": "any"
          },
          "categoryEstimates": {
            "type": "any"
          }
        }
      }
    }
  }
}
```

