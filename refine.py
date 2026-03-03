import pandas as pd
import numpy as np
stocks = ["hyundai", "porsche", "samsung"]
price_df = pd.DataFrame()

for stock in stocks:
    data = pd.read_csv(f"data/{stock}.csv", parse_dates=["Date"])
    data = data.sort_values("Date")
    data.set_index("Date", inplace=True)
    price_df[stock] = data["Close"]

price_df = price_df.dropna()

returns = price_df.pct_change().dropna()
log_returns = np.log(price_df / price_df.shift(1)).dropna()

daily_volatility = log_returns.std()
annual_volatility = daily_volatility * np.sqrt(252)


cov_matrix = returns.cov()
corr_matrix = returns.corr()

weights = np.array([0.4, 0.3, 0.3])

mean_returns = returns.mean()
portfolio_return = np.dot(weights, mean_returns) * 252  # Annual return

portfolio_variance = np.dot(weights.T, np.dot(cov_matrix * 252, weights))
portfolio_volatility = np.sqrt(portfolio_variance)


risk_free_rate = 0.05  # 5% assumed
sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility


print("\n========== INDIVIDUAL STOCK METRICS ==========")
print("Daily Volatility:\n", daily_volatility)
print("\nAnnual Volatility:\n", annual_volatility)

print("\n========== COVARIANCE MATRIX ==========")
print(cov_matrix)

print("\n========== CORRELATION MATRIX ==========")
print(corr_matrix)

print("\n========== PORTFOLIO METRICS ==========")
print("Expected Annual Return:", portfolio_return)
print("Portfolio Volatility:", portfolio_volatility)
print("Sharpe Ratio:", sharpe_ratio)
