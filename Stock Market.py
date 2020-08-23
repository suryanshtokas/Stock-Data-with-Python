#Import pandas for dataframe management
import pandas as pd

# Import datetime to pass the start and end dates
import datetime as dt

# Import pandas_datareader as web to import stock data
import pandas_datareader.data as web

# Import matplotlib to plot graphs
import matplotlib.pyplot as plt

# Use the datetime module as Datareader takes time in a certain format
# Declare variables to hold start and end points
start = dt.datetime(2020, 1, 1)
end = dt.datetime(2020, 8, 22)

# Get the stock data from yahoo finance
# We specify 'MSFT' as the ticker as we want the stock data of Microsoft
# We also pass our start and end times 
data = web.DataReader('MSFT', 'yahoo', start, end)

# Calculate the SMA(Simple Moving Average) for the closing data
data['SMA'] = data['Close'].rolling(window=15).mean()

# Calculate the WMA (Weighted Moving Average) for the closing data
def WMACalc(w):
    def g(x):
        return sum(w * x) / sum(w)
    return g

weights = list(reversed([(14-n) * 14 for n in range(14)]))
data['WMA'] = data['Close'].rolling(window=14).apply(WMACalc(weights), raw=True)

# Calculate the EMA (Exponential Moving Average) for the closing data
data['EMA'] = data['Close'].ewm(span=15).mean()

# Create a new dataframe with Closing Values, SMA, WMA, EMA
total_df = pd.concat([data['Close'].iloc[14::], data['SMA'], data['EMA'].iloc[14::], data['WMA']], axis=1)
print(total_df)
total_df.plot()
plt.title('Stock Data')
plt.ylabel('Stock Prices (Prices in USD($)')
plt.show()
