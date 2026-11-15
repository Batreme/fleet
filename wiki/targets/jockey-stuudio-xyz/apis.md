---
title: "APIs & Protocols: jockey-stuudio-xyz"
date: 2026-11-14
target: "jockey-stuudio-xyz"
---

# Discovered APIs & Protocols: jockey-stuudio-xyz

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/v1/video/demo/piccadilly-night.mp4` | `200` | REST endpoint |
| `GET` | `/v1/video/footer/footer-clip.mp4` | `200` | REST endpoint |
| `GET` | `/v1/video/demo/piccadilly-night.mp4` | `200` | REST endpoint |
| `GET` | `/pixels/a2_gyliz4afueyh/config` | `200` | REST endpoint |
| `POST` | `/v1/initialize` | `200` | REST endpoint |
| `POST` | `/v1/rgstr` | `202` | REST endpoint |
| `GET` | `/v2/20253029/banner.js` | `200` | REST endpoint |
| `POST` | `/v1/rgstr` | `202` | REST endpoint |
| `POST` | `/v1/initialize` | `200` | REST endpoint |
| `POST` | `/events` | `200` | REST endpoint |
| `GET` | `/hs-script-loader-public/v2/config/pixels-and-events/json` | `200` | REST endpoint |
| `GET` | `/livechat-public/v1/message/public` | `200` | REST endpoint |
| `GET` | `/collected-forms/v1/config/json` | `200` | REST endpoint |
| `POST` | `/v1/rgstr` | `-1` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /pixels/a2_gyliz4afueyh/config
```json
{
  "type": "object",
  "properties": {
    "aam": {
      "type": "object",
      "properties": {
        "email": {
          "type": "boolean"
        }
      }
    },
    "esc": {
      "type": "object",
      "properties": {
        "page_metadata": {
          "type": "boolean"
        }
      }
    }
  }
}
```
### `POST` /v1/initialize
```json
{
  "type": "object",
  "properties": {
    "feature_gates": {
      "type": "object",
      "properties": {}
    },
    "dynamic_configs": {
      "type": "object",
      "properties": {
        "1833265777": {
          "type": "object",
          "properties": {
            "name": {
              "type": "any"
            },
            "value": {
              "type": "any"
            },
            "rule_id": {
              "type": "any"
            },
            "group": {
              "type": "any"
            },
            "group_name": {
              "type": "any"
            },
            "is_device_based": {
              "type": "any"
            },
            "id_type": {
              "type": "any"
            },
            "is_experiment_active": {
              "type": "any"
            },
            "is_user_in_experiment": {
              "type": "any"
            },
            "secondary_exposures": {
              "type": "any"
            }
          }
        },
        "2273961308": {
          "type": "object",
          "properties": {
            "name": {
              "type": "any"
            },
            "value": {
              "type": "any"
            },
            "rule_id": {
              "type": "any"
            },
            "group": {
              "type": "any"
            },
            "is_device_based": {
              "type": "any"
            },
            "id_type": {
              "type": "any"
            },
            "is_experiment_active": {
              "type": "any"
            },
            "is_user_in_experiment": {
              "type": "any"
            },
            "secondary_exposures": {
              "type": "any"
            }
          }
        },
        "2551237796": {
          "type": "object",
          "properties": {
            "name": {
              "type": "any"
            },
            "value": {
              "type": "any"
            },
            "rule_id": {
              "type": "any"
            },
            "group": {
              "type": "any"
            },
            "is_device_based": {
              "type": "any"
            },
            "passed": {
              "type": "any"
            },
            "id_type": {
              "type": "any"
            },
            "secondary_exposures": {
              "type": "any"
            }
          }
        },
        "2573114601": {
          "type": "object",
          "properties": {
            "name": {
              "type": "any"
            },
            "value": {
              "type": "any"
            },
            "rule_id": {
              "type": "any"
            },
            "group": {
              "type": "any"
            },
            "is_device_based": {
              "type": "any"
            },
            "id_type": {
              "type": "any"
            },
            "is_experiment_active": {
              "type": "any"
            },
            "is_user_in_experiment": {
              "type": "any"
            },
            "secondary_exposures": {
              "type": "any"
            }
          }
        }
      }
    },
    "layer_configs": {
      "type": "object",
      "properties": {}
    },
    "sdkParams": {
      "type": "object",
      "properties": {}
    },
    "has_updates": {
      "type": "boolean"
    },
    "generator": {
      "type": "string"
    },
    "time": {
      "type": "number"
    },
    "company_lcut": {
      "type": "number"
    },
    "evaluated_keys": {
      "type": "object",
      "properties": {
        "stableID": {
          "type": "string"
        },
        "customIDs": {
          "type": "object",
          "properties": {}
        }
      }
    },
    "hash_used": {
      "type": "string"
    },
    "derived_fields": {
      "type": "object",
      "properties": {
        "ip": {
          "type": "string"
        },
        "country": {
          "type": "string"
        },
        "browserName": {
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
        },
        "browser_name": {
          "type": "string"
        },
        "browser_version": {
          "type": "string"
        },
        "os_name": {
          "type": "string"
        },
        "os_version": {
          "type": "string"
        }
      }
    },
    "hashed_sdk_key_used": {
      "type": "string"
    },
    "can_record_session": {
      "type": "boolean"
    },
    "recording_blocked": {
      "type": "boolean"
    },
    "session_recording_rate": {
      "type": "number"
    },
    "full_checksum": {
      "type": "string"
    }
  }
}
```
### `POST` /v1/rgstr
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

