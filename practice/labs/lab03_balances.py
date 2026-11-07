"""Lab 03: degree of reduction and carbon-yield ceilings."""
import re

def parse_formula(formula: str) -> dict:
    out = {}
    for el, n in re.findall(r"([A-Z][a-z]?)(\d*)", formula):
        if el:
            out[el] = out.get(el, 0) + (int(n) if n else 1)
    return out

def degree_of_reduction(formula: str) -> float:
    """Electrons available per carbon, relative to CO2, H2O and NH3."""
    a = parse_formula(formula)
    c = a.get("C", 0)
    if c == 0:
        raise ValueError("no carbon")
    return (4 * c + a.get("H", 0) - 2 * a.get("O", 0) - 3 * a.get("N", 0)) / c

def carbon_yield_ceiling(substrate: str, product: str) -> float:
    """Mol product per mol substrate from carbon conservation only."""
    cs = parse_formula(substrate).get("C", 0)
    cp = parse_formula(product).get("C", 0)
    if cs == 0 or cp == 0:
        raise ValueError("carbon-free formula")
    return cs / cp

def main() -> None:
    for f in ("C6H12O6", "C2H6O", "C2H4O2", "C3H6O3"):
        print(f, "DOR/C =", round(degree_of_reduction(f), 3))
    print("glucose -> ethanol carbon ceiling =", carbon_yield_ceiling("C6H12O6", "C2H6O"))

if __name__ == "__main__":
    main()
