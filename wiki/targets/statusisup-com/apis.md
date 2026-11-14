---
title: "APIs & Protocols: statusisup-com"
date: 2026-11-14
target: "[[overview|statusisup-com]]"
---

# Discovered APIs & Protocols: statusisup-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/` | `200` | REST endpoint |
| `GET` | `/data/catalog-release.json` | `200` | REST endpoint |
| `GET` | `/data/sid-public-metrics.json` | `200` | REST endpoint |
| `GET` | `/api/trpc/sidMetrics.current` | `200` | REST endpoint |
| `GET` | `/getconfig/sodar` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /
```json
{
  "type": "object",
  "properties": {
    "buttons": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  }
}
```
### `GET` /data/catalog-release.json
```json
{
  "type": "object",
  "properties": {
    "schemaVersion": {
      "type": "number"
    },
    "generatedAt": {
      "type": "string"
    },
    "source": {
      "type": "object",
      "properties": {
        "refreshedAt": {
          "type": "string"
        },
        "etag": {
          "type": "string"
        },
        "total": {
          "type": "number"
        },
        "totalPages": {
          "type": "number"
        }
      }
    },
    "windows": {
      "type": "object",
      "properties": {
        "outageCount90d": {
          "type": "object",
          "properties": {
            "label": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "available": {
              "type": "any"
            }
          }
        },
        "outageCount12m": {
          "type": "object",
          "properties": {
            "label": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "available": {
              "type": "any"
            }
          }
        },
        "outageCountAllTime": {
          "type": "object",
          "properties": {
            "label": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "available": {
              "type": "any"
            }
          }
        }
      }
    },
    "records": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "serviceId": {
            "type": "any"
          },
          "slug": {
            "type": "any"
          },
          "name": {
            "type": "any"
          },
          "category": {
            "type": "any"
          },
          "canonicalSidUrl": {
            "type": "any"
          },
          "officialDomain": {
            "type": "any"
          },
          "trackedSince": {
            "type": "any"
          },
          "outageCount90d": {
            "type": "any"
          },
          "outageCount12m": {
            "type": "any"
          },
          "outageCountAllTime": {
            "type": "any"
          },
          "latestOutageAt": {
            "type": "any"
          },
          "refreshedAt": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /data/sid-public-metrics.json
```json
{
  "type": "object",
  "properties": {
    "schemaVersion": {
      "type": "number"
    },
    "fetchedAt": {
      "type": "string"
    },
    "serviceDisplay": {
      "type": "string"
    },
    "serviceHeadlineFloor": {
      "type": "number"
    },
    "serviceExact": {
      "type": "number"
    },
    "websiteDisplay": {
      "type": "string"
    },
    "websiteCountFloor": {
      "type": "number"
    },
    "categoryExact": {
      "type": "number"
    },
    "sourceUrls": {
      "type": "object",
      "properties": {
        "homepage": {
          "type": "string"
        },
        "directory": {
          "type": "string"
        }
      }
    }
  }
}
```
### `GET` /api/trpc/sidMetrics.current
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "result": {
        "type": "object",
        "properties": {
          "data": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /getconfig/sodar
```json
{
  "type": "object",
  "properties": {
    "sodar_query_id": {
      "type": "string"
    },
    "injector_basename": {
      "type": "string"
    },
    "bg_hash_basename": {
      "type": "string"
    },
    "bg_binary": {
      "type": "string"
    },
    "rc_enable": {
      "type": "string"
    },
    "bg_snapshot_delay_ms": {
      "type": "string"
    },
    "is_gen_204": {
      "type": "string"
    }
  }
}
```

