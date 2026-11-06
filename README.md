# MNM AU Seekers 2.4

## Scope: live data and analysis only

**Trading execution is explicitly on hold.** This project is a read-only XAU/USD analysis dashboard. BUY, SELL and WAIT are research signals, not executable orders. No broker login, order submission, automatic execution, account balances, or trading permissions should be implemented or requested in this development phase.

## Current implementation

Minimal Android-browser-friendly status dashboard, read-only Twelve Data M15 candle proxy, health endpoint and Render blueprint. Live market access requires a valid provider subscription and `TWELVE_DATA_API_KEY` configured privately in Render.

## Planned analytical dashboard

- M15, H1 and H4 candle charts and cross-timeframe alignment
- EMA 5; MA 9, 21, 63, 84; Bollinger Bands (21,2); MACD (no RSI)
- Support/resistance, candlestick patterns, market structure and liquidity sweeps
- 12-category directional score and explanatory BUY/SELL/WAIT analysis
- Historical pattern comparison and validated backtesting
- Data freshness indicators and read-only alerts

## Deployment

1. Create a Render Blueprint service from the development branch.
2. Add `TWELVE_DATA_API_KEY` as a secret environment variable in Render, never in GitHub.
3. Verify `/api/health` and `/api/candles` after deployment.

## Limitations

The current GitHub branch contains an **initial integration scaffold**, not the full scanner or scoring engine. Historical testing, live feed entitlement, dashboard modules and production security remain pending. Provider quotes may differ from XM MT5. No real trades are placed.
