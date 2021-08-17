import numpy as np
import yfinance as yf
import pandas as pd
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import datetime as dt


class CAPM:
    def __init__(self, stocks, start_date, end_date):
        self.stocks = stocks
        self.start_date = start_date
        self.end_date = end_date

    def download_data(self):
        return pdr.get_data_yahoo(self.stocks, start=self.start_date, end=self.end_date)['Adj Close']

    def initialize(self):
        stock_data = self.download_data()
        stock_data = stock_data.resample('M').last()

        self.data = pd.DataFrame(
            {'s_adjclose': stock_data[self.stocks[0]], 'm_adjclose': stock_data[self.stocks[1]]})

        # log monthly return
        self.data[['s_returns', 'm_returns']] = np.log(
            self.data[['s_adjclose', 'm_adjclose']] / self.data[['s_adjclose', 'm_adjclose']].shift(1))
        # remove NaN
        self.data = self.data[1:]

    # How risky is our portfolio relative to the market
    def calculate_beta(self):
        covariance_matrix = np.cov(self.data["s_returns"], self.data["m_returns"])
        beta = covariance_matrix[0, 1] / covariance_matrix[1, 1]
        print("beta from formula: ", beta)

if __name__ == '__main__':
    start_date = dt.datetime(2010, 1, 1)
    end_date = dt.date.today()
    capm = CAPM(['IBM', '^GSPC'], start_date, end_date)
    capm.initialize()
    capm.calculate_beta()
