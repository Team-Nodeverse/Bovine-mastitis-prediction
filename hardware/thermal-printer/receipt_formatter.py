"""CattlePsiC receipt formatting scaffold.

This module formats a test result as plain text that can later be sent to a
58 mm thermal printer driver (for example, an ESC/POS-compatible driver).
It does not claim that a physical printer is already connected or validated.
"""

from datetime import datetime


def build_receipt(result: dict) -> str:
    timestamp = result.get("timestamp")
    if isinstance(timestamp, (int, float)):
        # Raspberry Pi code currently uses milliseconds.
        timestamp = datetime.fromtimestamp(timestamp / 1000).strftime("%d-%m-%Y %H:%M")
    elif not timestamp:
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M")

    lines = [
        "================================",
        "          CattlePsiC",
        "       Team Nodeverse",
        "--------------------------------",
        f"Cow ID      : {result.get('cow_id', 'N/A')}",
        f"Test ID     : {result.get('test_id', 'N/A')}",
        f"Date/Time   : {timestamp}",
        "--------------------------------",
        f"pH          : {result.get('ph', 'N/A')}",
        f"EC          : {result.get('ec', 'N/A')}",
        f"Temperature : {result.get('temperature', 'N/A')} C",
        f"Turbidity   : {result.get('turbidity', 'N/A')}",
        "--------------------------------",
        f"Risk Status : {result.get('risk_status', 'N/A')}",
        "--------------------------------",
        "Screening result only.",
        "Consult a veterinarian when needed.",
        "================================",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    demo = {
        "cow_id": "COW001",
        "test_id": "DEMO-001",
        "ph": 6.72,
        "ec": 5.20,
        "temperature": 38.10,
        "turbidity": 2.40,
        "risk_status": "ATTENTION",
    }
    print(build_receipt(demo))
