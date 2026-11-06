# MNM AU Seekers 2.4

Early cloud integration scaffold for XAU/USD research. Includes a mobile-friendly feed-status page, read-only Twelve Data M15 candle proxy, health endpoint and Render blueprint.

## Deployment

1. Create a Render Blueprint service from this repository's development branch.
2. Add `TWELVE_DATA_API_KEY` as a secret environment variable in Render. Do not commit the key.
3. Verify `/api/health` and `/api/candles` after deployment.

The API key must have access to XAU/USD 15-minute historical candles. Provider entitlement and costs vary.

## Limitations

This GitHub branch currently contains a **minimal integration scaffold**, not the complete offline MNM 2.4 dashboard, historical backtesting engine, or 12-category scanner. Those modules still require migration and verification. No real trades are placed. Market data may differ from XM MT5 quotes.
