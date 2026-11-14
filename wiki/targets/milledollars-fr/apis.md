---
title: "APIs & Protocols: milledollars-fr"
date: 2026-11-14
target: "[[overview|milledollars-fr]]"
---

# Discovered APIs & Protocols: milledollars-fr

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/v2` | `200` | REST endpoint |
| `GET` | `/api/v2/documents/search` | `200` | REST endpoint |
| `GET` | `/api/v2/documents/search` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/v2
```json
{
  "type": "object",
  "properties": {
    "refs": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "ref": {
            "type": "any"
          },
          "label": {
            "type": "any"
          },
          "isMasterRef": {
            "type": "any"
          }
        }
      }
    },
    "bookmarks": {
      "type": "object",
      "properties": {}
    },
    "experiments": {
      "type": "object",
      "properties": {
        "draft": {
          "type": "array",
          "items": "any"
        },
        "running": {
          "type": "array",
          "items": "any"
        }
      }
    },
    "types": {
      "type": "object",
      "properties": {
        "about": {
          "type": "string"
        },
        "contact": {
          "type": "string"
        },
        "home": {
          "type": "string"
        },
        "navigation": {
          "type": "string"
        },
        "project": {
          "type": "string"
        },
        "settings": {
          "type": "string"
        },
        "works": {
          "type": "string"
        }
      }
    },
    "languages": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "name": {
            "type": "any"
          },
          "is_master": {
            "type": "any"
          }
        }
      }
    },
    "forms": {
      "type": "object",
      "properties": {
        "everything": {
          "type": "object",
          "properties": {
            "method": {
              "type": "any"
            },
            "enctype": {
              "type": "any"
            },
            "action": {
              "type": "any"
            },
            "fields": {
              "type": "any"
            }
          }
        },
        "tags": {
          "type": "object",
          "properties": {
            "method": {
              "type": "any"
            },
            "enctype": {
              "type": "any"
            },
            "action": {
              "type": "any"
            },
            "fields": {
              "type": "any"
            }
          }
        }
      }
    },
    "oauth_initiate": {
      "type": "string"
    },
    "oauth_token": {
      "type": "string"
    },
    "tags": {
      "type": "array",
      "items": "any"
    },
    "license": {
      "type": "string"
    },
    "version": {
      "type": "string"
    }
  }
}
```
### `GET` /api/v2/documents/search
```json
{
  "type": "object",
  "properties": {
    "page": {
      "type": "number"
    },
    "results_per_page": {
      "type": "number"
    },
    "results_size": {
      "type": "number"
    },
    "total_results_size": {
      "type": "number"
    },
    "total_pages": {
      "type": "number"
    },
    "next_page": {
      "type": "null"
    },
    "prev_page": {
      "type": "null"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "uid": {
            "type": "any"
          },
          "url": {
            "type": "any"
          },
          "type": {
            "type": "any"
          },
          "href": {
            "type": "any"
          },
          "tags": {
            "type": "any"
          },
          "first_publication_date": {
            "type": "any"
          },
          "last_publication_date": {
            "type": "any"
          },
          "slugs": {
            "type": "any"
          },
          "linked_documents": {
            "type": "any"
          },
          "lang": {
            "type": "any"
          },
          "alternate_languages": {
            "type": "any"
          },
          "data": {
            "type": "any"
          }
        }
      }
    },
    "version": {
      "type": "string"
    },
    "license": {
      "type": "string"
    }
  }
}
```
### `GET` /api/v2/documents/search
```json
{
  "type": "object",
  "properties": {
    "page": {
      "type": "number"
    },
    "results_per_page": {
      "type": "number"
    },
    "results_size": {
      "type": "number"
    },
    "total_results_size": {
      "type": "number"
    },
    "total_pages": {
      "type": "number"
    },
    "next_page": {
      "type": "null"
    },
    "prev_page": {
      "type": "null"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "uid": {
            "type": "any"
          },
          "url": {
            "type": "any"
          },
          "type": {
            "type": "any"
          },
          "href": {
            "type": "any"
          },
          "tags": {
            "type": "any"
          },
          "first_publication_date": {
            "type": "any"
          },
          "last_publication_date": {
            "type": "any"
          },
          "slugs": {
            "type": "any"
          },
          "linked_documents": {
            "type": "any"
          },
          "lang": {
            "type": "any"
          },
          "alternate_languages": {
            "type": "any"
          },
          "data": {
            "type": "any"
          }
        }
      }
    },
    "version": {
      "type": "string"
    },
    "license": {
      "type": "string"
    }
  }
}
```

