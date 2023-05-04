import yahoodata

yd=yahoodata.YahooData()
data=yd.getHistoricalData('SPY', '2023-01-01', '2023-03-31')
print(data.to_json(orient='columns'))
