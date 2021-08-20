import numpy as np
from numpy.lib.function_base import percentile
import yfinance as yf
import datetime as dt
import pandas as pd


def download_data(stock, start, end):
    data = {}
    ticker = yf.download(stock, start, end)
    data['Adj Close'] = ticker['Adj Close']
    return pd.DataFrame(data)


class ValueAtRiskMonteCarlo:

    def __init__(self, S, mu, sigma, c, n, iterations):
        # S is value of investment at t=0 (1000 dollars)
        self.S, self.mu, self.sigma, self.c, self.n, self.iterations = S, mu, sigma, c, n, iterations

    def simulation(self):
        rand = np.random.normal(0, 1, [1, self.iterations])

        # equation for the S(t) stock price
        # the random walk of initial investment
        stock_price = self.S * \
            np.exp(self.n * (self.mu - 0.5 * self.sigma ** 2) +
                   self.sigma * np.sqrt(self.n) * rand)
        stock_price = np.sort(stock_price)

        percentile = np.percentile(stock_price, (1 - self.c) * 100)

        return self.S - percentile


if __name__ == '__main__':
    start_date = dt.datetime(2010, 1, 1)
    end_date = dt.date.today()
    S = 1e6 # 1m $
    c = 0.95 # confidence level
    n = 1 # 1 day
    iterations = 100000 # iterations number

    citi = download_data('C', start_date, end_date)
    citi['returns'] = citi['Adj Close'].pct_change()

    mu = np.mean(citi['returns'])
    sigma = np.std(citi['returns']) # standard deviation

    model = ValueAtRiskMonteCarlo(S, mu, sigma, c, n, iterations)
    print("Value at Risk with monte carlo simulaiton: $%.2f" % model.simulation())
