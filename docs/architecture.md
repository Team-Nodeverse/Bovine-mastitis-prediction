# 🏗️ CattleΨic System Architecture

## Overview

CattleΨic uses a Raspberry Pi as the edge-processing unit to collect and analyse multiple milk parameters for early mastitis-risk screening.

The current prototype focuses on the sensor-to-result pipeline. Validated ML forecasting, final large-display hardware selection, physical thermal-printer integration and field validation are still under development.

## System Architecture

```text
                         MILK SAMPLE
                              │
             ┌────────────────┼────────────────┐
             │                │                │
         pH Sensor        EC Sensor      Turbidity Sensor
             │                │                │
             └─────────────┬──┴────────────────┘
                           │
                        ADS1115
                           │
                           ▼
                      Raspberry Pi
                           │
             ┌─────────────┴─────────────┐
             │                           │
      DS18B20 Temperature        Sensor Processing
                                         │
                                         ▼
                              Filtering & Averaging
                                         │
                                         ▼
                              Risk Analysis Layer
                                         │
                            ┌────────────┼────────────┐
                            ▼            ▼            ▼
                         Healthy     Attention     High Risk
                                         │
                  ┌──────────────────────┼──────────────────────┐
                  ▼                      ▼                      ▼
       Large Local Display        Offline Storage       Receipt Formatter
       (HDMI/DSI Touch UI)              │                      │
                  │                     ▼                      ▼
                  │              Backend / Cloud      58 mm Thermal Printer
                  │                     │               (integration planned)
                  │          ┌──────────┴──────────┐
                  └─────────►▼                     ▼
                       Farmer Dashboard       Health History
```

## Current Edge Functions

- Multi-sensor data acquisition
- Multiple-reading averaging
- pH, EC, temperature and turbidity value handling
- Rule-based Healthy / Attention / High Risk screening
- Local large-display status output through `current_status.json`
- Offline JSON storage
- Backend POST support

## Local Display Strategy

The earlier 16x4 LCD concept has been removed from the current design direction. The final device is planned around a larger Raspberry Pi-compatible HDMI/DSI display or touchscreen.

The sensor process writes a common local status object. A separate display UI reads that file and presents large, farmer-friendly values and risk status. This keeps the software independent from the exact display model.

See: [Integrated Large Display](../hardware/display/README.md)

## Output Strategy

One test result object is intended to feed all user outputs:

- Large local device display
- Dashboard/mobile interface
- Offline record
- Cloud/backend history
- Compact thermal receipt

Using one common test object reduces the risk of different values being shown on different outputs.

## Thermal Receipt Integration

A compact 58 mm thermal receipt printer is being treated as a **current prototype extension**, not as a field-validated feature. The receipt can contain Cow ID, test time, sensor readings, risk status and a screening disclaimer.

See: [Thermal Receipt Printer Integration](thermal-receipt-printer.md)

## AI/ML Layer

The current Raspberry Pi prototype uses rule-based screening to validate the end-to-end hardware/data path. The planned ML layer will use labelled longitudinal dairy data and compare models such as Logistic Regression, Random Forest and gradient-boosted trees using proper validation methodology.
