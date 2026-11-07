import math
import unittest
import numpy as np
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))
from labs import lab01_ph, lab02_kinetics, lab03_balances, lab04_monod, lab05_fba, lab06_mdv, lab07_power, lab08_doe, lab09_ml, lab10_bootstrap

class TestLabs(unittest.TestCase):
    def test_ph(self):
        self.assertAlmostEqual(lab01_ph.undissociated_fraction(3.86, 3.86), 0.5, places=6)
        self.assertLess(lab01_ph.lactate_fraction(6.0), lab01_ph.lactate_fraction(4.0))

    def test_kinetics(self):
        s = np.array([0.5, 1, 2, 4, 8, 16, 32], float)
        v = lab02_kinetics.mm_rate(s, 10, 4)
        fit = lab02_kinetics.fit_mm(s, v)
        self.assertAlmostEqual(fit["vmax"], 10, delta=0.2)
        self.assertAlmostEqual(fit["km"], 4, delta=0.2)

    def test_balances(self):
        self.assertAlmostEqual(lab03_balances.degree_of_reduction("C6H12O6"), 4.0)
        self.assertAlmostEqual(lab03_balances.degree_of_reduction("C2H6O"), 6.0)
        self.assertEqual(lab03_balances.carbon_yield_ceiling("C6H12O6", "C2H6O"), 3.0)

    def test_monod(self):
        s = np.array([0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10], float)
        mu = lab04_monod.monod(s, 0.45, 0.08)
        fit = lab04_monod.fit_monod(s, mu)
        self.assertAlmostEqual(fit["mu_max"], 0.45, delta=0.02)
        self.assertAlmostEqual(fit["ks"], 0.08, delta=0.02)

    def test_fba(self):
        out = lab05_fba.lp_max_2d((2, 1), [(1, 1, "<=", 10), (1, 0, "<=", 6), (0, 1, "<=", 8)])
        self.assertAlmostEqual(out["objective"], 16.0)
        self.assertAlmostEqual(out["x"], 6.0)

    def test_mdv(self):
        d = lab06_mdv.mdv_two_pool(0.5)
        self.assertAlmostEqual(d.sum(), 1.0, places=12)
        self.assertAlmostEqual(lab06_mdv.mean_label(d), 0.5, delta=0.02)

    def test_power(self):
        n = lab07_power.sample_size_two_sample(1.0, 1.0)
        self.assertGreaterEqual(n, 15)
        self.assertGreater(lab07_power.power_two_sample(n, 1.0, 1.0), 0.75)
        self.assertLess(n, lab07_power.sample_size_two_sample(0.5, 1.0))

    def test_doe(self):
        a, b = lab08_doe.design_ccd()
        y = 10 + 3*a - 2*b + 1.5*a*b - 2*a**2 - 1*b**2
        fit = lab08_doe.fit_quadratic(a, b, y)
        self.assertAlmostEqual(fit["a"], 3.0, places=6)
        self.assertAlmostEqual(fit["b"], -2.0, places=6)
        self.assertAlmostEqual(fit["ab"], 1.5, places=6)

    def test_ml(self):
        rng = np.random.default_rng(1)
        X = rng.normal(size=(80, 4)); y = 2*X[:, 0] - X[:, 1]
        beta = lab09_ml.ridge_fit(X, y, 1e-6)
        self.assertAlmostEqual(beta[1], 2.0, delta=0.05)
        self.assertAlmostEqual(beta[2], -1.0, delta=0.05)
        groups = np.repeat(np.arange(8), 10)
        tr, te = lab09_ml.scaffold_split(groups)
        self.assertTrue(tr.any() and te.any())
        self.assertFalse(set(groups[tr]) & set(groups[te]))

    def test_bootstrap(self):
        rng = np.random.default_rng(2)
        x = rng.normal(5, 1, 30)
        lo, hi = lab10_bootstrap.bootstrap_ci(x, n_boot=500)
        self.assertLess(lo, x.mean())
        self.assertGreater(hi, x.mean())

if __name__ == "__main__":
    unittest.main()
