---
title: "APIs & Protocols: mychess-events"
date: 2026-11-14
target: "mychess-events"
---

# Discovered APIs & Protocols: mychess-events

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/currency/info/en.json` | `200` | REST endpoint |
| `GET` | `/entrypoint_config` | `200` | REST endpoint |
| `GET` | `/api/sponsors/any` | `200` | REST endpoint |
| `GET` | `/ext/partner/settings` | `200` | REST endpoint |
| `GET` | `/ext/partner/flags` | `200` | REST endpoint |
| `GET` | `/getconfig/sodar` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /currency/info/en.json
```json
{
  "type": "object",
  "properties": {
    "meta": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "code": {
            "type": "any"
          },
          "name": {
            "type": "any"
          },
          "sign": {
            "type": "any"
          },
          "format": {
            "type": "any"
          },
          "popular": {
            "type": "any"
          },
          "abbreviation": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /entrypoint_config
```json
{
  "type": "object",
  "properties": {
    "marker": {
      "type": "string"
    },
    "project": {
      "type": "object",
      "properties": {
        "trs": {
          "type": "number"
        },
        "subscribed_brands": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "domain": {
          "type": "string"
        }
      }
    },
    "assets_domain": {
      "type": "string"
    },
    "trace_id": {
      "type": "string"
    },
    "services": {
      "type": "object",
      "properties": {
        "emerald": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            }
          }
        },
        "integration": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            }
          }
        },
        "link_switcher": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            }
          }
        },
        "tooltip": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            }
          }
        }
      }
    },
    "erid_extender_enabled": {
      "type": "boolean"
    },
    "processed_content": {
      "type": "boolean"
    },
    "processed_content_types": {
      "type": "object",
      "properties": {
        "html": {
          "type": "boolean"
        },
        "paragraphs": {
          "type": "boolean"
        }
      }
    },
    "ab_tests": {
      "type": "object",
      "properties": {
        "bb_adblock_show": {
          "type": "string"
        },
        "bb_skip_untrusted_events": {
          "type": "string"
        },
        "global_control": {
          "type": "string"
        },
        "global_control_q3": {
          "type": "string"
        },
        "is_bb_activation_gate": {
          "type": "string"
        },
        "tripcom_cut": {
          "type": "string"
        },
        "tripcom_prediction_replacer": {
          "type": "string"
        }
      }
    },
    "evaluation_id": {
      "type": "string"
    },
    "short_link_domain": {
      "type": "string"
    }
  }
}
```
### `GET` /ext/partner/settings
```json
{
  "type": "object",
  "properties": {
    "aid": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "campaignIDs": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "groupId": {
      "type": "string"
    },
    "lmaSettings": {
      "type": "object",
      "properties": {
        "groupId": {
          "type": "string"
        },
        "domain": {
          "type": "string"
        },
        "deepStruct": {
          "type": "array",
          "items": "any"
        },
        "excludes": {
          "type": "array",
          "items": "any"
        },
        "includes": {
          "type": "array",
          "items": "any"
        },
        "installationMethod": {
          "type": "string"
        },
        "name": {
          "type": "string"
        },
        "campaign": {
          "type": "string"
        },
        "lastActiveAt": {
          "type": "string"
        },
        "status": {
          "type": "string"
        },
        "inline": {
          "type": "object",
          "properties": {
            "excludes": {
              "type": "any"
            },
            "includes": {
              "type": "any"
            },
            "hyperlink": {
              "type": "any"
            }
          }
        },
        "nova": {
          "type": "object",
          "properties": {
            "disabledDevices": {
              "type": "any"
            },
            "disabledMediums": {
              "type": "any"
            },
            "isParticipatingRetail": {
              "type": "any"
            }
          }
        },
        "disableLinkSwap": {
          "type": "boolean"
        }
      }
    },
    "legacyAID": {
      "type": "string"
    },
    "campaignID": {
      "type": "string"
    },
    "isLegacyAID": {
      "type": "boolean"
    },
    "isAlien": {
      "type": "boolean"
    },
    "queryMethod": {
      "type": "string"
    },
    "lmaID": {
      "type": "string"
    },
    "sparkBypass": {
      "type": "object",
      "properties": {
        "blockedHosts": {
          "type": "array",
          "items": "any"
        },
        "blockAll": {
          "type": "boolean"
        }
      }
    },
    "userData": {
      "type": "object",
      "properties": {
        "sessionID": {
          "type": "string"
        },
        "abtest": {
          "type": "object",
          "properties": {
            "testName": {
              "type": "any"
            },
            "isOn": {
              "type": "any"
            },
            "version": {
              "type": "any"
            },
            "weight": {
              "type": "any"
            }
          }
        },
        "fpType": {
          "type": "string"
        },
        "conMeth": {
          "type": "null"
        },
        "isBot": {
          "type": "boolean"
        },
        "isBotLight": {
          "type": "boolean"
        },
        "countryCode": {
          "type": "string"
        },
        "ip": {
          "type": "string"
        },
        "hip22": {
          "type": "string"
        },
        "isIPv4": {
          "type": "boolean"
        },
        "lang": {
          "type": "string"
        },
        "fullUserLang": {
          "type": "string"
        },
        "langShort": {
          "type": "string"
        },
        "userLangShort": {
          "type": "string"
        },
        "officialLang": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "browserName": {
          "type": "string"
        },
        "browserType": {
          "type": "string"
        },
        "browserVersion": {
          "type": "string"
        },
        "osName": {
          "type": "string"
        },
        "osVersion": {
          "type": "string"
        }
      }
    },
    "adStack": {
      "type": "null"
    },
    "canRoam": {
      "type": "boolean"
    },
    "disableHyperlink": {
      "type": "boolean"
    },
    "disableLinkSwap": {
      "type": "boolean"
    },
    "disablePop": {
      "type": "boolean"
    },
    "disableWidgets": {
      "type": "boolean"
    },
    "excludes": {
      "type": "array",
      "items": "any"
    }
  }
}
```
### `GET` /ext/partner/flags
```json
{
  "type": "object",
  "properties": {
    "flags": {
      "type": "object",
      "properties": {
        "novaConsentTrap": {
          "type": "boolean"
        },
        "intentTiming": {
          "type": "boolean"
        },
        "sparkGalleryWidget": {
          "type": "boolean"
        },
        "sparkGalleryCtaColor": {
          "type": "boolean"
        },
        "pageHotels": {
          "type": "boolean"
        }
      }
    },
    "assignments": {
      "type": "object",
      "properties": {}
    },
    "sessionID": {
      "type": "string"
    }
  }
}
```
### `GET` /getconfig/sodar
```json
{
  "type": "object",
  "properties": {
    "sodar_query_id": {
      "type": "string"
    },
    "injector_basename": {
      "type": "string"
    },
    "bg_hash_basename": {
      "type": "string"
    },
    "bg_binary": {
      "type": "string"
    },
    "rc_enable": {
      "type": "string"
    },
    "bg_snapshot_delay_ms": {
      "type": "string"
    },
    "is_gen_204": {
      "type": "string"
    }
  }
}
```

