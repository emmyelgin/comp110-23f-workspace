"""Challenge Question."""

_author_ = "730464992"


def w_sum(vals: list[float]) -> float:
    """Compute the sum of a list using while loops."""
    total: float = 0.0
    idx: int = 0 
    while idx < len(vals):
        total += vals[idx]
        idx += 1
    return total
    

def f_sum(vals: list[float]) -> float:
    """Compute the usm of a list using a for in loop."""
    total = 0.0
    for items in vals:
        total += items
    return total


def f_range_sum(vals: list[float]) -> float:
    """Compute the sum of a list using for in range loop."""
    total = 0.0 
    for elem in range(len(vals)):
        total += vals[elem]
    return total