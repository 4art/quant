from .repo_abstract import RepoAbstract
import pandas as pd

# https://stockmarketmba.com/listofstocksforanexchange.php?s=GY
class GermStocks(RepoAbstract):

    def __init__(self):
        self.stocks = {}
        self.__set_stocks()
        
    def __set_stocks(self):
        df = pd.read_csv('repo/List of Stocks For An Exchange.csv')

        tickers = df[['Local Symbol', 'Description']].to_dict('records')
        
        for ticker in tickers:
            self.stocks[ticker['Local Symbol']] = ticker['Description']