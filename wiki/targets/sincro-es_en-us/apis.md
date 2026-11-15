---
title: "APIs & Protocols: sincro-es_en-us"
date: 2026-11-14
target: "sincro-es_en-us"
---

# Discovered APIs & Protocols: sincro-es_en-us

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/_i18n/UVBXLm-z/en/messages.json` | `200` | REST endpoint |
| `GET` | `/carbon-data.json` | `200` | REST endpoint |
| `GET` | `/files/06wn0w2g/production/ea79ff7760dc4e6d174451dfe506ad2567aa6a9a.json` | `200` | REST endpoint |
| `GET` | `/files/06wn0w2g/production/1dedfda77da54538894c4b46a95701ce9e6c1369.json` | `200` | REST endpoint |
| `GET` | `/files/06wn0w2g/production/861dd48cb375955dfb2216a97e19753c5f47dba2.json` | `200` | REST endpoint |
| `GET` | `/files/06wn0w2g/production/11955410480d1e312ad8f34c403a34f225dd5ecd.json` | `200` | REST endpoint |
| `GET` | `/files/06wn0w2g/production/42395f5e7571eb11efab519721aeea9c06e43162.json` | `200` | REST endpoint |
| `GET` | `/files/06wn0w2g/production/c08ce8efa5bc3cb0c54723559a483bea4b2bf942.json` | `200` | REST endpoint |
| `GET` | `/files/06wn0w2g/production/7bc9448e0932956dd96cfa43c49cb3e9b5105309.json` | `200` | REST endpoint |
| `GET` | `/files/06wn0w2g/production/54d632665c6ef890382ee6d14f5112a8e4f52218.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /_i18n/UVBXLm-z/en/messages.json
```json
{
  "type": "object",
  "properties": {
    "en": {
      "type": "object",
      "properties": {}
    }
  }
}
```
### `GET` /carbon-data.json
```json
{
  "type": "object",
  "properties": {
    "buildData": {
      "type": "object",
      "properties": {
        "htmlBytes": {
          "type": "number"
        },
        "cssBytes": {
          "type": "number"
        },
        "jsBytes": {
          "type": "number"
        },
        "imageBytes": {
          "type": "number"
        },
        "fontBytes": {
          "type": "number"
        },
        "estimatedPageLoad": {
          "type": "number"
        }
      }
    },
    "carbonMetrics": {
      "type": "object",
      "properties": {
        "bytes": {
          "type": "number"
        },
        "green": {
          "type": "boolean"
        },
        "gco2e": {
          "type": "number"
        },
        "rating": {
          "type": "string"
        },
        "statistics": {
          "type": "object",
          "properties": {
            "adjustedBytes": {
              "type": "any"
            },
            "energy": {
              "type": "any"
            },
            "co2": {
              "type": "any"
            }
          }
        },
        "cleanerThan": {
          "type": "number"
        }
      }
    }
  }
}
```
### `GET` /files/06wn0w2g/production/ea79ff7760dc4e6d174451dfe506ad2567aa6a9a.json
```json
{
  "type": "object",
  "properties": {
    "v": {
      "type": "string"
    },
    "fr": {
      "type": "number"
    },
    "ip": {
      "type": "number"
    },
    "op": {
      "type": "number"
    },
    "w": {
      "type": "number"
    },
    "h": {
      "type": "number"
    },
    "nm": {
      "type": "string"
    },
    "ddd": {
      "type": "number"
    },
    "assets": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "nm": {
            "type": "any"
          },
          "fr": {
            "type": "any"
          },
          "layers": {
            "type": "any"
          }
        }
      }
    },
    "layers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "ddd": {
            "type": "any"
          },
          "ind": {
            "type": "any"
          },
          "ty": {
            "type": "any"
          },
          "nm": {
            "type": "any"
          },
          "refId": {
            "type": "any"
          },
          "sr": {
            "type": "any"
          },
          "ks": {
            "type": "any"
          },
          "ao": {
            "type": "any"
          },
          "tm": {
            "type": "any"
          },
          "w": {
            "type": "any"
          },
          "h": {
            "type": "any"
          },
          "ip": {
            "type": "any"
          },
          "op": {
            "type": "any"
          },
          "st": {
            "type": "any"
          },
          "bm": {
            "type": "any"
          }
        }
      }
    },
    "markers": {
      "type": "array",
      "items": "any"
    },
    "props": {
      "type": "object",
      "properties": {}
    }
  }
}
```
### `GET` /files/06wn0w2g/production/1dedfda77da54538894c4b46a95701ce9e6c1369.json
```json
{
  "type": "object",
  "properties": {
    "v": {
      "type": "string"
    },
    "fr": {
      "type": "number"
    },
    "ip": {
      "type": "number"
    },
    "op": {
      "type": "number"
    },
    "w": {
      "type": "number"
    },
    "h": {
      "type": "number"
    },
    "nm": {
      "type": "string"
    },
    "ddd": {
      "type": "number"
    },
    "assets": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "nm": {
            "type": "any"
          },
          "fr": {
            "type": "any"
          },
          "layers": {
            "type": "any"
          }
        }
      }
    },
    "layers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "ddd": {
            "type": "any"
          },
          "ind": {
            "type": "any"
          },
          "ty": {
            "type": "any"
          },
          "nm": {
            "type": "any"
          },
          "refId": {
            "type": "any"
          },
          "sr": {
            "type": "any"
          },
          "ks": {
            "type": "any"
          },
          "ao": {
            "type": "any"
          },
          "w": {
            "type": "any"
          },
          "h": {
            "type": "any"
          },
          "ip": {
            "type": "any"
          },
          "op": {
            "type": "any"
          },
          "st": {
            "type": "any"
          },
          "ct": {
            "type": "any"
          },
          "bm": {
            "type": "any"
          }
        }
      }
    },
    "markers": {
      "type": "array",
      "items": "any"
    },
    "props": {
      "type": "object",
      "properties": {}
    }
  }
}
```
### `GET` /files/06wn0w2g/production/861dd48cb375955dfb2216a97e19753c5f47dba2.json
```json
{
  "type": "object",
  "properties": {
    "v": {
      "type": "string"
    },
    "fr": {
      "type": "number"
    },
    "ip": {
      "type": "number"
    },
    "op": {
      "type": "number"
    },
    "w": {
      "type": "number"
    },
    "h": {
      "type": "number"
    },
    "nm": {
      "type": "string"
    },
    "ddd": {
      "type": "number"
    },
    "assets": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "nm": {
            "type": "any"
          },
          "fr": {
            "type": "any"
          },
          "layers": {
            "type": "any"
          }
        }
      }
    },
    "layers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "ddd": {
            "type": "any"
          },
          "ind": {
            "type": "any"
          },
          "ty": {
            "type": "any"
          },
          "nm": {
            "type": "any"
          },
          "tt": {
            "type": "any"
          },
          "tp": {
            "type": "any"
          },
          "sr": {
            "type": "any"
          },
          "ks": {
            "type": "any"
          },
          "ao": {
            "type": "any"
          },
          "sw": {
            "type": "any"
          },
          "sh": {
            "type": "any"
          },
          "sc": {
            "type": "any"
          },
          "ip": {
            "type": "any"
          },
          "op": {
            "type": "any"
          },
          "st": {
            "type": "any"
          },
          "bm": {
            "type": "any"
          }
        }
      }
    },
    "markers": {
      "type": "array",
      "items": "any"
    },
    "props": {
      "type": "object",
      "properties": {}
    }
  }
}
```
### `GET` /files/06wn0w2g/production/11955410480d1e312ad8f34c403a34f225dd5ecd.json
```json
{
  "type": "object",
  "properties": {
    "v": {
      "type": "string"
    },
    "fr": {
      "type": "number"
    },
    "ip": {
      "type": "number"
    },
    "op": {
      "type": "number"
    },
    "w": {
      "type": "number"
    },
    "h": {
      "type": "number"
    },
    "nm": {
      "type": "string"
    },
    "ddd": {
      "type": "number"
    },
    "assets": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "nm": {
            "type": "any"
          },
          "fr": {
            "type": "any"
          },
          "layers": {
            "type": "any"
          }
        }
      }
    },
    "layers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "ddd": {
            "type": "any"
          },
          "ind": {
            "type": "any"
          },
          "ty": {
            "type": "any"
          },
          "nm": {
            "type": "any"
          },
          "tt": {
            "type": "any"
          },
          "tp": {
            "type": "any"
          },
          "sr": {
            "type": "any"
          },
          "ks": {
            "type": "any"
          },
          "ao": {
            "type": "any"
          },
          "sw": {
            "type": "any"
          },
          "sh": {
            "type": "any"
          },
          "sc": {
            "type": "any"
          },
          "ip": {
            "type": "any"
          },
          "op": {
            "type": "any"
          },
          "st": {
            "type": "any"
          },
          "bm": {
            "type": "any"
          }
        }
      }
    },
    "markers": {
      "type": "array",
      "items": "any"
    },
    "props": {
      "type": "object",
      "properties": {}
    }
  }
}
```
### `GET` /files/06wn0w2g/production/42395f5e7571eb11efab519721aeea9c06e43162.json
```json
{
  "type": "object",
  "properties": {
    "v": {
      "type": "string"
    },
    "fr": {
      "type": "number"
    },
    "ip": {
      "type": "number"
    },
    "op": {
      "type": "number"
    },
    "w": {
      "type": "number"
    },
    "h": {
      "type": "number"
    },
    "nm": {
      "type": "string"
    },
    "ddd": {
      "type": "number"
    },
    "assets": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "nm": {
            "type": "any"
          },
          "fr": {
            "type": "any"
          },
          "layers": {
            "type": "any"
          }
        }
      }
    },
    "layers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "ddd": {
            "type": "any"
          },
          "ind": {
            "type": "any"
          },
          "ty": {
            "type": "any"
          },
          "nm": {
            "type": "any"
          },
          "tt": {
            "type": "any"
          },
          "tp": {
            "type": "any"
          },
          "sr": {
            "type": "any"
          },
          "ks": {
            "type": "any"
          },
          "ao": {
            "type": "any"
          },
          "sw": {
            "type": "any"
          },
          "sh": {
            "type": "any"
          },
          "sc": {
            "type": "any"
          },
          "ip": {
            "type": "any"
          },
          "op": {
            "type": "any"
          },
          "st": {
            "type": "any"
          },
          "bm": {
            "type": "any"
          }
        }
      }
    },
    "markers": {
      "type": "array",
      "items": "any"
    },
    "props": {
      "type": "object",
      "properties": {}
    }
  }
}
```
### `GET` /files/06wn0w2g/production/c08ce8efa5bc3cb0c54723559a483bea4b2bf942.json
```json
{
  "type": "object",
  "properties": {
    "v": {
      "type": "string"
    },
    "fr": {
      "type": "number"
    },
    "ip": {
      "type": "number"
    },
    "op": {
      "type": "number"
    },
    "w": {
      "type": "number"
    },
    "h": {
      "type": "number"
    },
    "nm": {
      "type": "string"
    },
    "ddd": {
      "type": "number"
    },
    "assets": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "nm": {
            "type": "any"
          },
          "fr": {
            "type": "any"
          },
          "layers": {
            "type": "any"
          }
        }
      }
    },
    "layers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "ddd": {
            "type": "any"
          },
          "ind": {
            "type": "any"
          },
          "ty": {
            "type": "any"
          },
          "nm": {
            "type": "any"
          },
          "refId": {
            "type": "any"
          },
          "sr": {
            "type": "any"
          },
          "ks": {
            "type": "any"
          },
          "ao": {
            "type": "any"
          },
          "w": {
            "type": "any"
          },
          "h": {
            "type": "any"
          },
          "ip": {
            "type": "any"
          },
          "op": {
            "type": "any"
          },
          "st": {
            "type": "any"
          },
          "bm": {
            "type": "any"
          }
        }
      }
    },
    "markers": {
      "type": "array",
      "items": "any"
    },
    "props": {
      "type": "object",
      "properties": {}
    }
  }
}
```
### `GET` /files/06wn0w2g/production/7bc9448e0932956dd96cfa43c49cb3e9b5105309.json
```json
{
  "type": "object",
  "properties": {
    "v": {
      "type": "string"
    },
    "fr": {
      "type": "number"
    },
    "ip": {
      "type": "number"
    },
    "op": {
      "type": "number"
    },
    "w": {
      "type": "number"
    },
    "h": {
      "type": "number"
    },
    "nm": {
      "type": "string"
    },
    "ddd": {
      "type": "number"
    },
    "assets": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "nm": {
            "type": "any"
          },
          "fr": {
            "type": "any"
          },
          "layers": {
            "type": "any"
          }
        }
      }
    },
    "layers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "ddd": {
            "type": "any"
          },
          "ind": {
            "type": "any"
          },
          "ty": {
            "type": "any"
          },
          "nm": {
            "type": "any"
          },
          "refId": {
            "type": "any"
          },
          "sr": {
            "type": "any"
          },
          "ks": {
            "type": "any"
          },
          "ao": {
            "type": "any"
          },
          "w": {
            "type": "any"
          },
          "h": {
            "type": "any"
          },
          "ip": {
            "type": "any"
          },
          "op": {
            "type": "any"
          },
          "st": {
            "type": "any"
          },
          "bm": {
            "type": "any"
          }
        }
      }
    },
    "markers": {
      "type": "array",
      "items": "any"
    },
    "props": {
      "type": "object",
      "properties": {}
    }
  }
}
```
### `GET` /files/06wn0w2g/production/54d632665c6ef890382ee6d14f5112a8e4f52218.json
```json
{
  "type": "object",
  "properties": {
    "v": {
      "type": "string"
    },
    "fr": {
      "type": "number"
    },
    "ip": {
      "type": "number"
    },
    "op": {
      "type": "number"
    },
    "w": {
      "type": "number"
    },
    "h": {
      "type": "number"
    },
    "nm": {
      "type": "string"
    },
    "ddd": {
      "type": "number"
    },
    "assets": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "nm": {
            "type": "any"
          },
          "fr": {
            "type": "any"
          },
          "layers": {
            "type": "any"
          }
        }
      }
    },
    "layers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "ddd": {
            "type": "any"
          },
          "ind": {
            "type": "any"
          },
          "ty": {
            "type": "any"
          },
          "nm": {
            "type": "any"
          },
          "refId": {
            "type": "any"
          },
          "sr": {
            "type": "any"
          },
          "ks": {
            "type": "any"
          },
          "ao": {
            "type": "any"
          },
          "w": {
            "type": "any"
          },
          "h": {
            "type": "any"
          },
          "ip": {
            "type": "any"
          },
          "op": {
            "type": "any"
          },
          "st": {
            "type": "any"
          },
          "ct": {
            "type": "any"
          },
          "bm": {
            "type": "any"
          }
        }
      }
    },
    "markers": {
      "type": "array",
      "items": "any"
    },
    "props": {
      "type": "object",
      "properties": {}
    }
  }
}
```

