"""Lab 02: Michaelis-Menten fit and the bias of Lineweaver-Burk."""
import numpy as np

def mm_rate(s, vmax, km):
    s = np.asarray(s, dtype=float)
    return vmax * s / (km + s)

def fit_mm(s, v):
    """Grid search on Km with linear least squares for Vmax."""
    s = np.asarray(s, dtype=float); v = np.asarray(v, dtype=float)
    best = (float("inf"), None, None)
    for km in np.geomspace(0.05, 100.0, 4000):
        a = s / (km + s)
        vmax = float(a @ v / (a @ a))
        sse = float(np.sum((v - vmax * a) ** 2))
        if sse < best[0]:
            best = (sse, vmax, float(km))
    return {"vmax": best[1], "km": best[2], "sse": best[0]}

def lineweaver_burk(s, v):
    s = np.asarray(s, dtype=float); v = np.asarray(v, dtype=float)
    x = 1.0 / s; y = 1.0 / v
    slope, intercept = np.polyfit(x, y, 1)
    return {"vmax": 1.0 / intercept, "km": slope / intercept}

def r2(y, yhat):
    y = np.asarray(y); yhat = np.asarray(yhat)
    return 1.0 - np.sum((y - yhat) ** 2) / np.sum((y - np.mean(y)) ** 2)

def main() -> None:
    s = np.array([0.5, 1.0, 2.0, 4.0, 8.0, 16.0, 32.0])
    v = mm_rate(s, 10.0, 4.0) * np.array([1.00, 1.02, 0.98, 1.01, 0.99, 1.03, 0.97])
    nonlinear = fit_mm(s, v)
    linear = lineweaver_burk(s, v)
    print("nonlinear", {k: round(x, 3) for k, x in nonlinear.items()})
    print("Lineweaver-Burk", {k: round(x, 3) for k, x in linear.items()})
    print("R2 nonlinear", round(r2(v, mm_rate(s, nonlinear["vmax"], nonlinear["km"])), 4))

if __name__ == "__main__":
    main()
