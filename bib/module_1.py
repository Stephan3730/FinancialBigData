import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf


def retrieve_yfinance_data(ticker, start_date, end_date, period):
    data = yf.download(ticker, start=start_date, end=end_date, period=period)
    return data

def compute_log_returns(df: pd.DataFrame, target_column = "Close"):
    return np.log(df[target_column] / df[target_column].shift(1))

def plot_ACF(series):
    fig, ax = plt.subplots()
    plot_acf(series, ax=ax)
    # Show the plot
    plt.show()

