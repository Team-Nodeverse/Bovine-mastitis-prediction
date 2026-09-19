<p align="center">
  <img src="cattlepsic-logo.png" width="170" alt="CattlePsiC Logo">
</p>

<h1 align="center">CattleΨic</h1>

<p align="center">
  <b>AI-Assisted Edge System for Early Mastitis Risk Screening in Dairy Cattle</b>
</p>

<p align="center">
  <b>Team Nodeverse</b> • SIH26109 • Raspberry Pi • Multi-Sensor Milk Analysis • Farmer Dashboard
</p>

---

## 🚀 Project Overview

CattleΨic is a Raspberry Pi based cattle-health screening prototype designed to identify abnormal milk patterns associated with bovine mastitis risk.

The current prototype combines **pH, electrical conductivity (EC), temperature and turbidity** measurements with local edge processing, offline storage, LCD output and a farmer-facing dashboard architecture.

A compact **58 mm thermal receipt printer** is also being designed as a current prototype extension so a farmer can receive a physical test slip alongside the digital result. The receipt formatter is present in the repository; physical printer integration and field testing are still pending.

> **Current stage:** integrated prototype / approximately 60% development. ML forecasting and field validation are still in progress.

> **Important:** CattleΨic currently provides risk screening and decision support. It is not a veterinary diagnosis and does not yet claim validated 7–14 day forecasting.

---

## 📸 Prototype Preview

<p align="center">
  <img src="dashboard-home.png" width="47%" alt="CattlePsiC Dashboard">
  <img src="assets/hardware-prototype.jpeg" width="47%" alt="CattlePsiC Hardware Prototype">
</p>

---

## ✨ Key Features

- Raspberry Pi edge processing
- pH, EC, temperature and turbidity sensing pipeline
- ADS1115 analog sensor interface
- Multiple-reading averaging
- 16x4 LCD local result
- Healthy / Attention / High Risk screening states
- Offline JSON storage when cloud is unavailable
- Backend POST support for future live synchronization
- Farmer dashboard prototype
- Cow-wise test-history architecture
- Thermal receipt output design + formatter scaffold
- ML-ready architecture with validation roadmap

## ⚙️ End-to-End Flow

```text
Milk Sample
     ↓
pH + EC + Temperature + Turbidity Sensors
     ↓
ADS1115 + Raspberry Pi
     ↓
Filtering + Multiple Reading Averaging
     ↓
Current Rule-Based Risk Screening
     ↓
Healthy / Attention / High Risk
     ↓
┌──────────────┬──────────────────┬─────────────────────┐
│ 16x4 LCD     │ Dashboard/Cloud  │ Thermal Receipt     │
│              │ + Offline Record │ (integration plan)  │
└──────────────┴──────────────────┴─────────────────────┘
```

## 🔧 Hardware Architecture

| Component | Function | Status |
|---|---|---|
| Raspberry Pi | Main edge-processing controller | Prototype |
| ADS1115 | Analog sensor interface | Prototype |
| pH Sensor | Milk pH measurement | Calibration pending |
| EC Sensor | Electrical conductivity measurement | Calibration pending |
| DS18B20 | Temperature measurement | Prototype |
| Turbidity Sensor | Turbidity / optical-change input | Calibration/evidence validation pending |
| 16x4 LCD | Local risk result display | Prototype |
| Push Button | Starts a milk test | Prototype |
| 58 mm Thermal Printer | Prints farmer test receipt | Planned current-device integration |

## 🧾 Farmer Receipt Output

The planned receipt printer is intended to print the same test result that is shown digitally. The slip can include:

- Cow ID
- Test ID and date/time
- pH
- EC
- temperature
- turbidity
- screening risk status
- short screening disclaimer

This is useful for farms with intermittent connectivity and for sharing a result physically with a farmer or veterinarian.

➡️ [View thermal receipt printer integration design](docs/thermal-receipt-printer.md)

## 📈 Prototype Status

### ✅ Implemented / Demonstrated in Prototype

- Raspberry Pi sensor acquisition pipeline
- pH, EC, temperature and turbidity input handling
- Multiple-reading averaging
- Local LCD result
- Rule-based risk screening
- Offline result storage
- Backend communication support
- Farmer dashboard prototype
- Receipt text format + Raspberry Pi receipt formatter scaffold

### 🟡 In Progress

- Sensor calibration with validated reference samples
- Live Raspberry Pi-to-cloud synchronization
- Physical thermal-printer integration
- Labelled longitudinal dataset collection
- ML training and model validation
- Farmer/veterinarian alerting

### 🔴 Requires Future Validation

- 7–14 day pre-clinical forecasting
- SCC/laboratory data integration
- Herd-level risk forecasting
- Wearable activity / rumination monitoring
- Multi-farm external validation
- GIS disease-risk mapping

## 🎯 SIH26109 Alignment

The official SIH26109 scope asks for an integrated system combining sensor hardware, multi-source historical data, AI/ML forecasting, animal-wise and herd-level risk scores, alerts, dashboards, mobile/multilingual access and field validation.

CattleΨic currently focuses on building the **edge sensor-to-dashboard foundation** while keeping the ML forecasting layer explicitly under validation.

➡️ [View detailed SIH26109 requirement mapping](docs/sih26109-requirements.md)

## 🧠 AI / ML Roadmap

The present Raspberry Pi code uses a transparent rule-based screening layer to validate the hardware and end-to-end data pipeline.

The next ML stage will compare models such as **Logistic Regression, Random Forest and gradient-boosted trees**, using proper train/validation/test methodology and metrics such as sensitivity, specificity, precision, F1-score, ROC-AUC and calibration.

➡️ [View ML development roadmap](ml/README.md)

## 🔬 Research-Backed Design Direction

The project roadmap is informed by mastitis ML studies, multi-source livestock-health pipelines and continuous cattle-monitoring research. These external results guide our design; they are **not** presented as CattleΨic performance claims.

➡️ [Research & evidence base](docs/references.md)

## 📊 Comparison & Gap Analysis

A dedicated comparison document tracks what is already present in CattleΨic, what public mastitis projects demonstrate, and what remains to fully meet SIH26109.

➡️ [View comparison and gap analysis](docs/comparison-gap-analysis.md)

## 🔗 Project Documentation

- [System Architecture](docs/architecture.md)
- [SIH26109 Requirement Alignment](docs/sih26109-requirements.md)
- [Comparison & Gap Analysis](docs/comparison-gap-analysis.md)
- [Thermal Receipt Printer Integration](docs/thermal-receipt-printer.md)
- [Hardware Pin Connections](hardware/pin-connections.md)
- [Raspberry Pi Module](hardware/raspberry-pi/README.md)
- [Thermal Printer Hardware Module](hardware/thermal-printer/README.md)
- [Software Documentation](software/README.md)
- [Prototype Demo](docs/demo.md)
- [Research & References](docs/references.md)
- [ML Roadmap](ml/README.md)

## 🔮 Future Scope

- Calibrated and validated sensor system
- Trained forecasting model using longitudinal labelled data
- SCC and laboratory-record integration
- Animal-history and treatment-record integration
- Wearable body-temperature / activity / rumination module
- Herd-level analytics
- SMS / WhatsApp / app alerts
- Veterinary dashboard
- Hindi and regional-language farmer interface
- GIS risk-map layer
- Portable low-power enclosure
- Real dairy-farm field validation

## 👥 Team

**Team Nodeverse**

Building practical, farmer-friendly technology for livestock health and precision dairy management.
