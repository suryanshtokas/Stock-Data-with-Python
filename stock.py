import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web

start = dt.datetime(2020, 1, 1)#YYYY-MM-DD
end = dt.datetime(2020, 8, 24)#YYYY-MM-DD

# Name of the Stock
ticker = input('Enter the ticker symbol   -  ').upper()

# Period
period = 14

data = web.DataReader(ticker, 'yahoo', start, end)

# Calculate the SMA(Simple Moving Average)
data['SMA'] = data['Close'].rolling(window=period).mean()

# Calculate the EMA (Exponential Moving Average) for the closing data
data['EMA'] = data['Close'].ewm(span=period).mean()

# Calculate the WMA (Weighted Moving Average) for the closing data
def WMACalc(w):
    def g(x):
        return sum(w * x) / sum(w)
    return g

weights = list(reversed([(14-n) * 14 for n in range(14)]))
data['WMA'] = data['Close'].rolling(window=14).apply(WMACalc(weights), raw=True)

# Create the List that stores everything needed to make the final graph
finalList = [data['Close'].iloc[period-1::], 
			data['SMA'], data['EMA'].iloc[period-1::], 
			data['WMA'],
]

# Create a new pandas Series that stores everything
finalData = pd.concat(finalList, axis=1)

print(finalData.head())
print(finalData.tail())

# Plot the graph from the data
finalData.plot()
plt.title(f'''Stock Prices of {ticker}''')
plt.ylabel('Prices in USD($)')
plt.show()


finalData.to_excel('Test1.xlsx')
data.to_excel('Test2.xlsx')
data.to_csv('Test2.csv')
