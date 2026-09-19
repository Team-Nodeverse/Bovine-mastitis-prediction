# 🏗️ CattleΨic System Architecture

## Overview

CattleΨic uses a Raspberry Pi as the edge-processing unit to collect and analyse multiple milk parameters for mastitis-risk assessment.

The current hardware revision uses a **large integrated display / touchscreen** instead of the earlier small character LCD, and includes a **58 mm thermal receipt printer** in the device output architecture.

The Random Forest model has been trained on the currently available labelled dataset. Current work focuses on final Raspberry Pi deployment integration, calibration and validation documentation.

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
      DS18B20 Temperature        Data Preprocessing
                                         │
                                         ▼
                            Filtering / Averaging
                                         │
                                         ▼
                           Feature Preparation
                                         │
                                         ▼
                           Trained Random Forest
                                         │
                               Risk Classification
                                         │
                          ┌──────────────┼──────────────┐
                          ▼              ▼              ▼
                        LOW          MODERATE          HIGH
                                         │
                  ┌──────────────────────┼──────────────────────┐
                  ▼                      ▼                      ▼
          Large Local Display      Dashboard / Cloud     58 mm Receipt
          / Touchscreen UI         + Offline Records      Printer Output
```

## Current Edge Functions

- multi-sensor data acquisition
- pH, EC, temperature and turbidity handling
- multiple-reading averaging
- preprocessing / feature preparation
- trained Random Forest model workflow
- local risk classification output
- offline record storage
- dashboard / backend communication architecture
- thermal receipt formatting

## Large Display Strategy

The earlier 16x4 LCD concept has been removed from the current design direction.

The new local display is intended to show:

- Cow ID
- sensor values
- test progress
- mastitis-risk level
- next-step guidance
- connectivity status
- receipt / print status

The final screen may use a Raspberry Pi-compatible HDMI, DSI or touchscreen panel depending on enclosure and power constraints.

See: [Integrated Large Display](../hardware/display/README.md)

## Output Strategy

One structured test result should feed all outputs:

- large local device display
- farmer dashboard / mobile interface
- local offline record
- cloud history
- 58 mm physical receipt

This prevents different values being shown on different user interfaces.

## Thermal Receipt Integration

The 58 mm thermal printer is included as a current device integration extension. The physical slip can contain:

- Cow ID
- test date/time
- pH
- EC
- temperature
- turbidity
- risk result
- next-step guidance

See: [Thermal Receipt Printer Integration](thermal-receipt-printer.md)

## AI / ML Layer

The Random Forest model has been trained on the available labelled dataset. The remaining ML work is focused on deployment integration and documented validation rather than initial model training.

Validation documentation should include the actual measured metrics from the model run and, for SIH26109's early-forecasting objective, separate evaluation of pre-clinical forecast horizons when longitudinal data is available.
