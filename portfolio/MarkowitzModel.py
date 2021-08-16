import numpy as np
import yfinance as yf
import pandas as pd
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import scipy.optimize as optimisation
import datetime as dt

NUM_TRADING_DAYS = 252
stocks = ['AAPL', 'WMT', 'TSLA', 'GE', 'AMZN', 'DB']

start_date = dt.datetime(2010, 1, 1)
end_date = dt.date.today()

stock_data = {}


def download_data():
    return pdr.get_data_yahoo(stocks, start=start_date, end=end_date)['Close']


def show_data(data):
    data.plot(figsize=(10, 5))
    plt.show()


def calculate_return(data):
    log_return = np.log(data/data.shift(1))
    return log_return[1:]


def show_statistics(returns):
    # instead of daily metrics we are after annual metrics
    # mean of anual return
    print(returns.mean() * NUM_TRADING_DAYS)
    print(returns.cov() * NUM_TRADING_DAYS)


def show_mean_variance(returns, weights):
    portfolio_return = np.sum(returns.mean()*weights) * NUM_TRADING_DAYS
    portfolio_vola = np.sqrt(np.dot(weights, np.dot(
        returns.cov() * NUM_TRADING_DAYS, weights)))

    print("Expected portfolio mean(return) is %s" % portfolio_return)
    print("Expected portfolio vola (standard deviation) is %s" % portfolio_vola)


if __name__ == '__main__':
    dataset = download_data()
    ret = calculate_return(dataset)
    show_statistics(ret)
    show_mean_variance(ret, [15, 10, 25, 15, 25, 10])
