---
title: "APIs & Protocols: 11moissanstoit-com"
date: 2026-11-14
target: "[[overview|11moissanstoit-com]]"
---

# Discovered APIs & Protocols: 11moissanstoit-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/data/translations.en.json` | `200` | REST endpoint |
| `GET` | `/data/trajets/routes.json` | `200` | REST endpoint |
| `GET` | `/planet` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /data/translations.en.json
```json
{
  "type": "object",
  "properties": {
    "locale": {
      "type": "string"
    },
    "entries": {
      "type": "object",
      "properties": {
        "tw:23894775401:text": {
          "type": "object",
          "properties": {
            "en": {
              "type": "any"
            },
            "h": {
              "type": "any"
            }
          }
        },
        "tw:23899256512:text": {
          "type": "object",
          "properties": {
            "en": {
              "type": "any"
            },
            "h": {
              "type": "any"
            }
          }
        },
        "tw:23900714571:text": {
          "type": "object",
          "properties": {
            "en": {
              "type": "any"
            },
            "h": {
              "type": "any"
            }
          }
        },
        "tw:23900878674:text": {
          "type": "object",
          "properties": {
            "en": {
              "type": "any"
            },
            "h": {
              "type": "any"
            }
          }
        },
        "tw:23901392392:text": {
          "type": "object",
          "properties": {
            "en": {
              "type": "any"
            },
            "h": {
              "type": "any"
            }
          }
        },
        "tw:23905416438:text": {
          "type": "object",
          "properties": {
            "en": {
              "type": "any"
            },
            "h": {
              "type": "any"
            }
          }
        },
        "tw:24005438460:text": {
          "type": "object",
          "properties": {
            "en": {
              "type": "any"
            },
            "h": {
              "type": "any"
            }
          }
        },
        "tw:25022149259:text": {
          "type": "object",
          "properties": {
            "en": {
              "type": "any"
            },
            "h": {
              "type": "any"
            }
          }
        },
        "tw:25042015526:text": {
          "type": "object",
          "properties": {
            "en": {
              "type": "any"
            },
            "h": {
              "type": "any"
            }
          }
        },
        "tw:25707609386:text": {
          "type": "object",
          "properties": {
            "en": {
              "type": "any"
            },
            "h": {
              "type": "any"
            }
          }
        },
        "tw:26030879172:text": {
          "type": "object",
          "properties": {
            "en": {
              "type": "any"
            },
            "h": {
              "type": "any"
            }
          }
        },
        "tw:26102887155:text": {
          "type": "object",
          "properties": {
            "en": {
              "type": "any"
            },
            "h": {
              "type": "any"
            }
          }
        },
        "tw:26103233098:text": {
          "type": "object",
          "properties": {
            "en": {
              "type": "any"
            },
            "h": {
              "type": "any"
            }
          }
        },
        "tw:26119213286:text": {
          "type": "object",
          "properties": {
            "en": {
              "type": "any"
            },
            "h": {
              "type": "any"
            }
          }
        },
        "tw:26233419549:text": {
          "type": "object",
          "properties": {
            "en": {
              "type": "any"
            },
            "h": {
              "type": "any"
            }
          }
        },
        "tw:26233777741:text": {
          "type": "object",
          "properties": {
            "en": {
              "type": "any"
            },
            "h": {
              "type": "any"
            }
          }
        },
        "tw:26235298389:text": {
          "type": "object",
          "properties": {
            "en": {
              "type": "any"
            },
            "h": {
              "type": "any"
            }
          }
        },
        "ptw:26218182944:text": {
          "type": "object",
          "properties": {
            "en": {
              "type": "any"
            },
            "h": {
              "type": "any"
            }
          }
        },
        "ptw:26234291339:text": {
          "type": "object",
          "properties": {
            "en": {
              "type": "any"
            },
            "h": {
              "type": "any"
            }
          }
        },
        "ptw:26235023433:text": {
          "type": "object",
          "properties": {
            "en": {
              "type": "any"
            },
            "h": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `GET` /data/trajets/routes.json
```json
{
  "type": "object",
  "properties": {
    "bus-3-4": {
      "type": "object",
      "properties": {
        "transport": {
          "type": "string"
        },
        "from": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "to": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "geometry": {
          "type": "object",
          "properties": {
            "coordinates": {
              "type": "any"
            },
            "type": {
              "type": "any"
            }
          }
        }
      }
    },
    "bus-4-5": {
      "type": "object",
      "properties": {
        "transport": {
          "type": "string"
        },
        "from": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "to": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "geometry": {
          "type": "object",
          "properties": {
            "coordinates": {
              "type": "any"
            },
            "type": {
              "type": "any"
            }
          }
        }
      }
    },
    "bus-5-6": {
      "type": "object",
      "properties": {
        "transport": {
          "type": "string"
        },
        "from": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "to": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "geometry": {
          "type": "object",
          "properties": {
            "coordinates": {
              "type": "any"
            },
            "type": {
              "type": "any"
            }
          }
        }
      }
    },
    "bus-6-7": {
      "type": "object",
      "properties": {
        "transport": {
          "type": "string"
        },
        "from": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "to": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "geometry": {
          "type": "object",
          "properties": {
            "coordinates": {
              "type": "any"
            },
            "type": {
              "type": "any"
            }
          }
        }
      }
    },
    "bus-7-8": {
      "type": "object",
      "properties": {
        "transport": {
          "type": "string"
        },
        "from": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "to": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "geometry": {
          "type": "object",
          "properties": {
            "coordinates": {
              "type": "any"
            },
            "type": {
              "type": "any"
            }
          }
        }
      }
    },
    "bus-8-9": {
      "type": "object",
      "properties": {
        "transport": {
          "type": "string"
        },
        "from": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "to": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "geometry": {
          "type": "object",
          "properties": {
            "coordinates": {
              "type": "any"
            },
            "type": {
              "type": "any"
            }
          }
        }
      }
    },
    "bus-9-10": {
      "type": "object",
      "properties": {
        "transport": {
          "type": "string"
        },
        "from": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "to": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "geometry": {
          "type": "object",
          "properties": {
            "coordinates": {
              "type": "any"
            },
            "type": {
              "type": "any"
            }
          }
        }
      }
    },
    "bus-10-12": {
      "type": "object",
      "properties": {
        "transport": {
          "type": "string"
        },
        "from": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "to": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "geometry": {
          "type": "object",
          "properties": {
            "coordinates": {
              "type": "any"
            },
            "type": {
              "type": "any"
            }
          }
        }
      }
    },
    "\u00e0 pied-12-13": {
      "type": "object",
      "properties": {
        "transport": {
          "type": "string"
        },
        "from": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "to": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "geometry": {
          "type": "object",
          "properties": {
            "coordinates": {
              "type": "any"
            },
            "type": {
              "type": "any"
            }
          }
        }
      }
    },
    "\u00e0 pied-13-15": {
      "type": "object",
      "properties": {
        "transport": {
          "type": "string"
        },
        "from": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "to": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "geometry": {
          "type": "object",
          "properties": {
            "coordinates": {
              "type": "any"
            },
            "type": {
              "type": "any"
            }
          }
        }
      }
    },
    "\u00e0 pied-15-16": {
      "type": "object",
      "properties": {
        "transport": {
          "type": "string"
        },
        "from": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "to": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "geometry": {
          "type": "object",
          "properties": {
            "coordinates": {
              "type": "any"
            },
            "type": {
              "type": "any"
            }
          }
        }
      }
    },
    "bus-16-19": {
      "type": "object",
      "properties": {
        "transport": {
          "type": "string"
        },
        "from": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "to": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "geometry": {
          "type": "object",
          "properties": {
            "coordinates": {
              "type": "any"
            },
            "type": {
              "type": "any"
            }
          }
        }
      }
    },
    "bus-19-20": {
      "type": "object",
      "properties": {
        "transport": {
          "type": "string"
        },
        "from": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "to": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "geometry": {
          "type": "object",
          "properties": {
            "coordinates": {
              "type": "any"
            },
            "type": {
              "type": "any"
            }
          }
        }
      }
    },
    "bus-20-21": {
      "type": "object",
      "properties": {
        "transport": {
          "type": "string"
        },
        "from": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "to": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "geometry": {
          "type": "object",
          "properties": {
            "coordinates": {
              "type": "any"
            },
            "type": {
              "type": "any"
            }
          }
        }
      }
    },
    "bus-21-22": {
      "type": "object",
      "properties": {
        "transport": {
          "type": "string"
        },
        "from": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "to": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "geometry": {
          "type": "object",
          "properties": {
            "coordinates": {
              "type": "any"
            },
            "type": {
              "type": "any"
            }
          }
        }
      }
    },
    "van-22-23": {
      "type": "object",
      "properties": {
        "transport": {
          "type": "string"
        },
        "from": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "to": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "geometry": {
          "type": "object",
          "properties": {
            "coordinates": {
              "type": "any"
            },
            "type": {
              "type": "any"
            }
          }
        }
      }
    },
    "bus-23-24": {
      "type": "object",
      "properties": {
        "transport": {
          "type": "string"
        },
        "from": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "to": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "geometry": {
          "type": "object",
          "properties": {
            "coordinates": {
              "type": "any"
            },
            "type": {
              "type": "any"
            }
          }
        }
      }
    },
    "bus-24-25": {
      "type": "object",
      "properties": {
        "transport": {
          "type": "string"
        },
        "from": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "to": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "geometry": {
          "type": "object",
          "properties": {
            "coordinates": {
              "type": "any"
            },
            "type": {
              "type": "any"
            }
          }
        }
      }
    },
    "bus-25-27": {
      "type": "object",
      "properties": {
        "transport": {
          "type": "string"
        },
        "from": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "to": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "geometry": {
          "type": "object",
          "properties": {
            "coordinates": {
              "type": "any"
            },
            "type": {
              "type": "any"
            }
          }
        }
      }
    },
    "bus-27-28": {
      "type": "object",
      "properties": {
        "transport": {
          "type": "string"
        },
        "from": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "to": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "ville": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lng": {
              "type": "any"
            }
          }
        },
        "geometry": {
          "type": "object",
          "properties": {
            "coordinates": {
              "type": "any"
            },
            "type": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `GET` /planet
```json
{
  "type": "object",
  "properties": {
    "tilejson": {
      "type": "string"
    },
    "tiles": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "vector_layers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "fields": {
            "type": "any"
          },
          "minzoom": {
            "type": "any"
          },
          "maxzoom": {
            "type": "any"
          }
        }
      }
    },
    "attribution": {
      "type": "string"
    },
    "bounds": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "center": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "description": {
      "type": "string"
    },
    "maxzoom": {
      "type": "number"
    },
    "minzoom": {
      "type": "number"
    },
    "name": {
      "type": "string"
    },
    "version": {
      "type": "string"
    }
  }
}
```

