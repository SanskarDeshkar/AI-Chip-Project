# The AI Chip Wars: A Correlation & Lead/Lag Analysis

This is a Python-based project analyzing the stock market relationship between semiconductor suppliers and the hardware original equipment manufacturers (OEMs for short) that use them in their devices.

**Project Question:** How correlated are chip suppliers (like Nvidia, AMD) to hardware makers (like Apple, Dell)? Is there a "lead/lag" effect, where chip stock performance can predict hardware stock performance?

---

## Tools & Libraries Used

* **Python 3**
* **yfinance:** To download historical stock data from the Yahoo Finance API.
* **pandas:** For all data manipulation, cleaning, and analysis (calculating returns, correlations, and lead/lag shifts).
* **matplotlib & seaborn:** To visualize the results.

---

## Analysis & Findings

### 1. Correlation of Daily Returns (2020-2025)

After analyzing 4 years of daily returns, I found that the highest correlation usually falls between two chip manufacturers. For example, NVIDIA and AMD have the highest correlation, at r = 0.75. These results strongly imply that the market views the chip manufacturers and the hardware OEMs as one giant interconnected business, where a rise in one correlates to a rise in another.

`![Correlation Heatmap](correlation_heatmap.png)`

### 2. Lead/Lag Effect

To test for a predictive relationship, I shifted just the semiconductor supplier data forward by one day. My analysis found that every correlation between a lagged chip manufacturer and a hardware OEM was negative, but close to 0. The lowest correlations were between a lagged and unlagged chip manufacturer (lagged Qualcomm & unlagged NVIDIA had a correlation of r = 0.13). These results seemingly imply that there is little to no predictive relationship between a chip supplier's stock yesterday and a hardware OEM's stock today.

`![Lagged Correlation Heatmap](lagged_correlation_heatmap.png)`

### 3. Performance & Growth

These charts show the cumulative growth of $1 invested in both semiconductor suppliers and hardware OEMs. The clear winner in the chip manufacturers is NVIDIA (ending at around $23 for each $1 invested), while the clear winner in the hardware OEMs is Dell (ending at a little less than $5 for each $1 invested). The losing chip supplier is Intel and the losing device manufacturer is Samsung (both making barely over $1 for each $1 invested). Both growth charts share a similar patterns, with a low start, small dip in early 2020, constant flucutation, and an end with a single stock finishing way above the others.

`![Chip Manufacturer Growth Chart](chip_mfrs_growth_chart.png)`
`![Hardware OEMs Growth Chart](hardware_oems_growth_chart.png)`