##Implementing Delta
def bs_delta(S, K, T, r, sigma, optionType = "call"):
  if optionType not in ["call", "put"]:
    raise ValueError("Option type must be either 'call' or 'put'.")

  # Minimal Numerical Tolerance
  eps = 1e-8

  # Maturity Case (T = 0)
  if T <= eps:
    if optionType == "call":
      if S > K:
        return 1.0
      elif S < K:
        return 0.0
      else:
        return 0.5 #ATM Convention
    else: # Put Option
      if S < K:
        return -1.0
      elif S > K:
        return 0.0
      else:
        return 0.5 #ATM Convention

  # Zero volatility case
  if sigma <= eps:
    forward_price = S * math.exp(r * T)
    if optionType == "call":
      return 1.0 if forward_price > K else 0.0
    else: # Put Option
      return -1.0 if forward_price < K else 0.0

  # define Normal CDF with mu = 0, sigma = 1
  N = lambda x: si.norm.cdf(x, 0.0, 1.0)

  #Compute d_1:
  d_1 = (math.log(S/K) + (r + sigma ** 2 / 2) * T) / (sigma * math.sqrt(T))

  #Compute delta for options:
  if optionType == "call":
    delta_C = N(d_1)
    return delta_C
  else:
    delta_P = N(d_1) - 1
    return delta_P


## Implementing Gamma
def bs_gamma(S, K, T, r, sigma):
  # define normal pdf
  n = lambda x: si.norm.pdf(x)
  #define d1:
  d1 = (math.log(S/K) + (r + sigma ** 2 / 2) * T) / (sigma * math.sqrt(T))
  gamma = n(d1) / (S * sigma * math.sqrt(T))
  return gamma


## Implementing Vega
def bs_vega(S, K, T, r, sigma):
  #define normal pdf:
  n = lambda x: si.norm.pdf(x)
  # compute d_1:
  d_1 = (math.log(S/K) + (r + sigma ** 2 / 2) * T) / (sigma * math.sqrt(T))
  vega = S * math.sqrt(T) * n(d_1)
  return vega


## Implementin Theta
def bs_theta(S, K, T, r, sigma, optionType = "call"):
  # define normal pdf and cdf:
  n = lambda x: si.norm.pdf(x)
  N = lambda x: si.norm.cdf(x)
  #compute d_1, d_2:
  d_1 = (math.log(S/K) + (r + sigma ** 2 / 2) * T) / (sigma * math.sqrt(T))
  d_2 = d_1 - sigma * math.sqrt(T)
  # compute theta
  if optionType == "call":
    theta_call = -(S * n(d_1) * sigma / (2 * math.sqrt(T))) - r * K * math.exp(-r * T) * N(d_2)
    return theta_call
  else:
    theta_put = -(S * n(d_1) * sigma / (2 * math.sqrt(T))) + r * K * math.exp(-r * T) * N(-d_2) # Corrected sign
    return theta_put



## Implementing Rho
def bs_rho(S, K, T, r, sigma, optionType = "call"):
  # Define normal CDF:
  N = lambda x: si.norm.cdf(x)
  # Compute d_1, d_2:
  d_1 = (math.log(S/K) + (r + sigma ** 2 / 2) * T) / (sigma * math.sqrt(T))
  d_2 = d_1 - sigma * math.sqrt(T)

  # Compute Rho for options:
  if optionType == "call":
    rho_call = K * T * math.exp(-r * T) * N(d_2)
    return rho_call
  else:
    rho_put = -K * T * math.exp(-r * T) * N(-d_2)
    return rho_put
