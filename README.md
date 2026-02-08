# options-pricing-monte-carlo
# Options Pricing with Black–Scholes and Monte Carlo

This project implements analytical and simulation-based pricing methods for European options,
with a focus on numerical accuracy, Greeks estimation, and variance reduction techniques.

## Features
- Black–Scholes pricing for European call and put options
- Analytical Greeks: Delta, Gamma, Vega, Theta
- Monte Carlo pricing under geometric Brownian motion
- Monte Carlo Greeks estimation
- Variance reduction techniques:
  - Antithetic variates
  - Control variates using the Black–Scholes price
- Numerical comparison and convergence analysis

## Motivation
Monte Carlo methods are widely used in quantitative finance but suffer from slow convergence.
This project explores how variance reduction techniques improve estimator efficiency without
increasing computational cost.

## Methodology
- Risk-neutral pricing framework
- Exact Black–Scholes formulas as analytical benchmark
- Monte Carlo simulation of terminal prices
- Variance reduction via correlation exploitation

## Results
- Monte Carlo prices converge to analytical Black–Scholes values
- Antithetic variates reduce variance with minimal overhead
- Control variates achieve significant variance reduction using known expectations

## Technologies
- Python
- NumPy
- SciPy
- Matplotlib

## How to Run
Clone the repository and open the notebook:

```bash
pip install -r requirements.txt
jupyter notebook notebooks/BlackScholesMonteCarlo.ipynb
