# Gender Gap in Life Expectancy and Healthy Life Expectancy
## Statistical, Econometric and Machine Learning Analysis

## Overview

This repository contains the work conducted during my **Bachelor’s internship (L3 MIASHS, 2025–2026)** at the **AGEIS Research Laboratory (Université Grenoble Alpes)**.

The project analyzes gender disparities in life expectancy (LE) and healthy life expectancy (HALE) using international health, socio-economic and demographic data.
It combines exploratory data analysis, econometric modeling, and Machine Learning to identify key determinants and structural patterns across countries.

---

# Research Objectives

- Quantify gender gaps in life expectancy and healthy life expectancy
- Identify health and socio-economic factors associated with these gaps
- Apply panel data econometric methods to control for country heterogeneity
- Use Machine Learning to predict gender gaps and identify country profiles

---

## Repository Structure

.
├── CleanData/             # Cleaned and harmonized datasets
├── EDA/                   # Exploratory Data Analysis (figures & notebooks)
├── Images/                # Main figures used in the report
├── MachineLearning/       # Supervised & unsupervised ML models
├── Regression/            # Econometric models and regression outputs
├── RapportdeStage.pdf     # Final internship report (PDF)
└── README.md


## Data Sources

The analysis relies on international indicators from:

-**World Bank (World Development Indicators)**
-**World Health Organization (WHO – GHO)**
-**United Nations Development Programme (HDI)**
-**Institute for Health Metrics and Evaluation (IHME – GBD)**

Data were cleaned, harmonized and analyzed without extrapolation.
The final comparative analysis focuses on 26 countries, primarily for the year 2021, to ensure temporal consistency.

---

## Methodology

### Exploratory Data Analysis

-Univariate and bivariate statistical analysis
-Temporal evolution of gender gaps
-Cross-country comparison by development status
-Econometric Analysis

### Multiple linear regression (MCO)

-Panel data models (fixed and random effects)
-Specification and diagnostic tests:
  -Hausman test
  -Wooldridge test
  -Breusch–Pagan and White tests
-Robust standard errors clustered at the country level

### Machine Learning

**Supervised learning**

-Linear Regression, Ridge, ElasticNet
-Random Forest, Gradient Boosting
-Temporal validation (train: 2000–2017, test: 2018–2021)

**Unsupervised learning**
-k-means clustering
-Optimal number of clusters selected using silhouette scores
-Identification of homogeneous country profiles

---

## Key Results

-Women live longer than men in almost all countries, but spend more years in poor health on average.
-Health-related factors (notably HIV/AIDS and certain cancers) play a major role in explaining gender gaps.
-After econometric corrections, economic variables show weaker direct effects.
-Simple linear models achieve strong predictive performance while remaining interpretable.
-Clustering highlights structurally distinct country groups according to health and development indicators.

___

## Tools & Technologies

-**Languages**: R, Python
-**Libraries**:
 -R: `tidyverse`, `plm`
 -Python: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`
-**Scientific writing**: LaTeX, Jupyter Notebook

---

## Author

**Mohamed FOFANA**
Bachelor’s degree in MIASHS – Université Grenoble Alpes
Internship at AGEIS Research Laboratory

📅 September 2025 – January 2026
Supervisors:
-Jacques Demongeot
-Julien Grepat

___

## Reference
If you use or refer to this work, please cite the internship report available as
RapportdeStage.pdf in this repository.
