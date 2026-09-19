# ============================================================
# CattlePsiC - Raspberry Pi Edge Health Screening Prototype
# Team Nodeverse
#
# Sensors:
#   ADS1115 A0 -> pH Sensor
#   ADS1115 A1 -> EC Sensor
#   ADS1115 A2 -> Turbidity Sensor
#   DS18B20    -> Temperature Sensor
#   GPIO17     -> Push Button
#
# Local output:
#   Large Raspberry Pi display / touchscreen reads current_status.json
#
# NOTE:
# This prototype provides mastitis RISK INDICATION only.
# It is not a veterinary diagnosis.
# ============================================================

import json
import os
import time

import requests
import RPi.GPIO as GPIO
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from w1thermsensor import W1ThermSensor


# ============================================================
# CONFIGURATION
# ============================================================

DEVICE_ID = "RPI_001"
COW_ID = "COW001"
SERVER_URL = ""
DEVICE_TOKEN = ""
BUTTON_PIN = 17
SAMPLE_COUNT = 50
SAMPLE_DELAY = 0.03
OFFLINE_FILE = "offline_readings.json"
DISPLAY_STATUS_FILE = "current_status.json"


# ============================================================
# SENSOR CALIBRATION PLACEHOLDERS
# ============================================================
# Real calibration must be performed using validated references.

PH_SLOPE = -5.70
PH_OFFSET = 21.34
EC_SLOPE = 2.00
EC_OFFSET = 0.00
TURBIDITY_SLOPE = 1.00
TURBIDITY_OFFSET = 0.00


# ============================================================
# GPIO + I2C + ADC
# ============================================================

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

ph_channel = AnalogIn(ads, ADS.P0)
ec_channel = AnalogIn(ads, ADS.P1)
turbidity_channel = AnalogIn(ads, ADS.P2)
temperature_sensor = W1ThermSensor()


# ============================================================
# LARGE DISPLAY STATUS OUTPUT
# ============================================================

def write_display_status(state, message, sensor_data=None, analysis=None):
    """Write one local JSON state for the integrated display UI."""

    payload = {
        "state": state,
        "message": message,
        "device_id": DEVICE_ID,
        "cow_id": COW_ID,
        "timestamp": int(time.time() * 1000),
    }

    if sensor_data:
        payload["sensor_data"] = sensor_data

    if analysis:
        payload["analysis"] = analysis

    temp_file = DISPLAY_STATUS_FILE + ".tmp"
    with open(temp_file, "w", encoding="utf-8") as file:
        json.dump(payload, file, indent=2)

    os.replace(temp_file, DISPLAY_STATUS_FILE)


# ============================================================
# SENSOR HELPERS
# ============================================================

def average_voltage(channel):
    readings = []

    for _ in range(SAMPLE_COUNT):
        try:
            readings.append(float(channel.voltage))
        except Exception:
            pass
        time.sleep(SAMPLE_DELAY)

    if not readings:
        return 0.0

    return sum(readings) / len(readings)


def convert_ph(voltage):
    return round(voltage * PH_SLOPE + PH_OFFSET, 2)


def convert_ec(voltage):
    return round(voltage * EC_SLOPE + EC_OFFSET, 2)


def convert_turbidity(voltage):
    return round(voltage * TURBIDITY_SLOPE + TURBIDITY_OFFSET, 2)


def read_temperature():
    try:
        return round(temperature_sensor.get_temperature(), 2)
    except Exception as error:
        print("Temperature error:", error)
        return 0.0


# ============================================================
# READ ALL SENSORS
# ============================================================

def read_sensors():
    print("\nReading sensors...")
    write_display_status("reading", "Reading milk sensors...")

    ph_voltage = average_voltage(ph_channel)
    ec_voltage = average_voltage(ec_channel)
    turbidity_voltage = average_voltage(turbidity_channel)
    temperature = read_temperature()

    return {
        "temperature": temperature,
        "ph": convert_ph(ph_voltage),
        "ec": convert_ec(ec_voltage),
        "turbidity": convert_turbidity(turbidity_voltage),
        "raw": {
            "ph_voltage": round(ph_voltage, 4),
            "ec_voltage": round(ec_voltage, 4),
            "turbidity_voltage": round(turbidity_voltage, 4),
        },
    }


