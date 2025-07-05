class Car:
    def __init__(self, name="", fuel=0):
        """
        Set up a new car with name and fuel.
        """
        self.name = name
        self.fuel = fuel
        self._odometer = 0
