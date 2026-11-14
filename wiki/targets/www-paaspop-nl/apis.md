---
title: "APIs & Protocols: www-paaspop-nl"
date: 2026-11-14
target: "[[overview|www-paaspop-nl]]"
---

# Discovered APIs & Protocols: www-paaspop-nl

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/consentconfig/994dc602-4dc7-4362-a73b-59692ade5124/settings.json` | `200` | REST endpoint |
| `GET` | `/widget/config` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /consentconfig/994dc602-4dc7-4362-a73b-59692ade5124/settings.json
```json
{
  "type": "object",
  "properties": {
    "widget": {
      "type": "object",
      "properties": {
        "enabled": {
          "type": "boolean"
        },
        "position": {
          "type": "object",
          "properties": {
            "position": {
              "type": "any"
            },
            "distanceVerticalPx": {
              "type": "any"
            },
            "distanceHorizontalPx": {
              "type": "any"
            }
          }
        },
        "theme": {
          "type": "object",
          "properties": {
            "closed": {
              "type": "any"
            },
            "opened": {
              "type": "any"
            }
          }
        },
        "content": {
          "type": "object",
          "properties": {
            "cultures": {
              "type": "any"
            },
            "default": {
              "type": "any"
            },
            "autodetectLanguage": {
              "type": "any"
            }
          }
        }
      }
    },
    "twipla": {
      "type": "null"
    }
  }
}
```
### `GET` /widget/config
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "websocket_url": {
      "type": "string"
    },
    "wa_me_url": {
      "type": "string"
    },
    "whatsapp_popup_text": {
      "type": "string"
    },
    "agent_name": {
      "type": "string"
    },
    "persona": {
      "type": "string"
    },
    "theme_color": {
      "type": "string"
    },
    "text_color": {
      "type": "string"
    },
    "suggestion_button_text_color": {
      "type": "string"
    },
    "logo": {
      "type": "string"
    },
    "button_logo": {
      "type": "null"
    },
    "opening_message": {
      "type": "string"
    },
    "button_message": {
      "type": "string"
    },
    "input_placeholder_text": {
      "type": "string"
    },
    "suggestions": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "title": {
            "type": "any"
          }
        }
      }
    },
    "open_on_paths": {
      "type": "array",
      "items": "any"
    },
    "disabled_on_paths": {
      "type": "array",
      "items": "any"
    },
    "widget_location": {
      "type": "string"
    },
    "margin_bottom_px": {
      "type": "null"
    },
    "margin_left_px": {
      "type": "null"
    }
  }
}
```

