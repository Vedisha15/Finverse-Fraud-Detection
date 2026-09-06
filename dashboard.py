import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Finverse | Fraud Monitoring",
    page_icon="🔎",
    layout="wide"
)

st.title("Finverse")
st.subheader("Fraud Detection & Risk Monitoring Dashboard")
st.caption("BankSim transaction analysis and fraud-risk exploration")

uploaded = st.file_uploader(
    "Upload bs140513_032310.csv",
    type=["csv"]
)

if uploaded is None:
    st.info("Upload the BankSim CSV to view the monitoring dashboard.")
    st.markdown("""
### Dashboard sections
- Transaction overview
- Fraud rate
- Fraud by category
- Transaction amount analysis
- Customer behavior
- Risk-monitoring workflow

The supplied notebook uses BankSim transaction data and an XGBoost fraud classifier.
""")
    st.stop()

df = pd.read_csv(uploaded)

if "fraud" not in df.columns:
    st.error("The uploaded file must contain a `fraud` column.")
    st.stop()

# Sidebar
st.sidebar.header("Filters")

if "category" in df.columns:
    categories = sorted(df["category"].dropna().astype(str).unique())
    selected = st.sidebar.multiselect(
        "Transaction category",
        categories
    )
    if selected:
        df = df[df["category"].astype(str).isin(selected)]

# KPI cards
total = len(df)
fraud = int(df["fraud"].sum())
genuine = total - fraud
fraud_rate = (fraud / total * 100) if total else 0

c1, c2, c3, c4 = st.columns(4)
c1.metric("Transactions", f"{total:,}")
c2.metric("Fraud", f"{fraud:,}")
c3.metric("Genuine", f"{genuine:,}")
c4.metric("Fraud Rate", f"{fraud_rate:.2f}%")

st.divider()

left, right = st.columns(2)

with left:
    st.markdown("### Fraud vs Genuine")
    fig, ax = plt.subplots()
    ax.bar(["Genuine", "Fraud"], [genuine, fraud])
    ax.set_ylabel("Number of transactions")
    st.pyplot(fig)

with right:
    st.markdown("### Fraud by Category")
    if "category" in df.columns:
        fraud_category = (
            df[df["fraud"] == 1]["category"]
            .astype(str)
            .value_counts()
            .sort_values()
        )
        fig, ax = plt.subplots()
        fraud_category.plot(kind="barh", ax=ax)
        ax.set_xlabel("Fraud transactions")
        st.pyplot(fig)

if "amount" in df.columns:
    st.markdown("### Transaction Amount Distribution")
    fig, ax = plt.subplots()
    df[df["fraud"] == 0]["amount"].plot(
        kind="hist", bins=40, alpha=0.65, ax=ax, label="Genuine"
    )
    df[df["fraud"] == 1]["amount"].plot(
        kind="hist", bins=40, alpha=0.65, ax=ax, label="Fraud"
    )
    ax.set_xlabel("Transaction amount")
    ax.legend()
    st.pyplot(fig)

st.markdown("### Risk-monitoring workflow")
st.markdown(
    "**Transaction → Behavioral Features → XGBoost Risk Score → "
    "Fraud Flag → Analyst Review**"
)
