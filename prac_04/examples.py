# Initial Program
birth_month = int(input("Enter your birth month: "))
while birth_month < 1 or birth_month > 12:
    print("Invalid month")
    birth_month = int(input("Enter your birth month: "))

for count in range(1, birth_month + 1):
    print(count, end=" ")
print()

# Updated program
MINIMUM_MONTH = 1
MAXIMUM_MONTH = 10

birth_month = int(input(f"Enter the month number ({MINIMUM_MONTH}-{MAXIMUM_MONTH}): "))
while birth_month < MINIMUM_MONTH or birth_month > MAXIMUM_MONTH:
    print("Invalid month")
    birth_month = int(input(f"Enter the month number ({MINIMUM_MONTH}-{MAXIMUM_MONTH}): "))

if birth_month <= MAXIMUM_MONTH / 2:
    print("This birth month is in the first half of the year.")
else:
    print("The birth month is in the second half of the year.")

for count in range(1, birth_month + 1):
    print(count, end=" ")
print()
