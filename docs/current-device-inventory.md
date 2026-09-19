# 📋 CattleΨic Current Device Inventory

This document separates what is already part of the current build direction from integration work and later-stage expansion. It is intended to keep the GitHub repository and SIH presentation consistent.

## Current Device / Software Inventory

| Layer | Current CattleΨic Item | Status |
|---|---|---|
| Controller | Raspberry Pi | Current design |
| Analog acquisition | ADS1115 | Prototype |
| Milk sensing | pH sensor | Prototype / calibration refinement |
| Milk sensing | EC sensor | Prototype / calibration refinement |
| Milk sensing | Temperature sensor (DS18B20) | Prototype |
| Milk sensing | Turbidity sensor | Prototype / evidence refinement |
| Edge AI | Trained Random Forest model | Training completed; final deployment integration / evaluation documentation continuing |
| Local UI | Large Raspberry Pi-compatible display / touchscreen | Current hardware revision; software UI available |
| User input | Push button / test control | Prototype |
| Offline mode | Local result storage | Architecture / prototype available |
| Cloud path | Backend / dashboard synchronization | Integration path available; live device sync refinement ongoing |
| Farmer dashboard | Sensor values, risk, history direction | Prototype available |
| Physical output | 58 mm thermal receipt printer | Current device integration extension |
| Printed report | Cow ID, test values, risk and short guidance | Formatter available; physical printer integration continuing |
| Records | Cow-wise health / test-history architecture | Prototype |
| Alerts | App / SMS architecture | Integration work |

## Current User Journey

```text
Cow Selected / Cow ID
        ↓
Milk Sample
        ↓
pH + EC + Temperature + Turbidity
        ↓
Raspberry Pi
        ↓
Preprocessing / Feature Preparation
        ↓
Random Forest Risk Model
        ↓
Low / Moderate / High Risk
        ↓
┌──────────────────────┬───────────────────┬────────────────────┐
│ Large Device Display │ Dashboard / Record│ Thermal Test Slip  │
└──────────────────────┴───────────────────┴────────────────────┘
```

## Presentation Progress Positioning

Recommended presentation wording:

> **Overall prototype development: ~60%**

Completed / demonstrated work should be shown separately from integration and validation work. This communicates meaningful progress without implying that production deployment and multi-farm validation are already finished.

### Completed / demonstrated

- core Raspberry Pi sensing pipeline
- trained Random Forest baseline
- multi-parameter sensor workflow
- dashboard prototype
- offline architecture
- large-display software UI
- receipt-formatting software

### Current integration / refinement

- sensor calibration
- final Random Forest deployment path on Raspberry Pi
- final large-display mounting
- physical thermal-printer connection
- live cloud sync
- measured model-evaluation report
- alert service integration

### Later-stage scope

- smart collar / activity / rumination sensing
- large-scale SCC / lab-system integration
- GIS disease hotspot mapping
- cooperative-wide multi-farm analytics
- production-scale rugged / solar field deployment
- multi-farm 7–14 day longitudinal forecasting validation

## Device Design Change

The earlier small 16x4 character LCD is **not part of the current device direction**. The current design uses a larger local display / touchscreen so the farmer can view readings, risk, guidance and print status on one screen.

The earlier hardware photograph remains in the repository only as evidence of prototype progress.
