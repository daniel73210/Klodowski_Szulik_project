import pandas as pd

def prepare_price_df(extra_df: pd.DataFrame) -> pd.DataFrame:
    """
    Counts the price change, converts "date" to datetime, removes unnecessary columns and adds a multiindex
    :param extra_df: contains data to be connected to the main dataframe
    :return: modified extra_df
    """
    symbol = extra_df["symbol"].iloc[0]
    df = extra_df.copy()
    df["date"] = pd.to_datetime(df["date"])
    df["perc_change"] = df["close"].pct_change()

    df = df[["date", "close", "perc_change"]]

    df.columns = [c if c == "date" else (symbol, c) for c in df.columns]

    return df.set_index("date")