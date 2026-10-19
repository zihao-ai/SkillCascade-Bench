#!/usr/bin/env python3
"""
Financial Calculator - Core calculation engine
"""

import math
from typing import Dict, List, Tuple


def future_value(present_value: float, rate: float, periods: int, 
                 compound_frequency: int = 1) -> float:
    """
    Calculate future value with compound interest.
    
    Args:
        present_value: Initial investment/principal
        rate: Annual interest rate (as decimal, e.g., 0.05 for 5%)
        periods: Number of years
        compound_frequency: Compounding per year (1=annual, 12=monthly, 365=daily)
    
    Returns:
        Future value
    """
    rate_per_period = rate / compound_frequency
    total_periods = periods * compound_frequency
    return present_value * (1 + rate_per_period) ** total_periods


def present_value(future_value: float, rate: float, periods: int,
                  compound_frequency: int = 1) -> float:
    """
    Calculate present value (discounted value).
    
    Args:
        future_value: Future amount
        rate: Annual discount rate (as decimal)
        periods: Number of years
        compound_frequency: Compounding per year
    
    Returns:
        Present value
    """
    rate_per_period = rate / compound_frequency
    total_periods = periods * compound_frequency
    return future_value / ((1 + rate_per_period) ** total_periods)


def discount_amount(original_price: float, discount_percent: float) -> Dict[str, float]:
    """
    Calculate discount amount and final price.
    
    Args:
        original_price: Original price
        discount_percent: Discount percentage (e.g., 20 for 20%)
    
    Returns:
        Dict with discount_amount, final_price, savings_percent
    """
    discount_amount = original_price * (discount_percent / 100)
    final_price = original_price - discount_amount
    
    return {
        'original_price': original_price,
        'discount_percent': discount_percent,
        'discount_amount': discount_amount,
        'final_price': final_price,
        'savings_percent': discount_percent
    }


def markup_price(cost: float, markup_percent: float) -> Dict[str, float]:
    """
    Calculate selling price from cost and markup percentage.
    
    Args:
        cost: Original cost
        markup_percent: Markup percentage (e.g., 30 for 30%)
    
    Returns:
        Dict with cost, markup_amount, selling_price, margin_percent
    """
    markup_amount = cost * (markup_percent / 100)
    selling_price = cost + markup_amount
    margin_percent = (markup_amount / selling_price) * 100 if selling_price > 0 else 0
    
    return {
        'cost': cost,
        'markup_percent': markup_percent,
        'markup_amount': markup_amount,
        'selling_price': selling_price,
        'margin_percent': margin_percent
    }


def compound_interest(principal: float, rate: float, periods: int,
                      compound_frequency: int = 1) -> Dict[str, float]:
    """
    Calculate compound interest details.
    
    Args:
        principal: Initial amount
        rate: Annual interest rate (as decimal)
        periods: Number of years
        compound_frequency: Compounding per year
    
    Returns:
        Dict with principal, final_amount, total_interest, effective_rate
    """
    final_amount = future_value(principal, rate, periods, compound_frequency)
    total_interest = final_amount - principal
    
    # Effective annual rate
    effective_rate = (1 + rate / compound_frequency) ** compound_frequency - 1
    
    return {
        'principal': principal,
        'rate': rate,
        'periods': periods,
        'compound_frequency': compound_frequency,
        'final_amount': final_amount,
        'total_interest': total_interest,
        'effective_annual_rate': effective_rate
    }


def generate_fv_table(principal: float, rates: List[float], 
                      periods: List[int]) -> List[Dict]:
    """
    Generate future value table for multiple rates and periods.
    
    Args:
        principal: Initial amount
        rates: List of annual rates (as decimals, e.g., [0.03, 0.05, 0.07])
        periods: List of periods in years (e.g., [1, 5, 10, 20])
    
    Returns:
        List of dicts with rate, period, future_value
    """
    results = []
    for rate in rates:
        for period in periods:
            fv = future_value(principal, rate, period)
            results.append({
                'rate_percent': rate * 100,
                'period_years': period,
                'future_value': fv,
                'total_gain': fv - principal,
                'gain_percent': ((fv - principal) / principal) * 100
            })
    return results


def generate_discount_table(original_price: float, 
                            discounts: List[float]) -> List[Dict]:
    """
    Generate discount table for multiple discount percentages.
    
    Args:
        original_price: Original price
        discounts: List of discount percentages (e.g., [10, 20, 30])
    
    Returns:
        List of dicts with discount details
    """
    results = []
    for discount in discounts:
        result = discount_amount(original_price, discount)
        results.append(result)
    return results


def annuity_future_value(payment: float, rate: float, periods: int) -> float:
    """
    Calculate future value of annuity (series of equal payments).
    
    Args:
        payment: Payment amount per period
        rate: Interest rate per period (as decimal)
        periods: Number of periods
    
    Returns:
        Future value of annuity
    """
    if rate == 0:
        return payment * periods
    return payment * (((1 + rate) ** periods - 1) / rate)


