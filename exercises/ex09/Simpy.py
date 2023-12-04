"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730669473"


class Simpy:
    """The most public class."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Going to construct."""
        self.values = values
        
    def __str__(self) -> str:
        """STR METHOD."""
        return f"Simpy({self.values})"
    
    def fill(self, floater: float, inty: int) -> None:
        """I dont know what htis does yet."""
        self.values = []
        idx: int = 0
        while idx < inty:
            self.values.append(floater)
            idx += 1
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Gong to make them run."""
        self.values = []
        assert step != 0.0
        while start < stop:
            self.values.append(start)
            start += step
        while stop < start:
            self.values.append(start)
            start += step
        
    def sum(self) -> float:
        """Going to get the sum of the list."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Going to overide the addition operator."""
        idx: int = 0
        list2: list = []
        while idx < len(self.values):
            if isinstance(rhs, Simpy):
                assert len(self.values) == len(rhs.values)
                list2.append(self.values[idx] + rhs.values[idx])
            else:
                list2.append(self.values[idx] + rhs)
            idx += 1
        return Simpy(list2)
        
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Going to be giving the power of 2 to things."""
        idx: int = 0
        empt: list = []
        while idx < len(self.values):
            if isinstance(rhs, Simpy): 
                assert len(self.values) == len(rhs.values)
                empt.append(self.values[idx] ** rhs.values[idx])
            elif (rhs):
                empt.append(self.values[idx] ** rhs)
            else:
                raise TypeError(f"Operand type is not allowed for **: {type(rhs)}")
            idx += 1
        return Simpy(empt)
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Going to check if equal."""
        is_equal = []
        idx = 0
        while idx < len(self.values):
            if isinstance(rhs, Simpy):
                if self.values[idx] == rhs.values[idx]:
                    is_equal.append(True)
                else: 
                    is_equal.append(False)
            else:
                if self.values[idx] == rhs:
                    is_equal.append(True)
                else:
                    is_equal.append(False)
            idx += 1
        return is_equal
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Checking if greater than."""
        is_equal: list[bool] = []
        idx: int = 0
        while idx < len(self.values):
            if isinstance(rhs, Simpy):
                if self.values[idx] > rhs.values[idx]:
                    is_equal.append(True)
                else: 
                    is_equal.append(False)
            else:
                if self.values[idx] > rhs:
                    is_equal.append(True)
                else:
                    is_equal.append(False)
            idx += 1
        return is_equal
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """So hard for what."""
        list1: list[bool] = []
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            assert len(self.values) == len(rhs)
            for elem in range(len(self.values)):
                if rhs[elem]:
                    list1.append(self.values[elem])
            return Simpy(list1)