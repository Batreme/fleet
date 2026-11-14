---
title: "APIs & Protocols: aqualoqa-com"
date: 2026-11-14
target: "[[overview|aqualoqa-com]]"
---

# Discovered APIs & Protocols: aqualoqa-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/cdn/shopifycloud/storefront/assets/storefront/horizon.specrules-5654ba2e.json` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/loader.init-shop-cart-sync.en.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/client.init-shop-cart-sync_B_uppJgi.en.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/chunk.document_DMcRsBXN.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/chunk.window_CAbVMZox.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/chunk.init_C-ooJD99.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/chunk.register_CWAkTP1C.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/chunk.networkErrorMessages_Du380vAr.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/client.shop-cart-sync_BkYDJPZz.en.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/chunk.defineInitFunction_DyjeAYT_.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/chunk.casing_U_9x-Om3.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/chunk.v4_C3N_0s0v.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/chunk.utils_Cjeq_SSZ.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/chunk.useUserRecognitionSignal_D_xRcsqT.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/chunk.storage_n5jjEbMM.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/chunk.hooks_hUU__FPJ.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/chunk.authorize_DINGMyE5.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/chunk.useEventListener_DWE4XdI5.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/chunk.validators_BbO3UEjF.esm.js` | `200` | REST endpoint |
| `POST` | `/v1/metrics` | `200` | REST endpoint |
| `POST` | `/api/collect` | `204` | REST endpoint |
| `POST` | `/v1/metrics` | `200` | REST endpoint |
| `POST` | `/v1/metrics` | `200` | REST endpoint |
| `POST` | `/api/collect` | `204` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/chunk.reportAssetMetrics_DatZfDzQ.esm.js` | `200` | REST endpoint |
| `POST` | `/v1/metrics` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /cdn/shopifycloud/storefront/assets/storefront/horizon.specrules-5654ba2e.json
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
          "where": {
            "type": "any"
          },
          "eagerness": {
            "type": "any"
          }
        }
      }
    }
  }
}
```

