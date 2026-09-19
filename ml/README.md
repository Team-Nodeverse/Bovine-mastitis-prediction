# 🧠 CattleΨic ML Module

The current CattleΨic hardware prototype uses rule-based risk screening. This folder defines the next step: a reproducible ML forecasting pipeline that can be trained only when properly labelled data is available.

## Planned Input Features

### Milk and sensor features
- pH
- electrical conductivity (EC)
- milk temperature
- turbidity
- milk yield
- SCC when available

### Animal-history features
- breed
- age
- lactation number
- days in milk
- previous mastitis episodes
- treatment history
- vaccination status

### Behaviour / wearable features
- body temperature
- activity
- rumination
- feeding behaviour

### Farm and environmental features
- ambient temperature / humidity
- housing and hygiene indicators
- milking schedule and procedure
- nutrition / feeding information

## Baseline Models to Compare

- Logistic Regression
- Random Forest
- XGBoost / gradient boosting

Model selection should be based on validation performance, interpretability, computational cost and robustness—not on training accuracy alone.

## Evaluation

At minimum report:

- sensitivity / recall
- specificity
- precision
- F1-score
- confusion matrix
- ROC-AUC where appropriate
- calibration of predicted risk

For the SIH26109 forecasting goal, evaluate **7-day and 14-day pre-clinical horizons separately**.

## Data Leakage Warning

Records from the same cow or same disease episode should not be split in a way that leaks future information into training. Prefer cow-wise, time-aware and ideally farm-wise validation.

## Current Status

🟡 ML integration and validation are in progress. No clinically validated performance claim is made by the current repository.
