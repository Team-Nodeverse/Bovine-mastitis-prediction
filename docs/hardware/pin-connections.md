# 🔌 Raspberry Pi Hardware Connections

## Sensor Connections

| Device | Connection |
|---|---|
| pH Sensor | ADS1115 A0 |
| EC Sensor | ADS1115 A1 |
| Turbidity Sensor | ADS1115 A2 |
| ADS1115 SDA | Raspberry Pi GPIO2 / SDA |
| ADS1115 SCL | Raspberry Pi GPIO3 / SCL |
| DS18B20 Data | Raspberry Pi GPIO4 |
| Push Button | Raspberry Pi GPIO17 |
| 16x4 LCD SDA | Raspberry Pi GPIO2 / SDA |
| 16x4 LCD SCL | Raspberry Pi GPIO3 / SCL |

## Communication

- ADS1115 communicates through I2C.
- LCD uses the I2C interface.
- DS18B20 uses the 1-Wire protocol.
- Push button is used to start a milk test.

## Important Hardware Note

Sensor power requirements depend on the exact modules used. All modules must share a common ground and Raspberry Pi GPIO pins must be protected from voltages above their supported logic level.

## Prototype Sensor Channels

```text
ADS1115

A0 → pH
A1 → EC
A2 → Turbidity
A3 → Reserved for future sensor
