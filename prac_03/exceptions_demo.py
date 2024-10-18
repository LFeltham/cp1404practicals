"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? ValueError will occur if the user inputs a non-integer value.
2. When will a ZeroDivisionError occur? If the user inputs a 0 for the denominator, as can not be divided
3. Could you change the code to avoid the possibility of a ZeroDivisionError? Other than using try/except to catch
the exception you could change the output to state to the user not to input 0, additionally can LBYL and use an
if else statement to stop the possibility of a ZeroDivisionError.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator (cannot be 0): "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
