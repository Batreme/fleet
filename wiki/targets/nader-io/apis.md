---
title: "APIs & Protocols: nader-io"
date: 2026-11-14
target: "[[overview|nader-io]]"
---

# Discovered APIs & Protocols: nader-io

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/s` | `200` | REST endpoint |
| `GET` | `/api/p` | `200` | REST endpoint |
| `POST` | `/api/e` | `202` | REST endpoint |
| `POST` | `/api/h` | `202` | REST endpoint |
| `GET` | `/webmcp/manifest.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /webmcp/manifest.json
```json
{
  "type": "object",
  "properties": {
    "webmcpVersion": {
      "type": "string"
    },
    "generatedAt": {
      "type": "string"
    },
    "site": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "url": {
          "type": "string"
        },
        "description": {
          "type": "string"
        },
        "llmsTxt": {
          "type": "string"
        }
      }
    },
    "links": {
      "type": "object",
      "properties": {
        "booking": {
          "type": "string"
        },
        "bookingDirect": {
          "type": "string"
        },
        "linkedin": {
          "type": "string"
        },
        "x": {
          "type": "string"
        },
        "github": {
          "type": "string"
        },
        "shop": {
          "type": "string"
        }
      }
    },
    "pages": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "url": {
            "type": "any"
          },
          "title": {
            "type": "any"
          },
          "description": {
            "type": "any"
          }
        }
      }
    },
    "posts": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "slug": {
            "type": "any"
          },
          "url": {
            "type": "any"
          },
          "title": {
            "type": "any"
          },
          "description": {
            "type": "any"
          },
          "date": {
            "type": "any"
          },
          "excerpt": {
            "type": "any"
          },
          "wordCount": {
            "type": "any"
          },
          "contentUrl": {
            "type": "any"
          }
        }
      }
    },
    "projects": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "url": {
            "type": "any"
          },
          "title": {
            "type": "any"
          },
          "description": {
            "type": "any"
          },
          "tag": {
            "type": "any"
          },
          "external": {
            "type": "any"
          }
        }
      }
    },
    "art": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "url": {
            "type": "any"
          },
          "title": {
            "type": "any"
          },
          "description": {
            "type": "any"
          },
          "external": {
            "type": "any"
          }
        }
      }
    },
    "datasets": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "title": {
            "type": "any"
          },
          "description": {
            "type": "any"
          },
          "pageUrl": {
            "type": "any"
          },
          "dataUrl": {
            "type": "any"
          },
          "docsUrl": {
            "type": "any"
          },
          "tools": {
            "type": "any"
          },
          "recordCount": {
            "type": "any"
          },
          "updated": {
            "type": "any"
          }
        }
      }
    }
  }
}
```

