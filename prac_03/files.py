# 1.
name_file = open("names.txt", "w")
user_name = input('Enter your name: ')
print(user_name, file=name_file)
name_file.close()

# 2.
name_file = open("names.txt", "r")
name = name_file.read().strip()
name_file.close()
print(f"Hi {name}!")

# 3.
with open("numbers.txt", "r") as numbers_file:
    number1 = int(numbers_file.readline())
    number2 = int(numbers_file.readline())
print(number1 + number2)

# 4.
total = 0
with open("numbers.txt", "r") as numbers_file:
    for line in numbers_file:
        number = int(line)
        total += number
    print(total)
print()
