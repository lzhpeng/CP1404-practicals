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

    def __str__(self):
        """Return a string representation of a Car object."""
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance