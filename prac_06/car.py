class Car:
    def __init__(self, name="", fuel=0):
        """
        Set up a new car with name and fuel.
        """
        self.name = name
        self.fuel = fuel
        self._odometer = 0

    def __str__(self):
        """
        Return car details as a string.
        """
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"