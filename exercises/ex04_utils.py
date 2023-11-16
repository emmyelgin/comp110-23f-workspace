"""List Utility Functions."""

_author_ = "730464992"


def all(numbers: list[int], an_int: int) -> bool:
    """Returns true if numbers are equal to an_int."""
    if len(numbers) == 0: 
        return False
    for num in numbers:
        if num != an_int:
            return False
    return True


def max(input: list[int]) -> int:
    """Returns the largest number."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    large: int = input[0]
    for val in input:
        if val > large: 
            large = val
    return large


def is_equal(left: list[int], right: list[int]) -> bool:
    """Return true if left and right are identical."""
    if len(left) != len(right):
        return False
    idx: int = 0
    while idx < len(left):
        if left[idx] != right[idx]:
            return False
        idx += 1
    return True
