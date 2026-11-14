---
title: "APIs & Protocols: www-alpineguides-co-nz"
date: 2026-11-14
target: "[[overview|www-alpineguides-co-nz]]"
---

# Discovered APIs & Protocols: www-alpineguides-co-nz

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/v3/` | `200` | REST endpoint |
| `GET` | `/maps/api/js` | `200` | REST endpoint |
| `GET` | `/maps-api-v3/api/js/66/13d/geometry.js` | `200` | REST endpoint |
| `GET` | `/maps-api-v3/api/js/66/13d/search.js` | `200` | REST endpoint |
| `GET` | `/maps-api-v3/api/js/66/13d/main.js` | `200` | REST endpoint |
| `GET` | `/repos/dani-mello/agl-webflow-scripts/commits/main` | `200` | REST endpoint |
| `GET` | `/v3/m-outer-0edadf75b42c6ef7240c043f3272f3f9.html` | `200` | REST endpoint |
| `GET` | `/v3/fingerprinted/js/m-outer-df5ee3b49f88025f22168cdfc5823764.js` | `200` | REST endpoint |
| `GET` | `/maps/api/mapsjs/gen_204` | `200` | REST endpoint |
| `GET` | `/maps-api-v3/api/js/66/13d/common.js` | `200` | REST endpoint |
| `GET` | `/maps-api-v3/api/js/66/13d/util.js` | `200` | REST endpoint |
| `GET` | `/maps-api-v3/api/js/66/13d/map.js` | `200` | REST endpoint |
| `GET` | `/maps-api-v3/api/js/66/13d/controls.js` | `200` | REST endpoint |
| `GET` | `/maps-api-v3/api/js/66/13d/places_impl.js` | `200` | REST endpoint |
| `GET` | `/maps-api-v3/api/js/66/13d/places.js` | `200` | REST endpoint |
| `GET` | `/maps/api/js/StaticMapService.GetMapImage` | `200` | REST endpoint |
| `GET` | `/maps-api-v3/api/js/66/13d/onion.js` | `200` | REST endpoint |
| `GET` | `/maps-api-v3/api/js/66/13d/search_impl.js` | `200` | REST endpoint |
| `POST` | `/6` | `200` | REST endpoint |
| `GET` | `/pagead/id` | `200` | REST endpoint |
| `POST` | `/youtubei/v1/log_event` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /repos/dani-mello/agl-webflow-scripts/commits/main
```json
{
  "type": "object",
  "properties": {
    "sha": {
      "type": "string"
    },
    "node_id": {
      "type": "string"
    },
    "commit": {
      "type": "object",
      "properties": {
        "author": {
          "type": "object",
          "properties": {
            "name": {
              "type": "any"
            },
            "email": {
              "type": "any"
            },
            "date": {
              "type": "any"
            }
          }
        },
        "committer": {
          "type": "object",
          "properties": {
            "name": {
              "type": "any"
            },
            "email": {
              "type": "any"
            },
            "date": {
              "type": "any"
            }
          }
        },
        "message": {
          "type": "string"
        },
        "tree": {
          "type": "object",
          "properties": {
            "sha": {
              "type": "any"
            },
            "url": {
              "type": "any"
            }
          }
        },
        "url": {
          "type": "string"
        },
        "comment_count": {
          "type": "number"
        },
        "verification": {
          "type": "object",
          "properties": {
            "verified": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "signature": {
              "type": "any"
            },
            "payload": {
              "type": "any"
            },
            "verified_at": {
              "type": "any"
            }
          }
        }
      }
    },
    "url": {
      "type": "string"
    },
    "html_url": {
      "type": "string"
    },
    "comments_url": {
      "type": "string"
    },
    "author": {
      "type": "object",
      "properties": {
        "login": {
          "type": "string"
        },
        "id": {
          "type": "number"
        },
        "node_id": {
          "type": "string"
        },
        "avatar_url": {
          "type": "string"
        },
        "gravatar_id": {
          "type": "string"
        },
        "url": {
          "type": "string"
        },
        "html_url": {
          "type": "string"
        },
        "followers_url": {
          "type": "string"
        },
        "following_url": {
          "type": "string"
        },
        "gists_url": {
          "type": "string"
        },
        "starred_url": {
          "type": "string"
        },
        "subscriptions_url": {
          "type": "string"
        },
        "organizations_url": {
          "type": "string"
        },
        "repos_url": {
          "type": "string"
        },
        "events_url": {
          "type": "string"
        },
        "received_events_url": {
          "type": "string"
        },
        "type": {
          "type": "string"
        },
        "user_view_type": {
          "type": "string"
        },
        "site_admin": {
          "type": "boolean"
        }
      }
    },
    "committer": {
      "type": "object",
      "properties": {
        "login": {
          "type": "string"
        },
        "id": {
          "type": "number"
        },
        "node_id": {
          "type": "string"
        },
        "avatar_url": {
          "type": "string"
        },
        "gravatar_id": {
          "type": "string"
        },
        "url": {
          "type": "string"
        },
        "html_url": {
          "type": "string"
        },
        "followers_url": {
          "type": "string"
        },
        "following_url": {
          "type": "string"
        },
        "gists_url": {
          "type": "string"
        },
        "starred_url": {
          "type": "string"
        },
        "subscriptions_url": {
          "type": "string"
        },
        "organizations_url": {
          "type": "string"
        },
        "repos_url": {
          "type": "string"
        },
        "events_url": {
          "type": "string"
        },
        "received_events_url": {
          "type": "string"
        },
        "type": {
          "type": "string"
        },
        "user_view_type": {
          "type": "string"
        },
        "site_admin": {
          "type": "boolean"
        }
      }
    },
    "parents": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "sha": {
            "type": "any"
          },
          "url": {
            "type": "any"
          },
          "html_url": {
            "type": "any"
          }
        }
      }
    },
    "stats": {
      "type": "object",
      "properties": {
        "total": {
          "type": "number"
        },
        "additions": {
          "type": "number"
        },
        "deletions": {
          "type": "number"
        }
      }
    },
    "files": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "sha": {
            "type": "any"
          },
          "filename": {
            "type": "any"
          },
          "status": {
            "type": "any"
          },
          "additions": {
            "type": "any"
          },
          "deletions": {
            "type": "any"
          },
          "changes": {
            "type": "any"
          },
          "blob_url": {
            "type": "any"
          },
          "raw_url": {
            "type": "any"
          },
          "contents_url": {
            "type": "any"
          },
          "patch": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /maps/api/mapsjs/gen_204
```json
{
  "type": "object",
  "properties": {}
}
```

