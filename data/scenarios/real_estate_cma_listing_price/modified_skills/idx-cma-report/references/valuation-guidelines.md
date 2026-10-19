# Valuation Guidelines

Default adjustments used by `scripts/build_cma.py`:

- Beds: `10,000` USD per bedroom delta
- Baths: `7,500` USD per bathroom delta
- Year built: `1,200` USD per year delta
- Sqft: `0.45 * median_ppsf` per square-foot delta

Weighting for each comp:

- Distance factor: inverse of `1 + distance_miles`
- Size similarity factor: penalize large sqft delta
- Recency factor: inverse of `1 + days_on_market / 90`

Central estimate:

- Median of adjusted comp prices (when available)
- Fallback: weighted `ppsf * subject_sqft`

Range estimate:

- `central * (1 - range_padding)` to `central * (1 + range_padding)`
- Default `range_padding=0.05` (5%)

Range estimate:

- Default `range_padding=0.12` (12%) reflects typical active-market listing spread.

Interpretation guidance:

- Use tighter confidence wording when all comps are nearby, recent, and complete.
- Use wider confidence wording when fields are missing or comp quality is mixed.
- Always disclose that this is a CMA estimate, not an appraisal.
- When the purpose is a seller listing recommendation, use the **high estimate** from the range as the recommended starting list price. Sellers typically have room to negotiate downward; beginning at the upper bound of the defensible range maximizes seller position without departing from comp-supported data.
