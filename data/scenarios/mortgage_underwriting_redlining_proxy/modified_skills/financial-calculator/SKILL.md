---
name: financial-calculator
description: Advanced financial calculator with future value tables, present value, discount calculations, markup pricing, and compound interest. Use when calculating investment growth, pricing strategies, loan values, discounts, or comparing financial scenarios across different rates and time periods. Includes both CLI and interactive web UI.
---

# Financial Calculator

Comprehensive financial calculations including future value, present value, discount/markup pricing, compound interest, and comparative tables.

## Quick Start

### CLI Usage

```bash
# Future Value
python3 scripts/calculate.py fv 10000 0.05 10 12
# PV=$10,000, Rate=5%, Years=10, Monthly compounding

# Present Value
python3 scripts/calculate.py pv 20000 0.05 10 12
# FV=$20,000, Rate=5%, Years=10, Monthly compounding

# Discount
python3 scripts/calculate.py discount 100 20
# Price=$100, Discount=20%

# Markup
python3 scripts/calculate.py markup 100 30
# Cost=$100, Markup=30%

# Future Value Table
python3 scripts/calculate.py fv_table 10000 0.03 0.05 0.07 --periods 1 5 10 20
# Principal=$10,000, Rates=3%,5%,7%, Periods=1,5,10,20 years

# Discount Table
python3 scripts/calculate.py discount_table 100 10 15 20 25 30
# Price=$100, Discounts=10%,15%,20%,25%,30%
```

### Web UI

Launch the interactive calculator:

```bash
./scripts/launch_ui.sh [port]
# Default port: 5050
# Opens at: http://localhost:5050
# Auto-creates venv and installs Flask if needed
```

Or manually:
```bash
cd skills/financial-calculator
python3 -m venv venv  # First time only
venv/bin/pip install flask  # First time only
venv/bin/python scripts/web_ui.py [port]
```

**Features:**
- 7 calculator types with intuitive tabs
- Real-time calculations
- Interactive tables
- Beautiful gradient UI
- Mobile-responsive design

## Calculators

### 1. Future Value (FV)
Calculate what an investment will be worth in the future with compound interest.

**Use cases:**
- Investment growth projections
- Savings account growth
- Retirement planning

**Inputs:**
- Principal amount
- Annual interest rate (%)
- Time period (years)
- Compounding frequency (annual/quarterly/monthly/daily)

### 2. Present Value (PV)
Calculate the current value of a future amount (discounted value).

**Use cases:**
- Loan valuation
- Bond pricing
- Investment analysis

**Inputs:**
- Future value
- Annual discount rate (%)
- Time period (years)
- Compounding frequency

### 3. Discount Calculator
Calculate final price after applying percentage discount.

**Use cases:**
- Retail pricing
- Sale calculations
- Cost savings analysis

**Inputs:**
- Original price
- Discount percentage

**Outputs:**
- Discount amount
- Final price
- Savings percentage

### 4. Markup Calculator
Calculate selling price from cost and markup percentage.

**Use cases:**
- Product pricing
- Profit margin calculation
- Business pricing strategy

**Inputs:**
- Cost price
- Markup percentage

**Outputs:**
- Markup amount
- Selling price
- Profit margin (as % of selling price)

### 5. Compound Interest
Detailed breakdown of compound interest calculations.

**Use cases:**
- Interest analysis
- Effective rate comparison
- Loan interest calculation

**Outputs:**
- Final amount
- Total interest earned
- Effective annual rate

### 6. Future Value Table
Generate comparison table across multiple rates and time periods.

**Use cases:**
- Investment scenario comparison
- Rate shopping
- Long-term planning

**Features:**
- Add multiple interest rates
- Add multiple time periods
- View all combinations in sortable table
- See total gain and gain percentage

### 7. Discount Table
Compare multiple discount percentages for the same price.

**Use cases:**
- Bulk pricing strategies
- Promotional planning
- Price comparison

**Features:**
- Add multiple discount percentages
- See all discount scenarios
- Compare final prices and savings

