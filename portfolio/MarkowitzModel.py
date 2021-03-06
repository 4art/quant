import numpy as np
import yfinance as yf
import pandas as pd
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import scipy.optimize as optimisation
import datetime as dt

NUM_TRADING_DAYS = 252
NUM_PORTFOLIOS = 10000
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


def generate_portfolios(returns):
    portfolio_weights = []
    portfolio_means = []
    portfolio_risks = []
    for _ in range(NUM_PORTFOLIOS):
        # generate random weight
        w = np.random.random(len(stocks))
        w /= np.sum(w)
        portfolio_weights.append(w)
        portfolio_means.append(np.sum(returns.mean() * w) * NUM_TRADING_DAYS)
        portfolio_risks.append(np.sqrt(np.dot(w, np.dot(
            returns.cov() * NUM_TRADING_DAYS, w))))

    return np.array(portfolio_weights), np.array(portfolio_means), np.array(portfolio_risks)


def show_portfolios(returns, volatilities):
    plt.figure(figsize=(10, 6))
    plt.scatter(volatilities, returns , c=returns/volatilities, marker='o')
    plt.grid(True)
    plt.xlabel('Expected Volatility')
    plt.xlabel('Expected Returns')
    plt.colorbar(label='Sharpe ratio')
    plt.show()

if __name__ == '__main__':
    dataset = download_data()
    show_data(dataset)
    ret = calculate_return(dataset)
    show_statistics(ret)
    show_mean_variance(ret, [15, 10, 25, 15, 25, 10])
    weights, means, risks = generate_portfolios(ret)
    show_portfolios(means, risks)
