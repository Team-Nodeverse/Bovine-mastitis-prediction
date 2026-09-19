# 🎯 SIH26109 Requirement Alignment

This document maps the official SIH26109 expectations to the current CattleΨic prototype and planned work.

| SIH26109 expectation | CattleΨic status | Evidence / next action |
|---|---|---|
| Sensor-based hardware prototype | ✅ Implemented prototype | Raspberry Pi + pH + EC + temperature + turbidity + LCD |
| Milk conductivity monitoring | ✅ Implemented prototype | ADS1115 A1 pipeline |
| Milk temperature monitoring | ✅ Implemented prototype | DS18B20 pipeline |
| Milk pH monitoring | ✅ Implemented prototype | ADS1115 A0 pipeline |
| Multi-parameter risk screening | ✅ Implemented prototype | pH + EC + temperature + turbidity |
| Local / offline operation | ✅ Implemented prototype | Local LCD + offline JSON storage |
| Farmer-facing dashboard | ✅ Prototype | Dashboard prototype documented |
| Cloud data integration | 🟡 In progress | Backend POST support exists; live deployment pending |
| Animal-wise health history | 🟡 Prototype | Cow ID structure present; production persistence pending |
| ML-based forecasting | 🟡 In progress | Current edge layer is rule-based; labelled ML pipeline required |
| 7–14 day forecasting | 🔴 Not validated | Requires longitudinal pre-disease records and horizon-specific validation |
| Herd-level risk assessment | 🔴 Planned | Add herd aggregation and farm-level risk dashboard |
| SCC integration | 🔴 Planned | Add SCC/lab data as optional validated feature |
| Historical treatment / disease data | 🔴 Planned | Add cow health-history fields and ingestion |
| Activity / rumination monitoring | 🔴 Planned | Wearable/IMU extension |
| Environmental / farm hygiene data | 🔴 Planned | Add temperature-humidity/hygiene/manual input layer |
| Real-time farmer/vet alerts | 🔴 Planned | SMS / WhatsApp / app alert integration |
| Preventive recommendations | 🔴 Planned | Rule + model-explanation based decision-support layer |
| Mobile / multilingual interface | 🔴 Planned | Farmer app / PWA with Hindi + regional-language support |
| GIS / hotspot visualization | 🔴 Planned | Farm geo-tagging and risk-map layer |
| Field validation | 🔴 Pending | Requires dairy-farm and veterinary collaboration |
| Data security and access control | 🟡 Architecture planned | Device authentication, RBAC and secure cloud policies |

## Priority for the Next Prototype Iteration

1. Calibrate sensors and document calibration curves.
2. Build a reproducible labelled dataset pipeline.
3. Train a baseline ML model with proper train/test validation.
4. Add cow-history and herd-level aggregation.
5. Connect live Raspberry Pi data to the dashboard.
6. Add alerting and field-validation protocol.
7. Evaluate 7-day and 14-day forecasting separately.

## Important Positioning

CattleΨic should currently be presented as an **integrated edge-assisted mastitis risk-screening prototype with an ML-ready architecture**. Claims of validated 7–14 day forecasting should only be made after longitudinal field data and proper external validation are available.
