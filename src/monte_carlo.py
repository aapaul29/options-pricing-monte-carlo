## Implementing Monte Carlo Pricing
def monte_carlo_price(S, K, T, r, sigma, optionType = "call", num_simulations = 10000, random_numbers=None):
  # Generate random numbers if not provided (for CRN technique)
  if random_numbers is None:
      Z = np.random.standard_normal(size = num_simulations)
  else:
      Z = random_numbers

  #Compute S_T:
  S_T = S * np.exp((r - 0.5 * sigma ** 2) * T + sigma * math.sqrt(T) * Z)
  # Compute payoff:
  if optionType == "call":
    payoff = np.maximum(S_T - K, 0)
  else:
    payoff = np.maximum(K - S_T, 0)
  # Discount the average
  price = math.exp(-r * T) * np.mean(payoff)
  return price
