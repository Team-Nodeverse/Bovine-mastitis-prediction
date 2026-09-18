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

Install the required Python packages:

```bash
pip install -r ../../requirements.txt
