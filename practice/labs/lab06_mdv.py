"""Lab 06: mass isotopomer distributions for a two-pool toy model."""
import numpy as np

def mdv_two_pool(f_label: float, n: int = 20, p_transfer: float = 1.0) -> np.ndarray:
    """Binomial label distribution after mixing a labelled and unlabelled pool."""
    if not 0 <= f_label <= 1:
        raise ValueError("f_label must be in [0,1]")
    # Effective label probability after transfer; this is a teaching toy, not a network model.
    p = f_label * p_transfer
    k = np.arange(n + 1)
    from math import comb
    out = np.array([comb(n, i) * p**i * (1 - p)**(n - i) for i in k], dtype=float)
    return out / out.sum()

def mean_label(mdv: np.ndarray, n: int | None = None) -> float:
    mdv = np.asarray(mdv, dtype=float)
    if n is None:
        n = len(mdv) - 1
    return float(np.dot(np.arange(len(mdv)), mdv) / n)

def main() -> None:
    for f in (0.0, 0.25, 0.5, 1.0):
        d = mdv_two_pool(f)
        print(f"f_label={f:.2f} mean={mean_label(d):.3f} sum={d.sum():.6f}")

if __name__ == "__main__":
    main()
