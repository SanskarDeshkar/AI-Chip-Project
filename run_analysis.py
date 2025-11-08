import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# creating a list with chip manufacturers and hardware oems
chip_mfrs = ["NVDA", "AMD", "INTC", "QCOM"]
hardware_oems = ["AAPL", "DELL", "005930.KS", "HPQ"]
all_tickers = chip_mfrs + hardware_oems

# setting start and end dates for data collection
start_date = "2020-01-01"
end_date = "2024-12-31"

# # downloading all the stock data
# all_data = yf.download(all_tickers, start = start_date, end = end_date)

# # checking to see if the download worked
# if all_data.empty:
#     print("Download failed")
# else:
#     print("Download successful")

#     # getting the closing prices
#     closing_prices = all_data['Close']
#     print(closing_prices.head()) # print the first few rows to see if it worked

#     # saving the closing prices to a CSV file
#     closing_prices.to_csv("closing_prices.csv")
#     print("Data saved to closing_prices.csv") # confirm it saved


# loading data from the CSV file
data = pd.read_csv("closing_prices.csv", index_col = 0, parse_dates = True) # lets pandas know the first column is dates

# creating a new dataframe for the percent changes in closing prices
pct_changes = data.pct_change()

# replacing any blank values with 0's
pct_changes = pct_changes.fillna(0)

print(pct_changes.head()) # print the first few rows to see if it worked


# calculating the correlation matrix of the percent changes
correlation_matrix = pct_changes.corr()

print("Correlation matrix:" + str(correlation_matrix)) # print the correlation matrix to see the results and check if it worked

# creating a new copy of pct_changes to make changes to for the lag test
lagged_test_df = pct_changes.copy()

# goes through every chip manufacturer, creates a new column, and moves all data down 1 row (date)
for x in chip_mfrs:
    lagged_test_df[f"{x}_LAGGED"] = lagged_test_df[x].shift(1) 

# calculate the correlation matrix of the lagged dataframe
lagged_correlation_matrix = lagged_test_df.corr()

print("Lagged Correlation matrix:" + str(lagged_correlation_matrix)) # print the lagged correlation matrix to see the results and check if it worked


# creating a correlation heatmap of the percent changes in closing prices
plt.figure(figsize=(12, 10)) # creating a canvas for the heatmap
sns.heatmap( # drawing the heatmap
    correlation_matrix, 
    annot = True, # shows the correlation numbers on the heatmap
    cmap = "coolwarm", # color scheme is blue to red
    fmt = ".2f" # format of the numbers to 2 decimal places
 ) 

plt.title("Correlation Heatmap of Percent Changes in Closing Prices") # title of the heatmap
plt.savefig("correlation_heatmap.png") # saving the heatmap as a PNG file

print("Heatmap saved as correlation_heatmap.png") # confirm it saved

# creating a growth chart of the chip manufacturers
cumulative_growth = (1 + pct_changes).cumprod() # calculates how much $1 would grow over time

plt.figure(figsize=(12, 8)) # creating a canvas for the growth chart

cumulative_growth[chip_mfrs].plot(ax = plt.gca(), legend = True) # plotting only the chip manufacturers

plt.title("Cumulative Growth of $1 Invested in Chip Manufacturers (2020-2024)") # title of the growth chart
plt.savefig("chip_mfrs_growth_chart.png") # saving the growth chart as a PNG file

print("Growth chart saved as chip_mfrs_growth_chart.png") # confirm it saved

# creating a growth chart of the hardware OEMs
plt.figure(figsize=(12, 8)) # creating a canvas for the growth chart

cumulative_growth[hardware_oems].plot(ax = plt.gca(), legend = True) # plotting only the hardware OEMs

plt.title("Cumulative Growth of $1 Invested in Hardware OEMs (2020-2024)") # title of the growth chart
plt.savefig("hardware_oems_growth_chart.png") # saving the growth chart as a PNG file

print("Growth chart saved as hardware_oems_growth_chart.png") # confirm it saved    