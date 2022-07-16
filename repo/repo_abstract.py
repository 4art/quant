from pandas import DataFrame
import datetime as dt
from pandas_datareader import data


class RepoAbstract():
    def __init__(self):
        self.stocks = {}

    def get_tickers(self) -> list:
        return list(self.stocks.keys())

    def get_info(self, ticker: str) -> str:
        return self.stocks[ticker]

    def get_df(self, start=dt.datetime(2020, 1, 1)) -> DataFrame:
        return data.get_data_yahoo(self.get_tickers(), start=start, end=dt.date.today())['Close']
