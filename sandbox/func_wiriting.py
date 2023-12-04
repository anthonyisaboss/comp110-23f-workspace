"""Function writing."""

class Course:
    """UNC COURse."""
    name: str
    level: int
    prerequisites: list[str]

    def is_valid_course(self, prereq: str) -> bool:
        """RAHHHHHH"""
        is_in: bool = False
        idx: int  = 0
        while idx < len(self.prerequisites):
            if self.level >= 400 and self.prerequisites[idx] == prereq:
                is_in = True
            idx += 1
        return is_in