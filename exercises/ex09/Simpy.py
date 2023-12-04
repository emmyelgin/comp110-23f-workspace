"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730464992"


class Simpy:
    """A mathematical simulation class for numerical data."""
    values: list[float]

    # TODO: Your constructor and methods will go here.

    def __init__(self, values: list[float]):
        """List of floating point values representing the simulation data."""
        self.values = values

    def __repr__(self) -> str:
        """Returns a string expressing Simpy with attribute values."""
        return f'Simpy({self.values})'

    def __str__(self) -> str:
        """Initializes the Simpy object with a list of floating point values.."""
        return f"Simpy({str(self.values)})"

    def fill(self, fill_value: float, num_values: int) -> None:
        """Fills values with specified values."""
        i: int = 0
        if len(self.values) != num_values:
            self.values = []
        while i < num_values:
            self.values.append(fill_value)
            i += 1
    
    def arange(self, start: float, stop: float = None, step: float = 1.0) -> None: 
        """Generates a sequence of values from start to stop."""
        assert step != 0.0
        self.values.append(start)
        i: float = start
        if start < stop:
            while i < stop - step:
                i += step
                self.values.append(i)
        else:
            while i > stop - step: 
                i += step
                self.values.append(i)
    
    def sum(self) -> float:
        """Use sum method."""
        Sum = sum(self.values)
        return Sum
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add another Simpy object."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value + rhs)
        else:
            assert len(self.values) == len(rhs.value)
            for idx in range(len(self.values)):
                result.values.append(self.values[idx] + rhs.values[idx])
        return result
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Produces expontiation."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value ** rhs)
        else:
            assert isinstance(rhs, Simpy)
            assert len(self.values) == len(rhs.values)
            for idx in range(len(self.values)):
                result.values.append(self.values[idx] ** rhs.values[idx])
        return result
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Use operator overload to create a mask and compare values."""
        result: list[bool] = []
        chance: bool = False
        if isinstance(rhs, float):
            for value in self.values:
                if value == rhs:
                    chance = True
                else:
                    chance = False
                result.append(chance) 
        else:
            assert len(self.values) == len(rhs.values)
            for idx in range(len(self.values)):
                if self.values[idx] == rhs.values[idx]:
                    chance = True
                else:
                    chance = False
                result.append(chance)
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Use operator to test if values are greater through overloading."""
        result: list[bool] = []
        greater: bool = False
        if isinstance(rhs, float):
            for value in self.values:
                if value > rhs:
                    greater = True
                else:
                    greater = False
                result.append(greater)
        else:
            assert len(self.values) == len(rhs.values)
            for idx in range(len(self.values)):
                if self.values[idx] > rhs.values[idx]:
                    greater = True
                else:
                    greater = False
                result.append(greater)
        return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Use operator to specify array values."""
        if isinstance(rhs, int):
            result: float = self.values[rhs]
        else:
            assert len(self.values) == len(rhs)
            result: Simpy = Simpy([])
            for i in range(len(rhs)):
                if rhs[i] is True:
                    result.values.append(self.values[i])
        return result