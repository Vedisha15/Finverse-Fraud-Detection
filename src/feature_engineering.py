import pandas as pd

def add_customer_transaction_counts(df: pd.DataFrame) -> pd.DataFrame:
    """Add 1/7/30-day transaction counts for each customer."""
    df = df.copy()

    def add_count(group, window, column):
        temp = pd.Series(group.index, index=group["step"], name=column).sort_index()
        counts = temp.rolling(window).count() - 1
        counts.index = temp.values
        group[column] = counts.reindex(group.index)
        return group

    for window, col in [("1d", "count_1_day"),
                        ("7d", "count_7_days"),
                        ("30d", "count_30_days")]:
        df = df.groupby("customer", group_keys=False).apply(
            lambda g: add_count(g, window, col)
        )
    return df

def add_customer_merchant_counts(df: pd.DataFrame) -> pd.DataFrame:
    """Add 1/7/30-day counts for each customer-merchant pair."""
    df = df.copy()

    def add_count(group, window, column):
        temp = pd.Series(group.index, index=group["step"], name=column).sort_index()
        counts = temp.rolling(window).count() - 1
        counts.index = temp.values
        group[column] = counts.reindex(group.index)
        return group

    for window, col in [("1d", "count_cust_merch_1_day"),
                        ("7d", "count_cust_merch_7_days"),
                        ("30d", "count_cust_merch_30_days")]:
        df = df.groupby(["customer", "merchant"], group_keys=False).apply(
            lambda g: add_count(g, window, col)
        )
    return df
