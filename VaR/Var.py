import numpy as np
import yfinance as yf
from scipy.stats import norm
import pandas as pd
import datetime as dt

def download_data(stock, start_date, end_date):
    data = {}
    ticker = yf.download(stock, start_date, end_date)
    data[stock] = ticker['Adj Close']
    return pd.DataFrame(data)

# calculate VaR tomorrow (n=1)
def calculate_var(position, c, mu, sigma):
    return calculate_var_n(position, c, mu, sigma, 1)

# calculate VaR for any days in the future
def calculate_var_n(position, c, mu, sigma, n):
    var = position * (mu * n - sigma * np.sqrt(n) * norm.ppf(1 - c))
    return var


if __name__ == '__main__':
    start_date = dt.datetime(2010, 1, 1)
    end_date = dt.date.today()
    stock_data = download_data('C', start_date, end_date)
    stock_data['returns'] = np.log(stock_data['C'] / stock_data['C'].shift(1))[1:]
    print(stock_data)
    
    # investment value
    S = 1e6

    # confidence level 95% or 99%
    c = 0.95

    # we assume that daily returnsare normally  distributed
    mu = np.mean(stock_data['returns'])
    sigma = np.std(stock_data['returns'])

    var = calculate_var(S, c, mu, sigma)
    print('Value at risk for 1 day is: $%0.2f' % var)
    print('Value at risk for 10 days is: $%0.2f' % calculate_var_n(S, c, mu, sigma, 10))