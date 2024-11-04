"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""


from car import Car


def main():
    """Demonstrate how to use the Car class."""
    user_car = Car("Leah's Car",  180)
    user_car.drive_distance(30)
    print(f"{user_car.name} has fuel remaining: {user_car.fuel}")
    print(user_car)

    # Create a new Car object "limo" with 100 units of fuel
    limo = Car("Leah's Limo", 100)
    # Add 20 units of fuel to limo
    limo.add_fuel(20)
    # Print the amount of fuel in limo
    print(f"{limo.name} has fuel: {limo.fuel}")
    # Attempt to drive 115 km
    limo.drive_distance(115)
    # Print the limo object to display __str__ method output
    print(limo)


main()
