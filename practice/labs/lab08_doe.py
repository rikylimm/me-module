"""Lab 08: fit a two-factor response surface by least squares."""
import numpy as np

def design_ccd():
    a = np.array([-1, 1, -1, 1, -1.414, 1.414, 0, 0])
    b = np.array([-1, -1, 1, 1, 0, 0, -1.414, 1.414])
    return a, b

def fit_quadratic(a, b, y):
    a = np.asarray(a, float); b = np.asarray(b, float); y = np.asarray(y, float)
    X = np.column_stack([np.ones_like(a), a, b, a * b, a**2, b**2])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    return dict(zip(["intercept", "a", "b", "ab", "a2", "b2"], beta))

def main() -> None:
    a, b = design_ccd()
    # synthetic surface: 10 + 3a - 2b + 1.5ab - 2a^2 - 1b^2
    y = 10 + 3*a - 2*b + 1.5*a*b - 2*a**2 - 1*b**2
    print({k: round(v, 3) for k, v in fit_quadratic(a, b, y).items()})

if __name__ == "__main__":
    main()
