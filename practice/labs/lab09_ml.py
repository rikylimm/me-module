"""Lab 09: ridge regression and a grouped/scaffold split."""
import numpy as np

def ridge_fit(X, y, lam=1.0):
    X = np.asarray(X, float); y = np.asarray(y, float)
    n, p = X.shape
    Xa = np.column_stack([np.ones(n), X])
    pen = np.eye(p + 1) * lam
    pen[0, 0] = 0.0
    return np.linalg.solve(Xa.T @ Xa + pen, Xa.T @ y)

def predict(beta, X):
    X = np.asarray(X, float)
    return np.column_stack([np.ones(len(X)), X]) @ beta

def scaffold_split(groups, test_fraction=0.2):
    groups = np.asarray(groups)
    unique = np.unique(groups)
    rng = np.random.default_rng(7)
    rng.shuffle(unique)
    n_test = max(1, int(round(len(unique) * test_fraction)))
    test_groups = set(unique[:n_test])
    test = np.array([g in test_groups for g in groups])
    return ~test, test

def main() -> None:
    rng = np.random.default_rng(1)
    X = rng.normal(size=(80, 4))
    y = 2*X[:, 0] - X[:, 1] + 0.5*X[:, 2] + rng.normal(scale=0.1, size=80)
    beta = ridge_fit(X, y, lam=0.1)
    print("beta", np.round(beta, 3))
    groups = np.repeat(np.arange(8), 10)
    tr, te = scaffold_split(groups)
    print("train/test", tr.sum(), te.sum())

if __name__ == "__main__":
    main()
