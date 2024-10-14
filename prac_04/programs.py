# # 1. Error Checking
def main():
    worker_level = int(input("Worker level: "))

    while worker_level < 1 or worker_level > 10:
        print("Invalid worker level")
        worker_level = int(input("Worker level: "))

    salary = calculate_salary(worker_level)
    print(f"With worker level {worker_level}, your salary is ${salary:,.2f}")


def calculate_salary(worker_level):
    return worker_level * 5000


main()

# 2a. Number Sequences
starting_number = 1
ending_number = 100

for odd_number in range(starting_number, ending_number + 1, 2):
    print(odd_number)

# 2b.
starting_year = 1896
current_year = 2024

for olympic_year in range(starting_year, current_year + 1, 4):
    print(olympic_year, end=" ")

# 2c.
# This loop counts down from 100 to 1 in decrements of 5 printing each number on the same line
for number in range(100, 0, -5):
    print(number, end=" ")

# 3. Menus
"""
display menu
get choice
while choice != <quit option>
    if choice == <first option>
        <do first task>
    else if choice == <second option>
        <do second task>
    ...
    else if choice == <n-th option>
        <do n-th task>
    else
        display invalid input error message
    display menu
    get choice
<do final thing, if needed>
"""


def main():
    display_menu()
    user_choice = input("Enter your choice: ").lower()

    while user_choice != 'q':
        if user_choice == 's':
            print(":)")
        elif user_choice == 'f':
            print(":(")
        else:
            print("Invalid choice")

        display_menu()
        user_choice = input("Enter your choice: ").lower()

    print("Farewell")


def display_menu():
    print("(S)miley")
    print("(F)rowny")
    print("(Q)uit")


main()

# 4a. Accumulation- Sentinel
SENTINEL_VALUE = -1
total_age = 0
count_of_ages = 0

age = int(input("Enter an age (or -1 to quit): "))

while age != SENTINEL_VALUE:
    total_age += age
    count_of_ages += 1
    age = int(input("Enter an age (or -1 to finish): "))

if count_of_ages > 0:
    average_age = total_age / count_of_ages
    print(f"The average age is: {average_age:.2f}")
else:
    print("No ages were entered.")


# 4b. Accumulation- Ask-the-user-to-quit
count_of_smiles = 0
count_of_frowns = 0
is_finished = False

while not is_finished:
    choice = input("Enter 's' for smiley, 'f' for frowny, or 'q' to quit: ").strip().lower()

    if choice == 'q':
        is_finished = True
    elif choice == 's':
        print(":)")
        count_of_smiles += 1
    elif choice == 'f':
        print(":(")
        count_of_frowns += 1
    else:
        print("Invalid choice")

print(f"You printed {count_of_smiles} smiley(s) and {count_of_frowns} frowny(s).")

# 4c. Accumulation- Definite Count
total_sum = 0
count_of_numbers = int(input("How many numbers do you want to add up? "))

for i in range(count_of_numbers):
    value = float(input(f"Enter number {i + 1}: "))
    total_sum += value

print(f"The total of those {count_of_numbers} numbers is {total_sum}.")

# 5. Guessing Game
SECRET_NUMBER = 6
guess_count = 0

guess = int(input("Guess a number: "))
while guess != SECRET_NUMBER:
    guess_count += 1
    if guess < SECRET_NUMBER:
        print("Higher")
    else:
        print("Lower")
    guess = int(input("Guess a number: "))

guess_count += 1
print(f"You got it in {guess_count} guesses!")

# 6. Nested Loops
number_of_rows = int(input("Rows: "))
number_of_columns = int(input("Columns: "))

for row in range(number_of_rows):
    for column in range(number_of_columns):
        print(column, end=" ")
    print()
