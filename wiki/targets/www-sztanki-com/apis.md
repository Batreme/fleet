---
title: "APIs & Protocols: www-sztanki-com"
date: 2026-11-14
target: "[[overview|www-sztanki-com]]"
---

# Discovered APIs & Protocols: www-sztanki-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/assets/excon-bold.json` | `200` | REST endpoint |
| `GET` | `/assets/excon-regular.json` | `200` | REST endpoint |
| `GET` | `/assets/excon-medium.json` | `200` | REST endpoint |
| `GET` | `/assets/antonio-semibold.json` | `200` | REST endpoint |
| `GET` | `/assets/models/dairamon.gltf` | `200` | REST endpoint |
| `GET` | `/assets/models/portrait.dgltf.gltf` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /assets/excon-bold.json
```json
{
  "type": "object",
  "properties": {
    "pages": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "chars": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "index": {
            "type": "any"
          },
          "char": {
            "type": "any"
          },
          "width": {
            "type": "any"
          },
          "height": {
            "type": "any"
          },
          "xoffset": {
            "type": "any"
          },
          "yoffset": {
            "type": "any"
          },
          "xadvance": {
            "type": "any"
          },
          "chnl": {
            "type": "any"
          },
          "x": {
            "type": "any"
          },
          "y": {
            "type": "any"
          },
          "page": {
            "type": "any"
          }
        }
      }
    },
    "info": {
      "type": "object",
      "properties": {
        "face": {
          "type": "string"
        },
        "size": {
          "type": "number"
        },
        "bold": {
          "type": "number"
        },
        "italic": {
          "type": "number"
        },
        "charset": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "unicode": {
          "type": "number"
        },
        "stretchH": {
          "type": "number"
        },
        "smooth": {
          "type": "number"
        },
        "aa": {
          "type": "number"
        },
        "padding": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "spacing": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "outline": {
          "type": "number"
        }
      }
    },
    "common": {
      "type": "object",
      "properties": {
        "lineHeight": {
          "type": "number"
        },
        "base": {
          "type": "number"
        },
        "scaleW": {
          "type": "number"
        },
        "scaleH": {
          "type": "number"
        },
        "pages": {
          "type": "number"
        },
        "packed": {
          "type": "number"
        },
        "alphaChnl": {
          "type": "number"
        },
        "redChnl": {
          "type": "number"
        },
        "greenChnl": {
          "type": "number"
        },
        "blueChnl": {
          "type": "number"
        }
      }
    },
    "distanceField": {
      "type": "object",
      "properties": {
        "fieldType": {
          "type": "string"
        },
        "distanceRange": {
          "type": "number"
        }
      }
    },
    "kernings": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "first": {
            "type": "any"
          },
          "second": {
            "type": "any"
          },
          "amount": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /assets/excon-regular.json
```json
{
  "type": "object",
  "properties": {
    "pages": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "chars": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "index": {
            "type": "any"
          },
          "char": {
            "type": "any"
          },
          "width": {
            "type": "any"
          },
          "height": {
            "type": "any"
          },
          "xoffset": {
            "type": "any"
          },
          "yoffset": {
            "type": "any"
          },
          "xadvance": {
            "type": "any"
          },
          "chnl": {
            "type": "any"
          },
          "x": {
            "type": "any"
          },
          "y": {
            "type": "any"
          },
          "page": {
            "type": "any"
          }
        }
      }
    },
    "info": {
      "type": "object",
      "properties": {
        "face": {
          "type": "string"
        },
        "size": {
          "type": "number"
        },
        "bold": {
          "type": "number"
        },
        "italic": {
          "type": "number"
        },
        "charset": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "unicode": {
          "type": "number"
        },
        "stretchH": {
          "type": "number"
        },
        "smooth": {
          "type": "number"
        },
        "aa": {
          "type": "number"
        },
        "padding": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "spacing": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "outline": {
          "type": "number"
        }
      }
    },
    "common": {
      "type": "object",
      "properties": {
        "lineHeight": {
          "type": "number"
        },
        "base": {
          "type": "number"
        },
        "scaleW": {
          "type": "number"
        },
        "scaleH": {
          "type": "number"
        },
        "pages": {
          "type": "number"
        },
        "packed": {
          "type": "number"
        },
        "alphaChnl": {
          "type": "number"
        },
        "redChnl": {
          "type": "number"
        },
        "greenChnl": {
          "type": "number"
        },
        "blueChnl": {
          "type": "number"
        }
      }
    },
    "distanceField": {
      "type": "object",
      "properties": {
        "fieldType": {
          "type": "string"
        },
        "distanceRange": {
          "type": "number"
        }
      }
    },
    "kernings": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "first": {
            "type": "any"
          },
          "second": {
            "type": "any"
          },
          "amount": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /assets/excon-medium.json
