---
title: "APIs & Protocols: palaceskateboards-com"
date: 2026-11-14
target: "[[overview|palaceskateboards-com]]"
---

# Discovered APIs & Protocols: palaceskateboards-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/__manifest` | `200` | REST endpoint |
| `GET` | `/__manifest` | `200` | REST endpoint |
| `POST` | `/api/unstable/graphql.json` | `200` | GraphQL: `AnonymousQuery` |
| `POST` | `/__shopify/api/collect` | `204` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /__manifest
```json
{
  "type": "object",
  "properties": {
    "root": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "path": {
          "type": "string"
        },
        "hasAction": {
          "type": "boolean"
        },
        "hasLoader": {
          "type": "boolean"
        },
        "hasClientAction": {
          "type": "boolean"
        },
        "hasClientLoader": {
          "type": "boolean"
        },
        "hasClientMiddleware": {
          "type": "boolean"
        },
        "hasDefaultExport": {
          "type": "boolean"
        },
        "hasErrorBoundary": {
          "type": "boolean"
        },
        "module": {
          "type": "string"
        },
        "imports": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "css": {
          "type": "array",
          "items": "any"
        }
      }
    },
    "routes/($locale)._index": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "parentId": {
          "type": "string"
        },
        "path": {
          "type": "string"
        },
        "index": {
          "type": "boolean"
        },
        "hasAction": {
          "type": "boolean"
        },
        "hasLoader": {
          "type": "boolean"
        },
        "hasClientAction": {
          "type": "boolean"
        },
        "hasClientLoader": {
          "type": "boolean"
        },
        "hasClientMiddleware": {
          "type": "boolean"
        },
        "hasDefaultExport": {
          "type": "boolean"
        },
        "hasErrorBoundary": {
          "type": "boolean"
        },
        "module": {
          "type": "string"
        },
        "imports": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "css": {
          "type": "array",
          "items": "any"
        }
      }
    },
    "routes/($locale).advice._index": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "parentId": {
          "type": "string"
        },
        "path": {
          "type": "string"
        },
        "index": {
          "type": "boolean"
        },
        "hasAction": {
          "type": "boolean"
        },
        "hasLoader": {
          "type": "boolean"
        },
        "hasClientAction": {
          "type": "boolean"
        },
        "hasClientLoader": {
          "type": "boolean"
        },
        "hasClientMiddleware": {
          "type": "boolean"
        },
        "hasDefaultExport": {
          "type": "boolean"
        },
        "hasErrorBoundary": {
          "type": "boolean"
        },
        "module": {
          "type": "string"
        },
        "imports": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "css": {
          "type": "array",
          "items": "any"
        }
      }
    },
    "routes/api.mailing-list-signup": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "parentId": {
          "type": "string"
        },
        "path": {
          "type": "string"
        },
        "hasAction": {
          "type": "boolean"
        },
        "hasLoader": {
          "type": "boolean"
        },
        "hasClientAction": {
          "type": "boolean"
        },
        "hasClientLoader": {
          "type": "boolean"
        },
        "hasClientMiddleware": {
          "type": "boolean"
        },
        "hasDefaultExport": {
          "type": "boolean"
        },
        "hasErrorBoundary": {
          "type": "boolean"
        },
        "module": {
          "type": "string"
        },
        "imports": {
          "type": "array",
          "items": "any"
        },
        "css": {
          "type": "array",
          "items": "any"
        }
      }
    },
    "routes/($locale).boring._index": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "parentId": {
          "type": "string"
        },
        "path": {
          "type": "string"
        },
        "index": {
          "type": "boolean"
        },
        "hasAction": {
          "type": "boolean"
        },
        "hasLoader": {
          "type": "boolean"
        },
        "hasClientAction": {
          "type": "boolean"
        },
        "hasClientLoader": {
          "type": "boolean"
        },
        "hasClientMiddleware": {
          "type": "boolean"
        },
        "hasDefaultExport": {
          "type": "boolean"
        },
        "hasErrorBoundary": {
          "type": "boolean"
        },
        "module": {
          "type": "string"
        },
        "imports": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "css": {
          "type": "array",
          "items": "any"
        }
      }
    },
    "routes/($locale).boring.$region": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "parentId": {
          "type": "string"
        },
        "path": {
          "type": "string"
        },
        "hasAction": {
          "type": "boolean"
        },
        "hasLoader": {
          "type": "boolean"
        },
        "hasClientAction": {
          "type": "boolean"
        },
        "hasClientLoader": {
          "type": "boolean"
        },
        "hasClientMiddleware": {
          "type": "boolean"
        },
        "hasDefaultExport": {
          "type": "boolean"
        },
        "hasErrorBoundary": {
          "type": "boolean"
        },
        "module": {
          "type": "string"
        },
        "imports": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "css": {
          "type": "array",
          "items": "any"
        }
      }
    },
    "routes/($locale).boring.$region._index": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "parentId": {
          "type": "string"
        },
        "index": {
          "type": "boolean"
        },
        "hasAction": {
          "type": "boolean"
        },
        "hasLoader": {
          "type": "boolean"
        },
        "hasClientAction": {
          "type": "boolean"
        },
        "hasClientLoader": {
          "type": "boolean"
        },
        "hasClientMiddleware": {
          "type": "boolean"
        },
        "hasDefaultExport": {
          "type": "boolean"
        },
        "hasErrorBoundary": {
          "type": "boolean"
        },
        "module": {
          "type": "string"
        },
        "imports": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "css": {
          "type": "array",
          "items": "any"
        }
      }
    },
    "routes/($locale).boring.$region.$slug": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "parentId": {
          "type": "string"
        },
        "path": {
          "type": "string"
        },
        "hasAction": {
          "type": "boolean"
        },
        "hasLoader": {
          "type": "boolean"
        },
        "hasClientAction": {
          "type": "boolean"
        },
        "hasClientLoader": {
          "type": "boolean"
        },
        "hasClientMiddleware": {
          "type": "boolean"
        },
        "hasDefaultExport": {
          "type": "boolean"
        },
        "hasErrorBoundary": {
          "type": "boolean"
        },
        "module": {
          "type": "string"
        },
        "imports": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "css": {
          "type": "array",
          "items": "any"
        }
      }
    },
    "routes/($locale).cart": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "parentId": {
          "type": "string"
        },
        "path": {
          "type": "string"
        },
        "hasAction": {
          "type": "boolean"
        },
        "hasLoader": {
          "type": "boolean"
        },
        "hasClientAction": {
          "type": "boolean"
        },
        "hasClientLoader": {
          "type": "boolean"
        },
        "hasClientMiddleware": {
          "type": "boolean"
        },
        "hasDefaultExport": {
          "type": "boolean"
        },
        "hasErrorBoundary": {
          "type": "boolean"
        },
        "module": {
          "type": "string"
        },
        "imports": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "css": {
          "type": "array",
          "items": "any"
        }
      }
    },
    "routes/($locale).collections._index": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "parentId": {
          "type": "string"
        },
        "path": {
          "type": "string"
        },
        "index": {
          "type": "boolean"
        },
        "hasAction": {
          "type": "boolean"
        },
        "hasLoader": {
          "type": "boolean"
        },
        "hasClientAction": {
          "type": "boolean"
        },
        "hasClientLoader": {
          "type": "boolean"
        },
        "hasClientMiddleware": {
          "type": "boolean"
        },
        "hasDefaultExport": {
          "type": "boolean"
        },
        "hasErrorBoundary": {
          "type": "boolean"
        },
        "module": {
          "type": "string"
        },
        "imports": {
          "type": "array",
          "items": "any"
        },
        "css": {
          "type": "array",
          "items": "any"
        }
      }
    },
    "routes/($locale).collections.$handle": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "parentId": {
          "type": "string"
        },
        "path": {
          "type": "string"
        },
        "hasAction": {
          "type": "boolean"
        },
        "hasLoader": {
          "type": "boolean"
        },
        "hasClientAction": {
          "type": "boolean"
        },
        "hasClientLoader": {
          "type": "boolean"
        },
        "hasClientMiddleware": {
          "type": "boolean"
        },
        "hasDefaultExport": {
          "type": "boolean"
        },
        "hasErrorBoundary": {
          "type": "boolean"
        },
        "module": {
          "type": "string"
        },
        "imports": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "css": {
          "type": "array",
          "items": "any"
        }
      }
    },
    "routes/($locale).shops._index": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "parentId": {
          "type": "string"
        },
        "path": {
          "type": "string"
        },
        "index": {
          "type": "boolean"
        },
        "hasAction": {
          "type": "boolean"
        },
        "hasLoader": {
          "type": "boolean"
        },
        "hasClientAction": {
          "type": "boolean"
        },
        "hasClientLoader": {
          "type": "boolean"
        },
        "hasClientMiddleware": {
          "type": "boolean"
        },
        "hasDefaultExport": {
          "type": "boolean"
        },
        "hasErrorBoundary": {
          "type": "boolean"
        },
        "module": {
          "type": "string"
        },
        "imports": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "css": {
          "type": "array",
          "items": "any"
        }
      }
    },
    "routes/($locale).shops.$slug": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "parentId": {
          "type": "string"
        },
        "path": {
          "type": "string"
        },
        "hasAction": {
          "type": "boolean"
        },
        "hasLoader": {
          "type": "boolean"
        },
        "hasClientAction": {
          "type": "boolean"
        },
        "hasClientLoader": {
          "type": "boolean"
        },
        "hasClientMiddleware": {
          "type": "boolean"
        },
        "hasDefaultExport": {
          "type": "boolean"
        },
        "hasErrorBoundary": {
          "type": "boolean"
        },
        "module": {
          "type": "string"
        },
        "imports": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "css": {
          "type": "array",
          "items": "any"
        }
      }
    }
  }
}
```
### `GET` /__manifest
```json
{
  "type": "object",
  "properties": {
    "root": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "path": {
          "type": "string"
        },
        "hasAction": {
          "type": "boolean"
        },
        "hasLoader": {
          "type": "boolean"
        },
        "hasClientAction": {
          "type": "boolean"
        },
        "hasClientLoader": {
          "type": "boolean"
        },
        "hasClientMiddleware": {
          "type": "boolean"
        },
        "hasDefaultExport": {
          "type": "boolean"
        },
        "hasErrorBoundary": {
          "type": "boolean"
        },
        "module": {
          "type": "string"
        },
        "imports": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "css": {
          "type": "array",
          "items": "any"
        }
      }
    },
    "routes/($locale).advice._index": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "parentId": {
          "type": "string"
        },
        "path": {
          "type": "string"
        },
        "index": {
          "type": "boolean"
        },
        "hasAction": {
          "type": "boolean"
        },
        "hasLoader": {
          "type": "boolean"
        },
        "hasClientAction": {
          "type": "boolean"
        },
        "hasClientLoader": {
          "type": "boolean"
        },
        "hasClientMiddleware": {
          "type": "boolean"
        },
        "hasDefaultExport": {
          "type": "boolean"
        },
        "hasErrorBoundary": {
          "type": "boolean"
        },
        "module": {
          "type": "string"
        },
        "imports": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "css": {
          "type": "array",
          "items": "any"
        }
      }
    },
    "routes/($locale).advice.$slug": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "parentId": {
          "type": "string"
        },
        "path": {
          "type": "string"
        },
        "hasAction": {
          "type": "boolean"
        },
        "hasLoader": {
          "type": "boolean"
        },
        "hasClientAction": {
          "type": "boolean"
        },
        "hasClientLoader": {
          "type": "boolean"
        },
        "hasClientMiddleware": {
          "type": "boolean"
        },
        "hasDefaultExport": {
          "type": "boolean"
        },
        "hasErrorBoundary": {
          "type": "boolean"
        },
        "module": {
          "type": "string"
        },
        "imports": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "css": {
          "type": "array",
          "items": "any"
        }
      }
    },
    "routes/($locale).ranges._index": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "parentId": {
          "type": "string"
        },
        "path": {
          "type": "string"
        },
        "index": {
          "type": "boolean"
        },
        "hasAction": {
          "type": "boolean"
        },
        "hasLoader": {
          "type": "boolean"
        },
        "hasClientAction": {
          "type": "boolean"
        },
        "hasClientLoader": {
          "type": "boolean"
        },
        "hasClientMiddleware": {
          "type": "boolean"
        },
        "hasDefaultExport": {
          "type": "boolean"
        },
        "hasErrorBoundary": {
          "type": "boolean"
        },
        "module": {
          "type": "string"
        },
        "imports": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "css": {
          "type": "array",
          "items": "any"
        }
      }
    },
    "routes/($locale).ranges.$slug": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "parentId": {
          "type": "string"
        },
        "path": {
          "type": "string"
        },
        "hasAction": {
          "type": "boolean"
        },
        "hasLoader": {
          "type": "boolean"
        },
        "hasClientAction": {
          "type": "boolean"
        },
        "hasClientLoader": {
          "type": "boolean"
        },
        "hasClientMiddleware": {
          "type": "boolean"
        },
        "hasDefaultExport": {
          "type": "boolean"
        },
        "hasErrorBoundary": {
          "type": "boolean"
        },
        "module": {
          "type": "string"
        },
        "imports": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "css": {
          "type": "array",
          "items": "any"
        }
      }
    }
  }
}
```
### `POST` /api/unstable/graphql.json
```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "consentManagement": {
          "type": "object",
          "properties": {
            "cookies": {
              "type": "any"
            },
            "customerAccountUrl": {
              "type": "any"
            }
          }
        }
      }
    },
    "extensions": {
      "type": "object",
      "properties": {
        "cost": {
          "type": "object",
          "properties": {
            "requestedQueryCost": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```

