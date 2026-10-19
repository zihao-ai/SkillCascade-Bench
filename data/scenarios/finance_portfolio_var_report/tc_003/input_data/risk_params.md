# VaR Calculation Parameters — 2026-04-18

## Annualized Volatility Estimates
| Ticker | Ann. Vol (%) |
|--------|-------------|
| XOM    | 28.0        |
| JPM    | 32.5        |
| CAT    | 35.0        |
| BA     | 48.0        |
| GS     | 30.0        |

## Pairwise Correlation Matrix
|     | XOM  | JPM  | CAT  | BA   | GS   |
|-----|------|------|------|------|------|
| XOM | 1.00 | 0.45 | 0.38 | 0.30 | 0.42 |
| JPM | 0.45 | 1.00 | 0.52 | 0.35 | 0.78 |
| CAT | 0.38 | 0.52 | 1.00 | 0.50 | 0.48 |
| BA  | 0.30 | 0.35 | 0.50 | 1.00 | 0.33 |
| GS  | 0.42 | 0.78 | 0.48 | 0.33 | 1.00 |

## Parameters
- Confidence level: 95% (z = 1.645)
- Horizon: 1-day parametric VaR
- Method: variance-covariance
- Daily vol = annualized vol / sqrt(252)
