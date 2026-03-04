import pandas as pd

def match_price_dates(data_frame_1: pd.DataFrame, data_frame_2: pd.DataFrame):
    """
    Matches price dates between two dataframes and removes useless columns
    :param data_frame_1:
    :param data_frame_2:
    :return: new dataFrame
    """
    df1 = data_frame_1.copy()
    df2 = data_frame_2.copy()
    df1 = df1[['date', 'open', 'close']]
    df2 = df2[['date', 'open', 'close']]
    df1["date"] = pd.to_datetime(df1["date"])
    df2["date"] = pd.to_datetime(df2["date"])

    return pd.merge(df1, df2, on="date", how="inner", suffixes=('_1', '_2'))

def calculate_proc_change(data_frame: pd.DataFrame):
    """
    Adds percent change in prices for two instruments
    :param data_frame: dataFrame processed by match_price_dates function
    :return: new dataFrame with proc_change column
    """
    temp = data_frame.copy()
    temp["proc_change_1"] = (temp["close_1"] / temp["open_1"] - 1) * 100
    temp["proc_change_2"] = (temp["close_2"] / temp["open_2"] - 1) * 100

    return temp