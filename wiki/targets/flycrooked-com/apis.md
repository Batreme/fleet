---
title: "APIs & Protocols: flycrooked-com"
date: 2026-11-14
target: "flycrooked-com"
---

# Discovered APIs & Protocols: flycrooked-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/cdn-cgi/rum` | `204` | REST endpoint |
| `GET` | `/entrypoint_config` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

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