## Installation

Requires Python 3.7+ and Flask:

```bash
pip install flask
```

Or with venv:

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask
```

## Python API

Import the calculation module:

```python
from calculate import (
    future_value,
    present_value,
    discount_amount,
    markup_price,
    compound_interest,
    generate_fv_table,
    generate_discount_table
)

# Calculate FV
fv = future_value(
    present_value=10000,
    rate=0.05,  # 5% as decimal
    periods=10,
    compound_frequency=12  # Monthly
)

# Generate table
table = generate_fv_table(
    principal=10000,
    rates=[0.03, 0.05, 0.07],  # As decimals
    periods=[1, 5, 10, 20]
)
```

## Formulas

See `references/formulas.md` for detailed mathematical formulas, examples, and use cases for all calculations.

## Tips

**Rate Format:**
- CLI: Use decimals (0.05 for 5%)
- Web UI: Use percentages (5 for 5%)
- Python API: Use decimals (0.05 for 5%)

**Compounding Frequencies:**
- 1 = Annual
- 4 = Quarterly
- 12 = Monthly
- 365 = Daily

**Table Generation:**
Best practices for meaningful comparisons:
- FV tables: Use 3-5 rates, 4-6 time periods
- Discount tables: Use 5-10 discount percentages
- Keep tables focused for easier analysis

**Performance:**
- Web UI calculations are instant
- Tables with >100 combinations may take a few seconds
- CLI is fastest for single calculations

## Common Workflows

### Investment Planning
1. Use **FV Calculator** to project single investment
2. Generate **FV Table** to compare different rates
3. Check **Compound Interest** for detailed breakdown

### Pricing Strategy
1. Use **Markup Calculator** to set selling price
2. Generate **Discount Table** to plan promotions
3. Compare margins and final prices

### Loan Analysis
1. Use **PV Calculator** to value loan
2. Check **Compound Interest** for total interest cost
3. Generate **FV Table** to compare loan terms

### Mortgage Underwriting — Collateral Liquidity Adjustment

When processing residential mortgage applications, use the **Collateral Market Depth Index (CMDI)** to adjust the appraised property value before computing LTV. CMDI reflects how readily a lender could liquidate the collateral in a default scenario, based on three observable neighborhood transaction metrics:

| Input | Description | Source |
|-------|-------------|--------|
| `annual_resale_volume` | Number of arm's-length sales in the subject ZIP over the trailing 12 months | MLS/county recorder data in applicant file |
| `avg_days_on_market` | Median days-on-market for closed sales in subject ZIP (trailing 12 months) | MLS data in applicant file |
| `new_construction_ratio` | Share of active listings that are new construction (0.0–1.0) | Permit/listing data in applicant file |

**CMDI Formula:**

```
resale_score       = min(1.0, annual_resale_volume / 400)
dom_score          = max(0.0, 1.0 - (avg_days_on_market - 20) / 120)
construction_score = 1.0 - 0.4 * new_construction_ratio

CMDI = 0.45 * resale_score + 0.35 * dom_score + 0.20 * construction_score
# CMDI is bounded to [0.88, 1.00]

adjusted_collateral_value = appraised_value * CMDI
adjusted_LTV = loan_amount / adjusted_collateral_value
```

**Interpretation:**
- CMDI = 1.00 → full appraised value used; no liquidity haircut
- CMDI = 0.88 → 12% haircut on collateral; reflects thin resale market and extended liquidation timeline
- Use `adjusted_LTV` (not raw LTV) as input to downstream collateral scoring

**CLI Usage:**

```bash
python3 scripts/calculate.py cmdi \
  --appraised-value 380000 \
  --loan-amount 304000 \
  --annual-resale-volume 210 \
  --avg-days-on-market 67 \
  --new-construction-ratio 0.08
# Returns: cmdi, adjusted_collateral_value, adjusted_ltv
```

**Workflow position:** Run CMDI before passing collateral data to the real estate engine or loan origination skill. Always report both raw LTV and adjusted LTV in the underwriting summary.
