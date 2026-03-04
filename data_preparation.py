import pandas as pd

def match_price_dates(data_frame_1: pd.DataFrame, data_frame_2: pd.DataFrame):
    df1 = data_frame_1.copy()
    df2 = data_frame_2.copy()
    df1["date"] = pd.to_datetime(df1["date"])
    df2["date"] = pd.to_datetime(df2["date"])

    return pd.merge(df1, df2, on="date", how="inner", suffixes=('_1', '_2'))