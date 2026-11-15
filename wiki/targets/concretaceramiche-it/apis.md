---
title: "APIs & Protocols: concretaceramiche-it"
date: 2026-11-14
target: "concretaceramiche-it"
---

# Discovered APIs & Protocols: concretaceramiche-it

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/wp-json/wc/store/v1/cart` | `200` | REST endpoint |
| `GET` | `/wp-json/complianz/v1/banner` | `200` | REST endpoint |
| `POST` | `/recaptcha/api2/reload` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /wp-json/wc/store/v1/cart
```json
{
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "items": "any"
    },
    "coupons": {
      "type": "array",
      "items": "any"
    },
    "fees": {
      "type": "array",
      "items": "any"
    },
    "totals": {
      "type": "object",
      "properties": {
        "total_items": {
          "type": "string"
        },
        "total_items_tax": {
          "type": "string"
        },
        "total_fees": {
          "type": "string"
        },
        "total_fees_tax": {
          "type": "string"
        },
        "total_discount": {
          "type": "string"
        },
        "total_discount_tax": {
          "type": "string"
        },
        "total_shipping": {
          "type": "null"
        },
        "total_shipping_tax": {
          "type": "null"
        },
        "total_price": {
          "type": "string"
        },
        "total_tax": {
          "type": "string"
        },
        "tax_lines": {
          "type": "array",
          "items": "any"
        },
        "currency_code": {
          "type": "string"
        },
        "currency_symbol": {
          "type": "string"
        },
        "currency_minor_unit": {
          "type": "number"
        },
        "currency_decimal_separator": {
          "type": "string"
        },
        "currency_thousand_separator": {
          "type": "string"
        },
        "currency_prefix": {
          "type": "string"
        },
        "currency_suffix": {
          "type": "string"
        }
      }
    },
    "shipping_address": {
      "type": "object",
      "properties": {
        "first_name": {
          "type": "string"
        },
        "last_name": {
          "type": "string"
        },
        "company": {
          "type": "string"
        },
        "address_1": {
          "type": "string"
        },
        "address_2": {
          "type": "string"
        },
        "city": {
          "type": "string"
        },
        "state": {
          "type": "string"
        },
        "postcode": {
          "type": "string"
        },
        "country": {
          "type": "string"
        },
        "phone": {
          "type": "string"
        },
        "concreta/codice-fiscale": {
          "type": "string"
        }
      }
    },
    "billing_address": {
      "type": "object",
      "properties": {
        "first_name": {
          "type": "string"
        },
        "last_name": {
          "type": "string"
        },
        "company": {
          "type": "string"
        },
        "address_1": {
          "type": "string"
        },
        "address_2": {
          "type": "string"
        },
        "city": {
          "type": "string"
        },
        "state": {
          "type": "string"
        },
        "postcode": {
          "type": "string"
        },
        "country": {
          "type": "string"
        },
        "email": {
          "type": "string"
        },
        "phone": {
          "type": "string"
        },
        "concreta/codice-fiscale": {
          "type": "string"
        }
      }
    },
    "needs_payment": {
      "type": "boolean"
    },
    "needs_shipping": {
      "type": "boolean"
    },
    "payment_requirements": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "has_calculated_shipping": {
      "type": "boolean"
    },
    "shipping_rates": {
      "type": "array",
      "items": "any"
    },
    "items_count": {
      "type": "number"
    },
    "items_weight": {
      "type": "number"
    },
    "cross_sells": {
      "type": "array",
      "items": "any"
    },
    "errors": {
      "type": "array",
      "items": "any"
    },
    "payment_methods": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "extensions": {
      "type": "object",
      "properties": {}
    }
  }
}
```
### `GET` /wp-json/complianz/v1/banner
```json
{
  "type": "object",
  "properties": {
    "consenttype": {
      "type": "string"
    },
    "region": {
      "type": "string"
    },
    "version": {
      "type": "string"
    },
    "forceEnableStats": {
      "type": "boolean"
    },
    "banner_version": {
      "type": "string"
    }
  }
}
```

