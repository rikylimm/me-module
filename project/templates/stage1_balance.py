"""Stage 1 starter: close carbon and electron balances.

The CSV is synthetic teaching data. Fill the TODOs; do not claim it is the thesis.
"""
import csv
from pathlib import Path

DATA = Path(__file__).parents[1] / "data" / "teaching_fermentation.csv"

def load():
    with DATA.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))

def c_mol(glucose_gL, biomass_gL, ethanol_gL, lactate_gL, acetate_gL):
    # TODO: convert g/L to C-mol/L using carbon fractions.
    raise NotImplementedError

def dor_balance(rows):
    # TODO: compute degree-of-reduction in and out; name the missing stream.
    raise NotImplementedError

if __name__ == "__main__":
    rows = load()
    print(f"{len(rows)} rows; implement c_mol and dor_balance")
