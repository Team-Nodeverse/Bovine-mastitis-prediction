# 🧠 CattleΨic Random Forest Model Card

## Model Summary

**Model:** Random Forest classifier  
**Purpose:** Mastitis-risk classification from milk-quality and sensor-derived features  
**Deployment target:** Raspberry Pi edge device  
**Current project stage:** Trained baseline model with deployment integration and broader validation continuing

## Current Input Direction

The current device pipeline supports:

- milk pH
- electrical conductivity (EC)
- milk temperature
- turbidity

The exact feature order used by the trained artifact must remain identical between training and Raspberry Pi inference.

## Farmer-Facing Output

The device UI presents a simple risk result such as:

- Low Risk
- Moderate Risk
- High Risk

The farmer-facing categories are designed for screening and decision support rather than confirmed veterinary diagnosis.

## Current Completed Work

- Random Forest training completed on the currently available labelled dataset
- tabular sensor-feature workflow established
- edge deployment architecture selected
- farmer-facing risk-output structure defined

## Current Validation / Integration Work

- export / load final trained artifact in the Raspberry Pi inference path
- lock exact feature order and preprocessing steps
- document dataset version used for training
- publish confusion matrix and measured evaluation metrics
- validate threshold mapping for Low / Moderate / High risk
- test across more cows, milk conditions and farms

## Metrics to Report

Only measured results from the actual evaluation run should be published:

- accuracy
- sensitivity / recall
- specificity
- precision
- F1-score
- confusion matrix
- ROC-AUC where appropriate

## SIH26109 Forecasting Note

A trained classifier is one part of the SIH26109 solution. Demonstrating true 7–14 day pre-clinical forecasting requires longitudinal records where the model is evaluated on information available before clinical onset. This remains a dedicated validation stage.

## Future Feature Expansion

Larger validated versions can add:

- SCC
- milk yield
- breed, age and lactation number
- previous mastitis / treatment history
- body temperature
- activity and rumination
- environmental temperature / humidity
- farm hygiene and management context

## Deployment Principle

CattleΨic uses a modular design so the trained model can be updated independently from the sensor-acquisition, dashboard, display and thermal-printer layers.
