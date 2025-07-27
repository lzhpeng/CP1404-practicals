"""
Car class for CP1404 Practical 9
Represents a basic car with fuel and odometer tracking.
"""


class Car:
    """Represent a Car object with fuel and odometer tracking."""

    def __init__(self, name="", fuel=0):
        """Initialize a Car instance.

        Args:
            name: string, reference name for car
            fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.fuel = fuel
        self.odometer = 0
