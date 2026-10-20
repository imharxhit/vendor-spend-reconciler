# vendor-spend-reconciler

Automated P&L variance, procurement rate-card audit, and DCF valuation bridge built with Python, MySQL, and MS Excel.

## Key Capabilities
- **Rate-Card & SLA Audit (`src/reconcile_invoices.py`)**: Matches invoice line items against contracted SKU/service rates and flags variances `>1.5%`.
- **Working Capital & DCF Sensitivity**: Computes Free Cash Flow to Firm (FCFF), WACC, and intrinsic enterprise value across Bull, Base, and Bear operating margin scenarios.
