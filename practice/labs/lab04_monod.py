"""Lab 04: Monod fit and the mu_max-Ks correlation."""
import numpy as np

def monod(s, mu_max, ks):
    s = np.asarray(s, dtype=float)
    return mu_max * s / (ks + s)

def fit_monod(s, mu):
    s = np.asarray(s, dtype=float); mu = np.asarray(mu, dtype=float)
    best = (float("inf"), None, None)
    for ks in np.geomspace(0.005, 20.0, 3000):
        a = s / (ks + s)
        mu_max = float(a @ mu / (a @ a))
        sse = float(np.sum((mu - mu_max * a) ** 2))
        if sse < best[0]:
            best = (sse, mu_max, float(ks))
    return {"mu_max": best[1], "ks": best[2], "sse": best[0]}

def correlation_from_fit(s, mu, mu_max, ks):
    """Approximate local correlation of mu_max and Ks from finite differences."""
    s = np.asarray(s, dtype=float); mu = np.asarray(mu, dtype=float)
    eps = 1e-4
    J = np.column_stack([
        monod(s, mu_max * (1 + eps), ks) - monod(s, mu_max, ks),
        monod(s, mu_max, ks * (1 + eps)) - monod(s, mu_max, ks),
    ]) / eps
    # scale columns so the correlation is not dominated by units
    J = J / np.maximum(np.linalg.norm(J, axis=0), 1e-12)
    return float(J[:, 0] @ J[:, 1])

def main() -> None:
    s = np.array([0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0])
    mu = monod(s, 0.45, 0.08) * np.array([0.99, 1.01, 0.98, 1.02, 1.00, 1.01, 0.99, 1.00, 0.98])
    fit = fit_monod(s, mu)
    print({k: round(v, 5) for k, v in fit.items()})
    print("mu_max-Ks correlation", round(correlation_from_fit(s, mu, fit["mu_max"], fit["ks"]), 3))

if __name__ == "__main__":
    main()
