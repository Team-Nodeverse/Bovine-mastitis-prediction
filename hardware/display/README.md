# 🖥️ Integrated Large Display

CattleΨic is moving away from the small 16x4 LCD concept and is being designed around a **larger Raspberry Pi-connected display / touchscreen** similar to a compact tablet screen.

## Purpose

The local screen is intended to show:

- Cow ID
- Live pH
- Electrical conductivity (EC)
- Temperature
- Turbidity
- Test progress
- Healthy / Attention / High Risk result
- Short next-step guidance
- Printer/report status

## Interface Approach

The Raspberry Pi sensor program writes the latest local result to:

```text
hardware/raspberry-pi/current_status.json
```

The local display application reads this file and updates the full-screen interface.

This keeps the sensing code independent from the exact screen model.

## Supported Display Direction

The final prototype can use a Raspberry Pi compatible:

- HDMI display
- DSI touchscreen
- 5–7 inch integrated touchscreen

The exact model will be finalized based on enclosure size, power requirement, brightness, touch support and cost.

## Run Display UI

On Raspberry Pi OS with a graphical desktop:

```bash
python3 hardware/display/cattlepsic_display.py
```

If Tkinter is not installed:

```bash
sudo apt install python3-tk
```

## Status

| Item | Status |
|---|---|
| Small 16x4 LCD | Removed from current design direction |
| Large-display software interface | ✅ Repository prototype available |
| Final display model | 🟡 To be finalized |
| Enclosure integration | 🟡 Planned |
| Touch controls | 🟡 Planned |
| Field testing | 🔴 Pending |

> The existing hardware prototype photograph is retained only as evidence of earlier prototype progress. The final hardware design will use the larger integrated display.
