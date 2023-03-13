import yfinance as yf

# get the stock data
ticker = yf.Ticker("AAPL")
history = ticker.history(period="max")

# set the moving average period
moving_average_period = 50

# calculate the moving average
history["Moving Average"] = history["Close"].rolling(window=moving_average_period).mean()

# print the moving average values
print(history["Moving Average"])
