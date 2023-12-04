"""practiing writing clases."""

class ChristmasTreeFarm:
    """Creating a christmas tree farm class."""

    plots: list[int]

    def __init__(self, plots: int, initial_plantsings: int) -> None:
        """RAJH."""
        self.plots = []
        while idx < initial_plantsings:
            self.plots.append(1)
            idx += 1
        while idx < plots:
            self.plots.append(0)
            idx += 1
        
    def plant(self, planting: int) -> None:
        """planting."""
        self.plots[planting] == 1

    def growth(self) -> None:
        """Defining growth."""
        idx: int = 0
        while idx < len(self.plots):
            if self.plots[idx] != 0:
                self.plots[idx] += 1
    