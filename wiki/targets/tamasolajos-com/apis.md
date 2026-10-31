---
title: "APIs & Protocols: tamasolajos-com"
date: 2026-10-31
target: "[[overview|tamasolajos-com]]"
---

# Discovered APIs & Protocols: tamasolajos-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/data/site.json` | `200` | REST endpoint |
| `GET` | `/assets/alpino-black.json` | `200` | REST endpoint |
| `GET` | `/assets/satoshi-regular.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /data/site.json
```json
{
  "type": "object",
  "properties": {
    "meta": {
      "type": "object",
      "properties": {
        "siteTitle": {
          "type": "string"
        },
        "email": {
          "type": "string"
        }
      }
    },
    "menu": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "any"
          },
          "link": {
            "type": "any"
          },
          "visible": {
            "type": "any"
          }
        }
      }
    },
    "pages": {
      "type": "object",
      "properties": {
        "home": {
          "type": "object",
          "properties": {
            "overline": {
              "type": "any"
            },
            "headline": {
              "type": "any"
            },
            "subheading": {
              "type": "any"
            },
            "cta": {
              "type": "any"
            },
            "video": {
              "type": "any"
            },
            "video_short": {
              "type": "any"
            }
          }
        },
        "work": {
          "type": "object",
          "properties": {
            "heading": {
              "type": "any"
            },
            "projects": {
              "type": "any"
            }
          }
        },
        "about": {
          "type": "object",
          "properties": {
            "heading": {
              "type": "any"
            },
            "title": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "brands": {
              "type": "any"
            },
            "video_short": {
              "type": "any"
            },
            "text_short": {
              "type": "any"
            }
          }
        },
        "contact": {
          "type": "object",
          "properties": {
            "overline": {
              "type": "any"
            },
            "headline": {
              "type": "any"
            },
            "subheading": {
              "type": "any"
            },
            "video_short": {
              "type": "any"
            },
            "text_short": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `GET` /assets/alpino-black.json
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
### `GET` /assets/satoshi-regular.json
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

