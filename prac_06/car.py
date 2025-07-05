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

    def add_fuel(self, amount):
        """
        Add fuel to the car.
        """
        self.fuel += amount

    def drive(self, distance):
        """
        Drive the car and update fuel and odometer.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance