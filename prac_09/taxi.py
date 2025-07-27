"""
Taxi class for CP1404 Practical 9
"""

from car import Car


class Taxi(Car):
    """Taxi class that extends Car with fare calculation functionality."""

    price_per_km = 1.23

    def __init__(self, name, fuel):
        """Initialize taxi with name and fuel."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self):
        """Return string representation of taxi."""
        return f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km"

    def get_fare(self):
        """Calculate and return the fare for current trip."""
        fare = round(self.price_per_km * self.current_fare_distance, 1)
        return fare

    def start_fare(self):
        """Reset current fare distance to 0."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive the taxi and update fare distance."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven