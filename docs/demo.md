# 🎬 CattleΨic Prototype Demo

## Current Demo Flow

```text
Milk Sample
     ↓
pH + EC + Temperature + Turbidity Sensors
     ↓
ADS1115 + Raspberry Pi
     ↓
Filtering + Multiple Reading Averaging
     ↓
Rule-based Risk Screening
     ↓
Healthy / Attention / High Risk
     ↓
┌──────────────┬────────────────────┐
│ 16x4 LCD     │ Farmer Dashboard   │
└──────────────┴────────────────────┘
     ↓
Offline / Health History
```

## Current Prototype Extension

A compact **58 mm thermal receipt printer** is being integrated into the device concept. After one cow test, the same result object will be used for:

```text
LCD Result
   +
Dashboard/Mobile Result
   +
Printed Farmer Receipt
```

The repository already contains the receipt format and formatter scaffold. Physical printer connection and testing are still pending.

## What is implemented now

- Raspberry Pi sensor acquisition pipeline
- pH, EC, temperature and turbidity input handling
- Multiple-reading averaging
- Local LCD result display
- Offline JSON storage when cloud is unavailable
- Backend POST request support when a server URL is configured
- Farmer dashboard prototype and backend prototype
- Thermal receipt format and formatter scaffold

## What is still in progress

- Sensor calibration using validated reference samples
- Live Raspberry Pi-to-cloud synchronization
- Physical thermal-printer integration
- Labelled longitudinal farm dataset collection
- ML model training and external validation
- 7–14 day forecasting validation
- Field testing with dairy farms and veterinarians

> CattleΨic currently demonstrates an early risk-screening pipeline. It does not yet claim clinically validated 7–14 day forecasting.
