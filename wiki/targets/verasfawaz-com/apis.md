---
title: "APIs & Protocols: verasfawaz-com"
date: 2026-11-14
target: "verasfawaz-com"
---

# Discovered APIs & Protocols: verasfawaz-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/_content/release/d998304cc36275d70b0c12350f5a3a244904ea801a80c197c420ed8d774e351f` | `200` | REST endpoint |
| `GET` | `/sleeves/manifest.json` | `200` | REST endpoint |
| `GET` | `/v1/forecast` | `200` | REST endpoint |
| `GET` | `/detail-v71/manifest.json` | `200` | REST endpoint |
| `GET` | `/city-v5/assets/cities/windows.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /_content/release/d998304cc36275d70b0c12350f5a3a244904ea801a80c197c420ed8d774e351f
```json
{
  "type": "object",
  "properties": {
    "protocol": {
      "type": "number"
    },
    "revision": {
      "type": "number"
    },
    "document": {
      "type": "object",
      "properties": {
        "release": {
          "type": "string"
        },
        "revision": {
          "type": "number"
        },
        "films": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "projectFiles": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "settings": {
          "type": "object",
          "properties": {
            "notes": {
              "type": "any"
            },
            "scripts": {
              "type": "any"
            },
            "city": {
              "type": "any"
            },
            "screenplays": {
              "type": "any"
            },
            "records": {
              "type": "any"
            }
          }
        },
        "work": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "content": {
          "type": "object",
          "properties": {
            "schemaVersion": {
              "type": "any"
            },
            "records": {
              "type": "any"
            },
            "projects": {
              "type": "any"
            },
            "entries": {
              "type": "any"
            }
          }
        },
        "projects": {
          "type": "object",
          "properties": {
            "gleam": {
              "type": "any"
            },
            "wewerehere": {
              "type": "any"
            },
            "warm": {
              "type": "any"
            },
            "leeuw": {
              "type": "any"
            },
            "joshuadewit": {
              "type": "any"
            },
            "dejas": {
              "type": "any"
            },
            "europapa": {
              "type": "any"
            },
            "stiekem": {
              "type": "any"
            },
            "noodgeval": {
              "type": "any"
            },
            "oehyeah": {
              "type": "any"
            },
            "lovemyself": {
              "type": "any"
            },
            "aanheteindevandetijd": {
              "type": "any"
            },
            "redons": {
              "type": "any"
            },
            "leugenaar": {
              "type": "any"
            },
            "scandinavianboy": {
              "type": "any"
            },
            "alleeninbed": {
              "type": "any"
            },
            "legokastelen": {
              "type": "any"
            },
            "unbubble": {
              "type": "any"
            },
            "deeeuwigejeugd": {
              "type": "any"
            },
            "cominghome": {
              "type": "any"
            }
          }
        },
        "blogMetadata": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "shared": {
          "type": "object",
          "properties": {
            "gleam": {
              "type": "any"
            }
          }
        },
        "entries": {
          "type": "array",
          "items": "any"
        },
        "relatedProjects": {
          "type": "array",
          "items": "any"
        },
        "demos": {
          "type": "null"
        },
        "seo": {
          "type": "object",
          "properties": {
            "note-0": {
              "type": "any"
            }
          }
        },
        "removed": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "hiddenObjects": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "routes": {
          "type": "object",
          "properties": {
            "/thegleam": {
              "type": "any"
            },
            "/wewerehereonce": {
              "type": "any"
            },
            "/warm": {
              "type": "any"
            },
            "/leeuwpanterwolvin": {
              "type": "any"
            },
            "/joshuadewit": {
              "type": "any"
            },
            "/dejas": {
              "type": "any"
            },
            "/europapa": {
              "type": "any"
            },
            "/stiekem": {
              "type": "any"
            },
            "/noodgeval": {
              "type": "any"
            },
            "/oehyeah": {
              "type": "any"
            },
            "/lovemyself": {
              "type": "any"
            },
            "/aanheteindevandetijd": {
              "type": "any"
            },
            "/redons": {
              "type": "any"
            },
            "/leugenaar": {
              "type": "any"
            },
            "/scandinavianboy": {
              "type": "any"
            },
            "/alleeninbed": {
              "type": "any"
            },
            "/legokastelen": {
              "type": "any"
            },
            "/unbubble": {
              "type": "any"
            },
            "/deeeuwigejeugd": {
              "type": "any"
            },
            "/cominghome": {
              "type": "any"
            }
          }
        }
      }
    },
    "films": {
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
          "path": {
            "type": "any"
          },
          "year": {
            "type": "any"
          },
          "kind": {
            "type": "any"
          },
          "artist": {
            "type": "any"
          },
          "runtime": {
            "type": "any"
          },
          "source": {
            "type": "any"
          },
          "metadata": {
            "type": "any"
          },
          "documents": {
            "type": "any"
          },
          "createdAt": {
            "type": "any"
          },
          "isNew": {
            "type": "any"
          },
          "dvd": {
            "type": "any"
          },
          "studio": {
            "type": "any"
          },
          "wrapURL": {
            "type": "any"
          },
          "spine": {
            "type": "any"
          },
          "documentsEdited": {
            "type": "any"
          }
        }
      }
    },
    "layout": {
      "type": "null"
    },
    "awards": {
      "type": "array",
      "items": "any"
    },
    "routes": {
      "type": "object",
      "properties": {
        "/thegleam": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "panel": {
              "type": "any"
            },
            "title": {
              "type": "any"
            },
            "seoAuthored": {
              "type": "any"
            },
            "template": {
              "type": "any"
            },
            "seo": {
              "type": "any"
            },
            "body": {
              "type": "any"
            },
            "blog": {
              "type": "any"
            },
            "publishedAt": {
              "type": "any"
            }
          }
        },
        "/wewerehereonce": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "panel": {
              "type": "any"
            },
            "title": {
              "type": "any"
            },
            "seoAuthored": {
              "type": "any"
            },
            "template": {
              "type": "any"
            },
            "seo": {
              "type": "any"
            },
            "body": {
              "type": "any"
            },
            "blog": {
              "type": "any"
            },
            "publishedAt": {
              "type": "any"
            }
          }
        },
        "/warm": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "panel": {
              "type": "any"
            },
            "title": {
              "type": "any"
            },
            "seoAuthored": {
              "type": "any"
            },
            "template": {
              "type": "any"
            },
            "seo": {
              "type": "any"
            },
            "body": {
              "type": "any"
            },
            "blog": {
              "type": "any"
            },
            "publishedAt": {
              "type": "any"
            }
          }
        },
        "/leeuwpanterwolvin": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "panel": {
              "type": "any"
            },
            "title": {
              "type": "any"
            },
            "seoAuthored": {
              "type": "any"
            },
            "template": {
              "type": "any"
            },
            "seo": {
              "type": "any"
            },
            "body": {
              "type": "any"
            },
            "blog": {
              "type": "any"
            },
            "publishedAt": {
              "type": "any"
            }
          }
        },
        "/joshuadewit": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "panel": {
              "type": "any"
            },
            "title": {
              "type": "any"
            },
            "seoAuthored": {
              "type": "any"
            },
            "template": {
              "type": "any"
            },
            "seo": {
              "type": "any"
            },
            "body": {
              "type": "any"
            },
            "blog": {
              "type": "any"
            },
            "publishedAt": {
              "type": "any"
            }
          }
        },
        "/dejas": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "panel": {
              "type": "any"
            },
            "title": {
              "type": "any"
            },
            "seoAuthored": {
              "type": "any"
            },
            "template": {
              "type": "any"
            },
            "seo": {
              "type": "any"
            },
            "body": {
              "type": "any"
            },
            "blog": {
              "type": "any"
            },
            "publishedAt": {
              "type": "any"
            }
          }
        },
        "/europapa": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "panel": {
              "type": "any"
            },
            "title": {
              "type": "any"
            },
            "seoAuthored": {
              "type": "any"
            },
            "template": {
              "type": "any"
            },
            "seo": {
              "type": "any"
            },
            "body": {
              "type": "any"
            },
            "blog": {
              "type": "any"
            },
            "publishedAt": {
              "type": "any"
            }
          }
        },
        "/stiekem": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "panel": {
              "type": "any"
            },
            "title": {
              "type": "any"
            },
            "seoAuthored": {
              "type": "any"
            },
            "template": {
              "type": "any"
            },
            "seo": {
              "type": "any"
            },
            "body": {
              "type": "any"
            },
            "blog": {
              "type": "any"
            },
            "publishedAt": {
              "type": "any"
            }
          }
        },
        "/noodgeval": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "panel": {
              "type": "any"
            },
            "title": {
              "type": "any"
            },
            "seoAuthored": {
              "type": "any"
            },
            "template": {
              "type": "any"
            },
            "seo": {
              "type": "any"
            },
            "body": {
              "type": "any"
            },
            "blog": {
              "type": "any"
            },
            "publishedAt": {
              "type": "any"
            }
          }
        },
        "/oehyeah": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "panel": {
              "type": "any"
            },
            "title": {
              "type": "any"
            },
            "seoAuthored": {
              "type": "any"
            },
            "template": {
              "type": "any"
            },
            "seo": {
              "type": "any"
            },
            "body": {
              "type": "any"
            },
            "blog": {
              "type": "any"
            },
            "publishedAt": {
              "type": "any"
            }
          }
        },
        "/lovemyself": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "panel": {
              "type": "any"
            },
            "title": {
              "type": "any"
            },
            "seoAuthored": {
              "type": "any"
            },
            "template": {
              "type": "any"
            },
            "seo": {
              "type": "any"
            },
            "body": {
              "type": "any"
            },
            "blog": {
              "type": "any"
            },
            "publishedAt": {
              "type": "any"
            }
          }
        },
        "/aanheteindevandetijd": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "panel": {
              "type": "any"
            },
            "title": {
              "type": "any"
            },
            "seoAuthored": {
              "type": "any"
            },
            "template": {
              "type": "any"
            },
            "seo": {
              "type": "any"
            },
            "body": {
              "type": "any"
            },
            "blog": {
              "type": "any"
            },
            "publishedAt": {
              "type": "any"
            }
          }
        },
        "/redons": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "panel": {
              "type": "any"
            },
            "title": {
              "type": "any"
            },
            "seoAuthored": {
              "type": "any"
            },
            "template": {
              "type": "any"
            },
            "seo": {
              "type": "any"
            },
            "body": {
              "type": "any"
            },
            "blog": {
              "type": "any"
            },
            "publishedAt": {
              "type": "any"
            }
          }
        },
        "/leugenaar": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "panel": {
              "type": "any"
            },
            "title": {
              "type": "any"
            },
            "seoAuthored": {
              "type": "any"
            },
            "template": {
              "type": "any"
            },
            "seo": {
              "type": "any"
            },
            "body": {
              "type": "any"
            },
            "blog": {
              "type": "any"
            },
            "publishedAt": {
              "type": "any"
            }
          }
        },
        "/scandinavianboy": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "panel": {
              "type": "any"
            },
            "title": {
              "type": "any"
            },
            "seoAuthored": {
              "type": "any"
            },
            "template": {
              "type": "any"
            },
            "seo": {
              "type": "any"
            },
            "body": {
              "type": "any"
            },
            "blog": {
              "type": "any"
            },
            "publishedAt": {
              "type": "any"
            }
          }
        },
        "/alleeninbed": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "panel": {
              "type": "any"
            },
            "title": {
              "type": "any"
            },
            "seoAuthored": {
              "type": "any"
            },
            "template": {
              "type": "any"
            },
            "seo": {
              "type": "any"
            },
            "body": {
              "type": "any"
            },
            "blog": {
              "type": "any"
            },
            "publishedAt": {
              "type": "any"
            }
          }
        },
        "/legokastelen": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "panel": {
              "type": "any"
            },
            "title": {
              "type": "any"
            },
            "seoAuthored": {
              "type": "any"
            },
            "template": {
              "type": "any"
            },
            "seo": {
              "type": "any"
            },
            "body": {
              "type": "any"
            },
            "blog": {
              "type": "any"
            },
            "publishedAt": {
              "type": "any"
            }
          }
        },
        "/unbubble": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "panel": {
              "type": "any"
            },
            "title": {
              "type": "any"
            },
            "seoAuthored": {
              "type": "any"
            },
            "template": {
              "type": "any"
            },
            "seo": {
              "type": "any"
            },
            "body": {
              "type": "any"
            },
            "blog": {
              "type": "any"
            },
            "publishedAt": {
              "type": "any"
            }
          }
        },
        "/deeeuwigejeugd": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "panel": {
              "type": "any"
            },
            "title": {
              "type": "any"
            },
            "seoAuthored": {
              "type": "any"
            },
            "template": {
              "type": "any"
            },
            "seo": {
              "type": "any"
            },
            "body": {
              "type": "any"
            },
            "blog": {
              "type": "any"
            },
            "publishedAt": {
              "type": "any"
            }
          }
        },
        "/cominghome": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "panel": {
              "type": "any"
            },
            "title": {
              "type": "any"
            },
            "seoAuthored": {
              "type": "any"
            },
            "template": {
              "type": "any"
            },
            "seo": {
              "type": "any"
            },
            "body": {
              "type": "any"
            },
            "blog": {
              "type": "any"
            },
            "publishedAt": {
              "type": "any"
            }
          }
        }
      }
    },
    "aliases": {
      "type": "object",
      "properties": {}
    },
    "gone": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "homeSEO": {
      "type": "null"
    },
    "media": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "version": {
      "type": "string"
    }
  }
}
```
### `GET` /sleeves/manifest.json
```json
{
  "type": "object",
  "properties": {
    "revision": {
      "type": "number"
    },
    "sourceRevision": {
      "type": "string"
    },
    "projects": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "kind": {
            "type": "any"
          },
          "file": {
            "type": "any"
          },
          "dimensions_mm": {
            "type": "any"
          },
          "sha256": {
            "type": "any"
          },
          "sourceRevision": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /v1/forecast
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
    "current_units": {
      "type": "object",
      "properties": {
        "time": {
          "type": "string"
        },
        "interval": {
          "type": "string"
        },
        "temperature_2m": {
          "type": "string"
        },
        "weather_code": {
          "type": "string"
        },
        "is_day": {
          "type": "string"
        }
      }
    },
    "current": {
      "type": "object",
      "properties": {
        "time": {
          "type": "number"
        },
        "interval": {
          "type": "number"
        },
        "temperature_2m": {
          "type": "number"
        },
        "weather_code": {
          "type": "number"
        },
        "is_day": {
          "type": "number"
        }
      }
    },
    "daily_units": {
      "type": "object",
      "properties": {
        "time": {
          "type": "string"
        },
        "sunrise": {
          "type": "string"
        },
        "sunset": {
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
        "sunrise": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "sunset": {
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
### `GET` /detail-v71/manifest.json
```json
{
  "type": "object",
  "properties": {
    "version": {
      "type": "number"
    },
    "bytes": {
      "type": "number"
    },
    "encodedBytes": {
      "type": "number"
    },
    "records": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "key": {
            "type": "any"
          },
          "name": {
            "type": "any"
          },
          "original": {
            "type": "any"
          },
          "levels": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /city-v5/assets/cities/windows.json
```json
{
  "type": "object",
  "properties": {
    "amsterdam": {
      "type": "array",
      "items": {
        "type": "array",
        "items": {
          "type": "any"
        }
      }
    },
    "london": {
      "type": "array",
      "items": {
        "type": "array",
        "items": {
          "type": "any"
        }
      }
    },
    "tokyo": {
      "type": "array",
      "items": {
        "type": "array",
        "items": {
          "type": "any"
        }
      }
    },
    "los-angeles": {
      "type": "array",
      "items": {
        "type": "array",
        "items": {
          "type": "any"
        }
      }
    }
  }
}
```

