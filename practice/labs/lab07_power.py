"""Lab 07: power and sample size with the normal approximation."""
from statistics import NormalDist

def sample_size_two_sample(delta: float, sd: float, alpha: float = 0.05, power: float = 0.8) -> int:
    if delta == 0 or sd <= 0:
        raise ValueError("delta must be non-zero and sd positive")
    z_a = NormalDist().inv_cdf(1 - alpha / 2)
    z_b = NormalDist().inv_cdf(power)
    return int(-(-(2 * ((z_a + z_b) * sd / abs(delta)) ** 2) // 1))

def power_two_sample(n: int, delta: float, sd: float, alpha: float = 0.05) -> float:
    z_a = NormalDist().inv_cdf(1 - alpha / 2)
    z = abs(delta) / (sd * (2 / n) ** 0.5)
    return 1 - NormalDist().cdf(z_a - z) + NormalDist().cdf(-z_a - z)

def main() -> None:
    for d in (0.5, 1.0, 2.0):
        n = sample_size_two_sample(d, 1.0)
        print(f"delta={d} n/group={n} achieved power={power_two_sample(n,d,1.0):.3f}")

if __name__ == "__main__":
    main()
