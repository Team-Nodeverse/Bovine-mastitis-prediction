# 🍓 Raspberry Pi Edge Module

This folder contains the Raspberry Pi based edge-processing prototype used in CattleΨic.

## Hardware Used

- Raspberry Pi
- ADS1115 ADC
- pH Sensor
- EC Sensor
- Turbidity Sensor
- DS18B20 Temperature Sensor
- 16x4 I2C LCD
- Push Button

## Sensor Mapping

| Sensor | Interface |
|---|---|
| pH Sensor | ADS1115 A0 |
| EC Sensor | ADS1115 A1 |
| Turbidity Sensor | ADS1115 A2 |
| DS18B20 | 1-Wire |
| Push Button | GPIO17 |
| LCD | I2C |

## Installation

From the repository root:

```bash
pip install -r requirements.txt
```

## Run

```bash
python3 cattlepsic_pi.py
```

## Prototype Workflow

1. Milk sample is placed for testing.
2. Sensors collect pH, EC, temperature and turbidity readings.
3. Raspberry Pi averages multiple readings.
4. The current edge layer applies rule-based risk screening.
5. Result is classified as Healthy, Attention or High Risk.
6. Result is displayed on LCD and can be sent to the backend when configured.

## Current Status

The sensor-to-result pipeline is implemented as a prototype. Sensor calibration, validated ML forecasting, live cloud synchronization and field validation remain in progress.

> CattleΨic is an early risk-screening prototype and does not replace veterinary diagnosis.
