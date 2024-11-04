from guitar import Guitar


def run_tests():
    """Run tests on Guitar class methods get_age and is_vintage."""
    # Set up test cases
    gibson_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 1512.9)

    print(f"{gibson_guitar.name} get_age() - Expected {95}. Got {gibson_guitar.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected {5}. Got {another_guitar.get_age()}")
    print()
    print(f"{gibson_guitar.name} is_vintage() - Expected {True}. Got {gibson_guitar.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected {False}. Got {another_guitar.is_vintage()}")


run_tests()
