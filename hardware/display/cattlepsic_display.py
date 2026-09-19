"""CattlePsiC large local display UI.

Designed for a Raspberry Pi HDMI/DSI touchscreen or tablet-like display.
Reads current_status.json written by cattlepsic_pi.py and shows the latest
sensor values and screening status in a simple full-screen interface.
"""

import json
import os
import tkinter as tk

STATUS_FILE = os.path.join(
    os.path.dirname(__file__),
    "..",
    "raspberry-pi",
    "current_status.json",
)

REFRESH_MS = 1000


class CattlePsiCDisplay:
    def __init__(self, root):
        self.root = root
        self.root.title("CattlePsiC")
        self.root.attributes("-fullscreen", True)

        self.title = tk.Label(root, text="CattleΨic", font=("Arial", 34, "bold"))
        self.title.pack(pady=(25, 5))

        self.subtitle = tk.Label(
            root,
            text="Bovine Mastitis Risk Screening",
            font=("Arial", 18),
        )
        self.subtitle.pack(pady=(0, 20))

        self.status = tk.Label(root, text="Starting...", font=("Arial", 28, "bold"))
        self.status.pack(pady=10)

        self.values = tk.Label(
            root,
            text="Waiting for sensor data",
            font=("Arial", 22),
            justify="left",
        )
        self.values.pack(pady=20)

        self.message = tk.Label(root, text="", font=("Arial", 16), wraplength=900)
        self.message.pack(pady=10)

        self.exit_button = tk.Button(
            root,
            text="Exit Display",
            font=("Arial", 14),
            command=root.destroy,
        )
        self.exit_button.pack(side="bottom", pady=20)

        self.refresh()

    def load_status(self):
        try:
            with open(STATUS_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception:
            return None

    def refresh(self):
        data = self.load_status()

        if data:
            state = data.get("state", "ready")
            message = data.get("message", "")
            sensor_data = data.get("sensor_data", {})
            analysis = data.get("analysis", {})

            if state == "result":
                self.status.config(text=analysis.get("status", "RESULT"))
                self.values.config(
                    text=(
                        f"Cow ID: {data.get('cow_id', '-') }\n"
                        f"pH: {sensor_data.get('ph', '-')}\n"
                        f"EC: {sensor_data.get('ec', '-')}\n"
                        f"Temperature: {sensor_data.get('temperature', '-')} °C\n"
                        f"Turbidity: {sensor_data.get('turbidity', '-')}"
                    )
                )
            elif state == "reading":
                self.status.config(text="READING SAMPLE")
                self.values.config(text="Collecting and averaging sensor readings...")
            elif state == "stopped":
                self.status.config(text="DEVICE STOPPED")
                self.values.config(text="")
            else:
                self.status.config(text="READY")
                self.values.config(text="Press the device button to start a milk test")

            self.message.config(text=message)

        self.root.after(REFRESH_MS, self.refresh)


if __name__ == "__main__":
    app_root = tk.Tk()
    CattlePsiCDisplay(app_root)
    app_root.mainloop()
