# class that gets data from yahoo finance api
import yfinance as yf
import json

class YahooData:
    def __init__(self) -> None:
        pass

    def getHistoricalData(self, ticker, start_date, end_date):
        # get data from yahoo finance api
        data = yf.download(ticker, start_date, end_date)
        return data.to_json(orient='columns')
    
