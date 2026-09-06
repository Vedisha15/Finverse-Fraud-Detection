# Finverse: Instant Fraud Alerts

> **Machine-learning based fraud detection project using BankSim transaction data, behavioral feature engineering, XGBoost and an interactive monitoring dashboard.**

## 📌 Project Overview

**Finverse** is a fraud-detection and risk-monitoring project built around transaction-level data.

The project has two practical goals:

1. **Identify suspicious transaction patterns** using machine learning.
2. **Present fraud-related insights clearly** through a monitoring dashboard so that suspicious activity can be reviewed faster.

The analysis uses the **BankSim** transaction dataset. The notebook performs exploratory analysis, behavioral feature engineering, model training with **XGBoost**, and evaluation using **AUPRC (Average Precision)**.

---

## 🎯 Problem Statement

Financial transaction datasets are usually highly imbalanced: genuine transactions are much more common than fraudulent transactions.

A useful fraud-detection system therefore needs to:

- understand normal transaction behavior,
- identify unusual patterns,
- handle class imbalance,
- create meaningful behavioral features,
- evaluate the model using a metric suitable for imbalanced classification,
- and make the results easy to monitor.

---

## 🧠 Solution Approach

The project follows this workflow:

```text
BankSim Transaction Data
          ↓
Data Preparation
          ↓
Exploratory Data Analysis
          ↓
Behavioral Feature Engineering
          ↓
Label Encoding
          ↓
Train / Test Split
          ↓
XGBoost Classifier
          ↓
AUPRC Evaluation
          ↓
Fraud Risk Insights
          ↓
Monitoring Dashboard
```

---

## 📊 Dataset

The notebook loads:

```text
bs140513_032310.csv
```

from the BankSim dataset.

The analyzed data contains:

- **594,643 total transactions**
- **7,200 fraud transactions**
- **587,443 non-fraud transactions**

Fraud therefore represents only about **1.21%** of all transactions, making class imbalance an important consideration.

> The dataset itself is intentionally **not included** in this repository because large/raw datasets should not be committed to GitHub. See `data/README.md` for the expected filename and setup.

---

## 🔎 Exploratory Analysis

The notebook explores fraud transactions by:

- age code,
- gender code,
- transaction category,
- transaction amount,
- recent transaction frequency.

Examples from the analysis:

- Maximum fraud transaction amount: **8329.96**
- Maximum genuine transaction amount: **2144.86**
- The most frequent fraud age code in the notebook output is **2**
- The most frequent fraud gender code is **F**
- The most frequent fraud category in the shown output is **es_sportsandtoys**

These values are dataset-specific and should be interpreted in the context of BankSim.

---

## ⚙️ Behavioral Feature Engineering

A key part of Finverse is creating features that describe **recent transaction behavior**.

### Customer-level features

For every customer, the notebook calculates transaction counts over:

- previous 1 day,
- previous 7 days,
- previous 30 days.

The resulting features are:

```text
count_1_day
count_7_days
count_30_days
```

### Customer–merchant features

The same idea is applied to each customer–merchant pair:

```text
count_cust_merch_1_day
count_cust_merch_7_days
count_cust_merch_30_days
```

### Why are these useful?

Suppose a customer normally makes a small number of transactions, but suddenly makes many transactions within a short period.

That behavior can be a useful signal for a fraud-detection model.

This is the main idea behind the behavioral feature engineering in the notebook.

---

## 🤖 Machine Learning Model

The notebook uses:

### **XGBoost Classifier**

XGBoost is a gradient-boosting algorithm that builds multiple decision trees sequentially and combines them to make a strong predictive model.

The notebook uses:

```python
XGBClassifier(
    max_depth=3,
    scale_pos_weights=weights,
    n_jobs=4
)
```

The categorical columns:

```text
age
gender
category
```

are label encoded before training.

---

## ⚖️ Handling Class Imbalance

Fraud is much less common than genuine activity.

The notebook calculates:

```python
weights = (Y == 0).sum() / (Y == 1).sum()
```

and passes this value as the positive-class weighting parameter to XGBoost.

The purpose is to give more importance to the minority fraud class during model training.

