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
- Large Raspberry Pi-compatible display / touchscreen (final model to be selected)
- 58 mm thermal printer (integration in progress)

> The small 16x4 LCD has been removed from the current product direction. The final prototype is planned around a larger local display similar to a compact tablet screen.

## Sensor Mapping

| Sensor | Interface |
|---|---|
| pH Sensor | ADS1115 A0 |
| EC Sensor | ADS1115 A1 |
| Turbidity Sensor | ADS1115 A2 |
| DS18B20 | 1-Wire |
| Push Button | GPIO17 |
| Large Display | Raspberry Pi HDMI/DSI depending on selected model |

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

Open another terminal/session and run:

```bash
python3 hardware/display/cattlepsic_display.py
```

## Prototype Workflow

1. Milk sample is placed for testing.
2. Sensors collect pH, EC, temperature and turbidity readings.
3. Raspberry Pi averages multiple readings.
4. The current edge layer applies rule-based risk screening.
5. Result is classified as Healthy, Attention or High Risk.
6. The latest result is written to `current_status.json`.
7. The large local display reads that status and shows the farmer-friendly result.
8. The same result can also be stored offline, synchronized to the backend and formatted for a thermal receipt.

## Current Status

The sensor-to-result pipeline and a large-display software interface are present as prototypes. Sensor calibration, final display hardware selection, physical printer integration, validated ML forecasting, live cloud synchronization and field validation remain in progress.

> CattleΨic is an early risk-screening prototype and does not replace veterinary diagnosis.
