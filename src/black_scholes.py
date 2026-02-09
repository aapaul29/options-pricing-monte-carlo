##Black-Scholes Pricing Function
def black_scholes_price(S, K, T, r, sigma, optionType = "call"):
  #Check valid market inputs
  if optionType not in ["call", "put"]:
    raise ValueError("Option type must be either 'call' or 'put'.")
  if sigma <= 0:
    raise ValueError("Volatility (sigma) must be greater than zero.")
  if T < 0:
    raise ValueError("Time to expiry (T) must be greater than zero.")
  if S < 0:
    raise ValueError("Spot price (S) must be greater than zero.")
  if K < 0:
    raise ValueError("Strike price (K) must be greater than zero.")

  #immediate payoff (T = 0)
  if T <= 1e-8:
    if optionType == "call":
      return max(0, S - K)
    else:
      return max(0, K - S)

  #Zero volatility (sigma = 0)
  if sigma == 1e-8:
    if optionType == "call":
      return max(0, S - K * math.exp(-r * T))
    else:
      return max(0, K * math.exp(-r * T) - S)
  #Compute d_1:
  d_1 = (math.log(S/K) + (r + sigma ** 2 / 2) * T) / (sigma * math.sqrt(T))
  #Compute d_2:
  d_2 = d_1 - sigma * math.sqrt(T)

  # Define Normal CDF function with mu = 0, sigma = 1
  N = lambda x: si.norm.cdf(x, 0.0, 1.0)

  # return call and put option
  if optionType == "call":
    call = S * N(d_1) - N(d_2) * K * math.exp(-r * T)
    return call
  else:
    put = K * math.exp(-r * T) * N(-d_2) - S * N(-d_1)
    return put
