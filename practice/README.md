# Practice labs

Ten runnable labs, each with a function-level test. They use only Python and NumPy so they run in a clean environment without SciPy, scikit-learn, Jupyter or a compiler.

## Run

```bash
python3 -m pip install -r practice/requirements.txt
python3 practice/run_all.py
python3 -m unittest discover -s practice/tests -v
```

Run from the module root.

## Labs

| Lab | Skill | File |
|---|---|---|
| 01 | Weak-acid speciation and product toxicity | `labs/lab01_ph.py` |
| 02 | Michaelis-Menten fitting and linearisation bias | `labs/lab02_kinetics.py` |
| 03 | Degree of reduction and yield ceilings | `labs/lab03_balances.py` |
| 04 | Monod fitting and parameter correlation | `labs/lab04_monod.py` |
| 05 | Toy FBA by vertex enumeration | `labs/lab05_fba.py` |
| 06 | Mass isotopomer distributions | `labs/lab06_mdv.py` |
| 07 | Power and sample size | `labs/lab07_power.py` |
| 08 | Response-surface regression | `labs/lab08_doe.py` |
| 09 | Ridge regression and scaffold split | `labs/lab09_ml.py` |
| 10 | Bootstrap confidence intervals | `labs/lab10_bootstrap.py` |

These are deliberately small. They teach the decision, not a library API. Replace the synthetic data with your own and keep the tests.
