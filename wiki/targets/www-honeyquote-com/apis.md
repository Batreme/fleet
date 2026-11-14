---
title: "APIs & Protocols: www-honeyquote-com"
date: 2026-11-14
target: "[[overview|www-honeyquote-com]]"
---

# Discovered APIs & Protocols: www-honeyquote-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/context-v2/117608328` | `200` | REST endpoint |
| `POST` | `/prediction/117608328` | `200` | REST endpoint |
| `GET` | `/6a21ae820094dc6f56f29b98/6a4ea11836b242da919994de_260708_HoneyQuote.json` | `200` | REST endpoint |
| `POST` | `/logger` | `200` | REST endpoint |
| `POST` | `/logger` | `200` | REST endpoint |
| `GET` | `/pixel-config/v1/BUBiygMZXVHQuj7krwmj2p.json` | `200` | REST endpoint |
| `POST` | `/-/events/page-event` | `200` | REST endpoint |
| `POST` | `/v1/sdk/events` | `202` | REST endpoint |
| `POST` | `/-/widgets/get` | `200` | REST endpoint |
| `GET` | `/6a21ae820094dc6f56f29b98/6a4272c4e60eb2e1ad2d0dfb_bb8fb27d8ed8d99402a8c7ad95289bf3_animation.json` | `200` | REST endpoint |
| `GET` | `/6a21ae820094dc6f56f29b98/6a4272c4e60eb2e1ad2d0dfb_bb8fb27d8ed8d99402a8c7ad95289bf3_animation.json` | `200` | REST endpoint |
| `GET` | `/6a21ae820094dc6f56f29b98/6a4272c4e60eb2e1ad2d0dfb_bb8fb27d8ed8d99402a8c7ad95289bf3_animation.json` | `200` | REST endpoint |
| `GET` | `/6a21ae820094dc6f56f29b98/6a4272c4e60eb2e1ad2d0dfb_bb8fb27d8ed8d99402a8c7ad95289bf3_animation.json` | `200` | REST endpoint |
| `GET` | `/6a21ae820094dc6f56f29b98/6a4272c4e60eb2e1ad2d0dfb_bb8fb27d8ed8d99402a8c7ad95289bf3_animation.json` | `200` | REST endpoint |
| `GET` | `/6a21ae820094dc6f56f29b98/6a4272c4e60eb2e1ad2d0dfb_bb8fb27d8ed8d99402a8c7ad95289bf3_animation.json` | `200` | REST endpoint |
| `GET` | `/6a21ae820094dc6f56f29b98/6a4272c4e60eb2e1ad2d0dfb_bb8fb27d8ed8d99402a8c7ad95289bf3_animation.json` | `200` | REST endpoint |
| `GET` | `/6a21ae820094dc6f56f29b98/6a4272c4e60eb2e1ad2d0dfb_bb8fb27d8ed8d99402a8c7ad95289bf3_animation.json` | `200` | REST endpoint |
| `GET` | `/6a21ae820094dc6f56f29b98/6a4272c4e60eb2e1ad2d0dfb_bb8fb27d8ed8d99402a8c7ad95289bf3_animation.json` | `200` | REST endpoint |
| `GET` | `/6a21ae820094dc6f56f29b98/6a4272c4e60eb2e1ad2d0dfb_bb8fb27d8ed8d99402a8c7ad95289bf3_animation.json` | `200` | REST endpoint |
| `GET` | `/6a21ae820094dc6f56f29b98/6a4272c4e60eb2e1ad2d0dfb_bb8fb27d8ed8d99402a8c7ad95289bf3_animation.json` | `200` | REST endpoint |
| `POST` | `/events` | `200` | REST endpoint |
| `POST` | `/events` | `200` | REST endpoint |
| `GET` | `/api/v2/client/auth/0surti` | `200` | REST endpoint |
| `POST` | `/v1/sdk/events` | `202` | REST endpoint |
| `GET` | `/6a21ae820094dc6f56f29b98/6a4ea11836b242da919994de_260708_HoneyQuote.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /context-v2/117608328
```json
{
  "type": "object",
  "properties": {
    "requestId": {
      "type": "string"
    },
    "clientIp": {
      "type": "string"
    },
    "userAgentDigest": {
      "type": "string"
    },
    "userAgent": {
      "type": "object",
      "properties": {
        "deviceClass": {
          "type": "string"
        },
        "deviceName": {
          "type": "string"
        },
        "deviceBrand": {
          "type": "string"
        },
        "osClass": {
          "type": "string"
        },
        "osName": {
          "type": "string"
        },
        "osVersion": {
          "type": "string"
        },
        "agentClass": {
          "type": "string"
        },
        "agentName": {
          "type": "string"
        },
        "agentVersionMajor": {
          "type": "string"
        }
      }
    },
    "location": {
      "type": "object",
      "properties": {
        "countryIso": {
          "type": "string"
        },
        "countryName": {
          "type": "string"
        }
      }
    },
    "integrationData": {
      "type": "object",
      "properties": {}
    }
  }
}
```
### `POST` /prediction/117608328
```json
{
  "type": "object",
  "properties": {
    "policy": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "timestamp": {
          "type": "number"
        },
        "experiences": {
          "type": "object",
          "properties": {}
        }
      }
    }
  }
}
```
### `GET` /6a21ae820094dc6f56f29b98/6a4ea11836b242da919994de_260708_HoneyQuote.json
```json
{
  "type": "object",
  "properties": {
    "v": {
      "type": "string"
    },
    "fr": {
      "type": "number"
    },
    "ip": {
      "type": "number"
    },
    "op": {
      "type": "number"
    },
    "w": {
      "type": "number"
    },
    "h": {
      "type": "number"
    },
    "nm": {
      "type": "string"
    },
    "ddd": {
      "type": "number"
    },
    "assets": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "nm": {
            "type": "any"
          },
          "layers": {
            "type": "any"
          }
        }
      }
    },
    "layers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "ddd": {
            "type": "any"
          },
          "ind": {
            "type": "any"
          },
          "ty": {
            "type": "any"
          },
          "nm": {
            "type": "any"
          },
          "parent": {
            "type": "any"
          },
          "sr": {
            "type": "any"
          },
          "ks": {
            "type": "any"
          },
          "ao": {
            "type": "any"
          },
          "shapes": {
            "type": "any"
          },
          "ip": {
            "type": "any"
          },
          "op": {
            "type": "any"
          },
          "st": {
            "type": "any"
          },
          "bm": {
            "type": "any"
          }
        }
      }
    },
    "markers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "tm": {
            "type": "any"
          },
          "cm": {
            "type": "any"
          },
          "dr": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `POST` /logger
