# Finverse: Instant Fraud Alerts

## Project Overview

Finverse: Instant Fraud Alerts is a machine learning based fraud detection project designed to identify potentially fraudulent financial transactions and support faster fraud monitoring.

The project uses the BankSim transaction dataset and applies exploratory data analysis, behavioral feature engineering and XGBoost classification to identify fraudulent transactions.

The current implementation focuses on transaction analysis and machine learning model development. Real-time transaction streaming and automated alert generation are planned as future enhancements.

---

## Problem Statement

Financial transaction datasets contain a large number of genuine transactions and a much smaller number of fraudulent transactions.

Because fraudulent transactions are rare and may follow different behavioral patterns, identifying them using only individual transaction attributes can be challenging.

Finverse aims to identify suspicious transaction patterns using machine learning and transaction behavior-based features.

---

## Project Objective

The main objectives of Finverse are:

- Analyze financial transaction data.
- Identify patterns associated with fraudulent transactions.
- Create behavioral features based on recent transaction activity.
- Train a machine learning model for fraud detection.
- Evaluate the model using a suitable metric for imbalanced classification.
- Present fraud-related insights through a monitoring dashboard concept.

---

## Dataset

The project uses the BankSim transaction dataset.

### Dataset Statistics

| Metric | Value |
|---|---:|
| Total Transactions | 594,643 |
| Fraud Transactions | 7,200 |
| Genuine Transactions | 587,443 |
| Fraud Rate | Approximately 1.21% |

The dataset is highly imbalanced because genuine transactions greatly outnumber fraudulent transactions.

The raw dataset is not included in this repository.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Jupyter Notebook
- Streamlit

---

## Project Workflow

```text
BankSim Transaction Data
          ↓
Data Loading & Cleaning
          ↓
Exploratory Data Analysis
          ↓
Behavioral Feature Engineering
          ↓
Categorical Encoding
          ↓
Train/Test Split
          ↓
XGBoost Classifier
          ↓
AUPRC Evaluation
          ↓
Feature Importance
          ↓
Fraud Risk Insights
```

---

## Exploratory Data Analysis

The project analyzes different characteristics of fraudulent transactions, including:

- Age
- Gender
- Transaction category
- Transaction amount
- Customer transaction behavior

The analysis helps understand patterns within fraudulent transactions.

---

## Feature Engineering

Behavioral features were created to capture recent transaction activity.

### Customer Transaction Features

The project calculates customer transaction counts over:

- 1 day
- 7 days
- 30 days

### Customer-Merchant Transaction Features

The project also calculates customer-merchant transaction counts over:

- 1 day
- 7 days
- 30 days

These features provide additional context about transaction frequency instead of looking only at the current transaction.

---

## Categorical Encoding

The following categorical columns are label encoded:

- Age
- Gender
- Category

Customer, merchant, zipcode and step columns are removed from the final modeling features according to the notebook workflow.

---

## Machine Learning Model

The project uses an **XGBoost Classifier** for fraud detection.

XGBoost is used to classify transactions into:

- Genuine transactions
- Fraudulent transactions

Because fraud is a minority class, positive-class weighting is used during model training to address class imbalance.

---

## Model Evaluation

Fraud detection is a highly imbalanced classification problem, so accuracy alone may not provide a useful picture of model performance.

The project uses **Area Under the Precision-Recall Curve (AUPRC)** as the primary evaluation metric.

### Model Comparison

| Model Setup | AUPRC |
|---|---:|
| Standard Features | 0.8331 |
| Feature-Engineered Features | 0.8812 |

Feature engineering improved AUPRC by approximately:

**0.0481 points**

or

**4.81 percentage points**

This corresponds to approximately **5.77% relative improvement** over the baseline.

---

## Why AUPRC?

Fraudulent transactions represent only a small percentage of all transactions.

In such an imbalanced dataset, accuracy can be misleading because a model could achieve high accuracy by mostly predicting the majority class.

AUPRC focuses on the relationship between:

- Precision
- Recall

for the positive class, which makes it useful for evaluating fraud detection performance.

---

## Dashboard / Monitoring

The project includes a dashboard concept for presenting fraud-related insights.

The dashboard focuses on:

1. Fraud vs genuine transaction volume
2. Fraud transaction amount analysis
3. Fraud category distribution
4. Fraud profile by age and gender
5. Customer transaction-frequency behavior
6. Model performance comparison
7. Feature-engineering impact
8. Risk-monitoring workflow

---

## Risk Monitoring Workflow

```text
Transaction
     ↓
Behavioral Features
     ↓
XGBoost Score
     ↓
Risk Flag
     ↓
Analyst Review
```

The current notebook demonstrates the analytical and machine learning pipeline.

A production implementation can connect the scoring stage to a live transaction stream and an automated alerting service.

---

## Key Insights

- The dataset contains a very small proportion of fraudulent transactions.
- Fraud detection is therefore an imbalanced classification problem.
- Recent customer transaction activity provides useful behavioral information.
- Customer-merchant transaction frequency can provide additional context.
- Feature engineering improved AUPRC from 0.8331 to 0.8812.
- The dashboard concept helps present fraud-related findings in an easier monitoring format.

---

## Repository Structure

```text
Finverse-Fraud-Detection/
│
├── assets/
│   └── Finverse_Dashboard_Presentation.pptx
│
├── dashboard/
│   └── dashboard.py
│
├── data/
│   └── README.md
│
├── docs/
│   ├── PROJECT_EXPLANATION.md
│   ├── INTERVIEW_QUESTIONS.md
│   └── DASHBOARD_GUIDE.md
│
├── models/
│   └── README.md
│
├── notebooks/
│   └── Finverse_Fraud_Detection_BankSim.ipynb
│
├── src/
│   ├── feature_engineering.py
│   └── model_training.py
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Vedisha15/Finverse-Fraud-Detection.git
```

### 2. Open the project folder

```bash
cd Finverse-Fraud-Detection
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Open the notebook

Open:

```text
notebooks/Finverse_Fraud_Detection_BankSim.ipynb
```

### 5. Dataset

Download the BankSim dataset separately and update the dataset path according to your local environment.

---

## Future Scope

The project can be extended with:

- Real-time transaction streaming
- Automated fraud alert generation
- Model drift monitoring
- Threshold optimization
- Precision/recall tuning
- Interactive fraud monitoring dashboard
- Explainable AI for fraud-risk reasons
- Cloud deployment

---

## Project Status

**Current Status:** Machine Learning Fraud Detection Pipeline + Dashboard Concept

The current implementation demonstrates data analysis, behavioral feature engineering, XGBoost modeling and fraud-risk analysis.

Real-time alert generation is planned as a future production enhancement.

---

## Interview Explanation

**30-second explanation:**

> Finverse is an ML-based fraud detection project built using BankSim transaction data. I analyzed transaction patterns, created behavioral features using recent customer and customer-merchant transaction counts, and trained an XGBoost classifier. Since fraud is a highly imbalanced class, I used AUPRC for evaluation. The standard feature model achieved 0.8331 AUPRC, while feature engineering improved it to 0.8812. The project also provides the foundation for a risk-monitoring dashboard and automated alert workflow.

---

## Author

**Vedisha Tiwari**

Computer Science & Engineering

GitHub: [Vedisha15](https://github.com/Vedisha15)
