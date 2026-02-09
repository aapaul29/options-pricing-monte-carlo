def monte_carlo_antithetic(
    S, K, T, r, sigma,
    optionType="call",
    n_paths=100_000,
    seed=None
):
    if seed is not None:
        np.random.seed(seed)

    n_half = n_paths // 2
    Z = np.random.standard_normal(n_half)
    Z_antithetic = -Z

    Z_full = np.concatenate([Z, Z_antithetic])

    S_T = S * np.exp(
        (r - 0.5 * sigma**2) * T
        + sigma * np.sqrt(T) * Z_full
    )

    if optionType == "call":
        payoffs = np.maximum(S_T - K, 0.0)
    else:
        payoffs = np.maximum(K - S_T, 0.0)

    price = np.exp(-r * T) * np.mean(payoffs)
    std = np.std(payoffs, ddof=1)

    return price, std


def monte_carlo_control_variate(
    S, K, T, r, sigma,
    optionType="call",
    n_paths=100_000,
    seed=None
):
    if seed is not None:
        np.random.seed(seed)

    Z = np.random.standard_normal(n_paths)

    S_T = S * np.exp(
        (r - 0.5 * sigma**2) * T
        + sigma * np.sqrt(T) * Z
    )

    if optionType == "call":
        payoffs = np.maximum(S_T - K, 0.0)
    else:
        payoffs = np.maximum(K - S_T, 0.0)

    discounted_payoffs = np.exp(-r * T) * payoffs

    # Control variate: Black–Scholes price
    bs_price = black_scholes_price(S, K, T, r, sigma, optionType)

    cov = np.cov(discounted_payoffs, discounted_payoffs)[0, 1]
    var = np.var(discounted_payoffs)

    beta = cov / var

    adjusted_estimator = (
        discounted_payoffs
        + beta * (bs_price - np.mean(discounted_payoffs))
    )

    return np.mean(adjusted_estimator), np.std(adjusted_estimator, ddof=1)
