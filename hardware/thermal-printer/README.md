# 🧾 Thermal Printer Module

This folder documents the planned compact thermal-printer integration for the CattleΨic prototype.

## Target Use

After a milk test, the Raspberry Pi should be able to provide the same result through:

- 16x4 LCD
- Farmer dashboard/mobile view
- Printed thermal receipt

## Suggested Device Class

Use a compact **58 mm thermal receipt printer** that supports a Raspberry Pi-compatible communication method such as USB or UART/TTL.

The final printer model should be selected only after checking:

- Supported voltage and current
- Raspberry Pi communication interface
- ESC/POS or vendor command support
- Print width and characters per line
- Paper availability
- Mounting size
- Thermal protection and enclosure ventilation

## Power Safety

Do **not** power the printer directly from a Raspberry Pi GPIO pin. Thermal printers can draw substantially more current than GPIO can supply. Use the printer's required external power source and follow the selected module datasheet.

## Integration Sequence

```text
Raspberry Pi Test Result
        ↓
Receipt Formatter
        ↓
Printer Driver / ESC-POS Layer
        ↓
58 mm Thermal Printer
        ↓
Farmer Test Slip
```

## Current Repository Status

- Receipt concept: defined
- Receipt formatter: available in this folder
- Exact printer driver: pending printer selection
- Physical wiring and field test: pending
