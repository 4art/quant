import numpy as np
import yfinance as yf
import pandas as pd
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import datetime as dt

RISK_FREE_RATE = 0.05
MONTHS_IN_YEAR = 12


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
        covariance_matrix = np.cov(
            self.data["s_returns"], self.data["m_returns"])
        beta = covariance_matrix[0, 1] / covariance_matrix[1, 1]
        print("beta from formula: ", beta)

    def regression(self):
        beta, alpha = np.polyfit(
            self.data['m_returns'], self.data['s_returns'], deg=1)
        print("Beta from regression: ", beta)
        # calculate the expected return according to the CAPM formula
        # we are after annual return (this is why multiply by 12)
        expected_return = RISK_FREE_RATE + beta * \
            (self.data['m_returns'].mean() * MONTHS_IN_YEAR - RISK_FREE_RATE)
        print("Expected return : ", expected_return)
        self.plot_regression(alpha, beta)

    def plot_regression(self, alpha, beta):
        fig, axis = plt.subplots(1, figsize=(20, 10))
        axis.scatter(self.data["m_returns"],
                     self.data['s_returns'], label="Data Points")
        axis.plot(self.data['m_returns'], beta *
                  self.data['m_returns'] + alpha, color='red', label="CAPM Line")
        plt.title('Capital Asset Pricing Model, finding alpha and beta')
        plt.xlabel('Market return $R_m$', fontsize=18)
        plt.ylabel('Stock return $R_a$')
        plt.text(0.08, 0.05, r'$R_a = \beta * R_m + \alpha$', fontsize=18)
        plt.legend()
        plt.grid(True)
        plt.show()

if __name__ == '__main__':
    start_date = dt.datetime(2010, 1, 1)
    end_date = dt.date.today()
    capm = CAPM(['IBM', '^GSPC'], start_date, end_date)
    capm.initialize()
    capm.calculate_beta()
    capm.regression()
