import numpy as np
from numpy.linalg import norm
import yfinance as yf
import pandas as pd
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import datetime as dt
from scipy.stats import norm


def download_data(stock, start_date, end_date):
    data = {}
    ticker = yf.download(stock, start_date, end_date)
    data['Price'] = ticker['Adj Close']
    return pd.DataFrame(data)


def calculate_returns(stock_data):
    stock_data['Price'] = np.log(
        stock_data['Price'] / stock_data['Price'].shift(1))
    # remove first Nan
    return stock_data[1:]


def show(stock_data):
    plt.hist(stock_data, bins=700)
    stock_variance = stock_data.var()
    stock_mean = stock_data.mean()
    sigma = np.sqrt(stock_variance)
    x = np.linspace(stock_mean - 5 * sigma, stock_mean + 5 * sigma, 100)
    plt.plot(x, norm.pdf(x, stock_mean, sigma))
    plt.show()


if __name__ == '__main__':
    start_date = dt.datetime(2010, 1, 1)
    end_date = dt.date.today()
    stock_data = download_data('IBM', start_date, end_date)
    returns = calculate_returns(stock_data)
    show(returns)
