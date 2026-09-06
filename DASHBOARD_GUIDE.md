# Finverse Dashboard Guide

## Recommended dashboard sections

### 1. Overview

Show four KPI cards:

- Total Transactions
- Fraud Transactions
- Genuine Transactions
- Fraud Rate

### 2. Fraud by Category

Use a horizontal bar chart.

Purpose: quickly see which transaction categories contain more fraud records.

### 3. Amount Analysis

Compare transaction amount distributions for fraud and genuine transactions.

Important: use this as an analytical signal, not as a hard fraud rule.

### 4. Customer Behavior

Use recent transaction-frequency features:

- 1 day
- 7 days
- 30 days

These help explain why behavioral feature engineering improves model performance.

### 5. Model Performance

Show:

```text
Standard Features       0.8331 AUPRC
Feature Engineering     0.8812 AUPRC
```

### 6. Risk Workflow

```text
Transaction
    ↓
Feature Preparation
    ↓
XGBoost Score
    ↓
Risk Flag
    ↓
Analyst Review
```

## Presentation style

Keep the dashboard simple and business-focused.

Avoid putting too many charts on one page. The goal is to help an analyst answer:

1. How much activity is happening?
2. How much is flagged as fraud?
3. Where is fraud concentrated?
4. Are transaction behaviors unusual?
5. What does the model performance look like?
