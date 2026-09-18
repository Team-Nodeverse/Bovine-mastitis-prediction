# 🏗️ CattleΨic System Architecture

## Overview

CattleΨic uses a Raspberry Pi as the edge-processing unit to collect and analyse multiple milk parameters for early mastitis-risk screening.

## System Architecture

```text
                 MILK SAMPLE
                      │
        ┌─────────────┼─────────────┐
        │             │             │
    pH Sensor     EC Sensor    Turbidity Sensor
        │             │             │
        └──────────┬──┴─────────────┘
                   │
                ADS1115
                   │
                   ▼
              Raspberry Pi
                   │
        ┌──────────┴──────────┐
        │                     │
 Temperature Sensor      Sensor Processing
     DS18B20                  │
                              ▼
                   Filtering & Averaging
                              │
                              ▼
                      Risk Analysis Layer
                              │
                   ┌──────────┼──────────┐
                   ▼          ▼          ▼
                Healthy   Attention   High Risk
                   │
          ┌────────┴─────────┐
          ▼                  ▼
      16x4 LCD        Farmer Dashboard
                             │
                             ▼
                      Backend / Cloud
                             │
                             ▼
                       Health History
