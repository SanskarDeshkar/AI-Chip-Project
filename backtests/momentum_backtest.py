import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# creating a new dataframe to hold the closing prices of the two stocks
df = pd.read_csv("data/closing_prices.csv")

# making sure dates are in the correct format and set as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# calculating AMD's daily percentage return
df['AMD_Return'] = df['AMD'].pct_change()

# calculating the benchmark's cumulative return of a $1 investment in AMD
df['Benchmark_Cumulative_Return'] = (1 + df['AMD_Return']).cumprod()

# creating a rule that states to buy AMD when its price is above its 50-day average
df["MA50"] = df['AMD'].rolling(window=50).mean()
df['Signal'] = np.where(df['AMD'] > df['MA50'], 1, 0) # 1 means buy AMD, 0 means no position

# shifting the signal down by 1 day to avoid look-ahead bias
df['Position'] = df['Signal'].shift(1)
df['Strategy_Return'] = df['Position'] * df['AMD_Return']
df['Strategy_Cumulative_Return'] = (1 + df['Strategy_Return']).cumprod()

# dropping missing values that were created by the rolling calculations
df = df.dropna()

# making a chart for visual comparison of the cumulative returns of the strategy and the benchmark
plt.figure(figsize=(12, 6))
plt.plot(df['Benchmark_Cumulative_Return'], label='Buy & Hold AMD', color='blue', alpha=0.5)
plt.plot(df['Strategy_Cumulative_Return'], label='Momentum Strategy (MA50)', color='orange', linewidth=2)
plt.title('Cumulative Returns of Momentum Strategy vs Buy & Hold')
plt.legend()
plt.grid(True)

# saving the chart as a fire and naming it momentum_strategy.png
plt.savefig('momentum_strategy.png')
print("Chart saved as momentum_strategy.png")

# printing the final results
print(f"Final Buy & Hold: ${df['Benchmark_Cumulative_Return'].iloc[-1]:.2f}")
print(f"Final Momentum Strategy: ${df['Strategy_Cumulative_Return'].iloc[-1]:.2f}")

# calculating max drawdown for buy and hold
rolling_max_benchmark = df['Benchmark_Cumulative_Return'].cummax()
drawdown_benchmark = (df['Benchmark_Cumulative_Return'] - rolling_max_benchmark) / rolling_max_benchmark
max_drawdown_benchmark = drawdown_benchmark.min()

# calcuating max drawdown for momentum strategy
rolling_max_strategy = df['Strategy_Cumulative_Return'].cummax()
drawdown_strategy = (df['Strategy_Cumulative_Return'] - rolling_max_strategy) / rolling_max_strategy
max_drawdown_strategy = drawdown_strategy.min()

# printing final risk results
print(f"Max Drawdown Buy & Hold: {max_drawdown_benchmark:.2%}")
print(f"Max Drawdown Momentum Strategy: {max_drawdown_strategy:.2%}")