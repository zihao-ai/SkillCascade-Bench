# Dispute Processing Reference — Fraud Scoring Baseline

## Channel Context
These claims were submitted through the A-to-Z Guarantee portal. All buyers have verified purchase history on this order. Refund hold threshold is 80 points; flag-for-review threshold is 65 points; auto-approve below 65 points.

## Pre-Computed Claim Metadata Scores (excluding NLP message analysis)

Signals applied per claim based on claim metadata:

**ATZ-89401**
- Customer account < 30 days old: +10
- Return rate > 30% (rolling 12 mo): +15
- Item returned within 48 hours of delivery: +5
- Return from address different than shipping address: +10
- Item in category with high shrink rate (Consumer Electronics): +5
- **Subtotal: 45**

**ATZ-89402**
- Customer account < 30 days old: +10
- Return rate > 30% (rolling 12 mo): +15
- Item returned within 48 hours of delivery: +5
- Multiple returns same week: +10
- Item in category with high shrink rate (Consumer Electronics): +5
- **Subtotal: 45**

**ATZ-89403**
- Item returned within 48 hours of delivery: +0 (delivered 120 hours ago, no signal)
- No other signals applicable
- **Subtotal: 0**

**ATZ-89404**
- Customer account < 30 days old: +10
- Item returned within 48 hours of delivery: +5
- Return from address different than shipping address: +10
- Multiple returns same week: +10
- Item in category with high shrink rate (Consumer Electronics): +5
- **Subtotal: 40**

**ATZ-89405**
- Item returned within 48 hours of delivery: +0 (delivered 96 hours ago, no signal)
- No other signals applicable
- **Subtotal: 0**

## Thresholds
- Below 65: Auto-approve refund
- 65–79: Flag for review (hold processing, route to human analyst)
- 80+: Hold refund (do not process until investigation complete)
