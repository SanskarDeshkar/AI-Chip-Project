import yfinance as yf
import pandas as pd

# creating a list with chip manufacturers and hardware oems
chip_mfrs = ["NVDA", "AMD", "INTC", "QCOM"]
hardware_oems = ["AAPL", "DELL", "005930.KS", "HPQ"]
all_tickers = chip_mfrs + hardware_oems

# setting start and end dates for data collection
start_date = "2020-01-01"
end_date = "2024-12-31"

# downloading all the stock data
all_data = yf.download(all_tickers, start = start_date, end = end_date)

# checking to see if the download worked
if all_data.empty:
    print("Download failed")
else:
    print("Download successful")

    # getting the closing prices
    closing_prices = all_data['Close']
    print(closing_prices.head()) # print the first few rows to see if it worked

    # saving the closing prices to a CSV file
    closing_prices.to_csv("closing_prices.csv")
    print("Data saved to closing_prices.csv") # confirm it saved