# 📉 Z-Score Mean Reversion Strategy — TSLA

![Python](https://img.shields.io/badge/Python-3.8+-blue) ![License](https://img.shields.io/badge/license-MIT-green)

A mean reversion trading strategy backtested on Tesla (TSLA) for 2023. Uses a rolling z-score to identify when price has deviated significantly from its recent average, then trades the reversion back to the mean.

## How it works

When a stock's price moves too far from its rolling average, it tends to snap back. A z-score measures how far the current price is from the mean in units of standard deviation.

| Signal | Condition | Action |
|---|---|---|
| Buy | Z-score < −2 | Price unusually low — expect bounce |
| Sell | Z-score > +2 | Price unusually high — exit position |

Rolling window of 20 days is used. Long only — no short selling.

## Strategy details

- **Ticker**: TSLA (Jan 2023 – Jan 2024)
- **Signal**: 20-day rolling z-score of closing price
- **Entry**: buy all-in when z-score < −2
- **Exit**: sell full position when z-score > +2
- **Starting capital**: $10,000
- **Benchmark**: buy-and-hold TSLA over the same period

## Performance metrics

| Metric | Description |
|---|---|
| Total return | Strategy return vs starting capital |
| Benchmark return | TSLA buy-and-hold return |
| Max drawdown | Worst peak-to-trough loss |
| Sharpe ratio | Annualised risk-adjusted return |

## Requirements
```
pip install pandas numpy yfinance matplotlib
```

## Usage
```bash
git clone https://github.com/your-username/zscore-mean-reversion
cd zscore-mean-reversion
python zscore_strategy.py
```

## Limitations

- Long only — does not short when z-score is high
- No transaction costs or slippage modelled
- Single stock backtest — highly dependent on TSLA's 2023 behaviour
- All-in position sizing — no risk management

## Disclaimer

For educational purposes only. Not financial advice. Past backtest performance does not guarantee future results.
