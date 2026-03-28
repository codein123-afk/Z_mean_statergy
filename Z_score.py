import yfinance as yf 
import matplotlib.pyplot as plt 
import pandas as pd 
import math 

data=yf.download("TSLA",start="2023-01-01",end="2024-01-01")
close=data["Close"]["TSLA"]

rolling_mean=close.rolling(window=20).mean()
rolling_std=close.rolling(window=20).std()

z_score=(close-rolling_mean)/rolling_std

buy_signal=(z_score < -2)
sell_signal=(z_score > 2)

buy=close[buy_signal]
sell=close[sell_signal]

close.plot()
plt.scatter(buy.index,buy.values,color="green",label="buy")
plt.scatter(sell.index,sell.values,color="red",label="sell")
plt.xlabel("Date")
plt.ylabel("price")
plt.show()

cash=10000
shares=0
portfolio=[]

for date in close.index:
    if buy_signal[date] == True and cash>close[date]:
        shares_today =cash//close[date]
        cash-=shares_today*close[date]
        shares+=shares_today

    if sell_signal[date]== True and shares>0:
        cash+=shares*close[date]
        shares=0
    portfolio_today=cash+ shares*close[date]
    portfolio.append(portfolio_today)


portfolio_series=pd.Series(portfolio,index=close.index)

Total_return = (portfolio_series.iloc[-1]- portfolio_series[0])/portfolio_series.iloc[0]*100
print(f"Total return:{Total_return:.2f}%")

Benchmark_return=((close.iloc[-1]-close.iloc[0])/close.iloc[0]*100)
print(f'Benchmark Returns:{Benchmark_return:.2f}%')

rolling_peak=portfolio_series.cummax()
drawdown=(portfolio_series-rolling_peak)/rolling_peak*100
Max_Drawdown=drawdown.min()
print(f"Max Drawdown:{Max_Drawdown:.2f}%")

daily_returns=portfolio_series.pct_change()
daily_average_return=daily_returns.mean()
std_daily_return=daily_returns.std()
sharpe_ratio= (daily_average_return/std_daily_return)*math.sqrt(252)
print(f"Sharpe Ratio:{sharpe_ratio:.2f}")


