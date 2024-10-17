def main():
    choice = ""
    while choice != "Q":
        print_menu()
        choice = input("Enter your choice: ").strip().upper()

        if choice == "C":
            celsius = input("Enter temperature in Celsius: ")
            celsius = float(celsius)
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is {fahrenheit}°F")

        elif choice == "F":
            fahrenheit = input("Enter temperature in Fahrenheit: ")
            fahrenheit = float(fahrenheit)
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is {celsius}°C")
        else:
            print("Invalid input. F, C or Q.")
    print("Farewell!!")


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def print_menu():
    print("Please elect conversion option:")
    print("F. Celsius to Fahrenheit")
    print("C. Fahrenheit to Celsius")
    print("Q. Quit")


main()
