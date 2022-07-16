from .repo_abstract import RepoAbstract
import pandas as pd
import yfinance as yf


class NasdaqStocks(RepoAbstract):

    def __init__(self):
        self.stocks = {}
        self.__set_stocks()
        
    def __set_stocks(self):
        yf.pdr_override()
        # no need for requests or BeautifulSoup use read_html

        df = pd.read_html('https://en.wikipedia.org/wiki/Nasdaq-100')[3]
        # convert symbol column to list

        tickers = df[['Ticker', 'Company']].to_dict('records')
        
        for ticker in tickers:
            self.stocks[ticker['Ticker']] = ticker['Company']