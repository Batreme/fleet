---
title: "APIs & Protocols: ondocollective-jp"
date: 2026-10-31
target: "[[overview|ondocollective-jp]]"
---

# Discovered APIs & Protocols: ondocollective-jp

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/webgl/stroke-data.json` | `200` | REST endpoint |
| `GET` | `/webgl/scene-config.json` | `200` | REST endpoint |
| `GET` | `/webgl/stroke-data.json` | `200` | REST endpoint |
| `GET` | `/webgl/scene-config.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /webgl/stroke-data.json
```json
{
  "type": "object",
  "properties": {
    "width": {
      "type": "number"
    },
    "height": {
      "type": "number"
    },
    "playbackMode": {
      "type": "string"
    },
    "groups": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "strokes": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /webgl/scene-config.json
```json
{
  "type": "object",
  "properties": {
    "version": {
      "type": "number"
    },
    "strokeGap": {
      "type": "number"
    },
    "draw": {
      "type": "object",
      "properties": {
        "duration": {
          "type": "number"
        },
        "initialProgress": {
          "type": "number"
        },
        "autoplay": {
          "type": "boolean"
        }
      }
    },
    "depth": {
      "type": "object",
      "properties": {
        "mode": {
          "type": "string"
        },
        "axes": {
          "type": "object",
          "properties": {
            "x": {
              "type": "any"
            },
            "y": {
              "type": "any"
            },
            "z": {
              "type": "any"
            }
          }
        }
      }
    },
    "camera": {
      "type": "object",
      "properties": {
        "x": {
          "type": "number"
        },
        "y": {
          "type": "number"
        },
        "z": {
          "type": "number"
        }
      }
    },
    "perspective": {
      "type": "object",
      "properties": {
        "enabled": {
          "type": "boolean"
        }
      }
    },
    "fog": {
      "type": "object",
      "properties": {
        "enabled": {
          "type": "boolean"
        },
        "nearOffset": {
          "type": "number"
        },
        "farOffset": {
          "type": "number"
        },
        "color": {
          "type": "string"
        }
      }
    },
    "wave": {
      "type": "object",
      "properties": {
        "enabled": {
          "type": "boolean"
        },
        "strength": {
          "type": "number"
        }
      }
    },
    "style": {
      "type": "object",
      "properties": {
        "strokeColor": {
          "type": "string"
        }
      }
    },
    "background": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string"
        },
        "name": {
          "type": "string"
        }
      }
    },
    "assets": {
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
          "visible": {
            "type": "any"
          },
          "strokeSrc": {
            "type": "any"
          },
          "transform": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /webgl/stroke-data.json
```json
{
  "type": "object",
  "properties": {
    "width": {
      "type": "number"
    },
    "height": {
      "type": "number"
    },
    "playbackMode": {
      "type": "string"
    },
    "groups": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "strokes": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /webgl/scene-config.json
```json
{
  "type": "object",
  "properties": {
    "version": {
      "type": "number"
    },
    "strokeGap": {
      "type": "number"
    },
    "draw": {
      "type": "object",
      "properties": {
        "duration": {
          "type": "number"
        },
        "initialProgress": {
          "type": "number"
        },
        "autoplay": {
          "type": "boolean"
        }
      }
    },
    "depth": {
      "type": "object",
      "properties": {
        "mode": {
          "type": "string"
        },
        "axes": {
          "type": "object",
          "properties": {
            "x": {
              "type": "any"
            },
            "y": {
              "type": "any"
            },
            "z": {
              "type": "any"
            }
          }
        }
      }
    },
    "camera": {
      "type": "object",
      "properties": {
        "x": {
          "type": "number"
        },
        "y": {
          "type": "number"
        },
        "z": {
          "type": "number"
        }
      }
    },
    "perspective": {
      "type": "object",
      "properties": {
        "enabled": {
          "type": "boolean"
        }
      }
    },
    "fog": {
      "type": "object",
      "properties": {
        "enabled": {
          "type": "boolean"
        },
        "nearOffset": {
          "type": "number"
        },
        "farOffset": {
          "type": "number"
        },
        "color": {
          "type": "string"
        }
      }
    },
    "wave": {
      "type": "object",
      "properties": {
        "enabled": {
          "type": "boolean"
        },
        "strength": {
          "type": "number"
        }
      }
    },
    "style": {
      "type": "object",
      "properties": {
        "strokeColor": {
          "type": "string"
        }
      }
    },
    "background": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string"
        },
        "name": {
          "type": "string"
        }
      }
    },
    "assets": {
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
          "visible": {
            "type": "any"
          },
          "strokeSrc": {
            "type": "any"
          },
          "transform": {
            "type": "any"
          }
        }
      }
    }
  }
}
```

