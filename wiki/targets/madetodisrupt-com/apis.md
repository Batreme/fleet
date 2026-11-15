---
title: "APIs & Protocols: madetodisrupt-com"
date: 2026-11-14
target: "madetodisrupt-com"
---

# Discovered APIs & Protocols: madetodisrupt-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/api/v1/log` | `200` | REST endpoint |
| `GET` | `/client_data/52cf1d3ccb6532b61fd9007f19733339/mI_wRB7a.json` | `200` | REST endpoint |
| `GET` | `/client_data/52cf1d3ccb6532b61fd9007f19733339/config/bwh4acrx.json` | `200` | REST endpoint |
| `GET` | `/client_data/52cf1d3ccb6532b61fd9007f19733339/translations/QyxeKe_c.json` | `200` | REST endpoint |
| `GET` | `/client_data/52cf1d3ccb6532b61fd9007f19733339/audit-table/RuGV1i1L.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /client_data/52cf1d3ccb6532b61fd9007f19733339/mI_wRB7a.json
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "targetBanner": {
        "type": "number"
      },
      "condition": {
        "type": "string"
      }
    }
  }
}
```
### `GET` /client_data/52cf1d3ccb6532b61fd9007f19733339/config/bwh4acrx.json
```json
{
  "type": "object",
  "properties": {
    "reloadOnAccept": {
      "type": "boolean"
    },
    "dataShortCodes": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "key": {
            "type": "any"
          },
          "content": {
            "type": "any"
          },
          "uiTag": {
            "type": "any"
          },
          "type": {
            "type": "any"
          },
          "customTag": {
            "type": "any"
          },
          "attributes": {
            "type": "any"
          },
          "processedHTML": {
            "type": "any"
          }
        }
      }
    },
    "iabDataShortCodes": {
      "type": "array",
      "items": "any"
    },
    "activeLaw": {
      "type": "string"
    },
    "showAuditTable": {
      "type": "boolean"
    },
    "showToggler": {
      "type": "boolean"
    },
    "googleACMEnabled": {
      "type": "boolean"
    },
    "readMore": {
      "type": "object",
      "properties": {
        "status": {
          "type": "boolean"
        },
        "styles": {
          "type": "object",
          "properties": {
            "color": {
              "type": "any"
            },
            "border-color": {
              "type": "any"
            },
            "background-color": {
              "type": "any"
            }
          }
        },
        "type": {
          "type": "string"
        }
      }
    },
    "togglerSwitch": {
      "type": "object",
      "properties": {
        "status": {
          "type": "boolean"
        },
        "styles": {
          "type": "object",
          "properties": {
            "activeColor": {
              "type": "any"
            },
            "inactiveColor": {
              "type": "any"
            }
          }
        }
      }
    },
    "togglerIABSwitch": {
      "type": "object",
      "properties": {
        "status": {
          "type": "boolean"
        },
        "styles": {
          "type": "object",
          "properties": {
            "activeColor": {
              "type": "any"
            },
            "inactiveColor": {
              "type": "any"
            }
          }
        }
      }
    },
    "ccpaSwitch": {
      "type": "object",
      "properties": {
        "status": {
          "type": "boolean"
        },
        "styles": {
          "type": "object",
          "properties": {
            "activeColor": {
              "type": "any"
            },
            "inactiveColor": {
              "type": "any"
            }
          }
        }
      }
    },
    "placeHolder": {
      "type": "object",
      "properties": {
        "status": {
          "type": "boolean"
        },
        "styles": {
          "type": "object",
          "properties": {
            "border-color": {
              "type": "any"
            },
            "background-color": {
              "type": "any"
            },
            "color": {
              "type": "any"
            }
          }
        }
      }
    },
    "togglerIABTab": {
      "type": "object",
      "properties": {
        "status": {
          "type": "boolean"
        },
        "styles": {
          "type": "object",
          "properties": {
            "activeColor": {
              "type": "any"
            },
            "inactiveColor": {
              "type": "any"
            }
          }
        }
      }
    },
    "html": {
      "type": "string"
    },
    "css": {
      "type": "string"
    },
    "defaultLanguage": {
      "type": "string"
    },
    "bannerType": {
      "type": "string"
    },
    "respectGPC": {
      "type": "boolean"
    },
    "iabEnabled": {
      "type": "boolean"
    },
    "scriptExpiry": {
      "type": "string"
    }
  }
}
```
### `GET` /client_data/52cf1d3ccb6532b61fd9007f19733339/translations/QyxeKe_c.json
```json
{
  "type": "object",
  "properties": {
    "cky_notice_title": {
      "type": "string"
    },
    "cky_notice_description": {
      "type": "string"
    },
    "cky_notice_close_label": {
      "type": "string"
    },
    "cky_readmore_text": {
      "type": "string"
    },
    "cky_readmore_privacyLink": {
      "type": "string"
    },
    "cky_revisit_title": {
      "type": "string"
    },
    "cky_video_placeholder_title": {
      "type": "string"
    },
    "cky_accept_text": {
      "type": "string"
    },
    "cky_reject_text": {
      "type": "string"
    },
    "cky_settings_text": {
      "type": "string"
    },
    "cky_preference_title": {
      "type": "string"
    },
    "cky_preference_description": {
      "type": "string"
    },
    "cky_preference_always_enabled": {
      "type": "string"
    },
    "cky_preference_save_text": {
      "type": "string"
    },
    "cky_preference_accept_text": {
      "type": "string"
    },
    "cky_preference_reject_text": {
      "type": "string"
    },
    "cky_preview_save_text": {
      "type": "string"
    },
    "cky_enable_category_label": {
      "type": "string"
    },
    "cky_disable_category_label": {
      "type": "string"
    },
    "cky_preference_close_label": {
      "type": "string"
    }
  }
}
```
### `GET` /client_data/52cf1d3ccb6532b61fd9007f19733339/audit-table/RuGV1i1L.json
```json
{
  "type": "object",
  "properties": {
    "cookies": {
      "type": "object",
      "properties": {
        "elementor": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "wpEmojiSettingsSupports": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "cookieyes-consent": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        }
      }
    },
    "cky_audit_table_empty_text": {
      "type": "string"
    },
    "cky_audit_table_header_id": {
      "type": "string"
    },
    "cky_audit_table_header_duration": {
      "type": "string"
    },
    "cky_audit_table_header_description": {
      "type": "string"
    },
    "cky_preference_necessary_title": {
      "type": "string"
    },
    "cky_preference_necessary_description": {
      "type": "string"
    },
    "cky_preference_functional_title": {
      "type": "string"
    },
    "cky_preference_functional_description": {
      "type": "string"
    },
    "cky_preference_analytics_title": {
      "type": "string"
    },
    "cky_preference_analytics_description": {
      "type": "string"
    },
    "cky_preference_performance_title": {
      "type": "string"
    },
    "cky_preference_performance_description": {
      "type": "string"
    },
    "cky_preference_advertisement_title": {
      "type": "string"
    },
    "cky_preference_advertisement_description": {
      "type": "string"
    }
  }
}
```