```json
{
  "type": "object",
  "properties": {}
}
```
### `POST` /logger
```json
{
  "type": "object",
  "properties": {}
}
```
### `GET` /pixel-config/v1/BUBiygMZXVHQuj7krwmj2p.json
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
### `POST` /-/events/page-event
```json
{
  "type": "object",
  "properties": {
    "session_id": {
      "type": "string"
    },
    "session_key": {
      "type": "string"
    }
  }
}
```
### `POST` /-/widgets/get
```json
{
  "type": "object",
  "properties": {
    "widgets": {
      "type": "array",
      "items": "any"
    },
    "has_logo": {
      "type": "boolean"
    },
    "enabled_gdpr": {
      "type": "boolean"
    },
    "country_code": {
      "type": "string"
    },
    "cdn_url": {
      "type": "string"
    },
    "date_format": {
      "type": "string"
    },
    "prioritization": {
      "type": "boolean"
    }
  }
}
```
### `GET` /6a21ae820094dc6f56f29b98/6a4272c4e60eb2e1ad2d0dfb_bb8fb27d8ed8d99402a8c7ad95289bf3_animation.json
```json
{
  "type": "object",
  "properties": {
    "v": {
      "type": "string"
    },
    "meta": {
      "type": "object",
      "properties": {
        "g": {
          "type": "string"
        },
        "a": {
          "type": "string"
        },
        "k": {
          "type": "string"
        },
        "d": {
          "type": "string"
        },
        "tc": {
          "type": "string"
        }
      }
    },
    "fr": {
      "type": "number"
    },
    "ip": {
      "type": "number"
    },
    "op": {
      "type": "number"
    },
    "w": {
      "type": "number"
    },
    "h": {
      "type": "number"
    },
    "nm": {
      "type": "string"
    },
    "ddd": {
      "type": "number"
    },
    "assets": {
      "type": "array",
      "items": "any"
    },
    "layers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "ddd": {
            "type": "any"
          },
          "ind": {
            "type": "any"
          },
          "ty": {
            "type": "any"
          },
          "nm": {
            "type": "any"
          },
          "sr": {
            "type": "any"
          },
          "ks": {
            "type": "any"
          },
          "ao": {
            "type": "any"
          },
          "shapes": {
            "type": "any"
          },
          "ip": {
            "type": "any"
          },
          "op": {
            "type": "any"
          },
          "st": {
            "type": "any"
          },
          "bm": {
            "type": "any"
          }
        }
      }
    },
    "markers": {
      "type": "array",
      "items": "any"
    }
  }
}
```

