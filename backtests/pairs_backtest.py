import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# creating a new dataframe to hold the closing prices of the two stocks
df = pd.read_csv("data/closing_prices.csv")

# making sure dates are in the correct format and set as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# calculating the price ratio between NVDA and AMD
df['Spread'] = df['NVDA'] / df['AMD']

# calculating the 20 day rolling mean and standard deviation of the spread and then the z-score of the spread to identify when the spread is significantly different from its mean, which could indicate a potential trading opportunity.
df['Rolling_Mean'] = df['Spread'].rolling(window=60).mean()
df['Rolling_Std'] = df['Spread'].rolling(window=60).std()
df['Z_Score'] = (df['Spread'] - df['Rolling_Mean']) / df['Rolling_Std']

# setting a rule to buy AMD and sell NVDA when the z-score is above 2, and to do the opposite when the z-score is below -2 
df['Signal'] = np.where(df['Z_Score'] > 1, 1, 0) # 1 means buy AMD and sell NVDA, 0 means no position
df['Position'] = df['Signal'].shift(1) # shift the signal down by 1 day to avoid look-ahead bias

# calculating AMD's and NVDA's daily percentage return
df['AMD_Return'] = df['AMD'].pct_change()
df['NVDA_Return'] = df['NVDA'].pct_change()

# calculating the strategy's daily return based on the position and the returns of the two stocks
df['Strategy_Return'] = df['Position'] * df['AMD_Return']

# calculating the cumulative returns of a $1 investment
df['Benchmark_Cumulative_Return'] = (1 + df['AMD_Return']).cumprod()
df['Strategy_Cumulative_Return'] = (1 + df['Strategy_Return']).cumprod()

# dropping missing values that were created by the rolling calculations
df = df.dropna()

#printing the final dataframe to see the results
print(f"$1 Buy & Hold AMD: ${df['Benchmark_Cumulative_Return'].iloc[-1]:.2f}")
print(f"$1 Pairs Trading Strategy: ${df['Strategy_Cumulative_Return'].iloc[-1]:.2f}")

# creating a chart for visual comparison of the cumulative returns of the strategy and the benchmark
plt.figure(figsize=(12, 6))
plt.plot(df['Benchmark_Cumulative_Return'], label='Buy & Hold AMD', color='blue')
plt.plot(df['Strategy_Cumulative_Return'], label='Pairs Trading (Z-Score)', color='orange')
plt.title('Cumulative Returns of Pairs Trading Strategy vs Buy & Hold')
plt.legend()
plt.savefig('pairs_trading_strategy.png')
print("Chart saved as pairs_trading_strategy.png")