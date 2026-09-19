# 🧠 CattleΨic ML Module

CattleΨic now includes a **trained Random Forest model** built on the currently available labelled mastitis dataset. The current development focus is on integrating the trained artifact cleanly with the Raspberry Pi inference pipeline and documenting evaluation evidence.

## Current ML Status

### ✅ Completed

- Random Forest model training
- Feature-based mastitis-risk classification workflow
- Model architecture selected for edge deployment
- Risk output designed for Low / Moderate / High farmer-facing states

### 🟡 Current Integration / Validation Work

- Connect the trained model artifact to the final Raspberry Pi inference path
- Record the exact dataset version and feature order used during training
- Document train / validation / test split
- Add confusion matrix and evaluation metrics
- Calibrate decision thresholds for farmer-facing risk levels
- Validate robustness on more cows, farms and milk conditions

## Current Core Sensor Features

The present device pipeline supports:

- pH
- electrical conductivity (EC)
- milk temperature
- turbidity

Additional historical features can be introduced when validated records are available.

## Model

**Primary model:** Random Forest

Why it fits the prototype:

- handles nonlinear relationships between milk parameters
- supports feature importance / explainability
- practical for tabular sensor data
- can be exported for local inference on a Raspberry Pi

## Evaluation Evidence to Publish

The repository should report the actual measured values from the training notebook/logs for:

- sensitivity / recall
- specificity
- precision
- F1-score
- confusion matrix
- ROC-AUC where appropriate
- probability calibration

Do not replace these with estimated values. Only publish the metrics produced by the actual training/evaluation run.

## Forecasting Validation

The SIH26109 target includes early forecasting before clinical symptoms. A trained classifier is an important step, but **7-day and 14-day forecasting performance should be demonstrated separately using longitudinal pre-disease records**.

This is a validation task, not a model-training task.

## Advanced Feature Expansion

Future large-scale versions can combine:

### Animal history
- breed
- age
- lactation number
- days in milk
- previous mastitis episodes
- treatment history

### Laboratory / production data
- SCC
- milk yield
- other validated quality indicators

### Wearable / behaviour data
- body temperature
- activity
- rumination
- feeding behaviour

### Farm context
- ambient temperature / humidity
- hygiene indicators
- milking schedule
- nutrition / feeding information

## Model Artifact

When the final trained `.pkl` / `.joblib` artifact and training notebook are ready for public submission, place them under this folder together with the exact feature-order and preprocessing information used during training.