```json
{
  "type": "object",
  "properties": {
    "pages": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "chars": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "index": {
            "type": "any"
          },
          "char": {
            "type": "any"
          },
          "width": {
            "type": "any"
          },
          "height": {
            "type": "any"
          },
          "xoffset": {
            "type": "any"
          },
          "yoffset": {
            "type": "any"
          },
          "xadvance": {
            "type": "any"
          },
          "chnl": {
            "type": "any"
          },
          "x": {
            "type": "any"
          },
          "y": {
            "type": "any"
          },
          "page": {
            "type": "any"
          }
        }
      }
    },
    "info": {
      "type": "object",
      "properties": {
        "face": {
          "type": "string"
        },
        "size": {
          "type": "number"
        },
        "bold": {
          "type": "number"
        },
        "italic": {
          "type": "number"
        },
        "charset": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "unicode": {
          "type": "number"
        },
        "stretchH": {
          "type": "number"
        },
        "smooth": {
          "type": "number"
        },
        "aa": {
          "type": "number"
        },
        "padding": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "spacing": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "outline": {
          "type": "number"
        }
      }
    },
    "common": {
      "type": "object",
      "properties": {
        "lineHeight": {
          "type": "number"
        },
        "base": {
          "type": "number"
        },
        "scaleW": {
          "type": "number"
        },
        "scaleH": {
          "type": "number"
        },
        "pages": {
          "type": "number"
        },
        "packed": {
          "type": "number"
        },
        "alphaChnl": {
          "type": "number"
        },
        "redChnl": {
          "type": "number"
        },
        "greenChnl": {
          "type": "number"
        },
        "blueChnl": {
          "type": "number"
        }
      }
    },
    "distanceField": {
      "type": "object",
      "properties": {
        "fieldType": {
          "type": "string"
        },
        "distanceRange": {
          "type": "number"
        }
      }
    },
    "kernings": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "first": {
            "type": "any"
          },
          "second": {
            "type": "any"
          },
          "amount": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /assets/antonio-semibold.json
```json
{
  "type": "object",
  "properties": {
    "pages": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "chars": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "index": {
            "type": "any"
          },
          "char": {
            "type": "any"
          },
          "width": {
            "type": "any"
          },
          "height": {
            "type": "any"
          },
          "xoffset": {
            "type": "any"
          },
          "yoffset": {
            "type": "any"
          },
          "xadvance": {
            "type": "any"
          },
          "chnl": {
            "type": "any"
          },
          "x": {
            "type": "any"
          },
          "y": {
            "type": "any"
          },
          "page": {
            "type": "any"
          }
        }
      }
    },
    "info": {
      "type": "object",
      "properties": {
        "face": {
          "type": "string"
        },
        "size": {
          "type": "number"
        },
        "bold": {
          "type": "number"
        },
        "italic": {
          "type": "number"
        },
        "charset": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "unicode": {
          "type": "number"
        },
        "stretchH": {
          "type": "number"
        },
        "smooth": {
          "type": "number"
        },
        "aa": {
          "type": "number"
        },
        "padding": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "spacing": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "outline": {
          "type": "number"
        }
      }
    },
    "common": {
      "type": "object",
      "properties": {
        "lineHeight": {
          "type": "number"
        },
        "base": {
          "type": "number"
        },
        "scaleW": {
          "type": "number"
        },
        "scaleH": {
          "type": "number"
        },
        "pages": {
          "type": "number"
        },
        "packed": {
          "type": "number"
        },
        "alphaChnl": {
          "type": "number"
        },
        "redChnl": {
          "type": "number"
        },
        "greenChnl": {
          "type": "number"
        },
        "blueChnl": {
          "type": "number"
        }
      }
    },
    "distanceField": {
      "type": "object",
      "properties": {
        "fieldType": {
          "type": "string"
        },
        "distanceRange": {
          "type": "number"
        }
      }
    },
    "kernings": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "first": {
            "type": "any"
          },
          "second": {
            "type": "any"
          },
          "amount": {
            "type": "any"
          }
        }
      }
    }
  }
}
```

