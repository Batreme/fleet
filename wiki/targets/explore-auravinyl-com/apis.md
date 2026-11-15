---
title: "APIs & Protocols: explore-auravinyl-com"
date: 2026-11-14
target: "explore-auravinyl-com"
---

# Discovered APIs & Protocols: explore-auravinyl-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/visit` | `200` | REST endpoint |
| `POST` | `/analytics/update` | `200` | REST endpoint |
| `POST` | `/log` | `200` | REST endpoint |
| `POST` | `/log` | `200` | REST endpoint |
| `GET` | `/shaderCache/lookup/aura_sampled-1_hjwnbw1c1zevq13a` | `200` | REST endpoint |
| `GET` | `/shaderCache/lookup/aura_sampled-1_1wsg9m1l1t0c87gt` | `200` | REST endpoint |
| `GET` | `/shaderCache/lookup/aura_sampled-1_1usaqh5ymjy8p3gb` | `200` | REST endpoint |
| `GET` | `/shaderCache/lookup/aura_sampled-1_fwadymttvvau6c9` | `200` | REST endpoint |
| `GET` | `/shaderCache/lookup/aura_sampled-1_no5c63nbb0y5eox` | `200` | REST endpoint |
| `GET` | `/shaderCache/lookup/aura_sampled-1_1xdkptl1jd6v9j2bj` | `200` | REST endpoint |
| `GET` | `/shaderCache/lookup/aura_sampled-1_4cqan51biglx15iw` | `200` | REST endpoint |
| `GET` | `/shaderCache/lookup/aura_sampled-1_1knas4k1jr8ws82my` | `200` | REST endpoint |
| `GET` | `/shaderCache/lookup/aura_sampled-1_ic4hqiv5s4ksdvk` | `200` | REST endpoint |
| `GET` | `/shaderCache/lookup/aura_sampled-1_1rwpd5xb9x40j51g` | `200` | REST endpoint |
| `GET` | `/shaderCache/lookup/aura_sampled-1_opkuf01pjqdoo1iq` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /analytics/update
```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean"
    }
  }
}
```
### `GET` /shaderCache/lookup/aura_sampled-1_hjwnbw1c1zevq13a
```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean"
    },
    "filename": {
      "type": "string"
    },
    "content": {
      "type": "object",
      "properties": {
        "target": {
          "type": "string"
        },
        "vs": {
          "type": "string"
        },
        "fs": {
          "type": "string"
        },
        "reflection": {
          "type": "object",
          "properties": {
            "bindings": {
              "type": "any"
            },
            "inputs": {
              "type": "any"
            },
            "outputs": {
              "type": "any"
            },
            "local": {
              "type": "any"
            },
            "textures": {
              "type": "any"
            }
          }
        }
      }
    },
    "originalSize": {
      "type": "number"
    },
    "compressedSize": {
      "type": "number"
    },
    "lastModified": {
      "type": "string"
    }
  }
}
```
### `GET` /shaderCache/lookup/aura_sampled-1_1wsg9m1l1t0c87gt
```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean"
    },
    "filename": {
      "type": "string"
    },
    "content": {
      "type": "object",
      "properties": {
        "target": {
          "type": "string"
        },
        "vs": {
          "type": "string"
        },
        "fs": {
          "type": "string"
        },
        "reflection": {
          "type": "object",
          "properties": {
            "bindings": {
              "type": "any"
            },
            "inputs": {
              "type": "any"
            },
            "outputs": {
              "type": "any"
            },
            "local": {
              "type": "any"
            },
            "textures": {
              "type": "any"
            }
          }
        }
      }
    },
    "originalSize": {
      "type": "number"
    },
    "compressedSize": {
      "type": "number"
    },
    "lastModified": {
      "type": "string"
    }
  }
}
```
### `GET` /shaderCache/lookup/aura_sampled-1_1usaqh5ymjy8p3gb
```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean"
    },
    "filename": {
      "type": "string"
    },
    "content": {
      "type": "object",
      "properties": {
        "target": {
          "type": "string"
        },
        "vs": {
          "type": "string"
        },
        "fs": {
          "type": "string"
        },
        "reflection": {
          "type": "object",
          "properties": {
            "bindings": {
              "type": "any"
            },
            "inputs": {
              "type": "any"
            },
            "outputs": {
              "type": "any"
            },
            "local": {
              "type": "any"
            },
            "textures": {
              "type": "any"
            }
          }
        }
      }
    },
    "originalSize": {
      "type": "number"
    },
    "compressedSize": {
      "type": "number"
    },
    "lastModified": {
      "type": "string"
    }
  }
}
```
### `GET` /shaderCache/lookup/aura_sampled-1_fwadymttvvau6c9
```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean"
    },
    "filename": {
      "type": "string"
    },
    "content": {
      "type": "object",
      "properties": {
        "target": {
          "type": "string"
        },
        "vs": {
          "type": "string"
        },
        "fs": {
          "type": "string"
        },
        "reflection": {
          "type": "object",
          "properties": {
            "bindings": {
              "type": "any"
            },
            "inputs": {
              "type": "any"
            },
            "outputs": {
              "type": "any"
            },
            "local": {
              "type": "any"
            },
            "textures": {
              "type": "any"
            }
          }
        }
      }
    },
    "originalSize": {
      "type": "number"
    },
    "compressedSize": {
      "type": "number"
    },
    "lastModified": {
      "type": "string"
    }
  }
}
```
### `GET` /shaderCache/lookup/aura_sampled-1_no5c63nbb0y5eox
```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean"
    },
    "filename": {
      "type": "string"
    },
    "content": {
      "type": "object",
      "properties": {
        "target": {
          "type": "string"
        },
        "vs": {
          "type": "string"
        },
        "fs": {
          "type": "string"
        },
        "reflection": {
          "type": "object",
          "properties": {
            "bindings": {
              "type": "any"
            },
            "inputs": {
              "type": "any"
            },
            "outputs": {
              "type": "any"
            },
            "local": {
              "type": "any"
            },
            "textures": {
              "type": "any"
            }
          }
        }
      }
    },
    "originalSize": {
      "type": "number"
    },
    "compressedSize": {
      "type": "number"
    },
    "lastModified": {
      "type": "string"
    }
  }
}
```
### `GET` /shaderCache/lookup/aura_sampled-1_1xdkptl1jd6v9j2bj
```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean"
    },
    "filename": {
      "type": "string"
    },
    "content": {
      "type": "object",
      "properties": {
        "target": {
          "type": "string"
        },
        "vs": {
          "type": "string"
        },
        "fs": {
          "type": "string"
        },
        "reflection": {
          "type": "object",
          "properties": {
            "bindings": {
              "type": "any"
            },
            "inputs": {
              "type": "any"
            },
            "outputs": {
              "type": "any"
            },
            "local": {
              "type": "any"
            },
            "textures": {
              "type": "any"
            }
          }
        }
      }
    },
    "originalSize": {
      "type": "number"
    },
    "compressedSize": {
      "type": "number"
    },
    "lastModified": {
      "type": "string"
    }
  }
}
```

