---
title: "APIs & Protocols: www-sentientx-com"
date: 2026-11-14
target: "[[overview|www-sentientx-com]]"
---

# Discovered APIs & Protocols: www-sentientx-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/consentconfig/8a0a689d-df02-4390-9af8-b5557efa96e2/settings.json` | `200` | REST endpoint |
| `POST` | `/api/v1/bulklog` | `204` | REST endpoint |
| `GET` | `/pages/pages/thunderbolt` | `200` | REST endpoint |
| `GET` | `/pages/pages/thunderbolt` | `200` | REST endpoint |
| `GET` | `/pages/pages/thunderbolt` | `200` | REST endpoint |
| `POST` | `/api/v1/bulklog` | `204` | REST endpoint |
| `GET` | `/pages/pages/thunderbolt` | `200` | REST endpoint |
| `POST` | `/api/v1/bulklog` | `204` | REST endpoint |
| `POST` | `/api/v1/bulklog` | `204` | REST endpoint |
| `GET` | `/_api/v1/access-tokens` | `200` | REST endpoint |
| `POST` | `/api/v1/bulklog` | `204` | REST endpoint |
| `POST` | `/api/v1/bulklog` | `204` | REST endpoint |
| `POST` | `/api/v1/bulklog` | `204` | REST endpoint |
| `GET` | `/services/editor-elements/1.15638.0/rb_wixui.corvid.manifest.min.json` | `200` | REST endpoint |
| `GET` | `/services/editor-elements/1.15638.0/rb_dsgnsys.corvid.manifest.min.json` | `200` | REST endpoint |
| `POST` | `/api/v1/bulklog` | `204` | REST endpoint |
| `GET` | `/_api/tag-manager/api/v1/tags/sites/0bc334b8-a9b0-463d-b477-a4ec6505a92e` | `200` | REST endpoint |
| `GET` | `/pages/pages/thunderbolt` | `200` | REST endpoint |
| `GET` | `/services/editor-elements/1.15638.0/rb_wixui.thunderbolt.manifest.min.json` | `200` | REST endpoint |
| `GET` | `/services/editor-elements/1.15638.0/rb_dsgnsys.thunderbolt.manifest.min.json` | `200` | REST endpoint |
| `POST` | `/api/v1/bulklog` | `204` | REST endpoint |
| `POST` | `/api/v1/bulklog` | `204` | REST endpoint |
| `POST` | `/api/v1/bulklog` | `204` | REST endpoint |
| `POST` | `/api/v1/bulklog` | `204` | REST endpoint |
| `POST` | `/api/v1/bulklog` | `204` | REST endpoint |
| `GET` | `/pages/pages/thunderbolt` | `200` | REST endpoint |
| `GET` | `/pages/pages/thunderbolt` | `200` | REST endpoint |
| `GET` | `/pages/pages/thunderbolt` | `200` | REST endpoint |
| `GET` | `/pages/pages/thunderbolt` | `200` | REST endpoint |
| `POST` | `/api/v1/bulklog` | `204` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /consentconfig/8a0a689d-df02-4390-9af8-b5557efa96e2/settings.json
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
        },
        "windowWixCodeSdk": {
          "type": "object",
          "properties": {
            "popupNameToPageId": {
              "type": "any"
            },
            "popupPageIdToName": {
              "type": "any"
            },
            "popupTpaPageIdToPageId": {
              "type": "any"
            },
            "pageId": {
              "type": "any"
            },
            "templateIdToCompIdMap": {
              "type": "any"
            },
            "appDefIdToCompIdsMap": {
              "type": "any"
            }
          }
        },
        "seoWixCodeSdk": {
          "type": "object",
          "properties": {
            "pageId": {
              "type": "any"
            },
            "description": {
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
        "motion": {
          "type": "object",
          "properties": {
            "animationDataByCompId": {
              "type": "any"
            },
            "scrubAnimationBreakpoints": {
              "type": "any"
            },
            "repeaterTemplateToParentMap": {
              "type": "any"
            },
            "isResponsive": {
              "type": "any"
            }
          }
        },
        "triggersAndReactions": {
          "type": "object",
          "properties": {
            "compsToTriggers": {
              "type": "any"
            },
            "compIdsWithAccessibleTrigger": {
              "type": "any"
            },
            "isTouchDevice": {
              "type": "any"
            },
            "repeaterDescendantToRepeaterMapper": {
              "type": "any"
            },
            "compsToEffects": {
              "type": "any"
            },
            "compEffectsToVariantId": {
              "type": "any"
            },
            "variantIdToEffect": {
              "type": "any"
            },
            "viewportTriggerCompsToParams": {
              "type": "any"
            },
            "presetVariantsToReactionVariants": {
              "type": "any"
            },
            "effectTriggerToReaction": {
              "type": "any"
            },
            "scrubReactionWithBpRanges": {
              "type": "any"
            },
            "scrubBpRanges": {
              "type": "any"
            },
            "dynamicCompToDescendants": {
              "type": "any"
            },
            "isMotionEnabled": {
              "type": "any"
            },
            "breakpointsRanges": {
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
        "comp-mqurid64_r_comp-kbgajy18": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqurv9i6": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            },
            "currentConsentPolicy": {
              "type": "any"
            },
            "openSettingModal": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqusywao8": {
          "type": "object",
          "properties": {
            "reportBi": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqusywar4": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqusywat": {
          "type": "object",
          "properties": {
            "reportBi": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqz5gs6e": {
          "type": "object",
          "properties": {
            "reducedMotion": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqz5gs721": {
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
        "comp-mqurid64_r_comp-mqz5gs79": {
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
        "comp-mqurid64_r_comp-mqz7h97y": {
          "type": "object",
          "properties": {
            "reportBi": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mvrybn04": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqz7e94a": {
          "type": "object",
          "properties": {
            "reportBi": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqz7j0ah": {
          "type": "object",
          "properties": {
            "reportBi": {
              "type": "any"
            },
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqz5o9ow": {
          "type": "object",
          "properties": {
            "observeChildListChange": {
              "type": "any"
            },
            "observeChildListChangeMaster": {
              "type": "any"
            },
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqz5o9p92": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqz5o9p92__item1": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqz5o9p92__item-mqqsnz8y1": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqz5o9p92__item-mqqso0ga": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqz5o9p92__item-mqqso2uw1": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqz5o9p92__item-mqqso48d1": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqz5o9pe15": {
          "type": "object",
          "properties": {
            "reportBi": {
              "type": "any"
            },
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
            "comp-mqurid64-pinned-layer": {
              "type": "any"
            },
            "comp-mqurid64": {
              "type": "any"
            },
            "comp-mqurid64_r_comp-kbgajy18": {
              "type": "any"
            },
            "comp-mqurid64_r_comp-kbgajy18_relative": {
              "type": "any"
            },
            "comp-mqurid64_r_comp-mqurv9i6": {
              "type": "any"
            },
            "comp-mqurid64_r_comp-mqusy7r2": {
              "type": "any"
            },
            "comp-mqurid64_r_comp-mqusy7r2_relative": {
              "type": "any"
            },
            "comp-mqurid64_r_comp-mqusywam": {
              "type": "any"
            },
            "comp-mqurid64_r_comp-mqusywam_relative": {
              "type": "any"
            },
            "comp-mqurid64_r_comp-mqusywao8": {
              "type": "any"
            },
            "comp-mqurid64_r_comp-mqusywar4": {
              "type": "any"
            },
            "comp-mqurid64_r_comp-mqusywat": {
              "type": "any"
            },
            "comp-mqurid64_r_comp-mqz6smh3": {
              "type": "any"
            },
            "comp-mqurid64_r_comp-mqz6smh3_relative": {
              "type": "any"
            },
            "comp-mqurid64_r_comp-mqz4vzbc": {
              "type": "any"
            },
            "comp-mqurid64_r_comp-mqz4vzbc_relative": {
              "type": "any"
            },
            "comp-mqurid64_r_comp-mqz5gs6e": {
              "type": "any"
            },
            "VideoBox_dummy_comp-mqurid64_r_comp-mqz5gs6e": {
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
        "onloadCompsBehaviors": {
          "type": "object",
          "properties": {
            "compsBehaviors": {
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
        },
        "windowWixCodeSdk": {
          "type": "object",
          "properties": {
            "isPopup": {
              "type": "any"
            },
            "popupNameToPageId": {
              "type": "any"
            },
            "popupPageIdToName": {
              "type": "any"
            },
            "popupTpaPageIdToPageId": {
              "type": "any"
            },
            "pageId": {
              "type": "any"
            },
            "templateIdToCompIdMap": {
              "type": "any"
            },
            "appDefIdToCompIdsMap": {
              "type": "any"
            }
          }
        },
        "seoWixCodeSdk": {
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
        "comp-mqurid64_r_comp-mqusy7r2": {
          "type": "object",
          "properties": {
            "initialSdkStyles": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqusywam": {
          "type": "object",
          "properties": {
            "initialSdkStyles": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqusywao8": {
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
        "comp-mqurid64_r_comp-mqusywar4": {
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
        "comp-mqurid64_r_comp-mqusywat": {
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
        "comp-mqurid64_r_comp-mqz6smh3": {
          "type": "object",
          "properties": {
            "initialSdkStyles": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqz4vzbc": {
          "type": "object",
          "properties": {
            "initialSdkStyles": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqz7hyef": {
          "type": "object",
          "properties": {
            "initialSdkStyles": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqz7ae3o": {
          "type": "object",
          "properties": {
            "initialSdkStyles": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqz7f49s": {
          "type": "object",
          "properties": {
            "initialSdkStyles": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqz7h97y": {
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
        "comp-mqurid64_r_comp-mvrybn04": {
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
        "comp-mqurid64_r_comp-mqz7e94a": {
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
        "comp-mqurid64_r_comp-mqz7j0ah": {
          "type": "object",
          "properties": {
            "initialSdkStyles": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqz5o9ow": {
          "type": "object",
          "properties": {
            "repeaterChildComponents": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqz5o9p04": {
          "type": "object",
          "properties": {
            "initialSdkStyles": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqz5o9p22": {
          "type": "object",
          "properties": {
            "initialSdkStyles": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqz5o9p92": {
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
        "comp-mqurid64_r_comp-mqz5o9pe15": {
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
      "properties": {
        "comp-mqurid64_r_comp-mqz4vzbc": {
          "type": "object",
          "properties": {
            "hiddenOnLoad": {
              "type": "any"
            },
            "collapseOnLoad": {
              "type": "any"
            }
          }
        }
      }
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
        "comp-mqurid64": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mqurid64_r_comp-kbgajy18": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mqurid64_r_comp-mqusy7r2": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mqurid64_r_comp-mqusywam": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mqurid64_r_comp-mqz6smh3": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mqurid64_r_comp-mqz4vzbc": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mqurid64_r_comp-mqz5gs6e": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mqurid64_r_comp-mqz7hyef": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mqurid64_r_comp-mqz7ae3o": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mqurid64_r_comp-mqz5o9ow": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mqurid64_r_comp-mqz5o9p04": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mqurid64_r_comp-mqusbiy8": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mqurid64_r_comp-mqusl9h6": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mqurid64_r_comp-mqusju80": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mqurid64_r_comp-mqusm8vo": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mqurid64_r_comp-mqutquoh": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mqurid64_r_comp-mqutquok": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mqurid64_r_comp-mqutquol10": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mqurid64_r_comp-mqutquon1": {
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
        "comp-mqurid64_r_comp-mqz5o9p04": {
          "type": "string"
        },
        "comp-mqurid64_r_comp-mqz5o9p22": {
          "type": "string"
        },
        "comp-mqurid64_r_comp-mqz5o9p92": {
          "type": "string"
        },
        "comp-mqurid64_r_comp-mqz5o9pe15": {
          "type": "string"
        },
        "comp-mqurid64_r_comp-mqz5o9pj2": {
          "type": "string"
        },
        "comp-mqurid64_r_comp-mqz60u12": {
          "type": "string"
        },
        "comp-kbgakxmn_r_comp-mqqsbzic": {
          "type": "string"
        },
        "comp-kbgakxmn_r_comp-mqqskuie": {
          "type": "string"
        },
        "comp-kbgakxmn_r_comp-mqqsi5dz": {
          "type": "string"
        },
        "comp-kbgakxmn_r_comp-mqqsrd84": {
          "type": "string"
        },
        "comp-kbgakxmn_r_comp-mqqsj20q": {
          "type": "string"
        },
        "comp-kbgakxmn_r_comp-mqqsrykh9": {
          "type": "string"
        },
        "comp-kbgakxmn_r_comp-mqqsrykj2": {
          "type": "string"
        },
        "comp-kbgakxmn_r_comp-mqqsrykk9": {
          "type": "string"
        },
        "comp-kbgakxmn_r_comp-mqqsrykl13": {
          "type": "string"
        },
        "comp-kbgakxmn_r_comp-mqqsrykm": {
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
          "properties": {}
        },
        "props": {
          "type": "object",
          "properties": {}
        },
        "parentComponentsUpdates": {
          "type": "object",
          "properties": {}
        }
      }
    },
    "slots": {
      "type": "object",
      "properties": {}
    },
    "applications": {
      "type": "object",
      "properties": {
        "675bbcef-18d8-41f5-800e-131ec9e08762": {
          "type": "object",
          "properties": {
            "wixCode": {
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
            "html2": {
              "type": "any"
            },
            "box227": {
              "type": "any"
            },
            "box228": {
              "type": "any"
            },
            "vectorImage64": {
              "type": "any"
            },
            "pageTitle": {
              "type": "any"
            },
            "vectorImage63": {
              "type": "any"
            },
            "menuWrap": {
              "type": "any"
            },
            "menuBox2": {
              "type": "any"
            },
            "videoBox8": {
              "type": "any"
            },
            "box341": {
              "type": "any"
            },
            "box338": {
              "type": "any"
            },
            "box339": {
              "type": "any"
            },
            "vectorImage94": {
              "type": "any"
            },
            "text376": {
              "type": "any"
            },
            "vectorImage93": {
              "type": "any"
            },
            "button14": {
              "type": "any"
            },
            "line31": {
              "type": "any"
            },
            "repeater7": {
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
        "comp-mqurid64_r_comp-kbgajy18": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqurv9i6": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqusy7r2": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqusywam": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqusywao8": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqusywar4": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqusywat": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqz6smh3": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqz4vzbc": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqz5gs6e": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqz7hyef": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqz7ae3o": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqz7f49s": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqz7h97y": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mvrybn04": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqz7e94a": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqz7j0ah": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mvryl6d7": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mqurid64_r_comp-mqz5o9ow": {
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
      "items": "any"
    },
    "controllerConfigs": {
      "type": "object",
      "properties": {
        "675bbcef-18d8-41f5-800e-131ec9e08762": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        }
      }
    },
    "applicationsPublicData": {
      "type": "object",
      "properties": {}
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
        },
        "windowWixCodeSdk": {
          "type": "object",
          "properties": {
            "popupNameToPageId": {
              "type": "any"
            },
            "popupPageIdToName": {
              "type": "any"
            },
            "popupTpaPageIdToPageId": {
              "type": "any"
            },
            "pageId": {
              "type": "any"
            },
            "templateIdToCompIdMap": {
              "type": "any"
            },
            "appDefIdToCompIdsMap": {
              "type": "any"
            }
          }
        },
        "seoWixCodeSdk": {
          "type": "object",
          "properties": {
            "pageId": {
              "type": "any"
            },
            "description": {
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
        "motion": {
          "type": "object",
          "properties": {
            "animationDataByCompId": {
              "type": "any"
            },
            "scrubAnimationBreakpoints": {
              "type": "any"
            },
            "repeaterTemplateToParentMap": {
              "type": "any"
            },
            "isResponsive": {
              "type": "any"
            }
          }
        },
        "triggersAndReactions": {
          "type": "object",
          "properties": {
            "compsToTriggers": {
              "type": "any"
            },
            "compIdsWithAccessibleTrigger": {
              "type": "any"
            },
            "isTouchDevice": {
              "type": "any"
            },
            "repeaterDescendantToRepeaterMapper": {
              "type": "any"
            },
            "compsToEffects": {
              "type": "any"
            },
            "compEffectsToVariantId": {
              "type": "any"
            },
            "variantIdToEffect": {
              "type": "any"
            },
            "viewportTriggerCompsToParams": {
              "type": "any"
            },
            "presetVariantsToReactionVariants": {
              "type": "any"
            },
            "effectTriggerToReaction": {
              "type": "any"
            },
            "scrubReactionWithBpRanges": {
              "type": "any"
            },
            "scrubBpRanges": {
              "type": "any"
            },
            "dynamicCompToDescendants": {
              "type": "any"
            },
            "isMotionEnabled": {
              "type": "any"
            },
            "breakpointsRanges": {
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
        "225dd912-7dea-4738-8688-4b8c6955ffc2": {
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
        },
        "14d7032a-0a65-5270-cca7-30f599708fed": {
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
        "14b89688-9b25-5214-d1cb-a3fb9683618b": {
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
        "ea2821fc-7d97-40a9-9f75-772f29178430": {
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
        "1973457f-c021-4da5-941f-58444ff761d4": {
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
        "57d13128-4a4c-494b-80b3-a6fb2e28018d": {
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
        "55cd9036-36bb-480b-8ddc-afda3cb2eb8d": {
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
        "9bead16f-1c73-4cda-b6c4-28cff46988db": {
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
        "7516f85b-0868-4c23-9fcb-cea7784243df": {
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

