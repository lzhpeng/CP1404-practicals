"""
Silver Service Taxi class for CP1404 Practical 9
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Silver service taxi with additional flagfall charge."""

    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialize a SilverServiceTaxi with name, fuel and fanciness."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return string representation with flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Calculate fare including flagfall charge."""
        return self.flagfall + super().get_fare()