---
title: "APIs & Protocols: recurziv-com"
date: 2026-11-14
target: "[[overview|recurziv-com]]"
---

# Discovered APIs & Protocols: recurziv-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/wp-content/themes/recurziv/cache/suggestions.json` | `200` | REST endpoint |
| `POST` | `/wp-json/recurziv/v1/pulse` | `204` | REST endpoint |
| `POST` | `/wp-json/recurziv/v1/pulse` | `204` | REST endpoint |
| `GET` | `/wp-content/themes/recurziv/assets/data/cmudict.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /wp-content/themes/recurziv/cache/suggestions.json
```json
{
  "type": "object",
  "properties": {
    "updated_at": {
      "type": "string"
    },
    "default": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "by_industry": {
      "type": "object",
      "properties": {
        "retail": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "fashion": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "food-cpg": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "qsr": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "fintech": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "banking": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "real-estate": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "tech": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "tech-services": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "tech-saas": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "saas": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "consulting": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "media": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "biotech": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "pharma": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "telecom": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "automotive": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "logistics": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "tourism-hospitality": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "architecture": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    },
    "by_persona": {
      "type": "object",
      "properties": {
        "corporate-prospect": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "corporate": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "founder-or-personal": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "individual": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "privacy-conscious": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    },
    "questions": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  }
}
```
### `GET` /wp-content/themes/recurziv/assets/data/cmudict.json
```json
{
  "type": "object",
  "properties": {
    "A": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "A'S": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "A.": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "A.'S": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "A.D.": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "A.M.": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "A.S": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "AAA": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "AABERG": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "AACHEN": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "AACHENER": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "AAKER": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "AALBORG": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "AALBURG": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "AALEN": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "AALIYAH": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "AALSETH": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "AALSMEER": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "AALTO": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "AAMODT": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  }
}
```