# ============================================================
# RISK ANALYSIS ENGINE
# ============================================================
# Prototype heuristic thresholds only.
# Replace with validated ML inference after model validation.


def analyze_risk(data):
    temperature = data["temperature"]
    ph = data["ph"]
    ec = data["ec"]
    turbidity = data["turbidity"]

    risk_points = 0
    reasons = []

    if temperature > 39.5 or temperature < 37.5:
        risk_points += 2
        reasons.append("Abnormal temperature")

    if ph >= 6.8:
        risk_points += 2
        reasons.append("Elevated pH")
    elif ph >= 6.6:
        risk_points += 1
        reasons.append("pH requires attention")

    if ec >= 5.8:
        risk_points += 2
        reasons.append("High conductivity")
    elif ec >= 5.0:
        risk_points += 1
        reasons.append("EC requires attention")

    if turbidity >= 3.0:
        risk_points += 2
        reasons.append("Abnormal turbidity")

    if risk_points >= 4:
        status = "HIGH RISK"
        risk_level = "High"
    elif risk_points >= 2:
        status = "ATTENTION"
        risk_level = "Medium"
    else:
        status = "HEALTHY"
        risk_level = "Low"

    if not reasons:
        reasons.append("Readings within prototype range")

    return {
        "status": status,
        "risk_level": risk_level,
        "risk_score": min(risk_points * 15, 100),
        "reasons": reasons,
    }


# ============================================================
# OFFLINE STORAGE
# ============================================================

def save_offline(packet):
    data = []

    if os.path.exists(OFFLINE_FILE):
        try:
            with open(OFFLINE_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
        except Exception:
            data = []

    data.append(packet)

    with open(OFFLINE_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)

    print("Reading saved offline.")


# ============================================================
# SEND TO BACKEND
# ============================================================

def send_to_server(packet):
    if not SERVER_URL:
        print("Cloud sync disabled.")
        save_offline(packet)
        return False

    endpoint = SERVER_URL.rstrip("/") + "/api/device-data"
    headers = {"Content-Type": "application/json"}

    if DEVICE_TOKEN:
        headers["Authorization"] = "Bearer " + DEVICE_TOKEN

    try:
        response = requests.post(
            endpoint,
            json=packet,
            headers=headers,
            timeout=10,
        )

        if 200 <= response.status_code < 300:
            print("Cloud synced successfully.")
            return True

        print("Server error:", response.status_code, response.text)

    except Exception as error:
        print("Network error:", error)

    save_offline(packet)
    return False


# ============================================================
# PROCESS ONE TEST
# ============================================================

def perform_test():
    sensor_data = read_sensors()
    analysis = analyze_risk(sensor_data)

    packet = {
        "device_id": DEVICE_ID,
        "cow_id": COW_ID,
        "temperature": sensor_data["temperature"],
        "ph": sensor_data["ph"],
        "ec": sensor_data["ec"],
        "turbidity": sensor_data["turbidity"],
        "timestamp": int(time.time() * 1000),
        "risk_status": analysis["status"],
        "risk_level": analysis["risk_level"],
    }

    print("\n======================")
    print("CattlePsiC Test")
    print("======================")
    print("Temperature:", sensor_data["temperature"], "C")
    print("pH:", sensor_data["ph"])
    print("EC:", sensor_data["ec"])
    print("Turbidity:", sensor_data["turbidity"])
    print("Status:", analysis["status"])
    print("Risk:", analysis["risk_level"])
    print("Reasons:", ", ".join(analysis["reasons"]))

    write_display_status(
        "result",
        "Milk test complete",
        sensor_data=sensor_data,
        analysis=analysis,
    )

    synced = send_to_server(packet)
    print("Status:", "CLOUD SYNCED" if synced else "OFFLINE SAVED")


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():
    print("\nCattlePsiC")
    print("Team Nodeverse")
    print("Raspberry Pi Edge Prototype")
    print("Press button to start test.")

    write_display_status("ready", "Press button to start milk test")

    try:
        while True:
            if GPIO.input(BUTTON_PIN) == GPIO.LOW:
                perform_test()
                time.sleep(1.5)
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nProgram stopped.")
        write_display_status("stopped", "Device stopped")

    finally:
        GPIO.cleanup()


if __name__ == "__main__":
    main()
