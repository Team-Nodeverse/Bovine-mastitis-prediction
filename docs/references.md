# 📚 Research & Evidence Base

CattleΨic is being developed around evidence from bovine mastitis research, sensor-based livestock monitoring and machine-learning studies. The references below are used to guide feature selection, system design and the validation roadmap. They are not presented as proof that the current CattleΨic prototype has already achieved the same performance.

## 1. SIH26109 Problem Statement

**Smart India Hackathon 2026 — SIH26109:** AI-Based Predictive Modelling for Early Forecasting of Bovine Mastitis in Indian Dairy Farms.

Key requirements relevant to CattleΨic include multi-source data, animal-wise and herd-level risk scores, real-time alerts, dashboards, mobile/multilingual deployment, sensor-based hardware, cloud integration and 7–14 day early forecasting.

Reference mirror:
https://github.com/vedantchalke36/sih-2026-problem-statements/blob/main/ps_2026/SIH26109.md

## 2. MasPA — Machine Learning for Mastitis Risk

N. Abdul Ghafoor and B. Sitkowska, "MasPA: A Machine Learning Application to Predict Risk of Mastitis in Cattle from AMS Sensor Data," AgriEngineering, 2021.

- Used data from 6,600 cattle.
- Compared 26 classification models.
- Applied hyperparameter tuning and K-fold cross-validation.
- Built a Random-Forest-based web application.

Paper:
https://doi.org/10.3390/agriengineering3030037

Open-source implementation:
https://github.com/naeemmrz/MasPA.py

## 3. Explainable Multi-Source Mastitis Detection

GSSI mastitis-detection project demonstrates a larger multi-source ML workflow using productive, reproductive, clinical, demographic and electrical-conductivity data.

It includes Random Forest, XGBoost, LightGBM and CatBoost models, feature engineering and explainability-driven feature analysis.

Repository:
https://github.com/gssi/mastitis-detection

## 4. Dairy Disease Monitoring Web Application

University of Peradeniya project for subclinical mastitis monitoring combines an ML model with frontend, backend and web-app components. Inputs include lactation number, pH, conductivity, fat content and salt levels.

Repository:
https://github.com/cepdnaclk/e18-6sp-Disease-Monitoring-in-dairy-industry

## 5. Intelligent Wearable Cattle Monitoring

Z. Yu et al., "Design of an intelligent wearable device for real-time cattle health monitoring," Frontiers in Robotics and AI, 2024.

The work demonstrates continuous temperature and movement monitoring, solar-powered operation, local storage, ergonomic wearable design and field testing on cattle.

Article:
https://pmc.ncbi.nlm.nih.gov/articles/PMC11617366/

## 6. Additional Public Mastitis Data Resource

The following public repository contains mastitis-related datasets and analysis code, but its genomics-focused data is not a direct replacement for the longitudinal farm/sensor dataset required by SIH26109.

https://github.com/MdRabiulAuwul/Mastitis-Data

## Validation Principles for CattleΨic

Before making predictive-performance claims, the project should document:

- source and size of labelled data
- train/validation/test split strategy
- animal-wise or farm-wise leakage prevention
- sensitivity / recall
- specificity
- precision
- F1-score
- ROC-AUC where appropriate
- confusion matrix
- calibration of risk probabilities
- performance across farms, breeds and lactation stages
- separate evaluation of 7-day and 14-day forecasting horizons

## Current Position

The present CattleΨic Raspberry Pi prototype uses a rule-based screening layer for hardware and end-to-end pipeline validation. A trained and externally validated forecasting model remains under development.
