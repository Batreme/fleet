---
title: "APIs & Protocols: gpg-dops-agency"
date: 2026-11-14
target: "gpg-dops-agency"
---

# Discovered APIs & Protocols: gpg-dops-agency

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/services` | `200` | REST endpoint |
| `GET` | `/api/reviews` | `200` | REST endpoint |
| `GET` | `/api/services` | `200` | REST endpoint |
| `GET` | `/api/reviews` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/services
```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "attributes": {
            "type": "any"
          }
        }
      }
    },
    "meta": {
      "type": "object",
      "properties": {
        "pagination": {
          "type": "object",
          "properties": {
            "start": {
              "type": "any"
            },
            "limit": {
              "type": "any"
            },
            "total": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `GET` /api/reviews
```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "id": {
          "type": "number"
        },
        "attributes": {
          "type": "object",
          "properties": {
            "title": {
              "type": "any"
            },
            "createdAt": {
              "type": "any"
            },
            "updatedAt": {
              "type": "any"
            },
            "publishedAt": {
              "type": "any"
            },
            "reviews_list": {
              "type": "any"
            }
          }
        }
      }
    },
    "meta": {
      "type": "object",
      "properties": {}
    }
  }
}
```
### `GET` /api/services
```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "attributes": {
            "type": "any"
          }
        }
      }
    },
    "meta": {
      "type": "object",
      "properties": {
        "pagination": {
          "type": "object",
          "properties": {
            "start": {
              "type": "any"
            },
            "limit": {
              "type": "any"
            },
            "total": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `GET` /api/reviews
```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "id": {
          "type": "number"
        },
        "attributes": {
          "type": "object",
          "properties": {
            "title": {
              "type": "any"
            },
            "createdAt": {
              "type": "any"
            },
            "updatedAt": {
              "type": "any"
            },
            "publishedAt": {
              "type": "any"
            },
            "reviews_list": {
              "type": "any"
            }
          }
        }
      }
    },
    "meta": {
      "type": "object",
      "properties": {}
    }
  }
}
```

