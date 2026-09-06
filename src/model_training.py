import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import average_precision_score
from xgboost import XGBClassifier

FEATURE_COLUMNS = [
    "count_1_day", "count_7_days", "count_30_days",
    "count_cust_merch_1_day", "count_cust_merch_7_days",
    "count_cust_merch_30_days"
]

def prepare_data(df):
    data = df.drop(
        ["customer", "merchant", "zipcodeOri", "zipMerchant", "step"],
        axis=1
    ).copy()

    for col in ["age", "gender", "category"]:
        data[col] = LabelEncoder().fit_transform(data[col])

    return data

def train_model(data, use_engineered_features=True):
    y = data["fraud"]

    if use_engineered_features:
        x = data.drop("fraud", axis=1)
    else:
        x = data.drop(["fraud"] + FEATURE_COLUMNS, axis=1)

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=1
    )

    weights = (y == 0).sum() / (y == 1).sum()

    model = XGBClassifier(
        max_depth=3,
        scale_pos_weights=weights,
        n_jobs=4
    )

    model.fit(x_train, y_train)
    score = average_precision_score(
        y_test, model.predict_proba(x_test)[:, 1]
    )

    return model, score

if __name__ == "__main__":
    print("Load BankSim data, apply feature engineering, then call train_model().")
