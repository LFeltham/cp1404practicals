"""
Time to complete- programming_language.py & languages.py
Estimated= 40
Actual=
"""


class ProgrammingLanguage:
    """Represent a programming language with specific characteristics."""

    def __init__(self, name, typing_type, supports_reflection, first_appeared_year):
        """Initialize a ProgrammingLanguage instance with its attributes."""
        self.name = name
        self.typing_type = typing_type
        self.supports_reflection = supports_reflection
        self.first_appeared_year = first_appeared_year

    def is_dynamic(self):
        """Return True if the programming language is dynamically typed, otherwise False."""
        return self.typing_type.lower() == "dynamic"

    def __str__(self):
        """Return a string representation of the programming language's details."""
        reflection_text = "True" if self.supports_reflection else "False"
        return (f"{self.name}, {self.typing_type} Typing, Reflection={reflection_text}, "
                f"First appeared in {self.first_appeared_year}")
