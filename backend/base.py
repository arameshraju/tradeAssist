from flask import Flask
from yahoodata import YahooData


api = Flask(__name__)


@api.route('/profile')
def my_profile():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }
    return response_body

# create api route called /getHistoricalData that takes in a ticker, start_date, and end_date and returns the data from the yahoo finance api
@api.route('/getHistoricalData')
def getHistoricalData():
    # calles yahoodata.getHistoricalData and returns the data
     response_body = YahooData().getHistoricalData('SPY', '2023-01-01', '2023-03-01')
     return response_body




    # return response_body