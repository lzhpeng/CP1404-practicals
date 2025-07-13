CURRENT_YEAR = 2017
VINTAGE_AGE = 50


class Guitar:

    """Represents a guitar with name, year and cost"""

    def __init__(self, name="", year=0, cost=0):
        """Initialize guitar with name, year and cost"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return formatted string representation"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Calculate guitar age in years"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Check if guitar is vintage (50+ years old)"""
        return self.get_age() >= VINTAGE_AGE


# Test code
guitar1 = Guitar("Fender Stratocaster", 1965, 1500)
guitar2 = Guitar("Gibson Les Paul", 1959, 2500)
guitar3 = Guitar("Martin D-28", 1972, 1800)
guitars = [guitar1, guitar2, guitar3]
sorted_guitars = sorted(guitars, key=lambda x: x.year)
for guitar in sorted_guitars:
    print(guitar)