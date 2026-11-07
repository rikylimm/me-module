"""Lab 10: bootstrap confidence interval for a mean."""
import numpy as np

def bootstrap_ci(x, n_boot=2000, alpha=0.05, seed=1):
    x = np.asarray(x, float)
    rng = np.random.default_rng(seed)
    means = np.array([rng.choice(x, size=len(x), replace=True).mean() for _ in range(n_boot)])
    return float(np.quantile(means, alpha / 2)), float(np.quantile(means, 1 - alpha / 2))

def main() -> None:
    rng = np.random.default_rng(2)
    x = rng.normal(loc=5.0, scale=1.0, size=30)
    lo, hi = bootstrap_ci(x)
    print(f"mean={x.mean():.3f} 95% CI=({lo:.3f}, {hi:.3f})")

if __name__ == "__main__":
    main()
