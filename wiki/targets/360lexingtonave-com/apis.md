---
title: "APIs & Protocols: 360lexingtonave-com"
date: 2026-11-14
target: "360lexingtonave-com"
---

# Discovered APIs & Protocols: 360lexingtonave-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/px/` | `200` | REST endpoint |
| `POST` | `/sdk/get_info` | `200` | REST endpoint |
| `POST` | `/sdk/user/add_properties` | `200` | REST endpoint |
| `POST` | `/sdk/event/track` | `200` | REST endpoint |
| `POST` | `/sdk/user/add_properties` | `200` | REST endpoint |
| `POST` | `/sdk/user/add_properties` | `200` | REST endpoint |
| `POST` | `/sdk/user/add_properties` | `200` | REST endpoint |
| `GET` | `/pixel/ip-info` | `200` | REST endpoint |
| `GET` | `/pixel/0d43e7a4-79b6-4d33-8b60-9ace73ecaa0c/settings` | `200` | REST endpoint |
| `POST` | `/pixel/0d43e7a4-79b6-4d33-8b60-9ace73ecaa0c/new-visitor` | `201` | REST endpoint |
| `GET` | `/pixel/phoenix/rp/j` | `200` | REST endpoint |
| `POST` | `/pixel/li` | `200` | REST endpoint |
| `POST` | `/sdk/event/update_properties` | `200` | REST endpoint |
| `POST` | `/anonymous` | `200` | REST endpoint |
| `GET` | `/auth/web/access-token` | `200` | REST endpoint |
| `POST` | `/sdk/event/update_properties` | `200` | REST endpoint |
| `POST` | `/pixel/0d43e7a4-79b6-4d33-8b60-9ace73ecaa0c/visitor/36612af8-eed3-4ff2-8217-2f47e7b40aa0/cerebro` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /px/
```json
{
  "type": "object",
  "properties": {
    "visitor_id": {
      "type": "string"
    }
  }
}
```
### `POST` /sdk/get_info
```json
{
  "type": "object",
  "properties": {
    "auto_track": {
      "type": "boolean"
    },
    "auto_track_spa_page_view": {
      "type": "boolean"
    },
    "auto_form_capture": {
      "type": "boolean"
    },
    "auto_click_capture": {
      "type": "boolean"
    },
    "exclude_bot": {
      "type": "boolean"
    },
    "auto_capture_form_fills": {
      "type": "boolean"
    },
    "int_drift": {
      "type": "boolean"
    },
    "int_clear_bit": {
      "type": "boolean"
    },
    "int_client_six_signal_key": {
      "type": "null"
    },
    "int_factors_six_signal_key": {
      "type": "null"
    },
    "user_id": {
      "type": "string"
    },
    "int_sdk_data_layer": {
      "type": "boolean"
    },
    "google_abm_conversion_id": {
      "type": "null"
    },
    "google_abm_enabled": {
      "type": "boolean"
    }
  }
}
```
### `POST` /sdk/user/add_properties
```json
{
  "type": "object",
  "properties": {
    "message": {
      "type": "string"
    }
  }
}
```
### `POST` /sdk/event/track
```json
{
  "type": "object",
  "properties": {
    "event_id": {
      "type": "string"
    },
    "message": {
      "type": "string"
    }
  }
}
```
### `POST` /sdk/user/add_properties
```json
{
  "type": "object",
  "properties": {
    "message": {
      "type": "string"
    }
  }
}
```
### `POST` /sdk/user/add_properties
```json
{
  "type": "object",
  "properties": {
    "message": {
      "type": "string"
    }
  }
}
```
### `POST` /sdk/user/add_properties
```json
{
  "type": "object",
  "properties": {
    "message": {
      "type": "string"
    }
  }
}
```
### `GET` /pixel/ip-info
```json
{
  "type": "object",
  "properties": {
    "ipInfo": {
      "type": "object",
      "properties": {
        "as": {
          "type": "string"
        },
        "city": {
          "type": "string"
        },
        "country": {
          "type": "string"
        },
        "countryCode": {
          "type": "string"
        },
        "isp": {
          "type": "string"
        },
        "lat": {
          "type": "number"
        },
        "lon": {
          "type": "number"
        },
        "org": {
          "type": "string"
        },
        "query": {
          "type": "string"
        },
        "region": {
          "type": "string"
        },
        "regionName": {
          "type": "string"
        },
        "status": {
          "type": "string"
        },
        "timezone": {
          "type": "string"
        },
        "zip": {
          "type": "string"
        }
      }
    },
    "isCloudProvider": {
      "type": "boolean"
    }
  }
}
```
### `GET` /pixel/0d43e7a4-79b6-4d33-8b60-9ace73ecaa0c/settings
```json
{
  "type": "object",
  "properties": {
    "pixelUseCerebroWaterfall": {
      "type": "boolean"
    },
    "pixelNonUsIpCompanyLookup": {
      "type": "boolean"
    },
    "pixelNonUsVisitors": {
      "type": "string"
    },
    "pixelNonUsIpCompanyLookupEnabled": {
      "type": "boolean"
    },
    "tartarus": {
      "type": "boolean"
    },
    "pixelMode": {
      "type": "string"
    }
  }
}
```
### `POST` /pixel/0d43e7a4-79b6-4d33-8b60-9ace73ecaa0c/new-visitor
```json
{
  "type": "object",
  "properties": {
    "visitor": {
      "type": "object",
      "properties": {
        "id": {
          "type": "number"
        },
        "uuid": {
          "type": "string"
        },
        "created_at": {
          "type": "string"
        },
        "org": {
          "type": "number"
        },
        "ip_info": {
          "type": "object",
          "properties": {
            "as": {
              "type": "any"
            },
            "isp": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lon": {
              "type": "any"
            },
            "org": {
              "type": "any"
            },
            "zip": {
              "type": "any"
            },
            "city": {
              "type": "any"
            },
            "query": {
              "type": "any"
            },
            "region": {
              "type": "any"
            },
            "status": {
              "type": "any"
            },
            "country": {
              "type": "any"
            },
            "timezone": {
              "type": "any"
            },
            "regionName": {
              "type": "any"
            },
            "countryCode": {
              "type": "any"
            }
          }
        },
        "first_name": {
          "type": "null"
        },
        "last_name": {
          "type": "null"
        },
        "email": {
          "type": "null"
        },
        "title": {
          "type": "null"
        },
        "company_name": {
          "type": "null"
        },
        "company_domain": {
          "type": "null"
        },
        "linkedin_url": {
          "type": "null"
        },
        "mobile_phone": {
          "type": "null"
        },
        "fbf_cc_id": {
          "type": "null"
        },
        "fbf_up_id": {
          "type": "null"
        },
        "pdl_id": {
          "type": "null"
        },
        "hem2upid_attempted_at": {
          "type": "null"
        },
        "is_us_geo": {
          "type": "boolean"
        },
        "ip2company_attempted_at": {
          "type": "null"
        },
        "company_linkedin_url": {
          "type": "null"
        }
      }
    },
    "activity": {
      "type": "object",
      "properties": {
        "id": {
          "type": "number"
        },
        "page_url": {
          "type": "string"
        },
        "page_title": {
          "type": "string"
        },
        "created_at": {
          "type": "string"
        },
        "visitor_uuid": {
          "type": "string"
        },
        "page_path": {
          "type": "string"
        },
        "utm_source": {
          "type": "string"
        },
        "utm_medium": {
          "type": "string"
        },
        "utm_campaign": {
          "type": "string"
        },
        "utm_term": {
          "type": "string"
        },
        "utm_content": {
          "type": "string"
        },
        "org": {
          "type": "number"
        },
        "referrer": {
          "type": "string"
        },
        "ip_info": {
          "type": "object",
          "properties": {
            "as": {
              "type": "any"
            },
            "isp": {
              "type": "any"
            },
            "lat": {
              "type": "any"
            },
            "lon": {
              "type": "any"
            },
            "org": {
              "type": "any"
            },
            "zip": {
              "type": "any"
            },
            "city": {
              "type": "any"
            },
            "query": {
              "type": "any"
            },
            "region": {
              "type": "any"
            },
            "status": {
              "type": "any"
            },
            "country": {
              "type": "any"
            },
            "timezone": {
              "type": "any"
            },
            "regionName": {
              "type": "any"
            },
            "countryCode": {
              "type": "any"
            }
          }
        },
        "user_agent": {
          "type": "string"
        },
        "vector_campaign": {
          "type": "string"
        },
        "vector_id": {
          "type": "string"
        },
        "vector_source": {
          "type": "string"
        },
        "utm_id": {
          "type": "string"
        }
      }
    }
  }
}
```

