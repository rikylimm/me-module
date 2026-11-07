"""Run every practice lab and print its result."""
import importlib
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1]))

LABS = [
    "lab01_ph", "lab02_kinetics", "lab03_balances", "lab04_monod", "lab05_fba",
    "lab06_mdv", "lab07_power", "lab08_doe", "lab09_ml", "lab10_bootstrap",
]

def main() -> None:
    for name in LABS:
        print(f"\n=== {name} ===")
        mod = importlib.import_module(f"practice.labs.{name}")
        mod.main()

if __name__ == "__main__":
    main()
