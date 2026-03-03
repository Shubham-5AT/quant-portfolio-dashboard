import pandas as pd
import numpy as np
df=pd.read_csv("data\hyundai.csv",parse_dates=["Date"])
df=df.sort_values("Date")
df.set_index("Date",inplace=True)

df=df.dropna()

df["Returns"] = df["Close"].pct_change()


df["Log_Returns"] = np.log(df["Close"] / df["Close"].shift(1))

volatility = df["Log_Returns"].std()

annual_vol = volatility * np.sqrt(252)
stocks = ["hyndai", "prosche", "samsung"]
price_df = pd.DataFrame()

for stock in stocks:
    data = pd.read_csv(f"data\{stock}.csv")
    price_df[stock] = data["Close"]

returns = price_df.pct_change().dropna()
cov_matrix = returns.cov()

corr_matrix = returns.corr()

 
weights = np.array([0.4, 0.3, 0.3])
portfolio_variance = np.dot(weights.T, np.dot(cov_matrix, weights))
portfolio_volatility = np.sqrt(portfolio_variance)
