# 🍓 Raspberry Pi Edge Module

This folder contains the Raspberry Pi based edge-processing prototype used in CattleΨic.

## Hardware Used

- Raspberry Pi
- ADS1115 ADC
- pH Sensor
- EC Sensor
- Turbidity Sensor
- DS18B20 Temperature Sensor
- Push Button
- Large Raspberry Pi-compatible display / touchscreen
- 58 mm thermal printer

> The small 16x4 LCD has been removed from the current product direction. The current device revision uses a larger local display similar to a compact tablet screen.

## Sensor Mapping

| Sensor / Device | Interface |
|---|---|
| pH Sensor | ADS1115 A0 |
| EC Sensor | ADS1115 A1 |
| Turbidity Sensor | ADS1115 A2 |
| DS18B20 | 1-Wire |
| Push Button | GPIO17 |
| Large Display | HDMI / DSI depending selected panel |
| Thermal Printer | USB or UART/TTL depending selected printer |

## Installation

From the repository root:

```bash
pip install -r requirements.txt
```

For the local full-screen display UI on Raspberry Pi OS:

```bash
sudo apt install python3-tk
```

## Run Sensor Process

```bash
python3 hardware/raspberry-pi/cattlepsic_pi.py
```

## Run Large Local Display

```bash
python3 hardware/display/cattlepsic_display.py
```

## Current ML Status

A **Random Forest model has been trained on the currently available labelled mastitis dataset**. The current engineering task is to integrate the trained model artifact into the final Raspberry Pi inference path and document the exact evaluation evidence.

During sensor calibration and integration work, the edge software can retain a transparent fallback screening rule so hardware testing can continue even when the final model artifact is not loaded.

## Prototype Workflow

1. Farmer selects / enters the cow ID.
2. Milk sample is placed for testing.
3. pH, EC, temperature and turbidity readings are collected.
4. Raspberry Pi performs averaging, preprocessing and feature preparation.
5. The trained Random Forest inference path produces a risk classification when the model artifact is loaded.
6. Result is shown on the large local display.
7. The same structured result can be stored offline, synchronized to the dashboard and formatted for a thermal receipt.

## Current Status

### Completed / available

- Raspberry Pi sensor pipeline
- multi-sensor acquisition
- preprocessing / averaging logic
- Random Forest model training
- large-display software interface
- offline storage architecture
- dashboard communication path
- thermal receipt formatter

### Integration / validation in progress

- final model artifact deployment in the Raspberry Pi inference path
- exact evaluation-report publication
- final sensor calibration
- final display hardware mounting
- physical printer connection
- live cloud synchronization
- wider field validation

> CattleΨic is an early-risk forecasting / screening prototype and does not replace veterinary diagnosis.
