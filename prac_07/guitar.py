CURRENT_YEAR = 2017
VINTAGE_AGE = 50


class Guitar:
    """Represents a guitar with name, year and cost"""

    def __init__(self, name="", year=0, cost=0):
        """Initialize guitar with name, year and cost"""
        self.name = name
        self.year = year
        self.cost = cost

