---
title: "APIs & Protocols: www-iamsunnywang-com"
date: 2026-11-14
target: "[[overview|www-iamsunnywang-com]]"
---

# Discovered APIs & Protocols: www-iamsunnywang-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/default-language` | `200` | REST endpoint |
| `GET` | `/assets/storymode-production/thoughts/thoughts-memory-river-scene-v1.metadata.json` | `200` | REST endpoint |
| `GET` | `/assets/storymode-production/about/layout/about-layout-defaults.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/default-language
```json
{
  "type": "object",
  "properties": {
    "lang": {
      "type": "string"
    },
    "country": {
      "type": "string"
    },
    "source": {
      "type": "string"
    }
  }
}
```
### `GET` /assets/storymode-production/thoughts/thoughts-memory-river-scene-v1.metadata.json
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "version": {
      "type": "string"
    },
    "authoredBy": {
      "type": "string"
    },
    "sourceOfTruth": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "scene": {
      "type": "object",
      "properties": {
        "size": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "aspect": {
          "type": "number"
        },
        "renderOrder": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    },
    "background": {
      "type": "object",
      "properties": {
        "src": {
          "type": "string"
        },
        "canvas": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "fit": {
          "type": "string"
        }
      }
    },
    "river": {
      "type": "object",
      "properties": {
        "src": {
          "type": "string"
        },
        "canvas": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "alphaBBox": {
          "type": "object",
          "properties": {
            "x": {
              "type": "any"
            },
            "y": {
              "type": "any"
            },
            "width": {
              "type": "any"
            },
            "height": {
              "type": "any"
            }
          }
        },
        "drawRect": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "note": {
          "type": "string"
        }
      }
    },
    "route": {
      "type": "object",
      "properties": {
        "space": {
          "type": "string"
        },
        "sampleCount": {
          "type": "number"
        },
        "points": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "tangents": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "stops": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "derivation": {
          "type": "string"
        }
      }
    },
    "character": {
      "type": "object",
      "properties": {
        "src": {
          "type": "string"
        },
        "canvas": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "alphaBBox": {
          "type": "object",
          "properties": {
            "x": {
              "type": "any"
            },
            "y": {
              "type": "any"
            },
            "width": {
              "type": "any"
            },
            "height": {
              "type": "any"
            }
          }
        },
        "scale": {
          "type": "number"
        },
        "center": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "visibleSize": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "centerNorm": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "visibleWidthNorm": {
          "type": "number"
        },
        "role": {
          "type": "string"
        },
        "inseparable": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "note": {
          "type": "string"
        }
      }
    },
    "portal": {
      "type": "object",
      "properties": {
        "src": {
          "type": "string"
        },
        "canvas": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "alphaBBox": {
          "type": "object",
          "properties": {
            "x": {
              "type": "any"
            },
            "y": {
              "type": "any"
            },
            "width": {
              "type": "any"
            },
            "height": {
              "type": "any"
            }
          }
        },
        "scale": {
          "type": "number"
        },
        "center": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "visibleSize": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "centerNorm": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "visibleWidthNorm": {
          "type": "number"
        },
        "opening": {
          "type": "object",
          "properties": {
            "canvasPolygon": {
              "type": "any"
            },
            "canvasRightEdge": {
              "type": "any"
            },
            "authoredRimCount": {
              "type": "any"
            },
            "canvasOuterRightEdge": {
              "type": "any"
            },
            "nearCanopyMouth": {
              "type": "any"
            },
            "nearCanopyFromX": {
              "type": "any"
            },
            "canvasFrac": {
              "type": "any"
            },
            "widthOfPaintedWidth": {
              "type": "any"
            }
          }
        }
      }
    },
    "islands": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "src": {
            "type": "any"
          },
          "canvas": {
            "type": "any"
          },
          "alphaBBox": {
            "type": "any"
          },
          "scale": {
            "type": "any"
          },
          "center": {
            "type": "any"
          },
          "visibleSize": {
            "type": "any"
          },
          "centerNorm": {
            "type": "any"
          },
          "visibleWidthNorm": {
            "type": "any"
          },
          "id": {
            "type": "any"
          },
          "order": {
            "type": "any"
          },
          "revealOrder": {
            "type": "any"
          },
          "title": {
            "type": "any"
          },
          "routeStopId": {
            "type": "any"
          },
          "routeProgress": {
            "type": "any"
          },
          "dock": {
            "type": "any"
          }
        }
      }
    },
    "lanterns": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "src": {
            "type": "any"
          },
          "canvas": {
            "type": "any"
          },
          "alphaBBox": {
            "type": "any"
          },
          "scale": {
            "type": "any"
          },
          "center": {
            "type": "any"
          },
          "visibleSize": {
            "type": "any"
          },
          "centerNorm": {
            "type": "any"
          },
          "visibleWidthNorm": {
            "type": "any"
          }
        }
      }
    },
    "props": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "src": {
            "type": "any"
          },
          "canvas": {
            "type": "any"
          },
          "alphaBBox": {
            "type": "any"
          },
          "scale": {
            "type": "any"
          },
          "center": {
            "type": "any"
          },
          "visibleSize": {
            "type": "any"
          },
          "centerNorm": {
            "type": "any"
          },
          "visibleWidthNorm": {
            "type": "any"
          },
          "opacity": {
            "type": "any"
          }
        }
      }
    },
    "foreground": {
      "type": "object",
      "properties": {
        "left": {
          "type": "object",
          "properties": {
            "src": {
              "type": "any"
            },
            "canvas": {
              "type": "any"
            },
            "alphaBBox": {
              "type": "any"
            },
            "scale": {
              "type": "any"
            },
            "center": {
              "type": "any"
            },
            "visibleSize": {
              "type": "any"
            },
            "centerNorm": {
              "type": "any"
            },
            "visibleWidthNorm": {
              "type": "any"
            },
            "pin": {
              "type": "any"
            }
          }
        },
        "right": {
          "type": "object",
          "properties": {
            "src": {
              "type": "any"
            },
            "canvas": {
              "type": "any"
            },
            "alphaBBox": {
              "type": "any"
            },
            "scale": {
              "type": "any"
            },
            "center": {
              "type": "any"
            },
            "visibleSize": {
              "type": "any"
            },
            "centerNorm": {
              "type": "any"
            },
            "visibleWidthNorm": {
              "type": "any"
            },
            "pin": {
              "type": "any"
            }
          }
        }
      }
    },
    "chapterSign": {
      "type": "object",
      "properties": {
        "src": {
          "type": "object",
          "properties": {
            "en": {
              "type": "any"
            },
            "zh": {
              "type": "any"
            }
          }
        },
        "canvas": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "alphaBBox": {
          "type": "object",
          "properties": {
            "x": {
              "type": "any"
            },
            "y": {
              "type": "any"
            },
            "width": {
              "type": "any"
            },
            "height": {
              "type": "any"
            }
          }
        },
        "center": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "visibleSize": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "centerNorm": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "visibleWidthNorm": {
          "type": "number"
        }
      }
    },
    "islandMarkers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "order": {
            "type": "any"
          },
          "src": {
            "type": "any"
          },
          "zhIsEnglish": {
            "type": "any"
          },
          "canvas": {
            "type": "any"
          },
          "alphaBBox": {
            "type": "any"
          },
          "center": {
            "type": "any"
          },
          "visibleSize": {
            "type": "any"
          },
          "centerNorm": {
            "type": "any"
          },
          "visibleWidthNorm": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /assets/storymode-production/about/layout/about-layout-defaults.json
```json
{
  "type": "object",
  "properties": {
    "about-prologue-polaroid": {
      "type": "object",
      "properties": {
        "rotation": {
          "type": "number"
        },
        "scale": {
          "type": "number"
        },
        "unit": {
          "type": "string"
        },
        "x": {
          "type": "number"
        },
        "y": {
          "type": "number"
        }
      }
    },
    "ai-lab-architecture": {
      "type": "object",
      "properties": {
        "rotation": {
          "type": "number"
        },
        "scale": {
          "type": "number"
        },
        "unit": {
          "type": "string"
        },
        "x": {
          "type": "number"
        },
        "y": {
          "type": "number"
        }
      }
    },
    "ai-lab-line": {
      "type": "object",
      "properties": {
        "rotation": {
          "type": "number"
        },
        "scale": {
          "type": "number"
        },
        "unit": {
          "type": "string"
        },
        "x": {
          "type": "number"
        },
        "y": {
          "type": "number"
        }
      }
    },
    "ai-lab-objects": {
      "type": "object",
      "properties": {
        "rotation": {
          "type": "number"
        },
        "scale": {
          "type": "number"
        },
        "unit": {
          "type": "string"
        },
        "x": {
          "type": "number"
        },
        "y": {
          "type": "number"
        }
      }
    },
    "airbnb-architecture": {
      "type": "object",
      "properties": {
        "rotation": {
          "type": "number"
        },
        "scale": {
          "type": "number"
        },
        "unit": {
          "type": "string"
        },
        "x": {
          "type": "number"
        },
        "y": {
          "type": "number"
        }
      }
    },
    "airbnb-line": {
      "type": "object",
      "properties": {
        "rotation": {
          "type": "number"
        },
        "scale": {
          "type": "number"
        },
        "unit": {
          "type": "string"
        },
        "x": {
          "type": "number"
        },
        "y": {
          "type": "number"
        }
      }
    },
    "airbnb-objects": {
      "type": "object",
      "properties": {
        "rotation": {
          "type": "number"
        },
        "scale": {
          "type": "number"
        },
        "unit": {
          "type": "string"
        },
        "x": {
          "type": "number"
        },
        "y": {
          "type": "number"
        }
      }
    },
    "art-architecture": {
      "type": "object",
      "properties": {
        "rotation": {
          "type": "number"
        },
        "scale": {
          "type": "number"
        },
        "unit": {
          "type": "string"
        },
        "x": {
          "type": "number"
        },
        "y": {
          "type": "number"
        }
      }
    },
    "art-line": {
      "type": "object",
      "properties": {
        "rotation": {
          "type": "number"
        },
        "scale": {
          "type": "number"
        },
        "unit": {
          "type": "string"
        },
        "x": {
          "type": "number"
        },
        "y": {
          "type": "number"
        }
      }
    },
    "art-objects": {
      "type": "object",
      "properties": {
        "rotation": {
          "type": "number"
        },
        "scale": {
          "type": "number"
        },
        "unit": {
          "type": "string"
        },
        "x": {
          "type": "number"
        },
        "y": {
          "type": "number"
        }
      }
    },
    "bubble-polaroid": {
      "type": "object",
      "properties": {
        "rotation": {
          "type": "number"
        },
        "scale": {
          "type": "number"
        },
        "unit": {
          "type": "string"
        },
        "x": {
          "type": "number"
        },
        "y": {
          "type": "number"
        }
      }
    },
    "cmu-architecture": {
      "type": "object",
      "properties": {
        "rotation": {
          "type": "number"
        },
        "scale": {
          "type": "number"
        },
        "unit": {
          "type": "string"
        },
        "x": {
          "type": "number"
        },
        "y": {
          "type": "number"
        }
      }
    },
    "cmu-line": {
      "type": "object",
      "properties": {
        "rotation": {
          "type": "number"
        },
        "scale": {
          "type": "number"
        },
        "unit": {
          "type": "string"
        },
        "x": {
          "type": "number"
        },
        "y": {
          "type": "number"
        }
      }
    },
    "cmu-objects": {
      "type": "object",
      "properties": {
        "rotation": {
          "type": "number"
        },
        "scale": {
          "type": "number"
        },
        "unit": {
          "type": "string"
        },
        "x": {
          "type": "number"
        },
        "y": {
          "type": "number"
        }
      }
    },
    "college-architecture": {
      "type": "object",
      "properties": {
        "rotation": {
          "type": "number"
        },
        "scale": {
          "type": "number"
        },
        "unit": {
          "type": "string"
        },
        "x": {
          "type": "number"
        },
        "y": {
          "type": "number"
        }
      }
    },
    "college-line": {
      "type": "object",
      "properties": {
        "rotation": {
          "type": "number"
        },
        "scale": {
          "type": "number"
        },
        "unit": {
          "type": "string"
        },
        "x": {
          "type": "number"
        },
        "y": {
          "type": "number"
        }
      }
    },
    "college-objects": {
      "type": "object",
      "properties": {
        "rotation": {
          "type": "number"
        },
        "scale": {
          "type": "number"
        },
        "unit": {
          "type": "string"
        },
        "x": {
          "type": "number"
        },
        "y": {
          "type": "number"
        }
      }
    },
    "contents-copy": {
      "type": "object",
      "properties": {
        "rotation": {
          "type": "number"
        },
        "scale": {
          "type": "number"
        },
        "unit": {
          "type": "string"
        },
        "x": {
          "type": "number"
        },
        "y": {
          "type": "number"
        }
      }
    },
    "credits-copy": {
      "type": "object",
      "properties": {
        "rotation": {
          "type": "number"
        },
        "scale": {
          "type": "number"
        },
        "unit": {
          "type": "string"
        },
        "x": {
          "type": "number"
        },
        "y": {
          "type": "number"
        }
      }
    },
    "credits-footnote": {
      "type": "object",
      "properties": {
        "rotation": {
          "type": "number"
        },
        "scale": {
          "type": "number"
        },
        "unit": {
          "type": "string"
        },
        "x": {
          "type": "number"
        },
        "y": {
          "type": "number"
        }
      }
    }
  }
}
```

