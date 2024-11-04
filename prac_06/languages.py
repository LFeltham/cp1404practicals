"""client code to test the ProgrammingLanguage class."""
from programming_language import ProgrammingLanguage


def main():
    """Test the ProgrammingLanguage class functionality."""
    # Create instances of ProgrammingLanguage
    python_language = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby_language = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic_language = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Test the __str__ method by printing each instance
    print(python_language)
    print(ruby_language)
    print(visual_basic_language)

    # Store the language objects in a list
    programming_languages = [python_language, ruby_language, visual_basic_language]
    # Print dynamically typed languages
    print("\nThe dynamically typed languages are:")
    for language in programming_languages:
        if language.is_dynamic():
            print(language.name)


main()
