"""Time taken to complete - Guitar program.
Estimated= 50 mins
Actual= 29 mins
"""
from datetime import datetime


class Guitar:
    """Represent a Guitar object with name, year, and cost attributes."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance with name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a formatted string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Calculate and return the age of the guitar based on the current year."""
        current_year = datetime.now().year
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is vintage (50 or more years old), else False."""
        return self.get_age() >= 50