---

## 📈 Model Evaluation

The project uses **AUPRC / Average Precision**:

```python
average_precision_score(
    Ytest,
    clf.predict_proba(Xtest)[:,1]
)
```

### Results

| Model | AUPRC |
|---|---:|
| Standard features | **0.8331** |
| Feature-engineered data | **0.8812** |

The feature-engineered model therefore improves AUPRC by approximately:

- **0.0481 AUPRC points**
- **4.81 percentage points**
- **5.77% relative improvement**

This is the strongest directly reproducible performance result from the supplied notebook.

---

## 📊 Why AUPRC?

Fraud detection is an **imbalanced classification problem**.

If we use accuracy alone, a model could appear strong simply because most transactions are genuine.

AUPRC focuses more directly on the relationship between:

- precision,
- recall,
- and the minority positive class.

That makes it useful for evaluating fraud-ranking performance.

---

## 🖥️ Monitoring Dashboard

The repository also contains a Streamlit dashboard prototype.

It is designed around the project workflow:

```text
Transaction Data
      ↓
Risk / Fraud Analysis
      ↓
Monitoring KPIs
      ↓
Category & Amount Insights
      ↓
Analyst Review
```

The dashboard includes:

- transaction count,
- fraud count,
- genuine transaction count,
- fraud rate,
- fraud by category,
- transaction amount distribution,
- category filtering,
- risk-monitoring workflow.

Run it with:

```bash
streamlit run dashboard/dashboard.py
```

---

## 📁 Repository Structure

```text
Finverse_GitHub_Repo/
│
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
│
├── notebooks/
│   └── Finverse_Fraud_Detection_BankSim.ipynb
│
├── src/
│   ├── feature_engineering.py
│   └── model_training.py
│
├── dashboard/
│   └── dashboard.py
│
├── data/
│   └── README.md
│
├── models/
│   └── README.md
│
├── docs/
│   ├── PROJECT_EXPLANATION.md
│   ├── INTERVIEW_QUESTIONS.md
│   └── DASHBOARD_GUIDE.md
│
└── assets/
    └── dashboard_slides.pptx
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Finverse_GitHub_Repo
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add the dataset

Place:

```text
bs140513_032310.csv
```

inside your local `data/` folder, or upload it directly to the Streamlit dashboard.

### 5. Run the notebook

Open:

```text
notebooks/Finverse_Fraud_Detection_BankSim.ipynb
```

and run the cells in order.

### 6. Run the dashboard

```bash
streamlit run dashboard/dashboard.py
```

---

## 💡 Key Insights

### Insight 1 — Fraud is highly imbalanced

Only a small fraction of transactions are labeled as fraud.

This means fraud detection cannot rely on accuracy alone.

### Insight 2 — Recent behavior is useful

Customer-level and customer–merchant transaction counts over 1, 7 and 30 days provide additional behavioral information.

### Insight 3 — Feature engineering improves model performance

The AUPRC increased from **0.8331 to 0.8812** after adding behavioral features.

### Insight 4 — Transaction amount can be a useful signal

The maximum fraud amount in the notebook is considerably higher than the maximum genuine amount, although amount alone should not be treated as a fraud rule.

---

## ⚠️ Important Project Scope Note

The supplied notebook demonstrates the **data-analysis and ML modeling pipeline**.

The production-style concept of:

```text
live transaction → model score → instant alert → analyst dashboard
```

is the intended monitoring workflow.

For a production deployment, the model would need to be connected to a live transaction stream/API, persistent model serving, an alerting mechanism and a production dashboard backend.

---

## 🔮 Future Scope

- Real-time transaction streaming
- Automated alert notifications
- Model monitoring and drift detection
- More robust fraud-risk scoring
- Threshold optimization
- Explainable AI for analyst decisions
- Cloud deployment
- Database integration
- Authentication and role-based dashboard access

---

## 🛠️ Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Seaborn
- Streamlit
- Jupyter Notebook
- Git & GitHub

---

## 👩‍💻 Project

**Finverse — Fraud Detection & Risk Monitoring**

Built as an academic/portfolio ML and analytics project using BankSim transaction data.
