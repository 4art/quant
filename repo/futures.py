from .repo_abstract import RepoAbstract
import pandas as pd
import yfinance as yf


class Futures(RepoAbstract):

    def __init__(self):
        self.stocks = {
            "YM=F": "Dow Jones Industrial Average",
            "ES=F": "S&P 500 Mini",
            "NQ=F": "Nasdaq 100 mini",
            "RTY=F": "Russel 2000 mini",
            "^N225": "Nikkei 225",
            "^STOXX50E": "Stoxx 50",
            "^GDAXI": "DAX",
            "^VIX": "CBOE Volatility Index",
            "CL=F": "Crude Oil",
            "BZ=F": "Brent Crude Oil",
            "RB=F": "RBOB Gasoline",
            "HO=F": "Heating Oil",
            "NG=F": "Natural Gas",
            "ZB=F": "U.S. Treasury Bond",
            "ZN=F": "10-Year T-Note",
            "TWE=F": "20-Year U.S. Treasury Bond",
            "UB=F": "Ultra U.S. Treasury Bond",
            "ZF=F": "Five-Year US Treasury Note",
            "ZT=F": "2-Year T-Note",
            "CC=F": "Cocoa",
            "CT=F": "Cotton",
            "OJ=F": "Orange Juice",
            "KC=F": "Coffee",
            "LBS=F": "Random Length Lumber",
            "SB=F": "Sugar",
            "GC=F": "Gold",
            "SI=F": "Silver",
            "PL=F": "Platinum",
            "HG=F": "Copper",
            "PA=F": "Palladium",
            "LE=F": "Live Cattle Futures",
            "GF=F ": "Feeder Cattle",
            "HE=F": "Lean Hogs",
            "ZS=F": "Soybean",
            "ZL=F": "Soybean Oil",
            "ZC=F": "Corn Futures",
            "ZW=F": "Chicago SRW Wheat",
            "ZR=F": "Rough Rice",
            "ZO=F": "Oat",
            "6E=F": "Euro FX",
            "JPY=X": "USD/JPY",
            "GBPUSD=X": "GBP/USD",
            "CAD=X": "USD/CAD",
            "CHF=X": "USD/CHF",
            "AUDUSD=X": "AUD/USD",
            "NZDUSD=X": "NZD/USD",
            "RUB=X": "USD/RUB",
            "UTE.VI": "Ukrainian Traded Index in EUR"
        }
