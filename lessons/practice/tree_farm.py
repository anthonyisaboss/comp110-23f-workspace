"""Writing a calss for practice."""

from __future__ import annotations

class CrhistmasTreeFarm:
    """Creating a class for christmas trees"""

    plots: list[int]
    
    def __init__(self, plots: int, intitial_plantings: int) -> None:
        """Default docstring."""
        self.plots = []
        idx: int = 0
        while idx < intitial_plantings:
            self.plots.append(1)
            idx += 1
        while idx < plots:
            self.plots.append(0)
            idx += 1
    
    def plant(self, plot: int) -> None:
        """going to plant."""
        self.plots[plot] = 1
    
    def growth(self) -> None:
        """Growth."""
        idx: int = 0
        while self.plots[idx] != 0:
            self.plots[idx] += 1
            idx += 1

    

            
                




            
            