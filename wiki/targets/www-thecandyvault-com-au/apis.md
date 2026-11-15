---
title: "APIs & Protocols: www-thecandyvault-com-au"
date: 2026-11-14
target: "www-thecandyvault-com-au"
---

# Discovered APIs & Protocols: www-thecandyvault-com-au

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/api/v1/bulklog` | `204` | REST endpoint |
| `GET` | `/pages/pages/thunderbolt` | `200` | REST endpoint |
| `GET` | `/pages/pages/thunderbolt` | `200` | REST endpoint |
| `GET` | `/pages/pages/thunderbolt` | `200` | REST endpoint |
| `POST` | `/api/v1/bulklog` | `204` | REST endpoint |
| `GET` | `/pages/pages/thunderbolt` | `200` | REST endpoint |
| `GET` | `/_api/v1/access-tokens` | `200` | REST endpoint |
| `GET` | `/_api/tag-manager/api/v1/tags/sites/d71b7674-fb72-4326-848f-bceab1f6b474` | `200` | REST endpoint |
| `GET` | `/pages/pages/thunderbolt` | `200` | REST endpoint |
| `GET` | `/services/editor-elements/1.15653.0/rb_wixui.thunderbolt.manifest.min.json` | `200` | REST endpoint |
| `GET` | `/services/editor-elements/1.15653.0/rb_dsgnsys.thunderbolt.manifest.min.json` | `200` | REST endpoint |
| `POST` | `/api/v1/bulklog` | `204` | REST endpoint |
| `GET` | `/services/editor-elements/1.15653.0/rb_wixui.corvid.manifest.min.json` | `200` | REST endpoint |
| `GET` | `/services/editor-elements/1.15653.0/rb_dsgnsys.corvid.manifest.min.json` | `200` | REST endpoint |
| `POST` | `/api/v1/bulklog` | `204` | REST endpoint |
| `POST` | `/api/v1/bulklog` | `204` | REST endpoint |
| `GET` | `/pages/pages/thunderbolt` | `200` | REST endpoint |
| `GET` | `/pages/pages/thunderbolt` | `200` | REST endpoint |
| `GET` | `/pages/pages/thunderbolt` | `200` | REST endpoint |
| `GET` | `/pages/pages/thunderbolt` | `200` | REST endpoint |
| `POST` | `/api/v1/bulklog` | `204` | REST endpoint |
| `POST` | `/api/v1/bulklog` | `204` | REST endpoint |
| `GET` | `/services/auto-frontend-modules/1.6238.0/webworker/manifest-worker.min.json` | `200` | REST endpoint |
| `POST` | `/api/v1/bulklog` | `204` | REST endpoint |
| `POST` | `/api/v1/bulklog` | `204` | REST endpoint |
| `POST` | `/api/v1/bulklog` | `204` | REST endpoint |
| `GET` | `/_api/cart-v2/v2/carts/current` | `200` | REST endpoint |
| `GET` | `/_api/ecommerce-settings/v1/ecommerce-settings` | `200` | REST endpoint |
| `POST` | `/api/v1/bulklog` | `204` | REST endpoint |
| `GET` | `/services/wixstores-client-gallery/1.6062.0/assets/locale/gallery/gallery_en.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /pages/pages/thunderbolt
```json
{
  "type": "object",
  "properties": {
    "stateRefs": {
      "type": "object",
      "properties": {}
    },
    "structure": {
      "type": "object",
      "properties": {
        "components": {
          "type": "object",
          "properties": {
            "masterPage": {
              "type": "any"
            },
            "BACKGROUND_GROUP": {
              "type": "any"
            },
            "SCROLL_TO_TOP": {
              "type": "any"
            },
            "SCROLL_TO_BOTTOM": {
              "type": "any"
            },
            "SKIP_TO_CONTENT_BTN": {
              "type": "any"
            },
            "SITE_HEADER": {
              "type": "any"
            },
            "PAGES_CONTAINER": {
              "type": "any"
            },
            "SITE_PAGES": {
              "type": "any"
            },
            "SITE_FOOTER": {
              "type": "any"
            }
          }
        },
        "features": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "siteFeaturesConfigs": {
          "type": "object",
          "properties": {
            "mpaNavigation": {
              "type": "any"
            },
            "pages": {
              "type": "any"
            },
            "reporter": {
              "type": "any"
            },
            "passwordProtectedPage": {
              "type": "any"
            },
            "environmentService": {
              "type": "any"
            },
            "siteLocaleService": {
              "type": "any"
            },
            "translations": {
              "type": "any"
            },
            "pageAnchors": {
              "type": "any"
            },
            "lightbox": {
              "type": "any"
            },
            "stickyToComponent": {
              "type": "any"
            },
            "componentsLoader": {
              "type": "any"
            },
            "ooi": {
              "type": "any"
            },
            "siteMembers": {
              "type": "any"
            },
            "captcha": {
              "type": "any"
            },
            "protectedPages": {
              "type": "any"
            },
            "windowScroll": {
              "type": "any"
            },
            "ooiTpaSharedConfig": {
              "type": "any"
            },
            "tpa": {
              "type": "any"
            },
            "seo": {
              "type": "any"
            },
            "router": {
              "type": "any"
            }
          }
        }
      }
    },
    "props": {
      "type": "object",
      "properties": {
        "scrollRestoration": {
          "type": "object",
          "properties": {
            "shouldRestoreScrollPosition": {
              "type": "any"
            }
          }
        },
        "accessibilityBrowserZoom": {
          "type": "object",
          "properties": {
            "isBuilder": {
              "type": "any"
            },
            "isStudio": {
              "type": "any"
            }
          }
        },
        "domSelectors": {
          "type": "object",
          "properties": {
            "allComponentIds": {
              "type": "any"
            }
          }
        },
        "components": {
          "type": "object",
          "properties": {
            "componentsUnderFoldMap": {
              "type": "any"
            }
          }
        },
        "reporter": {
          "type": "object",
          "properties": {
            "skipPageView": {
              "type": "any"
            }
          }
        },
        "__componentsConfig__": {
          "type": "object",
          "properties": {}
        },
        "render": {
          "type": "object",
          "properties": {
            "compProps": {
              "type": "any"
            }
          }
        }
      }
    },
    "nicknameToCompIdMaps": {
      "type": "object",
      "properties": {}
    }
  }
}
```
### `GET` /pages/pages/thunderbolt
```json
{
  "type": "object",
  "properties": {
    "stateRefs": {
      "type": "object",
      "properties": {
        "comp-kbgakxea_r_comp-kbgajy18": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mu3k9pvx": {
          "type": "object",
          "properties": {
            "reportBi": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mb5540mw": {
          "type": "object",
          "properties": {
            "currentUrl": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mb5540nl1": {
          "type": "object",
          "properties": {
            "editorType": {
              "type": "any"
            },
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mb5540nm5": {
          "type": "object",
          "properties": {
            "reportBi": {
              "type": "any"
            },
            "reducedMotion": {
              "type": "any"
            },
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mb5540no": {
          "type": "object",
          "properties": {
            "setSiteScrollingBlocked": {
              "type": "any"
            },
            "enableCyclicTabbing": {
              "type": "any"
            },
            "disableCyclicTabbing": {
              "type": "any"
            },
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mb5540np4": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-muavojp8": {
          "type": "object",
          "properties": {
            "reportBi": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mb5540nq12": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mb5540nr1": {
          "type": "object",
          "properties": {
            "reportBi": {
              "type": "any"
            },
            "reducedMotion": {
              "type": "any"
            },
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-muf8dldd": {
          "type": "object",
          "properties": {
            "reportBi": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-muf9u48i": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-muf9u48q": {
          "type": "object",
          "properties": {
            "reportBi": {
              "type": "any"
            },
            "reducedMotion": {
              "type": "any"
            },
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-muf9vcyc": {
          "type": "object",
          "properties": {
            "reportBi": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-muf77bg3": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-muf77bg6": {
          "type": "object",
          "properties": {
            "reportBi": {
              "type": "any"
            },
            "reducedMotion": {
              "type": "any"
            },
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-mu3xtrpz": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-mu3xwirr": {
          "type": "object",
          "properties": {
            "reducedMotion": {
              "type": "any"
            },
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-mu59zamz": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-mu3xtrq510": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        }
      }
    },
    "structure": {
      "type": "object",
      "properties": {
        "components": {
          "type": "object",
          "properties": {
            "c1dmp": {
              "type": "any"
            },
            "Containerc1dmp": {
              "type": "any"
            },
            "comp-kbgakxea-pinned-layer": {
              "type": "any"
            },
            "comp-kbgakxea": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-kbgajy18": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-kbgajy18_relative": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-mu3m4vxb": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-mu3m4vxb_relative": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-mu3k9pvx": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-mu3k868h": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-muf9l3p4": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-muf9l3p4_relative": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-mb5540mw": {
              "type": "any"
            },
            "portal-comp-kbgakxea_r_comp-mb5540mw": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-mb5540nl1": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-mb5540nm5": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-mb5540no": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-mb5540np4": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-muavojp8": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-mb5540nq12": {
              "type": "any"
            }
          }
        },
        "features": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "siteFeaturesConfigs": {
          "type": "object",
          "properties": {}
        }
      }
    },
    "props": {
      "type": "object",
      "properties": {
        "landingPage": {
          "type": "object",
          "properties": {
            "isLandingPage": {
              "type": "any"
            }
          }
        },
        "scrollRestoration": {
          "type": "object",
          "properties": {
            "shouldRestoreScrollPosition": {
              "type": "any"
            }
          }
        },
        "accessibilityBrowserZoom": {
          "type": "object",
          "properties": {
            "isBuilder": {
              "type": "any"
            },
            "isStudio": {
              "type": "any"
            }
          }
        },
        "animations": {
          "type": "object",
          "properties": {
            "repeaterTemplateToParentMap": {
              "type": "any"
            },
            "isPreview": {
              "type": "any"
            }
          }
        },
        "pageAnchors": {
          "type": "object",
          "properties": {
            "anchors": {
              "type": "any"
            },
            "pageAnchorsObservers": {
              "type": "any"
            },
            "activeAnchorObservers": {
              "type": "any"
            },
            "headerComponentId": {
              "type": "any"
            },
            "isBuilderComponentModel": {
              "type": "any"
            }
          }
        },
        "menuContainer": {
          "type": "object",
          "properties": {
            "menuContainerConfig": {
              "type": "any"
            },
            "menuTogglesConfig": {
              "type": "any"
            }
          }
        },
        "repeaters": {
          "type": "object",
          "properties": {
            "repeatersData": {
              "type": "any"
            }
          }
        },
        "imagePlaceholder": {
          "type": "object",
          "properties": {
            "staticMediaUrl": {
              "type": "any"
            },
            "isSEOBot": {
              "type": "any"
            },
            "userDomainMediaBaseUrl": {
              "type": "any"
            },
            "userDomainMediaPrefixes": {
              "type": "any"
            }
          }
        },
        "siteMembers": {
          "type": "object",
          "properties": {
            "componentIds": {
              "type": "any"
            }
          }
        },
        "scrollToAnchor": {
          "type": "object",
          "properties": {
            "anchorDataIdToCompIdMap": {
              "type": "any"
            },
            "nicknameToCompIdMap": {
              "type": "any"
            },
            "compsToUpdate": {
              "type": "any"
            },
            "isAnchorsLinksOnPageWithoutTopAndBottom": {
              "type": "any"
            },
            "isBuilderComponentModel": {
              "type": "any"
            },
            "anchorNameToCompIdMap": {
              "type": "any"
            },
            "isResponsive": {
              "type": "any"
            }
          }
        },
        "windowScroll": {
          "type": "object",
          "properties": {
            "headerContainerComponentId": {
              "type": "any"
            }
          }
        },
        "ooi": {
          "type": "object",
          "properties": {
            "ooiComponents": {
              "type": "any"
            },
            "accessibilityEnabled": {
              "type": "any"
            },
            "pagesToShowSosp": {
              "type": "any"
            }
          }
        },
        "tpa": {
          "type": "object",
          "properties": {
            "widgets": {
              "type": "any"
            },
            "tpaGalleriesImageItems": {
              "type": "any"
            },
            "pageId": {
              "type": "any"
            },
            "hasWixTpaOnPage": {
              "type": "any"
            },
            "tpaInnerRouteConfig": {
              "type": "any"
            },
            "appPublicData": {
              "type": "any"
            },
            "isFixedHeader": {
              "type": "any"
            },
            "siteScale": {
              "type": "any"
            }
          }
        },
        "svgLoader": {
          "type": "object",
          "properties": {
            "compIdToSvgDataMap": {
              "type": "any"
            },
            "colorsMap": {
              "type": "any"
            },
            "mediaRootUrl": {
              "type": "any"
            },
            "compIdToVectorArtPropsPaths": {
              "type": "any"
            }
          }
        },
        "seo": {
          "type": "object",
          "properties": {
            "pageId": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "indexPage": {
              "type": "any"
            },
            "ogImage": {
              "type": "any"
            },
            "ogImageHeight": {
              "type": "any"
            },
            "ogImageWidth": {
              "type": "any"
            },
            "pageName": {
              "type": "any"
            },
            "title": {
              "type": "any"
            },
            "advancedSeoData": {
              "type": "any"
            },
            "currentPageUrl": {
              "type": "any"
            },
            "translationsData": {
              "type": "any"
            },
            "tpaPageId": {
              "type": "any"
            },
            "managingAppDefId": {
              "type": "any"
            }
          }
        },
        "menusCurrentPage": {
          "type": "object",
          "properties": {}
        },
        "domSelectors": {
          "type": "object",
          "properties": {
            "allComponentIds": {
              "type": "any"
            }
          }
        },
        "components": {
          "type": "object",
          "properties": {
            "componentsUnderFoldMap": {
              "type": "any"
            }
          }
        },
        "mobileFullScreen": {
          "type": "object",
          "properties": {}
        },
        "siteWixCodeSdk": {
          "type": "object",
          "properties": {
            "pagesData": {
              "type": "any"
            },
            "nonPopupsPagesData": {
              "type": "any"
            },
            "lightboxes": {
              "type": "any"
            }
          }
        }
      }
    },
    "nicknameToCompIdMaps": {
      "type": "object",
      "properties": {}
    }
  }
}
```
### `GET` /pages/pages/thunderbolt
```json
{
  "type": "object",
  "properties": {
    "sdkData": {
      "type": "object",
      "properties": {
        "c1dmp": {
          "type": "object",
          "properties": {
            "currentPageSEODescription": {
              "type": "any"
            },
            "currentPageSEOKeywords": {
              "type": "any"
            },
            "currentUrlPageTitle": {
              "type": "any"
            },
            "visibleInMenu": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mu3m4vxb": {
          "type": "object",
          "properties": {
            "initialSdkStyles": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mu3k9pvx": {
          "type": "object",
          "properties": {
            "isResponsive": {
              "type": "any"
            },
            "svgId": {
              "type": "any"
            },
            "altText": {
              "type": "any"
            },
            "compId": {
              "type": "any"
            },
            "strokeWidth": {
              "type": "any"
            },
            "properties": {
              "type": "any"
            },
            "layout": {
              "type": "any"
            },
            "shadow": {
              "type": "any"
            },
            "colorsMap": {
              "type": "any"
            },
            "overrideColors": {
              "type": "any"
            },
            "mediaSvgUrl": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mu3k868j2": {
          "type": "object",
          "properties": {
            "menuItems": {
              "type": "any"
            },
            "navBarItems": {
              "type": "any"
            },
            "isMobileView": {
              "type": "any"
            },
            "baseSvgMediaUrl": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-muf9l3p4": {
          "type": "object",
          "properties": {
            "initialSdkStyles": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mb5540mw": {
          "type": "object",
          "properties": {
            "pageList": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mb5540nm5": {
          "type": "object",
          "properties": {
            "mediaSvgUrl": {
              "type": "any"
            },
            "svgId": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mb5540nr1": {
          "type": "object",
          "properties": {
            "mediaSvgUrl": {
              "type": "any"
            },
            "svgId": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-muf9u48q": {
          "type": "object",
          "properties": {
            "mediaSvgUrl": {
              "type": "any"
            },
            "svgId": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-muf9vcyc": {
          "type": "object",
          "properties": {
            "isResponsive": {
              "type": "any"
            },
            "svgId": {
              "type": "any"
            },
            "altText": {
              "type": "any"
            },
            "compId": {
              "type": "any"
            },
            "strokeWidth": {
              "type": "any"
            },
            "properties": {
              "type": "any"
            },
            "layout": {
              "type": "any"
            },
            "shadow": {
              "type": "any"
            },
            "colorsMap": {
              "type": "any"
            },
            "overrideColors": {
              "type": "any"
            },
            "mediaSvgUrl": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-muf77bg6": {
          "type": "object",
          "properties": {
            "mediaSvgUrl": {
              "type": "any"
            },
            "svgId": {
              "type": "any"
            }
          }
        },
        "comp-mu3xtrpz": {
          "type": "object",
          "properties": {
            "initialSdkStyles": {
              "type": "any"
            }
          }
        },
        "comp-mu5a715t": {
          "type": "object",
          "properties": {
            "initialSdkStyles": {
              "type": "any"
            }
          }
        },
        "comp-mu41qqkt": {
          "type": "object",
          "properties": {
            "initialSdkStyles": {
              "type": "any"
            }
          }
        },
        "comp-mu59zamz": {
          "type": "object",
          "properties": {
            "linkPropsByHref": {
              "type": "any"
            },
            "shouldAttachSemanticClassNames": {
              "type": "any"
            }
          }
        },
        "comp-mu7x2lsi": {
          "type": "object",
          "properties": {
            "initialSdkStyles": {
              "type": "any"
            }
          }
        },
        "comp-mu3xtrq510": {
          "type": "object",
          "properties": {
            "linkPropsByHref": {
              "type": "any"
            },
            "shouldAttachSemanticClassNames": {
              "type": "any"
            }
          }
        },
        "comp-mu3xtrq610": {
          "type": "object",
          "properties": {
            "mediaSvgUrl": {
              "type": "any"
            },
            "svgId": {
              "type": "any"
            }
          }
        },
        "comp-mu19a2q3": {
          "type": "object",
          "properties": {
            "initialSdkStyles": {
              "type": "any"
            }
          }
        },
        "comp-mu8fu7xk": {
          "type": "object",
          "properties": {
            "initialSdkStyles": {
              "type": "any"
            }
          }
        }
      }
    },
    "isBuilderDocument": {
      "type": "boolean"
    },
    "responsiveCompsInClassic": {
      "type": "object",
      "properties": {}
    },
    "onLoadProperties": {
      "type": "object",
      "properties": {}
    },
    "containersChildrenIds": {
      "type": "object",
      "properties": {
        "c1dmp": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-kbgakxea": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-kbgakxea_r_comp-kbgajy18": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-kbgakxea_r_comp-mu3m4vxb": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-kbgakxea_r_comp-mu3k868h": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-kbgakxea_r_comp-muf9l3p4": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-kbgakxea_r_comp-mb5540mw": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-kbgakxea_r_comp-mb5540nl1": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-kbgakxea_r_comp-mb5540no": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-kbgakxea_r_comp-mb5540np4": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-kbgakxea_r_comp-muf9u48i": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-kbgakxea_r_comp-mb5540ni1": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-kbgakxea_r_comp-muf77bg3": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mu3xtrpz": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mu5a715t": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mu41qqkt": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mu7x2lsi": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mu19a2q3": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mu8fu7xk": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mu8fu7xm1": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    },
    "compIdToRepeaterId": {
      "type": "object",
      "properties": {
        "comp-mu43swhe5": {
          "type": "string"
        },
        "comp-mu80dji2": {
          "type": "string"
        },
        "comp-mu5blq1o": {
          "type": "string"
        },
        "comp-mu43swhn": {
          "type": "string"
        },
        "comp-mu7yyiav": {
          "type": "string"
        },
        "comp-mvj5yi2r9": {
          "type": "string"
        },
        "comp-mvj5yi302": {
          "type": "string"
        },
        "comp-mvj5yi3q": {
          "type": "string"
        },
        "comp-mvj5yi3f": {
          "type": "string"
        },
        "comp-mvj7d6cl": {
          "type": "string"
        }
      }
    },
    "staticEvents": {
      "type": "array",
      "items": "any"
    },
    "ghosts": {
      "type": "object",
      "properties": {
        "structure": {
          "type": "object",
          "properties": {
            "comp-kbgakxea_r_comp-mu3k868h": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-mu3k868j2": {
              "type": "any"
            }
          }
        },
        "props": {
          "type": "object",
          "properties": {
            "comp-kbgakxea_r_comp-mu3k868h": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-mu3k868j2": {
              "type": "any"
            }
          }
        },
        "parentComponentsUpdates": {
          "type": "object",
          "properties": {}
        }
      }
    },
    "slots": {
      "type": "object",
      "properties": {
        "comp-kbgakxea_r_comp-mb5540mw": {
          "type": "object",
          "properties": {
            "f05f7045-dbcb-454d-a442-74d5396fc278": {
              "type": "any"
            }
          }
        },
        "comp-mu93k1t9_r_comp-mu93jvrk8": {
          "type": "object",
          "properties": {
            "f05f7045-dbcb-454d-a442-74d5396fc278": {
              "type": "any"
            }
          }
        },
        "comp-mu93k1t9_r_comp-mu93jvrr6": {
          "type": "object",
          "properties": {
            "f05f7045-dbcb-454d-a442-74d5396fc278": {
              "type": "any"
            }
          }
        }
      }
    },
    "applications": {
      "type": "object",
      "properties": {
        "14cc59bc-f0b7-15b8-e1c7-89ce41d0e0c9": {
          "type": "object",
          "properties": {
            "comp-kbgakxea_r_comp-mu3k868h": {
              "type": "any"
            }
          }
        },
        "1484cb44-49cd-5b39-9681-75188ab429de": {
          "type": "object",
          "properties": {
            "comp-kbgakxea_r_comp-muf9u48i": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-muf77bg3": {
              "type": "any"
            }
          }
        },
        "1380b703-ce81-ff05-f115-39571d94dfcd": {
          "type": "object",
          "properties": {
            "comp-kbgakxea_r_comp-mu3k84ei": {
              "type": "any"
            },
            "comp-muarzsca": {
              "type": "any"
            }
          }
        }
      }
    },
    "connections": {
      "type": "object",
      "properties": {
        "wixCode": {
          "type": "object",
          "properties": {
            "page1": {
              "type": "any"
            },
            "section3": {
              "type": "any"
            },
            "box199": {
              "type": "any"
            },
            "vectorImage12": {
              "type": "any"
            },
            "membersLoginBar1": {
              "type": "any"
            },
            "accountNavBar1": {
              "type": "any"
            },
            "box205": {
              "type": "any"
            },
            "menu5": {
              "type": "any"
            },
            "hamburgerOpenButton5": {
              "type": "any"
            },
            "hamburgerOpenButtonHidden5": {
              "type": "any"
            },
            "hamburgerOverlay5": {
              "type": "any"
            },
            "hamburgerMenuContainer5": {
              "type": "any"
            },
            "imageX4": {
              "type": "any"
            },
            "hamburgerMenuContent5": {
              "type": "any"
            },
            "hamburgerCloseButton5": {
              "type": "any"
            },
            "socialBar2": {
              "type": "any"
            },
            "searchButtonController2": {
              "type": "any"
            },
            "searchButton2": {
              "type": "any"
            },
            "vectorImage15": {
              "type": "any"
            },
            "dropdownContainer5": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mu3k868h": {
          "type": "object",
          "properties": {
            "members-login-bar": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-muf9u48i": {
          "type": "object",
          "properties": {
            "searchButton": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-muf77bg3": {
          "type": "object",
          "properties": {
            "searchButton": {
              "type": "any"
            }
          }
        }
      }
    },
    "compIdConnections": {
      "type": "object",
      "properties": {
        "c1dmp": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-kbgajy18": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mu3m4vxb": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mu3k9pvx": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mu3k868h": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mu3k868j2": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-mu3k868h": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-muf9l3p4": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mb5540mw": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mb5540nl1": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mb5540nm5": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mb5540no": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mb5540np4": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-muavojp8": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mb5540nq12": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mb5540nr1": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-muf8dldd": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-muf9u48i": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-muf9u48q": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-muf9u48i": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-muf9vcyc": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mb5540ni1": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        }
      }
    },
    "orderedControllers": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "controllerConfigs": {
      "type": "object",
      "properties": {
        "14cc59bc-f0b7-15b8-e1c7-89ce41d0e0c9": {
          "type": "object",
          "properties": {
            "comp-kbgakxea_r_comp-mu3k868h": {
              "type": "any"
            }
          }
        },
        "1484cb44-49cd-5b39-9681-75188ab429de": {
          "type": "object",
          "properties": {
            "comp-kbgakxea_r_comp-muf9u48i": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-muf77bg3": {
              "type": "any"
            }
          }
        },
        "1380b703-ce81-ff05-f115-39571d94dfcd": {
          "type": "object",
          "properties": {
            "comp-kbgakxea_r_comp-mu3k84ei": {
              "type": "any"
            },
            "comp-muarzsca": {
              "type": "any"
            }
          }
        }
      }
    },
    "applicationsPublicData": {
      "type": "object",
      "properties": {
        "14cc59bc-f0b7-15b8-e1c7-89ce41d0e0c9": {
          "type": "object",
          "properties": {
            "APP": {
              "type": "any"
            }
          }
        },
        "3c3f3569-205d-4802-9c2d-8e13aaf0d695": {
          "type": "object",
          "properties": {
            "APP": {
              "type": "any"
            }
          }
        },
        "d80111c5-a0f4-47a8-b63a-65b54d774a27": {
          "type": "object",
          "properties": {
            "APP": {
              "type": "any"
            }
          }
        }
      }
    },
    "hasTPAComponentOnPage": {
      "type": "boolean"
    },
    "hasBlocksWidgetOnPage": {
      "type": "boolean"
    },
    "allControllersOnPageAreGhosts": {
      "type": "boolean"
    },
    "sosp": {
      "type": "object",
      "properties": {
        "pagesToShowSosp": {
          "type": "object",
          "properties": {}
        },
        "controllersInSosp": {
          "type": "object",
          "properties": {}
        }
      }
    }
  }
}
```
### `GET` /pages/pages/thunderbolt
```json
{
  "type": "object",
  "properties": {
    "stateRefs": {
      "type": "object",
      "properties": {}
    },
    "structure": {
      "type": "object",
      "properties": {
        "components": {
          "type": "object",
          "properties": {
            "masterPage": {
              "type": "any"
            },
            "BACKGROUND_GROUP": {
              "type": "any"
            },
            "SCROLL_TO_TOP": {
              "type": "any"
            },
            "SCROLL_TO_BOTTOM": {
              "type": "any"
            },
            "SKIP_TO_CONTENT_BTN": {
              "type": "any"
            },
            "SITE_HEADER": {
              "type": "any"
            },
            "PAGES_CONTAINER": {
              "type": "any"
            },
            "SITE_PAGES": {
              "type": "any"
            },
            "SITE_FOOTER": {
              "type": "any"
            }
          }
        },
        "features": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "siteFeaturesConfigs": {
          "type": "object",
          "properties": {
            "mpaNavigation": {
              "type": "any"
            },
            "pages": {
              "type": "any"
            },
            "reporter": {
              "type": "any"
            },
            "passwordProtectedPage": {
              "type": "any"
            },
            "environmentService": {
              "type": "any"
            },
            "siteLocaleService": {
              "type": "any"
            },
            "translations": {
              "type": "any"
            },
            "pageAnchors": {
              "type": "any"
            },
            "lightbox": {
              "type": "any"
            },
            "stickyToComponent": {
              "type": "any"
            },
            "componentsLoader": {
              "type": "any"
            },
            "ooi": {
              "type": "any"
            },
            "siteMembers": {
              "type": "any"
            },
            "captcha": {
              "type": "any"
            },
            "protectedPages": {
              "type": "any"
            },
            "windowScroll": {
              "type": "any"
            },
            "ooiTpaSharedConfig": {
              "type": "any"
            },
            "tpa": {
              "type": "any"
            },
            "seo": {
              "type": "any"
            },
            "router": {
              "type": "any"
            }
          }
        }
      }
    },
    "props": {
      "type": "object",
      "properties": {
        "scrollRestoration": {
          "type": "object",
          "properties": {
            "shouldRestoreScrollPosition": {
              "type": "any"
            }
          }
        },
        "accessibilityBrowserZoom": {
          "type": "object",
          "properties": {
            "isBuilder": {
              "type": "any"
            },
            "isStudio": {
              "type": "any"
            }
          }
        },
        "domSelectors": {
          "type": "object",
          "properties": {
            "allComponentIds": {
              "type": "any"
            }
          }
        },
        "components": {
          "type": "object",
          "properties": {
            "componentsUnderFoldMap": {
              "type": "any"
            }
          }
        },
        "reporter": {
          "type": "object",
          "properties": {
            "skipPageView": {
              "type": "any"
            }
          }
        },
        "__componentsConfig__": {
          "type": "object",
          "properties": {}
        },
        "render": {
          "type": "object",
          "properties": {
            "compProps": {
              "type": "any"
            }
          }
        }
      }
    },
    "nicknameToCompIdMaps": {
      "type": "object",
      "properties": {}
    }
  }
}
```
### `GET` /_api/v1/access-tokens
```json
{
  "type": "object",
  "properties": {
    "hs": {
      "type": "number"
    },
    "visitorId": {
      "type": "string"
    },
    "svSession": {
      "type": "string"
    },
    "ctToken": {
      "type": "string"
    },
    "mediaAuthToken": {
      "type": "string"
    },
    "metaSiteId": {
      "type": "string"
    },
    "apps": {
      "type": "object",
      "properties": {
        "f4d83b06-b408-4f3b-afd4-de8db311d7d8": {
          "type": "object",
          "properties": {
            "instance": {
              "type": "any"
            },
            "intId": {
              "type": "any"
            },
            "accessToken": {
              "type": "any"
            }
          }
        },
        "e593b0bd-b783-45b8-97c2-873d42aacaf4": {
          "type": "object",
          "properties": {
            "instance": {
              "type": "any"
            },
            "intId": {
              "type": "any"
            },
            "accessToken": {
              "type": "any"
            }
          }
        },
        "1052fa8e-e3e2-46dc-ab66-8badb2d08fe9": {
          "type": "object",
          "properties": {
            "instance": {
              "type": "any"
            },
            "intId": {
              "type": "any"
            },
            "accessToken": {
              "type": "any"
            }
          }
        },
        "139ef4fa-c108-8f9a-c7be-d5f492a2c939": {
          "type": "object",
          "properties": {
            "instance": {
              "type": "any"
            },
            "intId": {
              "type": "any"
            },
            "accessToken": {
              "type": "any"
            }
          }
        },
        "141fbfae-511e-6817-c9f0-48993a7547d1": {
          "type": "object",
          "properties": {
            "instance": {
              "type": "any"
            },
            "intId": {
              "type": "any"
            },
            "accessToken": {
              "type": "any"
            }
          }
        },
        "324cf725-53d9-4bb2-b8f6-0c8ec9a77f45": {
          "type": "object",
          "properties": {
            "instance": {
              "type": "any"
            },
            "intId": {
              "type": "any"
            },
            "accessToken": {
              "type": "any"
            }
          }
        },
        "d70b68e2-8d77-4e0c-9c00-c292d6e0025e": {
          "type": "object",
          "properties": {
            "instance": {
              "type": "any"
            },
            "intId": {
              "type": "any"
            },
            "accessToken": {
              "type": "any"
            }
          }
        },
        "af1a6b7c-227f-4c4a-bc55-f7854cbc58b9": {
          "type": "object",
          "properties": {
            "instance": {
              "type": "any"
            },
            "intId": {
              "type": "any"
            },
            "accessToken": {
              "type": "any"
            }
          }
        },
        "50d8c12f-715e-41ad-be25-d0f61375dbee": {
          "type": "object",
          "properties": {
            "instance": {
              "type": "any"
            },
            "intId": {
              "type": "any"
            },
            "accessToken": {
              "type": "any"
            }
          }
        },
        "146c0d71-352e-4464-9a03-2e868aabe7b9": {
          "type": "object",
          "properties": {
            "instance": {
              "type": "any"
            },
            "intId": {
              "type": "any"
            },
            "accessToken": {
              "type": "any"
            }
          }
        },
        "898091f9-dc3b-4ee6-95c7-ff0a7864ecb7": {
          "type": "object",
          "properties": {
            "instance": {
              "type": "any"
            },
            "intId": {
              "type": "any"
            },
            "dataToken": {
              "type": "any"
            },
            "accessToken": {
              "type": "any"
            }
          }
        },
        "fc9314bc-a317-4a2b-a9d4-5ad21cc57856": {
          "type": "object",
          "properties": {
            "instance": {
              "type": "any"
            },
            "intId": {
              "type": "any"
            },
            "accessToken": {
              "type": "any"
            }
          }
        },
        "b976560c-3122-4351-878f-453f337b7245": {
          "type": "object",
          "properties": {
            "instance": {
              "type": "any"
            },
            "intId": {
              "type": "any"
            },
            "accessToken": {
              "type": "any"
            }
          }
        },
        "4aebd0cb-fbdb-4da7-b5d1-d05660a30172": {
          "type": "object",
          "properties": {
            "instance": {
              "type": "any"
            },
            "intId": {
              "type": "any"
            },
            "accessToken": {
              "type": "any"
            }
          }
        },
        "307ba931-689c-4b55-bb1d-6a382bad9222": {
          "type": "object",
          "properties": {
            "instance": {
              "type": "any"
            },
            "intId": {
              "type": "any"
            },
            "accessToken": {
              "type": "any"
            }
          }
        },
        "edd04d8e-3c81-46d7-b176-39b076fe7bbd": {
          "type": "object",
          "properties": {
            "instance": {
              "type": "any"
            },
            "intId": {
              "type": "any"
            },
            "accessToken": {
              "type": "any"
            }
          }
        },
        "4e0b3af1-73a5-4482-b1fb-87ca6c18905c": {
          "type": "object",
          "properties": {
            "instance": {
              "type": "any"
            },
            "intId": {
              "type": "any"
            },
            "accessToken": {
              "type": "any"
            }
          }
        },
        "49a4ef91-9d6e-43ff-94de-88cb5481cdf5": {
          "type": "object",
          "properties": {
            "instance": {
              "type": "any"
            },
            "intId": {
              "type": "any"
            },
            "accessToken": {
              "type": "any"
            }
          }
        },
        "d80111c5-a0f4-47a8-b63a-65b54d774a27": {
          "type": "object",
          "properties": {
            "instance": {
              "type": "any"
            },
            "intId": {
              "type": "any"
            },
            "accessToken": {
              "type": "any"
            }
          }
        },
        "4b10fcce-732d-4be3-9d46-801d271acda9": {
          "type": "object",
          "properties": {
            "instance": {
              "type": "any"
            },
            "intId": {
              "type": "any"
            },
            "accessToken": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `GET` /_api/tag-manager/api/v1/tags/sites/d71b7674-fb72-4326-848f-bceab1f6b474
```json
{
  "type": "object",
  "properties": {
    "tags": {
      "type": "array",
      "items": "any"
    },
    "errors": {
      "type": "array",
      "items": "any"
    },
    "config": {
      "type": "object",
      "properties": {
        "consentPolicy": {
          "type": "null"
        },
        "geo": {
          "type": "string"
        },
        "experiments": {
          "type": "object",
          "properties": {
            "specs.cookieConsent.CcpHostsIntegrationSUPPORT": {
              "type": "any"
            },
            "specs.tagManagerConfigOverrides": {
              "type": "any"
            },
            "specs.cookieConsent.CcpHostsIntegrationLOGIN_PAGE_SYMPHONY": {
              "type": "any"
            },
            "specs.tagManagerRenderTagByPageID": {
              "type": "any"
            },
            "wixBannerUseNewCipaDesign": {
              "type": "any"
            },
            "specs.tagManagerUseRouterAndPremiumForSiteMetadata": {
              "type": "any"
            },
            "specs.ignoreDisabledAppMarketTemplates": {
              "type": "any"
            },
            "specs.tagManagerEmbedScriptsFreeSites": {
              "type": "any"
            },
            "specs.cookieConsent.gtmDeferredDataLayerPush": {
              "type": "any"
            },
            "specs.cookieConsent.CcpWixCookieBannerDeclineAll": {
              "type": "any"
            },
            "specs.tagManagerRenderGoogleConsentModeTags": {
              "type": "any"
            },
            "specs.cookieConsent.CcpHostsIntegrationFUNNEL": {
              "type": "any"
            },
            "specs.cookieConsent.CcpHostsIntegrationTEMPLATES": {
              "type": "any"
            },
            "specs.migrateGetAppEmbeddedScriptComponentsToGetAppsRuntimeData": {
              "type": "any"
            },
            "specs.cookieConsent.CcpHostsIntegrationARENA": {
              "type": "any"
            },
            "specs.cookieConsent.CcpHostsIntegrationAPP_MARKET_STANDALONE": {
              "type": "any"
            },
            "specs.tagManagerNewSiteEmbedsService": {
              "type": "any"
            },
            "capiLeadKeepalive": {
              "type": "any"
            },
            "specs.cookieConsent.CcpHostsIntegrationRELEASE_NOTES": {
              "type": "any"
            },
            "enableGtgFirstPartyTags": {
              "type": "any"
            }
          }
        },
        "gdprEnforcedGeo": {
          "type": "boolean"
        },
        "dynamicConfigs": {
          "type": "object",
          "properties": {
            "TagManagerConsentPolicyByGeo": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `GET` /pages/pages/thunderbolt
```json
{
  "type": "object",
  "properties": {
    "stateRefs": {
      "type": "object",
      "properties": {
        "comp-kbgakxea_r_comp-kbgajy18": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mu3k9pvx": {
          "type": "object",
          "properties": {
            "reportBi": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mb5540mw": {
          "type": "object",
          "properties": {
            "currentUrl": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mb5540nl1": {
          "type": "object",
          "properties": {
            "editorType": {
              "type": "any"
            },
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mb5540nm5": {
          "type": "object",
          "properties": {
            "reportBi": {
              "type": "any"
            },
            "reducedMotion": {
              "type": "any"
            },
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mb5540no": {
          "type": "object",
          "properties": {
            "setSiteScrollingBlocked": {
              "type": "any"
            },
            "enableCyclicTabbing": {
              "type": "any"
            },
            "disableCyclicTabbing": {
              "type": "any"
            },
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mb5540np4": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-muavojp8": {
          "type": "object",
          "properties": {
            "reportBi": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mb5540nq12": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-mb5540nr1": {
          "type": "object",
          "properties": {
            "reportBi": {
              "type": "any"
            },
            "reducedMotion": {
              "type": "any"
            },
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-muf8dldd": {
          "type": "object",
          "properties": {
            "reportBi": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-muf9u48i": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-muf9u48q": {
          "type": "object",
          "properties": {
            "reportBi": {
              "type": "any"
            },
            "reducedMotion": {
              "type": "any"
            },
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-muf9vcyc": {
          "type": "object",
          "properties": {
            "reportBi": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-muf77bg3": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-kbgakxea_r_comp-muf77bg6": {
          "type": "object",
          "properties": {
            "reportBi": {
              "type": "any"
            },
            "reducedMotion": {
              "type": "any"
            },
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-mu3xtrpz": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-mu3xwirr": {
          "type": "object",
          "properties": {
            "reducedMotion": {
              "type": "any"
            },
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-mu59zamz": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-mu3xtrq510": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        }
      }
    },
    "structure": {
      "type": "object",
      "properties": {
        "components": {
          "type": "object",
          "properties": {
            "c1dmp": {
              "type": "any"
            },
            "Containerc1dmp": {
              "type": "any"
            },
            "comp-kbgakxea-pinned-layer": {
              "type": "any"
            },
            "comp-kbgakxea": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-kbgajy18": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-kbgajy18_relative": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-mu3m4vxb": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-mu3m4vxb_relative": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-mu3k9pvx": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-mu3k868h": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-muf9l3p4": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-muf9l3p4_relative": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-mb5540mw": {
              "type": "any"
            },
            "portal-comp-kbgakxea_r_comp-mb5540mw": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-mb5540nl1": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-mb5540nm5": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-mb5540no": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-mb5540np4": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-muavojp8": {
              "type": "any"
            },
            "comp-kbgakxea_r_comp-mb5540nq12": {
              "type": "any"
            }
          }
        },
        "features": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "siteFeaturesConfigs": {
          "type": "object",
          "properties": {}
        }
      }
    },
    "props": {
      "type": "object",
      "properties": {
        "landingPage": {
          "type": "object",
          "properties": {
            "isLandingPage": {
              "type": "any"
            }
          }
        },
        "scrollRestoration": {
          "type": "object",
          "properties": {
            "shouldRestoreScrollPosition": {
              "type": "any"
            }
          }
        },
        "accessibilityBrowserZoom": {
          "type": "object",
          "properties": {
            "isBuilder": {
              "type": "any"
            },
            "isStudio": {
              "type": "any"
            }
          }
        },
        "animations": {
          "type": "object",
          "properties": {
            "repeaterTemplateToParentMap": {
              "type": "any"
            },
            "isPreview": {
              "type": "any"
            }
          }
        },
        "pageAnchors": {
          "type": "object",
          "properties": {
            "anchors": {
              "type": "any"
            },
            "pageAnchorsObservers": {
              "type": "any"
            },
            "activeAnchorObservers": {
              "type": "any"
            },
            "headerComponentId": {
              "type": "any"
            },
            "isBuilderComponentModel": {
              "type": "any"
            }
          }
        },
        "menuContainer": {
          "type": "object",
          "properties": {
            "menuContainerConfig": {
              "type": "any"
            },
            "menuTogglesConfig": {
              "type": "any"
            }
          }
        },
        "repeaters": {
          "type": "object",
          "properties": {
            "repeatersData": {
              "type": "any"
            }
          }
        },
        "imagePlaceholder": {
          "type": "object",
          "properties": {
            "staticMediaUrl": {
              "type": "any"
            },
            "isSEOBot": {
              "type": "any"
            },
            "userDomainMediaBaseUrl": {
              "type": "any"
            },
            "userDomainMediaPrefixes": {
              "type": "any"
            }
          }
        },
        "siteMembers": {
          "type": "object",
          "properties": {
            "componentIds": {
              "type": "any"
            }
          }
        },
        "scrollToAnchor": {
          "type": "object",
          "properties": {
            "anchorDataIdToCompIdMap": {
              "type": "any"
            },
            "nicknameToCompIdMap": {
              "type": "any"
            },
            "compsToUpdate": {
              "type": "any"
            },
            "isAnchorsLinksOnPageWithoutTopAndBottom": {
              "type": "any"
            },
            "isBuilderComponentModel": {
              "type": "any"
            },
            "anchorNameToCompIdMap": {
              "type": "any"
            },
            "isResponsive": {
              "type": "any"
            }
          }
        },
        "windowScroll": {
          "type": "object",
          "properties": {
            "headerContainerComponentId": {
              "type": "any"
            }
          }
        },
        "ooi": {
          "type": "object",
          "properties": {
            "ooiComponents": {
              "type": "any"
            },
            "accessibilityEnabled": {
              "type": "any"
            },
            "pagesToShowSosp": {
              "type": "any"
            }
          }
        },
        "tpa": {
          "type": "object",
          "properties": {
            "widgets": {
              "type": "any"
            },
            "tpaGalleriesImageItems": {
              "type": "any"
            },
            "pageId": {
              "type": "any"
            },
            "hasWixTpaOnPage": {
              "type": "any"
            },
            "tpaInnerRouteConfig": {
              "type": "any"
            },
            "appPublicData": {
              "type": "any"
            },
            "isFixedHeader": {
              "type": "any"
            },
            "siteScale": {
              "type": "any"
            }
          }
        },
        "svgLoader": {
          "type": "object",
          "properties": {
            "compIdToSvgDataMap": {
              "type": "any"
            },
            "colorsMap": {
              "type": "any"
            },
            "mediaRootUrl": {
              "type": "any"
            },
            "compIdToVectorArtPropsPaths": {
              "type": "any"
            }
          }
        },
        "seo": {
          "type": "object",
          "properties": {
            "pageId": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "indexPage": {
              "type": "any"
            },
            "ogImage": {
              "type": "any"
            },
            "ogImageHeight": {
              "type": "any"
            },
            "ogImageWidth": {
              "type": "any"
            },
            "pageName": {
              "type": "any"
            },
            "title": {
              "type": "any"
            },
            "advancedSeoData": {
              "type": "any"
            },
            "currentPageUrl": {
              "type": "any"
            },
            "translationsData": {
              "type": "any"
            },
            "tpaPageId": {
              "type": "any"
            },
            "managingAppDefId": {
              "type": "any"
            }
          }
        },
        "menusCurrentPage": {
          "type": "object",
          "properties": {}
        },
        "domSelectors": {
          "type": "object",
          "properties": {
            "allComponentIds": {
              "type": "any"
            }
          }
        },
        "components": {
          "type": "object",
          "properties": {
            "componentsUnderFoldMap": {
              "type": "any"
            }
          }
        },
        "mobileFullScreen": {
          "type": "object",
          "properties": {}
        },
        "siteWixCodeSdk": {
          "type": "object",
          "properties": {
            "pagesData": {
              "type": "any"
            },
            "nonPopupsPagesData": {
              "type": "any"
            },
            "lightboxes": {
              "type": "any"
            }
          }
        }
      }
    },
    "nicknameToCompIdMaps": {
      "type": "object",
      "properties": {}
    }
  }
}
```
### `GET` /services/editor-elements/1.15653.0/rb_wixui.thunderbolt.manifest.min.json
```json
{
  "type": "object",
  "properties": {
    "version": {
      "type": "string"
    },
    "host": {
      "type": "string"
    },
    "namespace": {
      "type": "string"
    },
    "baseURL": {
      "type": "string"
    },
    "model": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "assets": {
      "type": "array",
      "items": {
        "type": "array",
        "items": {
          "type": "any"
        }
      }
    },
    "components": {
      "type": "object",
      "properties": {
        "Container_TiltedAreaSkin": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "SiteButton_SloopyButton": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "DropDownMenu_OverlineMenuButtonHorizontalMenuAdaptationSkin": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "SliderGallery_SliderGalleryDefaultSkin": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "FacebookShare": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "StylableButton_Button": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "FiveGridLine_SolidLine": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "TextEffectsSticker": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "FormContainer_ResponsiveSkin": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "VerticalAnchorsMenu_VerticalAnchorsMenuLinkedNoTextSkin": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "HeaderContainer_NoiseScreen": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "VerticalMenu_ComboBoxInputNavigation": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "LoginSocialBar": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "WPhoto_LiftedShadowPhoto": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "MediaPlayer_videoBoxResponsive": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "PaginatedGridGalleryItem": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "AppWidget_Classic": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "ProgressBar": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "CoBrandingBannerMobile": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "SelectionTag": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    },
    "batches": {
      "type": "object",
      "properties": {
        "bootstrap": {
          "type": "object",
          "properties": {
            "url": {
              "type": "any"
            },
            "components": {
              "type": "any"
            },
            "parts": {
              "type": "any"
            }
          }
        },
        "bootstrap-responsive": {
          "type": "object",
          "properties": {
            "url": {
              "type": "any"
            },
            "components": {
              "type": "any"
            },
            "parts": {
              "type": "any"
            }
          }
        },
        "mobile": {
          "type": "object",
          "properties": {
            "url": {
              "type": "any"
            },
            "components": {
              "type": "any"
            },
            "parts": {
              "type": "any"
            }
          }
        },
        "menu": {
          "type": "object",
          "properties": {
            "url": {
              "type": "any"
            },
            "components": {
              "type": "any"
            },
            "parts": {
              "type": "any"
            }
          }
        },
        "common-site-members-dialogs": {
          "type": "object",
          "properties": {
            "url": {
              "type": "any"
            },
            "components": {
              "type": "any"
            },
            "parts": {
              "type": "any"
            }
          }
        },
        "popup": {
          "type": "object",
          "properties": {
            "url": {
              "type": "any"
            },
            "components": {
              "type": "any"
            },
            "parts": {
              "type": "any"
            }
          }
        },
        "slideshow": {
          "type": "object",
          "properties": {
            "url": {
              "type": "any"
            },
            "components": {
              "type": "any"
            },
            "parts": {
              "type": "any"
            }
          }
        },
        "selectable-container": {
          "type": "object",
          "properties": {
            "url": {
              "type": "any"
            },
            "components": {
              "type": "any"
            },
            "parts": {
              "type": "any"
            }
          }
        },
        "bootstrap-classic": {
          "type": "object",
          "properties": {
            "url": {
              "type": "any"
            },
            "components": {
              "type": "any"
            },
            "parts": {
              "type": "any"
            }
          }
        }
      }
    },
    "shared": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  }
}
```

