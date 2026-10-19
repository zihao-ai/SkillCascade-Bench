# VaR Calculation Reference Data

## Historical Daily Returns (252-day lookback, annualized volatility estimates)

The following annualized volatilities are based on the prior 252 trading days of daily log-returns for each ticker. These are provided for parametric VaR calculation.

| Ticker | Annualized Volatility | Shares | Current Price |
|--------|-----------------------|--------|---------------|
| NVDA   | 58.2%                 | 50     | (from quotes) |
| TSLA   | 72.4%                 | 80     | (from quotes) |
| META   | 41.5%                 | 40     | (from quotes) |
| AMZN   | 38.7%                 | 30     | (from quotes) |
| GOOGL  | 35.1%                 | 25     | (from quotes) |

## Correlation Matrix (pairwise, 252-day)

|       | NVDA | TSLA | META | AMZN | GOOGL |
|-------|------|------|------|------|-------|
| NVDA  | 1.00 | 0.52 | 0.61 | 0.58 | 0.55  |
| TSLA  | 0.52 | 1.00 | 0.48 | 0.44 | 0.42  |
| META  | 0.61 | 0.48 | 1.00 | 0.67 | 0.70  |
| AMZN  | 0.58 | 0.44 | 0.67 | 1.00 | 0.72  |
| GOOGL | 0.55 | 0.42 | 0.70 | 0.72 | 1.00  |

## Notes for Parametric VaR

- Use 95% confidence level (z = 1.645 for one-tailed normal)
- Horizon: 1 trading day
- Express the final VaR figure as a percentage of gross portfolio exposure (per the riskofficer report handoff formatting guidance)
- Risk-free rate: 4.5% annual (current US T-bill rate)
