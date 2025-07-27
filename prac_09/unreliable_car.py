"""
Unreliable Car class for CP1404 Practical 9
"""

from random import randint
from car import Car


class UnreliableCar(Car):
    """Unreliable car that may not drive based on reliability percentage."""

    def __init__(self, name, fuel, reliability):
        """Initialize unreliable car with name, fuel and reliability."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car if it's reliable enough."""
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven