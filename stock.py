import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime as dt

start = dt.datetime(2020, 1, 1)
end = dt.datetime(2020, 8, 23)

ticker = 'MSFT'

data = web.DataReader(ticker, 'yahoo', start, end)

period = 14

# Calculate SMA(Simple Moving Average)
data['SMA'] = data['Close'].rolling(window=period).mean()

data2 = pd.concat([data['Close'].iloc[period-1::], data['SMA']], axis=1)

data2.plot()
plt.title(f'''Stock Prices of {ticker}''')
plt.ylabel('Prices in USD($)')
plt.show()