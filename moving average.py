import yfinance as yf

# set the stock ticker symbol and moving average period
ticker_symbol = "AAPL"
moving_average_period = 50

# get the stock data
ticker = yf.Ticker(ticker_symbol)
history = ticker.history(period="max")

# calculate the moving average
history["Moving Average"] = history["Close"].rolling(window=moving_average_period).mean()

# determine whether to take a trade based on the moving average
if history["Close"][-1] > history["Moving Average"][-1] and history["Close"][-2] < history["Moving Average"][-2]:
    print(f"Buy {ticker_symbol}")
elif history["Close"][-1] < history["Moving Average"][-1] and history["Close"][-2] > history["Moving Average"][-2]:
    print(f"Sell {ticker_symbol}")
else:
    print(f"No action for {ticker_symbol}")
