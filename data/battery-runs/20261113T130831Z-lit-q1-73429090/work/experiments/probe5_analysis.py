#!/usr/bin/env python3
"""probe5_analysis.py

Compute the mean of the 40 probe-5 scores and a 95% two-sided confidence
interval for the mean using the Student t distribution with n-1 degrees of
freedom.

Input : /work/experiments/probe5_scores.csv  (columns: id, score; 40 data rows)
Output: printed statistics (mean, sample SD, SE, t*, CI bounds)

No third-party dependencies are available in this environment (no numpy,
scipy, or mpmath), so the t quantile is computed from first principles:
  1. Student t CDF via the regularized incomplete beta function I_x(a, b)
     (Numerical Recipes continued-fraction / Lentz algorithm).
  2. t* = quantile 0.975 found by bisection on that CDF.
The implementation is validated below against published table values.
"""

import csv
import math

CSV_PATH = "/work/experiments/probe5_scores.csv"
CONF = 0.95


# ---------------------------------------------------------------- incomplete beta
def betacf(a, b, x):
    """Continued fraction for the incomplete beta function (Lentz's method)."""
    MAXIT, EPS, FPMIN = 300, 3.0e-16, 1.0e-300
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < FPMIN:
        d = FPMIN
    d = 1.0 / d
    h = d
    for m in range(1, MAXIT + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < FPMIN:
            d = FPMIN
        c = 1.0 + aa / c
        if abs(c) < FPMIN:
            c = FPMIN
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < FPMIN:
            d = FPMIN
        c = 1.0 + aa / c
        if abs(c) < FPMIN:
            c = FPMIN
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < EPS:
            break
    return h


def betai(a, b, x):
    """Regularized incomplete beta function I_x(a, b)."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    lnbt = (math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
            + a * math.log(x) + b * math.log1p(-x))
    bt = math.exp(lnbt)
    if x < (a + 1.0) / (a + b + 2.0):
        return bt * betacf(a, b, x) / a
    return 1.0 - bt * betacf(b, a, 1.0 - x) / b


# ---------------------------------------------------------------- student t
def t_cdf(t, df):
    """CDF of Student's t distribution."""
    x = df / (df + t * t)
    tail = 0.5 * betai(df / 2.0, 0.5, x)
    return 1.0 - tail if t > 0 else tail


def t_ppf(p, df):
    """Quantile (inverse CDF) of Student's t via bisection on t_cdf."""
    if not 0.0 < p < 1.0:
        raise ValueError("p must be in (0, 1)")
    if p == 0.5:
        return 0.0
    if p < 0.5:
        return -t_ppf(1.0 - p, df)
    lo, hi = 0.0, 1.0
    while t_cdf(hi, df) < p:
        hi *= 2.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if t_cdf(mid, df) < p:
            lo = mid
        else:
            hi = mid
        if hi - lo < 1e-14:
            break
    return 0.5 * (lo + hi)


# ---------------------------------------------------------------- validation
def _selftest():
    # Published two-sided 95% critical values (t_{0.975, df}).
    table = {1: 12.7062, 2: 4.3027, 5: 2.5706, 10: 2.2281,
             20: 2.0860, 30: 2.0423, 39: 2.0227, 40: 2.0211, 100: 1.9840}
    for df, expected in table.items():
        got = t_ppf(0.975, df)
        assert abs(got - expected) < 5e-4, (df, got, expected)
    assert abs(t_cdf(0.0, 39) - 0.5) < 1e-12


# ---------------------------------------------------------------- main
def main():
    _selftest()

    scores = []
    with open(CSV_PATH, newline="") as fh:
        for row in csv.DictReader(fh):
            scores.append(float(row["score"]))

    n = len(scores)
    mean = sum(scores) / n
    ss = sum((x - mean) ** 2 for x in scores)
    sd = math.sqrt(ss / (n - 1))
    se = sd / math.sqrt(n)

    df = n - 1
    alpha = 1.0 - CONF
    t_crit = t_ppf(1.0 - alpha / 2.0, df)
    margin = t_crit * se

    lo, hi = mean - margin, mean + margin
    # sanity: the critical value must reproduce the target tail probability
    assert abs(t_cdf(t_crit, df) - (1.0 - alpha / 2.0)) < 1e-10

    print(f"n           = {n}")
    print(f"df          = {df}")
    print(f"mean        = {mean:.10f}  -> {mean:.2f}")
    print(f"sample sd   = {sd:.10f}")
    print(f"std error   = {se:.10f}")
    print(f"t*(0.975)   = {t_crit:.10f}")
    print(f"margin      = {margin:.10f}")
    print(f"95% CI      = [{lo:.10f}, {hi:.10f}]  -> [{lo:.2f}, {hi:.2f}]")
    print(f"min, max    = {min(scores):.2f}, {max(scores):.2f}")


if __name__ == "__main__":
    main()
