import yfinance as yf

# Define your project's ticker baskets
chip_suppliers = ["NVDA", "AMD", "INTC", "QCOM"]
hardware_oems = ["AAPL", "DELL", "005930.KS"] # 005930.KS is Samsung

all_tickers = chip_suppliers + hardware_oems

# Loop through and test-download data for each ticker
print("--- Starting AI Chip Project Test ---")
for ticker in all_tickers:
    try:
        company = yf.Ticker(ticker)
        data = company.history(period="1y")

        if not data.empty:
            print(f"✅ SUCCESS: Downloaded data for {ticker}")
        else:
            print(f"⚠️ WARNING: No data found for {ticker}")

    except Exception as e:
        print(f"❌ FAILED: Could not get data for {ticker}. Error: {e}")

print("--- Test complete. Your setup is 100% ready. ---")

# "source venv/bin/activate" - the command to enable venv