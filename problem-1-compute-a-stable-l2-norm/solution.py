import numpy as np


def solve(x):
    """Numerically stable L2 norm: scale by max |x_i| to avoid overflow/underflow."""
    try:
        x = np.asarray(x, dtype=np.float64)
    except (TypeError, ValueError):
        raise ValueError("input must be a real numeric vector")

    if x.ndim != 1:
        raise ValueError("input must be a 1-D vector")
    if x.size == 0:
        raise ValueError("input must be non-empty")
    if not np.all(np.isfinite(x)):
        raise ValueError("input must contain only finite values")

    abs_x = np.abs(x)
    m = abs_x.max()
    if m == 0.0:
        return 0.0                      # all-zero vector, as the README specifies

    scaled = abs_x / m                  # all entries now in [0, 1]
    return float(m * np.sqrt(np.dot(scaled, scaled)))
