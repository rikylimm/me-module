"""Lab 05: a toy FBA solved by vertex enumeration.

This is deliberately not COBRApy. It makes the geometry visible:
maximise c.v subject to linear constraints by testing vertices.
"""
import itertools
import numpy as np

def lp_max_2d(c, constraints):
    """Maximise c.[x,y] over a bounded 2-D polygon.

    constraints: list of (a, b, op, rhs), op in {'<=', '>='}. Bounds must be finite.
    """
    lines = []
    for a, b, op, rhs in constraints:
        # Convert >= to <=
        if op == ">=":
            a, b, rhs = -a, -b, -rhs
        lines.append((a, b, rhs))
    # add non-negativity as constraints
    lines += [(-1, 0, 0), (0, -1, 0)]
    pts = []
    for (a1, b1, c1), (a2, b2, c2) in itertools.combinations(lines, 2):
        det = a1 * b2 - a2 * b1
        if abs(det) < 1e-12:
            continue
        x = (c1 * b2 - c2 * b1) / det
        y = (a1 * c2 - a2 * c1) / det
        if all(a * x + b * y <= rhs + 1e-9 for a, b, rhs in lines):
            pts.append((x, y))
    if not pts:
        raise ValueError("infeasible or unbounded")
    best = max(pts, key=lambda p: c[0] * p[0] + c[1] * p[1])
    return {"x": best[0], "y": best[1], "objective": c[0] * best[0] + c[1] * best[1]}

def main() -> None:
    # Toy network: v1 + v2 <= 10, v1 <= 6, v2 <= 8; maximise 2 v1 + v2
    constraints = [(1, 1, "<=", 10), (1, 0, "<=", 6), (0, 1, "<=", 8)]
    print(lp_max_2d((2, 1), constraints))

if __name__ == "__main__":
    main()
