---
title: "APIs & Protocols: www-rosshalfin-com"
date: 2026-11-14
target: "[[overview|www-rosshalfin-com]]"
---

# Discovered APIs & Protocols: www-rosshalfin-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/cdn-cgi/speculation` | `200` | REST endpoint |
| `GET` | `/wp-json/complianz/v1/banner` | `200` | REST endpoint |
| `GET` | `/` | `200` | REST endpoint |
| `POST` | `/` | `200` | REST endpoint |
| `GET` | `/v3/controller-with-preconnect-aaa82383600f40249fd1931c20e2df23.html` | `200` | REST endpoint |
| `GET` | `/v3/fingerprinted/js/shared-7aaeb02320f7b259f99fcb22c093f0f5.js` | `200` | REST endpoint |
| `GET` | `/v3/fingerprinted/js/controller-with-preconnect-1b34fb120f6e8f2058d662c8ad77fd4d.js` | `200` | REST endpoint |
| `GET` | `/v3/.deploy_status_henson.json` | `200` | REST endpoint |
| `GET` | `/v3/fingerprinted/js/stripe-cookies-342e5a3c90613ebd49e7001b6682f9f8.js` | `200` | REST endpoint |
| `GET` | `/v3/.deploy_status_henson.json` | `200` | REST endpoint |
| `GET` | `/v3/fingerprinted/js/consumerSchema-83a22fb235852a7ced5e094bc777e12f.js` | `200` | REST endpoint |
| `GET` | `/v3/.deploy_status_henson.json` | `200` | REST endpoint |
| `GET` | `/v1/elements/sessions` | `200` | REST endpoint |
| `GET` | `/v3/fingerprinted/js/elements-inner-accessory-render-b8528ea4fd51f48b7a08e9886c1dfbe0.js` | `200` | REST endpoint |
| `GET` | `/link/get-cookie` | `200` | REST endpoint |
| `GET` | `/v3/m-outer-0edadf75b42c6ef7240c043f3272f3f9.html` | `200` | REST endpoint |
| `POST` | `/cdn-cgi/rum` | `204` | REST endpoint |
| `POST` | `/xoplatform/logger/api/logger` | `-1` | REST endpoint |
| `POST` | `/xoplatform/logger/api/logger` | `200` | REST endpoint |
| `GET` | `/v3/fingerprinted/js/m-outer-df5ee3b49f88025f22168cdfc5823764.js` | `200` | REST endpoint |
| `POST` | `/6` | `200` | REST endpoint |
| `POST` | `/recaptcha/api2/reload` | `200` | REST endpoint |
| `GET` | `/v3/hcaptcha-invisible-cd8f1521e69d2758c2c76ef4dad27aab.html` | `200` | REST endpoint |
| `GET` | `/captcha/v1/221126bfaff10f69f5e2c60a7ff42e4b9f16aed7/static/hcaptcha.html` | `200` | REST endpoint |
| `GET` | `/captcha/v1/221126bfaff10f69f5e2c60a7ff42e4b9f16aed7/static/hcaptcha.html` | `200` | REST endpoint |
| `GET` | `/captcha/v1/221126bfaff10f69f5e2c60a7ff42e4b9f16aed7/static/hcaptcha.html` | `200` | REST endpoint |
| `GET` | `/captcha/v1/221126bfaff10f69f5e2c60a7ff42e4b9f16aed7/static/hcaptcha.html` | `200` | REST endpoint |
| `POST` | `/checksiteconfig` | `200` | REST endpoint |
| `POST` | `/6` | `200` | REST endpoint |
| `POST` | `/6` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /cdn-cgi/speculation
```json
{
  "type": "object",
  "properties": {
    "tag": {
      "type": "string"
    },
    "prefetch": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "eagerness": {
            "type": "any"
          },
          "source": {
            "type": "any"
          },
          "where": {
            "type": "any"
          }
        }
      }
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
### `GET` /
```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "number"
    },
    "nonce": {
      "type": "string"
    },
    "state": {
      "type": "number"
    }
  }
}
```
### `POST` /
```json
{
  "type": "object",
  "properties": {
    "fragments": {
      "type": "object",
      "properties": {
        "div.widget_shopping_cart_content": {
          "type": "string"
        },
        "wc_stripe_data": {
          "type": "object",
          "properties": {
            "cart": {
              "type": "any"
            }
          }
        },
        "div.shoptimizer-cart": {
          "type": "string"
        }
      }
    },
    "cart_hash": {
      "type": "string"
    }
  }
}
```
### `GET` /v3/.deploy_status_henson.json
```json
{
  "type": "object",
  "properties": {
    "canaryPercentage": {
      "type": "number"
    },
    "deployedRevisions": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  }
}
```
### `GET` /v3/.deploy_status_henson.json
```json
{
  "type": "object",
  "properties": {
    "canaryPercentage": {
      "type": "number"
    },
    "deployedRevisions": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  }
}
```

