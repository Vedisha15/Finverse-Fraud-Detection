# Finverse — Project Explanation

## 1. What is Finverse?

Finverse is a fraud-detection and risk-monitoring project.

The goal is to analyze transaction behavior and use machine learning to identify suspicious transactions.

---

## 2. Why did I choose this project?

Fraud is a real-world problem where detecting unusual transaction behavior quickly is important.

The project gave me an opportunity to combine:

- Python
- data analysis
- feature engineering
- machine learning
- visualization

---

## 3. What dataset did I use?

I used the BankSim transaction dataset.

The notebook contains 594,643 transactions:

- 7,200 fraud
- 587,443 non-fraud

The dataset is highly imbalanced.

---

## 4. What algorithm did I use?

I used **XGBoost Classifier**.

### Simple explanation

XGBoost is a boosting algorithm based on decision trees.

It builds trees one after another, where later trees try to improve the mistakes made by earlier trees.

---

## 5. Why XGBoost?

For this project, XGBoost is useful because it works well with structured/tabular data and can capture non-linear relationships between transaction features.

---

## 6. What feature engineering did I perform?

This is one of the most important parts of my project.

I calculated how many transactions a customer made in the previous:

- 1 day
- 7 days
- 30 days

I also calculated the same counts for each customer–merchant pair.

This creates behavioral features that tell the model about recent transaction activity.

---

## 7. Why is this useful?

Suppose a customer normally makes only a few transactions.

If the customer suddenly performs many transactions in a short period, that behavior may be unusual.

The model can use this information along with other transaction features.

---

## 8. How did I handle categorical data?

The notebook uses `LabelEncoder` for:

- age
- gender
- category

---

## 9. How did I handle class imbalance?

Fraud is the minority class.

The notebook calculates the ratio between genuine and fraud records and passes it to the XGBoost classifier through the positive-class weighting parameter.

---

## 10. How did I evaluate the model?

I used **AUPRC / Average Precision**.

The results were:

```text
Standard features      → 0.8331
Feature engineered     → 0.8812
```

This shows that the behavioral features improved the model's AUPRC.

---

## 11. Why not just use accuracy?

Because fraud is rare.

A model can get high accuracy by predicting almost everything as genuine.

AUPRC is more informative for the positive/fraud class because it considers precision and recall across prediction thresholds.

---

## 12. What is the dashboard doing?

The dashboard is designed to make the fraud analysis easier to monitor.

It shows:

- total transactions,
- fraud transactions,
- genuine transactions,
- fraud rate,
- fraud categories,
- transaction amount patterns.

---

## 13. What is the future production workflow?

```text
Live Transaction
      ↓
Feature Generation
      ↓
XGBoost Model
      ↓
Risk Score
      ↓
Fraud Alert
      ↓
Analyst Review
```

The current notebook demonstrates the analysis and ML pipeline. Connecting it to a live stream, alert service and production dashboard would be the next deployment step.
