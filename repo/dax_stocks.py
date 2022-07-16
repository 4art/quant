from .repo_abstract import RepoAbstract
import pandas as pd
import yfinance as yf


class DaxStocks(RepoAbstract):

    def __init__(self):
        self.stocks = {}
        self.__set_stocks()
        
    def __set_stocks(self):
        yf.pdr_override()
        # no need for requests or BeautifulSoup use read_html
        df = pd.read_html('https://de.wikipedia.org/wiki/DAX')[1]

        tickers = df[['Symbol', 'Name']].to_dict('records')
        
        for ticker in tickers:
            self.stocks[ticker['Symbol']] = ticker['Name']
