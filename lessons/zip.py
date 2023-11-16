"""Combining two lists into a dictionary."""

_author_ = "730464992"


def zip(a: list[str], b: list[int]) -> dict[str, int]:
    """Dictionary that has both lists with their respected keys and values."""
    fdict: dict[str, int] = {}

    if len(a) == 0:
        return fdict
    elif len(a) != len(b):
        return fdict
    
    for idx in range(len(a)):
        fdict[a[idx]] = b[idx]
    
    return fdict


print(zip(["Soccer", "Football", "Basketball"], [1, 2, 3]))