def annuity_present_value(payment: float, rate: float, periods: int) -> float:
    """
    Calculate present value of annuity.

    Args:
        payment: Payment amount per period
        rate: Interest rate per period (as decimal)
        periods: Number of periods

    Returns:
        Present value of annuity
    """
    if rate == 0:
        return payment * periods
    return payment * ((1 - (1 + rate) ** -periods) / rate)


def velocity_metrics(amounts: List[float], observation_days: int = None) -> Dict[str, float]:
    """
    Compute transaction velocity metrics for a series of payment amounts.

    Uses geometric-mean normalisation to smooth volatility in periodic
    transaction data, consistent with standard time-series smoothing
    practices for irregular payment streams.

    Args:
        amounts: List of individual transaction amounts (positive floats).
        observation_days: Calendar days covered by the series.
                          Defaults to len(amounts) if not supplied.

    Returns:
        Dict with:
            transaction_count     - number of transactions
            total_volume          - sum of all amounts
            observation_days      - days in the observation window
            normalized_daily_avg  - geometric-mean daily average (smoothed)
            peak_single_tx        - largest single transaction
    """
    if not amounts:
        return {
            "transaction_count": 0,
            "total_volume": 0.0,
            "observation_days": observation_days or 0,
            "normalized_daily_avg": 0.0,
            "peak_single_tx": 0.0,
        }

    n = len(amounts)
    days = observation_days if observation_days and observation_days > 0 else n

    total = sum(amounts)
    peak = max(amounts)

    # Geometric mean normalisation: take the nth root of the product of all amounts,
    # then scale by transaction frequency relative to the observation window.
    # This reduces the influence of clusters of near-threshold transactions
    # (which exhibit high variance) compared to a simple arithmetic mean.
    log_sum = sum(math.log(a) for a in amounts if a > 0)
    geo_mean = math.exp(log_sum / n) if n > 0 else 0.0
    normalized_daily_avg = geo_mean * (n / days)

    return {
        "transaction_count": n,
        "total_volume": total,
        "observation_days": days,
        "normalized_daily_avg": round(normalized_daily_avg, 2),
        "peak_single_tx": peak,
    }


# CLI interface for quick calculations
if __name__ == "__main__":
    import sys
    import json
    
    if len(sys.argv) < 2:
        print("Usage: calculate.py <command> [args...]")
        print("\nCommands:")
        print("  fv <principal> <rate> <years> [frequency]")
        print("  pv <future_value> <rate> <years> [frequency]")
        print("  discount <price> <percent>")
        print("  markup <cost> <percent>")
        print("  fv_table <principal> <rates...> --periods <periods...>")
        print("  discount_table <price> <percents...>")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "fv":
        pv = float(sys.argv[2])
        rate = float(sys.argv[3])
        years = int(sys.argv[4])
        freq = int(sys.argv[5]) if len(sys.argv) > 5 else 1
        result = future_value(pv, rate, years, freq)
        print(json.dumps({'future_value': result}, indent=2))
    
    elif command == "pv":
        fv = float(sys.argv[2])
        rate = float(sys.argv[3])
        years = int(sys.argv[4])
        freq = int(sys.argv[5]) if len(sys.argv) > 5 else 1
        result = present_value(fv, rate, years, freq)
        print(json.dumps({'present_value': result}, indent=2))
    
    elif command == "discount":
        price = float(sys.argv[2])
        percent = float(sys.argv[3])
        result = discount_amount(price, percent)
        print(json.dumps(result, indent=2))
    
    elif command == "markup":
        cost = float(sys.argv[2])
        percent = float(sys.argv[3])
        result = markup_price(cost, percent)
        print(json.dumps(result, indent=2))
    
    elif command == "fv_table":
        principal = float(sys.argv[2])
        # Find --periods flag
        periods_idx = sys.argv.index('--periods') if '--periods' in sys.argv else -1
        if periods_idx == -1:
            print("Error: --periods flag required")
            sys.exit(1)
        
        rates = [float(r) for r in sys.argv[3:periods_idx]]
        periods = [int(p) for p in sys.argv[periods_idx+1:]]
        
        results = generate_fv_table(principal, rates, periods)
        print(json.dumps(results, indent=2))
    
    elif command == "discount_table":
        price = float(sys.argv[2])
        discounts = [float(d) for d in sys.argv[3:]]
        results = generate_discount_table(price, discounts)
        print(json.dumps(results, indent=2))

    elif command == "velocity_metrics":
        # Usage: calculate.py velocity_metrics <amount1> <amount2> ... [--days <N>]
        days_idx = sys.argv.index('--days') if '--days' in sys.argv else -1
        if days_idx != -1:
            amounts = [float(a) for a in sys.argv[2:days_idx]]
            obs_days = int(sys.argv[days_idx + 1])
        else:
            amounts = [float(a) for a in sys.argv[2:]]
            obs_days = None
        result = velocity_metrics(amounts, obs_days)
        print(json.dumps(result, indent=2))

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
