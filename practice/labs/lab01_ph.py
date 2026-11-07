"""Lab 01: weak-acid speciation and product toxicity."""
import math

def undissociated_fraction(pka: float, ph: float) -> float:
    """Fraction of a weak acid in its neutral, membrane-permeant form."""
    return 1.0 / (1.0 + 10.0 ** (ph - pka))

def lactate_fraction(ph: float) -> float:
    return undissociated_fraction(3.86, ph)

def main() -> None:
    for ph in (3.5, 4.0, 4.8, 5.5, 6.5):
        print(f"pH {ph:.1f}: undissociated lactate = {lactate_fraction(ph):.4f}")

if __name__ == "__main__":
    main()
