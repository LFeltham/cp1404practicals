"""CP1404/CP5632 Practical - Car class example."""


class Car:
    """Represent a Car Object."""

    def __init__(self, name="Car", fuel=0):
        """Initialise a Car instance"""

        # name: str, the name of the car
        self.name = name
        # fuel: float, one unit of fuel drives one kilometre
        self.fuel = fuel
        self.odometer_reading = 0

    def add_fuel(self, fuel_amount):
        """Add the specified fuel amount to the car's fuel."""
        self.fuel += fuel_amount

    def drive_distance(self, distance_to_drive):
        """Drive the car a given distance,
        drive the specified distance if the car has enough fuel,
        or drive until fuel runs out. returns the distance actually driven"""
        if distance_to_drive > self.fuel:
            distance_to_drive = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance_to_drive
        self.odometer_reading += distance_to_drive
        return distance_to_drive

    def __str__(self):
        """Return a string representation of the car's details."""
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer_reading}"
