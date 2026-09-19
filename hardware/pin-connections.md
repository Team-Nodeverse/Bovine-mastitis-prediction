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
| Large Display / Touchscreen | HDMI / DSI / USB-touch depending final panel |
| 58 mm Thermal Printer | USB or UART/TTL depending final printer module |

## Communication

- ADS1115 communicates through I2C.
- DS18B20 uses the 1-Wire protocol.
- Push button starts / controls a milk test.
- The earlier 16x4 LCD wiring has been removed from the current hardware revision.
- The larger display is handled as a Raspberry Pi display device rather than a small character LCD.
- The thermal printer interface will depend on the exact selected printer model.

## Prototype Sensor Channels

```text
ADS1115
A0 → pH
A1 → EC
A2 → Turbidity
A3 → Reserved for future validated sensor input
```

## Safety Note

Sensor modules, displays and thermal printers can use different supply voltages and current levels. Verify the exact datasheets before wiring, use a common ground where required, and never power a thermal printer directly from a Raspberry Pi GPIO pin.
