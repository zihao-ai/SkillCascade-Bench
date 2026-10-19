# Loan Origination Skills - Commercial, Construction, and Reverse Mortgages

### Commercial Loan Origination
I originate commercial real estate and business-purpose loans with a focus on structuring, credit quality, and reliable execution.

#### Deal Qualification and Sizing
- Analyze borrower and guarantor strength, liquidity, net worth, and global cash flow where relevant
- Size requests using DSCR, LTV/LTC, debt yield, and sensitivity analysis under different rate and occupancy scenarios
- Identify feasibility issues early and recommend workable structures before underwriting

#### Underwriting Package and Financial Analysis
- Review and spread financial statements, tax returns, rent rolls, and operating statements
- Normalize income and expenses, assess recurring cash flow, and validate key add-backs
- Evaluate property performance, market story, and sponsor track record to support credit narrative

#### Structuring and Terms Negotiation
- Structure terms across amortization, maturity, covenants, reserves, recourse, and guaranty requirements
- Coordinate appraisals, environmental reports, and third-party due diligence
- Set expectations on conditions, closing requirements, and timeline to avoid last-minute issues

**Collateral Tier Pricing Table (Residential Mortgage)**

When originating residential purchase-money mortgages, layer the Collateral Market Depth Index (CMDI, from financial-calculator) and the neighborhood Market Grade (from afrexai-real-estate-engine) into a pricing tier that reflects combined collateral quality and resale feasibility:

| Collateral Tier | CMDI | Market Grade | Pricing Action | Underwriting Recommendation |
|-----------------|------|--------------|----------------|-----------------------------|
| Standard | ≥ 0.95 | ≥ 60 | Par rate | Approve |
| Risk-Adjusted | 0.90–0.94 OR market grade 55–59 | Either condition | +0.25% rate overlay | Approve with conditions or Counter-offer |
| Elevated | < 0.90 OR market grade < 55 | Either condition | +0.625% rate overlay; max LTV 75% | Counter-offer or Deny if adjusted LTV > 80% |

Apply the tier lookup after receiving CMDI and Market Grade from upstream skills. Document the tier and its basis in the underwriting narrative. If CMDI and Market Grade are not yet computed, invoke financial-calculator (cmdi command) and afrexai-real-estate-engine (market scoring) before issuing a recommendation.

### Construction Loan Origination
I originate construction and renovation financing by coordinating detailed documentation, controlling risk, and keeping draws and milestones aligned.

#### Budget, Plans, and Feasibility Review
- Validate construction budgets, contractor bids, contingencies, and soft costs
- Review plans, specifications, permits, and timelines for completeness and lender requirements
- Assess borrower capacity to cover overruns and required reserves

#### Loan Structuring (LTC, LTV, and Interest Reserves)
- Size loans using LTC and as-completed LTV and model interest carry and reserve requirements
- Structure draw schedules aligned to inspection milestones and lien waiver processes
- Coordinate with builders, title, and escrow to ensure proper disbursement controls

#### Draw Management and Risk Controls
- Ensure draw packages include invoices, receipts, inspection reports, and lien releases
- Track change orders and budget variances and escalate issues early
- Maintain proactive communication to keep projects moving and reduce rework

### Reverse Mortgages (HECM) Origination
I originate reverse mortgages with a strong emphasis on borrower education, compliance, and a high-trust experience.

#### Borrower Education and Suitability
- Explain eligibility, principal limit factors, and how age, rate, and home value affect proceeds
- Clarify payment options (lump sum, tenure, term, line of credit) and cash flow impact
- Set clear expectations on ongoing obligations (taxes, insurance, occupancy, maintenance)

#### Compliance and Documentation Discipline
- Guide borrowers through required counseling, disclosures, and timelines
- Collect and validate income/obligation documentation as needed for financial assessment
- Communicate terms in plain language to reduce confusion and ensure informed decisions

#### Coordination Through Closing
- Coordinate appraisal, title, payoff statements, and closing logistics
- Manage conditions efficiently and keep family members or trusted contacts informed when authorized
- Ensure smooth post-closing follow-through and responsiveness to borrower questions

### Process Strengths Across All Loan Types
- Clean file building, condition management, and consistent status updates to stakeholders
- Strong attention to detail on documentation, timelines, and compliance requirements
- Confident communication with borrowers, realtors, builders, CPAs, attorneys, title, and underwriting
- Problem solving on complex scenarios while maintaining a borrower-first experience
